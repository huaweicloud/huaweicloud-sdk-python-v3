# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecurityGroupPolicyRequestBody:

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
        'policy_name': 'str',
        'security_groups': 'list[SecurityGroup]'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'security_groups': 'security_groups'
    }

    def __init__(self, policy_id=None, policy_name=None, security_groups=None):
        r"""UpdateSecurityGroupPolicyRequestBody

        The model defined in huaweicloud sdk

        :param policy_id: 安全策略ID
        :type policy_id: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param security_groups: 安全组列表
        :type security_groups: list[:class:`huaweicloudsdkhss.v5.SecurityGroup`]
        """
        
        

        self._policy_id = None
        self._policy_name = None
        self._security_groups = None
        self.discriminator = None

        self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        self.security_groups = security_groups

    @property
    def policy_id(self):
        r"""Gets the policy_id of this UpdateSecurityGroupPolicyRequestBody.

        安全策略ID

        :return: The policy_id of this UpdateSecurityGroupPolicyRequestBody.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this UpdateSecurityGroupPolicyRequestBody.

        安全策略ID

        :param policy_id: The policy_id of this UpdateSecurityGroupPolicyRequestBody.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this UpdateSecurityGroupPolicyRequestBody.

        策略名称

        :return: The policy_name of this UpdateSecurityGroupPolicyRequestBody.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this UpdateSecurityGroupPolicyRequestBody.

        策略名称

        :param policy_name: The policy_name of this UpdateSecurityGroupPolicyRequestBody.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def security_groups(self):
        r"""Gets the security_groups of this UpdateSecurityGroupPolicyRequestBody.

        安全组列表

        :return: The security_groups of this UpdateSecurityGroupPolicyRequestBody.
        :rtype: list[:class:`huaweicloudsdkhss.v5.SecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this UpdateSecurityGroupPolicyRequestBody.

        安全组列表

        :param security_groups: The security_groups of this UpdateSecurityGroupPolicyRequestBody.
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
        if not isinstance(other, UpdateSecurityGroupPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
