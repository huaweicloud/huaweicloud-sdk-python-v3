# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddPolicyRequest:

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
        'os_type': 'str',
        'policy_name': 'str',
        'body': 'AddPolicyRequestInfo'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'os_type': 'os_type',
        'policy_name': 'policy_name',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, os_type=None, policy_name=None, body=None):
        r"""AddPolicyRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param os_type: 操作系统类型，包含如下2种。 - Linux - Windows
        :type os_type: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param body: Body of the AddPolicyRequest
        :type body: :class:`huaweicloudsdkhss.v5.AddPolicyRequestInfo`
        """
        
        

        self._enterprise_project_id = None
        self._os_type = None
        self._policy_name = None
        self._body = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if os_type is not None:
            self.os_type = os_type
        self.policy_name = policy_name
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this AddPolicyRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this AddPolicyRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this AddPolicyRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this AddPolicyRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def os_type(self):
        r"""Gets the os_type of this AddPolicyRequest.

        操作系统类型，包含如下2种。 - Linux - Windows

        :return: The os_type of this AddPolicyRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this AddPolicyRequest.

        操作系统类型，包含如下2种。 - Linux - Windows

        :param os_type: The os_type of this AddPolicyRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def policy_name(self):
        r"""Gets the policy_name of this AddPolicyRequest.

        策略名称

        :return: The policy_name of this AddPolicyRequest.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this AddPolicyRequest.

        策略名称

        :param policy_name: The policy_name of this AddPolicyRequest.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def body(self):
        r"""Gets the body of this AddPolicyRequest.

        :return: The body of this AddPolicyRequest.
        :rtype: :class:`huaweicloudsdkhss.v5.AddPolicyRequestInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AddPolicyRequest.

        :param body: The body of this AddPolicyRequest.
        :type body: :class:`huaweicloudsdkhss.v5.AddPolicyRequestInfo`
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
        if not isinstance(other, AddPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
