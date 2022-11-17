# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartConnectivityTestReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'address_and_ports': 'list[AddressAndPorts]'
    }

    attribute_map = {
        'address_and_ports': 'addressAndPorts'
    }

    def __init__(self, address_and_ports=None):
        """StartConnectivityTestReq

        The model defined in huaweicloud sdk

        :param address_and_ports: 地址和端口列表。
        :type address_and_ports: list[:class:`huaweicloudsdkcss.v1.AddressAndPorts`]
        """
        
        

        self._address_and_ports = None
        self.discriminator = None

        self.address_and_ports = address_and_ports

    @property
    def address_and_ports(self):
        """Gets the address_and_ports of this StartConnectivityTestReq.

        地址和端口列表。

        :return: The address_and_ports of this StartConnectivityTestReq.
        :rtype: list[:class:`huaweicloudsdkcss.v1.AddressAndPorts`]
        """
        return self._address_and_ports

    @address_and_ports.setter
    def address_and_ports(self, address_and_ports):
        """Sets the address_and_ports of this StartConnectivityTestReq.

        地址和端口列表。

        :param address_and_ports: The address_and_ports of this StartConnectivityTestReq.
        :type address_and_ports: list[:class:`huaweicloudsdkcss.v1.AddressAndPorts`]
        """
        self._address_and_ports = address_and_ports

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
        if not isinstance(other, StartConnectivityTestReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
