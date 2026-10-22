# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetachV2AgencyPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency_name': 'str',
        'policy_name': 'str'
    }

    attribute_map = {
        'agency_name': 'agency_name',
        'policy_name': 'policy_name'
    }

    def __init__(self, agency_name=None, policy_name=None):
        r"""DetachV2AgencyPolicyRequest

        The model defined in huaweicloud sdk

        :param agency_name: **参数解释**：委托名称。 **约束限制**：固定值ai_datalake_admin_trust。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type agency_name: str
        :param policy_name: **参数解释**：权限策略名称，使用AI DataLake的功能，需要授权一些权限策略。 **约束限制**：不支持移除必选策略。 **取值范围**：   - AI_DATALAKE_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN。   - AI_DATALAKE_AOM_POLICY：AOM功能相关权限策略。   - AI_DATALAKE_SWR_POLICY：镜像包注册功能相关权限策略。   - AI_DATALAKE_VPCEP_POLICY：网络打通功能相关权限策略。   - AI_DATALAKE_DNS_POLICY：DNS相关权限策略。   - AI_DATALAKE_OBS_POLICY：OBS相关权限策略。   - AI_DATALAKE_VPC_POLICY：VPC相关权限策略。   - AI_DATALAKE_DCS_POLICY：DCS相关权限策略。   - AI_DATALAKE_DEW_POLICY：DEW相关权限策略。 **默认取值**：不涉及。
        :type policy_name: str
        """
        
        

        self._agency_name = None
        self._policy_name = None
        self.discriminator = None

        self.agency_name = agency_name
        self.policy_name = policy_name

    @property
    def agency_name(self):
        r"""Gets the agency_name of this DetachV2AgencyPolicyRequest.

        **参数解释**：委托名称。 **约束限制**：固定值ai_datalake_admin_trust。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The agency_name of this DetachV2AgencyPolicyRequest.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this DetachV2AgencyPolicyRequest.

        **参数解释**：委托名称。 **约束限制**：固定值ai_datalake_admin_trust。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param agency_name: The agency_name of this DetachV2AgencyPolicyRequest.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def policy_name(self):
        r"""Gets the policy_name of this DetachV2AgencyPolicyRequest.

        **参数解释**：权限策略名称，使用AI DataLake的功能，需要授权一些权限策略。 **约束限制**：不支持移除必选策略。 **取值范围**：   - AI_DATALAKE_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN。   - AI_DATALAKE_AOM_POLICY：AOM功能相关权限策略。   - AI_DATALAKE_SWR_POLICY：镜像包注册功能相关权限策略。   - AI_DATALAKE_VPCEP_POLICY：网络打通功能相关权限策略。   - AI_DATALAKE_DNS_POLICY：DNS相关权限策略。   - AI_DATALAKE_OBS_POLICY：OBS相关权限策略。   - AI_DATALAKE_VPC_POLICY：VPC相关权限策略。   - AI_DATALAKE_DCS_POLICY：DCS相关权限策略。   - AI_DATALAKE_DEW_POLICY：DEW相关权限策略。 **默认取值**：不涉及。

        :return: The policy_name of this DetachV2AgencyPolicyRequest.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this DetachV2AgencyPolicyRequest.

        **参数解释**：权限策略名称，使用AI DataLake的功能，需要授权一些权限策略。 **约束限制**：不支持移除必选策略。 **取值范围**：   - AI_DATALAKE_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN。   - AI_DATALAKE_AOM_POLICY：AOM功能相关权限策略。   - AI_DATALAKE_SWR_POLICY：镜像包注册功能相关权限策略。   - AI_DATALAKE_VPCEP_POLICY：网络打通功能相关权限策略。   - AI_DATALAKE_DNS_POLICY：DNS相关权限策略。   - AI_DATALAKE_OBS_POLICY：OBS相关权限策略。   - AI_DATALAKE_VPC_POLICY：VPC相关权限策略。   - AI_DATALAKE_DCS_POLICY：DCS相关权限策略。   - AI_DATALAKE_DEW_POLICY：DEW相关权限策略。 **默认取值**：不涉及。

        :param policy_name: The policy_name of this DetachV2AgencyPolicyRequest.
        :type policy_name: str
        """
        self._policy_name = policy_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DetachV2AgencyPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
