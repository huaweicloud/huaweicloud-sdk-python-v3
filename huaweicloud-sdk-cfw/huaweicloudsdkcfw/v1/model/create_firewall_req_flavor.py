# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFirewallReqFlavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'extend_eip_count': 'int',
        'extend_bandwidth': 'int',
        'extend_vpc_count': 'int'
    }

    attribute_map = {
        'version': 'version',
        'extend_eip_count': 'extend_eip_count',
        'extend_bandwidth': 'extend_bandwidth',
        'extend_vpc_count': 'extend_vpc_count'
    }

    def __init__(self, version=None, extend_eip_count=None, extend_bandwidth=None, extend_vpc_count=None):
        r"""CreateFirewallReqFlavor

        The model defined in huaweicloud sdk

        :param version: 防火墙版本 “charge_mode”为“prePaid”时，支持标准版、专业版。 “charge_mode”为“postPaid”时，仅支持专业版。  Standard - 标准版 Professional - 专业版
        :type version: str
        :param extend_eip_count: 扩展EIP数量，仅包周期场景下生效，当用户需要在增加EIP使用时需要使用此参数。
        :type extend_eip_count: int
        :param extend_bandwidth: 扩展带宽，步长为5，仅包周期场景下生效，当用户需要在增加带宽使用时需要使用此参数。
        :type extend_bandwidth: int
        :param extend_vpc_count: 扩展VPC数量，仅包周期场景下生效，当用户需要增加VPC使用时需要使用此参数。
        :type extend_vpc_count: int
        """
        
        

        self._version = None
        self._extend_eip_count = None
        self._extend_bandwidth = None
        self._extend_vpc_count = None
        self.discriminator = None

        self.version = version
        if extend_eip_count is not None:
            self.extend_eip_count = extend_eip_count
        if extend_bandwidth is not None:
            self.extend_bandwidth = extend_bandwidth
        if extend_vpc_count is not None:
            self.extend_vpc_count = extend_vpc_count

    @property
    def version(self):
        r"""Gets the version of this CreateFirewallReqFlavor.

        防火墙版本 “charge_mode”为“prePaid”时，支持标准版、专业版。 “charge_mode”为“postPaid”时，仅支持专业版。  Standard - 标准版 Professional - 专业版

        :return: The version of this CreateFirewallReqFlavor.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateFirewallReqFlavor.

        防火墙版本 “charge_mode”为“prePaid”时，支持标准版、专业版。 “charge_mode”为“postPaid”时，仅支持专业版。  Standard - 标准版 Professional - 专业版

        :param version: The version of this CreateFirewallReqFlavor.
        :type version: str
        """
        self._version = version

    @property
    def extend_eip_count(self):
        r"""Gets the extend_eip_count of this CreateFirewallReqFlavor.

        扩展EIP数量，仅包周期场景下生效，当用户需要在增加EIP使用时需要使用此参数。

        :return: The extend_eip_count of this CreateFirewallReqFlavor.
        :rtype: int
        """
        return self._extend_eip_count

    @extend_eip_count.setter
    def extend_eip_count(self, extend_eip_count):
        r"""Sets the extend_eip_count of this CreateFirewallReqFlavor.

        扩展EIP数量，仅包周期场景下生效，当用户需要在增加EIP使用时需要使用此参数。

        :param extend_eip_count: The extend_eip_count of this CreateFirewallReqFlavor.
        :type extend_eip_count: int
        """
        self._extend_eip_count = extend_eip_count

    @property
    def extend_bandwidth(self):
        r"""Gets the extend_bandwidth of this CreateFirewallReqFlavor.

        扩展带宽，步长为5，仅包周期场景下生效，当用户需要在增加带宽使用时需要使用此参数。

        :return: The extend_bandwidth of this CreateFirewallReqFlavor.
        :rtype: int
        """
        return self._extend_bandwidth

    @extend_bandwidth.setter
    def extend_bandwidth(self, extend_bandwidth):
        r"""Sets the extend_bandwidth of this CreateFirewallReqFlavor.

        扩展带宽，步长为5，仅包周期场景下生效，当用户需要在增加带宽使用时需要使用此参数。

        :param extend_bandwidth: The extend_bandwidth of this CreateFirewallReqFlavor.
        :type extend_bandwidth: int
        """
        self._extend_bandwidth = extend_bandwidth

    @property
    def extend_vpc_count(self):
        r"""Gets the extend_vpc_count of this CreateFirewallReqFlavor.

        扩展VPC数量，仅包周期场景下生效，当用户需要增加VPC使用时需要使用此参数。

        :return: The extend_vpc_count of this CreateFirewallReqFlavor.
        :rtype: int
        """
        return self._extend_vpc_count

    @extend_vpc_count.setter
    def extend_vpc_count(self, extend_vpc_count):
        r"""Sets the extend_vpc_count of this CreateFirewallReqFlavor.

        扩展VPC数量，仅包周期场景下生效，当用户需要增加VPC使用时需要使用此参数。

        :param extend_vpc_count: The extend_vpc_count of this CreateFirewallReqFlavor.
        :type extend_vpc_count: int
        """
        self._extend_vpc_count = extend_vpc_count

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
        if not isinstance(other, CreateFirewallReqFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
