# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostPortRange:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_port': 'int',
        'min_port': 'int'
    }

    attribute_map = {
        'max_port': 'max_port',
        'min_port': 'min_port'
    }

    def __init__(self, max_port=None, min_port=None):
        """HostPortRange

        The model defined in huaweicloud sdk

        :param max_port: 主机端口上限值,1到65535之间的整数；max_port需大于min_port
        :type max_port: int
        :param min_port: 主机端口下限制,1到65535之间的整数
        :type min_port: int
        """
        
        

        self._max_port = None
        self._min_port = None
        self.discriminator = None

        self.max_port = max_port
        self.min_port = min_port

    @property
    def max_port(self):
        """Gets the max_port of this HostPortRange.

        主机端口上限值,1到65535之间的整数；max_port需大于min_port

        :return: The max_port of this HostPortRange.
        :rtype: int
        """
        return self._max_port

    @max_port.setter
    def max_port(self, max_port):
        """Sets the max_port of this HostPortRange.

        主机端口上限值,1到65535之间的整数；max_port需大于min_port

        :param max_port: The max_port of this HostPortRange.
        :type max_port: int
        """
        self._max_port = max_port

    @property
    def min_port(self):
        """Gets the min_port of this HostPortRange.

        主机端口下限制,1到65535之间的整数

        :return: The min_port of this HostPortRange.
        :rtype: int
        """
        return self._min_port

    @min_port.setter
    def min_port(self, min_port):
        """Sets the min_port of this HostPortRange.

        主机端口下限制,1到65535之间的整数

        :param min_port: The min_port of this HostPortRange.
        :type min_port: int
        """
        self._min_port = min_port

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
        if not isinstance(other, HostPortRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
