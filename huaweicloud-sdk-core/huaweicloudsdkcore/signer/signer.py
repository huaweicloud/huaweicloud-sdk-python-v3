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

import binascii
import hashlib
import hmac
from datetime import datetime

import six

from huaweicloudsdkcore.signer import hkdf

if six.PY2:
    from urllib import quote, unquote
else:
    from urllib.parse import quote, unquote


class Signer(object):
    EncodeUtf8 = "utf-8"
    BasicDateFormat = "%Y%m%dT%H%M%SZ"
    Algorithm = "SDK-HMAC-SHA256"
    HeaderXDate = "X-Sdk-Date"
    HeaderHost = "Host"
    HeaderAuthorization = "Authorization"
    HeaderContentSha256 = "X-Sdk-Content-Sha256"

    def __init__(self, credentials):
        self._ak = credentials.ak
        self._sk = credentials.sk

    def sign(self, request):
        if isinstance(request.body, six.text_type):
            request.body = six.ensure_binary(request.body)

        t = self.process_header_time(request)
        self.process_header_host(request)

        signed_headers = self.process_signed_headers(request)
        canonical_request = self.process_canonical_request(request, signed_headers)
        string_to_sign = self.process_string_to_sign(canonical_request, t)
        signature = self.sign_string_to_sign(string_to_sign, self._sk)
        auth_value = self.process_auth_header_value(signature, self._ak, signed_headers)
        request.header_params[self.HeaderAuthorization] = auth_value

        self.process_request_uri(request)

        return request

    @classmethod
    def process_request_uri(cls, request):
        canonical_query_string = cls.process_canonical_query_string(request)
        request.uri = "%s?%s" % (request.resource_path, canonical_query_string) \
            if canonical_query_string != "" else request.resource_path

    @classmethod
    def process_header_time(cls, request):
        header_time = cls.find_header(request, cls.HeaderXDate)
        if header_time is None:
            t = datetime.utcnow()
            request.header_params[cls.HeaderXDate] = datetime.strftime(t, cls.BasicDateFormat)
        else:
            t = datetime.strptime(header_time, cls.BasicDateFormat)
        return t

    @classmethod
    def process_header_host(cls, request):
        has_host_header = False
        for key in request.header_params:
            if key.lower() == 'host':
                has_host_header = True
                break
        if not has_host_header:
            request.header_params["Host"] = request.host

    @classmethod
    def hmac_sha256(cls, key_byte, message):
        return hmac.new(six.ensure_binary(key_byte), six.ensure_binary(message), digestmod=hashlib.sha256).digest()

    @classmethod
    def process_string_to_sign(cls, canonical_request, time):
        return "%s\n%s\n%s" % (
            cls.Algorithm,
            datetime.strftime(time, cls.BasicDateFormat),
            cls.hex_encode_sha256_hash(six.ensure_binary(canonical_request))
        )

    @classmethod
    def url_encode(cls, s):
        return quote(s, safe='~')

    @classmethod
    def find_header(cls, r, header):
        for k in r.header_params:
            if k.lower() == header.lower():
                return r.header_params[k]
        return None

    @classmethod
    def hex_encode_sha256_hash(cls, data):
        sha256 = hashlib.sha256()
        sha256.update(data)
        return sha256.hexdigest()

    @classmethod
    def process_canonical_request(cls, request, signed_headers):
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
        canonical_headers = cls.process_canonical_headers(request, signed_headers)
        hex_encode = cls.find_header(request, cls.HeaderContentSha256)
        if hex_encode is None:
            hex_encode = cls.hex_encode_sha256_hash(request.body)
        canonical_uri = cls.process_canonical_uri(request)
        canonical_query_string = cls.process_canonical_query_string(request)
        return "%s\n%s\n%s\n%s\n%s\n%s" % (request.method.upper(), canonical_uri, canonical_query_string,
                                           canonical_headers, ";".join(signed_headers), hex_encode)

    @classmethod
    def process_canonical_uri(cls, request):
        pattens = unquote(request.resource_path).split('/')
        uri = []
        for v in pattens:
            uri.append(cls.url_encode(v))
        url_path = "/".join(uri)

        if url_path[-1] != '/':
            url_path = url_path + "/"

        return url_path

    @classmethod
    def process_canonical_query_string(cls, request):
        params = []
        for param in request.query_params:
            params.append(param)
        params.sort()

        canonical_query_param = []
        for (key, value) in params:
            k = cls.url_encode(key)
            if isinstance(value, list):
                value.sort()
                for v in value:
                    kv = "%s=%s" % (k, cls.url_encode(str(v)))
                    canonical_query_param.append(kv)
            elif isinstance(value, bool):
                kv = "%s=%s" % (k, cls.url_encode(str(value).lower()))
                canonical_query_param.append(kv)
            else:
                kv = "%s=%s" % (k, cls.url_encode(str(value)))
                canonical_query_param.append(kv)

        return '&'.join(canonical_query_param)

    @classmethod
    def process_canonical_headers(cls, request, signed_headers):
        canonical_headers = []
        __headers = {}
        for key in request.header_params:
            key_encoded = key.lower()
            value = request.header_params[key]
            value_encoded = str(value).strip()
            __headers[key_encoded] = value_encoded
            if six.PY3:
                request.header_params[key] = value_encoded.encode(cls.EncodeUtf8).decode('iso-8859-1')

        for key in signed_headers:
            canonical_headers.append(key + ":" + __headers.get(key))

        return '\n'.join(canonical_headers) + "\n"

    @classmethod
    def process_signed_headers(cls, request):
        signed_headers = []
        for key in request.header_params:
            signed_headers.append(key.lower())
        signed_headers.sort()
        return signed_headers

    @classmethod
    def sign_string_to_sign(cls, string_to_sign, key):
        hm = cls.hmac_sha256(key, string_to_sign)
        return binascii.hexlify(hm).decode()

    @classmethod
    def process_auth_header_value(cls, signature, app_key, signed_headers):
        return "%s Access=%s, SignedHeaders=%s, Signature=%s" % (
            cls.Algorithm, app_key, ";".join(signed_headers), signature)


class DerivationAKSKSigner(Signer):
    BasicISODateFormat = "%Y%m%d"
    Algorithm = "V11-HMAC-SHA256"

    @classmethod
    def process_string_to_sign(cls, canonical_request, time, info=None):
        return "%s\n%s\n%s\n%s" % (
            cls.Algorithm,
            datetime.strftime(time, cls.BasicDateFormat),
            info,
            cls.hex_encode_sha256_hash(six.ensure_binary(canonical_request))
        )

    @classmethod
    def process_auth_header_value(cls, signature, app_key, signed_headers, info=None):
        return "%s Credential=%s/%s, SignedHeaders=%s, Signature=%s" % (
            cls.Algorithm, app_key, info, ";".join(signed_headers), signature)

    def sign(self, request, derived_auth_service_name=None, region_id=None):
        request.body = six.ensure_binary(request.body)

        t = self.process_header_time(request)
        self.process_header_host(request)

        signed_headers = self.process_signed_headers(request)
        canonical_request = self.process_canonical_request(request, signed_headers)
        date_str = datetime.strftime(datetime.utcnow(), self.BasicISODateFormat)
        info_str = "%s/%s/%s" % (date_str, region_id, derived_auth_service_name)
        string_to_sign = self.process_string_to_sign(canonical_request, t, info_str)
        derivation_key = hkdf.get_der_key_sha256(access_key=self._ak, secret_key=self._sk, info=info_str)
        signature = self.sign_string_to_sign(string_to_sign, derivation_key)
        auth_value = self.process_auth_header_value(signature, self._ak, signed_headers, info_str)
        request.header_params[self.HeaderAuthorization] = auth_value

        self.process_request_uri(request)

        return request

