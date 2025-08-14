# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServicePortInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desc': 'str',
        'type': 'str',
        'protocol': 'str',
        'user_port': 'int',
        'port': 'int'
    }

    attribute_map = {
        'desc': 'desc',
        'type': 'type',
        'protocol': 'protocol',
        'user_port': 'user_port',
        'port': 'port'
    }

    def __init__(self, desc=None, type=None, protocol=None, user_port=None, port=None):
        r"""ServicePortInfo

        The model defined in huaweicloud sdk

        :param desc: 服务名称
        :type desc: str
        :param type: 类型，可取值集合[http，https]
        :type type: str
        :param protocol: 默认tcp。可取值集合[tcp，udp]
        :type protocol: str
        :param user_port: 用户端口
        :type user_port: int
        :param port: 容器内部端口
        :type port: int
        """
        
        

        self._desc = None
        self._type = None
        self._protocol = None
        self._user_port = None
        self._port = None
        self.discriminator = None

        self.desc = desc
        if type is not None:
            self.type = type
        self.protocol = protocol
        if user_port is not None:
            self.user_port = user_port
        self.port = port

    @property
    def desc(self):
        r"""Gets the desc of this ServicePortInfo.

        服务名称

        :return: The desc of this ServicePortInfo.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this ServicePortInfo.

        服务名称

        :param desc: The desc of this ServicePortInfo.
        :type desc: str
        """
        self._desc = desc

    @property
    def type(self):
        r"""Gets the type of this ServicePortInfo.

        类型，可取值集合[http，https]

        :return: The type of this ServicePortInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ServicePortInfo.

        类型，可取值集合[http，https]

        :param type: The type of this ServicePortInfo.
        :type type: str
        """
        self._type = type

    @property
    def protocol(self):
        r"""Gets the protocol of this ServicePortInfo.

        默认tcp。可取值集合[tcp，udp]

        :return: The protocol of this ServicePortInfo.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ServicePortInfo.

        默认tcp。可取值集合[tcp，udp]

        :param protocol: The protocol of this ServicePortInfo.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def user_port(self):
        r"""Gets the user_port of this ServicePortInfo.

        用户端口

        :return: The user_port of this ServicePortInfo.
        :rtype: int
        """
        return self._user_port

    @user_port.setter
    def user_port(self, user_port):
        r"""Sets the user_port of this ServicePortInfo.

        用户端口

        :param user_port: The user_port of this ServicePortInfo.
        :type user_port: int
        """
        self._user_port = user_port

    @property
    def port(self):
        r"""Gets the port of this ServicePortInfo.

        容器内部端口

        :return: The port of this ServicePortInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ServicePortInfo.

        容器内部端口

        :param port: The port of this ServicePortInfo.
        :type port: int
        """
        self._port = port

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
        if not isinstance(other, ServicePortInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
