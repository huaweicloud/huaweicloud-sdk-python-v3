# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBotMTrafficDetectionConditionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'enterprise_project_id': 'str',
        'body': 'SaveTrafficDetectionConditionRequestBody'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'enterprise_project_id': 'enterprise_project_id',
        'body': 'body'
    }

    def __init__(self, policy_id=None, enterprise_project_id=None, body=None):
        r"""CreateBotMTrafficDetectionConditionRequest

        The model defined in huaweicloud sdk

        :param policy_id: policyId
        :type policy_id: str
        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        :param body: Body of the CreateBotMTrafficDetectionConditionRequest
        :type body: :class:`huaweicloudsdkwaf.v1.SaveTrafficDetectionConditionRequestBody`
        """
        
        

        self._policy_id = None
        self._enterprise_project_id = None
        self._body = None
        self.discriminator = None

        self.policy_id = policy_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if body is not None:
            self.body = body

    @property
    def policy_id(self):
        r"""Gets the policy_id of this CreateBotMTrafficDetectionConditionRequest.

        policyId

        :return: The policy_id of this CreateBotMTrafficDetectionConditionRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this CreateBotMTrafficDetectionConditionRequest.

        policyId

        :param policy_id: The policy_id of this CreateBotMTrafficDetectionConditionRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateBotMTrafficDetectionConditionRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this CreateBotMTrafficDetectionConditionRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateBotMTrafficDetectionConditionRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this CreateBotMTrafficDetectionConditionRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def body(self):
        r"""Gets the body of this CreateBotMTrafficDetectionConditionRequest.

        :return: The body of this CreateBotMTrafficDetectionConditionRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.SaveTrafficDetectionConditionRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateBotMTrafficDetectionConditionRequest.

        :param body: The body of this CreateBotMTrafficDetectionConditionRequest.
        :type body: :class:`huaweicloudsdkwaf.v1.SaveTrafficDetectionConditionRequestBody`
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
        if not isinstance(other, CreateBotMTrafficDetectionConditionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
