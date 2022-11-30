# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PhoneAccessInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'device_ip': 'str',
        'phone_ip': 'str',
        'listen_port': 'int',
        'access_ip': 'str',
        'public_ip': 'str',
        'intranet_ip': 'str',
        'server_ip': 'str',
        'access_port': 'int'
    }

    attribute_map = {
        'type': 'type',
        'device_ip': 'device_ip',
        'phone_ip': 'phone_ip',
        'listen_port': 'listen_port',
        'access_ip': 'access_ip',
        'public_ip': 'public_ip',
        'intranet_ip': 'intranet_ip',
        'server_ip': 'server_ip',
        'access_port': 'access_port'
    }

    def __init__(self, type=None, device_ip=None, phone_ip=None, listen_port=None, access_ip=None, public_ip=None, intranet_ip=None, server_ip=None, access_port=None):
        """PhoneAccessInfo

        The model defined in huaweicloud sdk

        :param type: 自定义端口类型，不超过16个字节
        :type type: str
        :param device_ip: 云手机IP（过期）
        :type device_ip: str
        :param phone_ip: 云手机IP
        :type phone_ip: str
        :param listen_port: 服务监听端口
        :type listen_port: int
        :param access_ip: 云手机服务器的访问IP（过期）
        :type access_ip: str
        :param public_ip: 云手机服务器的公网IP，如果端口设置了非公网访问，该字段返回空字符串
        :type public_ip: str
        :param intranet_ip: 云手机服务器的内网IP（过期）
        :type intranet_ip: str
        :param server_ip: 云手机服务器的内网IP
        :type server_ip: str
        :param access_port: 服务映射到公网的访问端口
        :type access_port: int
        """
        
        

        self._type = None
        self._device_ip = None
        self._phone_ip = None
        self._listen_port = None
        self._access_ip = None
        self._public_ip = None
        self._intranet_ip = None
        self._server_ip = None
        self._access_port = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if device_ip is not None:
            self.device_ip = device_ip
        if phone_ip is not None:
            self.phone_ip = phone_ip
        if listen_port is not None:
            self.listen_port = listen_port
        if access_ip is not None:
            self.access_ip = access_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if intranet_ip is not None:
            self.intranet_ip = intranet_ip
        if server_ip is not None:
            self.server_ip = server_ip
        if access_port is not None:
            self.access_port = access_port

    @property
    def type(self):
        """Gets the type of this PhoneAccessInfo.

        自定义端口类型，不超过16个字节

        :return: The type of this PhoneAccessInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PhoneAccessInfo.

        自定义端口类型，不超过16个字节

        :param type: The type of this PhoneAccessInfo.
        :type type: str
        """
        self._type = type

    @property
    def device_ip(self):
        """Gets the device_ip of this PhoneAccessInfo.

        云手机IP（过期）

        :return: The device_ip of this PhoneAccessInfo.
        :rtype: str
        """
        return self._device_ip

    @device_ip.setter
    def device_ip(self, device_ip):
        """Sets the device_ip of this PhoneAccessInfo.

        云手机IP（过期）

        :param device_ip: The device_ip of this PhoneAccessInfo.
        :type device_ip: str
        """
        self._device_ip = device_ip

    @property
    def phone_ip(self):
        """Gets the phone_ip of this PhoneAccessInfo.

        云手机IP

        :return: The phone_ip of this PhoneAccessInfo.
        :rtype: str
        """
        return self._phone_ip

    @phone_ip.setter
    def phone_ip(self, phone_ip):
        """Sets the phone_ip of this PhoneAccessInfo.

        云手机IP

        :param phone_ip: The phone_ip of this PhoneAccessInfo.
        :type phone_ip: str
        """
        self._phone_ip = phone_ip

    @property
    def listen_port(self):
        """Gets the listen_port of this PhoneAccessInfo.

        服务监听端口

        :return: The listen_port of this PhoneAccessInfo.
        :rtype: int
        """
        return self._listen_port

    @listen_port.setter
    def listen_port(self, listen_port):
        """Sets the listen_port of this PhoneAccessInfo.

        服务监听端口

        :param listen_port: The listen_port of this PhoneAccessInfo.
        :type listen_port: int
        """
        self._listen_port = listen_port

    @property
    def access_ip(self):
        """Gets the access_ip of this PhoneAccessInfo.

        云手机服务器的访问IP（过期）

        :return: The access_ip of this PhoneAccessInfo.
        :rtype: str
        """
        return self._access_ip

    @access_ip.setter
    def access_ip(self, access_ip):
        """Sets the access_ip of this PhoneAccessInfo.

        云手机服务器的访问IP（过期）

        :param access_ip: The access_ip of this PhoneAccessInfo.
        :type access_ip: str
        """
        self._access_ip = access_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this PhoneAccessInfo.

        云手机服务器的公网IP，如果端口设置了非公网访问，该字段返回空字符串

        :return: The public_ip of this PhoneAccessInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this PhoneAccessInfo.

        云手机服务器的公网IP，如果端口设置了非公网访问，该字段返回空字符串

        :param public_ip: The public_ip of this PhoneAccessInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def intranet_ip(self):
        """Gets the intranet_ip of this PhoneAccessInfo.

        云手机服务器的内网IP（过期）

        :return: The intranet_ip of this PhoneAccessInfo.
        :rtype: str
        """
        return self._intranet_ip

    @intranet_ip.setter
    def intranet_ip(self, intranet_ip):
        """Sets the intranet_ip of this PhoneAccessInfo.

        云手机服务器的内网IP（过期）

        :param intranet_ip: The intranet_ip of this PhoneAccessInfo.
        :type intranet_ip: str
        """
        self._intranet_ip = intranet_ip

    @property
    def server_ip(self):
        """Gets the server_ip of this PhoneAccessInfo.

        云手机服务器的内网IP

        :return: The server_ip of this PhoneAccessInfo.
        :rtype: str
        """
        return self._server_ip

    @server_ip.setter
    def server_ip(self, server_ip):
        """Sets the server_ip of this PhoneAccessInfo.

        云手机服务器的内网IP

        :param server_ip: The server_ip of this PhoneAccessInfo.
        :type server_ip: str
        """
        self._server_ip = server_ip

    @property
    def access_port(self):
        """Gets the access_port of this PhoneAccessInfo.

        服务映射到公网的访问端口

        :return: The access_port of this PhoneAccessInfo.
        :rtype: int
        """
        return self._access_port

    @access_port.setter
    def access_port(self, access_port):
        """Sets the access_port of this PhoneAccessInfo.

        服务映射到公网的访问端口

        :param access_port: The access_port of this PhoneAccessInfo.
        :type access_port: int
        """
        self._access_port = access_port

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
        if not isinstance(other, PhoneAccessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
