# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FieldResponseBody:

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
        'cloud_pack_version': 'str',
        'business_id': 'str',
        'business_type': 'str',
        'dataclass_name': 'str',
        'business_code': 'str',
        'field_key': 'str',
        'name': 'str',
        'description': 'str',
        'default_value': 'str',
        'display_type': 'str',
        'field_type': 'str',
        'extra_json': 'str',
        'field_tooltip': 'str',
        'iu_type': 'str',
        'used_by': 'str',
        'json_schema': 'str',
        'is_built_in': 'bool',
        'case_sensitive': 'bool',
        'read_only': 'bool',
        'required': 'bool',
        'searchable': 'bool',
        'visible': 'bool',
        'maintainable': 'bool',
        'editable': 'bool',
        'creatable': 'bool',
        'mapping': 'bool',
        'target_api': 'str',
        'creator_id': 'str',
        'creator_name': 'str',
        'modifier_id': 'str',
        'modifier_name': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cloud_pack_version': 'cloud_pack_version',
        'business_id': 'business_id',
        'business_type': 'business_type',
        'dataclass_name': 'dataclass_name',
        'business_code': 'business_code',
        'field_key': 'field_key',
        'name': 'name',
        'description': 'description',
        'default_value': 'default_value',
        'display_type': 'display_type',
        'field_type': 'field_type',
        'extra_json': 'extra_json',
        'field_tooltip': 'field_tooltip',
        'iu_type': 'iu_type',
        'used_by': 'used_by',
        'json_schema': 'json_schema',
        'is_built_in': 'is_built_in',
        'case_sensitive': 'case_sensitive',
        'read_only': 'read_only',
        'required': 'required',
        'searchable': 'searchable',
        'visible': 'visible',
        'maintainable': 'maintainable',
        'editable': 'editable',
        'creatable': 'creatable',
        'mapping': 'mapping',
        'target_api': 'target_api',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'modifier_id': 'modifier_id',
        'modifier_name': 'modifier_name',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, cloud_pack_version=None, business_id=None, business_type=None, dataclass_name=None, business_code=None, field_key=None, name=None, description=None, default_value=None, display_type=None, field_type=None, extra_json=None, field_tooltip=None, iu_type=None, used_by=None, json_schema=None, is_built_in=None, case_sensitive=None, read_only=None, required=None, searchable=None, visible=None, maintainable=None, editable=None, creatable=None, mapping=None, target_api=None, creator_id=None, creator_name=None, modifier_id=None, modifier_name=None, create_time=None, update_time=None):
        """FieldResponseBody

        The model defined in huaweicloud sdk

        :param id: Id value
        :type id: str
        :param cloud_pack_version: 订阅包版本
        :type cloud_pack_version: str
        :param business_id: 关联业务id
        :type business_id: str
        :param business_type: 关联业务
        :type business_type: str
        :param dataclass_name: 数据类名称
        :type dataclass_name: str
        :param business_code: 字段业务编码
        :type business_code: str
        :param field_key: 字段key
        :type field_key: str
        :param name: 字段名称
        :type name: str
        :param description: 字段描述
        :type description: str
        :param default_value: 默认值
        :type default_value: str
        :param display_type: 显示类型
        :type display_type: str
        :param field_type: 字段类型，如shorttext,radio,grid等
        :type field_type: str
        :param extra_json: 附加json
        :type extra_json: str
        :param field_tooltip: 工具提示
        :type field_tooltip: str
        :param iu_type: 输入输出类型
        :type iu_type: str
        :param used_by: 使用业务
        :type used_by: str
        :param json_schema: json模式
        :type json_schema: str
        :param is_built_in: 是否内置，true内置，false非内置
        :type is_built_in: bool
        :param case_sensitive: 大小写敏感，true敏感，false不敏感
        :type case_sensitive: bool
        :param read_only: 只读模式，true只读，false非只读
        :type read_only: bool
        :param required: 是否必填，true必填，false非必填
        :type required: bool
        :param searchable: 可搜索，true可搜索，false非可搜索
        :type searchable: bool
        :param visible: 可见，true可见，false非可见
        :type visible: bool
        :param maintainable: 可维护，true可维护，false非可维护
        :type maintainable: bool
        :param editable: 可编辑，true可编辑，false非可编辑
        :type editable: bool
        :param creatable: 可创建，true可创建，false非可创建
        :type creatable: bool
        :param mapping: 是否展示在分类映射外的其他地方
        :type mapping: bool
        :param target_api: 目标api
        :type target_api: str
        :param creator_id: Creator id value
        :type creator_id: str
        :param creator_name: Creator name value
        :type creator_name: str
        :param modifier_id: Modifier id value
        :type modifier_id: str
        :param modifier_name: Modifier name value
        :type modifier_name: str
        :param create_time: Create time
        :type create_time: str
        :param update_time: Update time
        :type update_time: str
        """
        
        

        self._id = None
        self._cloud_pack_version = None
        self._business_id = None
        self._business_type = None
        self._dataclass_name = None
        self._business_code = None
        self._field_key = None
        self._name = None
        self._description = None
        self._default_value = None
        self._display_type = None
        self._field_type = None
        self._extra_json = None
        self._field_tooltip = None
        self._iu_type = None
        self._used_by = None
        self._json_schema = None
        self._is_built_in = None
        self._case_sensitive = None
        self._read_only = None
        self._required = None
        self._searchable = None
        self._visible = None
        self._maintainable = None
        self._editable = None
        self._creatable = None
        self._mapping = None
        self._target_api = None
        self._creator_id = None
        self._creator_name = None
        self._modifier_id = None
        self._modifier_name = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cloud_pack_version is not None:
            self.cloud_pack_version = cloud_pack_version
        if business_id is not None:
            self.business_id = business_id
        if business_type is not None:
            self.business_type = business_type
        if dataclass_name is not None:
            self.dataclass_name = dataclass_name
        if business_code is not None:
            self.business_code = business_code
        if field_key is not None:
            self.field_key = field_key
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if default_value is not None:
            self.default_value = default_value
        if display_type is not None:
            self.display_type = display_type
        if field_type is not None:
            self.field_type = field_type
        if extra_json is not None:
            self.extra_json = extra_json
        if field_tooltip is not None:
            self.field_tooltip = field_tooltip
        if iu_type is not None:
            self.iu_type = iu_type
        if used_by is not None:
            self.used_by = used_by
        if json_schema is not None:
            self.json_schema = json_schema
        if is_built_in is not None:
            self.is_built_in = is_built_in
        if case_sensitive is not None:
            self.case_sensitive = case_sensitive
        if read_only is not None:
            self.read_only = read_only
        if required is not None:
            self.required = required
        if searchable is not None:
            self.searchable = searchable
        if visible is not None:
            self.visible = visible
        if maintainable is not None:
            self.maintainable = maintainable
        if editable is not None:
            self.editable = editable
        if creatable is not None:
            self.creatable = creatable
        if mapping is not None:
            self.mapping = mapping
        if target_api is not None:
            self.target_api = target_api
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if modifier_id is not None:
            self.modifier_id = modifier_id
        if modifier_name is not None:
            self.modifier_name = modifier_name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this FieldResponseBody.

        Id value

        :return: The id of this FieldResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FieldResponseBody.

        Id value

        :param id: The id of this FieldResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def cloud_pack_version(self):
        """Gets the cloud_pack_version of this FieldResponseBody.

        订阅包版本

        :return: The cloud_pack_version of this FieldResponseBody.
        :rtype: str
        """
        return self._cloud_pack_version

    @cloud_pack_version.setter
    def cloud_pack_version(self, cloud_pack_version):
        """Sets the cloud_pack_version of this FieldResponseBody.

        订阅包版本

        :param cloud_pack_version: The cloud_pack_version of this FieldResponseBody.
        :type cloud_pack_version: str
        """
        self._cloud_pack_version = cloud_pack_version

    @property
    def business_id(self):
        """Gets the business_id of this FieldResponseBody.

        关联业务id

        :return: The business_id of this FieldResponseBody.
        :rtype: str
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this FieldResponseBody.

        关联业务id

        :param business_id: The business_id of this FieldResponseBody.
        :type business_id: str
        """
        self._business_id = business_id

    @property
    def business_type(self):
        """Gets the business_type of this FieldResponseBody.

        关联业务

        :return: The business_type of this FieldResponseBody.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this FieldResponseBody.

        关联业务

        :param business_type: The business_type of this FieldResponseBody.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def dataclass_name(self):
        """Gets the dataclass_name of this FieldResponseBody.

        数据类名称

        :return: The dataclass_name of this FieldResponseBody.
        :rtype: str
        """
        return self._dataclass_name

    @dataclass_name.setter
    def dataclass_name(self, dataclass_name):
        """Sets the dataclass_name of this FieldResponseBody.

        数据类名称

        :param dataclass_name: The dataclass_name of this FieldResponseBody.
        :type dataclass_name: str
        """
        self._dataclass_name = dataclass_name

    @property
    def business_code(self):
        """Gets the business_code of this FieldResponseBody.

        字段业务编码

        :return: The business_code of this FieldResponseBody.
        :rtype: str
        """
        return self._business_code

    @business_code.setter
    def business_code(self, business_code):
        """Sets the business_code of this FieldResponseBody.

        字段业务编码

        :param business_code: The business_code of this FieldResponseBody.
        :type business_code: str
        """
        self._business_code = business_code

    @property
    def field_key(self):
        """Gets the field_key of this FieldResponseBody.

        字段key

        :return: The field_key of this FieldResponseBody.
        :rtype: str
        """
        return self._field_key

    @field_key.setter
    def field_key(self, field_key):
        """Sets the field_key of this FieldResponseBody.

        字段key

        :param field_key: The field_key of this FieldResponseBody.
        :type field_key: str
        """
        self._field_key = field_key

    @property
    def name(self):
        """Gets the name of this FieldResponseBody.

        字段名称

        :return: The name of this FieldResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FieldResponseBody.

        字段名称

        :param name: The name of this FieldResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this FieldResponseBody.

        字段描述

        :return: The description of this FieldResponseBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FieldResponseBody.

        字段描述

        :param description: The description of this FieldResponseBody.
        :type description: str
        """
        self._description = description

    @property
    def default_value(self):
        """Gets the default_value of this FieldResponseBody.

        默认值

        :return: The default_value of this FieldResponseBody.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this FieldResponseBody.

        默认值

        :param default_value: The default_value of this FieldResponseBody.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def display_type(self):
        """Gets the display_type of this FieldResponseBody.

        显示类型

        :return: The display_type of this FieldResponseBody.
        :rtype: str
        """
        return self._display_type

    @display_type.setter
    def display_type(self, display_type):
        """Sets the display_type of this FieldResponseBody.

        显示类型

        :param display_type: The display_type of this FieldResponseBody.
        :type display_type: str
        """
        self._display_type = display_type

    @property
    def field_type(self):
        """Gets the field_type of this FieldResponseBody.

        字段类型，如shorttext,radio,grid等

        :return: The field_type of this FieldResponseBody.
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this FieldResponseBody.

        字段类型，如shorttext,radio,grid等

        :param field_type: The field_type of this FieldResponseBody.
        :type field_type: str
        """
        self._field_type = field_type

    @property
    def extra_json(self):
        """Gets the extra_json of this FieldResponseBody.

        附加json

        :return: The extra_json of this FieldResponseBody.
        :rtype: str
        """
        return self._extra_json

    @extra_json.setter
    def extra_json(self, extra_json):
        """Sets the extra_json of this FieldResponseBody.

        附加json

        :param extra_json: The extra_json of this FieldResponseBody.
        :type extra_json: str
        """
        self._extra_json = extra_json

    @property
    def field_tooltip(self):
        """Gets the field_tooltip of this FieldResponseBody.

        工具提示

        :return: The field_tooltip of this FieldResponseBody.
        :rtype: str
        """
        return self._field_tooltip

    @field_tooltip.setter
    def field_tooltip(self, field_tooltip):
        """Sets the field_tooltip of this FieldResponseBody.

        工具提示

        :param field_tooltip: The field_tooltip of this FieldResponseBody.
        :type field_tooltip: str
        """
        self._field_tooltip = field_tooltip

    @property
    def iu_type(self):
        """Gets the iu_type of this FieldResponseBody.

        输入输出类型

        :return: The iu_type of this FieldResponseBody.
        :rtype: str
        """
        return self._iu_type

    @iu_type.setter
    def iu_type(self, iu_type):
        """Sets the iu_type of this FieldResponseBody.

        输入输出类型

        :param iu_type: The iu_type of this FieldResponseBody.
        :type iu_type: str
        """
        self._iu_type = iu_type

    @property
    def used_by(self):
        """Gets the used_by of this FieldResponseBody.

        使用业务

        :return: The used_by of this FieldResponseBody.
        :rtype: str
        """
        return self._used_by

    @used_by.setter
    def used_by(self, used_by):
        """Sets the used_by of this FieldResponseBody.

        使用业务

        :param used_by: The used_by of this FieldResponseBody.
        :type used_by: str
        """
        self._used_by = used_by

    @property
    def json_schema(self):
        """Gets the json_schema of this FieldResponseBody.

        json模式

        :return: The json_schema of this FieldResponseBody.
        :rtype: str
        """
        return self._json_schema

    @json_schema.setter
    def json_schema(self, json_schema):
        """Sets the json_schema of this FieldResponseBody.

        json模式

        :param json_schema: The json_schema of this FieldResponseBody.
        :type json_schema: str
        """
        self._json_schema = json_schema

    @property
    def is_built_in(self):
        """Gets the is_built_in of this FieldResponseBody.

        是否内置，true内置，false非内置

        :return: The is_built_in of this FieldResponseBody.
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        """Sets the is_built_in of this FieldResponseBody.

        是否内置，true内置，false非内置

        :param is_built_in: The is_built_in of this FieldResponseBody.
        :type is_built_in: bool
        """
        self._is_built_in = is_built_in

    @property
    def case_sensitive(self):
        """Gets the case_sensitive of this FieldResponseBody.

        大小写敏感，true敏感，false不敏感

        :return: The case_sensitive of this FieldResponseBody.
        :rtype: bool
        """
        return self._case_sensitive

    @case_sensitive.setter
    def case_sensitive(self, case_sensitive):
        """Sets the case_sensitive of this FieldResponseBody.

        大小写敏感，true敏感，false不敏感

        :param case_sensitive: The case_sensitive of this FieldResponseBody.
        :type case_sensitive: bool
        """
        self._case_sensitive = case_sensitive

    @property
    def read_only(self):
        """Gets the read_only of this FieldResponseBody.

        只读模式，true只读，false非只读

        :return: The read_only of this FieldResponseBody.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this FieldResponseBody.

        只读模式，true只读，false非只读

        :param read_only: The read_only of this FieldResponseBody.
        :type read_only: bool
        """
        self._read_only = read_only

    @property
    def required(self):
        """Gets the required of this FieldResponseBody.

        是否必填，true必填，false非必填

        :return: The required of this FieldResponseBody.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this FieldResponseBody.

        是否必填，true必填，false非必填

        :param required: The required of this FieldResponseBody.
        :type required: bool
        """
        self._required = required

    @property
    def searchable(self):
        """Gets the searchable of this FieldResponseBody.

        可搜索，true可搜索，false非可搜索

        :return: The searchable of this FieldResponseBody.
        :rtype: bool
        """
        return self._searchable

    @searchable.setter
    def searchable(self, searchable):
        """Sets the searchable of this FieldResponseBody.

        可搜索，true可搜索，false非可搜索

        :param searchable: The searchable of this FieldResponseBody.
        :type searchable: bool
        """
        self._searchable = searchable

    @property
    def visible(self):
        """Gets the visible of this FieldResponseBody.

        可见，true可见，false非可见

        :return: The visible of this FieldResponseBody.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this FieldResponseBody.

        可见，true可见，false非可见

        :param visible: The visible of this FieldResponseBody.
        :type visible: bool
        """
        self._visible = visible

    @property
    def maintainable(self):
        """Gets the maintainable of this FieldResponseBody.

        可维护，true可维护，false非可维护

        :return: The maintainable of this FieldResponseBody.
        :rtype: bool
        """
        return self._maintainable

    @maintainable.setter
    def maintainable(self, maintainable):
        """Sets the maintainable of this FieldResponseBody.

        可维护，true可维护，false非可维护

        :param maintainable: The maintainable of this FieldResponseBody.
        :type maintainable: bool
        """
        self._maintainable = maintainable

    @property
    def editable(self):
        """Gets the editable of this FieldResponseBody.

        可编辑，true可编辑，false非可编辑

        :return: The editable of this FieldResponseBody.
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this FieldResponseBody.

        可编辑，true可编辑，false非可编辑

        :param editable: The editable of this FieldResponseBody.
        :type editable: bool
        """
        self._editable = editable

    @property
    def creatable(self):
        """Gets the creatable of this FieldResponseBody.

        可创建，true可创建，false非可创建

        :return: The creatable of this FieldResponseBody.
        :rtype: bool
        """
        return self._creatable

    @creatable.setter
    def creatable(self, creatable):
        """Sets the creatable of this FieldResponseBody.

        可创建，true可创建，false非可创建

        :param creatable: The creatable of this FieldResponseBody.
        :type creatable: bool
        """
        self._creatable = creatable

    @property
    def mapping(self):
        """Gets the mapping of this FieldResponseBody.

        是否展示在分类映射外的其他地方

        :return: The mapping of this FieldResponseBody.
        :rtype: bool
        """
        return self._mapping

    @mapping.setter
    def mapping(self, mapping):
        """Sets the mapping of this FieldResponseBody.

        是否展示在分类映射外的其他地方

        :param mapping: The mapping of this FieldResponseBody.
        :type mapping: bool
        """
        self._mapping = mapping

    @property
    def target_api(self):
        """Gets the target_api of this FieldResponseBody.

        目标api

        :return: The target_api of this FieldResponseBody.
        :rtype: str
        """
        return self._target_api

    @target_api.setter
    def target_api(self, target_api):
        """Sets the target_api of this FieldResponseBody.

        目标api

        :param target_api: The target_api of this FieldResponseBody.
        :type target_api: str
        """
        self._target_api = target_api

    @property
    def creator_id(self):
        """Gets the creator_id of this FieldResponseBody.

        Creator id value

        :return: The creator_id of this FieldResponseBody.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this FieldResponseBody.

        Creator id value

        :param creator_id: The creator_id of this FieldResponseBody.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        """Gets the creator_name of this FieldResponseBody.

        Creator name value

        :return: The creator_name of this FieldResponseBody.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this FieldResponseBody.

        Creator name value

        :param creator_name: The creator_name of this FieldResponseBody.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def modifier_id(self):
        """Gets the modifier_id of this FieldResponseBody.

        Modifier id value

        :return: The modifier_id of this FieldResponseBody.
        :rtype: str
        """
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, modifier_id):
        """Sets the modifier_id of this FieldResponseBody.

        Modifier id value

        :param modifier_id: The modifier_id of this FieldResponseBody.
        :type modifier_id: str
        """
        self._modifier_id = modifier_id

    @property
    def modifier_name(self):
        """Gets the modifier_name of this FieldResponseBody.

        Modifier name value

        :return: The modifier_name of this FieldResponseBody.
        :rtype: str
        """
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, modifier_name):
        """Sets the modifier_name of this FieldResponseBody.

        Modifier name value

        :param modifier_name: The modifier_name of this FieldResponseBody.
        :type modifier_name: str
        """
        self._modifier_name = modifier_name

    @property
    def create_time(self):
        """Gets the create_time of this FieldResponseBody.

        Create time

        :return: The create_time of this FieldResponseBody.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this FieldResponseBody.

        Create time

        :param create_time: The create_time of this FieldResponseBody.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this FieldResponseBody.

        Update time

        :return: The update_time of this FieldResponseBody.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this FieldResponseBody.

        Update time

        :param update_time: The update_time of this FieldResponseBody.
        :type update_time: str
        """
        self._update_time = update_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FieldResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
