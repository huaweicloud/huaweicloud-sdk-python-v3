# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedirectUrlConfig:

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
        'status_code': 'str',
        'insert_headers_config': 'InsertHeadersConfig',
        'remove_headers_config': 'RemoveHeadersConfig'
    }

    attribute_map = {
        'protocol': 'protocol',
        'host': 'host',
        'port': 'port',
        'path': 'path',
        'query': 'query',
        'status_code': 'status_code',
        'insert_headers_config': 'insert_headers_config',
        'remove_headers_config': 'remove_headers_config'
    }

    def __init__(self, protocol=None, host=None, port=None, path=None, query=None, status_code=None, insert_headers_config=None, remove_headers_config=None):
        r"""RedirectUrlConfig

        The model defined in huaweicloud sdk

        :param protocol: **参数解释**：重定向的协议。  **取值范围**： - HTTP - HTTPS - ${protocol}，表示继承原值（即与被转发请求保持一致）。
        :type protocol: str
        :param host: **参数解释**：重定向的主机名。  **取值范围**：只能包含英文字母、数字、“-”、“.”。且必须以字母、数字开头。
        :type host: str
        :param port: **参数解释**：重定向到的端口。  **取值范围**：不涉及
        :type port: str
        :param path: **参数解释**：重定向的路径。  **取值范围**：支持英文字母、数字、_~&#39;;@^-%#&amp;$.*+?,&#x3D;!:|\\/()\\[\\]{}，且必须以\&quot;/\&quot;开头。
        :type path: str
        :param query: **参数解释**：重定向的查询字符串。举例如下： 将query设置为：${query}&amp;name&#x3D;my_name，则在转发符合条件的URL（如https://www.example.com:8080/elb?type&#x3D;loadbalancer）时，将会重定向到https://www.example.com:8080/elb?type&#x3D;loadbalancer&amp;name&#x3D;my_name。在例子中${query}表示type&#x3D;loadbalancer。  **取值范围**：只能包含英文字母、数字和特殊字符：!$&amp;&#39;()\\*+,-./:;&#x3D;?@^_&#x60;。字母区分大小写。其中$1，$2会匹配请求url通配符星号（\\*）
        :type query: str
        :param status_code: **参数解释**：重定向后的返回码。  **取值范围**： - 301 - 302 - 303 - 307 - 308
        :type status_code: str
        :param insert_headers_config: 
        :type insert_headers_config: :class:`huaweicloudsdkelb.v3.InsertHeadersConfig`
        :param remove_headers_config: 
        :type remove_headers_config: :class:`huaweicloudsdkelb.v3.RemoveHeadersConfig`
        """
        
        

        self._protocol = None
        self._host = None
        self._port = None
        self._path = None
        self._query = None
        self._status_code = None
        self._insert_headers_config = None
        self._remove_headers_config = None
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
        if status_code is not None:
            self.status_code = status_code
        if insert_headers_config is not None:
            self.insert_headers_config = insert_headers_config
        if remove_headers_config is not None:
            self.remove_headers_config = remove_headers_config

    @property
    def protocol(self):
        r"""Gets the protocol of this RedirectUrlConfig.

        **参数解释**：重定向的协议。  **取值范围**： - HTTP - HTTPS - ${protocol}，表示继承原值（即与被转发请求保持一致）。

        :return: The protocol of this RedirectUrlConfig.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this RedirectUrlConfig.

        **参数解释**：重定向的协议。  **取值范围**： - HTTP - HTTPS - ${protocol}，表示继承原值（即与被转发请求保持一致）。

        :param protocol: The protocol of this RedirectUrlConfig.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def host(self):
        r"""Gets the host of this RedirectUrlConfig.

        **参数解释**：重定向的主机名。  **取值范围**：只能包含英文字母、数字、“-”、“.”。且必须以字母、数字开头。

        :return: The host of this RedirectUrlConfig.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this RedirectUrlConfig.

        **参数解释**：重定向的主机名。  **取值范围**：只能包含英文字母、数字、“-”、“.”。且必须以字母、数字开头。

        :param host: The host of this RedirectUrlConfig.
        :type host: str
        """
        self._host = host

    @property
    def port(self):
        r"""Gets the port of this RedirectUrlConfig.

        **参数解释**：重定向到的端口。  **取值范围**：不涉及

        :return: The port of this RedirectUrlConfig.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this RedirectUrlConfig.

        **参数解释**：重定向到的端口。  **取值范围**：不涉及

        :param port: The port of this RedirectUrlConfig.
        :type port: str
        """
        self._port = port

    @property
    def path(self):
        r"""Gets the path of this RedirectUrlConfig.

        **参数解释**：重定向的路径。  **取值范围**：支持英文字母、数字、_~';@^-%#&$.*+?,=!:|\\/()\\[\\]{}，且必须以\"/\"开头。

        :return: The path of this RedirectUrlConfig.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this RedirectUrlConfig.

        **参数解释**：重定向的路径。  **取值范围**：支持英文字母、数字、_~';@^-%#&$.*+?,=!:|\\/()\\[\\]{}，且必须以\"/\"开头。

        :param path: The path of this RedirectUrlConfig.
        :type path: str
        """
        self._path = path

    @property
    def query(self):
        r"""Gets the query of this RedirectUrlConfig.

        **参数解释**：重定向的查询字符串。举例如下： 将query设置为：${query}&name=my_name，则在转发符合条件的URL（如https://www.example.com:8080/elb?type=loadbalancer）时，将会重定向到https://www.example.com:8080/elb?type=loadbalancer&name=my_name。在例子中${query}表示type=loadbalancer。  **取值范围**：只能包含英文字母、数字和特殊字符：!$&'()\\*+,-./:;=?@^_`。字母区分大小写。其中$1，$2会匹配请求url通配符星号（\\*）

        :return: The query of this RedirectUrlConfig.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this RedirectUrlConfig.

        **参数解释**：重定向的查询字符串。举例如下： 将query设置为：${query}&name=my_name，则在转发符合条件的URL（如https://www.example.com:8080/elb?type=loadbalancer）时，将会重定向到https://www.example.com:8080/elb?type=loadbalancer&name=my_name。在例子中${query}表示type=loadbalancer。  **取值范围**：只能包含英文字母、数字和特殊字符：!$&'()\\*+,-./:;=?@^_`。字母区分大小写。其中$1，$2会匹配请求url通配符星号（\\*）

        :param query: The query of this RedirectUrlConfig.
        :type query: str
        """
        self._query = query

    @property
    def status_code(self):
        r"""Gets the status_code of this RedirectUrlConfig.

        **参数解释**：重定向后的返回码。  **取值范围**： - 301 - 302 - 303 - 307 - 308

        :return: The status_code of this RedirectUrlConfig.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this RedirectUrlConfig.

        **参数解释**：重定向后的返回码。  **取值范围**： - 301 - 302 - 303 - 307 - 308

        :param status_code: The status_code of this RedirectUrlConfig.
        :type status_code: str
        """
        self._status_code = status_code

    @property
    def insert_headers_config(self):
        r"""Gets the insert_headers_config of this RedirectUrlConfig.

        :return: The insert_headers_config of this RedirectUrlConfig.
        :rtype: :class:`huaweicloudsdkelb.v3.InsertHeadersConfig`
        """
        return self._insert_headers_config

    @insert_headers_config.setter
    def insert_headers_config(self, insert_headers_config):
        r"""Sets the insert_headers_config of this RedirectUrlConfig.

        :param insert_headers_config: The insert_headers_config of this RedirectUrlConfig.
        :type insert_headers_config: :class:`huaweicloudsdkelb.v3.InsertHeadersConfig`
        """
        self._insert_headers_config = insert_headers_config

    @property
    def remove_headers_config(self):
        r"""Gets the remove_headers_config of this RedirectUrlConfig.

        :return: The remove_headers_config of this RedirectUrlConfig.
        :rtype: :class:`huaweicloudsdkelb.v3.RemoveHeadersConfig`
        """
        return self._remove_headers_config

    @remove_headers_config.setter
    def remove_headers_config(self, remove_headers_config):
        r"""Sets the remove_headers_config of this RedirectUrlConfig.

        :param remove_headers_config: The remove_headers_config of this RedirectUrlConfig.
        :type remove_headers_config: :class:`huaweicloudsdkelb.v3.RemoveHeadersConfig`
        """
        self._remove_headers_config = remove_headers_config

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
        if not isinstance(other, RedirectUrlConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
