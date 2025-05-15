# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandwidthPackageLineSpecCode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'level': 'str',
        'name_cn': 'str',
        'name_en': 'str',
        'spec_code': 'str',
        'max_bandwidth': 'int',
        'min_bandwidth': 'int',
        'support_billing_modes': 'list[BillingModeEnum]'
    }

    attribute_map = {
        'level': 'level',
        'name_cn': 'name_cn',
        'name_en': 'name_en',
        'spec_code': 'spec_code',
        'max_bandwidth': 'max_bandwidth',
        'min_bandwidth': 'min_bandwidth',
        'support_billing_modes': 'support_billing_modes'
    }

    def __init__(self, level=None, name_cn=None, name_en=None, spec_code=None, max_bandwidth=None, min_bandwidth=None, support_billing_modes=None):
        r"""BandwidthPackageLineSpecCode

        The model defined in huaweicloud sdk

        :param level: 带宽包等级。
        :type level: str
        :param name_cn: 实例名称。
        :type name_cn: str
        :param name_en: 实例名称。
        :type name_en: str
        :param spec_code: 带宽包实例的规格编码。
        :type spec_code: str
        :param max_bandwidth: 最大带宽。
        :type max_bandwidth: int
        :param min_bandwidth: 最小带宽。
        :type min_bandwidth: int
        :param support_billing_modes: 支持的计费模式。
        :type support_billing_modes: list[:class:`huaweicloudsdkcc.v3.BillingModeEnum`]
        """
        
        

        self._level = None
        self._name_cn = None
        self._name_en = None
        self._spec_code = None
        self._max_bandwidth = None
        self._min_bandwidth = None
        self._support_billing_modes = None
        self.discriminator = None

        if level is not None:
            self.level = level
        if name_cn is not None:
            self.name_cn = name_cn
        if name_en is not None:
            self.name_en = name_en
        if spec_code is not None:
            self.spec_code = spec_code
        if max_bandwidth is not None:
            self.max_bandwidth = max_bandwidth
        if min_bandwidth is not None:
            self.min_bandwidth = min_bandwidth
        if support_billing_modes is not None:
            self.support_billing_modes = support_billing_modes

    @property
    def level(self):
        r"""Gets the level of this BandwidthPackageLineSpecCode.

        带宽包等级。

        :return: The level of this BandwidthPackageLineSpecCode.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this BandwidthPackageLineSpecCode.

        带宽包等级。

        :param level: The level of this BandwidthPackageLineSpecCode.
        :type level: str
        """
        self._level = level

    @property
    def name_cn(self):
        r"""Gets the name_cn of this BandwidthPackageLineSpecCode.

        实例名称。

        :return: The name_cn of this BandwidthPackageLineSpecCode.
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        r"""Sets the name_cn of this BandwidthPackageLineSpecCode.

        实例名称。

        :param name_cn: The name_cn of this BandwidthPackageLineSpecCode.
        :type name_cn: str
        """
        self._name_cn = name_cn

    @property
    def name_en(self):
        r"""Gets the name_en of this BandwidthPackageLineSpecCode.

        实例名称。

        :return: The name_en of this BandwidthPackageLineSpecCode.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this BandwidthPackageLineSpecCode.

        实例名称。

        :param name_en: The name_en of this BandwidthPackageLineSpecCode.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def spec_code(self):
        r"""Gets the spec_code of this BandwidthPackageLineSpecCode.

        带宽包实例的规格编码。

        :return: The spec_code of this BandwidthPackageLineSpecCode.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this BandwidthPackageLineSpecCode.

        带宽包实例的规格编码。

        :param spec_code: The spec_code of this BandwidthPackageLineSpecCode.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def max_bandwidth(self):
        r"""Gets the max_bandwidth of this BandwidthPackageLineSpecCode.

        最大带宽。

        :return: The max_bandwidth of this BandwidthPackageLineSpecCode.
        :rtype: int
        """
        return self._max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        r"""Sets the max_bandwidth of this BandwidthPackageLineSpecCode.

        最大带宽。

        :param max_bandwidth: The max_bandwidth of this BandwidthPackageLineSpecCode.
        :type max_bandwidth: int
        """
        self._max_bandwidth = max_bandwidth

    @property
    def min_bandwidth(self):
        r"""Gets the min_bandwidth of this BandwidthPackageLineSpecCode.

        最小带宽。

        :return: The min_bandwidth of this BandwidthPackageLineSpecCode.
        :rtype: int
        """
        return self._min_bandwidth

    @min_bandwidth.setter
    def min_bandwidth(self, min_bandwidth):
        r"""Sets the min_bandwidth of this BandwidthPackageLineSpecCode.

        最小带宽。

        :param min_bandwidth: The min_bandwidth of this BandwidthPackageLineSpecCode.
        :type min_bandwidth: int
        """
        self._min_bandwidth = min_bandwidth

    @property
    def support_billing_modes(self):
        r"""Gets the support_billing_modes of this BandwidthPackageLineSpecCode.

        支持的计费模式。

        :return: The support_billing_modes of this BandwidthPackageLineSpecCode.
        :rtype: list[:class:`huaweicloudsdkcc.v3.BillingModeEnum`]
        """
        return self._support_billing_modes

    @support_billing_modes.setter
    def support_billing_modes(self, support_billing_modes):
        r"""Sets the support_billing_modes of this BandwidthPackageLineSpecCode.

        支持的计费模式。

        :param support_billing_modes: The support_billing_modes of this BandwidthPackageLineSpecCode.
        :type support_billing_modes: list[:class:`huaweicloudsdkcc.v3.BillingModeEnum`]
        """
        self._support_billing_modes = support_billing_modes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BandwidthPackageLineSpecCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
