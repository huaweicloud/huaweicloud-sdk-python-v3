# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatisticInterfaceResponseBodyMetrics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pki_digest_busi_statistic': 'float',
        'pki_decrypt_busi_statistic': 'float',
        'pki_generate_key_busi_statistic': 'float',
        'pki_verify_busi_statistic': 'float',
        'pki_encrypt_busi_statistic': 'float',
        'tsa_verify_busi_statistic': 'float',
        'tsa_parse_busi_statistic': 'float',
        'svs_verify_busi_statistic': 'float',
        'pki_random_busi_statistic': 'float',
        'timestamp': 'int',
        'svs_cert_busi_statistic': 'float',
        'svs_encode_busi_statistic': 'float',
        'tsa_apply_busi_statistic': 'float',
        'svs_sign_busi_statistic': 'float',
        'svs_decrypt_busi_statistic': 'float',
        'kms_busi_statistic': 'float',
        'seal_verify_busi_statistic': 'float',
        'pki_sign_busi_statistic': 'float',
        'secauth_busi_statistic': 'float',
        'seal_sign_busi_statistic': 'float',
        'split_busi_statistic': 'float',
        'svs_random_busi_statistic': 'float',
        'svs_encrypt_busi_statistic': 'float',
        'sms_dec_busi_statistic': 'float',
        'svs_digest_busi_statistic': 'float',
        'svs_decode_busi_statistic': 'float'
    }

    attribute_map = {
        'pki_digest_busi_statistic': 'pkiDigestBusiStatistic',
        'pki_decrypt_busi_statistic': 'pkiDecryptBusiStatistic',
        'pki_generate_key_busi_statistic': 'pkiGenerateKeyBusiStatistic',
        'pki_verify_busi_statistic': 'pkiVerifyBusiStatistic',
        'pki_encrypt_busi_statistic': 'pkiEncryptBusiStatistic',
        'tsa_verify_busi_statistic': 'tsaVerifyBusiStatistic',
        'tsa_parse_busi_statistic': 'tsaParseBusiStatistic',
        'svs_verify_busi_statistic': 'svsVerifyBusiStatistic',
        'pki_random_busi_statistic': 'pkiRandomBusiStatistic',
        'timestamp': 'timestamp',
        'svs_cert_busi_statistic': 'svsCertBusiStatistic',
        'svs_encode_busi_statistic': 'svsEncodeBusiStatistic',
        'tsa_apply_busi_statistic': 'tsaApplyBusiStatistic',
        'svs_sign_busi_statistic': 'svsSignBusiStatistic',
        'svs_decrypt_busi_statistic': 'svsDecryptBusiStatistic',
        'kms_busi_statistic': 'kmsBusiStatistic',
        'seal_verify_busi_statistic': 'sealVerifyBusiStatistic',
        'pki_sign_busi_statistic': 'pkiSignBusiStatistic',
        'secauth_busi_statistic': 'secauthBusiStatistic',
        'seal_sign_busi_statistic': 'sealSignBusiStatistic',
        'split_busi_statistic': 'splitBusiStatistic',
        'svs_random_busi_statistic': 'svsRandomBusiStatistic',
        'svs_encrypt_busi_statistic': 'svsEncryptBusiStatistic',
        'sms_dec_busi_statistic': 'smsDecBusiStatistic',
        'svs_digest_busi_statistic': 'svsDigestBusiStatistic',
        'svs_decode_busi_statistic': 'svsDecodeBusiStatistic'
    }

    def __init__(self, pki_digest_busi_statistic=None, pki_decrypt_busi_statistic=None, pki_generate_key_busi_statistic=None, pki_verify_busi_statistic=None, pki_encrypt_busi_statistic=None, tsa_verify_busi_statistic=None, tsa_parse_busi_statistic=None, svs_verify_busi_statistic=None, pki_random_busi_statistic=None, timestamp=None, svs_cert_busi_statistic=None, svs_encode_busi_statistic=None, tsa_apply_busi_statistic=None, svs_sign_busi_statistic=None, svs_decrypt_busi_statistic=None, kms_busi_statistic=None, seal_verify_busi_statistic=None, pki_sign_busi_statistic=None, secauth_busi_statistic=None, seal_sign_busi_statistic=None, split_busi_statistic=None, svs_random_busi_statistic=None, svs_encrypt_busi_statistic=None, sms_dec_busi_statistic=None, svs_digest_busi_statistic=None, svs_decode_busi_statistic=None):
        r"""ShowStatisticInterfaceResponseBodyMetrics

        The model defined in huaweicloud sdk

        :param pki_digest_busi_statistic: 杂凑
        :type pki_digest_busi_statistic: float
        :param pki_decrypt_busi_statistic: 解密
        :type pki_decrypt_busi_statistic: float
        :param pki_generate_key_busi_statistic: 生成密钥
        :type pki_generate_key_busi_statistic: float
        :param pki_verify_busi_statistic: 验章次数
        :type pki_verify_busi_statistic: float
        :param pki_encrypt_busi_statistic: 加密
        :type pki_encrypt_busi_statistic: float
        :param tsa_verify_busi_statistic: 验证次数
        :type tsa_verify_busi_statistic: float
        :param tsa_parse_busi_statistic: 解析次数
        :type tsa_parse_busi_statistic: float
        :param svs_verify_busi_statistic: svs验签
        :type svs_verify_busi_statistic: float
        :param pki_random_busi_statistic: 生成随机
        :type pki_random_busi_statistic: float
        :param timestamp: 统计时间，UNIX时间戳，单位毫秒
        :type timestamp: int
        :param svs_cert_busi_statistic: svs获取证书等相关证书操作
        :type svs_cert_busi_statistic: float
        :param svs_encode_busi_statistic: svs编码
        :type svs_encode_busi_statistic: float
        :param tsa_apply_busi_statistic: 申请次数
        :type tsa_apply_busi_statistic: float
        :param svs_sign_busi_statistic: svs签名
        :type svs_sign_busi_statistic: float
        :param svs_decrypt_busi_statistic: svs解密
        :type svs_decrypt_busi_statistic: float
        :param kms_busi_statistic: 调用次数
        :type kms_busi_statistic: float
        :param seal_verify_busi_statistic: 验章次数
        :type seal_verify_busi_statistic: float
        :param pki_sign_busi_statistic: 签名
        :type pki_sign_busi_statistic: float
        :param secauth_busi_statistic: 口令验证
        :type secauth_busi_statistic: float
        :param seal_sign_busi_statistic: 签章次数
        :type seal_sign_busi_statistic: float
        :param split_busi_statistic: 签名次数
        :type split_busi_statistic: float
        :param svs_random_busi_statistic: svs生成随机
        :type svs_random_busi_statistic: float
        :param svs_encrypt_busi_statistic: svs加密
        :type svs_encrypt_busi_statistic: float
        :param sms_dec_busi_statistic: 解密次数
        :type sms_dec_busi_statistic: float
        :param svs_digest_busi_statistic: svs杂凑
        :type svs_digest_busi_statistic: float
        :param svs_decode_busi_statistic: svs解码
        :type svs_decode_busi_statistic: float
        """
        
        

        self._pki_digest_busi_statistic = None
        self._pki_decrypt_busi_statistic = None
        self._pki_generate_key_busi_statistic = None
        self._pki_verify_busi_statistic = None
        self._pki_encrypt_busi_statistic = None
        self._tsa_verify_busi_statistic = None
        self._tsa_parse_busi_statistic = None
        self._svs_verify_busi_statistic = None
        self._pki_random_busi_statistic = None
        self._timestamp = None
        self._svs_cert_busi_statistic = None
        self._svs_encode_busi_statistic = None
        self._tsa_apply_busi_statistic = None
        self._svs_sign_busi_statistic = None
        self._svs_decrypt_busi_statistic = None
        self._kms_busi_statistic = None
        self._seal_verify_busi_statistic = None
        self._pki_sign_busi_statistic = None
        self._secauth_busi_statistic = None
        self._seal_sign_busi_statistic = None
        self._split_busi_statistic = None
        self._svs_random_busi_statistic = None
        self._svs_encrypt_busi_statistic = None
        self._sms_dec_busi_statistic = None
        self._svs_digest_busi_statistic = None
        self._svs_decode_busi_statistic = None
        self.discriminator = None

        if pki_digest_busi_statistic is not None:
            self.pki_digest_busi_statistic = pki_digest_busi_statistic
        if pki_decrypt_busi_statistic is not None:
            self.pki_decrypt_busi_statistic = pki_decrypt_busi_statistic
        if pki_generate_key_busi_statistic is not None:
            self.pki_generate_key_busi_statistic = pki_generate_key_busi_statistic
        if pki_verify_busi_statistic is not None:
            self.pki_verify_busi_statistic = pki_verify_busi_statistic
        if pki_encrypt_busi_statistic is not None:
            self.pki_encrypt_busi_statistic = pki_encrypt_busi_statistic
        if tsa_verify_busi_statistic is not None:
            self.tsa_verify_busi_statistic = tsa_verify_busi_statistic
        if tsa_parse_busi_statistic is not None:
            self.tsa_parse_busi_statistic = tsa_parse_busi_statistic
        if svs_verify_busi_statistic is not None:
            self.svs_verify_busi_statistic = svs_verify_busi_statistic
        if pki_random_busi_statistic is not None:
            self.pki_random_busi_statistic = pki_random_busi_statistic
        if timestamp is not None:
            self.timestamp = timestamp
        if svs_cert_busi_statistic is not None:
            self.svs_cert_busi_statistic = svs_cert_busi_statistic
        if svs_encode_busi_statistic is not None:
            self.svs_encode_busi_statistic = svs_encode_busi_statistic
        if tsa_apply_busi_statistic is not None:
            self.tsa_apply_busi_statistic = tsa_apply_busi_statistic
        if svs_sign_busi_statistic is not None:
            self.svs_sign_busi_statistic = svs_sign_busi_statistic
        if svs_decrypt_busi_statistic is not None:
            self.svs_decrypt_busi_statistic = svs_decrypt_busi_statistic
        if kms_busi_statistic is not None:
            self.kms_busi_statistic = kms_busi_statistic
        if seal_verify_busi_statistic is not None:
            self.seal_verify_busi_statistic = seal_verify_busi_statistic
        if pki_sign_busi_statistic is not None:
            self.pki_sign_busi_statistic = pki_sign_busi_statistic
        if secauth_busi_statistic is not None:
            self.secauth_busi_statistic = secauth_busi_statistic
        if seal_sign_busi_statistic is not None:
            self.seal_sign_busi_statistic = seal_sign_busi_statistic
        if split_busi_statistic is not None:
            self.split_busi_statistic = split_busi_statistic
        if svs_random_busi_statistic is not None:
            self.svs_random_busi_statistic = svs_random_busi_statistic
        if svs_encrypt_busi_statistic is not None:
            self.svs_encrypt_busi_statistic = svs_encrypt_busi_statistic
        if sms_dec_busi_statistic is not None:
            self.sms_dec_busi_statistic = sms_dec_busi_statistic
        if svs_digest_busi_statistic is not None:
            self.svs_digest_busi_statistic = svs_digest_busi_statistic
        if svs_decode_busi_statistic is not None:
            self.svs_decode_busi_statistic = svs_decode_busi_statistic

    @property
    def pki_digest_busi_statistic(self):
        r"""Gets the pki_digest_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        杂凑

        :return: The pki_digest_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._pki_digest_busi_statistic

    @pki_digest_busi_statistic.setter
    def pki_digest_busi_statistic(self, pki_digest_busi_statistic):
        r"""Sets the pki_digest_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        杂凑

        :param pki_digest_busi_statistic: The pki_digest_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type pki_digest_busi_statistic: float
        """
        self._pki_digest_busi_statistic = pki_digest_busi_statistic

    @property
    def pki_decrypt_busi_statistic(self):
        r"""Gets the pki_decrypt_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        解密

        :return: The pki_decrypt_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._pki_decrypt_busi_statistic

    @pki_decrypt_busi_statistic.setter
    def pki_decrypt_busi_statistic(self, pki_decrypt_busi_statistic):
        r"""Sets the pki_decrypt_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        解密

        :param pki_decrypt_busi_statistic: The pki_decrypt_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type pki_decrypt_busi_statistic: float
        """
        self._pki_decrypt_busi_statistic = pki_decrypt_busi_statistic

    @property
    def pki_generate_key_busi_statistic(self):
        r"""Gets the pki_generate_key_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        生成密钥

        :return: The pki_generate_key_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._pki_generate_key_busi_statistic

    @pki_generate_key_busi_statistic.setter
    def pki_generate_key_busi_statistic(self, pki_generate_key_busi_statistic):
        r"""Sets the pki_generate_key_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        生成密钥

        :param pki_generate_key_busi_statistic: The pki_generate_key_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type pki_generate_key_busi_statistic: float
        """
        self._pki_generate_key_busi_statistic = pki_generate_key_busi_statistic

    @property
    def pki_verify_busi_statistic(self):
        r"""Gets the pki_verify_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        验章次数

        :return: The pki_verify_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._pki_verify_busi_statistic

    @pki_verify_busi_statistic.setter
    def pki_verify_busi_statistic(self, pki_verify_busi_statistic):
        r"""Sets the pki_verify_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        验章次数

        :param pki_verify_busi_statistic: The pki_verify_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type pki_verify_busi_statistic: float
        """
        self._pki_verify_busi_statistic = pki_verify_busi_statistic

    @property
    def pki_encrypt_busi_statistic(self):
        r"""Gets the pki_encrypt_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        加密

        :return: The pki_encrypt_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._pki_encrypt_busi_statistic

    @pki_encrypt_busi_statistic.setter
    def pki_encrypt_busi_statistic(self, pki_encrypt_busi_statistic):
        r"""Sets the pki_encrypt_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        加密

        :param pki_encrypt_busi_statistic: The pki_encrypt_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type pki_encrypt_busi_statistic: float
        """
        self._pki_encrypt_busi_statistic = pki_encrypt_busi_statistic

    @property
    def tsa_verify_busi_statistic(self):
        r"""Gets the tsa_verify_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        验证次数

        :return: The tsa_verify_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._tsa_verify_busi_statistic

    @tsa_verify_busi_statistic.setter
    def tsa_verify_busi_statistic(self, tsa_verify_busi_statistic):
        r"""Sets the tsa_verify_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        验证次数

        :param tsa_verify_busi_statistic: The tsa_verify_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type tsa_verify_busi_statistic: float
        """
        self._tsa_verify_busi_statistic = tsa_verify_busi_statistic

    @property
    def tsa_parse_busi_statistic(self):
        r"""Gets the tsa_parse_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        解析次数

        :return: The tsa_parse_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._tsa_parse_busi_statistic

    @tsa_parse_busi_statistic.setter
    def tsa_parse_busi_statistic(self, tsa_parse_busi_statistic):
        r"""Sets the tsa_parse_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        解析次数

        :param tsa_parse_busi_statistic: The tsa_parse_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type tsa_parse_busi_statistic: float
        """
        self._tsa_parse_busi_statistic = tsa_parse_busi_statistic

    @property
    def svs_verify_busi_statistic(self):
        r"""Gets the svs_verify_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs验签

        :return: The svs_verify_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._svs_verify_busi_statistic

    @svs_verify_busi_statistic.setter
    def svs_verify_busi_statistic(self, svs_verify_busi_statistic):
        r"""Sets the svs_verify_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs验签

        :param svs_verify_busi_statistic: The svs_verify_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type svs_verify_busi_statistic: float
        """
        self._svs_verify_busi_statistic = svs_verify_busi_statistic

    @property
    def pki_random_busi_statistic(self):
        r"""Gets the pki_random_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        生成随机

        :return: The pki_random_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._pki_random_busi_statistic

    @pki_random_busi_statistic.setter
    def pki_random_busi_statistic(self, pki_random_busi_statistic):
        r"""Sets the pki_random_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        生成随机

        :param pki_random_busi_statistic: The pki_random_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type pki_random_busi_statistic: float
        """
        self._pki_random_busi_statistic = pki_random_busi_statistic

    @property
    def timestamp(self):
        r"""Gets the timestamp of this ShowStatisticInterfaceResponseBodyMetrics.

        统计时间，UNIX时间戳，单位毫秒

        :return: The timestamp of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this ShowStatisticInterfaceResponseBodyMetrics.

        统计时间，UNIX时间戳，单位毫秒

        :param timestamp: The timestamp of this ShowStatisticInterfaceResponseBodyMetrics.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def svs_cert_busi_statistic(self):
        r"""Gets the svs_cert_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs获取证书等相关证书操作

        :return: The svs_cert_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._svs_cert_busi_statistic

    @svs_cert_busi_statistic.setter
    def svs_cert_busi_statistic(self, svs_cert_busi_statistic):
        r"""Sets the svs_cert_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs获取证书等相关证书操作

        :param svs_cert_busi_statistic: The svs_cert_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type svs_cert_busi_statistic: float
        """
        self._svs_cert_busi_statistic = svs_cert_busi_statistic

    @property
    def svs_encode_busi_statistic(self):
        r"""Gets the svs_encode_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs编码

        :return: The svs_encode_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._svs_encode_busi_statistic

    @svs_encode_busi_statistic.setter
    def svs_encode_busi_statistic(self, svs_encode_busi_statistic):
        r"""Sets the svs_encode_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs编码

        :param svs_encode_busi_statistic: The svs_encode_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type svs_encode_busi_statistic: float
        """
        self._svs_encode_busi_statistic = svs_encode_busi_statistic

    @property
    def tsa_apply_busi_statistic(self):
        r"""Gets the tsa_apply_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        申请次数

        :return: The tsa_apply_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._tsa_apply_busi_statistic

    @tsa_apply_busi_statistic.setter
    def tsa_apply_busi_statistic(self, tsa_apply_busi_statistic):
        r"""Sets the tsa_apply_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        申请次数

        :param tsa_apply_busi_statistic: The tsa_apply_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type tsa_apply_busi_statistic: float
        """
        self._tsa_apply_busi_statistic = tsa_apply_busi_statistic

    @property
    def svs_sign_busi_statistic(self):
        r"""Gets the svs_sign_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs签名

        :return: The svs_sign_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._svs_sign_busi_statistic

    @svs_sign_busi_statistic.setter
    def svs_sign_busi_statistic(self, svs_sign_busi_statistic):
        r"""Sets the svs_sign_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs签名

        :param svs_sign_busi_statistic: The svs_sign_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type svs_sign_busi_statistic: float
        """
        self._svs_sign_busi_statistic = svs_sign_busi_statistic

    @property
    def svs_decrypt_busi_statistic(self):
        r"""Gets the svs_decrypt_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs解密

        :return: The svs_decrypt_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._svs_decrypt_busi_statistic

    @svs_decrypt_busi_statistic.setter
    def svs_decrypt_busi_statistic(self, svs_decrypt_busi_statistic):
        r"""Sets the svs_decrypt_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs解密

        :param svs_decrypt_busi_statistic: The svs_decrypt_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type svs_decrypt_busi_statistic: float
        """
        self._svs_decrypt_busi_statistic = svs_decrypt_busi_statistic

    @property
    def kms_busi_statistic(self):
        r"""Gets the kms_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        调用次数

        :return: The kms_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._kms_busi_statistic

    @kms_busi_statistic.setter
    def kms_busi_statistic(self, kms_busi_statistic):
        r"""Sets the kms_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        调用次数

        :param kms_busi_statistic: The kms_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type kms_busi_statistic: float
        """
        self._kms_busi_statistic = kms_busi_statistic

    @property
    def seal_verify_busi_statistic(self):
        r"""Gets the seal_verify_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        验章次数

        :return: The seal_verify_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._seal_verify_busi_statistic

    @seal_verify_busi_statistic.setter
    def seal_verify_busi_statistic(self, seal_verify_busi_statistic):
        r"""Sets the seal_verify_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        验章次数

        :param seal_verify_busi_statistic: The seal_verify_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type seal_verify_busi_statistic: float
        """
        self._seal_verify_busi_statistic = seal_verify_busi_statistic

    @property
    def pki_sign_busi_statistic(self):
        r"""Gets the pki_sign_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        签名

        :return: The pki_sign_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._pki_sign_busi_statistic

    @pki_sign_busi_statistic.setter
    def pki_sign_busi_statistic(self, pki_sign_busi_statistic):
        r"""Sets the pki_sign_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        签名

        :param pki_sign_busi_statistic: The pki_sign_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type pki_sign_busi_statistic: float
        """
        self._pki_sign_busi_statistic = pki_sign_busi_statistic

    @property
    def secauth_busi_statistic(self):
        r"""Gets the secauth_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        口令验证

        :return: The secauth_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._secauth_busi_statistic

    @secauth_busi_statistic.setter
    def secauth_busi_statistic(self, secauth_busi_statistic):
        r"""Sets the secauth_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        口令验证

        :param secauth_busi_statistic: The secauth_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type secauth_busi_statistic: float
        """
        self._secauth_busi_statistic = secauth_busi_statistic

    @property
    def seal_sign_busi_statistic(self):
        r"""Gets the seal_sign_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        签章次数

        :return: The seal_sign_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._seal_sign_busi_statistic

    @seal_sign_busi_statistic.setter
    def seal_sign_busi_statistic(self, seal_sign_busi_statistic):
        r"""Sets the seal_sign_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        签章次数

        :param seal_sign_busi_statistic: The seal_sign_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type seal_sign_busi_statistic: float
        """
        self._seal_sign_busi_statistic = seal_sign_busi_statistic

    @property
    def split_busi_statistic(self):
        r"""Gets the split_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        签名次数

        :return: The split_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._split_busi_statistic

    @split_busi_statistic.setter
    def split_busi_statistic(self, split_busi_statistic):
        r"""Sets the split_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        签名次数

        :param split_busi_statistic: The split_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type split_busi_statistic: float
        """
        self._split_busi_statistic = split_busi_statistic

    @property
    def svs_random_busi_statistic(self):
        r"""Gets the svs_random_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs生成随机

        :return: The svs_random_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._svs_random_busi_statistic

    @svs_random_busi_statistic.setter
    def svs_random_busi_statistic(self, svs_random_busi_statistic):
        r"""Sets the svs_random_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs生成随机

        :param svs_random_busi_statistic: The svs_random_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type svs_random_busi_statistic: float
        """
        self._svs_random_busi_statistic = svs_random_busi_statistic

    @property
    def svs_encrypt_busi_statistic(self):
        r"""Gets the svs_encrypt_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs加密

        :return: The svs_encrypt_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._svs_encrypt_busi_statistic

    @svs_encrypt_busi_statistic.setter
    def svs_encrypt_busi_statistic(self, svs_encrypt_busi_statistic):
        r"""Sets the svs_encrypt_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs加密

        :param svs_encrypt_busi_statistic: The svs_encrypt_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type svs_encrypt_busi_statistic: float
        """
        self._svs_encrypt_busi_statistic = svs_encrypt_busi_statistic

    @property
    def sms_dec_busi_statistic(self):
        r"""Gets the sms_dec_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        解密次数

        :return: The sms_dec_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._sms_dec_busi_statistic

    @sms_dec_busi_statistic.setter
    def sms_dec_busi_statistic(self, sms_dec_busi_statistic):
        r"""Sets the sms_dec_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        解密次数

        :param sms_dec_busi_statistic: The sms_dec_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type sms_dec_busi_statistic: float
        """
        self._sms_dec_busi_statistic = sms_dec_busi_statistic

    @property
    def svs_digest_busi_statistic(self):
        r"""Gets the svs_digest_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs杂凑

        :return: The svs_digest_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._svs_digest_busi_statistic

    @svs_digest_busi_statistic.setter
    def svs_digest_busi_statistic(self, svs_digest_busi_statistic):
        r"""Sets the svs_digest_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs杂凑

        :param svs_digest_busi_statistic: The svs_digest_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type svs_digest_busi_statistic: float
        """
        self._svs_digest_busi_statistic = svs_digest_busi_statistic

    @property
    def svs_decode_busi_statistic(self):
        r"""Gets the svs_decode_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs解码

        :return: The svs_decode_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :rtype: float
        """
        return self._svs_decode_busi_statistic

    @svs_decode_busi_statistic.setter
    def svs_decode_busi_statistic(self, svs_decode_busi_statistic):
        r"""Sets the svs_decode_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.

        svs解码

        :param svs_decode_busi_statistic: The svs_decode_busi_statistic of this ShowStatisticInterfaceResponseBodyMetrics.
        :type svs_decode_busi_statistic: float
        """
        self._svs_decode_busi_statistic = svs_decode_busi_statistic

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowStatisticInterfaceResponseBodyMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
