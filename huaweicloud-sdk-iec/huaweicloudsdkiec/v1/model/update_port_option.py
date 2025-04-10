# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePortOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'allowed_address_pairs': 'list[AllowedAddressPair]',
        'security_groups': 'list[str]'
    }

    attribute_map = {
        'allowed_address_pairs': 'allowed_address_pairs',
        'security_groups': 'security_groups'
    }

    def __init__(self, allowed_address_pairs=None, security_groups=None):
        r"""UpdatePortOption

        The model defined in huaweicloud sdk

        :param allowed_address_pairs: - 功能说明：IP/Mac对列表 - 约束：     IP地址不允许为 “0.0.0.0/0”     如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。     如果allowed_address_pairs为“1.1.1.1/0”，表示关闭源目地址检查开关     为虚拟IP配置后端边缘实例场景，       allowed_address_pairs中配置的IP地址，必须为边缘实例网卡已有的IP地址，否则可能会导致虚拟IP通信异常。       被绑定的边缘实例网卡allowed_address_pairs填“1.1.1.1/0”
        :type allowed_address_pairs: list[:class:`huaweicloudsdkiec.v1.AllowedAddressPair`]
        :param security_groups: 安全组列表
        :type security_groups: list[str]
        """
        
        

        self._allowed_address_pairs = None
        self._security_groups = None
        self.discriminator = None

        if allowed_address_pairs is not None:
            self.allowed_address_pairs = allowed_address_pairs
        if security_groups is not None:
            self.security_groups = security_groups

    @property
    def allowed_address_pairs(self):
        r"""Gets the allowed_address_pairs of this UpdatePortOption.

        - 功能说明：IP/Mac对列表 - 约束：     IP地址不允许为 “0.0.0.0/0”     如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。     如果allowed_address_pairs为“1.1.1.1/0”，表示关闭源目地址检查开关     为虚拟IP配置后端边缘实例场景，       allowed_address_pairs中配置的IP地址，必须为边缘实例网卡已有的IP地址，否则可能会导致虚拟IP通信异常。       被绑定的边缘实例网卡allowed_address_pairs填“1.1.1.1/0”

        :return: The allowed_address_pairs of this UpdatePortOption.
        :rtype: list[:class:`huaweicloudsdkiec.v1.AllowedAddressPair`]
        """
        return self._allowed_address_pairs

    @allowed_address_pairs.setter
    def allowed_address_pairs(self, allowed_address_pairs):
        r"""Sets the allowed_address_pairs of this UpdatePortOption.

        - 功能说明：IP/Mac对列表 - 约束：     IP地址不允许为 “0.0.0.0/0”     如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。     如果allowed_address_pairs为“1.1.1.1/0”，表示关闭源目地址检查开关     为虚拟IP配置后端边缘实例场景，       allowed_address_pairs中配置的IP地址，必须为边缘实例网卡已有的IP地址，否则可能会导致虚拟IP通信异常。       被绑定的边缘实例网卡allowed_address_pairs填“1.1.1.1/0”

        :param allowed_address_pairs: The allowed_address_pairs of this UpdatePortOption.
        :type allowed_address_pairs: list[:class:`huaweicloudsdkiec.v1.AllowedAddressPair`]
        """
        self._allowed_address_pairs = allowed_address_pairs

    @property
    def security_groups(self):
        r"""Gets the security_groups of this UpdatePortOption.

        安全组列表

        :return: The security_groups of this UpdatePortOption.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this UpdatePortOption.

        安全组列表

        :param security_groups: The security_groups of this UpdatePortOption.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

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
        if not isinstance(other, UpdatePortOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
