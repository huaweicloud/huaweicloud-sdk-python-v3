# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PortRange:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'from_port': 'int',
        'to_port': 'int'
    }

    attribute_map = {
        'from_port': 'from_port',
        'to_port': 'to_port'
    }

    def __init__(self, from_port=None, to_port=None):
        """PortRange

        The model defined in huaweicloud sdk

        :param from_port: 起始端口。
        :type from_port: int
        :param to_port: 结束端口。
        :type to_port: int
        """
        
        

        self._from_port = None
        self._to_port = None
        self.discriminator = None

        self.from_port = from_port
        self.to_port = to_port

    @property
    def from_port(self):
        """Gets the from_port of this PortRange.

        起始端口。

        :return: The from_port of this PortRange.
        :rtype: int
        """
        return self._from_port

    @from_port.setter
    def from_port(self, from_port):
        """Sets the from_port of this PortRange.

        起始端口。

        :param from_port: The from_port of this PortRange.
        :type from_port: int
        """
        self._from_port = from_port

    @property
    def to_port(self):
        """Gets the to_port of this PortRange.

        结束端口。

        :return: The to_port of this PortRange.
        :rtype: int
        """
        return self._to_port

    @to_port.setter
    def to_port(self, to_port):
        """Sets the to_port of this PortRange.

        结束端口。

        :param to_port: The to_port of this PortRange.
        :type to_port: int
        """
        self._to_port = to_port

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
        if not isinstance(other, PortRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
