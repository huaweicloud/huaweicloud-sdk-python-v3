# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Listener:

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
        'port': 'int',
        'backend': 'Backend',
        'ip_version': 'int'
    }

    attribute_map = {
        'name': 'name',
        'port': 'port',
        'backend': 'backend',
        'ip_version': 'ip_version'
    }

    def __init__(self, name=None, port=None, backend=None, ip_version=None):
        """Listener

        The model defined in huaweicloud sdk

        :param name: 监听器名称
        :type name: str
        :param port: 监听器对外提供服务端口
        :type port: int
        :param backend: 
        :type backend: :class:`huaweicloudsdkroma.v2.Backend`
        :param ip_version: 创建负载均衡器的IP协议类型
        :type ip_version: int
        """
        
        

        self._name = None
        self._port = None
        self._backend = None
        self._ip_version = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if port is not None:
            self.port = port
        if backend is not None:
            self.backend = backend
        if ip_version is not None:
            self.ip_version = ip_version

    @property
    def name(self):
        """Gets the name of this Listener.

        监听器名称

        :return: The name of this Listener.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Listener.

        监听器名称

        :param name: The name of this Listener.
        :type name: str
        """
        self._name = name

    @property
    def port(self):
        """Gets the port of this Listener.

        监听器对外提供服务端口

        :return: The port of this Listener.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Listener.

        监听器对外提供服务端口

        :param port: The port of this Listener.
        :type port: int
        """
        self._port = port

    @property
    def backend(self):
        """Gets the backend of this Listener.


        :return: The backend of this Listener.
        :rtype: :class:`huaweicloudsdkroma.v2.Backend`
        """
        return self._backend

    @backend.setter
    def backend(self, backend):
        """Sets the backend of this Listener.


        :param backend: The backend of this Listener.
        :type backend: :class:`huaweicloudsdkroma.v2.Backend`
        """
        self._backend = backend

    @property
    def ip_version(self):
        """Gets the ip_version of this Listener.

        创建负载均衡器的IP协议类型

        :return: The ip_version of this Listener.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this Listener.

        创建负载均衡器的IP协议类型

        :param ip_version: The ip_version of this Listener.
        :type ip_version: int
        """
        self._ip_version = ip_version

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
        if not isinstance(other, Listener):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
