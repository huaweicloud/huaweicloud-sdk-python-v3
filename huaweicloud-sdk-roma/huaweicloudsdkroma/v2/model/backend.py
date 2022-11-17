# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Backend:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip': 'list[str]',
        'port': 'int',
        'health_check': 'HealthCheck'
    }

    attribute_map = {
        'ip': 'ip',
        'port': 'port',
        'health_check': 'health_check'
    }

    def __init__(self, ip=None, port=None, health_check=None):
        """Backend

        The model defined in huaweicloud sdk

        :param ip: 后端主机地址列表
        :type ip: list[str]
        :param port: 后端服务端口，不存在时使用监听器端口
        :type port: int
        :param health_check: 
        :type health_check: :class:`huaweicloudsdkroma.v2.HealthCheck`
        """
        
        

        self._ip = None
        self._port = None
        self._health_check = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port
        if health_check is not None:
            self.health_check = health_check

    @property
    def ip(self):
        """Gets the ip of this Backend.

        后端主机地址列表

        :return: The ip of this Backend.
        :rtype: list[str]
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Backend.

        后端主机地址列表

        :param ip: The ip of this Backend.
        :type ip: list[str]
        """
        self._ip = ip

    @property
    def port(self):
        """Gets the port of this Backend.

        后端服务端口，不存在时使用监听器端口

        :return: The port of this Backend.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Backend.

        后端服务端口，不存在时使用监听器端口

        :param port: The port of this Backend.
        :type port: int
        """
        self._port = port

    @property
    def health_check(self):
        """Gets the health_check of this Backend.

        :return: The health_check of this Backend.
        :rtype: :class:`huaweicloudsdkroma.v2.HealthCheck`
        """
        return self._health_check

    @health_check.setter
    def health_check(self, health_check):
        """Sets the health_check of this Backend.

        :param health_check: The health_check of this Backend.
        :type health_check: :class:`huaweicloudsdkroma.v2.HealthCheck`
        """
        self._health_check = health_check

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
        if not isinstance(other, Backend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
