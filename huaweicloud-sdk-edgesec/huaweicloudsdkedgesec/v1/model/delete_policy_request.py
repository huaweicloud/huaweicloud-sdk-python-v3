# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeletePolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'policy_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'policy_id': 'policy_id'
    }

    def __init__(self, project_id=None, enterprise_project_id=None, policy_id=None):
        """DeletePolicyRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，对应华为云控制台用户名-&gt;我的凭证-&gt;项目列表-&gt;项目ID
        :type project_id: str
        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        :param policy_id: 防护策略id，您可以通过调用查询防护策略列表（ListPolicy）获取策略id
        :type policy_id: str
        """
        
        

        self._project_id = None
        self._enterprise_project_id = None
        self._policy_id = None
        self.discriminator = None

        self.project_id = project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.policy_id = policy_id

    @property
    def project_id(self):
        """Gets the project_id of this DeletePolicyRequest.

        项目ID，对应华为云控制台用户名->我的凭证->项目列表->项目ID

        :return: The project_id of this DeletePolicyRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DeletePolicyRequest.

        项目ID，对应华为云控制台用户名->我的凭证->项目列表->项目ID

        :param project_id: The project_id of this DeletePolicyRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this DeletePolicyRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this DeletePolicyRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this DeletePolicyRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this DeletePolicyRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def policy_id(self):
        """Gets the policy_id of this DeletePolicyRequest.

        防护策略id，您可以通过调用查询防护策略列表（ListPolicy）获取策略id

        :return: The policy_id of this DeletePolicyRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this DeletePolicyRequest.

        防护策略id，您可以通过调用查询防护策略列表（ListPolicy）获取策略id

        :param policy_id: The policy_id of this DeletePolicyRequest.
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
        if not isinstance(other, DeletePolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
