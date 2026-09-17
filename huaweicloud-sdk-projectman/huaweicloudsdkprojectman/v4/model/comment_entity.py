# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommentEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'category': 'str',
        'type': 'str',
        'top': 'bool',
        'top_time': 'str',
        'description': 'str',
        'issue_id': 'str',
        'top_flag': 'bool',
        'created_by': 'str',
        'created_date': 'str',
        'creator_info': 'UserVO',
        'extend_attribute': 'str',
        'extend_attribute_obj': 'CommentExtendAttribute',
        'extend_attribute_objs': 'list[CommentExtendAttribute]'
    }

    attribute_map = {
        'id': 'id',
        'category': 'category',
        'type': 'type',
        'top': 'top',
        'top_time': 'top_time',
        'description': 'description',
        'issue_id': 'issue_id',
        'top_flag': 'top_flag',
        'created_by': 'created_by',
        'created_date': 'created_date',
        'creator_info': 'creator_info',
        'extend_attribute': 'extend_attribute',
        'extend_attribute_obj': 'extend_attribute_obj',
        'extend_attribute_objs': 'extend_attribute_objs'
    }

    def __init__(self, id=None, category=None, type=None, top=None, top_time=None, description=None, issue_id=None, top_flag=None, created_by=None, created_date=None, creator_info=None, extend_attribute=None, extend_attribute_obj=None, extend_attribute_objs=None):
        r"""CommentEntity

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 评论ID。 **默认取值**： 不涉及。
        :type id: str
        :param category: **参数解释**： 评论类型。 **取值范围**： - comment：评论 - reply：回复 - operation：系统操作。 **默认取值**： 不涉及。
        :type category: str
        :param type: **参数解释**： 评论元数据类型。 **取值范围**： 固定为comment。 **默认取值**： 不涉及。
        :type type: str
        :param top: **参数解释**： 是否显示在置顶区域。 **取值范围**： - true：显示。 - false： 不显示。 **默认取值**： 不涉及。
        :type top: bool
        :param top_time: **参数解释**： 置顶时间的unix时间戳，单位：毫秒。当有多条置顶评论时，最后置顶的评论显示在最上层。 **默认取值**： 不涉及。
        :type top_time: str
        :param description: **参数解释**： 评论内容，表现形式为html标签。 **默认取值**： 不涉及。
        :type description: str
        :param issue_id: **参数解释**： 评论关联的工作项ID。 **默认取值**： 不涉及。
        :type issue_id: str
        :param top_flag: **参数解释**： 当前评论是否被置顶。 **取值范围**： - true：置顶。 - false： 不置顶。 **默认取值**： 不涉及。
        :type top_flag: bool
        :param created_by: **参数解释**： 评论创建人ID。 **默认取值**： 不涉及。
        :type created_by: str
        :param created_date: **参数解释**： 评论创建时间。 **默认取值**： 不涉及。
        :type created_date: str
        :param creator_info: 
        :type creator_info: :class:`huaweicloudsdkprojectman.v4.UserVO`
        :param extend_attribute: **参数解释**： 评论的一些扩展属性，表现为json字符串。 **默认取值**： 不涉及。
        :type extend_attribute: str
        :param extend_attribute_obj: 
        :type extend_attribute_obj: :class:`huaweicloudsdkprojectman.v4.CommentExtendAttribute`
        :param extend_attribute_objs: **参数解释**： 评论的扩展属性对象数组。 **默认取值**： 不涉及。
        :type extend_attribute_objs: list[:class:`huaweicloudsdkprojectman.v4.CommentExtendAttribute`]
        """
        
        

        self._id = None
        self._category = None
        self._type = None
        self._top = None
        self._top_time = None
        self._description = None
        self._issue_id = None
        self._top_flag = None
        self._created_by = None
        self._created_date = None
        self._creator_info = None
        self._extend_attribute = None
        self._extend_attribute_obj = None
        self._extend_attribute_objs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if category is not None:
            self.category = category
        if type is not None:
            self.type = type
        if top is not None:
            self.top = top
        if top_time is not None:
            self.top_time = top_time
        if description is not None:
            self.description = description
        if issue_id is not None:
            self.issue_id = issue_id
        if top_flag is not None:
            self.top_flag = top_flag
        if created_by is not None:
            self.created_by = created_by
        if created_date is not None:
            self.created_date = created_date
        if creator_info is not None:
            self.creator_info = creator_info
        if extend_attribute is not None:
            self.extend_attribute = extend_attribute
        if extend_attribute_obj is not None:
            self.extend_attribute_obj = extend_attribute_obj
        if extend_attribute_objs is not None:
            self.extend_attribute_objs = extend_attribute_objs

    @property
    def id(self):
        r"""Gets the id of this CommentEntity.

        **参数解释**： 评论ID。 **默认取值**： 不涉及。

        :return: The id of this CommentEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CommentEntity.

        **参数解释**： 评论ID。 **默认取值**： 不涉及。

        :param id: The id of this CommentEntity.
        :type id: str
        """
        self._id = id

    @property
    def category(self):
        r"""Gets the category of this CommentEntity.

        **参数解释**： 评论类型。 **取值范围**： - comment：评论 - reply：回复 - operation：系统操作。 **默认取值**： 不涉及。

        :return: The category of this CommentEntity.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CommentEntity.

        **参数解释**： 评论类型。 **取值范围**： - comment：评论 - reply：回复 - operation：系统操作。 **默认取值**： 不涉及。

        :param category: The category of this CommentEntity.
        :type category: str
        """
        self._category = category

    @property
    def type(self):
        r"""Gets the type of this CommentEntity.

        **参数解释**： 评论元数据类型。 **取值范围**： 固定为comment。 **默认取值**： 不涉及。

        :return: The type of this CommentEntity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CommentEntity.

        **参数解释**： 评论元数据类型。 **取值范围**： 固定为comment。 **默认取值**： 不涉及。

        :param type: The type of this CommentEntity.
        :type type: str
        """
        self._type = type

    @property
    def top(self):
        r"""Gets the top of this CommentEntity.

        **参数解释**： 是否显示在置顶区域。 **取值范围**： - true：显示。 - false： 不显示。 **默认取值**： 不涉及。

        :return: The top of this CommentEntity.
        :rtype: bool
        """
        return self._top

    @top.setter
    def top(self, top):
        r"""Sets the top of this CommentEntity.

        **参数解释**： 是否显示在置顶区域。 **取值范围**： - true：显示。 - false： 不显示。 **默认取值**： 不涉及。

        :param top: The top of this CommentEntity.
        :type top: bool
        """
        self._top = top

    @property
    def top_time(self):
        r"""Gets the top_time of this CommentEntity.

        **参数解释**： 置顶时间的unix时间戳，单位：毫秒。当有多条置顶评论时，最后置顶的评论显示在最上层。 **默认取值**： 不涉及。

        :return: The top_time of this CommentEntity.
        :rtype: str
        """
        return self._top_time

    @top_time.setter
    def top_time(self, top_time):
        r"""Sets the top_time of this CommentEntity.

        **参数解释**： 置顶时间的unix时间戳，单位：毫秒。当有多条置顶评论时，最后置顶的评论显示在最上层。 **默认取值**： 不涉及。

        :param top_time: The top_time of this CommentEntity.
        :type top_time: str
        """
        self._top_time = top_time

    @property
    def description(self):
        r"""Gets the description of this CommentEntity.

        **参数解释**： 评论内容，表现形式为html标签。 **默认取值**： 不涉及。

        :return: The description of this CommentEntity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CommentEntity.

        **参数解释**： 评论内容，表现形式为html标签。 **默认取值**： 不涉及。

        :param description: The description of this CommentEntity.
        :type description: str
        """
        self._description = description

    @property
    def issue_id(self):
        r"""Gets the issue_id of this CommentEntity.

        **参数解释**： 评论关联的工作项ID。 **默认取值**： 不涉及。

        :return: The issue_id of this CommentEntity.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this CommentEntity.

        **参数解释**： 评论关联的工作项ID。 **默认取值**： 不涉及。

        :param issue_id: The issue_id of this CommentEntity.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def top_flag(self):
        r"""Gets the top_flag of this CommentEntity.

        **参数解释**： 当前评论是否被置顶。 **取值范围**： - true：置顶。 - false： 不置顶。 **默认取值**： 不涉及。

        :return: The top_flag of this CommentEntity.
        :rtype: bool
        """
        return self._top_flag

    @top_flag.setter
    def top_flag(self, top_flag):
        r"""Sets the top_flag of this CommentEntity.

        **参数解释**： 当前评论是否被置顶。 **取值范围**： - true：置顶。 - false： 不置顶。 **默认取值**： 不涉及。

        :param top_flag: The top_flag of this CommentEntity.
        :type top_flag: bool
        """
        self._top_flag = top_flag

    @property
    def created_by(self):
        r"""Gets the created_by of this CommentEntity.

        **参数解释**： 评论创建人ID。 **默认取值**： 不涉及。

        :return: The created_by of this CommentEntity.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this CommentEntity.

        **参数解释**： 评论创建人ID。 **默认取值**： 不涉及。

        :param created_by: The created_by of this CommentEntity.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def created_date(self):
        r"""Gets the created_date of this CommentEntity.

        **参数解释**： 评论创建时间。 **默认取值**： 不涉及。

        :return: The created_date of this CommentEntity.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this CommentEntity.

        **参数解释**： 评论创建时间。 **默认取值**： 不涉及。

        :param created_date: The created_date of this CommentEntity.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def creator_info(self):
        r"""Gets the creator_info of this CommentEntity.

        :return: The creator_info of this CommentEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        return self._creator_info

    @creator_info.setter
    def creator_info(self, creator_info):
        r"""Sets the creator_info of this CommentEntity.

        :param creator_info: The creator_info of this CommentEntity.
        :type creator_info: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        self._creator_info = creator_info

    @property
    def extend_attribute(self):
        r"""Gets the extend_attribute of this CommentEntity.

        **参数解释**： 评论的一些扩展属性，表现为json字符串。 **默认取值**： 不涉及。

        :return: The extend_attribute of this CommentEntity.
        :rtype: str
        """
        return self._extend_attribute

    @extend_attribute.setter
    def extend_attribute(self, extend_attribute):
        r"""Sets the extend_attribute of this CommentEntity.

        **参数解释**： 评论的一些扩展属性，表现为json字符串。 **默认取值**： 不涉及。

        :param extend_attribute: The extend_attribute of this CommentEntity.
        :type extend_attribute: str
        """
        self._extend_attribute = extend_attribute

    @property
    def extend_attribute_obj(self):
        r"""Gets the extend_attribute_obj of this CommentEntity.

        :return: The extend_attribute_obj of this CommentEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.CommentExtendAttribute`
        """
        return self._extend_attribute_obj

    @extend_attribute_obj.setter
    def extend_attribute_obj(self, extend_attribute_obj):
        r"""Sets the extend_attribute_obj of this CommentEntity.

        :param extend_attribute_obj: The extend_attribute_obj of this CommentEntity.
        :type extend_attribute_obj: :class:`huaweicloudsdkprojectman.v4.CommentExtendAttribute`
        """
        self._extend_attribute_obj = extend_attribute_obj

    @property
    def extend_attribute_objs(self):
        r"""Gets the extend_attribute_objs of this CommentEntity.

        **参数解释**： 评论的扩展属性对象数组。 **默认取值**： 不涉及。

        :return: The extend_attribute_objs of this CommentEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.CommentExtendAttribute`]
        """
        return self._extend_attribute_objs

    @extend_attribute_objs.setter
    def extend_attribute_objs(self, extend_attribute_objs):
        r"""Sets the extend_attribute_objs of this CommentEntity.

        **参数解释**： 评论的扩展属性对象数组。 **默认取值**： 不涉及。

        :param extend_attribute_objs: The extend_attribute_objs of this CommentEntity.
        :type extend_attribute_objs: list[:class:`huaweicloudsdkprojectman.v4.CommentExtendAttribute`]
        """
        self._extend_attribute_objs = extend_attribute_objs

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
        if not isinstance(other, CommentEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
