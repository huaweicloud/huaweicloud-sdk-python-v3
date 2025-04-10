# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AllowAddressNetmask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'address_netmask': 'str',
        'description': 'str'
    }

    attribute_map = {
        'address_netmask': 'address_netmask',
        'description': 'description'
    }

    def __init__(self, address_netmask=None, description=None):
        r"""AllowAddressNetmask

        The model defined in huaweicloud sdk

        :param address_netmask: IP地址或网段，例如\&quot;192.168.0.1/24\&quot;。
        :type address_netmask: str
        :param description: 描述信息，不能包含特定字符\&quot;@\&quot;、\&quot;#\&quot;、\&quot;%\&quot;、\&quot;&amp;\&quot;、\&quot;&lt;\&quot;、\&quot;&gt;\&quot;、\&quot;\\\\\&quot;、\&quot;$\&quot;、\&quot;^\&quot;和\&quot;*\&quot;的字符串。
        :type description: str
        """
        
        

        self._address_netmask = None
        self._description = None
        self.discriminator = None

        self.address_netmask = address_netmask
        if description is not None:
            self.description = description

    @property
    def address_netmask(self):
        r"""Gets the address_netmask of this AllowAddressNetmask.

        IP地址或网段，例如\"192.168.0.1/24\"。

        :return: The address_netmask of this AllowAddressNetmask.
        :rtype: str
        """
        return self._address_netmask

    @address_netmask.setter
    def address_netmask(self, address_netmask):
        r"""Sets the address_netmask of this AllowAddressNetmask.

        IP地址或网段，例如\"192.168.0.1/24\"。

        :param address_netmask: The address_netmask of this AllowAddressNetmask.
        :type address_netmask: str
        """
        self._address_netmask = address_netmask

    @property
    def description(self):
        r"""Gets the description of this AllowAddressNetmask.

        描述信息，不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\\\"、\"$\"、\"^\"和\"*\"的字符串。

        :return: The description of this AllowAddressNetmask.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AllowAddressNetmask.

        描述信息，不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\\\"、\"$\"、\"^\"和\"*\"的字符串。

        :param description: The description of this AllowAddressNetmask.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, AllowAddressNetmask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
