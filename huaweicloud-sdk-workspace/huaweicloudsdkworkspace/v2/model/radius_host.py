# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RadiusHost:

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
        'radius_ip': 'str',
        'auth_port': 'int',
        'accept_port': 'int',
        'nas_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'radius_ip': 'radius_ip',
        'auth_port': 'auth_port',
        'accept_port': 'accept_port',
        'nas_id': 'nas_id'
    }

    def __init__(self, name=None, radius_ip=None, auth_port=None, accept_port=None, nas_id=None):
        """RadiusHost

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param radius_ip: IP地址
        :type radius_ip: str
        :param auth_port: 认证端口
        :type auth_port: int
        :param accept_port: 接收端口
        :type accept_port: int
        :param nas_id: NAS ID
        :type nas_id: str
        """
        
        

        self._name = None
        self._radius_ip = None
        self._auth_port = None
        self._accept_port = None
        self._nas_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if radius_ip is not None:
            self.radius_ip = radius_ip
        if auth_port is not None:
            self.auth_port = auth_port
        if accept_port is not None:
            self.accept_port = accept_port
        if nas_id is not None:
            self.nas_id = nas_id

    @property
    def name(self):
        """Gets the name of this RadiusHost.

        名称

        :return: The name of this RadiusHost.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RadiusHost.

        名称

        :param name: The name of this RadiusHost.
        :type name: str
        """
        self._name = name

    @property
    def radius_ip(self):
        """Gets the radius_ip of this RadiusHost.

        IP地址

        :return: The radius_ip of this RadiusHost.
        :rtype: str
        """
        return self._radius_ip

    @radius_ip.setter
    def radius_ip(self, radius_ip):
        """Sets the radius_ip of this RadiusHost.

        IP地址

        :param radius_ip: The radius_ip of this RadiusHost.
        :type radius_ip: str
        """
        self._radius_ip = radius_ip

    @property
    def auth_port(self):
        """Gets the auth_port of this RadiusHost.

        认证端口

        :return: The auth_port of this RadiusHost.
        :rtype: int
        """
        return self._auth_port

    @auth_port.setter
    def auth_port(self, auth_port):
        """Sets the auth_port of this RadiusHost.

        认证端口

        :param auth_port: The auth_port of this RadiusHost.
        :type auth_port: int
        """
        self._auth_port = auth_port

    @property
    def accept_port(self):
        """Gets the accept_port of this RadiusHost.

        接收端口

        :return: The accept_port of this RadiusHost.
        :rtype: int
        """
        return self._accept_port

    @accept_port.setter
    def accept_port(self, accept_port):
        """Sets the accept_port of this RadiusHost.

        接收端口

        :param accept_port: The accept_port of this RadiusHost.
        :type accept_port: int
        """
        self._accept_port = accept_port

    @property
    def nas_id(self):
        """Gets the nas_id of this RadiusHost.

        NAS ID

        :return: The nas_id of this RadiusHost.
        :rtype: str
        """
        return self._nas_id

    @nas_id.setter
    def nas_id(self, nas_id):
        """Sets the nas_id of this RadiusHost.

        NAS ID

        :param nas_id: The nas_id of this RadiusHost.
        :type nas_id: str
        """
        self._nas_id = nas_id

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
        if not isinstance(other, RadiusHost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
