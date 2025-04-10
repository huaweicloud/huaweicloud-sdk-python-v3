# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubnetConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'ipv6_enable': 'bool',
        'ipv6_bandwidth_enable': 'bool',
        'ipv6_bandwidth': 'Ipv6Bandwidth',
        'allowed_address_pairs': 'list[AllowedAddressPair]'
    }

    attribute_map = {
        'id': 'id',
        'ipv6_enable': 'ipv6_enable',
        'ipv6_bandwidth_enable': 'ipv6_bandwidth_enable',
        'ipv6_bandwidth': 'ipv6_bandwidth',
        'allowed_address_pairs': 'allowed_address_pairs'
    }

    def __init__(self, id=None, ipv6_enable=None, ipv6_bandwidth_enable=None, ipv6_bandwidth=None, allowed_address_pairs=None):
        r"""SubnetConfig

        The model defined in huaweicloud sdk

        :param id: 边缘子网ID。
        :type id: str
        :param ipv6_enable: 创建实例是否开启IPv6能力。
        :type ipv6_enable: bool
        :param ipv6_bandwidth_enable: 是否使用IPv6带宽。  约束： - ipv6_enable&#x3D;true时，有效； - 使用IPv6带宽后，优先根据ipv6_bandwidth中配置的带宽，如果ipv6_bandwidth未设置，则使用使用IPv6子网所在Ipv6池的带宽,如果当前IPv6所在池子下面没有带宽，则自动创建带宽
        :type ipv6_bandwidth_enable: bool
        :param ipv6_bandwidth: 
        :type ipv6_bandwidth: :class:`huaweicloudsdkiec.v1.Ipv6Bandwidth`
        :param allowed_address_pairs: - 功能说明：IP/Mac对列表 - 约束：     IP地址不允许为 “0.0.0.0/0”     如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。     如果allowed_address_pairs为“1.1.1.1/0”，表示关闭源目地址检查开关
        :type allowed_address_pairs: list[:class:`huaweicloudsdkiec.v1.AllowedAddressPair`]
        """
        
        

        self._id = None
        self._ipv6_enable = None
        self._ipv6_bandwidth_enable = None
        self._ipv6_bandwidth = None
        self._allowed_address_pairs = None
        self.discriminator = None

        self.id = id
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if ipv6_bandwidth_enable is not None:
            self.ipv6_bandwidth_enable = ipv6_bandwidth_enable
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth
        if allowed_address_pairs is not None:
            self.allowed_address_pairs = allowed_address_pairs

    @property
    def id(self):
        r"""Gets the id of this SubnetConfig.

        边缘子网ID。

        :return: The id of this SubnetConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SubnetConfig.

        边缘子网ID。

        :param id: The id of this SubnetConfig.
        :type id: str
        """
        self._id = id

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this SubnetConfig.

        创建实例是否开启IPv6能力。

        :return: The ipv6_enable of this SubnetConfig.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this SubnetConfig.

        创建实例是否开启IPv6能力。

        :param ipv6_enable: The ipv6_enable of this SubnetConfig.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def ipv6_bandwidth_enable(self):
        r"""Gets the ipv6_bandwidth_enable of this SubnetConfig.

        是否使用IPv6带宽。  约束： - ipv6_enable=true时，有效； - 使用IPv6带宽后，优先根据ipv6_bandwidth中配置的带宽，如果ipv6_bandwidth未设置，则使用使用IPv6子网所在Ipv6池的带宽,如果当前IPv6所在池子下面没有带宽，则自动创建带宽

        :return: The ipv6_bandwidth_enable of this SubnetConfig.
        :rtype: bool
        """
        return self._ipv6_bandwidth_enable

    @ipv6_bandwidth_enable.setter
    def ipv6_bandwidth_enable(self, ipv6_bandwidth_enable):
        r"""Sets the ipv6_bandwidth_enable of this SubnetConfig.

        是否使用IPv6带宽。  约束： - ipv6_enable=true时，有效； - 使用IPv6带宽后，优先根据ipv6_bandwidth中配置的带宽，如果ipv6_bandwidth未设置，则使用使用IPv6子网所在Ipv6池的带宽,如果当前IPv6所在池子下面没有带宽，则自动创建带宽

        :param ipv6_bandwidth_enable: The ipv6_bandwidth_enable of this SubnetConfig.
        :type ipv6_bandwidth_enable: bool
        """
        self._ipv6_bandwidth_enable = ipv6_bandwidth_enable

    @property
    def ipv6_bandwidth(self):
        r"""Gets the ipv6_bandwidth of this SubnetConfig.

        :return: The ipv6_bandwidth of this SubnetConfig.
        :rtype: :class:`huaweicloudsdkiec.v1.Ipv6Bandwidth`
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        r"""Sets the ipv6_bandwidth of this SubnetConfig.

        :param ipv6_bandwidth: The ipv6_bandwidth of this SubnetConfig.
        :type ipv6_bandwidth: :class:`huaweicloudsdkiec.v1.Ipv6Bandwidth`
        """
        self._ipv6_bandwidth = ipv6_bandwidth

    @property
    def allowed_address_pairs(self):
        r"""Gets the allowed_address_pairs of this SubnetConfig.

        - 功能说明：IP/Mac对列表 - 约束：     IP地址不允许为 “0.0.0.0/0”     如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。     如果allowed_address_pairs为“1.1.1.1/0”，表示关闭源目地址检查开关

        :return: The allowed_address_pairs of this SubnetConfig.
        :rtype: list[:class:`huaweicloudsdkiec.v1.AllowedAddressPair`]
        """
        return self._allowed_address_pairs

    @allowed_address_pairs.setter
    def allowed_address_pairs(self, allowed_address_pairs):
        r"""Sets the allowed_address_pairs of this SubnetConfig.

        - 功能说明：IP/Mac对列表 - 约束：     IP地址不允许为 “0.0.0.0/0”     如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。     如果allowed_address_pairs为“1.1.1.1/0”，表示关闭源目地址检查开关

        :param allowed_address_pairs: The allowed_address_pairs of this SubnetConfig.
        :type allowed_address_pairs: list[:class:`huaweicloudsdkiec.v1.AllowedAddressPair`]
        """
        self._allowed_address_pairs = allowed_address_pairs

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
        if not isinstance(other, SubnetConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
