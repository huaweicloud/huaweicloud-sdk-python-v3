# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworksResult:

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
        'ipv6_bandwidth': 'Ipv6Bandwidth',
        'allowed_address_pairs': 'list[AllowedAddressPair]'
    }

    attribute_map = {
        'id': 'id',
        'ipv6_enable': 'ipv6_enable',
        'ipv6_bandwidth': 'ipv6_bandwidth',
        'allowed_address_pairs': 'allowed_address_pairs'
    }

    def __init__(self, id=None, ipv6_enable=None, ipv6_bandwidth=None, allowed_address_pairs=None):
        """NetworksResult

        The model defined in huaweicloud sdk

        :param id: 网络ID
        :type id: str
        :param ipv6_enable: 是否启用IPv6。取值为true时，标识此网卡已启用IPv6。
        :type ipv6_enable: bool
        :param ipv6_bandwidth: 
        :type ipv6_bandwidth: :class:`huaweicloudsdkas.v1.Ipv6Bandwidth`
        :param allowed_address_pairs: 是否开启源/目的检查开关。
        :type allowed_address_pairs: list[:class:`huaweicloudsdkas.v1.AllowedAddressPair`]
        """
        
        

        self._id = None
        self._ipv6_enable = None
        self._ipv6_bandwidth = None
        self._allowed_address_pairs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth
        if allowed_address_pairs is not None:
            self.allowed_address_pairs = allowed_address_pairs

    @property
    def id(self):
        """Gets the id of this NetworksResult.

        网络ID

        :return: The id of this NetworksResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NetworksResult.

        网络ID

        :param id: The id of this NetworksResult.
        :type id: str
        """
        self._id = id

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this NetworksResult.

        是否启用IPv6。取值为true时，标识此网卡已启用IPv6。

        :return: The ipv6_enable of this NetworksResult.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this NetworksResult.

        是否启用IPv6。取值为true时，标识此网卡已启用IPv6。

        :param ipv6_enable: The ipv6_enable of this NetworksResult.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def ipv6_bandwidth(self):
        """Gets the ipv6_bandwidth of this NetworksResult.

        :return: The ipv6_bandwidth of this NetworksResult.
        :rtype: :class:`huaweicloudsdkas.v1.Ipv6Bandwidth`
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        """Sets the ipv6_bandwidth of this NetworksResult.

        :param ipv6_bandwidth: The ipv6_bandwidth of this NetworksResult.
        :type ipv6_bandwidth: :class:`huaweicloudsdkas.v1.Ipv6Bandwidth`
        """
        self._ipv6_bandwidth = ipv6_bandwidth

    @property
    def allowed_address_pairs(self):
        """Gets the allowed_address_pairs of this NetworksResult.

        是否开启源/目的检查开关。

        :return: The allowed_address_pairs of this NetworksResult.
        :rtype: list[:class:`huaweicloudsdkas.v1.AllowedAddressPair`]
        """
        return self._allowed_address_pairs

    @allowed_address_pairs.setter
    def allowed_address_pairs(self, allowed_address_pairs):
        """Sets the allowed_address_pairs of this NetworksResult.

        是否开启源/目的检查开关。

        :param allowed_address_pairs: The allowed_address_pairs of this NetworksResult.
        :type allowed_address_pairs: list[:class:`huaweicloudsdkas.v1.AllowedAddressPair`]
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
        if not isinstance(other, NetworksResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
