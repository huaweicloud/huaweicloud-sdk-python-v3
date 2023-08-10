# coding: utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""

import hashlib
import hmac
from datetime import datetime

import six

from huaweicloudsdkcore.exceptions.exceptions import SdkException
from huaweicloudsdkcore.sdk_request import SdkRequest
from huaweicloudsdkcore.signer import hkdf
from huaweicloudsdkcore.signer.sm3 import new_sm3_hash

if six.PY2:
    from urllib import quote, unquote
else:
    from urllib.parse import quote, unquote


class Signer(object):
    _ENCODE_UTF8 = "utf-8"
    _ENCODE_ISO_8859_1 = "iso-8859-1"
    _BASIC_DATE_FORMAT = "%Y%m%dT%H%M%SZ"
    _ALGORITHM = "SDK-HMAC-SHA256"
    _HEADER_X_DATE = "X-Sdk-Date"
    _HEADER_HOST = "Host"
    _HEADER_AUTHORIZATION = "Authorization"
    _HEADER_CONTENT_SHA256 = "X-Sdk-Content-Sha256"

    def __init__(self, credentials):
        self._ak = credentials.ak
        self._sk = credentials.sk

    def _verify_required(self):
        if not self._ak:
            raise ValueError("ak is required in credentials")
        if not self._sk:
            raise ValueError("sk is required in credentials")

    def sign(self, request):
        # type: (SdkRequest) -> SdkRequest
        self._verify_required()
        if isinstance(request.body, six.text_type):
            request.body = six.ensure_binary(request.body)

        t = self._process_header_time(request)
        self._process_header_host(request)

        signed_headers = self._process_signed_headers(request)
        canonical_request = self._process_canonical_request(request, signed_headers)
        string_to_sign = self._process_string_to_sign(canonical_request, t)
        signature = self._sign_string_to_sign(string_to_sign, self._sk)
        auth_value = self._process_auth_header_value(signature, self._ak, signed_headers)
        request.header_params[self._HEADER_AUTHORIZATION] = auth_value

        self.process_request_uri(request)

        return request

    @classmethod
    def process_request_uri(cls, request):
        # type: (SdkRequest) -> None
        canonical_query_string = cls._process_canonical_query_string(request)
        request.uri = "%s?%s" % (request.resource_path, canonical_query_string) \
            if canonical_query_string != "" else request.resource_path

    @classmethod
    def _process_header_time(cls, request):
        # type: (SdkRequest) -> datetime
        header_time = cls._find_header(request, cls._HEADER_X_DATE)
        if header_time is None:
            t = datetime.utcnow()
            request.header_params[cls._HEADER_X_DATE] = datetime.strftime(t, cls._BASIC_DATE_FORMAT)
        else:
            t = datetime.strptime(header_time, cls._BASIC_DATE_FORMAT)
        return t

    @classmethod
    def _process_header_host(cls, request):
        # type: (SdkRequest) -> None
        has_host_header = False
        for key in request.header_params:
            if key.lower() == 'host':
                has_host_header = True
                break
        if not has_host_header:
            request.header_params["Host"] = request.host

    @classmethod
    def _hash_hex_string(cls, data):
        # type: (bytes) -> str
        sha256 = hashlib.sha256(data)
        return sha256.hexdigest()

    @classmethod
    def _hmac(cls, key_byte, message):
        # type: (bytes|str, bytes|str) -> str
        return hmac.new(six.ensure_binary(key_byte), six.ensure_binary(message), digestmod=hashlib.sha256).hexdigest()

    @classmethod
    def _process_string_to_sign(cls, canonical_request, time):
        # type: (str, datetime) -> str
        return "%s\n%s\n%s" % (
            cls._ALGORITHM,
            datetime.strftime(time, cls._BASIC_DATE_FORMAT),
            cls._hash_hex_string(six.ensure_binary(canonical_request))
        )

    @classmethod
    def _url_encode(cls, s):
        # type: (str) -> str
        return quote(s, safe='~')

    @classmethod
    def _find_header(cls, r, header):
        # type: (SdkRequest, str) -> str
        for k in r.header_params:
            if k.lower() == header.lower():
                return r.header_params[k]
        return None

    @classmethod
    def _process_canonical_request(cls, request, signed_headers):
        # type: (SdkRequest, dict) -> str
        """
        Build a CanonicalRequest from a regular request string

        CanonicalRequest consists of several parts:
          Part 1. HTTPRequestMethod
          Part 2. CanonicalURI
          Part 3. CanonicalQueryString
          Part 4. CanonicalHeaders
          Part 5 SignedHeaders
          Part 6 HexEncode(Hash(RequestPayload))
        """
        canonical_headers = cls._process_canonical_headers(request, signed_headers)
        hex_encode = cls._find_header(request, cls._HEADER_CONTENT_SHA256)
        if hex_encode is None:
            hex_encode = cls._hash_hex_string(request.body)
        canonical_uri = cls._process_canonical_uri(request)
        canonical_query_string = cls._process_canonical_query_string(request)
        return "%s\n%s\n%s\n%s\n%s\n%s" % (request.method.upper(), canonical_uri, canonical_query_string,
                                           canonical_headers, ";".join(signed_headers), hex_encode)

    @classmethod
    def _process_canonical_uri(cls, request):
        # type: (SdkRequest) -> str
        pattens = unquote(request.resource_path).split('/')
        uri = []
        for v in pattens:
            uri.append(cls._url_encode(v))
        url_path = "/".join(uri)

        if url_path[-1] != '/':
            url_path = url_path + "/"

        return url_path

    @classmethod
    def _process_canonical_query_string(cls, request):
        # type: (SdkRequest) -> str
        params = []
        for param in request.query_params:
            params.append(param)
        params.sort()

        canonical_query_param = []
        for (key, value) in params:
            k = cls._url_encode(key)
            if isinstance(value, list):
                value.sort()
                for v in value:
                    kv = "%s=%s" % (k, cls._url_encode(str(v)))
                    canonical_query_param.append(kv)
            elif isinstance(value, bool):
                kv = "%s=%s" % (k, cls._url_encode(str(value).lower()))
                canonical_query_param.append(kv)
            else:
                kv = "%s=%s" % (k, cls._url_encode(str(value)))
                canonical_query_param.append(kv)

        return '&'.join(canonical_query_param)

    @classmethod
    def _process_canonical_headers(cls, request, signed_headers):
        # type: (SdkRequest, dict) -> str
        canonical_headers = []
        __headers = {}
        for key in request.header_params:
            key_encoded = key.lower()
            value = request.header_params[key]
            value_encoded = str(value).strip()
            __headers[key_encoded] = value_encoded
            if six.PY3:
                request.header_params[key] = value_encoded.encode(cls._ENCODE_UTF8).decode('iso-8859-1')

        for key in signed_headers:
            canonical_headers.append(key + ":" + __headers.get(key))

        return '\n'.join(canonical_headers) + "\n"

    @classmethod
    def _process_signed_headers(cls, request):
        # type: (SdkRequest) -> list
        signed_headers = []
        for key in request.header_params:
            signed_headers.append(key.lower())
        signed_headers.sort()
        return signed_headers

    @classmethod
    def _sign_string_to_sign(cls, string_to_sign, key):
        # type: (str, str) -> str
        return cls._hmac(key, string_to_sign)

    @classmethod
    def _process_auth_header_value(cls, signature, app_key, signed_headers):
        # type: (str, str, list) -> str
        return "%s Access=%s, SignedHeaders=%s, Signature=%s" % (
            cls._ALGORITHM, app_key, ";".join(signed_headers), signature)


class SM3Signer(Signer):
    _ALGORITHM = "SDK-HMAC-SM3"

    def _verify_required(self):
        super(SM3Signer, self)._verify_required()
        if six.PY2:
            raise SdkException("Signing algorithm SM3 is not supported in python2")

    @classmethod
    def _hash_hex_string(cls, data):
        # type: (bytes) -> str
        sm3 = new_sm3_hash(data)
        return sm3.hexdigest()

    @classmethod
    def _hmac(cls, key_byte, message):
        # type: (bytes|str, bytes|str) -> str
        return hmac.new(six.ensure_binary(key_byte), six.ensure_binary(message), digestmod=new_sm3_hash).hexdigest()


class DerivationAKSKSigner(Signer):
    BasicISODateFormat = "%Y%m%d"
    _ALGORITHM = "V11-HMAC-SHA256"

    @classmethod
    def _process_string_to_sign(cls, canonical_request, time, info=None):
        # type: (str, datetime, str) -> str
        return "%s\n%s\n%s\n%s" % (
            cls._ALGORITHM,
            datetime.strftime(time, cls._BASIC_DATE_FORMAT),
            info,
            cls._hash_hex_string(six.ensure_binary(canonical_request))
        )

    @classmethod
    def _process_auth_header_value(cls, signature, app_key, signed_headers, info=None):
        # type: (str, str, list, str) -> str
        return "%s Credential=%s/%s, SignedHeaders=%s, Signature=%s" % (
            cls._ALGORITHM, app_key, info, ";".join(signed_headers), signature)

    def sign(self, request, derived_auth_service_name=None, region_id=None):
        # type: (SdkRequest, str, str) -> SdkRequest
        self._verify_required()
        if not derived_auth_service_name:
            raise ValueError("derivedAuthServiceName is required in credentials when using derived auth")
        if not region_id:
            raise ValueError("regionId is required in credentials when using derived auth")

        request.body = six.ensure_binary(request.body)

        t = self._process_header_time(request)
        self._process_header_host(request)

        signed_headers = self._process_signed_headers(request)
        canonical_request = self._process_canonical_request(request, signed_headers)
        date_str = datetime.strftime(t, self.BasicISODateFormat)
        info_str = "%s/%s/%s" % (date_str, region_id, derived_auth_service_name)
        string_to_sign = self._process_string_to_sign(canonical_request, t, info_str)
        derivation_key = hkdf.get_der_key_sha256(access_key=self._ak, secret_key=self._sk, info=info_str)
        signature = self._sign_string_to_sign(string_to_sign, derivation_key)
        auth_value = self._process_auth_header_value(signature, self._ak, signed_headers, info_str)
        request.header_params[self._HEADER_AUTHORIZATION] = auth_value

        self.process_request_uri(request)

        return request
