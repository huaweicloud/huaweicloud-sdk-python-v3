# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGovernancePolicyRequest:

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
        'x_environment': 'str',
        'kind': 'str',
        'body': 'CreateGovPolicy'
    }

    attribute_map = {
        'content_type': 'Content-Type',
        'x_engine_id': 'x-engine-id',
        'x_enterprise_project_id': 'X-Enterprise-Project-ID',
        'x_environment': 'x-environment',
        'kind': 'kind',
        'body': 'body'
    }

    def __init__(self, content_type=None, x_engine_id=None, x_enterprise_project_id=None, x_environment=None, kind=None, body=None):
        """CreateGovernancePolicyRequest

        The model defined in huaweicloud sdk

        :param content_type: 该字段内容填为 \&quot;application/json;charset&#x3D;UTF-8\&quot;。
        :type content_type: str
        :param x_engine_id: 微服务引擎的实例ID
        :type x_engine_id: str
        :param x_enterprise_project_id: 企业项目ID
        :type x_enterprise_project_id: str
        :param x_environment: 所属环境
        :type x_environment: str
        :param kind: 治理策略类型
        :type kind: str
        :param body: Body of the CreateGovernancePolicyRequest
        :type body: :class:`huaweicloudsdkcse.v1.CreateGovPolicy`
        """
        
        

        self._content_type = None
        self._x_engine_id = None
        self._x_enterprise_project_id = None
        self._x_environment = None
        self._kind = None
        self._body = None
        self.discriminator = None

        self.content_type = content_type
        self.x_engine_id = x_engine_id
        self.x_enterprise_project_id = x_enterprise_project_id
        if x_environment is not None:
            self.x_environment = x_environment
        self.kind = kind
        if body is not None:
            self.body = body

    @property
    def content_type(self):
        """Gets the content_type of this CreateGovernancePolicyRequest.

        该字段内容填为 \"application/json;charset=UTF-8\"。

        :return: The content_type of this CreateGovernancePolicyRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this CreateGovernancePolicyRequest.

        该字段内容填为 \"application/json;charset=UTF-8\"。

        :param content_type: The content_type of this CreateGovernancePolicyRequest.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def x_engine_id(self):
        """Gets the x_engine_id of this CreateGovernancePolicyRequest.

        微服务引擎的实例ID

        :return: The x_engine_id of this CreateGovernancePolicyRequest.
        :rtype: str
        """
        return self._x_engine_id

    @x_engine_id.setter
    def x_engine_id(self, x_engine_id):
        """Sets the x_engine_id of this CreateGovernancePolicyRequest.

        微服务引擎的实例ID

        :param x_engine_id: The x_engine_id of this CreateGovernancePolicyRequest.
        :type x_engine_id: str
        """
        self._x_engine_id = x_engine_id

    @property
    def x_enterprise_project_id(self):
        """Gets the x_enterprise_project_id of this CreateGovernancePolicyRequest.

        企业项目ID

        :return: The x_enterprise_project_id of this CreateGovernancePolicyRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        """Sets the x_enterprise_project_id of this CreateGovernancePolicyRequest.

        企业项目ID

        :param x_enterprise_project_id: The x_enterprise_project_id of this CreateGovernancePolicyRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

    @property
    def x_environment(self):
        """Gets the x_environment of this CreateGovernancePolicyRequest.

        所属环境

        :return: The x_environment of this CreateGovernancePolicyRequest.
        :rtype: str
        """
        return self._x_environment

    @x_environment.setter
    def x_environment(self, x_environment):
        """Sets the x_environment of this CreateGovernancePolicyRequest.

        所属环境

        :param x_environment: The x_environment of this CreateGovernancePolicyRequest.
        :type x_environment: str
        """
        self._x_environment = x_environment

    @property
    def kind(self):
        """Gets the kind of this CreateGovernancePolicyRequest.

        治理策略类型

        :return: The kind of this CreateGovernancePolicyRequest.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this CreateGovernancePolicyRequest.

        治理策略类型

        :param kind: The kind of this CreateGovernancePolicyRequest.
        :type kind: str
        """
        self._kind = kind

    @property
    def body(self):
        """Gets the body of this CreateGovernancePolicyRequest.

        :return: The body of this CreateGovernancePolicyRequest.
        :rtype: :class:`huaweicloudsdkcse.v1.CreateGovPolicy`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateGovernancePolicyRequest.

        :param body: The body of this CreateGovernancePolicyRequest.
        :type body: :class:`huaweicloudsdkcse.v1.CreateGovPolicy`
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
        if not isinstance(other, CreateGovernancePolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
