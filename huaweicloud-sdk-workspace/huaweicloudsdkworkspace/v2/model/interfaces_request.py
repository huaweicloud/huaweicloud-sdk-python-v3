# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InterfacesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'method': 'str',
        'params': 'dict(str, str)',
        'headers': 'dict(str, str)',
        'body': 'str',
        'url': 'str',
        'configs': 'dict(str, object)'
    }

    attribute_map = {
        'method': 'method',
        'params': 'params',
        'headers': 'headers',
        'body': 'body',
        'url': 'url',
        'configs': 'configs'
    }

    def __init__(self, method=None, params=None, headers=None, body=None, url=None, configs=None):
        r"""InterfacesRequest

        The model defined in huaweicloud sdk

        :param method: 方法。
        :type method: str
        :param params: 请求参数。
        :type params: dict(str, str)
        :param headers: 请求头信息。
        :type headers: dict(str, str)
        :param body: 请求体。
        :type body: str
        :param url: URL。
        :type url: str
        :param configs: 配置。
        :type configs: dict(str, object)
        """
        
        

        self._method = None
        self._params = None
        self._headers = None
        self._body = None
        self._url = None
        self._configs = None
        self.discriminator = None

        if method is not None:
            self.method = method
        if params is not None:
            self.params = params
        if headers is not None:
            self.headers = headers
        if body is not None:
            self.body = body
        if url is not None:
            self.url = url
        if configs is not None:
            self.configs = configs

    @property
    def method(self):
        r"""Gets the method of this InterfacesRequest.

        方法。

        :return: The method of this InterfacesRequest.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        r"""Sets the method of this InterfacesRequest.

        方法。

        :param method: The method of this InterfacesRequest.
        :type method: str
        """
        self._method = method

    @property
    def params(self):
        r"""Gets the params of this InterfacesRequest.

        请求参数。

        :return: The params of this InterfacesRequest.
        :rtype: dict(str, str)
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this InterfacesRequest.

        请求参数。

        :param params: The params of this InterfacesRequest.
        :type params: dict(str, str)
        """
        self._params = params

    @property
    def headers(self):
        r"""Gets the headers of this InterfacesRequest.

        请求头信息。

        :return: The headers of this InterfacesRequest.
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        r"""Sets the headers of this InterfacesRequest.

        请求头信息。

        :param headers: The headers of this InterfacesRequest.
        :type headers: dict(str, str)
        """
        self._headers = headers

    @property
    def body(self):
        r"""Gets the body of this InterfacesRequest.

        请求体。

        :return: The body of this InterfacesRequest.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this InterfacesRequest.

        请求体。

        :param body: The body of this InterfacesRequest.
        :type body: str
        """
        self._body = body

    @property
    def url(self):
        r"""Gets the url of this InterfacesRequest.

        URL。

        :return: The url of this InterfacesRequest.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this InterfacesRequest.

        URL。

        :param url: The url of this InterfacesRequest.
        :type url: str
        """
        self._url = url

    @property
    def configs(self):
        r"""Gets the configs of this InterfacesRequest.

        配置。

        :return: The configs of this InterfacesRequest.
        :rtype: dict(str, object)
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        r"""Sets the configs of this InterfacesRequest.

        配置。

        :param configs: The configs of this InterfacesRequest.
        :type configs: dict(str, object)
        """
        self._configs = configs

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
        if not isinstance(other, InterfacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
