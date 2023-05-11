# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCcRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'policy_id': 'str',
        'body': 'CreateCcRuleRequestBody'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'policy_id': 'policy_id',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, policy_id=None, body=None):
        """CreateCcRuleRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        :param policy_id: 策略id（策略id从查询防护策略列表接口获取）
        :type policy_id: str
        :param body: Body of the CreateCcRuleRequest
        :type body: :class:`huaweicloudsdkwaf.v1.CreateCcRuleRequestBody`
        """
        
        

        self._enterprise_project_id = None
        self._policy_id = None
        self._body = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.policy_id = policy_id
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateCcRuleRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this CreateCcRuleRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateCcRuleRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this CreateCcRuleRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def policy_id(self):
        """Gets the policy_id of this CreateCcRuleRequest.

        策略id（策略id从查询防护策略列表接口获取）

        :return: The policy_id of this CreateCcRuleRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this CreateCcRuleRequest.

        策略id（策略id从查询防护策略列表接口获取）

        :param policy_id: The policy_id of this CreateCcRuleRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def body(self):
        """Gets the body of this CreateCcRuleRequest.

        :return: The body of this CreateCcRuleRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateCcRuleRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateCcRuleRequest.

        :param body: The body of this CreateCcRuleRequest.
        :type body: :class:`huaweicloudsdkwaf.v1.CreateCcRuleRequestBody`
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
        if not isinstance(other, CreateCcRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
