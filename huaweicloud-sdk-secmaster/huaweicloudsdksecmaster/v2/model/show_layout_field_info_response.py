# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLayoutFieldInfoResponse(SdkResponse):

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
        'cloud_pack_id': 'str',
        'cloud_pack_name': 'str',
        'dataclass_id': 'str',
        'cloud_pack_version': 'str',
        'field_key': 'str',
        'name': 'str',
        'description': 'str',
        'en_description': 'str',
        'default_value': 'str',
        'en_default_value': 'str',
        'field_type': 'str',
        'extra_json': 'str',
        'field_tooltip': 'str',
        'en_field_tooltip': 'str',
        'json_schema': 'str',
        'is_built_in': 'bool',
        'read_only': 'bool',
        'required': 'bool',
        'searchable': 'bool',
        'visible': 'bool',
        'maintainable': 'bool',
        'editable': 'bool',
        'creatable': 'bool',
        'creator_id': 'str',
        'creator_name': 'str',
        'modifier_id': 'str',
        'modifier_name': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'wizard_id': 'str',
        'aopworkflow_id': 'str',
        'aopworkflow_version_id': 'str',
        'playbook_id': 'str',
        'playbook_version_id': 'str',
        'boa_version': 'str',
        'version': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cloud_pack_id': 'cloud_pack_id',
        'cloud_pack_name': 'cloud_pack_name',
        'dataclass_id': 'dataclass_id',
        'cloud_pack_version': 'cloud_pack_version',
        'field_key': 'field_key',
        'name': 'name',
        'description': 'description',
        'en_description': 'en_description',
        'default_value': 'default_value',
        'en_default_value': 'en_default_value',
        'field_type': 'field_type',
        'extra_json': 'extra_json',
        'field_tooltip': 'field_tooltip',
        'en_field_tooltip': 'en_field_tooltip',
        'json_schema': 'json_schema',
        'is_built_in': 'is_built_in',
        'read_only': 'read_only',
        'required': 'required',
        'searchable': 'searchable',
        'visible': 'visible',
        'maintainable': 'maintainable',
        'editable': 'editable',
        'creatable': 'creatable',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'modifier_id': 'modifier_id',
        'modifier_name': 'modifier_name',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'wizard_id': 'wizard_id',
        'aopworkflow_id': 'aopworkflow_id',
        'aopworkflow_version_id': 'aopworkflow_version_id',
        'playbook_id': 'playbook_id',
        'playbook_version_id': 'playbook_version_id',
        'boa_version': 'boa_version',
        'version': 'version',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, id=None, cloud_pack_id=None, cloud_pack_name=None, dataclass_id=None, cloud_pack_version=None, field_key=None, name=None, description=None, en_description=None, default_value=None, en_default_value=None, field_type=None, extra_json=None, field_tooltip=None, en_field_tooltip=None, json_schema=None, is_built_in=None, read_only=None, required=None, searchable=None, visible=None, maintainable=None, editable=None, creatable=None, creator_id=None, creator_name=None, modifier_id=None, modifier_name=None, create_time=None, update_time=None, wizard_id=None, aopworkflow_id=None, aopworkflow_version_id=None, playbook_id=None, playbook_version_id=None, boa_version=None, version=None, x_request_id=None):
        r"""ShowLayoutFieldInfoResponse

        The model defined in huaweicloud sdk

        :param id: 字段ID
        :type id: str
        :param cloud_pack_id: 订阅包id
        :type cloud_pack_id: str
        :param cloud_pack_name: 订阅包名称
        :type cloud_pack_name: str
        :param dataclass_id: 数据类ID
        :type dataclass_id: str
        :param cloud_pack_version: 订阅包版本
        :type cloud_pack_version: str
        :param field_key: 字段key
        :type field_key: str
        :param name: 字段名称
        :type name: str
        :param description: 字段描述
        :type description: str
        :param en_description: 字段英文描述
        :type en_description: str
        :param default_value: 默认值
        :type default_value: str
        :param en_default_value: 字段英文默认值
        :type en_default_value: str
        :param field_type: 字段类型，如shorttext,radio,grid等
        :type field_type: str
        :param extra_json: 附加json
        :type extra_json: str
        :param field_tooltip: 工具提示
        :type field_tooltip: str
        :param en_field_tooltip: 英文工具提示
        :type en_field_tooltip: str
        :param json_schema: json模式
        :type json_schema: str
        :param is_built_in: 是否内置，true内置，false非内置
        :type is_built_in: bool
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
        :param creator_id: 创建者ID
        :type creator_id: str
        :param creator_name: 创建者名称
        :type creator_name: str
        :param modifier_id: 修改者ID
        :type modifier_id: str
        :param modifier_name: 修改者名称
        :type modifier_name: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param wizard_id: 字段绑定的页面id
        :type wizard_id: str
        :param aopworkflow_id: 字段绑定的流程id
        :type aopworkflow_id: str
        :param aopworkflow_version_id: 字段绑定的流程版本id
        :type aopworkflow_version_id: str
        :param playbook_id: 字段绑定的剧本id
        :type playbook_id: str
        :param playbook_version_id: 字段绑定的剧本版本id
        :type playbook_version_id: str
        :param boa_version: BOA底座版本
        :type boa_version: str
        :param version: 安全云脑版本
        :type version: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._id = None
        self._cloud_pack_id = None
        self._cloud_pack_name = None
        self._dataclass_id = None
        self._cloud_pack_version = None
        self._field_key = None
        self._name = None
        self._description = None
        self._en_description = None
        self._default_value = None
        self._en_default_value = None
        self._field_type = None
        self._extra_json = None
        self._field_tooltip = None
        self._en_field_tooltip = None
        self._json_schema = None
        self._is_built_in = None
        self._read_only = None
        self._required = None
        self._searchable = None
        self._visible = None
        self._maintainable = None
        self._editable = None
        self._creatable = None
        self._creator_id = None
        self._creator_name = None
        self._modifier_id = None
        self._modifier_name = None
        self._create_time = None
        self._update_time = None
        self._wizard_id = None
        self._aopworkflow_id = None
        self._aopworkflow_version_id = None
        self._playbook_id = None
        self._playbook_version_id = None
        self._boa_version = None
        self._version = None
        self._x_request_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cloud_pack_id is not None:
            self.cloud_pack_id = cloud_pack_id
        if cloud_pack_name is not None:
            self.cloud_pack_name = cloud_pack_name
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if cloud_pack_version is not None:
            self.cloud_pack_version = cloud_pack_version
        if field_key is not None:
            self.field_key = field_key
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if en_description is not None:
            self.en_description = en_description
        if default_value is not None:
            self.default_value = default_value
        if en_default_value is not None:
            self.en_default_value = en_default_value
        if field_type is not None:
            self.field_type = field_type
        if extra_json is not None:
            self.extra_json = extra_json
        if field_tooltip is not None:
            self.field_tooltip = field_tooltip
        if en_field_tooltip is not None:
            self.en_field_tooltip = en_field_tooltip
        if json_schema is not None:
            self.json_schema = json_schema
        if is_built_in is not None:
            self.is_built_in = is_built_in
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
        if wizard_id is not None:
            self.wizard_id = wizard_id
        if aopworkflow_id is not None:
            self.aopworkflow_id = aopworkflow_id
        if aopworkflow_version_id is not None:
            self.aopworkflow_version_id = aopworkflow_version_id
        if playbook_id is not None:
            self.playbook_id = playbook_id
        if playbook_version_id is not None:
            self.playbook_version_id = playbook_version_id
        if boa_version is not None:
            self.boa_version = boa_version
        if version is not None:
            self.version = version
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def id(self):
        r"""Gets the id of this ShowLayoutFieldInfoResponse.

        字段ID

        :return: The id of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowLayoutFieldInfoResponse.

        字段ID

        :param id: The id of this ShowLayoutFieldInfoResponse.
        :type id: str
        """
        self._id = id

    @property
    def cloud_pack_id(self):
        r"""Gets the cloud_pack_id of this ShowLayoutFieldInfoResponse.

        订阅包id

        :return: The cloud_pack_id of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._cloud_pack_id

    @cloud_pack_id.setter
    def cloud_pack_id(self, cloud_pack_id):
        r"""Sets the cloud_pack_id of this ShowLayoutFieldInfoResponse.

        订阅包id

        :param cloud_pack_id: The cloud_pack_id of this ShowLayoutFieldInfoResponse.
        :type cloud_pack_id: str
        """
        self._cloud_pack_id = cloud_pack_id

    @property
    def cloud_pack_name(self):
        r"""Gets the cloud_pack_name of this ShowLayoutFieldInfoResponse.

        订阅包名称

        :return: The cloud_pack_name of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._cloud_pack_name

    @cloud_pack_name.setter
    def cloud_pack_name(self, cloud_pack_name):
        r"""Sets the cloud_pack_name of this ShowLayoutFieldInfoResponse.

        订阅包名称

        :param cloud_pack_name: The cloud_pack_name of this ShowLayoutFieldInfoResponse.
        :type cloud_pack_name: str
        """
        self._cloud_pack_name = cloud_pack_name

    @property
    def dataclass_id(self):
        r"""Gets the dataclass_id of this ShowLayoutFieldInfoResponse.

        数据类ID

        :return: The dataclass_id of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        r"""Sets the dataclass_id of this ShowLayoutFieldInfoResponse.

        数据类ID

        :param dataclass_id: The dataclass_id of this ShowLayoutFieldInfoResponse.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def cloud_pack_version(self):
        r"""Gets the cloud_pack_version of this ShowLayoutFieldInfoResponse.

        订阅包版本

        :return: The cloud_pack_version of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._cloud_pack_version

    @cloud_pack_version.setter
    def cloud_pack_version(self, cloud_pack_version):
        r"""Sets the cloud_pack_version of this ShowLayoutFieldInfoResponse.

        订阅包版本

        :param cloud_pack_version: The cloud_pack_version of this ShowLayoutFieldInfoResponse.
        :type cloud_pack_version: str
        """
        self._cloud_pack_version = cloud_pack_version

    @property
    def field_key(self):
        r"""Gets the field_key of this ShowLayoutFieldInfoResponse.

        字段key

        :return: The field_key of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._field_key

    @field_key.setter
    def field_key(self, field_key):
        r"""Sets the field_key of this ShowLayoutFieldInfoResponse.

        字段key

        :param field_key: The field_key of this ShowLayoutFieldInfoResponse.
        :type field_key: str
        """
        self._field_key = field_key

    @property
    def name(self):
        r"""Gets the name of this ShowLayoutFieldInfoResponse.

        字段名称

        :return: The name of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowLayoutFieldInfoResponse.

        字段名称

        :param name: The name of this ShowLayoutFieldInfoResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowLayoutFieldInfoResponse.

        字段描述

        :return: The description of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowLayoutFieldInfoResponse.

        字段描述

        :param description: The description of this ShowLayoutFieldInfoResponse.
        :type description: str
        """
        self._description = description

    @property
    def en_description(self):
        r"""Gets the en_description of this ShowLayoutFieldInfoResponse.

        字段英文描述

        :return: The en_description of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._en_description

    @en_description.setter
    def en_description(self, en_description):
        r"""Sets the en_description of this ShowLayoutFieldInfoResponse.

        字段英文描述

        :param en_description: The en_description of this ShowLayoutFieldInfoResponse.
        :type en_description: str
        """
        self._en_description = en_description

    @property
    def default_value(self):
        r"""Gets the default_value of this ShowLayoutFieldInfoResponse.

        默认值

        :return: The default_value of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this ShowLayoutFieldInfoResponse.

        默认值

        :param default_value: The default_value of this ShowLayoutFieldInfoResponse.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def en_default_value(self):
        r"""Gets the en_default_value of this ShowLayoutFieldInfoResponse.

        字段英文默认值

        :return: The en_default_value of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._en_default_value

    @en_default_value.setter
    def en_default_value(self, en_default_value):
        r"""Sets the en_default_value of this ShowLayoutFieldInfoResponse.

        字段英文默认值

        :param en_default_value: The en_default_value of this ShowLayoutFieldInfoResponse.
        :type en_default_value: str
        """
        self._en_default_value = en_default_value

    @property
    def field_type(self):
        r"""Gets the field_type of this ShowLayoutFieldInfoResponse.

        字段类型，如shorttext,radio,grid等

        :return: The field_type of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        r"""Sets the field_type of this ShowLayoutFieldInfoResponse.

        字段类型，如shorttext,radio,grid等

        :param field_type: The field_type of this ShowLayoutFieldInfoResponse.
        :type field_type: str
        """
        self._field_type = field_type

    @property
    def extra_json(self):
        r"""Gets the extra_json of this ShowLayoutFieldInfoResponse.

        附加json

        :return: The extra_json of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._extra_json

    @extra_json.setter
    def extra_json(self, extra_json):
        r"""Sets the extra_json of this ShowLayoutFieldInfoResponse.

        附加json

        :param extra_json: The extra_json of this ShowLayoutFieldInfoResponse.
        :type extra_json: str
        """
        self._extra_json = extra_json

    @property
    def field_tooltip(self):
        r"""Gets the field_tooltip of this ShowLayoutFieldInfoResponse.

        工具提示

        :return: The field_tooltip of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._field_tooltip

    @field_tooltip.setter
    def field_tooltip(self, field_tooltip):
        r"""Sets the field_tooltip of this ShowLayoutFieldInfoResponse.

        工具提示

        :param field_tooltip: The field_tooltip of this ShowLayoutFieldInfoResponse.
        :type field_tooltip: str
        """
        self._field_tooltip = field_tooltip

    @property
    def en_field_tooltip(self):
        r"""Gets the en_field_tooltip of this ShowLayoutFieldInfoResponse.

        英文工具提示

        :return: The en_field_tooltip of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._en_field_tooltip

    @en_field_tooltip.setter
    def en_field_tooltip(self, en_field_tooltip):
        r"""Sets the en_field_tooltip of this ShowLayoutFieldInfoResponse.

        英文工具提示

        :param en_field_tooltip: The en_field_tooltip of this ShowLayoutFieldInfoResponse.
        :type en_field_tooltip: str
        """
        self._en_field_tooltip = en_field_tooltip

    @property
    def json_schema(self):
        r"""Gets the json_schema of this ShowLayoutFieldInfoResponse.

        json模式

        :return: The json_schema of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._json_schema

    @json_schema.setter
    def json_schema(self, json_schema):
        r"""Sets the json_schema of this ShowLayoutFieldInfoResponse.

        json模式

        :param json_schema: The json_schema of this ShowLayoutFieldInfoResponse.
        :type json_schema: str
        """
        self._json_schema = json_schema

    @property
    def is_built_in(self):
        r"""Gets the is_built_in of this ShowLayoutFieldInfoResponse.

        是否内置，true内置，false非内置

        :return: The is_built_in of this ShowLayoutFieldInfoResponse.
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        r"""Sets the is_built_in of this ShowLayoutFieldInfoResponse.

        是否内置，true内置，false非内置

        :param is_built_in: The is_built_in of this ShowLayoutFieldInfoResponse.
        :type is_built_in: bool
        """
        self._is_built_in = is_built_in

    @property
    def read_only(self):
        r"""Gets the read_only of this ShowLayoutFieldInfoResponse.

        只读模式，true只读，false非只读

        :return: The read_only of this ShowLayoutFieldInfoResponse.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        r"""Sets the read_only of this ShowLayoutFieldInfoResponse.

        只读模式，true只读，false非只读

        :param read_only: The read_only of this ShowLayoutFieldInfoResponse.
        :type read_only: bool
        """
        self._read_only = read_only

    @property
    def required(self):
        r"""Gets the required of this ShowLayoutFieldInfoResponse.

        是否必填，true必填，false非必填

        :return: The required of this ShowLayoutFieldInfoResponse.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this ShowLayoutFieldInfoResponse.

        是否必填，true必填，false非必填

        :param required: The required of this ShowLayoutFieldInfoResponse.
        :type required: bool
        """
        self._required = required

    @property
    def searchable(self):
        r"""Gets the searchable of this ShowLayoutFieldInfoResponse.

        可搜索，true可搜索，false非可搜索

        :return: The searchable of this ShowLayoutFieldInfoResponse.
        :rtype: bool
        """
        return self._searchable

    @searchable.setter
    def searchable(self, searchable):
        r"""Sets the searchable of this ShowLayoutFieldInfoResponse.

        可搜索，true可搜索，false非可搜索

        :param searchable: The searchable of this ShowLayoutFieldInfoResponse.
        :type searchable: bool
        """
        self._searchable = searchable

    @property
    def visible(self):
        r"""Gets the visible of this ShowLayoutFieldInfoResponse.

        可见，true可见，false非可见

        :return: The visible of this ShowLayoutFieldInfoResponse.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        r"""Sets the visible of this ShowLayoutFieldInfoResponse.

        可见，true可见，false非可见

        :param visible: The visible of this ShowLayoutFieldInfoResponse.
        :type visible: bool
        """
        self._visible = visible

    @property
    def maintainable(self):
        r"""Gets the maintainable of this ShowLayoutFieldInfoResponse.

        可维护，true可维护，false非可维护

        :return: The maintainable of this ShowLayoutFieldInfoResponse.
        :rtype: bool
        """
        return self._maintainable

    @maintainable.setter
    def maintainable(self, maintainable):
        r"""Sets the maintainable of this ShowLayoutFieldInfoResponse.

        可维护，true可维护，false非可维护

        :param maintainable: The maintainable of this ShowLayoutFieldInfoResponse.
        :type maintainable: bool
        """
        self._maintainable = maintainable

    @property
    def editable(self):
        r"""Gets the editable of this ShowLayoutFieldInfoResponse.

        可编辑，true可编辑，false非可编辑

        :return: The editable of this ShowLayoutFieldInfoResponse.
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        r"""Sets the editable of this ShowLayoutFieldInfoResponse.

        可编辑，true可编辑，false非可编辑

        :param editable: The editable of this ShowLayoutFieldInfoResponse.
        :type editable: bool
        """
        self._editable = editable

    @property
    def creatable(self):
        r"""Gets the creatable of this ShowLayoutFieldInfoResponse.

        可创建，true可创建，false非可创建

        :return: The creatable of this ShowLayoutFieldInfoResponse.
        :rtype: bool
        """
        return self._creatable

    @creatable.setter
    def creatable(self, creatable):
        r"""Sets the creatable of this ShowLayoutFieldInfoResponse.

        可创建，true可创建，false非可创建

        :param creatable: The creatable of this ShowLayoutFieldInfoResponse.
        :type creatable: bool
        """
        self._creatable = creatable

    @property
    def creator_id(self):
        r"""Gets the creator_id of this ShowLayoutFieldInfoResponse.

        创建者ID

        :return: The creator_id of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this ShowLayoutFieldInfoResponse.

        创建者ID

        :param creator_id: The creator_id of this ShowLayoutFieldInfoResponse.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        r"""Gets the creator_name of this ShowLayoutFieldInfoResponse.

        创建者名称

        :return: The creator_name of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this ShowLayoutFieldInfoResponse.

        创建者名称

        :param creator_name: The creator_name of this ShowLayoutFieldInfoResponse.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def modifier_id(self):
        r"""Gets the modifier_id of this ShowLayoutFieldInfoResponse.

        修改者ID

        :return: The modifier_id of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, modifier_id):
        r"""Sets the modifier_id of this ShowLayoutFieldInfoResponse.

        修改者ID

        :param modifier_id: The modifier_id of this ShowLayoutFieldInfoResponse.
        :type modifier_id: str
        """
        self._modifier_id = modifier_id

    @property
    def modifier_name(self):
        r"""Gets the modifier_name of this ShowLayoutFieldInfoResponse.

        修改者名称

        :return: The modifier_name of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, modifier_name):
        r"""Sets the modifier_name of this ShowLayoutFieldInfoResponse.

        修改者名称

        :param modifier_name: The modifier_name of this ShowLayoutFieldInfoResponse.
        :type modifier_name: str
        """
        self._modifier_name = modifier_name

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowLayoutFieldInfoResponse.

        创建时间

        :return: The create_time of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowLayoutFieldInfoResponse.

        创建时间

        :param create_time: The create_time of this ShowLayoutFieldInfoResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowLayoutFieldInfoResponse.

        更新时间

        :return: The update_time of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowLayoutFieldInfoResponse.

        更新时间

        :param update_time: The update_time of this ShowLayoutFieldInfoResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def wizard_id(self):
        r"""Gets the wizard_id of this ShowLayoutFieldInfoResponse.

        字段绑定的页面id

        :return: The wizard_id of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._wizard_id

    @wizard_id.setter
    def wizard_id(self, wizard_id):
        r"""Sets the wizard_id of this ShowLayoutFieldInfoResponse.

        字段绑定的页面id

        :param wizard_id: The wizard_id of this ShowLayoutFieldInfoResponse.
        :type wizard_id: str
        """
        self._wizard_id = wizard_id

    @property
    def aopworkflow_id(self):
        r"""Gets the aopworkflow_id of this ShowLayoutFieldInfoResponse.

        字段绑定的流程id

        :return: The aopworkflow_id of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._aopworkflow_id

    @aopworkflow_id.setter
    def aopworkflow_id(self, aopworkflow_id):
        r"""Sets the aopworkflow_id of this ShowLayoutFieldInfoResponse.

        字段绑定的流程id

        :param aopworkflow_id: The aopworkflow_id of this ShowLayoutFieldInfoResponse.
        :type aopworkflow_id: str
        """
        self._aopworkflow_id = aopworkflow_id

    @property
    def aopworkflow_version_id(self):
        r"""Gets the aopworkflow_version_id of this ShowLayoutFieldInfoResponse.

        字段绑定的流程版本id

        :return: The aopworkflow_version_id of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._aopworkflow_version_id

    @aopworkflow_version_id.setter
    def aopworkflow_version_id(self, aopworkflow_version_id):
        r"""Sets the aopworkflow_version_id of this ShowLayoutFieldInfoResponse.

        字段绑定的流程版本id

        :param aopworkflow_version_id: The aopworkflow_version_id of this ShowLayoutFieldInfoResponse.
        :type aopworkflow_version_id: str
        """
        self._aopworkflow_version_id = aopworkflow_version_id

    @property
    def playbook_id(self):
        r"""Gets the playbook_id of this ShowLayoutFieldInfoResponse.

        字段绑定的剧本id

        :return: The playbook_id of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._playbook_id

    @playbook_id.setter
    def playbook_id(self, playbook_id):
        r"""Sets the playbook_id of this ShowLayoutFieldInfoResponse.

        字段绑定的剧本id

        :param playbook_id: The playbook_id of this ShowLayoutFieldInfoResponse.
        :type playbook_id: str
        """
        self._playbook_id = playbook_id

    @property
    def playbook_version_id(self):
        r"""Gets the playbook_version_id of this ShowLayoutFieldInfoResponse.

        字段绑定的剧本版本id

        :return: The playbook_version_id of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._playbook_version_id

    @playbook_version_id.setter
    def playbook_version_id(self, playbook_version_id):
        r"""Sets the playbook_version_id of this ShowLayoutFieldInfoResponse.

        字段绑定的剧本版本id

        :param playbook_version_id: The playbook_version_id of this ShowLayoutFieldInfoResponse.
        :type playbook_version_id: str
        """
        self._playbook_version_id = playbook_version_id

    @property
    def boa_version(self):
        r"""Gets the boa_version of this ShowLayoutFieldInfoResponse.

        BOA底座版本

        :return: The boa_version of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._boa_version

    @boa_version.setter
    def boa_version(self, boa_version):
        r"""Sets the boa_version of this ShowLayoutFieldInfoResponse.

        BOA底座版本

        :param boa_version: The boa_version of this ShowLayoutFieldInfoResponse.
        :type boa_version: str
        """
        self._boa_version = boa_version

    @property
    def version(self):
        r"""Gets the version of this ShowLayoutFieldInfoResponse.

        安全云脑版本

        :return: The version of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowLayoutFieldInfoResponse.

        安全云脑版本

        :param version: The version of this ShowLayoutFieldInfoResponse.
        :type version: str
        """
        self._version = version

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowLayoutFieldInfoResponse.

        :return: The x_request_id of this ShowLayoutFieldInfoResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowLayoutFieldInfoResponse.

        :param x_request_id: The x_request_id of this ShowLayoutFieldInfoResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowLayoutFieldInfoResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowLayoutFieldInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
