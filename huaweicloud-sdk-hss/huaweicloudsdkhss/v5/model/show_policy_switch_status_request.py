# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPolicySwitchStatusRequest:

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
        'policy_name': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'policy_name': 'policy_name'
    }

    def __init__(self, enterprise_project_id=None, policy_name=None):
        r"""ShowPolicySwitchStatusRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param policy_name: **参数解释**： 策略名称 **约束限制**： 不涉及 **取值范围**： - sp_feature：自保护策略。  **默认取值**： 不涉及 
        :type policy_name: str
        """
        
        

        self._enterprise_project_id = None
        self._policy_name = None
        self.discriminator = None

        self.enterprise_project_id = enterprise_project_id
        self.policy_name = policy_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowPolicySwitchStatusRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowPolicySwitchStatusRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowPolicySwitchStatusRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowPolicySwitchStatusRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ShowPolicySwitchStatusRequest.

        **参数解释**： 策略名称 **约束限制**： 不涉及 **取值范围**： - sp_feature：自保护策略。  **默认取值**： 不涉及 

        :return: The policy_name of this ShowPolicySwitchStatusRequest.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ShowPolicySwitchStatusRequest.

        **参数解释**： 策略名称 **约束限制**： 不涉及 **取值范围**： - sp_feature：自保护策略。  **默认取值**： 不涉及 

        :param policy_name: The policy_name of this ShowPolicySwitchStatusRequest.
        :type policy_name: str
        """
        self._policy_name = policy_name

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
        if not isinstance(other, ShowPolicySwitchStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
