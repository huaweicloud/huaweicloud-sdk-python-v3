# coding: utf-8

from __future__ import absolute_import

import hashlib
import math
import hmac
import six
import copy
import binascii

from huaweicloudsdkcore.exceptions.exceptions import SdkException


def get_der_key_sha256(access_key, secret_key, info):
    if not access_key or not secret_key:
        return None
    try:
        tmp_key = extract(secret_key, access_key, HMAC_ALGORITHM)
        der_secret_key = expand(tmp_key, info.encode(UTF_8), HMAC_ALGORITHM, DERIVATION_KEY_LENGTH, EXPAND_CEIL)
        if der_secret_key is not None:
            return binascii.hexlify(der_secret_key).decode()
        return None
    except Exception as e:
        raise e


def get_hash_len(hmac_algorithm):
    if hmac_algorithm == HMAC_SHA1:
        return 20
    elif hmac_algorithm == HMAC_SHA256:
        return 32
    else:
        return 32


def extract(ikm, salt, hmac_algorithm):
    if not salt:
        salt = bytes(get_hash_len(hmac_algorithm)).decode(encoding=UTF_8)

    return hmac_sha256(salt, ikm, hmac_algorithm)


def expand(prk, info, hmac_algorithm, okm_len, ceil):
    if ceil == 1:
        raw_result = expand_first(prk, info, hmac_algorithm)
    else:
        raw_result = bytes()
        tmp = bytes()
        for i in range(1, ceil + 1):
            tmp = expand_once(prk, info, tmp, i, hmac_algorithm)
            raw_result = raw_result + tmp
    if okm_len == len(raw_result):
        return raw_result
    elif okm_len < len(raw_result):
        return raw_result[:okm_len + 1]
    else:
        return None


def expand_first(prk, info, hmac_algorithm):
    result = copy.deepcopy(info)
    result = result + bytearray((1,))
    return hmac_sha256(prk, result, hmac_algorithm)


def expand_once(prk, info, pre_tmp, i, hmac_algorithm):
    result = pre_tmp + info + bytearray((i,))
    return hmac_sha256(prk, result, hmac_algorithm)


def _get_expand_ceil(derivation_key_len, algorithm_hash_len):
    try:
        return int(math.ceil(float(derivation_key_len) / float(algorithm_hash_len)))
    except ZeroDivisionError as e:
        raise ValueError(e)


HMAC_SHA1 = hashlib.sha1
HMAC_SHA256 = hashlib.sha256
DERIVATION_KEY_LENGTH = 32
HMAC_ALGORITHM = HMAC_SHA256
ALGORITHM_HASH_LENGTH = get_hash_len(HMAC_ALGORITHM)
UTF_8 = "utf-8"
EXPAND_CEIL = _get_expand_ceil(DERIVATION_KEY_LENGTH, ALGORITHM_HASH_LENGTH)

if six.PY2:

    def hmac_sha256(key_byte, message, hmac_algorithm):
        return hmac.new(key_byte, message, digestmod=hmac_algorithm).digest()

else:

    def hmac_sha256(key_byte, message, hmac_algorithm):
        if isinstance(key_byte, str) and isinstance(message, str):
            return hmac.new(key_byte.encode(UTF_8), message.encode(UTF_8), digestmod=hmac_algorithm).digest()
        elif isinstance(key_byte, bytes) and isinstance(message, bytes):
            return hmac.new(key_byte, message, digestmod=hmac_algorithm).digest()
        else:
            raise SdkException()
