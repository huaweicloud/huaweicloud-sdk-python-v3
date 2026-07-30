# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CopyAiPolicyGroupRequestInfo:

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
        'group_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'group_name': 'group_name',
        'description': 'description'
    }

    def __init__(self, group_id=None, group_name=None, description=None):
        r"""CopyAiPolicyGroupRequestInfo

        The model defined in huaweicloud sdk

        :param group_id: **参数解释**： 策略组ID **约束限制**： 必填 **取值范围**： 字符长度1-20位 **默认取值**： 不涉及 
        :type group_id: str
        :param group_name: **参数解释**： 策略组名称 **约束限制**： 必填 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 
        :type group_name: str
        :param description: **参数解释**： 策略描述 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 
        :type description: str
        """
        
        

        self._group_id = None
        self._group_name = None
        self._description = None
        self.discriminator = None

        self.group_id = group_id
        self.group_name = group_name
        if description is not None:
            self.description = description

    @property
    def group_id(self):
        r"""Gets the group_id of this CopyAiPolicyGroupRequestInfo.

        **参数解释**： 策略组ID **约束限制**： 必填 **取值范围**： 字符长度1-20位 **默认取值**： 不涉及 

        :return: The group_id of this CopyAiPolicyGroupRequestInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this CopyAiPolicyGroupRequestInfo.

        **参数解释**： 策略组ID **约束限制**： 必填 **取值范围**： 字符长度1-20位 **默认取值**： 不涉及 

        :param group_id: The group_id of this CopyAiPolicyGroupRequestInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this CopyAiPolicyGroupRequestInfo.

        **参数解释**： 策略组名称 **约束限制**： 必填 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :return: The group_name of this CopyAiPolicyGroupRequestInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this CopyAiPolicyGroupRequestInfo.

        **参数解释**： 策略组名称 **约束限制**： 必填 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :param group_name: The group_name of this CopyAiPolicyGroupRequestInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def description(self):
        r"""Gets the description of this CopyAiPolicyGroupRequestInfo.

        **参数解释**： 策略描述 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :return: The description of this CopyAiPolicyGroupRequestInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CopyAiPolicyGroupRequestInfo.

        **参数解释**： 策略描述 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :param description: The description of this CopyAiPolicyGroupRequestInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CopyAiPolicyGroupRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
