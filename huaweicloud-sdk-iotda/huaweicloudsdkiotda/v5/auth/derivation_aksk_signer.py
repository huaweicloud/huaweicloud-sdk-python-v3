# coding: utf-8

import binascii
import hashlib
import hmac
from datetime import datetime
import six

import huaweicloudsdkiotda.v5.auth.hkdf as HKDF


if six.PY2:
    from urllib import quote, unquote


    def hmac_sha256(key_byte, message):
        return hmac.new(key_byte, message, digestmod=hashlib.sha256).digest()


    def process_string_to_sign(canonical_request, time, info):
        return "%s\n%s\n%s\n%s" % (
            Algorithm,
            datetime.strftime(time, BasicDateFormat),
            info,
            hex_encode_sha256_hash(canonical_request)
        )

else:
    from urllib.parse import quote, unquote


    def hmac_sha256(key_byte, message):
        return hmac.new(key_byte.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).digest()


    def process_string_to_sign(canonical_request, time, info):
        return "%s\n%s\n%s\n%s" % (
            Algorithm,
            datetime.strftime(time, BasicDateFormat),
            info,
            hex_encode_sha256_hash(canonical_request.encode('utf-8'))
        )

EncodeUtf8 = "utf-8"
BasicDateFormat = "%Y%m%dT%H%M%SZ"
BasicISODateFormat = "%Y%m%d"
Algorithm = "V11-HMAC-SHA256"
HeaderXDate = "X-Sdk-Date"
HeaderHost = "Host"
HeaderAuthorization = "Authorization"
HeaderContentSha256 = "X-Sdk-Content-Sha256"
IOT_DA = "iotdm"


def url_encode(s):
    return quote(s, safe='~')


def find_header(r, header):
    for k in r.header_params:
        if k.lower() == header.lower():
            return r.header_params[k]
    return None


def hex_encode_sha256_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()


# Build a CanonicalRequest from a regular request string
#
# CanonicalRequest consists of several parts:
#   Part 1. HTTPRequestMethod
#   Part 2. CanonicalURI
#   Part 3. CanonicalQueryString
#   Part 4. CanonicalHeaders
#   Part 5 SignedHeaders
#   Part 6 HexEncode(Hash(RequestPayload))
def process_canonical_request(request, signed_headers):
    canonical_headers = process_canonical_headers(request, signed_headers)
    hex_encode = find_header(request, HeaderContentSha256)
    if hex_encode is None:
        hex_encode = hex_encode_sha256_hash(request.body)
    canonical_uri = process_canonical_uri(request)
    canonical_query_string = process_canonical_query_string(request)
    return "%s\n%s\n%s\n%s\n%s\n%s" % (request.method.upper(), canonical_uri, canonical_query_string,
                                       canonical_headers, ";".join(signed_headers), hex_encode)


def process_canonical_uri(request):
    pattens = unquote(request.resource_path).split('/')
    uri = []
    for v in pattens:
        uri.append(url_encode(v))
    url_path = "/".join(uri)

    if url_path[-1] != '/':
        url_path = url_path + "/"

    return url_path


def process_canonical_query_string(request):
    params = []
    for param in request.query_params:
        params.append(param)
    params.sort()

    canonical_query_param = []
    for (key, value) in params:
        k = url_encode(key)
        if isinstance(value, list):
            value.sort()
            for v in value:
                kv = k + "=" + url_encode(str(v))
                canonical_query_param.append(kv)
        elif isinstance(value, bool):
            kv = k + "=" + url_encode(str(value).lower())
            canonical_query_param.append(kv)
        else:
            kv = k + "=" + url_encode(str(value))
            canonical_query_param.append(kv)

    return '&'.join(canonical_query_param)


def process_canonical_headers(request, signed_headers):
    canonical_headers = []
    __headers = {}
    for key in request.header_params:
        key_encoded = key.lower()
        value = request.header_params[key]
        value_encoded = value.strip()
        __headers[key_encoded] = value_encoded
        if six.PY3:
            request.header_params[key] = value_encoded.encode("utf-8").decode('iso-8859-1')

    for key in signed_headers:
        canonical_headers.append(key + ":" + __headers[key])

    return '\n'.join(canonical_headers) + "\n"


def process_signed_headers(request):
    signed_headers = []
    for key in request.header_params:
        signed_headers.append(key.lower())
    signed_headers.sort()
    return signed_headers


def sign_string_to_sign(string_to_sign, key):
    hm = hmac_sha256(key, string_to_sign)
    return binascii.hexlify(hm).decode()


def process_auth_header_value(signature, app_key, info, signed_headers):
    return "%s Credential=%s/%s, SignedHeaders=%s, Signature=%s" % (
    Algorithm, app_key, info, ";".join(signed_headers), signature)


class DerivationAKSKSigner(object):
    def __init__(self, credentials):
        self.__ak = credentials.ak
        self.__sk = credentials.sk

    def sign(self, request, region_id):
        if six.PY3 and isinstance(request.body, str):
            request.body = request.body.encode(EncodeUtf8)

        header_time = find_header(request, HeaderXDate)
        if header_time is None:
            t = datetime.utcnow()
            request.header_params[HeaderXDate] = datetime.strftime(t, BasicDateFormat)
        else:
            t = datetime.strptime(header_time, BasicDateFormat)

        has_host_header = False
        for key in request.header_params:
            if key.lower() == 'host':
                has_host_header = True
                break
        if has_host_header is False:
            request.header_params["Host"] = request.host

        signed_headers = process_signed_headers(request)
        canonical_request = process_canonical_request(request, signed_headers)
        date_str = datetime.strftime(datetime.utcnow(), BasicISODateFormat)
        info_str = date_str + "/" + region_id + "/" + IOT_DA
        string_to_sign = process_string_to_sign(canonical_request, t, info_str)
        derivation_key = HKDF.get_der_key_sha256(access_key=self.__ak, secret_key=self.__sk, info=info_str)
        signature = sign_string_to_sign(string_to_sign, derivation_key)
        auth_value = process_auth_header_value(signature, self.__ak, info_str, signed_headers)

        request.header_params[HeaderAuthorization] = auth_value

        canonical_query_string = process_canonical_query_string(request)
        request.uri = request.resource_path + "?" + canonical_query_string if canonical_query_string != "" else request.resource_path

        return request
