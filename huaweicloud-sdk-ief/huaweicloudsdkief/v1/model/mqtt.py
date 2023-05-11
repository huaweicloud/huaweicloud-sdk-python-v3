# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Mqtt:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bind_addr': 'str',
        'port': 'int',
        'type': 'str'
    }

    attribute_map = {
        'bind_addr': 'bind_addr',
        'port': 'port',
        'type': 'type'
    }

    def __init__(self, bind_addr=None, port=None, type=None):
        """Mqtt

        The model defined in huaweicloud sdk

        :param bind_addr: MQTT监听地址，根据type取值确定。
        :type bind_addr: str
        :param port: 端口号。
        :type port: int
        :param type: 类型。枚举值： - nic：网卡类型 - ip：IP类型
        :type type: str
        """
        
        

        self._bind_addr = None
        self._port = None
        self._type = None
        self.discriminator = None

        self.bind_addr = bind_addr
        self.port = port
        self.type = type

    @property
    def bind_addr(self):
        """Gets the bind_addr of this Mqtt.

        MQTT监听地址，根据type取值确定。

        :return: The bind_addr of this Mqtt.
        :rtype: str
        """
        return self._bind_addr

    @bind_addr.setter
    def bind_addr(self, bind_addr):
        """Sets the bind_addr of this Mqtt.

        MQTT监听地址，根据type取值确定。

        :param bind_addr: The bind_addr of this Mqtt.
        :type bind_addr: str
        """
        self._bind_addr = bind_addr

    @property
    def port(self):
        """Gets the port of this Mqtt.

        端口号。

        :return: The port of this Mqtt.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Mqtt.

        端口号。

        :param port: The port of this Mqtt.
        :type port: int
        """
        self._port = port

    @property
    def type(self):
        """Gets the type of this Mqtt.

        类型。枚举值： - nic：网卡类型 - ip：IP类型

        :return: The type of this Mqtt.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Mqtt.

        类型。枚举值： - nic：网卡类型 - ip：IP类型

        :param type: The type of this Mqtt.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, Mqtt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
