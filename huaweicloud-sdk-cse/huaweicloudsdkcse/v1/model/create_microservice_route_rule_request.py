# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMicroserviceRouteRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_type': 'str',
        'x_engine_id': 'str',
        'x_enterprise_project_id': 'str',
        'service_name': 'str',
        'environment': 'str',
        'app_id': 'str',
        'body': 'list[CreateRules]'
    }

    attribute_map = {
        'content_type': 'Content-Type',
        'x_engine_id': 'x-engine-id',
        'x_enterprise_project_id': 'X-Enterprise-Project-ID',
        'service_name': 'service_name',
        'environment': 'environment',
        'app_id': 'app_id',
        'body': 'body'
    }

    def __init__(self, content_type=None, x_engine_id=None, x_enterprise_project_id=None, service_name=None, environment=None, app_id=None, body=None):
        """CreateMicroserviceRouteRuleRequest

        The model defined in huaweicloud sdk

        :param content_type: 该字段内容填为 \&quot;application/json;charset&#x3D;UTF-8\&quot;。
        :type content_type: str
        :param x_engine_id: 微服务引擎专享版的实例ID
        :type x_engine_id: str
        :param x_enterprise_project_id: 企业项目ID
        :type x_enterprise_project_id: str
        :param service_name: 微服务名称
        :type service_name: str
        :param environment: 所属环境，不填表示&lt;空&gt;环境
        :type environment: str
        :param app_id: 所属应用，不填默认为default应用
        :type app_id: str
        :param body: Body of the CreateMicroserviceRouteRuleRequest
        :type body: list[:class:`huaweicloudsdkcse.v1.CreateRules`]
        """
        
        

        self._content_type = None
        self._x_engine_id = None
        self._x_enterprise_project_id = None
        self._service_name = None
        self._environment = None
        self._app_id = None
        self._body = None
        self.discriminator = None

        self.content_type = content_type
        self.x_engine_id = x_engine_id
        self.x_enterprise_project_id = x_enterprise_project_id
        self.service_name = service_name
        if environment is not None:
            self.environment = environment
        if app_id is not None:
            self.app_id = app_id
        if body is not None:
            self.body = body

    @property
    def content_type(self):
        """Gets the content_type of this CreateMicroserviceRouteRuleRequest.

        该字段内容填为 \"application/json;charset=UTF-8\"。

        :return: The content_type of this CreateMicroserviceRouteRuleRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this CreateMicroserviceRouteRuleRequest.

        该字段内容填为 \"application/json;charset=UTF-8\"。

        :param content_type: The content_type of this CreateMicroserviceRouteRuleRequest.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def x_engine_id(self):
        """Gets the x_engine_id of this CreateMicroserviceRouteRuleRequest.

        微服务引擎专享版的实例ID

        :return: The x_engine_id of this CreateMicroserviceRouteRuleRequest.
        :rtype: str
        """
        return self._x_engine_id

    @x_engine_id.setter
    def x_engine_id(self, x_engine_id):
        """Sets the x_engine_id of this CreateMicroserviceRouteRuleRequest.

        微服务引擎专享版的实例ID

        :param x_engine_id: The x_engine_id of this CreateMicroserviceRouteRuleRequest.
        :type x_engine_id: str
        """
        self._x_engine_id = x_engine_id

    @property
    def x_enterprise_project_id(self):
        """Gets the x_enterprise_project_id of this CreateMicroserviceRouteRuleRequest.

        企业项目ID

        :return: The x_enterprise_project_id of this CreateMicroserviceRouteRuleRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        """Sets the x_enterprise_project_id of this CreateMicroserviceRouteRuleRequest.

        企业项目ID

        :param x_enterprise_project_id: The x_enterprise_project_id of this CreateMicroserviceRouteRuleRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

    @property
    def service_name(self):
        """Gets the service_name of this CreateMicroserviceRouteRuleRequest.

        微服务名称

        :return: The service_name of this CreateMicroserviceRouteRuleRequest.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this CreateMicroserviceRouteRuleRequest.

        微服务名称

        :param service_name: The service_name of this CreateMicroserviceRouteRuleRequest.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def environment(self):
        """Gets the environment of this CreateMicroserviceRouteRuleRequest.

        所属环境，不填表示<空>环境

        :return: The environment of this CreateMicroserviceRouteRuleRequest.
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this CreateMicroserviceRouteRuleRequest.

        所属环境，不填表示<空>环境

        :param environment: The environment of this CreateMicroserviceRouteRuleRequest.
        :type environment: str
        """
        self._environment = environment

    @property
    def app_id(self):
        """Gets the app_id of this CreateMicroserviceRouteRuleRequest.

        所属应用，不填默认为default应用

        :return: The app_id of this CreateMicroserviceRouteRuleRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateMicroserviceRouteRuleRequest.

        所属应用，不填默认为default应用

        :param app_id: The app_id of this CreateMicroserviceRouteRuleRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def body(self):
        """Gets the body of this CreateMicroserviceRouteRuleRequest.

        :return: The body of this CreateMicroserviceRouteRuleRequest.
        :rtype: list[:class:`huaweicloudsdkcse.v1.CreateRules`]
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateMicroserviceRouteRuleRequest.

        :param body: The body of this CreateMicroserviceRouteRuleRequest.
        :type body: list[:class:`huaweicloudsdkcse.v1.CreateRules`]
        """
        self._body = body

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
        if not isinstance(other, CreateMicroserviceRouteRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
