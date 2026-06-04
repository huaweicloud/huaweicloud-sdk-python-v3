# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpsTlsVersion:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tls_version': 'str',
        'cipher_suite_group': 'str',
        'cipher_suite': 'str'
    }

    attribute_map = {
        'tls_version': 'tls_version',
        'cipher_suite_group': 'cipher_suite_group',
        'cipher_suite': 'cipher_suite'
    }

    def __init__(self, tls_version=None, cipher_suite_group=None, cipher_suite=None):
        r"""HttpsTlsVersion

        The model defined in huaweicloud sdk

        :param tls_version: **参数解释：** 传输层安全性协议，即TLS版本配置 **约束限制：** - 不可全部关闭 - 需开启连续或单个版本号，例：不可仅开启TLS1.0/1.2而关闭TLS1.1 - 多版本开启时，使用“,”拼接，例：TLSv1.1,TLSv1.2 - 配置TLS版本需要先开启HTTPS国际证书  **取值范围：** 目前支持TLSv1.0/1.1/1.2/1.3四个版本的协议  **默认取值：** 不涉及
        :type tls_version: str
        :param cipher_suite_group: **参数解释：** 加密算法套件组 **约束限制：** TLS版本仅选择1.0和（或）1.1时，不支持选择强加密套件。 **取值范围：** - default: 默认加密套件 - general: 一般加密套件 - strict: 强加密套件 - custom: 自定义加密套件  **默认取值：** 不涉及
        :type cipher_suite_group: str
        :param cipher_suite: **参数解释：** 加密套件 **约束限制：** - 当选择自定义加密套件时，必传 - 选择多个加密套件是以“,”分隔  **取值范围：** - ECDHE-ECDSA-AES128-GCM-SHA256 - ECDHE-ECDSA-AES256-GCM-SHA384 - ECDHE-RSA-AES128-GCM-SHA256 - ECDHE-RSA-AES256-GCM-SHA384 - DHE-RSA-AES128-GCM-SHA256 - DHE-RSA-AES256-GCM-SHA384 - ECDHE-ECDSA-AES128-SHA256 - ECDHE-ECDSA-AES256-SHA384 - ECDHE-RSA-AES128-SHA - ECDHE-RSA-AES128-SHA256 - ECDHE-RSA-AES256-SHA - ECDHE-RSA-AES256-SHA384 - DHE-RSA-AES128-SHA - DHE-RSA-AES128-SHA256 - DHE-RSA-AES256-SHA - DHE-RSA-AES256-SHA256 - AES128-GCM-SHA256 - AES256-GCM-SHA384 - AES128-SHA256 - AES256-SHA256 - ECDHE-ECDSA-CHACHA20-POLY1305 - ECDHE-RSA-CHACHA20-POLY1305 - DHE-RSA-CHACHA20-POLY1305 - ECDHE-ECDSA-AES128-SHA - ECDHE-ECDSA-AES256-SHA - AES128-SHA - AES256-SHA - DES-CBC3-SHA - RC4-SHA  **默认取值：** 不涉及
        :type cipher_suite: str
        """
        
        

        self._tls_version = None
        self._cipher_suite_group = None
        self._cipher_suite = None
        self.discriminator = None

        self.tls_version = tls_version
        self.cipher_suite_group = cipher_suite_group
        if cipher_suite is not None:
            self.cipher_suite = cipher_suite

    @property
    def tls_version(self):
        r"""Gets the tls_version of this HttpsTlsVersion.

        **参数解释：** 传输层安全性协议，即TLS版本配置 **约束限制：** - 不可全部关闭 - 需开启连续或单个版本号，例：不可仅开启TLS1.0/1.2而关闭TLS1.1 - 多版本开启时，使用“,”拼接，例：TLSv1.1,TLSv1.2 - 配置TLS版本需要先开启HTTPS国际证书  **取值范围：** 目前支持TLSv1.0/1.1/1.2/1.3四个版本的协议  **默认取值：** 不涉及

        :return: The tls_version of this HttpsTlsVersion.
        :rtype: str
        """
        return self._tls_version

    @tls_version.setter
    def tls_version(self, tls_version):
        r"""Sets the tls_version of this HttpsTlsVersion.

        **参数解释：** 传输层安全性协议，即TLS版本配置 **约束限制：** - 不可全部关闭 - 需开启连续或单个版本号，例：不可仅开启TLS1.0/1.2而关闭TLS1.1 - 多版本开启时，使用“,”拼接，例：TLSv1.1,TLSv1.2 - 配置TLS版本需要先开启HTTPS国际证书  **取值范围：** 目前支持TLSv1.0/1.1/1.2/1.3四个版本的协议  **默认取值：** 不涉及

        :param tls_version: The tls_version of this HttpsTlsVersion.
        :type tls_version: str
        """
        self._tls_version = tls_version

    @property
    def cipher_suite_group(self):
        r"""Gets the cipher_suite_group of this HttpsTlsVersion.

        **参数解释：** 加密算法套件组 **约束限制：** TLS版本仅选择1.0和（或）1.1时，不支持选择强加密套件。 **取值范围：** - default: 默认加密套件 - general: 一般加密套件 - strict: 强加密套件 - custom: 自定义加密套件  **默认取值：** 不涉及

        :return: The cipher_suite_group of this HttpsTlsVersion.
        :rtype: str
        """
        return self._cipher_suite_group

    @cipher_suite_group.setter
    def cipher_suite_group(self, cipher_suite_group):
        r"""Sets the cipher_suite_group of this HttpsTlsVersion.

        **参数解释：** 加密算法套件组 **约束限制：** TLS版本仅选择1.0和（或）1.1时，不支持选择强加密套件。 **取值范围：** - default: 默认加密套件 - general: 一般加密套件 - strict: 强加密套件 - custom: 自定义加密套件  **默认取值：** 不涉及

        :param cipher_suite_group: The cipher_suite_group of this HttpsTlsVersion.
        :type cipher_suite_group: str
        """
        self._cipher_suite_group = cipher_suite_group

    @property
    def cipher_suite(self):
        r"""Gets the cipher_suite of this HttpsTlsVersion.

        **参数解释：** 加密套件 **约束限制：** - 当选择自定义加密套件时，必传 - 选择多个加密套件是以“,”分隔  **取值范围：** - ECDHE-ECDSA-AES128-GCM-SHA256 - ECDHE-ECDSA-AES256-GCM-SHA384 - ECDHE-RSA-AES128-GCM-SHA256 - ECDHE-RSA-AES256-GCM-SHA384 - DHE-RSA-AES128-GCM-SHA256 - DHE-RSA-AES256-GCM-SHA384 - ECDHE-ECDSA-AES128-SHA256 - ECDHE-ECDSA-AES256-SHA384 - ECDHE-RSA-AES128-SHA - ECDHE-RSA-AES128-SHA256 - ECDHE-RSA-AES256-SHA - ECDHE-RSA-AES256-SHA384 - DHE-RSA-AES128-SHA - DHE-RSA-AES128-SHA256 - DHE-RSA-AES256-SHA - DHE-RSA-AES256-SHA256 - AES128-GCM-SHA256 - AES256-GCM-SHA384 - AES128-SHA256 - AES256-SHA256 - ECDHE-ECDSA-CHACHA20-POLY1305 - ECDHE-RSA-CHACHA20-POLY1305 - DHE-RSA-CHACHA20-POLY1305 - ECDHE-ECDSA-AES128-SHA - ECDHE-ECDSA-AES256-SHA - AES128-SHA - AES256-SHA - DES-CBC3-SHA - RC4-SHA  **默认取值：** 不涉及

        :return: The cipher_suite of this HttpsTlsVersion.
        :rtype: str
        """
        return self._cipher_suite

    @cipher_suite.setter
    def cipher_suite(self, cipher_suite):
        r"""Sets the cipher_suite of this HttpsTlsVersion.

        **参数解释：** 加密套件 **约束限制：** - 当选择自定义加密套件时，必传 - 选择多个加密套件是以“,”分隔  **取值范围：** - ECDHE-ECDSA-AES128-GCM-SHA256 - ECDHE-ECDSA-AES256-GCM-SHA384 - ECDHE-RSA-AES128-GCM-SHA256 - ECDHE-RSA-AES256-GCM-SHA384 - DHE-RSA-AES128-GCM-SHA256 - DHE-RSA-AES256-GCM-SHA384 - ECDHE-ECDSA-AES128-SHA256 - ECDHE-ECDSA-AES256-SHA384 - ECDHE-RSA-AES128-SHA - ECDHE-RSA-AES128-SHA256 - ECDHE-RSA-AES256-SHA - ECDHE-RSA-AES256-SHA384 - DHE-RSA-AES128-SHA - DHE-RSA-AES128-SHA256 - DHE-RSA-AES256-SHA - DHE-RSA-AES256-SHA256 - AES128-GCM-SHA256 - AES256-GCM-SHA384 - AES128-SHA256 - AES256-SHA256 - ECDHE-ECDSA-CHACHA20-POLY1305 - ECDHE-RSA-CHACHA20-POLY1305 - DHE-RSA-CHACHA20-POLY1305 - ECDHE-ECDSA-AES128-SHA - ECDHE-ECDSA-AES256-SHA - AES128-SHA - AES256-SHA - DES-CBC3-SHA - RC4-SHA  **默认取值：** 不涉及

        :param cipher_suite: The cipher_suite of this HttpsTlsVersion.
        :type cipher_suite: str
        """
        self._cipher_suite = cipher_suite

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
        if not isinstance(other, HttpsTlsVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
