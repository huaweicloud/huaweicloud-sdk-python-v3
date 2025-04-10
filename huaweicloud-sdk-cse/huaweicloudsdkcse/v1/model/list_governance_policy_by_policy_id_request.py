# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGovernancePolicyByPolicyIdRequest:

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
        'policy_id': 'str'
    }

    attribute_map = {
        'content_type': 'Content-Type',
        'x_engine_id': 'x-engine-id',
        'x_enterprise_project_id': 'X-Enterprise-Project-ID',
        'x_environment': 'x-environment',
        'kind': 'kind',
        'policy_id': 'policy_id'
    }

    def __init__(self, content_type=None, x_engine_id=None, x_enterprise_project_id=None, x_environment=None, kind=None, policy_id=None):
        r"""ListGovernancePolicyByPolicyIdRequest

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
        :param policy_id: 治理策略id
        :type policy_id: str
        """
        
        

        self._content_type = None
        self._x_engine_id = None
        self._x_enterprise_project_id = None
        self._x_environment = None
        self._kind = None
        self._policy_id = None
        self.discriminator = None

        self.content_type = content_type
        self.x_engine_id = x_engine_id
        self.x_enterprise_project_id = x_enterprise_project_id
        if x_environment is not None:
            self.x_environment = x_environment
        self.kind = kind
        self.policy_id = policy_id

    @property
    def content_type(self):
        r"""Gets the content_type of this ListGovernancePolicyByPolicyIdRequest.

        该字段内容填为 \"application/json;charset=UTF-8\"。

        :return: The content_type of this ListGovernancePolicyByPolicyIdRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this ListGovernancePolicyByPolicyIdRequest.

        该字段内容填为 \"application/json;charset=UTF-8\"。

        :param content_type: The content_type of this ListGovernancePolicyByPolicyIdRequest.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def x_engine_id(self):
        r"""Gets the x_engine_id of this ListGovernancePolicyByPolicyIdRequest.

        微服务引擎的实例ID

        :return: The x_engine_id of this ListGovernancePolicyByPolicyIdRequest.
        :rtype: str
        """
        return self._x_engine_id

    @x_engine_id.setter
    def x_engine_id(self, x_engine_id):
        r"""Sets the x_engine_id of this ListGovernancePolicyByPolicyIdRequest.

        微服务引擎的实例ID

        :param x_engine_id: The x_engine_id of this ListGovernancePolicyByPolicyIdRequest.
        :type x_engine_id: str
        """
        self._x_engine_id = x_engine_id

    @property
    def x_enterprise_project_id(self):
        r"""Gets the x_enterprise_project_id of this ListGovernancePolicyByPolicyIdRequest.

        企业项目ID

        :return: The x_enterprise_project_id of this ListGovernancePolicyByPolicyIdRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        r"""Sets the x_enterprise_project_id of this ListGovernancePolicyByPolicyIdRequest.

        企业项目ID

        :param x_enterprise_project_id: The x_enterprise_project_id of this ListGovernancePolicyByPolicyIdRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

    @property
    def x_environment(self):
        r"""Gets the x_environment of this ListGovernancePolicyByPolicyIdRequest.

        所属环境

        :return: The x_environment of this ListGovernancePolicyByPolicyIdRequest.
        :rtype: str
        """
        return self._x_environment

    @x_environment.setter
    def x_environment(self, x_environment):
        r"""Sets the x_environment of this ListGovernancePolicyByPolicyIdRequest.

        所属环境

        :param x_environment: The x_environment of this ListGovernancePolicyByPolicyIdRequest.
        :type x_environment: str
        """
        self._x_environment = x_environment

    @property
    def kind(self):
        r"""Gets the kind of this ListGovernancePolicyByPolicyIdRequest.

        治理策略类型

        :return: The kind of this ListGovernancePolicyByPolicyIdRequest.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ListGovernancePolicyByPolicyIdRequest.

        治理策略类型

        :param kind: The kind of this ListGovernancePolicyByPolicyIdRequest.
        :type kind: str
        """
        self._kind = kind

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ListGovernancePolicyByPolicyIdRequest.

        治理策略id

        :return: The policy_id of this ListGovernancePolicyByPolicyIdRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ListGovernancePolicyByPolicyIdRequest.

        治理策略id

        :param policy_id: The policy_id of this ListGovernancePolicyByPolicyIdRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

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
        if not isinstance(other, ListGovernancePolicyByPolicyIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
