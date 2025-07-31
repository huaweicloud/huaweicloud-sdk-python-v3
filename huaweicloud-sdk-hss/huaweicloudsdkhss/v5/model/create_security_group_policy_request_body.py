# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecurityGroupPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'workload_id': 'str',
        'workload_name': 'str',
        'workload_type': 'str',
        'security_groups': 'list[SecurityGroup]'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'workload_id': 'workload_id',
        'workload_name': 'workload_name',
        'workload_type': 'workload_type',
        'security_groups': 'security_groups'
    }

    def __init__(self, policy_name=None, workload_id=None, workload_name=None, workload_type=None, security_groups=None):
        r"""CreateSecurityGroupPolicyRequestBody

        The model defined in huaweicloud sdk

        :param policy_name: 策略名称
        :type policy_name: str
        :param workload_id: 工作负载ID
        :type workload_id: str
        :param workload_name: 工作负载名称
        :type workload_name: str
        :param workload_type: 工作负载类型
        :type workload_type: str
        :param security_groups: 安全组列表
        :type security_groups: list[:class:`huaweicloudsdkhss.v5.SecurityGroup`]
        """
        
        

        self._policy_name = None
        self._workload_id = None
        self._workload_name = None
        self._workload_type = None
        self._security_groups = None
        self.discriminator = None

        self.policy_name = policy_name
        self.workload_id = workload_id
        self.workload_name = workload_name
        self.workload_type = workload_type
        self.security_groups = security_groups

    @property
    def policy_name(self):
        r"""Gets the policy_name of this CreateSecurityGroupPolicyRequestBody.

        策略名称

        :return: The policy_name of this CreateSecurityGroupPolicyRequestBody.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this CreateSecurityGroupPolicyRequestBody.

        策略名称

        :param policy_name: The policy_name of this CreateSecurityGroupPolicyRequestBody.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def workload_id(self):
        r"""Gets the workload_id of this CreateSecurityGroupPolicyRequestBody.

        工作负载ID

        :return: The workload_id of this CreateSecurityGroupPolicyRequestBody.
        :rtype: str
        """
        return self._workload_id

    @workload_id.setter
    def workload_id(self, workload_id):
        r"""Sets the workload_id of this CreateSecurityGroupPolicyRequestBody.

        工作负载ID

        :param workload_id: The workload_id of this CreateSecurityGroupPolicyRequestBody.
        :type workload_id: str
        """
        self._workload_id = workload_id

    @property
    def workload_name(self):
        r"""Gets the workload_name of this CreateSecurityGroupPolicyRequestBody.

        工作负载名称

        :return: The workload_name of this CreateSecurityGroupPolicyRequestBody.
        :rtype: str
        """
        return self._workload_name

    @workload_name.setter
    def workload_name(self, workload_name):
        r"""Sets the workload_name of this CreateSecurityGroupPolicyRequestBody.

        工作负载名称

        :param workload_name: The workload_name of this CreateSecurityGroupPolicyRequestBody.
        :type workload_name: str
        """
        self._workload_name = workload_name

    @property
    def workload_type(self):
        r"""Gets the workload_type of this CreateSecurityGroupPolicyRequestBody.

        工作负载类型

        :return: The workload_type of this CreateSecurityGroupPolicyRequestBody.
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        r"""Sets the workload_type of this CreateSecurityGroupPolicyRequestBody.

        工作负载类型

        :param workload_type: The workload_type of this CreateSecurityGroupPolicyRequestBody.
        :type workload_type: str
        """
        self._workload_type = workload_type

    @property
    def security_groups(self):
        r"""Gets the security_groups of this CreateSecurityGroupPolicyRequestBody.

        安全组列表

        :return: The security_groups of this CreateSecurityGroupPolicyRequestBody.
        :rtype: list[:class:`huaweicloudsdkhss.v5.SecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this CreateSecurityGroupPolicyRequestBody.

        安全组列表

        :param security_groups: The security_groups of this CreateSecurityGroupPolicyRequestBody.
        :type security_groups: list[:class:`huaweicloudsdkhss.v5.SecurityGroup`]
        """
        self._security_groups = security_groups

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
        if not isinstance(other, CreateSecurityGroupPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
