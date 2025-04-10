# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyDetailsPortList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'int',
        'protocol': 'str'
    }

    attribute_map = {
        'port': 'port',
        'protocol': 'protocol'
    }

    def __init__(self, port=None, protocol=None):
        r"""PolicyDetailsPortList

        The model defined in huaweicloud sdk

        :param port: 端口
        :type port: int
        :param protocol: 协议类型 - \&quot;tcp\&quot; - \&quot;tcp6\&quot;
        :type protocol: str
        """
        
        

        self._port = None
        self._protocol = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol

    @property
    def port(self):
        r"""Gets the port of this PolicyDetailsPortList.

        端口

        :return: The port of this PolicyDetailsPortList.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this PolicyDetailsPortList.

        端口

        :param port: The port of this PolicyDetailsPortList.
        :type port: int
        """
        self._port = port

    @property
    def protocol(self):
        r"""Gets the protocol of this PolicyDetailsPortList.

        协议类型 - \"tcp\" - \"tcp6\"

        :return: The protocol of this PolicyDetailsPortList.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this PolicyDetailsPortList.

        协议类型 - \"tcp\" - \"tcp6\"

        :param protocol: The protocol of this PolicyDetailsPortList.
        :type protocol: str
        """
        self._protocol = protocol

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
        if not isinstance(other, PolicyDetailsPortList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
