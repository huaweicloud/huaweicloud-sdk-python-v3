# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CorsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'allow_origin': 'list[str]',
        'allow_methods': 'list[str]',
        'allow_headers': 'list[str]',
        'expose_headers': 'list[str]',
        'allow_credentials': 'bool',
        'max_age': 'int'
    }

    attribute_map = {
        'allow_origin': 'allow_origin',
        'allow_methods': 'allow_methods',
        'allow_headers': 'allow_headers',
        'expose_headers': 'expose_headers',
        'allow_credentials': 'allow_credentials',
        'max_age': 'max_age'
    }

    def __init__(self, allow_origin=None, allow_methods=None, allow_headers=None, expose_headers=None, allow_credentials=None, max_age=None):
        r"""CorsConfig

        The model defined in huaweicloud sdk

        :param allow_origin: **参数解释**：允许的访问来源列表。支持只配置一个元素*，或配置一个或多个值。  **约束限制**： - 单个值必须以http://或者https://开头，后边加一个正确的域名或一级泛域名。（例：http://*.test.abc.example.com） - 单个值可以不加端口，也可以指定端口，端口范围：1~65535。
        :type allow_origin: list[str]
        :param allow_methods: **参数解释**：选择跨域访问时允许的 HTTP 方法。  **取值范围**：不涉及
        :type allow_methods: list[str]
        :param allow_headers: **参数解释**：允许跨域的 Header 列表。  **取值范围**：不涉及
        :type allow_headers: list[str]
        :param expose_headers: **参数解释**：允许暴露的Header列表。  **取值范围**：不涉及
        :type expose_headers: list[str]
        :param allow_credentials: **参数解释**：是否允许携带凭证信息。  **取值范围**： - true：是。 - false：否。
        :type allow_credentials: bool
        :param max_age: **参数解释**：预检请求在浏览器的最大缓存时间，单位：秒。  **取值范围**：-1~172800
        :type max_age: int
        """
        
        

        self._allow_origin = None
        self._allow_methods = None
        self._allow_headers = None
        self._expose_headers = None
        self._allow_credentials = None
        self._max_age = None
        self.discriminator = None

        if allow_origin is not None:
            self.allow_origin = allow_origin
        if allow_methods is not None:
            self.allow_methods = allow_methods
        if allow_headers is not None:
            self.allow_headers = allow_headers
        if expose_headers is not None:
            self.expose_headers = expose_headers
        if allow_credentials is not None:
            self.allow_credentials = allow_credentials
        if max_age is not None:
            self.max_age = max_age

    @property
    def allow_origin(self):
        r"""Gets the allow_origin of this CorsConfig.

        **参数解释**：允许的访问来源列表。支持只配置一个元素*，或配置一个或多个值。  **约束限制**： - 单个值必须以http://或者https://开头，后边加一个正确的域名或一级泛域名。（例：http://*.test.abc.example.com） - 单个值可以不加端口，也可以指定端口，端口范围：1~65535。

        :return: The allow_origin of this CorsConfig.
        :rtype: list[str]
        """
        return self._allow_origin

    @allow_origin.setter
    def allow_origin(self, allow_origin):
        r"""Sets the allow_origin of this CorsConfig.

        **参数解释**：允许的访问来源列表。支持只配置一个元素*，或配置一个或多个值。  **约束限制**： - 单个值必须以http://或者https://开头，后边加一个正确的域名或一级泛域名。（例：http://*.test.abc.example.com） - 单个值可以不加端口，也可以指定端口，端口范围：1~65535。

        :param allow_origin: The allow_origin of this CorsConfig.
        :type allow_origin: list[str]
        """
        self._allow_origin = allow_origin

    @property
    def allow_methods(self):
        r"""Gets the allow_methods of this CorsConfig.

        **参数解释**：选择跨域访问时允许的 HTTP 方法。  **取值范围**：不涉及

        :return: The allow_methods of this CorsConfig.
        :rtype: list[str]
        """
        return self._allow_methods

    @allow_methods.setter
    def allow_methods(self, allow_methods):
        r"""Sets the allow_methods of this CorsConfig.

        **参数解释**：选择跨域访问时允许的 HTTP 方法。  **取值范围**：不涉及

        :param allow_methods: The allow_methods of this CorsConfig.
        :type allow_methods: list[str]
        """
        self._allow_methods = allow_methods

    @property
    def allow_headers(self):
        r"""Gets the allow_headers of this CorsConfig.

        **参数解释**：允许跨域的 Header 列表。  **取值范围**：不涉及

        :return: The allow_headers of this CorsConfig.
        :rtype: list[str]
        """
        return self._allow_headers

    @allow_headers.setter
    def allow_headers(self, allow_headers):
        r"""Sets the allow_headers of this CorsConfig.

        **参数解释**：允许跨域的 Header 列表。  **取值范围**：不涉及

        :param allow_headers: The allow_headers of this CorsConfig.
        :type allow_headers: list[str]
        """
        self._allow_headers = allow_headers

    @property
    def expose_headers(self):
        r"""Gets the expose_headers of this CorsConfig.

        **参数解释**：允许暴露的Header列表。  **取值范围**：不涉及

        :return: The expose_headers of this CorsConfig.
        :rtype: list[str]
        """
        return self._expose_headers

    @expose_headers.setter
    def expose_headers(self, expose_headers):
        r"""Sets the expose_headers of this CorsConfig.

        **参数解释**：允许暴露的Header列表。  **取值范围**：不涉及

        :param expose_headers: The expose_headers of this CorsConfig.
        :type expose_headers: list[str]
        """
        self._expose_headers = expose_headers

    @property
    def allow_credentials(self):
        r"""Gets the allow_credentials of this CorsConfig.

        **参数解释**：是否允许携带凭证信息。  **取值范围**： - true：是。 - false：否。

        :return: The allow_credentials of this CorsConfig.
        :rtype: bool
        """
        return self._allow_credentials

    @allow_credentials.setter
    def allow_credentials(self, allow_credentials):
        r"""Sets the allow_credentials of this CorsConfig.

        **参数解释**：是否允许携带凭证信息。  **取值范围**： - true：是。 - false：否。

        :param allow_credentials: The allow_credentials of this CorsConfig.
        :type allow_credentials: bool
        """
        self._allow_credentials = allow_credentials

    @property
    def max_age(self):
        r"""Gets the max_age of this CorsConfig.

        **参数解释**：预检请求在浏览器的最大缓存时间，单位：秒。  **取值范围**：-1~172800

        :return: The max_age of this CorsConfig.
        :rtype: int
        """
        return self._max_age

    @max_age.setter
    def max_age(self, max_age):
        r"""Sets the max_age of this CorsConfig.

        **参数解释**：预检请求在浏览器的最大缓存时间，单位：秒。  **取值范围**：-1~172800

        :param max_age: The max_age of this CorsConfig.
        :type max_age: int
        """
        self._max_age = max_age

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
        if not isinstance(other, CorsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
