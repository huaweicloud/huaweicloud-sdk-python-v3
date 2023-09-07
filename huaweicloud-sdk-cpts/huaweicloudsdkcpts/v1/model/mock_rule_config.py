# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MockRuleConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_type': 'str',
        'request_url': 'str',
        'request_method': 'str',
        'redirect_url': 'str',
        'mock_strategy': 'str',
        'enable': 'bool',
        'name': 'str',
        'project_id': 'str',
        'id': 'int',
        'response_header': 'dict(str, str)',
        'response_body': 'str',
        'response_time': 'int',
        'response_code': 'int'
    }

    attribute_map = {
        'service_type': 'service_type',
        'request_url': 'request_url',
        'request_method': 'request_method',
        'redirect_url': 'redirect_url',
        'mock_strategy': 'mock_strategy',
        'enable': 'enable',
        'name': 'name',
        'project_id': 'project_id',
        'id': 'id',
        'response_header': 'response_header',
        'response_body': 'response_body',
        'response_time': 'response_time',
        'response_code': 'response_code'
    }

    def __init__(self, service_type=None, request_url=None, request_method=None, redirect_url=None, mock_strategy=None, enable=None, name=None, project_id=None, id=None, response_header=None, response_body=None, response_time=None, response_code=None):
        """MockRuleConfig

        The model defined in huaweicloud sdk

        :param service_type: 服务类型（当前只支持http）
        :type service_type: str
        :param request_url: 请求地址
        :type request_url: str
        :param request_method: 请求方式（GET/POST/PUT/DELET/PATCH）
        :type request_method: str
        :param redirect_url: 重定向地址
        :type redirect_url: str
        :param mock_strategy: mock策略（redirect/json）
        :type mock_strategy: str
        :param enable: 是否启用
        :type enable: bool
        :param name: 规则名称
        :type name: str
        :param project_id: 项目id
        :type project_id: str
        :param id: 规则id
        :type id: int
        :param response_header: 自定义响应头
        :type response_header: dict(str, str)
        :param response_body: 自定义响应体
        :type response_body: str
        :param response_time: 自定义响应时长
        :type response_time: int
        :param response_code: 自定义响应码
        :type response_code: int
        """
        
        

        self._service_type = None
        self._request_url = None
        self._request_method = None
        self._redirect_url = None
        self._mock_strategy = None
        self._enable = None
        self._name = None
        self._project_id = None
        self._id = None
        self._response_header = None
        self._response_body = None
        self._response_time = None
        self._response_code = None
        self.discriminator = None

        if service_type is not None:
            self.service_type = service_type
        if request_url is not None:
            self.request_url = request_url
        if request_method is not None:
            self.request_method = request_method
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if mock_strategy is not None:
            self.mock_strategy = mock_strategy
        if enable is not None:
            self.enable = enable
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if id is not None:
            self.id = id
        if response_header is not None:
            self.response_header = response_header
        if response_body is not None:
            self.response_body = response_body
        if response_time is not None:
            self.response_time = response_time
        if response_code is not None:
            self.response_code = response_code

    @property
    def service_type(self):
        """Gets the service_type of this MockRuleConfig.

        服务类型（当前只支持http）

        :return: The service_type of this MockRuleConfig.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this MockRuleConfig.

        服务类型（当前只支持http）

        :param service_type: The service_type of this MockRuleConfig.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def request_url(self):
        """Gets the request_url of this MockRuleConfig.

        请求地址

        :return: The request_url of this MockRuleConfig.
        :rtype: str
        """
        return self._request_url

    @request_url.setter
    def request_url(self, request_url):
        """Sets the request_url of this MockRuleConfig.

        请求地址

        :param request_url: The request_url of this MockRuleConfig.
        :type request_url: str
        """
        self._request_url = request_url

    @property
    def request_method(self):
        """Gets the request_method of this MockRuleConfig.

        请求方式（GET/POST/PUT/DELET/PATCH）

        :return: The request_method of this MockRuleConfig.
        :rtype: str
        """
        return self._request_method

    @request_method.setter
    def request_method(self, request_method):
        """Sets the request_method of this MockRuleConfig.

        请求方式（GET/POST/PUT/DELET/PATCH）

        :param request_method: The request_method of this MockRuleConfig.
        :type request_method: str
        """
        self._request_method = request_method

    @property
    def redirect_url(self):
        """Gets the redirect_url of this MockRuleConfig.

        重定向地址

        :return: The redirect_url of this MockRuleConfig.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this MockRuleConfig.

        重定向地址

        :param redirect_url: The redirect_url of this MockRuleConfig.
        :type redirect_url: str
        """
        self._redirect_url = redirect_url

    @property
    def mock_strategy(self):
        """Gets the mock_strategy of this MockRuleConfig.

        mock策略（redirect/json）

        :return: The mock_strategy of this MockRuleConfig.
        :rtype: str
        """
        return self._mock_strategy

    @mock_strategy.setter
    def mock_strategy(self, mock_strategy):
        """Sets the mock_strategy of this MockRuleConfig.

        mock策略（redirect/json）

        :param mock_strategy: The mock_strategy of this MockRuleConfig.
        :type mock_strategy: str
        """
        self._mock_strategy = mock_strategy

    @property
    def enable(self):
        """Gets the enable of this MockRuleConfig.

        是否启用

        :return: The enable of this MockRuleConfig.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this MockRuleConfig.

        是否启用

        :param enable: The enable of this MockRuleConfig.
        :type enable: bool
        """
        self._enable = enable

    @property
    def name(self):
        """Gets the name of this MockRuleConfig.

        规则名称

        :return: The name of this MockRuleConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MockRuleConfig.

        规则名称

        :param name: The name of this MockRuleConfig.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this MockRuleConfig.

        项目id

        :return: The project_id of this MockRuleConfig.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this MockRuleConfig.

        项目id

        :param project_id: The project_id of this MockRuleConfig.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def id(self):
        """Gets the id of this MockRuleConfig.

        规则id

        :return: The id of this MockRuleConfig.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MockRuleConfig.

        规则id

        :param id: The id of this MockRuleConfig.
        :type id: int
        """
        self._id = id

    @property
    def response_header(self):
        """Gets the response_header of this MockRuleConfig.

        自定义响应头

        :return: The response_header of this MockRuleConfig.
        :rtype: dict(str, str)
        """
        return self._response_header

    @response_header.setter
    def response_header(self, response_header):
        """Sets the response_header of this MockRuleConfig.

        自定义响应头

        :param response_header: The response_header of this MockRuleConfig.
        :type response_header: dict(str, str)
        """
        self._response_header = response_header

    @property
    def response_body(self):
        """Gets the response_body of this MockRuleConfig.

        自定义响应体

        :return: The response_body of this MockRuleConfig.
        :rtype: str
        """
        return self._response_body

    @response_body.setter
    def response_body(self, response_body):
        """Sets the response_body of this MockRuleConfig.

        自定义响应体

        :param response_body: The response_body of this MockRuleConfig.
        :type response_body: str
        """
        self._response_body = response_body

    @property
    def response_time(self):
        """Gets the response_time of this MockRuleConfig.

        自定义响应时长

        :return: The response_time of this MockRuleConfig.
        :rtype: int
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        """Sets the response_time of this MockRuleConfig.

        自定义响应时长

        :param response_time: The response_time of this MockRuleConfig.
        :type response_time: int
        """
        self._response_time = response_time

    @property
    def response_code(self):
        """Gets the response_code of this MockRuleConfig.

        自定义响应码

        :return: The response_code of this MockRuleConfig.
        :rtype: int
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """Sets the response_code of this MockRuleConfig.

        自定义响应码

        :param response_code: The response_code of this MockRuleConfig.
        :type response_code: int
        """
        self._response_code = response_code

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
        if not isinstance(other, MockRuleConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
