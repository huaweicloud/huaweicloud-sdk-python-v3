# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRaspPolicyDetailResponse(SdkResponse):

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
        'os_type': 'str',
        'rule_list': 'list[CheckFeatureRuleInfo]'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'os_type': 'os_type',
        'rule_list': 'rule_list'
    }

    def __init__(self, policy_name=None, os_type=None, rule_list=None):
        r"""ShowRaspPolicyDetailResponse

        The model defined in huaweicloud sdk

        :param policy_name: 防护策略名称
        :type policy_name: str
        :param os_type: 操作系统类型
        :type os_type: str
        :param rule_list: list
        :type rule_list: list[:class:`huaweicloudsdkhss.v5.CheckFeatureRuleInfo`]
        """
        
        super(ShowRaspPolicyDetailResponse, self).__init__()

        self._policy_name = None
        self._os_type = None
        self._rule_list = None
        self.discriminator = None

        if policy_name is not None:
            self.policy_name = policy_name
        if os_type is not None:
            self.os_type = os_type
        if rule_list is not None:
            self.rule_list = rule_list

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ShowRaspPolicyDetailResponse.

        防护策略名称

        :return: The policy_name of this ShowRaspPolicyDetailResponse.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ShowRaspPolicyDetailResponse.

        防护策略名称

        :param policy_name: The policy_name of this ShowRaspPolicyDetailResponse.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def os_type(self):
        r"""Gets the os_type of this ShowRaspPolicyDetailResponse.

        操作系统类型

        :return: The os_type of this ShowRaspPolicyDetailResponse.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ShowRaspPolicyDetailResponse.

        操作系统类型

        :param os_type: The os_type of this ShowRaspPolicyDetailResponse.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def rule_list(self):
        r"""Gets the rule_list of this ShowRaspPolicyDetailResponse.

        list

        :return: The rule_list of this ShowRaspPolicyDetailResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.CheckFeatureRuleInfo`]
        """
        return self._rule_list

    @rule_list.setter
    def rule_list(self, rule_list):
        r"""Sets the rule_list of this ShowRaspPolicyDetailResponse.

        list

        :param rule_list: The rule_list of this ShowRaspPolicyDetailResponse.
        :type rule_list: list[:class:`huaweicloudsdkhss.v5.CheckFeatureRuleInfo`]
        """
        self._rule_list = rule_list

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
        if not isinstance(other, ShowRaspPolicyDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
