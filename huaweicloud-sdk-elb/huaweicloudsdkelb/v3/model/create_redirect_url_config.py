# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRedirectUrlConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol': 'str',
        'host': 'str',
        'port': 'str',
        'path': 'str',
        'query': 'str',
        'status_code': 'str'
    }

    attribute_map = {
        'protocol': 'protocol',
        'host': 'host',
        'port': 'port',
        'path': 'path',
        'query': 'query',
        'status_code': 'status_code'
    }

    def __init__(self, protocol=None, host=None, port=None, path=None, query=None, status_code=None):
        """CreateRedirectUrlConfig

        The model defined in huaweicloud sdk

        :param protocol: 重定向的协议。默认值${protocol}表示继承原值（即与被转发请求保持一致）。  取值范围： - HTTP - HTTPS - ${protocol}
        :type protocol: str
        :param host: 重定向的主机名。字符串只能包含英文字母、数字、“-”、“.”，必须以字母、数字开头。 默认值${host}表示继承原值（即与被转发请求保持一致）。
        :type host: str
        :param port: 重定向到的端口。默认值${port}表示继承原值（即与被转发请求保持一致）。
        :type port: str
        :param path: 重定向的路径。默认值${path}表示继承原值（即与被转发请求保持一致）。  只能包含英文字母、数字、_~&#39;;@^-%#&amp;$.*+?,&#x3D;!:|\\/()\\[\\]{}，且必须以\&quot;/\&quot;开头。
        :type path: str
        :param query: 重定向的查询字符串。默认${query}表示继承原值（即与被转发请求保持一致）。举例如下：  若该字段被设置为：${query}&amp;name&#x3D;my_name，则在转发符合条件的URL （如https://www.xxx.com:8080/elb?type&#x3D;loadbalancer， 此时${query}表示type&#x3D;loadbalancer）时，将会重定向到 https://www.xxx.com:8080/elb?type&#x3D;loadbalancer&amp;name&#x3D;my_name。  只能包含英文字母、数字和特殊字符：!$&amp;&#39;()*+,-./:;&#x3D;?@^_&#x60;。字母区分大小写。
        :type query: str
        :param status_code: 重定向后的返回码。  取值范围： - 301 - 302 - 303 - 307 - 308
        :type status_code: str
        """
        
        

        self._protocol = None
        self._host = None
        self._port = None
        self._path = None
        self._query = None
        self._status_code = None
        self.discriminator = None

        if protocol is not None:
            self.protocol = protocol
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if path is not None:
            self.path = path
        if query is not None:
            self.query = query
        self.status_code = status_code

    @property
    def protocol(self):
        """Gets the protocol of this CreateRedirectUrlConfig.

        重定向的协议。默认值${protocol}表示继承原值（即与被转发请求保持一致）。  取值范围： - HTTP - HTTPS - ${protocol}

        :return: The protocol of this CreateRedirectUrlConfig.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateRedirectUrlConfig.

        重定向的协议。默认值${protocol}表示继承原值（即与被转发请求保持一致）。  取值范围： - HTTP - HTTPS - ${protocol}

        :param protocol: The protocol of this CreateRedirectUrlConfig.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def host(self):
        """Gets the host of this CreateRedirectUrlConfig.

        重定向的主机名。字符串只能包含英文字母、数字、“-”、“.”，必须以字母、数字开头。 默认值${host}表示继承原值（即与被转发请求保持一致）。

        :return: The host of this CreateRedirectUrlConfig.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this CreateRedirectUrlConfig.

        重定向的主机名。字符串只能包含英文字母、数字、“-”、“.”，必须以字母、数字开头。 默认值${host}表示继承原值（即与被转发请求保持一致）。

        :param host: The host of this CreateRedirectUrlConfig.
        :type host: str
        """
        self._host = host

    @property
    def port(self):
        """Gets the port of this CreateRedirectUrlConfig.

        重定向到的端口。默认值${port}表示继承原值（即与被转发请求保持一致）。

        :return: The port of this CreateRedirectUrlConfig.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateRedirectUrlConfig.

        重定向到的端口。默认值${port}表示继承原值（即与被转发请求保持一致）。

        :param port: The port of this CreateRedirectUrlConfig.
        :type port: str
        """
        self._port = port

    @property
    def path(self):
        """Gets the path of this CreateRedirectUrlConfig.

        重定向的路径。默认值${path}表示继承原值（即与被转发请求保持一致）。  只能包含英文字母、数字、_~';@^-%#&$.*+?,=!:|\\/()\\[\\]{}，且必须以\"/\"开头。

        :return: The path of this CreateRedirectUrlConfig.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this CreateRedirectUrlConfig.

        重定向的路径。默认值${path}表示继承原值（即与被转发请求保持一致）。  只能包含英文字母、数字、_~';@^-%#&$.*+?,=!:|\\/()\\[\\]{}，且必须以\"/\"开头。

        :param path: The path of this CreateRedirectUrlConfig.
        :type path: str
        """
        self._path = path

    @property
    def query(self):
        """Gets the query of this CreateRedirectUrlConfig.

        重定向的查询字符串。默认${query}表示继承原值（即与被转发请求保持一致）。举例如下：  若该字段被设置为：${query}&name=my_name，则在转发符合条件的URL （如https://www.xxx.com:8080/elb?type=loadbalancer， 此时${query}表示type=loadbalancer）时，将会重定向到 https://www.xxx.com:8080/elb?type=loadbalancer&name=my_name。  只能包含英文字母、数字和特殊字符：!$&'()*+,-./:;=?@^_`。字母区分大小写。

        :return: The query of this CreateRedirectUrlConfig.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this CreateRedirectUrlConfig.

        重定向的查询字符串。默认${query}表示继承原值（即与被转发请求保持一致）。举例如下：  若该字段被设置为：${query}&name=my_name，则在转发符合条件的URL （如https://www.xxx.com:8080/elb?type=loadbalancer， 此时${query}表示type=loadbalancer）时，将会重定向到 https://www.xxx.com:8080/elb?type=loadbalancer&name=my_name。  只能包含英文字母、数字和特殊字符：!$&'()*+,-./:;=?@^_`。字母区分大小写。

        :param query: The query of this CreateRedirectUrlConfig.
        :type query: str
        """
        self._query = query

    @property
    def status_code(self):
        """Gets the status_code of this CreateRedirectUrlConfig.

        重定向后的返回码。  取值范围： - 301 - 302 - 303 - 307 - 308

        :return: The status_code of this CreateRedirectUrlConfig.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this CreateRedirectUrlConfig.

        重定向后的返回码。  取值范围： - 301 - 302 - 303 - 307 - 308

        :param status_code: The status_code of this CreateRedirectUrlConfig.
        :type status_code: str
        """
        self._status_code = status_code

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
        if not isinstance(other, CreateRedirectUrlConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
