# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthCheckConfigurationHttpGet:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'port': 'int',
        'scheme': 'str'
    }

    attribute_map = {
        'path': 'path',
        'port': 'port',
        'scheme': 'scheme'
    }

    def __init__(self, path=None, port=None, scheme=None):
        """HealthCheckConfigurationHttpGet

        The model defined in huaweicloud sdk

        :param path: URL路径。
        :type path: str
        :param port: 端口。
        :type port: int
        :param scheme: 协议。
        :type scheme: str
        """
        
        

        self._path = None
        self._port = None
        self._scheme = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if port is not None:
            self.port = port
        if scheme is not None:
            self.scheme = scheme

    @property
    def path(self):
        """Gets the path of this HealthCheckConfigurationHttpGet.

        URL路径。

        :return: The path of this HealthCheckConfigurationHttpGet.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this HealthCheckConfigurationHttpGet.

        URL路径。

        :param path: The path of this HealthCheckConfigurationHttpGet.
        :type path: str
        """
        self._path = path

    @property
    def port(self):
        """Gets the port of this HealthCheckConfigurationHttpGet.

        端口。

        :return: The port of this HealthCheckConfigurationHttpGet.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this HealthCheckConfigurationHttpGet.

        端口。

        :param port: The port of this HealthCheckConfigurationHttpGet.
        :type port: int
        """
        self._port = port

    @property
    def scheme(self):
        """Gets the scheme of this HealthCheckConfigurationHttpGet.

        协议。

        :return: The scheme of this HealthCheckConfigurationHttpGet.
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this HealthCheckConfigurationHttpGet.

        协议。

        :param scheme: The scheme of this HealthCheckConfigurationHttpGet.
        :type scheme: str
        """
        self._scheme = scheme

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
        if not isinstance(other, HealthCheckConfigurationHttpGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
