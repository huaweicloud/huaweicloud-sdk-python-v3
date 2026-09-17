# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelateAction:

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
        'action_display_name': 'str',
        'relate_object_list': 'list[RelationObject]'
    }

    attribute_map = {
        'action': 'action',
        'action_display_name': 'action_display_name',
        'relate_object_list': 'relate_object_list'
    }

    def __init__(self, action=None, action_display_name=None, relate_object_list=None):
        r"""RelateAction

        The model defined in huaweicloud sdk

        :param action: **参数解释**： 关联行为code。 **取值范围**： 不涉及。
        :type action: str
        :param action_display_name: **参数解释**： 关联行为名称。 **取值范围**： 不涉及。
        :type action_display_name: str
        :param relate_object_list: **参数解释**： 关联的对象列表。 **取值范围**： 不涉及。
        :type relate_object_list: list[:class:`huaweicloudsdkprojectman.v4.RelationObject`]
        """
        
        

        self._action = None
        self._action_display_name = None
        self._relate_object_list = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if action_display_name is not None:
            self.action_display_name = action_display_name
        if relate_object_list is not None:
            self.relate_object_list = relate_object_list

    @property
    def action(self):
        r"""Gets the action of this RelateAction.

        **参数解释**： 关联行为code。 **取值范围**： 不涉及。

        :return: The action of this RelateAction.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this RelateAction.

        **参数解释**： 关联行为code。 **取值范围**： 不涉及。

        :param action: The action of this RelateAction.
        :type action: str
        """
        self._action = action

    @property
    def action_display_name(self):
        r"""Gets the action_display_name of this RelateAction.

        **参数解释**： 关联行为名称。 **取值范围**： 不涉及。

        :return: The action_display_name of this RelateAction.
        :rtype: str
        """
        return self._action_display_name

    @action_display_name.setter
    def action_display_name(self, action_display_name):
        r"""Sets the action_display_name of this RelateAction.

        **参数解释**： 关联行为名称。 **取值范围**： 不涉及。

        :param action_display_name: The action_display_name of this RelateAction.
        :type action_display_name: str
        """
        self._action_display_name = action_display_name

    @property
    def relate_object_list(self):
        r"""Gets the relate_object_list of this RelateAction.

        **参数解释**： 关联的对象列表。 **取值范围**： 不涉及。

        :return: The relate_object_list of this RelateAction.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.RelationObject`]
        """
        return self._relate_object_list

    @relate_object_list.setter
    def relate_object_list(self, relate_object_list):
        r"""Sets the relate_object_list of this RelateAction.

        **参数解释**： 关联的对象列表。 **取值范围**： 不涉及。

        :param relate_object_list: The relate_object_list of this RelateAction.
        :type relate_object_list: list[:class:`huaweicloudsdkprojectman.v4.RelationObject`]
        """
        self._relate_object_list = relate_object_list

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
        if not isinstance(other, RelateAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
