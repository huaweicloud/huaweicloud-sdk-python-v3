# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommentCreateVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'issue_category': 'str',
        'description': 'str',
        'parent_id': 'str',
        'root_id': 'str',
        'at': 'str'
    }

    attribute_map = {
        'category': 'category',
        'issue_category': 'issue_category',
        'description': 'description',
        'parent_id': 'parent_id',
        'root_id': 'root_id',
        'at': 'at'
    }

    def __init__(self, category=None, issue_category=None, description=None, parent_id=None, root_id=None, at=None):
        r"""CommentCreateVO

        The model defined in huaweicloud sdk

        :param category: **参数解释**： 评论类型。 **取值范围**： - comment：评论 - reply：回复 - operation：系统操作（不支持创建）。 **默认取值**： 不涉及。
        :type category: str
        :param issue_category: **参数解释**： 评论关联的工作项类型。 **默认取值**： 不涉及。
        :type issue_category: str
        :param description: **参数解释**： 评论内容，使用html标记语言。 **默认取值**： 不涉及。
        :type description: str
        :param parent_id: **参数解释**： 评论的父ID，取值为需要回复的评论的ID。 **约束限制**： 回复评论时必填。 **取值范围**： 只支持CR。 **默认取值**： 不涉及。
        :type parent_id: str
        :param root_id: **参数解释**： 评论的根ID，取值为需要回复的首层评论的ID。 **约束限制**： 回复评论时必填，创建评论时不能填。 **默认取值**： 不涉及。
        :type root_id: str
        :param at: **参数解释**： 评论时@他人的用户ID，填写此参数后会通知被@的用户，通知形式在需求管理-设置-工作项设置-通知设置中配置。 **默认取值**： 不涉及。
        :type at: str
        """
        
        

        self._category = None
        self._issue_category = None
        self._description = None
        self._parent_id = None
        self._root_id = None
        self._at = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if issue_category is not None:
            self.issue_category = issue_category
        if description is not None:
            self.description = description
        if parent_id is not None:
            self.parent_id = parent_id
        if root_id is not None:
            self.root_id = root_id
        if at is not None:
            self.at = at

    @property
    def category(self):
        r"""Gets the category of this CommentCreateVO.

        **参数解释**： 评论类型。 **取值范围**： - comment：评论 - reply：回复 - operation：系统操作（不支持创建）。 **默认取值**： 不涉及。

        :return: The category of this CommentCreateVO.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CommentCreateVO.

        **参数解释**： 评论类型。 **取值范围**： - comment：评论 - reply：回复 - operation：系统操作（不支持创建）。 **默认取值**： 不涉及。

        :param category: The category of this CommentCreateVO.
        :type category: str
        """
        self._category = category

    @property
    def issue_category(self):
        r"""Gets the issue_category of this CommentCreateVO.

        **参数解释**： 评论关联的工作项类型。 **默认取值**： 不涉及。

        :return: The issue_category of this CommentCreateVO.
        :rtype: str
        """
        return self._issue_category

    @issue_category.setter
    def issue_category(self, issue_category):
        r"""Sets the issue_category of this CommentCreateVO.

        **参数解释**： 评论关联的工作项类型。 **默认取值**： 不涉及。

        :param issue_category: The issue_category of this CommentCreateVO.
        :type issue_category: str
        """
        self._issue_category = issue_category

    @property
    def description(self):
        r"""Gets the description of this CommentCreateVO.

        **参数解释**： 评论内容，使用html标记语言。 **默认取值**： 不涉及。

        :return: The description of this CommentCreateVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CommentCreateVO.

        **参数解释**： 评论内容，使用html标记语言。 **默认取值**： 不涉及。

        :param description: The description of this CommentCreateVO.
        :type description: str
        """
        self._description = description

    @property
    def parent_id(self):
        r"""Gets the parent_id of this CommentCreateVO.

        **参数解释**： 评论的父ID，取值为需要回复的评论的ID。 **约束限制**： 回复评论时必填。 **取值范围**： 只支持CR。 **默认取值**： 不涉及。

        :return: The parent_id of this CommentCreateVO.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this CommentCreateVO.

        **参数解释**： 评论的父ID，取值为需要回复的评论的ID。 **约束限制**： 回复评论时必填。 **取值范围**： 只支持CR。 **默认取值**： 不涉及。

        :param parent_id: The parent_id of this CommentCreateVO.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def root_id(self):
        r"""Gets the root_id of this CommentCreateVO.

        **参数解释**： 评论的根ID，取值为需要回复的首层评论的ID。 **约束限制**： 回复评论时必填，创建评论时不能填。 **默认取值**： 不涉及。

        :return: The root_id of this CommentCreateVO.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        r"""Sets the root_id of this CommentCreateVO.

        **参数解释**： 评论的根ID，取值为需要回复的首层评论的ID。 **约束限制**： 回复评论时必填，创建评论时不能填。 **默认取值**： 不涉及。

        :param root_id: The root_id of this CommentCreateVO.
        :type root_id: str
        """
        self._root_id = root_id

    @property
    def at(self):
        r"""Gets the at of this CommentCreateVO.

        **参数解释**： 评论时@他人的用户ID，填写此参数后会通知被@的用户，通知形式在需求管理-设置-工作项设置-通知设置中配置。 **默认取值**： 不涉及。

        :return: The at of this CommentCreateVO.
        :rtype: str
        """
        return self._at

    @at.setter
    def at(self, at):
        r"""Sets the at of this CommentCreateVO.

        **参数解释**： 评论时@他人的用户ID，填写此参数后会通知被@的用户，通知形式在需求管理-设置-工作项设置-通知设置中配置。 **默认取值**： 不涉及。

        :param at: The at of this CommentCreateVO.
        :type at: str
        """
        self._at = at

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
        if not isinstance(other, CommentCreateVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
