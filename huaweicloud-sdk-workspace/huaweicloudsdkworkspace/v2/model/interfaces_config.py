# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InterfacesConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'apply_platform': 'str',
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'results': 'dict(str, str)',
        'pagination': 'dict(str, object)',
        'request': 'InterfacesRequest',
        'response': 'str',
        'result_check': 'str'
    }

    attribute_map = {
        'apply_platform': 'apply_platform',
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'results': 'results',
        'pagination': 'pagination',
        'request': 'request',
        'response': 'response',
        'result_check': 'result_check'
    }

    def __init__(self, apply_platform=None, id=None, name=None, type=None, results=None, pagination=None, request=None, response=None, result_check=None):
        r"""InterfacesConfig

        The model defined in huaweicloud sdk

        :param apply_platform: 应用平台。
        :type apply_platform: str
        :param id: ID。
        :type id: str
        :param name: 名称。
        :type name: str
        :param type: 类型。
        :type type: str
        :param results: 结果。
        :type results: dict(str, str)
        :param pagination: 分页信息。
        :type pagination: dict(str, object)
        :param request: 
        :type request: :class:`huaweicloudsdkworkspace.v2.InterfacesRequest`
        :param response: 响应。
        :type response: str
        :param result_check: 检查结果。
        :type result_check: str
        """
        
        

        self._apply_platform = None
        self._id = None
        self._name = None
        self._type = None
        self._results = None
        self._pagination = None
        self._request = None
        self._response = None
        self._result_check = None
        self.discriminator = None

        if apply_platform is not None:
            self.apply_platform = apply_platform
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if results is not None:
            self.results = results
        if pagination is not None:
            self.pagination = pagination
        if request is not None:
            self.request = request
        if response is not None:
            self.response = response
        if result_check is not None:
            self.result_check = result_check

    @property
    def apply_platform(self):
        r"""Gets the apply_platform of this InterfacesConfig.

        应用平台。

        :return: The apply_platform of this InterfacesConfig.
        :rtype: str
        """
        return self._apply_platform

    @apply_platform.setter
    def apply_platform(self, apply_platform):
        r"""Sets the apply_platform of this InterfacesConfig.

        应用平台。

        :param apply_platform: The apply_platform of this InterfacesConfig.
        :type apply_platform: str
        """
        self._apply_platform = apply_platform

    @property
    def id(self):
        r"""Gets the id of this InterfacesConfig.

        ID。

        :return: The id of this InterfacesConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InterfacesConfig.

        ID。

        :param id: The id of this InterfacesConfig.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this InterfacesConfig.

        名称。

        :return: The name of this InterfacesConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InterfacesConfig.

        名称。

        :param name: The name of this InterfacesConfig.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this InterfacesConfig.

        类型。

        :return: The type of this InterfacesConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this InterfacesConfig.

        类型。

        :param type: The type of this InterfacesConfig.
        :type type: str
        """
        self._type = type

    @property
    def results(self):
        r"""Gets the results of this InterfacesConfig.

        结果。

        :return: The results of this InterfacesConfig.
        :rtype: dict(str, str)
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this InterfacesConfig.

        结果。

        :param results: The results of this InterfacesConfig.
        :type results: dict(str, str)
        """
        self._results = results

    @property
    def pagination(self):
        r"""Gets the pagination of this InterfacesConfig.

        分页信息。

        :return: The pagination of this InterfacesConfig.
        :rtype: dict(str, object)
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        r"""Sets the pagination of this InterfacesConfig.

        分页信息。

        :param pagination: The pagination of this InterfacesConfig.
        :type pagination: dict(str, object)
        """
        self._pagination = pagination

    @property
    def request(self):
        r"""Gets the request of this InterfacesConfig.

        :return: The request of this InterfacesConfig.
        :rtype: :class:`huaweicloudsdkworkspace.v2.InterfacesRequest`
        """
        return self._request

    @request.setter
    def request(self, request):
        r"""Sets the request of this InterfacesConfig.

        :param request: The request of this InterfacesConfig.
        :type request: :class:`huaweicloudsdkworkspace.v2.InterfacesRequest`
        """
        self._request = request

    @property
    def response(self):
        r"""Gets the response of this InterfacesConfig.

        响应。

        :return: The response of this InterfacesConfig.
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        r"""Sets the response of this InterfacesConfig.

        响应。

        :param response: The response of this InterfacesConfig.
        :type response: str
        """
        self._response = response

    @property
    def result_check(self):
        r"""Gets the result_check of this InterfacesConfig.

        检查结果。

        :return: The result_check of this InterfacesConfig.
        :rtype: str
        """
        return self._result_check

    @result_check.setter
    def result_check(self, result_check):
        r"""Sets the result_check of this InterfacesConfig.

        检查结果。

        :param result_check: The result_check of this InterfacesConfig.
        :type result_check: str
        """
        self._result_check = result_check

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
        if not isinstance(other, InterfacesConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
