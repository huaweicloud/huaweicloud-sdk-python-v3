# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAiPolicyGroupsRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id_list': 'list[str]'
    }

    attribute_map = {
        'group_id_list': 'group_id_list'
    }

    def __init__(self, group_id_list=None):
        r"""DeleteAiPolicyGroupsRequestInfo

        The model defined in huaweicloud sdk

        :param group_id_list: **参数解释**： 策略组ID列表 **约束限制**： 必填 **取值范围**： 1-200个策略组ID **默认取值**： 不涉及 
        :type group_id_list: list[str]
        """
        
        

        self._group_id_list = None
        self.discriminator = None

        self.group_id_list = group_id_list

    @property
    def group_id_list(self):
        r"""Gets the group_id_list of this DeleteAiPolicyGroupsRequestInfo.

        **参数解释**： 策略组ID列表 **约束限制**： 必填 **取值范围**： 1-200个策略组ID **默认取值**： 不涉及 

        :return: The group_id_list of this DeleteAiPolicyGroupsRequestInfo.
        :rtype: list[str]
        """
        return self._group_id_list

    @group_id_list.setter
    def group_id_list(self, group_id_list):
        r"""Sets the group_id_list of this DeleteAiPolicyGroupsRequestInfo.

        **参数解释**： 策略组ID列表 **约束限制**： 必填 **取值范围**： 1-200个策略组ID **默认取值**： 不涉及 

        :param group_id_list: The group_id_list of this DeleteAiPolicyGroupsRequestInfo.
        :type group_id_list: list[str]
        """
        self._group_id_list = group_id_list

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
        if not isinstance(other, DeleteAiPolicyGroupsRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
