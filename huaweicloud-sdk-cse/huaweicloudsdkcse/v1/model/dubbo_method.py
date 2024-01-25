# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DubboMethod:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_method': 'str',
        'headers_attach': 'str',
        'http_methods': 'list[str]',
        'http_path': 'str',
        'params': 'list[DubboMethodParam]'
    }

    attribute_map = {
        'service_method': 'serviceMethod',
        'headers_attach': 'headersAttach',
        'http_methods': 'httpMethods',
        'http_path': 'httpPath',
        'params': 'params'
    }

    def __init__(self, service_method=None, headers_attach=None, http_methods=None, http_path=None, params=None):
        """DubboMethod

        The model defined in huaweicloud sdk

        :param service_method: 服务方法。
        :type service_method: str
        :param headers_attach: 附加请求头。
        :type headers_attach: str
        :param http_methods: http 方法。
        :type http_methods: list[str]
        :param http_path: http 路径。
        :type http_path: str
        :param params: dubbo 方法参数。
        :type params: list[:class:`huaweicloudsdkcse.v1.DubboMethodParam`]
        """
        
        

        self._service_method = None
        self._headers_attach = None
        self._http_methods = None
        self._http_path = None
        self._params = None
        self.discriminator = None

        if service_method is not None:
            self.service_method = service_method
        if headers_attach is not None:
            self.headers_attach = headers_attach
        if http_methods is not None:
            self.http_methods = http_methods
        if http_path is not None:
            self.http_path = http_path
        if params is not None:
            self.params = params

    @property
    def service_method(self):
        """Gets the service_method of this DubboMethod.

        服务方法。

        :return: The service_method of this DubboMethod.
        :rtype: str
        """
        return self._service_method

    @service_method.setter
    def service_method(self, service_method):
        """Sets the service_method of this DubboMethod.

        服务方法。

        :param service_method: The service_method of this DubboMethod.
        :type service_method: str
        """
        self._service_method = service_method

    @property
    def headers_attach(self):
        """Gets the headers_attach of this DubboMethod.

        附加请求头。

        :return: The headers_attach of this DubboMethod.
        :rtype: str
        """
        return self._headers_attach

    @headers_attach.setter
    def headers_attach(self, headers_attach):
        """Sets the headers_attach of this DubboMethod.

        附加请求头。

        :param headers_attach: The headers_attach of this DubboMethod.
        :type headers_attach: str
        """
        self._headers_attach = headers_attach

    @property
    def http_methods(self):
        """Gets the http_methods of this DubboMethod.

        http 方法。

        :return: The http_methods of this DubboMethod.
        :rtype: list[str]
        """
        return self._http_methods

    @http_methods.setter
    def http_methods(self, http_methods):
        """Sets the http_methods of this DubboMethod.

        http 方法。

        :param http_methods: The http_methods of this DubboMethod.
        :type http_methods: list[str]
        """
        self._http_methods = http_methods

    @property
    def http_path(self):
        """Gets the http_path of this DubboMethod.

        http 路径。

        :return: The http_path of this DubboMethod.
        :rtype: str
        """
        return self._http_path

    @http_path.setter
    def http_path(self, http_path):
        """Sets the http_path of this DubboMethod.

        http 路径。

        :param http_path: The http_path of this DubboMethod.
        :type http_path: str
        """
        self._http_path = http_path

    @property
    def params(self):
        """Gets the params of this DubboMethod.

        dubbo 方法参数。

        :return: The params of this DubboMethod.
        :rtype: list[:class:`huaweicloudsdkcse.v1.DubboMethodParam`]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this DubboMethod.

        dubbo 方法参数。

        :param params: The params of this DubboMethod.
        :type params: list[:class:`huaweicloudsdkcse.v1.DubboMethodParam`]
        """
        self._params = params

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
        if not isinstance(other, DubboMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
