# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FieldEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'display_name': 'str',
        'code': 'str',
        'id': 'str',
        'description': 'str',
        'created_by': 'str',
        'created_date': 'int',
        'modified_by': 'str',
        'definition_type': 'str',
        'field_type_name': 'str',
        'required': 'bool',
        'controlled': 'bool',
        'immutable': 'bool',
        'no': 'int',
        'all_options': 'list[OptionEntity]'
    }

    attribute_map = {
        'display_name': 'display_name',
        'code': 'code',
        'id': 'id',
        'description': 'description',
        'created_by': 'created_by',
        'created_date': 'created_date',
        'modified_by': 'modified_by',
        'definition_type': 'definition_type',
        'field_type_name': 'field_type_name',
        'required': 'required',
        'controlled': 'controlled',
        'immutable': 'immutable',
        'no': 'no',
        'all_options': 'all_options'
    }

    def __init__(self, display_name=None, code=None, id=None, description=None, created_by=None, created_date=None, modified_by=None, definition_type=None, field_type_name=None, required=None, controlled=None, immutable=None, no=None, all_options=None):
        r"""FieldEntity

        The model defined in huaweicloud sdk

        :param display_name: **参数解释**： 字段名称。 **取值范围**： 不涉及
        :type display_name: str
        :param code: **参数解释**： 字段code。 **取值范围**： 不涉及
        :type code: str
        :param id: **参数解释**： 字段id。 **取值范围**： 不涉及
        :type id: str
        :param description: **参数解释**： 字段描述。 **取值范围**： 不涉及
        :type description: str
        :param created_by: **参数解释**： 字段创建人名称。 **取值范围**： 不涉及
        :type created_by: str
        :param created_date: **参数解释**： 字段创建时间，时间戳格式，示例:1715305846000。 **取值范围**： 不涉及
        :type created_date: int
        :param modified_by: **参数解释**： 字段最后更新人名称。 **取值范围**： 不涉及
        :type modified_by: str
        :param definition_type: **参数解释**： 字段级别。 **取值范围**： 1/2/3：系统预设字段。 4：租户自定义字段 5：项目自定义字段
        :type definition_type: str
        :param field_type_name: **参数解释**： 字段类型名称。 **取值范围**： 不涉及
        :type field_type_name: str
        :param required: **参数解释**： 字段在工作项中是否必填，和工作流配置不一致时以工作流为准。 **取值范围**： true（必填） false（非必填）
        :type required: bool
        :param controlled: **参数解释**： 字段在工作项中是否受控，修改已基线的工作项受控字段需要走变更评审流程，和工作流配置不一致时以工作流为准。 **取值范围**： true（受控） false（非受控）
        :type controlled: bool
        :param immutable: **参数解释**： 字段在工作项中是否可修改，和工作流配置不一致时以工作流为准。 **取值范围**： true（不可修改） false（可修改）
        :type immutable: bool
        :param no: **参数解释**： 字段排序的序号。 **取值范围**： 不涉及
        :type no: int
        :param all_options: **参数解释**： 字段选项。
        :type all_options: list[:class:`huaweicloudsdkprojectman.v4.OptionEntity`]
        """
        
        

        self._display_name = None
        self._code = None
        self._id = None
        self._description = None
        self._created_by = None
        self._created_date = None
        self._modified_by = None
        self._definition_type = None
        self._field_type_name = None
        self._required = None
        self._controlled = None
        self._immutable = None
        self._no = None
        self._all_options = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if code is not None:
            self.code = code
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if created_by is not None:
            self.created_by = created_by
        if created_date is not None:
            self.created_date = created_date
        if modified_by is not None:
            self.modified_by = modified_by
        if definition_type is not None:
            self.definition_type = definition_type
        if field_type_name is not None:
            self.field_type_name = field_type_name
        if required is not None:
            self.required = required
        if controlled is not None:
            self.controlled = controlled
        if immutable is not None:
            self.immutable = immutable
        if no is not None:
            self.no = no
        if all_options is not None:
            self.all_options = all_options

    @property
    def display_name(self):
        r"""Gets the display_name of this FieldEntity.

        **参数解释**： 字段名称。 **取值范围**： 不涉及

        :return: The display_name of this FieldEntity.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this FieldEntity.

        **参数解释**： 字段名称。 **取值范围**： 不涉及

        :param display_name: The display_name of this FieldEntity.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def code(self):
        r"""Gets the code of this FieldEntity.

        **参数解释**： 字段code。 **取值范围**： 不涉及

        :return: The code of this FieldEntity.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this FieldEntity.

        **参数解释**： 字段code。 **取值范围**： 不涉及

        :param code: The code of this FieldEntity.
        :type code: str
        """
        self._code = code

    @property
    def id(self):
        r"""Gets the id of this FieldEntity.

        **参数解释**： 字段id。 **取值范围**： 不涉及

        :return: The id of this FieldEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FieldEntity.

        **参数解释**： 字段id。 **取值范围**： 不涉及

        :param id: The id of this FieldEntity.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this FieldEntity.

        **参数解释**： 字段描述。 **取值范围**： 不涉及

        :return: The description of this FieldEntity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this FieldEntity.

        **参数解释**： 字段描述。 **取值范围**： 不涉及

        :param description: The description of this FieldEntity.
        :type description: str
        """
        self._description = description

    @property
    def created_by(self):
        r"""Gets the created_by of this FieldEntity.

        **参数解释**： 字段创建人名称。 **取值范围**： 不涉及

        :return: The created_by of this FieldEntity.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this FieldEntity.

        **参数解释**： 字段创建人名称。 **取值范围**： 不涉及

        :param created_by: The created_by of this FieldEntity.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def created_date(self):
        r"""Gets the created_date of this FieldEntity.

        **参数解释**： 字段创建时间，时间戳格式，示例:1715305846000。 **取值范围**： 不涉及

        :return: The created_date of this FieldEntity.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this FieldEntity.

        **参数解释**： 字段创建时间，时间戳格式，示例:1715305846000。 **取值范围**： 不涉及

        :param created_date: The created_date of this FieldEntity.
        :type created_date: int
        """
        self._created_date = created_date

    @property
    def modified_by(self):
        r"""Gets the modified_by of this FieldEntity.

        **参数解释**： 字段最后更新人名称。 **取值范围**： 不涉及

        :return: The modified_by of this FieldEntity.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this FieldEntity.

        **参数解释**： 字段最后更新人名称。 **取值范围**： 不涉及

        :param modified_by: The modified_by of this FieldEntity.
        :type modified_by: str
        """
        self._modified_by = modified_by

    @property
    def definition_type(self):
        r"""Gets the definition_type of this FieldEntity.

        **参数解释**： 字段级别。 **取值范围**： 1/2/3：系统预设字段。 4：租户自定义字段 5：项目自定义字段

        :return: The definition_type of this FieldEntity.
        :rtype: str
        """
        return self._definition_type

    @definition_type.setter
    def definition_type(self, definition_type):
        r"""Sets the definition_type of this FieldEntity.

        **参数解释**： 字段级别。 **取值范围**： 1/2/3：系统预设字段。 4：租户自定义字段 5：项目自定义字段

        :param definition_type: The definition_type of this FieldEntity.
        :type definition_type: str
        """
        self._definition_type = definition_type

    @property
    def field_type_name(self):
        r"""Gets the field_type_name of this FieldEntity.

        **参数解释**： 字段类型名称。 **取值范围**： 不涉及

        :return: The field_type_name of this FieldEntity.
        :rtype: str
        """
        return self._field_type_name

    @field_type_name.setter
    def field_type_name(self, field_type_name):
        r"""Sets the field_type_name of this FieldEntity.

        **参数解释**： 字段类型名称。 **取值范围**： 不涉及

        :param field_type_name: The field_type_name of this FieldEntity.
        :type field_type_name: str
        """
        self._field_type_name = field_type_name

    @property
    def required(self):
        r"""Gets the required of this FieldEntity.

        **参数解释**： 字段在工作项中是否必填，和工作流配置不一致时以工作流为准。 **取值范围**： true（必填） false（非必填）

        :return: The required of this FieldEntity.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this FieldEntity.

        **参数解释**： 字段在工作项中是否必填，和工作流配置不一致时以工作流为准。 **取值范围**： true（必填） false（非必填）

        :param required: The required of this FieldEntity.
        :type required: bool
        """
        self._required = required

    @property
    def controlled(self):
        r"""Gets the controlled of this FieldEntity.

        **参数解释**： 字段在工作项中是否受控，修改已基线的工作项受控字段需要走变更评审流程，和工作流配置不一致时以工作流为准。 **取值范围**： true（受控） false（非受控）

        :return: The controlled of this FieldEntity.
        :rtype: bool
        """
        return self._controlled

    @controlled.setter
    def controlled(self, controlled):
        r"""Sets the controlled of this FieldEntity.

        **参数解释**： 字段在工作项中是否受控，修改已基线的工作项受控字段需要走变更评审流程，和工作流配置不一致时以工作流为准。 **取值范围**： true（受控） false（非受控）

        :param controlled: The controlled of this FieldEntity.
        :type controlled: bool
        """
        self._controlled = controlled

    @property
    def immutable(self):
        r"""Gets the immutable of this FieldEntity.

        **参数解释**： 字段在工作项中是否可修改，和工作流配置不一致时以工作流为准。 **取值范围**： true（不可修改） false（可修改）

        :return: The immutable of this FieldEntity.
        :rtype: bool
        """
        return self._immutable

    @immutable.setter
    def immutable(self, immutable):
        r"""Sets the immutable of this FieldEntity.

        **参数解释**： 字段在工作项中是否可修改，和工作流配置不一致时以工作流为准。 **取值范围**： true（不可修改） false（可修改）

        :param immutable: The immutable of this FieldEntity.
        :type immutable: bool
        """
        self._immutable = immutable

    @property
    def no(self):
        r"""Gets the no of this FieldEntity.

        **参数解释**： 字段排序的序号。 **取值范围**： 不涉及

        :return: The no of this FieldEntity.
        :rtype: int
        """
        return self._no

    @no.setter
    def no(self, no):
        r"""Sets the no of this FieldEntity.

        **参数解释**： 字段排序的序号。 **取值范围**： 不涉及

        :param no: The no of this FieldEntity.
        :type no: int
        """
        self._no = no

    @property
    def all_options(self):
        r"""Gets the all_options of this FieldEntity.

        **参数解释**： 字段选项。

        :return: The all_options of this FieldEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.OptionEntity`]
        """
        return self._all_options

    @all_options.setter
    def all_options(self, all_options):
        r"""Sets the all_options of this FieldEntity.

        **参数解释**： 字段选项。

        :param all_options: The all_options of this FieldEntity.
        :type all_options: list[:class:`huaweicloudsdkprojectman.v4.OptionEntity`]
        """
        self._all_options = all_options

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
        if not isinstance(other, FieldEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
