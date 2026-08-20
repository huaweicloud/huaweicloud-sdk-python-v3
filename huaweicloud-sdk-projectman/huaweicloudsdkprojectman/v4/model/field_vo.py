# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FieldVO:

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
        'code': 'str',
        'display_name': 'str',
        'created_by': 'str',
        'created_date': 'str',
        'modified_by': 'str',
        'modified_date': 'str',
        'field_type': 'str',
        'field_type_id': 'str',
        'field_type_name': 'str',
        'definition_type': 'str',
        'show_on_card': 'bool',
        'optional': 'bool',
        'controlled': 'bool',
        'immutable': 'bool',
        'no': 'int',
        'default_value': 'str',
        'option': 'list[OptionEntity]',
        'all_options': 'list[OptionEntity]',
        'has_same_display_name': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'display_name': 'display_name',
        'created_by': 'created_by',
        'created_date': 'created_date',
        'modified_by': 'modified_by',
        'modified_date': 'modified_date',
        'field_type': 'field_type',
        'field_type_id': 'field_type_id',
        'field_type_name': 'field_type_name',
        'definition_type': 'definition_type',
        'show_on_card': 'show_on_card',
        'optional': 'optional',
        'controlled': 'controlled',
        'immutable': 'immutable',
        'no': 'no',
        'default_value': 'default_value',
        'option': 'option',
        'all_options': 'all_options',
        'has_same_display_name': 'has_same_display_name'
    }

    def __init__(self, id=None, code=None, display_name=None, created_by=None, created_date=None, modified_by=None, modified_date=None, field_type=None, field_type_id=None, field_type_name=None, definition_type=None, show_on_card=None, optional=None, controlled=None, immutable=None, no=None, default_value=None, option=None, all_options=None, has_same_display_name=None):
        r"""FieldVO

        The model defined in huaweicloud sdk

        :param id: 字段唯一标识。
        :type id: str
        :param code: 字段编码。在项目中使用时一般使用code作为字段标识而不是字段ID。
        :type code: str
        :param display_name: 字段显示名称。
        :type display_name: str
        :param created_by: 字段创建人ID。
        :type created_by: str
        :param created_date: 字段创建时间。时间戳格式，单位毫秒。
        :type created_date: str
        :param modified_by: 字段最后修改人ID。
        :type modified_by: str
        :param modified_date: 字段最后修改时间。时间戳格式，单位毫秒。
        :type modified_date: str
        :param field_type: 字段类型标识。
        :type field_type: str
        :param field_type_id: 字段类型ID。用于区分不同的字段类型。
        :type field_type_id: str
        :param field_type_name: 字段类型名称。如单选列表、多选列表、多行文本等。
        :type field_type_name: str
        :param definition_type: 字段定义类型。用于区分系统字段和自定义字段。
        :type definition_type: str
        :param show_on_card: 是否显示在云服务类型的迭代看板卡片模式中。
        :type show_on_card: bool
        :param optional: 字段是否为必填项。
        :type optional: bool
        :param controlled: 字段是否受控。如果工作项已经基线，修改受控字段值时会触发变更评审。
        :type controlled: bool
        :param immutable: 字段是否不可变。更新接口无法更新不可变字段。
        :type immutable: bool
        :param no: 字段排序序号。数值越小越靠前显示。
        :type no: int
        :param default_value: 字段默认值。创建工作项时自动填充。
        :type default_value: str
        :param option: 字段选项。单选列表类型字段的选项信息，包含选项ID、编码、显示名称等属性。
        :type option: list[:class:`huaweicloudsdkprojectman.v4.OptionEntity`]
        :param all_options: 字段所有选项。多选列表类型字段的全部选项信息，数组元素包含选项ID、编码、显示名称等属性。
        :type all_options: list[:class:`huaweicloudsdkprojectman.v4.OptionEntity`]
        :param has_same_display_name: 是否存在同名字段。用于检测字段名称冲突。
        :type has_same_display_name: bool
        """
        
        

        self._id = None
        self._code = None
        self._display_name = None
        self._created_by = None
        self._created_date = None
        self._modified_by = None
        self._modified_date = None
        self._field_type = None
        self._field_type_id = None
        self._field_type_name = None
        self._definition_type = None
        self._show_on_card = None
        self._optional = None
        self._controlled = None
        self._immutable = None
        self._no = None
        self._default_value = None
        self._option = None
        self._all_options = None
        self._has_same_display_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if display_name is not None:
            self.display_name = display_name
        if created_by is not None:
            self.created_by = created_by
        if created_date is not None:
            self.created_date = created_date
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_date is not None:
            self.modified_date = modified_date
        if field_type is not None:
            self.field_type = field_type
        if field_type_id is not None:
            self.field_type_id = field_type_id
        if field_type_name is not None:
            self.field_type_name = field_type_name
        if definition_type is not None:
            self.definition_type = definition_type
        if show_on_card is not None:
            self.show_on_card = show_on_card
        if optional is not None:
            self.optional = optional
        if controlled is not None:
            self.controlled = controlled
        if immutable is not None:
            self.immutable = immutable
        if no is not None:
            self.no = no
        if default_value is not None:
            self.default_value = default_value
        if option is not None:
            self.option = option
        if all_options is not None:
            self.all_options = all_options
        if has_same_display_name is not None:
            self.has_same_display_name = has_same_display_name

    @property
    def id(self):
        r"""Gets the id of this FieldVO.

        字段唯一标识。

        :return: The id of this FieldVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FieldVO.

        字段唯一标识。

        :param id: The id of this FieldVO.
        :type id: str
        """
        self._id = id

    @property
    def code(self):
        r"""Gets the code of this FieldVO.

        字段编码。在项目中使用时一般使用code作为字段标识而不是字段ID。

        :return: The code of this FieldVO.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this FieldVO.

        字段编码。在项目中使用时一般使用code作为字段标识而不是字段ID。

        :param code: The code of this FieldVO.
        :type code: str
        """
        self._code = code

    @property
    def display_name(self):
        r"""Gets the display_name of this FieldVO.

        字段显示名称。

        :return: The display_name of this FieldVO.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this FieldVO.

        字段显示名称。

        :param display_name: The display_name of this FieldVO.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def created_by(self):
        r"""Gets the created_by of this FieldVO.

        字段创建人ID。

        :return: The created_by of this FieldVO.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this FieldVO.

        字段创建人ID。

        :param created_by: The created_by of this FieldVO.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def created_date(self):
        r"""Gets the created_date of this FieldVO.

        字段创建时间。时间戳格式，单位毫秒。

        :return: The created_date of this FieldVO.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this FieldVO.

        字段创建时间。时间戳格式，单位毫秒。

        :param created_date: The created_date of this FieldVO.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def modified_by(self):
        r"""Gets the modified_by of this FieldVO.

        字段最后修改人ID。

        :return: The modified_by of this FieldVO.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this FieldVO.

        字段最后修改人ID。

        :param modified_by: The modified_by of this FieldVO.
        :type modified_by: str
        """
        self._modified_by = modified_by

    @property
    def modified_date(self):
        r"""Gets the modified_date of this FieldVO.

        字段最后修改时间。时间戳格式，单位毫秒。

        :return: The modified_date of this FieldVO.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this FieldVO.

        字段最后修改时间。时间戳格式，单位毫秒。

        :param modified_date: The modified_date of this FieldVO.
        :type modified_date: str
        """
        self._modified_date = modified_date

    @property
    def field_type(self):
        r"""Gets the field_type of this FieldVO.

        字段类型标识。

        :return: The field_type of this FieldVO.
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        r"""Sets the field_type of this FieldVO.

        字段类型标识。

        :param field_type: The field_type of this FieldVO.
        :type field_type: str
        """
        self._field_type = field_type

    @property
    def field_type_id(self):
        r"""Gets the field_type_id of this FieldVO.

        字段类型ID。用于区分不同的字段类型。

        :return: The field_type_id of this FieldVO.
        :rtype: str
        """
        return self._field_type_id

    @field_type_id.setter
    def field_type_id(self, field_type_id):
        r"""Sets the field_type_id of this FieldVO.

        字段类型ID。用于区分不同的字段类型。

        :param field_type_id: The field_type_id of this FieldVO.
        :type field_type_id: str
        """
        self._field_type_id = field_type_id

    @property
    def field_type_name(self):
        r"""Gets the field_type_name of this FieldVO.

        字段类型名称。如单选列表、多选列表、多行文本等。

        :return: The field_type_name of this FieldVO.
        :rtype: str
        """
        return self._field_type_name

    @field_type_name.setter
    def field_type_name(self, field_type_name):
        r"""Sets the field_type_name of this FieldVO.

        字段类型名称。如单选列表、多选列表、多行文本等。

        :param field_type_name: The field_type_name of this FieldVO.
        :type field_type_name: str
        """
        self._field_type_name = field_type_name

    @property
    def definition_type(self):
        r"""Gets the definition_type of this FieldVO.

        字段定义类型。用于区分系统字段和自定义字段。

        :return: The definition_type of this FieldVO.
        :rtype: str
        """
        return self._definition_type

    @definition_type.setter
    def definition_type(self, definition_type):
        r"""Sets the definition_type of this FieldVO.

        字段定义类型。用于区分系统字段和自定义字段。

        :param definition_type: The definition_type of this FieldVO.
        :type definition_type: str
        """
        self._definition_type = definition_type

    @property
    def show_on_card(self):
        r"""Gets the show_on_card of this FieldVO.

        是否显示在云服务类型的迭代看板卡片模式中。

        :return: The show_on_card of this FieldVO.
        :rtype: bool
        """
        return self._show_on_card

    @show_on_card.setter
    def show_on_card(self, show_on_card):
        r"""Sets the show_on_card of this FieldVO.

        是否显示在云服务类型的迭代看板卡片模式中。

        :param show_on_card: The show_on_card of this FieldVO.
        :type show_on_card: bool
        """
        self._show_on_card = show_on_card

    @property
    def optional(self):
        r"""Gets the optional of this FieldVO.

        字段是否为必填项。

        :return: The optional of this FieldVO.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        r"""Sets the optional of this FieldVO.

        字段是否为必填项。

        :param optional: The optional of this FieldVO.
        :type optional: bool
        """
        self._optional = optional

    @property
    def controlled(self):
        r"""Gets the controlled of this FieldVO.

        字段是否受控。如果工作项已经基线，修改受控字段值时会触发变更评审。

        :return: The controlled of this FieldVO.
        :rtype: bool
        """
        return self._controlled

    @controlled.setter
    def controlled(self, controlled):
        r"""Sets the controlled of this FieldVO.

        字段是否受控。如果工作项已经基线，修改受控字段值时会触发变更评审。

        :param controlled: The controlled of this FieldVO.
        :type controlled: bool
        """
        self._controlled = controlled

    @property
    def immutable(self):
        r"""Gets the immutable of this FieldVO.

        字段是否不可变。更新接口无法更新不可变字段。

        :return: The immutable of this FieldVO.
        :rtype: bool
        """
        return self._immutable

    @immutable.setter
    def immutable(self, immutable):
        r"""Sets the immutable of this FieldVO.

        字段是否不可变。更新接口无法更新不可变字段。

        :param immutable: The immutable of this FieldVO.
        :type immutable: bool
        """
        self._immutable = immutable

    @property
    def no(self):
        r"""Gets the no of this FieldVO.

        字段排序序号。数值越小越靠前显示。

        :return: The no of this FieldVO.
        :rtype: int
        """
        return self._no

    @no.setter
    def no(self, no):
        r"""Sets the no of this FieldVO.

        字段排序序号。数值越小越靠前显示。

        :param no: The no of this FieldVO.
        :type no: int
        """
        self._no = no

    @property
    def default_value(self):
        r"""Gets the default_value of this FieldVO.

        字段默认值。创建工作项时自动填充。

        :return: The default_value of this FieldVO.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this FieldVO.

        字段默认值。创建工作项时自动填充。

        :param default_value: The default_value of this FieldVO.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def option(self):
        r"""Gets the option of this FieldVO.

        字段选项。单选列表类型字段的选项信息，包含选项ID、编码、显示名称等属性。

        :return: The option of this FieldVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.OptionEntity`]
        """
        return self._option

    @option.setter
    def option(self, option):
        r"""Sets the option of this FieldVO.

        字段选项。单选列表类型字段的选项信息，包含选项ID、编码、显示名称等属性。

        :param option: The option of this FieldVO.
        :type option: list[:class:`huaweicloudsdkprojectman.v4.OptionEntity`]
        """
        self._option = option

    @property
    def all_options(self):
        r"""Gets the all_options of this FieldVO.

        字段所有选项。多选列表类型字段的全部选项信息，数组元素包含选项ID、编码、显示名称等属性。

        :return: The all_options of this FieldVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.OptionEntity`]
        """
        return self._all_options

    @all_options.setter
    def all_options(self, all_options):
        r"""Sets the all_options of this FieldVO.

        字段所有选项。多选列表类型字段的全部选项信息，数组元素包含选项ID、编码、显示名称等属性。

        :param all_options: The all_options of this FieldVO.
        :type all_options: list[:class:`huaweicloudsdkprojectman.v4.OptionEntity`]
        """
        self._all_options = all_options

    @property
    def has_same_display_name(self):
        r"""Gets the has_same_display_name of this FieldVO.

        是否存在同名字段。用于检测字段名称冲突。

        :return: The has_same_display_name of this FieldVO.
        :rtype: bool
        """
        return self._has_same_display_name

    @has_same_display_name.setter
    def has_same_display_name(self, has_same_display_name):
        r"""Sets the has_same_display_name of this FieldVO.

        是否存在同名字段。用于检测字段名称冲突。

        :param has_same_display_name: The has_same_display_name of this FieldVO.
        :type has_same_display_name: bool
        """
        self._has_same_display_name = has_same_display_name

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
        if not isinstance(other, FieldVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
