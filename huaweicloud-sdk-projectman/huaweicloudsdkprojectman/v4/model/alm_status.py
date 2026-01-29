# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlmStatus:

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
        'belonging': 'str',
        'space_id': 'str',
        'name': 'str',
        'code': 'str',
        'definition_type': 'str',
        'belong_definition_type': 'int',
        'display_value': 'str',
        'position': 'int',
        'displayable': 'int',
        'editable': 'int',
        'deletable': 'int',
        'mutable': 'int',
        'title_py': 'str',
        'created_by': 'str',
        'created_date': 'int',
        'modified_date': 'int',
        'modified_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'belonging': 'belonging',
        'space_id': 'space_id',
        'name': 'name',
        'code': 'code',
        'definition_type': 'definition_type',
        'belong_definition_type': 'belong_definition_type',
        'display_value': 'display_value',
        'position': 'position',
        'displayable': 'displayable',
        'editable': 'editable',
        'deletable': 'deletable',
        'mutable': 'mutable',
        'title_py': 'title_py',
        'created_by': 'created_by',
        'created_date': 'created_date',
        'modified_date': 'modified_date',
        'modified_by': 'modified_by'
    }

    def __init__(self, id=None, belonging=None, space_id=None, name=None, code=None, definition_type=None, belong_definition_type=None, display_value=None, position=None, displayable=None, editable=None, deletable=None, mutable=None, title_py=None, created_by=None, created_date=None, modified_date=None, modified_by=None):
        r"""AlmStatus

        The model defined in huaweicloud sdk

        :param id: **参数解释：**  状态Id。 **取值范围：**  不涉及。
        :type id: str
        :param belonging: **参数解释：**  工作项的状态属性。 **取值范围：**  - START - IN_PROGRESS - END
        :type belonging: str
        :param space_id: **参数解释：**  状态所属的项目空间id。 **取值范围：**  不涉及。
        :type space_id: str
        :param name: **参数解释：**  状态名称。 **取值范围：**  不涉及。
        :type name: str
        :param code: **参数解释：**  状态code值。 **取值范围：**  不涉及。
        :type code: str
        :param definition_type: **参数解释：**  状态定义级别，1,2,3为系统级，4为租户自定义，5为项目自定义。 **取值范围：**  不涉及。
        :type definition_type: str
        :param belong_definition_type: **参数解释：**  状态归属定义级别，1,2,3为系统级，4为租户自定义，5为项目自定义。区别于definition_type。如果为系统级和租户自定义级，在项目中会复制一份元数据，归属于项目空间。 **取值范围：**  不涉及。
        :type belong_definition_type: int
        :param display_value: **参数解释：**  状态名称，和name值相同。 **取值范围：**  不涉及。
        :type display_value: str
        :param position: **参数解释：**  位置顺序。 **取值范围：**  不涉及。
        :type position: int
        :param displayable: **参数解释：**  是否显示。 **取值范围：**  不涉及。
        :type displayable: int
        :param editable: **参数解释：**  是否可编辑。 **取值范围：**  不涉及。
        :type editable: int
        :param deletable: **参数解释：**  是否可删除。 **取值范围：**  不涉及。
        :type deletable: int
        :param mutable: **参数解释：**  是否可变，即是否为固定值。 **取值范围：**  不涉及。
        :type mutable: int
        :param title_py: **参数解释：**  标题的拼音首字母。 **取值范围：**  不涉及。
        :type title_py: str
        :param created_by: **参数解释：**  创建人用户Id。 **取值范围：**  不涉及。
        :type created_by: str
        :param created_date: **参数解释：**  创建时间。Unix时间戳，精度为毫秒。 **取值范围：**  不涉及。
        :type created_date: int
        :param modified_date: **参数解释：**  最近修改时间。Unix时间戳，精度为毫秒。 **取值范围：**  不涉及。
        :type modified_date: int
        :param modified_by: **参数解释：**  最近修改人用户Id。 **取值范围：**    不涉及。
        :type modified_by: str
        """
        
        

        self._id = None
        self._belonging = None
        self._space_id = None
        self._name = None
        self._code = None
        self._definition_type = None
        self._belong_definition_type = None
        self._display_value = None
        self._position = None
        self._displayable = None
        self._editable = None
        self._deletable = None
        self._mutable = None
        self._title_py = None
        self._created_by = None
        self._created_date = None
        self._modified_date = None
        self._modified_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if belonging is not None:
            self.belonging = belonging
        if space_id is not None:
            self.space_id = space_id
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if definition_type is not None:
            self.definition_type = definition_type
        if belong_definition_type is not None:
            self.belong_definition_type = belong_definition_type
        if display_value is not None:
            self.display_value = display_value
        if position is not None:
            self.position = position
        if displayable is not None:
            self.displayable = displayable
        if editable is not None:
            self.editable = editable
        if deletable is not None:
            self.deletable = deletable
        if mutable is not None:
            self.mutable = mutable
        if title_py is not None:
            self.title_py = title_py
        if created_by is not None:
            self.created_by = created_by
        if created_date is not None:
            self.created_date = created_date
        if modified_date is not None:
            self.modified_date = modified_date
        if modified_by is not None:
            self.modified_by = modified_by

    @property
    def id(self):
        r"""Gets the id of this AlmStatus.

        **参数解释：**  状态Id。 **取值范围：**  不涉及。

        :return: The id of this AlmStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AlmStatus.

        **参数解释：**  状态Id。 **取值范围：**  不涉及。

        :param id: The id of this AlmStatus.
        :type id: str
        """
        self._id = id

    @property
    def belonging(self):
        r"""Gets the belonging of this AlmStatus.

        **参数解释：**  工作项的状态属性。 **取值范围：**  - START - IN_PROGRESS - END

        :return: The belonging of this AlmStatus.
        :rtype: str
        """
        return self._belonging

    @belonging.setter
    def belonging(self, belonging):
        r"""Sets the belonging of this AlmStatus.

        **参数解释：**  工作项的状态属性。 **取值范围：**  - START - IN_PROGRESS - END

        :param belonging: The belonging of this AlmStatus.
        :type belonging: str
        """
        self._belonging = belonging

    @property
    def space_id(self):
        r"""Gets the space_id of this AlmStatus.

        **参数解释：**  状态所属的项目空间id。 **取值范围：**  不涉及。

        :return: The space_id of this AlmStatus.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        r"""Sets the space_id of this AlmStatus.

        **参数解释：**  状态所属的项目空间id。 **取值范围：**  不涉及。

        :param space_id: The space_id of this AlmStatus.
        :type space_id: str
        """
        self._space_id = space_id

    @property
    def name(self):
        r"""Gets the name of this AlmStatus.

        **参数解释：**  状态名称。 **取值范围：**  不涉及。

        :return: The name of this AlmStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AlmStatus.

        **参数解释：**  状态名称。 **取值范围：**  不涉及。

        :param name: The name of this AlmStatus.
        :type name: str
        """
        self._name = name

    @property
    def code(self):
        r"""Gets the code of this AlmStatus.

        **参数解释：**  状态code值。 **取值范围：**  不涉及。

        :return: The code of this AlmStatus.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this AlmStatus.

        **参数解释：**  状态code值。 **取值范围：**  不涉及。

        :param code: The code of this AlmStatus.
        :type code: str
        """
        self._code = code

    @property
    def definition_type(self):
        r"""Gets the definition_type of this AlmStatus.

        **参数解释：**  状态定义级别，1,2,3为系统级，4为租户自定义，5为项目自定义。 **取值范围：**  不涉及。

        :return: The definition_type of this AlmStatus.
        :rtype: str
        """
        return self._definition_type

    @definition_type.setter
    def definition_type(self, definition_type):
        r"""Sets the definition_type of this AlmStatus.

        **参数解释：**  状态定义级别，1,2,3为系统级，4为租户自定义，5为项目自定义。 **取值范围：**  不涉及。

        :param definition_type: The definition_type of this AlmStatus.
        :type definition_type: str
        """
        self._definition_type = definition_type

    @property
    def belong_definition_type(self):
        r"""Gets the belong_definition_type of this AlmStatus.

        **参数解释：**  状态归属定义级别，1,2,3为系统级，4为租户自定义，5为项目自定义。区别于definition_type。如果为系统级和租户自定义级，在项目中会复制一份元数据，归属于项目空间。 **取值范围：**  不涉及。

        :return: The belong_definition_type of this AlmStatus.
        :rtype: int
        """
        return self._belong_definition_type

    @belong_definition_type.setter
    def belong_definition_type(self, belong_definition_type):
        r"""Sets the belong_definition_type of this AlmStatus.

        **参数解释：**  状态归属定义级别，1,2,3为系统级，4为租户自定义，5为项目自定义。区别于definition_type。如果为系统级和租户自定义级，在项目中会复制一份元数据，归属于项目空间。 **取值范围：**  不涉及。

        :param belong_definition_type: The belong_definition_type of this AlmStatus.
        :type belong_definition_type: int
        """
        self._belong_definition_type = belong_definition_type

    @property
    def display_value(self):
        r"""Gets the display_value of this AlmStatus.

        **参数解释：**  状态名称，和name值相同。 **取值范围：**  不涉及。

        :return: The display_value of this AlmStatus.
        :rtype: str
        """
        return self._display_value

    @display_value.setter
    def display_value(self, display_value):
        r"""Sets the display_value of this AlmStatus.

        **参数解释：**  状态名称，和name值相同。 **取值范围：**  不涉及。

        :param display_value: The display_value of this AlmStatus.
        :type display_value: str
        """
        self._display_value = display_value

    @property
    def position(self):
        r"""Gets the position of this AlmStatus.

        **参数解释：**  位置顺序。 **取值范围：**  不涉及。

        :return: The position of this AlmStatus.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this AlmStatus.

        **参数解释：**  位置顺序。 **取值范围：**  不涉及。

        :param position: The position of this AlmStatus.
        :type position: int
        """
        self._position = position

    @property
    def displayable(self):
        r"""Gets the displayable of this AlmStatus.

        **参数解释：**  是否显示。 **取值范围：**  不涉及。

        :return: The displayable of this AlmStatus.
        :rtype: int
        """
        return self._displayable

    @displayable.setter
    def displayable(self, displayable):
        r"""Sets the displayable of this AlmStatus.

        **参数解释：**  是否显示。 **取值范围：**  不涉及。

        :param displayable: The displayable of this AlmStatus.
        :type displayable: int
        """
        self._displayable = displayable

    @property
    def editable(self):
        r"""Gets the editable of this AlmStatus.

        **参数解释：**  是否可编辑。 **取值范围：**  不涉及。

        :return: The editable of this AlmStatus.
        :rtype: int
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        r"""Sets the editable of this AlmStatus.

        **参数解释：**  是否可编辑。 **取值范围：**  不涉及。

        :param editable: The editable of this AlmStatus.
        :type editable: int
        """
        self._editable = editable

    @property
    def deletable(self):
        r"""Gets the deletable of this AlmStatus.

        **参数解释：**  是否可删除。 **取值范围：**  不涉及。

        :return: The deletable of this AlmStatus.
        :rtype: int
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        r"""Sets the deletable of this AlmStatus.

        **参数解释：**  是否可删除。 **取值范围：**  不涉及。

        :param deletable: The deletable of this AlmStatus.
        :type deletable: int
        """
        self._deletable = deletable

    @property
    def mutable(self):
        r"""Gets the mutable of this AlmStatus.

        **参数解释：**  是否可变，即是否为固定值。 **取值范围：**  不涉及。

        :return: The mutable of this AlmStatus.
        :rtype: int
        """
        return self._mutable

    @mutable.setter
    def mutable(self, mutable):
        r"""Sets the mutable of this AlmStatus.

        **参数解释：**  是否可变，即是否为固定值。 **取值范围：**  不涉及。

        :param mutable: The mutable of this AlmStatus.
        :type mutable: int
        """
        self._mutable = mutable

    @property
    def title_py(self):
        r"""Gets the title_py of this AlmStatus.

        **参数解释：**  标题的拼音首字母。 **取值范围：**  不涉及。

        :return: The title_py of this AlmStatus.
        :rtype: str
        """
        return self._title_py

    @title_py.setter
    def title_py(self, title_py):
        r"""Sets the title_py of this AlmStatus.

        **参数解释：**  标题的拼音首字母。 **取值范围：**  不涉及。

        :param title_py: The title_py of this AlmStatus.
        :type title_py: str
        """
        self._title_py = title_py

    @property
    def created_by(self):
        r"""Gets the created_by of this AlmStatus.

        **参数解释：**  创建人用户Id。 **取值范围：**  不涉及。

        :return: The created_by of this AlmStatus.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this AlmStatus.

        **参数解释：**  创建人用户Id。 **取值范围：**  不涉及。

        :param created_by: The created_by of this AlmStatus.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def created_date(self):
        r"""Gets the created_date of this AlmStatus.

        **参数解释：**  创建时间。Unix时间戳，精度为毫秒。 **取值范围：**  不涉及。

        :return: The created_date of this AlmStatus.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this AlmStatus.

        **参数解释：**  创建时间。Unix时间戳，精度为毫秒。 **取值范围：**  不涉及。

        :param created_date: The created_date of this AlmStatus.
        :type created_date: int
        """
        self._created_date = created_date

    @property
    def modified_date(self):
        r"""Gets the modified_date of this AlmStatus.

        **参数解释：**  最近修改时间。Unix时间戳，精度为毫秒。 **取值范围：**  不涉及。

        :return: The modified_date of this AlmStatus.
        :rtype: int
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this AlmStatus.

        **参数解释：**  最近修改时间。Unix时间戳，精度为毫秒。 **取值范围：**  不涉及。

        :param modified_date: The modified_date of this AlmStatus.
        :type modified_date: int
        """
        self._modified_date = modified_date

    @property
    def modified_by(self):
        r"""Gets the modified_by of this AlmStatus.

        **参数解释：**  最近修改人用户Id。 **取值范围：**    不涉及。

        :return: The modified_by of this AlmStatus.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this AlmStatus.

        **参数解释：**  最近修改人用户Id。 **取值范围：**    不涉及。

        :param modified_by: The modified_by of this AlmStatus.
        :type modified_by: str
        """
        self._modified_by = modified_by

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
        if not isinstance(other, AlmStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
