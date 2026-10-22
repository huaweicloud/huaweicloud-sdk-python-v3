# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateV2AgencyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_names': 'list[str]'
    }

    attribute_map = {
        'policy_names': 'policy_names'
    }

    def __init__(self, policy_names=None):
        r"""CreateV2AgencyRequestBody

        The model defined in huaweicloud sdk

        :param policy_names: **参数解释**：权限策略列表，指定需要授权给AI DataLake服务的权限策略，取值包括：   - AI_DATALAKE_COMMON_POLICY：基础服务权限策略。   - AI_DATALAKE_SELF_POLICY：AIDataLake服务自身访问权限策略，用于服务内部资源访问。   - AI_DATALAKE_LAKEFORMATION_POLICY：LakeFormation功能相关权限策略。   - AI_DATALAKE_LTS_POLICY：日志功能相关权限策略。   - AI_DATALAKE_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN。   - AI_DATALAKE_AOM_POLICY：AOM功能相关权限策略。   - AI_DATALAKE_SWR_POLICY：镜像包注册功能相关权限策略。   - AI_DATALAKE_VPCEP_POLICY：网络打通功能相关权限策略。   - AI_DATALAKE_DNS_POLICY：DNS相关权限策略。   - AI_DATALAKE_OBS_POLICY：OBS相关权限策略。   - AI_DATALAKE_VPC_POLICY：VPC相关权限策略。   - AI_DATALAKE_DCS_POLICY：DCS相关权限策略。   - AI_DATALAKE_DEW_POLICY：DEW相关权限策略。 **约束限制**：创建委托时，必须包含以下四个必需策略：   - AI_DATALAKE_COMMON_POLICY：基础服务权限策略。   - AI_DATALAKE_SELF_POLICY：AIDataLake服务自身访问权限策略，用于服务内部资源访问。   - AI_DATALAKE_LAKEFORMATION_POLICY：LakeFormation功能相关权限策略。   - AI_DATALAKE_LTS_POLICY：日志功能相关权限策略。
        :type policy_names: list[str]
        """
        
        

        self._policy_names = None
        self.discriminator = None

        self.policy_names = policy_names

    @property
    def policy_names(self):
        r"""Gets the policy_names of this CreateV2AgencyRequestBody.

        **参数解释**：权限策略列表，指定需要授权给AI DataLake服务的权限策略，取值包括：   - AI_DATALAKE_COMMON_POLICY：基础服务权限策略。   - AI_DATALAKE_SELF_POLICY：AIDataLake服务自身访问权限策略，用于服务内部资源访问。   - AI_DATALAKE_LAKEFORMATION_POLICY：LakeFormation功能相关权限策略。   - AI_DATALAKE_LTS_POLICY：日志功能相关权限策略。   - AI_DATALAKE_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN。   - AI_DATALAKE_AOM_POLICY：AOM功能相关权限策略。   - AI_DATALAKE_SWR_POLICY：镜像包注册功能相关权限策略。   - AI_DATALAKE_VPCEP_POLICY：网络打通功能相关权限策略。   - AI_DATALAKE_DNS_POLICY：DNS相关权限策略。   - AI_DATALAKE_OBS_POLICY：OBS相关权限策略。   - AI_DATALAKE_VPC_POLICY：VPC相关权限策略。   - AI_DATALAKE_DCS_POLICY：DCS相关权限策略。   - AI_DATALAKE_DEW_POLICY：DEW相关权限策略。 **约束限制**：创建委托时，必须包含以下四个必需策略：   - AI_DATALAKE_COMMON_POLICY：基础服务权限策略。   - AI_DATALAKE_SELF_POLICY：AIDataLake服务自身访问权限策略，用于服务内部资源访问。   - AI_DATALAKE_LAKEFORMATION_POLICY：LakeFormation功能相关权限策略。   - AI_DATALAKE_LTS_POLICY：日志功能相关权限策略。

        :return: The policy_names of this CreateV2AgencyRequestBody.
        :rtype: list[str]
        """
        return self._policy_names

    @policy_names.setter
    def policy_names(self, policy_names):
        r"""Sets the policy_names of this CreateV2AgencyRequestBody.

        **参数解释**：权限策略列表，指定需要授权给AI DataLake服务的权限策略，取值包括：   - AI_DATALAKE_COMMON_POLICY：基础服务权限策略。   - AI_DATALAKE_SELF_POLICY：AIDataLake服务自身访问权限策略，用于服务内部资源访问。   - AI_DATALAKE_LAKEFORMATION_POLICY：LakeFormation功能相关权限策略。   - AI_DATALAKE_LTS_POLICY：日志功能相关权限策略。   - AI_DATALAKE_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN。   - AI_DATALAKE_AOM_POLICY：AOM功能相关权限策略。   - AI_DATALAKE_SWR_POLICY：镜像包注册功能相关权限策略。   - AI_DATALAKE_VPCEP_POLICY：网络打通功能相关权限策略。   - AI_DATALAKE_DNS_POLICY：DNS相关权限策略。   - AI_DATALAKE_OBS_POLICY：OBS相关权限策略。   - AI_DATALAKE_VPC_POLICY：VPC相关权限策略。   - AI_DATALAKE_DCS_POLICY：DCS相关权限策略。   - AI_DATALAKE_DEW_POLICY：DEW相关权限策略。 **约束限制**：创建委托时，必须包含以下四个必需策略：   - AI_DATALAKE_COMMON_POLICY：基础服务权限策略。   - AI_DATALAKE_SELF_POLICY：AIDataLake服务自身访问权限策略，用于服务内部资源访问。   - AI_DATALAKE_LAKEFORMATION_POLICY：LakeFormation功能相关权限策略。   - AI_DATALAKE_LTS_POLICY：日志功能相关权限策略。

        :param policy_names: The policy_names of this CreateV2AgencyRequestBody.
        :type policy_names: list[str]
        """
        self._policy_names = policy_names

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
        if not isinstance(other, CreateV2AgencyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
