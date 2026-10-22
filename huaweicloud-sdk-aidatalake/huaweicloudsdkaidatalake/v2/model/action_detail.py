# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionDetail:

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
        'action_description': 'str'
    }

    attribute_map = {
        'action': 'action',
        'action_description': 'action_description'
    }

    def __init__(self, action=None, action_description=None):
        r"""ActionDetail

        The model defined in huaweicloud sdk

        :param action: **参数解释**：权限操作内容。 **取值范围**：只能由英文字母、数字、冒号及特殊字符组成，长度0~128个字符。
        :type action: str
        :param action_description: **参数解释**：权限操作的描述，说明该操作的具体含义。 **取值范围**：支持中文字符、英文字母、数字及特殊字符，长度0~1024个字符。
        :type action_description: str
        """
        
        

        self._action = None
        self._action_description = None
        self.discriminator = None

        self.action = action
        self.action_description = action_description

    @property
    def action(self):
        r"""Gets the action of this ActionDetail.

        **参数解释**：权限操作内容。 **取值范围**：只能由英文字母、数字、冒号及特殊字符组成，长度0~128个字符。

        :return: The action of this ActionDetail.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ActionDetail.

        **参数解释**：权限操作内容。 **取值范围**：只能由英文字母、数字、冒号及特殊字符组成，长度0~128个字符。

        :param action: The action of this ActionDetail.
        :type action: str
        """
        self._action = action

    @property
    def action_description(self):
        r"""Gets the action_description of this ActionDetail.

        **参数解释**：权限操作的描述，说明该操作的具体含义。 **取值范围**：支持中文字符、英文字母、数字及特殊字符，长度0~1024个字符。

        :return: The action_description of this ActionDetail.
        :rtype: str
        """
        return self._action_description

    @action_description.setter
    def action_description(self, action_description):
        r"""Sets the action_description of this ActionDetail.

        **参数解释**：权限操作的描述，说明该操作的具体含义。 **取值范围**：支持中文字符、英文字母、数字及特殊字符，长度0~1024个字符。

        :param action_description: The action_description of this ActionDetail.
        :type action_description: str
        """
        self._action_description = action_description

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
        if not isinstance(other, ActionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
