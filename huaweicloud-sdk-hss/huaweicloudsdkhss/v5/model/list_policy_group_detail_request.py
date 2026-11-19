# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPolicyGroupDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'enterprise_project_id': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'group_id': 'group_id',
        'enterprise_project_id': 'enterprise_project_id',
        'enabled': 'enabled'
    }

    def __init__(self, group_id=None, enterprise_project_id=None, enabled=None):
        r"""ListPolicyGroupDetailRequest

        The model defined in huaweicloud sdk

        :param group_id: **参数解释**： 策略组ID **约束限制**： 必填 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 
        :type group_id: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param enabled: **参数解释**： 策略开启状态 **约束限制**： 不涉及 **取值范围**： - true：开启 - false：关闭  **默认取值**： 不涉及 
        :type enabled: bool
        """
        
        

        self._group_id = None
        self._enterprise_project_id = None
        self._enabled = None
        self.discriminator = None

        self.group_id = group_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enabled is not None:
            self.enabled = enabled

    @property
    def group_id(self):
        r"""Gets the group_id of this ListPolicyGroupDetailRequest.

        **参数解释**： 策略组ID **约束限制**： 必填 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :return: The group_id of this ListPolicyGroupDetailRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListPolicyGroupDetailRequest.

        **参数解释**： 策略组ID **约束限制**： 必填 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :param group_id: The group_id of this ListPolicyGroupDetailRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListPolicyGroupDetailRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListPolicyGroupDetailRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListPolicyGroupDetailRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListPolicyGroupDetailRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enabled(self):
        r"""Gets the enabled of this ListPolicyGroupDetailRequest.

        **参数解释**： 策略开启状态 **约束限制**： 不涉及 **取值范围**： - true：开启 - false：关闭  **默认取值**： 不涉及 

        :return: The enabled of this ListPolicyGroupDetailRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ListPolicyGroupDetailRequest.

        **参数解释**： 策略开启状态 **约束限制**： 不涉及 **取值范围**： - true：开启 - false：关闭  **默认取值**： 不涉及 

        :param enabled: The enabled of this ListPolicyGroupDetailRequest.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, ListPolicyGroupDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
