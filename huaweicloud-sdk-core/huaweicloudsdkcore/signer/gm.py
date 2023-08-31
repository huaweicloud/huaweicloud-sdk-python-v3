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
from sys import version_info

import ecdsa
from ecdsa.curves import Curve
from ecdsa.ellipticcurve import CurveFp, PointJacobi, Point
from ecdsa.util import sigencode_der, sigdecode_der

from huaweicloudsdkcore.exceptions.exceptions import SdkException

_CURVE_FP_SM2 = CurveFp(p=0xfffffffeffffffffffffffffffffffffffffffff00000000ffffffffffffffff,
                        a=0xfffffffeffffffffffffffffffffffffffffffff00000000fffffffffffffffc,
                        b=0x28e9fa9e9d9f5e344d5a9e4bcf6509a7f39789f515ab8f92ddbcbd414d940e93,
                        h=0x01)

_GENERATOR_SM2 = PointJacobi(curve=_CURVE_FP_SM2,
                             x=0x32c4ae2c1f1981195f9904466a39c9948fe30bbff2660be1715a4589334c74c7,
                             y=0xbc3736a2f4f6779c59bdcee36b692153d0a9877cc62a474002df32e52139f0a0,
                             z=1,
                             order=0xfffffffeffffffffffffffffffffffff7203df6b21c6052b53bbf40939d54123,
                             generator=True)

_BASE_POINT_SM2 = Point(curve=_CURVE_FP_SM2,
                        x=_GENERATOR_SM2.x(),
                        y=_GENERATOR_SM2.y(),
                        order=_GENERATOR_SM2.order())

CURVE_SM2 = Curve(
    name="SM2",
    curve=_CURVE_FP_SM2,
    generator=_GENERATOR_SM2,
    oid=(1, 2, 156, 10197, 1, 301),
    openssl_name="prime256v1")

if version_info.major == 3:
    if version_info.minor < 7:
        _IV = [0x7380166f, 0x4914b2b9, 0x172442d7, 0xda8a0600, 0xa96f30bc, 0x163138aa, 0xe38dee4d, 0xb0fb0e4e]
        _T_J = [0x79cc4519 if j < 16 else 0x7a879d8a for j in range(64)]
        _0X8F = 0xffffffff

        _OUT_OF_RANGE_ERROR = ValueError("j out of range [0, 64)")


        def _left_rotate(n, k):
            # type: (int, int) -> int
            """
            Shift the binary representation of n to the left by k bits,
            and then shift the k bits of the highest bits to the lowest bits to form a new 32-bit unsigned integer.
            """
            return ((n << k) & _0X8F) | ((n >> (32 - k)) & _0X8F)


        def _ff_j(x, y, z, j):
            # type: (int, int, int, int) -> int
            """Boolean function, take different expressions as j changes. Based on GB/T 32905-2016."""
            if 0 <= j < 16:
                return x ^ y ^ z
            elif 16 <= j < 64:
                return (x & y) | (x & z) | (y & z)
            else:
                raise _OUT_OF_RANGE_ERROR


        def _gg_j(x, y, z, j):
            # type: (int, int, int, int) -> int
            """Boolean function, take different expressions as j changes, based on GB/T 32905-2016."""
            if 0 <= j < 16:
                return x ^ y ^ z
            elif 16 <= j < 64:
                return (x & y) ^ (~x & z)
            else:
                raise _OUT_OF_RANGE_ERROR


        def _p_0(x):
            # type: (int) -> int
            """permutation function in compression function, based on GB/T 32905-2016."""
            return x ^ _left_rotate(x, 9) ^ _left_rotate(x, 17)


        def _p_1(x):
            # type: (int) -> int
            """permutation function in compression function, based on GB/T 32905-2016."""
            return x ^ _left_rotate(x, 15) ^ _left_rotate(x, 23)


        def _cf(v_i, b_i):
            # type: (list[int], list[int]) -> list[int]
            """Compression function, based on GB/T 32905-2016."""
            w = [0] * 68
            for i in range(16):
                data = b_i[i * 4: (i + 1) * 4]
                w[i] = int.from_bytes(data, byteorder='big')

            for i in range(16, 68):
                w[i] = _p_1(w[i - 16] ^ w[i - 9] ^ (_left_rotate(w[i - 3], 15))) ^ (_left_rotate(w[i - 13], 7)) ^ w[
                    i - 6]

            w_1 = [w[i] ^ w[i + 4] for i in range(64)]

            a, b, c, d, e, f, g, h = v_i

            for i in range(64):
                ss_1 = _left_rotate((_left_rotate(a, 12) + e + _left_rotate(_T_J[i], i % 32)) & _0X8F, 7)
                ss_2 = ss_1 ^ _left_rotate(a, 12)
                tt_1 = (_ff_j(a, b, c, i) + d + ss_2 + w_1[i]) & _0X8F
                tt_2 = (_gg_j(e, f, g, i) + h + ss_1 + w[i]) & _0X8F
                d, c, b, a, h, g, f, e = c, _left_rotate(b, 9), a, tt_1, g, _left_rotate(f, 19), e, _p_0(tt_2)
                a, b, c, d, e, f, g, h = map(lambda x: x & _0X8F, (a, b, c, d, e, f, g, h))

            v_j = (a, b, c, d, e, f, g, h)
            return [v_j[i] ^ v_i[i] for i in range(8)]


        def _hash(data):
            # type: (bytes) -> bytes
            """Hash function, based on GB/T 32905-2016."""
            data_list = [i for i in data]
            length = len(data_list)
            bit_length = length * 8
            k = (56 - length - 1) % 64
            data_list.append(0x80)
            data_list.extend([0x00] * k)
            data_list.extend([i for i in bit_length.to_bytes(8, 'big')])

            iter_count = int(len(data_list) / 64)
            b = [data_list[i * 64:(i + 1) * 64] for i in range(iter_count)]

            v = [_IV]

            i = 0
            for i in range(iter_count):
                v.append(_cf(v[i], b[i]))

            return b''.join(map(lambda n: n.to_bytes(4, 'big'), v[i + 1]))


        class _SM3Hash:
            name = 'sm3'
            digest_size = 32
            block_size = 64

            def __init__(self, data=b''):
                self._bytearray = bytearray(data)

            def update(self, data):
                # type: (bytes) -> None
                self._bytearray.extend(data)

            def digest(self):
                # type: () -> bytes
                return _hash(bytes(self._bytearray))

            def hexdigest(self):
                # type: () -> str
                return self.digest().hex()

            def copy(self):
                # type: () -> _SM3Hash
                return self.__class__(bytes(self._bytearray))


        new_sm3_hash = lambda data=b'': _SM3Hash(data)
    else:
        import hashlib

        new_sm3_hash = lambda data=b'': hashlib.new('sm3', data)
else:
    new_sm3_hash = None


def _int_to_bytes(i):
    # type: (int) -> bytes
    return i.to_bytes(length=(i.bit_length() + 7) // 8, byteorder='big', signed=i < 0)


try:
    from secrets import randbelow


    def _secure_randint(a, b):
        # type: (int, int) -> int
        random_int = randbelow(b - a + 1) + a
        return random_int
except ImportError:
    from os import urandom


    def _secure_randint(a, b):
        # type: (int, int) -> int
        range_size = b - a + 1
        num_bytes = (range_size.bit_length() + 7) // 8
        rand_bytes = urandom(num_bytes)
        rand_int = int.from_bytes(rand_bytes, byteorder='big')
        return a + rand_int % range_size


def _za(public_key_bytes, uid=b'1234567812345678'):
    # type: (bytes, bytes) -> bytes
    """
    Cryptographic hash algorithm

    ZA = H256(ENTLA | | IDA | | a | | b | | xG | | yG | | xA | | yA)
    """
    array = bytearray()
    uid_len = len(uid)
    if uid_len >= 8192:
        raise ValueError("SM2: uid too large")

    entla = uid_len * 8
    array.append((entla >> 8) & 0xff)
    array.append(entla & 0xff)

    if uid_len > 0:
        array.extend(uid)

    array.extend(_int_to_bytes(_CURVE_FP_SM2.a()))
    array.extend(_int_to_bytes(_CURVE_FP_SM2.b()))
    array.extend(_int_to_bytes(_BASE_POINT_SM2.x()))
    array.extend(_int_to_bytes(_BASE_POINT_SM2.y()))
    array.extend(public_key_bytes)
    return new_sm3_hash(array).digest()


class SM2SigningKey(object):
    def __init__(self, private_key_bytes):
        # type: (bytes) -> None
        private_key = ecdsa.SigningKey.from_string(private_key_bytes, curve=CURVE_SM2, hashfunc=new_sm3_hash)
        public_key = private_key.get_verifying_key()
        self._d = private_key.privkey.secret_multiplier
        self._public_point = public_key.pubkey.point
        self._za = _za(public_key.to_string())

    def sign(self, data):
        # type: (bytes) -> bytes
        """
        SM2 sign, based on GB/T 32918.2-2016

        Step 1: M' = Za || M
        Step 2: e = Hash(M')
        Step 3: Random k in [1, n-1]
        Step 4: P(x,y) = [k]G(x,y)
        Step 5: r = (e + x1) mod n, back to step 3 if r = 0 or r + k = n
        Step 6: s = ((1 + D)^-1 · (k - r · D)) mod n, back to step 3 if s = 0
        Step 7: Encode r and s to ASN.1-DER
        """
        n = CURVE_SM2.order

        m = self._za + data

        hm = new_sm3_hash(m).digest()
        e = int.from_bytes(hm, byteorder='big')

        for _ in range(100):
            k = _secure_randint(1, n - 1)

            kp = k * _BASE_POINT_SM2

            r = (e + kp.x()) % n
            if r == 0 or r + k == n:
                continue

            d_1 = pow(self._d + 1, n - 2, n)
            s = (d_1 * (k + r) - r) % n
            if s == 0:
                continue

            return sigencode_der(r, s, n)

        raise SdkException("sm2 sign failed")

    def verify(self, signature, data):
        # type: (bytes, bytes) -> bool
        """
        SM2 verify, based on GB/T 32918.2-2016

        Step 1: assert r in [1, n-1]
        Step 2: assert s in [1, n-1]
        Step 3: M' = Za || M
        Step 4: e = Hash(M')
        Step 5: t = (r + s) mod n, failed if t = 0
        Step 6: P(x,y) = [s]G(x,y) + [t]Pub(x,y)
        Step 7: R = (e + x1) mod n, assert R = r
        """
        n = CURVE_SM2.order
        r, s = sigdecode_der(signature, n)

        if r < 1 or r > n - 1:
            return False

        if s < 1 or s > n - 1:
            return False

        m = self._za + data

        hm = new_sm3_hash(m).digest()
        e = int.from_bytes(hm, byteorder='big')

        t = (r + s) % n
        if t == 0:
            return False

        p = _BASE_POINT_SM2 * s + self._public_point * t

        r_ = (e + p.x()) % n
        return r_ == r
