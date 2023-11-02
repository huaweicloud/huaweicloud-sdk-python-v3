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

import ecdsa
import six

from huaweicloudsdkcore.exceptions.exceptions import SdkException
from huaweicloudsdkcore.sdk_request import SdkRequest
from huaweicloudsdkcore.signer import hkdf
from huaweicloudsdkcore.signer.gm import new_sm3_hash, CURVE_SM2, SM2SigningKey

if six.PY3:
    from urllib.parse import quote, unquote
else:
    from urllib import quote, unquote


class Signer(object):
    _ENCODE_UTF8 = "utf-8"
    _ENCODE_ISO_8859_1 = "iso-8859-1"
    _BASIC_DATE_FORMAT = "%Y%m%dT%H%M%SZ"
    _ALGORITHM = "SDK-HMAC-SHA256"
    _HEADER_X_DATE = "X-Sdk-Date"
    _HEADER_HOST = "Host"
    _HEADER_AUTHORIZATION = "Authorization"
    _HEADER_CONTENT = "X-Sdk-Content-Sha256"
    _EMPTY_HASH = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

    def __init__(self, credentials):
        self._ak = credentials.ak
        self._sk = credentials.sk
        self._hash_func = hashlib.sha256

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

        self._process_content_header(request)
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
    def _process_content_header(cls, request):
        # type: (SdkRequest) -> None
        content_type = request.header_params.get("Content-Type")
        if content_type and not content_type.startswith("application/json"):
            request.header_params[cls._HEADER_CONTENT] = "UNSIGNED-PAYLOAD"

    @classmethod
    def process_request_uri(cls, request):
        # type: (SdkRequest) -> None
        canonical_query_string = cls._process_canonical_query_string(request)
        request.uri = "%s?%s" % (request.resource_path, canonical_query_string) \
            if canonical_query_string != "" else request.resource_path

    @classmethod
    def _process_header_time(cls, request):
        # type: (SdkRequest) -> datetime
        header_time = cls._get_header_ignore_case(request, cls._HEADER_X_DATE)
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

    def _hash_hex_string(self, data):
        # type: (bytes) -> str
        _hash = self._hash_func(data)
        return _hash.hexdigest()

    def _hmac(self, key, data):
        # type: (bytes, bytes) -> bytes
        return hmac.new(key, data, digestmod=self._hash_func).digest()

    def _process_string_to_sign(self, canonical_request, time):
        # type: (str, datetime) -> str
        return "%s\n%s\n%s" % (
            self._ALGORITHM,
            datetime.strftime(time, self._BASIC_DATE_FORMAT),
            self._hash_hex_string(six.ensure_binary(canonical_request))
        )

    @classmethod
    def _url_encode(cls, s):
        # type: (str) -> str
        return quote(s, safe='~')

    @classmethod
    def _get_header_ignore_case(cls, r, header):
        # type: (SdkRequest, str) -> str|None
        for k in r.header_params:
            if k.lower() == header.lower():
                return r.header_params[k]
        return None

    def _process_canonical_request(self, request, signed_headers):
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
        canonical_headers = self._process_canonical_headers(request, signed_headers)

        hex_encode = self._process_hash_payload(request)
        canonical_uri = self._process_canonical_uri(request)
        canonical_query_string = self._process_canonical_query_string(request)
        return "%s\n%s\n%s\n%s\n%s\n%s" % (request.method.upper(), canonical_uri, canonical_query_string,
                                           canonical_headers, ";".join(signed_headers), hex_encode)

    def _process_hash_payload(self, request):
        # type: (SdkRequest) -> str
        if not request.body:
            return self._EMPTY_HASH

        hex_encode = self._get_header_ignore_case(request, self._HEADER_CONTENT)
        if hex_encode:
            return hex_encode

        return self._hash_hex_string(request.body)

    def _process_canonical_uri(self, request):
        # type: (SdkRequest) -> str
        pattens = unquote(request.resource_path).split('/')
        uri = []
        for v in pattens:
            uri.append(self._url_encode(v))
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

    def _process_canonical_headers(self, request, signed_headers):
        # type: (SdkRequest, dict) -> str
        canonical_headers = []
        __headers = {}
        for key in request.header_params:
            key_encoded = key.lower()
            value = request.header_params[key]
            value_encoded = str(value).strip()
            __headers[key_encoded] = value_encoded
            if six.PY3:
                request.header_params[key] = value_encoded.encode(self._ENCODE_UTF8).decode('iso-8859-1')

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

    def _sign_string_to_sign(self, string_to_sign, key):
        # type: (str, str) -> str
        return self._hex(self._hmac(six.ensure_binary(key), six.ensure_binary(string_to_sign)))

    def _process_auth_header_value(self, signature, app_key, signed_headers):
        # type: (str, str, list) -> str
        return "%s Access=%s, SignedHeaders=%s, Signature=%s" % (
            self._ALGORITHM, app_key, ";".join(signed_headers), signature)

    def _hex(self, data):
        if six.PY2:
            return "".join("{:02x}".format(ord(c)) for c in six.ensure_binary(data))
        return data.hex()


class SM3Signer(Signer):
    _ALGORITHM = "SDK-HMAC-SM3"
    _HEADER_CONTENT = "X-Sdk-Content-Sm3"
    _EMPTY_HASH = "1ab21d8355cfa17f8e61194831e81a8f22bec8c728fefb747ed035eb5082aa2b"

    def __init__(self, credentials):
        super(SM3Signer, self).__init__(credentials)
        self._hash_func = new_sm3_hash

    def _verify_required(self):
        super(SM3Signer, self)._verify_required()
        if six.PY2:
            raise SdkException("Signing algorithm %s is not supported in python2" % self._ALGORITHM)


class DerivationAKSKSigner(Signer):
    BasicISODateFormat = "%Y%m%d"
    _ALGORITHM = "V11-HMAC-SHA256"

    def _process_string_to_sign(self, canonical_request, time, info=None):
        # type: (str, datetime, str) -> str
        return "%s\n%s\n%s\n%s" % (
            self._ALGORITHM,
            datetime.strftime(time, self._BASIC_DATE_FORMAT),
            info,
            self._hash_hex_string(six.ensure_binary(canonical_request))
        )

    def _process_auth_header_value(self, signature, app_key, signed_headers, info=None):
        # type: (str, str, list, str) -> str
        return "%s Credential=%s/%s, SignedHeaders=%s, Signature=%s" % (
            self._ALGORITHM, app_key, info, ";".join(signed_headers), signature)

    def sign(self, request, derived_auth_service_name=None, region_id=None):
        # type: (SdkRequest, str, str) -> SdkRequest
        self._verify_required()
        if not derived_auth_service_name:
            raise ValueError("derivedAuthServiceName is required in credentials when using derived auth")
        if not region_id:
            raise ValueError("regionId is required in credentials when using derived auth")

        if isinstance(request.body, six.text_type):
            request.body = six.ensure_binary(request.body)

        self._process_content_header(request)
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


class P256SHA256Signer(Signer):
    _ALGORITHM = "SDK-ECDSA-P256-SHA256"
    _CURVE = ecdsa.NIST256p
    _N_MINUS_TWO = _CURVE.order - 2

    def _verify_required(self):
        super(P256SHA256Signer, self)._verify_required()
        if six.PY2:
            raise SdkException("Signing algorithm %s is not supported in python2" % self._ALGORITHM)

    def _sign_string_to_sign(self, data, key=None):
        # type: (str, str) -> str
        signing_key = self.get_signing_key()
        sig = signing_key.sign(six.ensure_binary(data), hashfunc=self._hash_func, sigencode=ecdsa.util.sigencode_der)
        return self._hex(sig)

    def _derive_key_bytes(self):
        # type: () -> bytes
        context = bytearray()
        data = bytearray()
        for counter in range(0xff):
            context.clear()
            data.clear()

            context.extend(six.ensure_binary(self._ak))
            context.append(counter)

            data.extend(b'\x00\x00\x00\x01')
            data.extend(six.ensure_binary(self._ALGORITHM))
            data.append(0x00)
            data.extend(context)
            data.extend(b'\x00\x00\x01\x00')

            candidate = int.from_bytes(self._hmac(six.ensure_binary(self._sk), bytes(data)), 'big')
            if candidate <= self._N_MINUS_TWO:
                secret_key = candidate + 1
                return int.to_bytes(secret_key, length=(secret_key.bit_length() + 7) // 8, byteorder='big')

        raise SdkException("derive candidate failed, counter out of range")

    def _generate_signing_key(self, key_bytes):
        return ecdsa.SigningKey.from_string(key_bytes, curve=self._CURVE, hashfunc=self._hash_func)

    def get_signing_key(self):
        key_bytes = self._derive_key_bytes()
        return self._generate_signing_key(key_bytes)


class SM2SM3Signer(P256SHA256Signer):
    _ALGORITHM = "SDK-SM2-SM3"
    _HEADER_CONTENT = "X-Sdk-Content-Sm3"
    _EMPTY_HASH = "1ab21d8355cfa17f8e61194831e81a8f22bec8c728fefb747ed035eb5082aa2b"
    _CURVE = CURVE_SM2
    _N_MINUS_TWO = _CURVE.order - 2

    def __init__(self, credentials):
        super(SM2SM3Signer, self).__init__(credentials)
        self._hash_func = new_sm3_hash

    def _sign_string_to_sign(self, data, key=None):
        # type: (str, str) -> str
        signing_key = self.get_signing_key()
        signature = signing_key.sign(six.ensure_binary(data))
        return self._hex(signature)

    def _generate_signing_key(self, key_bytes):
        return SM2SigningKey(key_bytes)
