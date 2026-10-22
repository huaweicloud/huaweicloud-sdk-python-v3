# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachV2AgencyPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str'
    }

    attribute_map = {
        'policy_name': 'policy_name'
    }

    def __init__(self, policy_name=None):
        r"""AttachV2AgencyPolicyRequestBody

        The model defined in huaweicloud sdk

        :param policy_name: **参数解释**：权限策略名称，指定要操作的权限策略。 **约束限制**：不支持操作必选策略（AI_DATALAKE_COMMON_POLICY、AI_DATALAKE_SELF_POLICY、AI_DATALAKE_LAKEFORMATION_POLICY、AI_DATALAKE_LTS_POLICY）。 **取值范围**：   - AI_DATALAKE_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN。   - AI_DATALAKE_AOM_POLICY：AOM功能相关权限策略。   - AI_DATALAKE_SWR_POLICY：镜像包注册功能相关权限策略。   - AI_DATALAKE_VPCEP_POLICY：VPCEP相关权限策略。   - AI_DATALAKE_DNS_POLICY：DNS相关权限策略。   - AI_DATALAKE_OBS_POLICY：OBS相关权限策略。   - AI_DATALAKE_VPC_POLICY：VPC相关权限策略。   - AI_DATALAKE_DCS_POLICY：DCS相关权限策略。   - AI_DATALAKE_DEW_POLICY：DEW相关权限策略。 **默认取值**：不涉及。
        :type policy_name: str
        """
        
        

        self._policy_name = None
        self.discriminator = None

        self.policy_name = policy_name

    @property
    def policy_name(self):
        r"""Gets the policy_name of this AttachV2AgencyPolicyRequestBody.

        **参数解释**：权限策略名称，指定要操作的权限策略。 **约束限制**：不支持操作必选策略（AI_DATALAKE_COMMON_POLICY、AI_DATALAKE_SELF_POLICY、AI_DATALAKE_LAKEFORMATION_POLICY、AI_DATALAKE_LTS_POLICY）。 **取值范围**：   - AI_DATALAKE_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN。   - AI_DATALAKE_AOM_POLICY：AOM功能相关权限策略。   - AI_DATALAKE_SWR_POLICY：镜像包注册功能相关权限策略。   - AI_DATALAKE_VPCEP_POLICY：VPCEP相关权限策略。   - AI_DATALAKE_DNS_POLICY：DNS相关权限策略。   - AI_DATALAKE_OBS_POLICY：OBS相关权限策略。   - AI_DATALAKE_VPC_POLICY：VPC相关权限策略。   - AI_DATALAKE_DCS_POLICY：DCS相关权限策略。   - AI_DATALAKE_DEW_POLICY：DEW相关权限策略。 **默认取值**：不涉及。

        :return: The policy_name of this AttachV2AgencyPolicyRequestBody.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this AttachV2AgencyPolicyRequestBody.

        **参数解释**：权限策略名称，指定要操作的权限策略。 **约束限制**：不支持操作必选策略（AI_DATALAKE_COMMON_POLICY、AI_DATALAKE_SELF_POLICY、AI_DATALAKE_LAKEFORMATION_POLICY、AI_DATALAKE_LTS_POLICY）。 **取值范围**：   - AI_DATALAKE_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN。   - AI_DATALAKE_AOM_POLICY：AOM功能相关权限策略。   - AI_DATALAKE_SWR_POLICY：镜像包注册功能相关权限策略。   - AI_DATALAKE_VPCEP_POLICY：VPCEP相关权限策略。   - AI_DATALAKE_DNS_POLICY：DNS相关权限策略。   - AI_DATALAKE_OBS_POLICY：OBS相关权限策略。   - AI_DATALAKE_VPC_POLICY：VPC相关权限策略。   - AI_DATALAKE_DCS_POLICY：DCS相关权限策略。   - AI_DATALAKE_DEW_POLICY：DEW相关权限策略。 **默认取值**：不涉及。

        :param policy_name: The policy_name of this AttachV2AgencyPolicyRequestBody.
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
        if not isinstance(other, AttachV2AgencyPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
