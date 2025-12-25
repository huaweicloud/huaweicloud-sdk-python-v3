# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLayoutFieldRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'layout_id': 'str',
        'wizard_id': 'str',
        'aopworkflow_id': 'str',
        'aopworkflow_version_id': 'str',
        'playbook_id': 'str',
        'playbook_version_id': 'str',
        'default_value': 'str',
        'display_type': 'str',
        'field_type': 'str',
        'extra_json': 'str',
        'field_tooltip': 'str',
        'json_schema': 'str',
        'readonly': 'bool',
        'required': 'bool',
        'searchable': 'bool',
        'visible': 'bool',
        'maintainable': 'bool',
        'editable': 'bool',
        'creatable': 'bool',
        'boa_version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'layout_id': 'layout_id',
        'wizard_id': 'wizard_id',
        'aopworkflow_id': 'aopworkflow_id',
        'aopworkflow_version_id': 'aopworkflow_version_id',
        'playbook_id': 'playbook_id',
        'playbook_version_id': 'playbook_version_id',
        'default_value': 'default_value',
        'display_type': 'display_type',
        'field_type': 'field_type',
        'extra_json': 'extra_json',
        'field_tooltip': 'field_tooltip',
        'json_schema': 'json_schema',
        'readonly': 'readonly',
        'required': 'required',
        'searchable': 'searchable',
        'visible': 'visible',
        'maintainable': 'maintainable',
        'editable': 'editable',
        'creatable': 'creatable',
        'boa_version': 'boa_version'
    }

    def __init__(self, name=None, description=None, layout_id=None, wizard_id=None, aopworkflow_id=None, aopworkflow_version_id=None, playbook_id=None, playbook_version_id=None, default_value=None, display_type=None, field_type=None, extra_json=None, field_tooltip=None, json_schema=None, readonly=None, required=None, searchable=None, visible=None, maintainable=None, editable=None, creatable=None, boa_version=None):
        r"""UpdateLayoutFieldRequestBody

        The model defined in huaweicloud sdk

        :param name: 字段名称
        :type name: str
        :param description: 字段描述
        :type description: str
        :param layout_id: 布局ID
        :type layout_id: str
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
        :param json_schema: json模式
        :type json_schema: str
        :param readonly: 只读模式，true只读，false非只读
        :type readonly: bool
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
        :param boa_version: BOA底座版本
        :type boa_version: str
        """
        
        

        self._name = None
        self._description = None
        self._layout_id = None
        self._wizard_id = None
        self._aopworkflow_id = None
        self._aopworkflow_version_id = None
        self._playbook_id = None
        self._playbook_version_id = None
        self._default_value = None
        self._display_type = None
        self._field_type = None
        self._extra_json = None
        self._field_tooltip = None
        self._json_schema = None
        self._readonly = None
        self._required = None
        self._searchable = None
        self._visible = None
        self._maintainable = None
        self._editable = None
        self._creatable = None
        self._boa_version = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if layout_id is not None:
            self.layout_id = layout_id
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
        if json_schema is not None:
            self.json_schema = json_schema
        if readonly is not None:
            self.readonly = readonly
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
        if boa_version is not None:
            self.boa_version = boa_version

    @property
    def name(self):
        r"""Gets the name of this UpdateLayoutFieldRequestBody.

        字段名称

        :return: The name of this UpdateLayoutFieldRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateLayoutFieldRequestBody.

        字段名称

        :param name: The name of this UpdateLayoutFieldRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateLayoutFieldRequestBody.

        字段描述

        :return: The description of this UpdateLayoutFieldRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateLayoutFieldRequestBody.

        字段描述

        :param description: The description of this UpdateLayoutFieldRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def layout_id(self):
        r"""Gets the layout_id of this UpdateLayoutFieldRequestBody.

        布局ID

        :return: The layout_id of this UpdateLayoutFieldRequestBody.
        :rtype: str
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        r"""Sets the layout_id of this UpdateLayoutFieldRequestBody.

        布局ID

        :param layout_id: The layout_id of this UpdateLayoutFieldRequestBody.
        :type layout_id: str
        """
        self._layout_id = layout_id

    @property
    def wizard_id(self):
        r"""Gets the wizard_id of this UpdateLayoutFieldRequestBody.

        字段绑定的页面id

        :return: The wizard_id of this UpdateLayoutFieldRequestBody.
        :rtype: str
        """
        return self._wizard_id

    @wizard_id.setter
    def wizard_id(self, wizard_id):
        r"""Sets the wizard_id of this UpdateLayoutFieldRequestBody.

        字段绑定的页面id

        :param wizard_id: The wizard_id of this UpdateLayoutFieldRequestBody.
        :type wizard_id: str
        """
        self._wizard_id = wizard_id

    @property
    def aopworkflow_id(self):
        r"""Gets the aopworkflow_id of this UpdateLayoutFieldRequestBody.

        字段绑定的流程id

        :return: The aopworkflow_id of this UpdateLayoutFieldRequestBody.
        :rtype: str
        """
        return self._aopworkflow_id

    @aopworkflow_id.setter
    def aopworkflow_id(self, aopworkflow_id):
        r"""Sets the aopworkflow_id of this UpdateLayoutFieldRequestBody.

        字段绑定的流程id

        :param aopworkflow_id: The aopworkflow_id of this UpdateLayoutFieldRequestBody.
        :type aopworkflow_id: str
        """
        self._aopworkflow_id = aopworkflow_id

    @property
    def aopworkflow_version_id(self):
        r"""Gets the aopworkflow_version_id of this UpdateLayoutFieldRequestBody.

        字段绑定的流程版本id

        :return: The aopworkflow_version_id of this UpdateLayoutFieldRequestBody.
        :rtype: str
        """
        return self._aopworkflow_version_id

    @aopworkflow_version_id.setter
    def aopworkflow_version_id(self, aopworkflow_version_id):
        r"""Sets the aopworkflow_version_id of this UpdateLayoutFieldRequestBody.

        字段绑定的流程版本id

        :param aopworkflow_version_id: The aopworkflow_version_id of this UpdateLayoutFieldRequestBody.
        :type aopworkflow_version_id: str
        """
        self._aopworkflow_version_id = aopworkflow_version_id

    @property
    def playbook_id(self):
        r"""Gets the playbook_id of this UpdateLayoutFieldRequestBody.

        字段绑定的剧本id

        :return: The playbook_id of this UpdateLayoutFieldRequestBody.
        :rtype: str
        """
        return self._playbook_id

    @playbook_id.setter
    def playbook_id(self, playbook_id):
        r"""Sets the playbook_id of this UpdateLayoutFieldRequestBody.

        字段绑定的剧本id

        :param playbook_id: The playbook_id of this UpdateLayoutFieldRequestBody.
        :type playbook_id: str
        """
        self._playbook_id = playbook_id

    @property
    def playbook_version_id(self):
        r"""Gets the playbook_version_id of this UpdateLayoutFieldRequestBody.

        字段绑定的剧本版本id

        :return: The playbook_version_id of this UpdateLayoutFieldRequestBody.
        :rtype: str
        """
        return self._playbook_version_id

    @playbook_version_id.setter
    def playbook_version_id(self, playbook_version_id):
        r"""Sets the playbook_version_id of this UpdateLayoutFieldRequestBody.

        字段绑定的剧本版本id

        :param playbook_version_id: The playbook_version_id of this UpdateLayoutFieldRequestBody.
        :type playbook_version_id: str
        """
        self._playbook_version_id = playbook_version_id

    @property
    def default_value(self):
        r"""Gets the default_value of this UpdateLayoutFieldRequestBody.

        默认值

        :return: The default_value of this UpdateLayoutFieldRequestBody.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this UpdateLayoutFieldRequestBody.

        默认值

        :param default_value: The default_value of this UpdateLayoutFieldRequestBody.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def display_type(self):
        r"""Gets the display_type of this UpdateLayoutFieldRequestBody.

        显示类型

        :return: The display_type of this UpdateLayoutFieldRequestBody.
        :rtype: str
        """
        return self._display_type

    @display_type.setter
    def display_type(self, display_type):
        r"""Sets the display_type of this UpdateLayoutFieldRequestBody.

        显示类型

        :param display_type: The display_type of this UpdateLayoutFieldRequestBody.
        :type display_type: str
        """
        self._display_type = display_type

    @property
    def field_type(self):
        r"""Gets the field_type of this UpdateLayoutFieldRequestBody.

        字段类型，如shorttext,radio,grid等

        :return: The field_type of this UpdateLayoutFieldRequestBody.
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        r"""Sets the field_type of this UpdateLayoutFieldRequestBody.

        字段类型，如shorttext,radio,grid等

        :param field_type: The field_type of this UpdateLayoutFieldRequestBody.
        :type field_type: str
        """
        self._field_type = field_type

    @property
    def extra_json(self):
        r"""Gets the extra_json of this UpdateLayoutFieldRequestBody.

        附加json

        :return: The extra_json of this UpdateLayoutFieldRequestBody.
        :rtype: str
        """
        return self._extra_json

    @extra_json.setter
    def extra_json(self, extra_json):
        r"""Sets the extra_json of this UpdateLayoutFieldRequestBody.

        附加json

        :param extra_json: The extra_json of this UpdateLayoutFieldRequestBody.
        :type extra_json: str
        """
        self._extra_json = extra_json

    @property
    def field_tooltip(self):
        r"""Gets the field_tooltip of this UpdateLayoutFieldRequestBody.

        工具提示

        :return: The field_tooltip of this UpdateLayoutFieldRequestBody.
        :rtype: str
        """
        return self._field_tooltip

    @field_tooltip.setter
    def field_tooltip(self, field_tooltip):
        r"""Sets the field_tooltip of this UpdateLayoutFieldRequestBody.

        工具提示

        :param field_tooltip: The field_tooltip of this UpdateLayoutFieldRequestBody.
        :type field_tooltip: str
        """
        self._field_tooltip = field_tooltip

    @property
    def json_schema(self):
        r"""Gets the json_schema of this UpdateLayoutFieldRequestBody.

        json模式

        :return: The json_schema of this UpdateLayoutFieldRequestBody.
        :rtype: str
        """
        return self._json_schema

    @json_schema.setter
    def json_schema(self, json_schema):
        r"""Sets the json_schema of this UpdateLayoutFieldRequestBody.

        json模式

        :param json_schema: The json_schema of this UpdateLayoutFieldRequestBody.
        :type json_schema: str
        """
        self._json_schema = json_schema

    @property
    def readonly(self):
        r"""Gets the readonly of this UpdateLayoutFieldRequestBody.

        只读模式，true只读，false非只读

        :return: The readonly of this UpdateLayoutFieldRequestBody.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        r"""Sets the readonly of this UpdateLayoutFieldRequestBody.

        只读模式，true只读，false非只读

        :param readonly: The readonly of this UpdateLayoutFieldRequestBody.
        :type readonly: bool
        """
        self._readonly = readonly

    @property
    def required(self):
        r"""Gets the required of this UpdateLayoutFieldRequestBody.

        是否必填，true必填，false非必填

        :return: The required of this UpdateLayoutFieldRequestBody.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this UpdateLayoutFieldRequestBody.

        是否必填，true必填，false非必填

        :param required: The required of this UpdateLayoutFieldRequestBody.
        :type required: bool
        """
        self._required = required

    @property
    def searchable(self):
        r"""Gets the searchable of this UpdateLayoutFieldRequestBody.

        可搜索，true可搜索，false非可搜索

        :return: The searchable of this UpdateLayoutFieldRequestBody.
        :rtype: bool
        """
        return self._searchable

    @searchable.setter
    def searchable(self, searchable):
        r"""Sets the searchable of this UpdateLayoutFieldRequestBody.

        可搜索，true可搜索，false非可搜索

        :param searchable: The searchable of this UpdateLayoutFieldRequestBody.
        :type searchable: bool
        """
        self._searchable = searchable

    @property
    def visible(self):
        r"""Gets the visible of this UpdateLayoutFieldRequestBody.

        可见，true可见，false非可见

        :return: The visible of this UpdateLayoutFieldRequestBody.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        r"""Sets the visible of this UpdateLayoutFieldRequestBody.

        可见，true可见，false非可见

        :param visible: The visible of this UpdateLayoutFieldRequestBody.
        :type visible: bool
        """
        self._visible = visible

    @property
    def maintainable(self):
        r"""Gets the maintainable of this UpdateLayoutFieldRequestBody.

        可维护，true可维护，false非可维护

        :return: The maintainable of this UpdateLayoutFieldRequestBody.
        :rtype: bool
        """
        return self._maintainable

    @maintainable.setter
    def maintainable(self, maintainable):
        r"""Sets the maintainable of this UpdateLayoutFieldRequestBody.

        可维护，true可维护，false非可维护

        :param maintainable: The maintainable of this UpdateLayoutFieldRequestBody.
        :type maintainable: bool
        """
        self._maintainable = maintainable

    @property
    def editable(self):
        r"""Gets the editable of this UpdateLayoutFieldRequestBody.

        可编辑，true可编辑，false非可编辑

        :return: The editable of this UpdateLayoutFieldRequestBody.
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        r"""Sets the editable of this UpdateLayoutFieldRequestBody.

        可编辑，true可编辑，false非可编辑

        :param editable: The editable of this UpdateLayoutFieldRequestBody.
        :type editable: bool
        """
        self._editable = editable

    @property
    def creatable(self):
        r"""Gets the creatable of this UpdateLayoutFieldRequestBody.

        可创建，true可创建，false非可创建

        :return: The creatable of this UpdateLayoutFieldRequestBody.
        :rtype: bool
        """
        return self._creatable

    @creatable.setter
    def creatable(self, creatable):
        r"""Sets the creatable of this UpdateLayoutFieldRequestBody.

        可创建，true可创建，false非可创建

        :param creatable: The creatable of this UpdateLayoutFieldRequestBody.
        :type creatable: bool
        """
        self._creatable = creatable

    @property
    def boa_version(self):
        r"""Gets the boa_version of this UpdateLayoutFieldRequestBody.

        BOA底座版本

        :return: The boa_version of this UpdateLayoutFieldRequestBody.
        :rtype: str
        """
        return self._boa_version

    @boa_version.setter
    def boa_version(self, boa_version):
        r"""Sets the boa_version of this UpdateLayoutFieldRequestBody.

        BOA底座版本

        :param boa_version: The boa_version of this UpdateLayoutFieldRequestBody.
        :type boa_version: str
        """
        self._boa_version = boa_version

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
        if not isinstance(other, UpdateLayoutFieldRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
