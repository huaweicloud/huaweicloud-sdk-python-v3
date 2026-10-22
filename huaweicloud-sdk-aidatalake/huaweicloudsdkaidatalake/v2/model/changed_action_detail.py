# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangedActionDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'action_description': 'str',
        'change_type': 'str'
    }

    attribute_map = {
        'action': 'action',
        'action_description': 'action_description',
        'change_type': 'change_type'
    }

    def __init__(self, action=None, action_description=None, change_type=None):
        r"""ChangedActionDetail

        The model defined in huaweicloud sdk

        :param action: **参数解释**：权限操作内容。 **取值范围**：长度0~256个字符。
        :type action: str
        :param action_description: **参数解释**：权限操作的描述信息。 **取值范围**：不涉及。
        :type action_description: str
        :param change_type: **参数解释**：变更类型。added 表示需要新增的权限操作。 **取值范围**：   - added：需要新增
        :type change_type: str
        """
        
        

        self._action = None
        self._action_description = None
        self._change_type = None
        self.discriminator = None

        self.action = action
        self.action_description = action_description
        self.change_type = change_type

    @property
    def action(self):
        r"""Gets the action of this ChangedActionDetail.

        **参数解释**：权限操作内容。 **取值范围**：长度0~256个字符。

        :return: The action of this ChangedActionDetail.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ChangedActionDetail.

        **参数解释**：权限操作内容。 **取值范围**：长度0~256个字符。

        :param action: The action of this ChangedActionDetail.
        :type action: str
        """
        self._action = action

    @property
    def action_description(self):
        r"""Gets the action_description of this ChangedActionDetail.

        **参数解释**：权限操作的描述信息。 **取值范围**：不涉及。

        :return: The action_description of this ChangedActionDetail.
        :rtype: str
        """
        return self._action_description

    @action_description.setter
    def action_description(self, action_description):
        r"""Sets the action_description of this ChangedActionDetail.

        **参数解释**：权限操作的描述信息。 **取值范围**：不涉及。

        :param action_description: The action_description of this ChangedActionDetail.
        :type action_description: str
        """
        self._action_description = action_description

    @property
    def change_type(self):
        r"""Gets the change_type of this ChangedActionDetail.

        **参数解释**：变更类型。added 表示需要新增的权限操作。 **取值范围**：   - added：需要新增

        :return: The change_type of this ChangedActionDetail.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        r"""Sets the change_type of this ChangedActionDetail.

        **参数解释**：变更类型。added 表示需要新增的权限操作。 **取值范围**：   - added：需要新增

        :param change_type: The change_type of this ChangedActionDetail.
        :type change_type: str
        """
        self._change_type = change_type

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
        if not isinstance(other, ChangedActionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
