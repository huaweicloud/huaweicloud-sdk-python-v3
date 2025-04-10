# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VirtualPortResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ipv6_bandwidth_id': 'str',
        'port_id': 'str'
    }

    attribute_map = {
        'ipv6_bandwidth_id': 'ipv6_bandwidth_id',
        'port_id': 'port_id'
    }

    def __init__(self, ipv6_bandwidth_id=None, port_id=None):
        r"""VirtualPortResponse

        The model defined in huaweicloud sdk

        :param ipv6_bandwidth_id: IPv6带宽ID。
        :type ipv6_bandwidth_id: str
        :param port_id: IPv6虚拟IP或私网IP ID。
        :type port_id: str
        """
        
        

        self._ipv6_bandwidth_id = None
        self._port_id = None
        self.discriminator = None

        if ipv6_bandwidth_id is not None:
            self.ipv6_bandwidth_id = ipv6_bandwidth_id
        if port_id is not None:
            self.port_id = port_id

    @property
    def ipv6_bandwidth_id(self):
        r"""Gets the ipv6_bandwidth_id of this VirtualPortResponse.

        IPv6带宽ID。

        :return: The ipv6_bandwidth_id of this VirtualPortResponse.
        :rtype: str
        """
        return self._ipv6_bandwidth_id

    @ipv6_bandwidth_id.setter
    def ipv6_bandwidth_id(self, ipv6_bandwidth_id):
        r"""Sets the ipv6_bandwidth_id of this VirtualPortResponse.

        IPv6带宽ID。

        :param ipv6_bandwidth_id: The ipv6_bandwidth_id of this VirtualPortResponse.
        :type ipv6_bandwidth_id: str
        """
        self._ipv6_bandwidth_id = ipv6_bandwidth_id

    @property
    def port_id(self):
        r"""Gets the port_id of this VirtualPortResponse.

        IPv6虚拟IP或私网IP ID。

        :return: The port_id of this VirtualPortResponse.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this VirtualPortResponse.

        IPv6虚拟IP或私网IP ID。

        :param port_id: The port_id of this VirtualPortResponse.
        :type port_id: str
        """
        self._port_id = port_id

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
        if not isinstance(other, VirtualPortResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
