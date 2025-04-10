# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnhancedConnectionHost:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'name': 'name',
        'ip': 'ip'
    }

    def __init__(self, name=None, ip=None):
        r"""EnhancedConnectionHost

        The model defined in huaweicloud sdk

        :param name: 自定义主机名称。长度128，数字字母下划线(\&quot;_\&quot;)横杠(\&quot;-\&quot;)句点(\&quot;.\&quot;)组成，字母开头。
        :type name: str
        :param ip: 主机对应的IPv4地址。
        :type ip: str
        """
        
        

        self._name = None
        self._ip = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if ip is not None:
            self.ip = ip

    @property
    def name(self):
        r"""Gets the name of this EnhancedConnectionHost.

        自定义主机名称。长度128，数字字母下划线(\"_\")横杠(\"-\")句点(\".\")组成，字母开头。

        :return: The name of this EnhancedConnectionHost.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EnhancedConnectionHost.

        自定义主机名称。长度128，数字字母下划线(\"_\")横杠(\"-\")句点(\".\")组成，字母开头。

        :param name: The name of this EnhancedConnectionHost.
        :type name: str
        """
        self._name = name

    @property
    def ip(self):
        r"""Gets the ip of this EnhancedConnectionHost.

        主机对应的IPv4地址。

        :return: The ip of this EnhancedConnectionHost.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this EnhancedConnectionHost.

        主机对应的IPv4地址。

        :param ip: The ip of this EnhancedConnectionHost.
        :type ip: str
        """
        self._ip = ip

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
        if not isinstance(other, EnhancedConnectionHost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
