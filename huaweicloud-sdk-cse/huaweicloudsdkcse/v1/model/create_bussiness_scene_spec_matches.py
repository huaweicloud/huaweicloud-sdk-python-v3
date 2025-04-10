# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBussinessSceneSpecMatches:

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
        'api_path': 'object',
        'headers': 'object',
        'method': 'list[str]',
        'service_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'api_path': 'apiPath',
        'headers': 'headers',
        'method': 'method',
        'service_name': 'serviceName'
    }

    def __init__(self, name=None, api_path=None, headers=None, method=None, service_name=None):
        r"""CreateBussinessSceneSpecMatches

        The model defined in huaweicloud sdk

        :param name: 条件名称
        :type name: str
        :param api_path: 匹配的PATH
        :type api_path: object
        :param headers: 匹配的Headers
        :type headers: object
        :param method: 匹配的Method列表
        :type method: list[str]
        :param service_name: 匹配的微服务名称
        :type service_name: str
        """
        
        

        self._name = None
        self._api_path = None
        self._headers = None
        self._method = None
        self._service_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if api_path is not None:
            self.api_path = api_path
        if headers is not None:
            self.headers = headers
        if method is not None:
            self.method = method
        if service_name is not None:
            self.service_name = service_name

    @property
    def name(self):
        r"""Gets the name of this CreateBussinessSceneSpecMatches.

        条件名称

        :return: The name of this CreateBussinessSceneSpecMatches.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateBussinessSceneSpecMatches.

        条件名称

        :param name: The name of this CreateBussinessSceneSpecMatches.
        :type name: str
        """
        self._name = name

    @property
    def api_path(self):
        r"""Gets the api_path of this CreateBussinessSceneSpecMatches.

        匹配的PATH

        :return: The api_path of this CreateBussinessSceneSpecMatches.
        :rtype: object
        """
        return self._api_path

    @api_path.setter
    def api_path(self, api_path):
        r"""Sets the api_path of this CreateBussinessSceneSpecMatches.

        匹配的PATH

        :param api_path: The api_path of this CreateBussinessSceneSpecMatches.
        :type api_path: object
        """
        self._api_path = api_path

    @property
    def headers(self):
        r"""Gets the headers of this CreateBussinessSceneSpecMatches.

        匹配的Headers

        :return: The headers of this CreateBussinessSceneSpecMatches.
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        r"""Sets the headers of this CreateBussinessSceneSpecMatches.

        匹配的Headers

        :param headers: The headers of this CreateBussinessSceneSpecMatches.
        :type headers: object
        """
        self._headers = headers

    @property
    def method(self):
        r"""Gets the method of this CreateBussinessSceneSpecMatches.

        匹配的Method列表

        :return: The method of this CreateBussinessSceneSpecMatches.
        :rtype: list[str]
        """
        return self._method

    @method.setter
    def method(self, method):
        r"""Sets the method of this CreateBussinessSceneSpecMatches.

        匹配的Method列表

        :param method: The method of this CreateBussinessSceneSpecMatches.
        :type method: list[str]
        """
        self._method = method

    @property
    def service_name(self):
        r"""Gets the service_name of this CreateBussinessSceneSpecMatches.

        匹配的微服务名称

        :return: The service_name of this CreateBussinessSceneSpecMatches.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this CreateBussinessSceneSpecMatches.

        匹配的微服务名称

        :param service_name: The service_name of this CreateBussinessSceneSpecMatches.
        :type service_name: str
        """
        self._service_name = service_name

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
        if not isinstance(other, CreateBussinessSceneSpecMatches):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
