# coding: utf-8
"""
 Copyright 2023 Huawei Technologies Co.,Ltd.

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
import six
import binascii
from huaweicloudsdkcore.sdk_request import SdkRequest
if six.PY3:
    from urllib.parse import quote
else:
    from urllib import quote

_OBS_HEADER_PREFIX = 'x-obs-'
_AUTHORIZATION_HEADER = 'Authorization'
_OBS_META_HEADER_PREFIX = 'x-obs-meta-'
_CANONICAL_STRING = 'CanonicalString'

_CONTENT_TYPE_HEADER = 'Content-Type'
_CONTENT_MD5_HEADER = 'Content-MD5'
_X_OBS_SECURITY_TOKEN = "x-obs-security-token"
_DATE_HEADER = 'Date'

_FILE = "file"

_CONTENT_LIST = [_CONTENT_TYPE_HEADER.lower(), _CONTENT_MD5_HEADER.lower(), _DATE_HEADER.lower()]

_ALLOWED_RESOURCE_PARAMTER_NAMES = (
    'acl',
    'backtosource',
    'policy',
    'torrent',
    'logging',
    'location',
    'storageinfo',
    'quota',
    'storageclass',
    'storagepolicy',
    'requestpayment',
    'versions',
    'versioning',
    'versionid',
    'uploads',
    'uploadid',
    'partnumber',
    'website',
    'notification',
    'lifecycle',
    'deletebucket',
    'delete',
    'cors',
    'restore',
    'tagging',
    'replication',
    'metadata',
    'encryption',

    # File System API
    'append',
    'position',
    'truncate',
    'modify',
    'rename',
    'length',
    'name',
    'fileinterface',

    'response-content-type',
    'response-content-language',
    'response-expires',
    'response-cache-control',
    'response-content-disposition',
    'response-content-encoding',
    'x-image-save-bucket',
    'x-image-save-object',
    'x-image-process',
    'x-oss-process',

    # workflow api
    'x-workflow-prefix',
    'x-workflow-start',
    'x-workflow-limit',
    'x-workflow-template-name',
    'x-workflow-graph-name',
    'x-workflow-execution-state',
    'x-workflow-execution-type',
    'x-workflow-next-marker',
    'obsworkflowtriggerpolicy',

    # virtual bucket api
    'obsbucketalias',
    'obsalias'
)
_IS_PYTHON2 = six.PY2


class OBSSigner(object):

    def __init__(self, credentials):
        self._ak = credentials.ak
        self._sk = credentials.sk

    @classmethod
    def auth_prefix(self):
        return 'OBS'

    @classmethod
    def _get_header_prefix(self):
        return _OBS_HEADER_PREFIX

    @classmethod
    def date_header(self):
        return self._get_header_prefix() + 'date'

    @classmethod
    def _get_meta_header_prefix(self):
        return _OBS_META_HEADER_PREFIX

    @classmethod
    def to_string(self, item):
        try:
            return str(item) if item is not None else ''
        except Exception:
            return ''

    @classmethod
    def encode_object_key(self, key):
        return self.encode_item(key, '/~')

    @classmethod
    def encode_item(self, item, safe='/'):
        return quote(self.to_string(item), safe)

    @classmethod
    def doAuth(self, credentials, method, bucket, key, path_args, headers, expires=None):
        if credentials.security_token is not None:
            headers[_X_OBS_SECURITY_TOKEN] = credentials.security_token
        ret = self.getSignature(credentials, method, bucket, key, path_args, headers, expires)
        return {
            _AUTHORIZATION_HEADER: '%s %s:%s' % (self.auth_prefix(), credentials.ak, ret['Signature']),
            _CANONICAL_STRING: ret[_CANONICAL_STRING]
        }

    @classmethod
    def getSignature(self, credentials, method, bucket, key, path_args, headers, expires=None):
        canonical_string = self.__make_canonical_string(method, bucket, key, path_args, headers, expires)
        return {
            'Signature': self.hmacSha128(credentials, canonical_string),
            _CANONICAL_STRING: canonical_string
        }

    @classmethod
    def hmacSha128(self, credentials, canonical_string):
        if _IS_PYTHON2:
            hashed = hmac.new(credentials.sk, canonical_string, hashlib.sha1)
            encode_canonical = binascii.b2a_base64(hashed.digest())[:-1]
        else:
            hashed = hmac.new(credentials.sk.encode('UTF-8'), canonical_string.encode('UTF-8'), hashlib.sha1)
            encode_canonical = binascii.b2a_base64(hashed.digest())[:-1].decode('UTF-8')

        return encode_canonical

    @classmethod
    def __make_canonical_string(self, method, bucket_name, key, path_args, headers, expires=None):
        interesting_headers = self.__make_canonicalstring_interesting_headers(headers, expires)
        key_list = sorted(interesting_headers.keys())
        str_list = self.__make_canonicalstring_str_list(key_list, method, interesting_headers)
        URI = ''
        _bucket_name = bucket_name
        if _bucket_name:
            URI += '/'
            URI += _bucket_name
            URI += '/'

        if key:
            if not URI.endswith('/'):
                URI += '/'
            URI += key

        if URI:
            str_list.append(URI)
        else:
            str_list.append('/')

        if path_args:
            e = '?'
            cannoList = sorted(path_args, key=lambda d: d[0])
            for path_key, path_value in cannoList:
                if path_key.lower() in _ALLOWED_RESOURCE_PARAMTER_NAMES or path_key.lower().startswith(
                        self._get_header_prefix()):
                    path_key = self.encode_item(path_key, '/')
                    if path_value == ' ' or not path_value:
                        e += path_key + '&'
                        continue
                    e += path_key + '=' + self.to_string(path_value) + '&'

            e = e[:-1]
            str_list.append(e)
        return ''.join(str_list)

    @classmethod
    def __make_canonicalstring_interesting_headers(self, headers, expires):
        interesting_headers = {}
        if isinstance(headers, dict):
            for hash_key in headers.keys():
                lk = hash_key.lower()
                if lk in _CONTENT_LIST or lk.startswith(self._get_header_prefix()):
                    s = headers.get(hash_key)
                    interesting_headers[lk] = ''.join(s)

        key_list = interesting_headers.keys()

        if self.date_header() in key_list:
            interesting_headers[_DATE_HEADER.lower()] = ''

        if expires:
            interesting_headers[_DATE_HEADER.lower()] = expires

        if _CONTENT_TYPE_HEADER.lower() not in key_list:
            interesting_headers[_CONTENT_TYPE_HEADER.lower()] = ''

        if _CONTENT_MD5_HEADER.lower() not in key_list:
            interesting_headers[_CONTENT_MD5_HEADER.lower()] = ''

        return interesting_headers

    @classmethod
    def __make_canonicalstring_str_list(self, keylist, method, interesting_headers):
        str_list = [method + '\n']
        for k in keylist:
            header_key = self.to_string(k)
            val = '' if interesting_headers[header_key] is None else interesting_headers[header_key]
            if header_key.startswith(self._get_meta_header_prefix()):
                str_list.append(header_key + ':' + self.to_string(val).strip())
            elif header_key.startswith(self._get_header_prefix()):
                str_list.append(header_key + ':' + val)
            else:
                str_list.append(val)
            str_list.append('\n')
        return str_list

    @classmethod
    def process_request_uri(cls, request):
        # type: (SdkRequest) -> None
        canonical_query_string = cls._process_canonical_query_string(request)
        request.uri = "%s?%s" % (request.resource_path, canonical_query_string) \
            if canonical_query_string != "" else request.resource_path

    @classmethod
    def _url_encode(cls, s):
        # type: (str) -> str
        return quote(s, safe='~')

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
            if value == ' ' or not value:
                canonical_query_param.append(k)
            elif isinstance(value, list):
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
