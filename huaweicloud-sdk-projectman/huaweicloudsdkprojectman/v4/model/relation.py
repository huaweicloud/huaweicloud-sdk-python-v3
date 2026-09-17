# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Relation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'categories': 'list[str]',
        'link_field_code': 'str',
        'relation_name': 'str',
        'description': 'str',
        'display_scope': 'str',
        'actions': 'list[RelateAction]',
        'relate_type': 'str'
    }

    attribute_map = {
        'type': 'type',
        'categories': 'categories',
        'link_field_code': 'link_field_code',
        'relation_name': 'relation_name',
        'description': 'description',
        'display_scope': 'display_scope',
        'actions': 'actions',
        'relate_type': 'relate_type'
    }

    def __init__(self, type=None, categories=None, link_field_code=None, relation_name=None, description=None, display_scope=None, actions=None, relate_type=None):
        r"""Relation

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 关系code。 **取值范围**： 不涉及。
        :type type: str
        :param categories: **参数解释**： 关联的工作项code列表。 **取值范围**： 不涉及。
        :type categories: list[str]
        :param link_field_code: **参数解释**： 工作流场景使用，前置校验中的关联关系校验字段。 **取值范围**： 不涉及。
        :type link_field_code: str
        :param relation_name: **参数解释**： 关系名称，在工作项详情关联项下左侧显示。 **取值范围**： 不涉及。
        :type relation_name: str
        :param description: **参数解释**： 关系描述。 **取值范围**： 不涉及。
        :type description: str
        :param display_scope: **参数解释**： 展示范围。 **取值范围**： 不涉及。
        :type display_scope: str
        :param actions: **参数解释**： 动作行为。 **取值范围**： 不涉及。
        :type actions: list[:class:`huaweicloudsdkprojectman.v4.RelateAction`]
        :param relate_type: **参数解释**： 动作行为。 **取值范围**： - ONE_TO_ONE 一对一 - ONE_TO_MANY 一对多 - MANY_TO_ONE 多对一 - MANY_TO_MANY 多对多
        :type relate_type: str
        """
        
        

        self._type = None
        self._categories = None
        self._link_field_code = None
        self._relation_name = None
        self._description = None
        self._display_scope = None
        self._actions = None
        self._relate_type = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if categories is not None:
            self.categories = categories
        if link_field_code is not None:
            self.link_field_code = link_field_code
        if relation_name is not None:
            self.relation_name = relation_name
        if description is not None:
            self.description = description
        if display_scope is not None:
            self.display_scope = display_scope
        if actions is not None:
            self.actions = actions
        if relate_type is not None:
            self.relate_type = relate_type

    @property
    def type(self):
        r"""Gets the type of this Relation.

        **参数解释**： 关系code。 **取值范围**： 不涉及。

        :return: The type of this Relation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Relation.

        **参数解释**： 关系code。 **取值范围**： 不涉及。

        :param type: The type of this Relation.
        :type type: str
        """
        self._type = type

    @property
    def categories(self):
        r"""Gets the categories of this Relation.

        **参数解释**： 关联的工作项code列表。 **取值范围**： 不涉及。

        :return: The categories of this Relation.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        r"""Sets the categories of this Relation.

        **参数解释**： 关联的工作项code列表。 **取值范围**： 不涉及。

        :param categories: The categories of this Relation.
        :type categories: list[str]
        """
        self._categories = categories

    @property
    def link_field_code(self):
        r"""Gets the link_field_code of this Relation.

        **参数解释**： 工作流场景使用，前置校验中的关联关系校验字段。 **取值范围**： 不涉及。

        :return: The link_field_code of this Relation.
        :rtype: str
        """
        return self._link_field_code

    @link_field_code.setter
    def link_field_code(self, link_field_code):
        r"""Sets the link_field_code of this Relation.

        **参数解释**： 工作流场景使用，前置校验中的关联关系校验字段。 **取值范围**： 不涉及。

        :param link_field_code: The link_field_code of this Relation.
        :type link_field_code: str
        """
        self._link_field_code = link_field_code

    @property
    def relation_name(self):
        r"""Gets the relation_name of this Relation.

        **参数解释**： 关系名称，在工作项详情关联项下左侧显示。 **取值范围**： 不涉及。

        :return: The relation_name of this Relation.
        :rtype: str
        """
        return self._relation_name

    @relation_name.setter
    def relation_name(self, relation_name):
        r"""Sets the relation_name of this Relation.

        **参数解释**： 关系名称，在工作项详情关联项下左侧显示。 **取值范围**： 不涉及。

        :param relation_name: The relation_name of this Relation.
        :type relation_name: str
        """
        self._relation_name = relation_name

    @property
    def description(self):
        r"""Gets the description of this Relation.

        **参数解释**： 关系描述。 **取值范围**： 不涉及。

        :return: The description of this Relation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Relation.

        **参数解释**： 关系描述。 **取值范围**： 不涉及。

        :param description: The description of this Relation.
        :type description: str
        """
        self._description = description

    @property
    def display_scope(self):
        r"""Gets the display_scope of this Relation.

        **参数解释**： 展示范围。 **取值范围**： 不涉及。

        :return: The display_scope of this Relation.
        :rtype: str
        """
        return self._display_scope

    @display_scope.setter
    def display_scope(self, display_scope):
        r"""Sets the display_scope of this Relation.

        **参数解释**： 展示范围。 **取值范围**： 不涉及。

        :param display_scope: The display_scope of this Relation.
        :type display_scope: str
        """
        self._display_scope = display_scope

    @property
    def actions(self):
        r"""Gets the actions of this Relation.

        **参数解释**： 动作行为。 **取值范围**： 不涉及。

        :return: The actions of this Relation.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.RelateAction`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this Relation.

        **参数解释**： 动作行为。 **取值范围**： 不涉及。

        :param actions: The actions of this Relation.
        :type actions: list[:class:`huaweicloudsdkprojectman.v4.RelateAction`]
        """
        self._actions = actions

    @property
    def relate_type(self):
        r"""Gets the relate_type of this Relation.

        **参数解释**： 动作行为。 **取值范围**： - ONE_TO_ONE 一对一 - ONE_TO_MANY 一对多 - MANY_TO_ONE 多对一 - MANY_TO_MANY 多对多

        :return: The relate_type of this Relation.
        :rtype: str
        """
        return self._relate_type

    @relate_type.setter
    def relate_type(self, relate_type):
        r"""Sets the relate_type of this Relation.

        **参数解释**： 动作行为。 **取值范围**： - ONE_TO_ONE 一对一 - ONE_TO_MANY 一对多 - MANY_TO_ONE 多对一 - MANY_TO_MANY 多对多

        :param relate_type: The relate_type of this Relation.
        :type relate_type: str
        """
        self._relate_type = relate_type

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
        if not isinstance(other, Relation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
