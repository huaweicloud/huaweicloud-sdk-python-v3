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
