# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectFieldConfigVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'updator': 'NameAndIdVo',
        'description': 'str',
        'custom_name': 'str',
        'table_field_name': 'str',
        'value_type': 'str',
        'value_type_name': 'str',
        'is_system': 'int',
        'is_display': 'int',
        'is_required': 'int',
        'sort_numb': 'int',
        'default_value': 'str',
        'custom_field_uri': 'str',
        'resource_type': 'str',
        'creator': 'NameAndIdVo',
        'create_time_stamp': 'int',
        'update_time_stamp': 'int',
        'project_uuid': 'str',
        'option_vos': 'list[ProjectFieldConfigOptionVo]',
        'custom_field_id': 'int',
        'custom_field_name': 'str',
        'custom_field_param': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'updator': 'updator',
        'description': 'description',
        'custom_name': 'customName',
        'table_field_name': 'table_field_name',
        'value_type': 'value_type',
        'value_type_name': 'value_type_name',
        'is_system': 'is_system',
        'is_display': 'is_display',
        'is_required': 'is_required',
        'sort_numb': 'sort_numb',
        'default_value': 'default_value',
        'custom_field_uri': 'custom_field_uri',
        'resource_type': 'resource_type',
        'creator': 'creator',
        'create_time_stamp': 'create_time_stamp',
        'update_time_stamp': 'update_time_stamp',
        'project_uuid': 'project_uuid',
        'option_vos': 'option_vos',
        'custom_field_id': 'custom_field_id',
        'custom_field_name': 'custom_field_name',
        'custom_field_param': 'custom_field_param'
    }

    def __init__(self, uri=None, updator=None, description=None, custom_name=None, table_field_name=None, value_type=None, value_type_name=None, is_system=None, is_display=None, is_required=None, sort_numb=None, default_value=None, custom_field_uri=None, resource_type=None, creator=None, create_time_stamp=None, update_time_stamp=None, project_uuid=None, option_vos=None, custom_field_id=None, custom_field_name=None, custom_field_param=None):
        r"""ProjectFieldConfigVo

        The model defined in huaweicloud sdk

        :param uri: 字段配置URI标识
        :type uri: str
        :param updator: 
        :type updator: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        :param description: 描述
        :type description: str
        :param custom_name: 项目用例自定义字段名称
        :type custom_name: str
        :param table_field_name: 字段名（对应后端参数名）
        :type table_field_name: str
        :param value_type: 字段类型(单行文本text、多行文本textArea、单选框radio、多选框checkbox、日期date、数字number、用户user)。
        :type value_type: str
        :param value_type_name: 字段类型国际化名称
        :type value_type_name: str
        :param is_system: 是否系统字段
        :type is_system: int
        :param is_display: 是否显示
        :type is_display: int
        :param is_required: 是否必填
        :type is_required: int
        :param sort_numb: 顺序数值
        :type sort_numb: int
        :param default_value: 默认值
        :type default_value: str
        :param custom_field_uri: 扩展字段uri(用于连表查扩展字段)
        :type custom_field_uri: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param creator: 
        :type creator: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        :param create_time_stamp: 创建时间时间戳
        :type create_time_stamp: int
        :param update_time_stamp: 更新时间时间戳
        :type update_time_stamp: int
        :param project_uuid: 项目ID
        :type project_uuid: str
        :param option_vos: 可选项
        :type option_vos: list[:class:`huaweicloudsdkcloudtest.v1.ProjectFieldConfigOptionVo`]
        :param custom_field_id: 项目用例自定义字段id（1-25数字）
        :type custom_field_id: int
        :param custom_field_name: 项目用例自定义字段名称
        :type custom_field_name: str
        :param custom_field_param: 项目用例自定义字段入参或者返回参数名称
        :type custom_field_param: str
        """
        
        

        self._uri = None
        self._updator = None
        self._description = None
        self._custom_name = None
        self._table_field_name = None
        self._value_type = None
        self._value_type_name = None
        self._is_system = None
        self._is_display = None
        self._is_required = None
        self._sort_numb = None
        self._default_value = None
        self._custom_field_uri = None
        self._resource_type = None
        self._creator = None
        self._create_time_stamp = None
        self._update_time_stamp = None
        self._project_uuid = None
        self._option_vos = None
        self._custom_field_id = None
        self._custom_field_name = None
        self._custom_field_param = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if updator is not None:
            self.updator = updator
        if description is not None:
            self.description = description
        if custom_name is not None:
            self.custom_name = custom_name
        if table_field_name is not None:
            self.table_field_name = table_field_name
        if value_type is not None:
            self.value_type = value_type
        if value_type_name is not None:
            self.value_type_name = value_type_name
        if is_system is not None:
            self.is_system = is_system
        if is_display is not None:
            self.is_display = is_display
        if is_required is not None:
            self.is_required = is_required
        if sort_numb is not None:
            self.sort_numb = sort_numb
        if default_value is not None:
            self.default_value = default_value
        if custom_field_uri is not None:
            self.custom_field_uri = custom_field_uri
        if resource_type is not None:
            self.resource_type = resource_type
        if creator is not None:
            self.creator = creator
        if create_time_stamp is not None:
            self.create_time_stamp = create_time_stamp
        if update_time_stamp is not None:
            self.update_time_stamp = update_time_stamp
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if option_vos is not None:
            self.option_vos = option_vos
        if custom_field_id is not None:
            self.custom_field_id = custom_field_id
        if custom_field_name is not None:
            self.custom_field_name = custom_field_name
        if custom_field_param is not None:
            self.custom_field_param = custom_field_param

    @property
    def uri(self):
        r"""Gets the uri of this ProjectFieldConfigVo.

        字段配置URI标识

        :return: The uri of this ProjectFieldConfigVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this ProjectFieldConfigVo.

        字段配置URI标识

        :param uri: The uri of this ProjectFieldConfigVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def updator(self):
        r"""Gets the updator of this ProjectFieldConfigVo.

        :return: The updator of this ProjectFieldConfigVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._updator

    @updator.setter
    def updator(self, updator):
        r"""Sets the updator of this ProjectFieldConfigVo.

        :param updator: The updator of this ProjectFieldConfigVo.
        :type updator: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._updator = updator

    @property
    def description(self):
        r"""Gets the description of this ProjectFieldConfigVo.

        描述

        :return: The description of this ProjectFieldConfigVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ProjectFieldConfigVo.

        描述

        :param description: The description of this ProjectFieldConfigVo.
        :type description: str
        """
        self._description = description

    @property
    def custom_name(self):
        r"""Gets the custom_name of this ProjectFieldConfigVo.

        项目用例自定义字段名称

        :return: The custom_name of this ProjectFieldConfigVo.
        :rtype: str
        """
        return self._custom_name

    @custom_name.setter
    def custom_name(self, custom_name):
        r"""Sets the custom_name of this ProjectFieldConfigVo.

        项目用例自定义字段名称

        :param custom_name: The custom_name of this ProjectFieldConfigVo.
        :type custom_name: str
        """
        self._custom_name = custom_name

    @property
    def table_field_name(self):
        r"""Gets the table_field_name of this ProjectFieldConfigVo.

        字段名（对应后端参数名）

        :return: The table_field_name of this ProjectFieldConfigVo.
        :rtype: str
        """
        return self._table_field_name

    @table_field_name.setter
    def table_field_name(self, table_field_name):
        r"""Sets the table_field_name of this ProjectFieldConfigVo.

        字段名（对应后端参数名）

        :param table_field_name: The table_field_name of this ProjectFieldConfigVo.
        :type table_field_name: str
        """
        self._table_field_name = table_field_name

    @property
    def value_type(self):
        r"""Gets the value_type of this ProjectFieldConfigVo.

        字段类型(单行文本text、多行文本textArea、单选框radio、多选框checkbox、日期date、数字number、用户user)。

        :return: The value_type of this ProjectFieldConfigVo.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        r"""Sets the value_type of this ProjectFieldConfigVo.

        字段类型(单行文本text、多行文本textArea、单选框radio、多选框checkbox、日期date、数字number、用户user)。

        :param value_type: The value_type of this ProjectFieldConfigVo.
        :type value_type: str
        """
        self._value_type = value_type

    @property
    def value_type_name(self):
        r"""Gets the value_type_name of this ProjectFieldConfigVo.

        字段类型国际化名称

        :return: The value_type_name of this ProjectFieldConfigVo.
        :rtype: str
        """
        return self._value_type_name

    @value_type_name.setter
    def value_type_name(self, value_type_name):
        r"""Sets the value_type_name of this ProjectFieldConfigVo.

        字段类型国际化名称

        :param value_type_name: The value_type_name of this ProjectFieldConfigVo.
        :type value_type_name: str
        """
        self._value_type_name = value_type_name

    @property
    def is_system(self):
        r"""Gets the is_system of this ProjectFieldConfigVo.

        是否系统字段

        :return: The is_system of this ProjectFieldConfigVo.
        :rtype: int
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        r"""Sets the is_system of this ProjectFieldConfigVo.

        是否系统字段

        :param is_system: The is_system of this ProjectFieldConfigVo.
        :type is_system: int
        """
        self._is_system = is_system

    @property
    def is_display(self):
        r"""Gets the is_display of this ProjectFieldConfigVo.

        是否显示

        :return: The is_display of this ProjectFieldConfigVo.
        :rtype: int
        """
        return self._is_display

    @is_display.setter
    def is_display(self, is_display):
        r"""Sets the is_display of this ProjectFieldConfigVo.

        是否显示

        :param is_display: The is_display of this ProjectFieldConfigVo.
        :type is_display: int
        """
        self._is_display = is_display

    @property
    def is_required(self):
        r"""Gets the is_required of this ProjectFieldConfigVo.

        是否必填

        :return: The is_required of this ProjectFieldConfigVo.
        :rtype: int
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        r"""Sets the is_required of this ProjectFieldConfigVo.

        是否必填

        :param is_required: The is_required of this ProjectFieldConfigVo.
        :type is_required: int
        """
        self._is_required = is_required

    @property
    def sort_numb(self):
        r"""Gets the sort_numb of this ProjectFieldConfigVo.

        顺序数值

        :return: The sort_numb of this ProjectFieldConfigVo.
        :rtype: int
        """
        return self._sort_numb

    @sort_numb.setter
    def sort_numb(self, sort_numb):
        r"""Sets the sort_numb of this ProjectFieldConfigVo.

        顺序数值

        :param sort_numb: The sort_numb of this ProjectFieldConfigVo.
        :type sort_numb: int
        """
        self._sort_numb = sort_numb

    @property
    def default_value(self):
        r"""Gets the default_value of this ProjectFieldConfigVo.

        默认值

        :return: The default_value of this ProjectFieldConfigVo.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this ProjectFieldConfigVo.

        默认值

        :param default_value: The default_value of this ProjectFieldConfigVo.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def custom_field_uri(self):
        r"""Gets the custom_field_uri of this ProjectFieldConfigVo.

        扩展字段uri(用于连表查扩展字段)

        :return: The custom_field_uri of this ProjectFieldConfigVo.
        :rtype: str
        """
        return self._custom_field_uri

    @custom_field_uri.setter
    def custom_field_uri(self, custom_field_uri):
        r"""Sets the custom_field_uri of this ProjectFieldConfigVo.

        扩展字段uri(用于连表查扩展字段)

        :param custom_field_uri: The custom_field_uri of this ProjectFieldConfigVo.
        :type custom_field_uri: str
        """
        self._custom_field_uri = custom_field_uri

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ProjectFieldConfigVo.

        资源类型

        :return: The resource_type of this ProjectFieldConfigVo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ProjectFieldConfigVo.

        资源类型

        :param resource_type: The resource_type of this ProjectFieldConfigVo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def creator(self):
        r"""Gets the creator of this ProjectFieldConfigVo.

        :return: The creator of this ProjectFieldConfigVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ProjectFieldConfigVo.

        :param creator: The creator of this ProjectFieldConfigVo.
        :type creator: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._creator = creator

    @property
    def create_time_stamp(self):
        r"""Gets the create_time_stamp of this ProjectFieldConfigVo.

        创建时间时间戳

        :return: The create_time_stamp of this ProjectFieldConfigVo.
        :rtype: int
        """
        return self._create_time_stamp

    @create_time_stamp.setter
    def create_time_stamp(self, create_time_stamp):
        r"""Sets the create_time_stamp of this ProjectFieldConfigVo.

        创建时间时间戳

        :param create_time_stamp: The create_time_stamp of this ProjectFieldConfigVo.
        :type create_time_stamp: int
        """
        self._create_time_stamp = create_time_stamp

    @property
    def update_time_stamp(self):
        r"""Gets the update_time_stamp of this ProjectFieldConfigVo.

        更新时间时间戳

        :return: The update_time_stamp of this ProjectFieldConfigVo.
        :rtype: int
        """
        return self._update_time_stamp

    @update_time_stamp.setter
    def update_time_stamp(self, update_time_stamp):
        r"""Sets the update_time_stamp of this ProjectFieldConfigVo.

        更新时间时间戳

        :param update_time_stamp: The update_time_stamp of this ProjectFieldConfigVo.
        :type update_time_stamp: int
        """
        self._update_time_stamp = update_time_stamp

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this ProjectFieldConfigVo.

        项目ID

        :return: The project_uuid of this ProjectFieldConfigVo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this ProjectFieldConfigVo.

        项目ID

        :param project_uuid: The project_uuid of this ProjectFieldConfigVo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def option_vos(self):
        r"""Gets the option_vos of this ProjectFieldConfigVo.

        可选项

        :return: The option_vos of this ProjectFieldConfigVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.ProjectFieldConfigOptionVo`]
        """
        return self._option_vos

    @option_vos.setter
    def option_vos(self, option_vos):
        r"""Sets the option_vos of this ProjectFieldConfigVo.

        可选项

        :param option_vos: The option_vos of this ProjectFieldConfigVo.
        :type option_vos: list[:class:`huaweicloudsdkcloudtest.v1.ProjectFieldConfigOptionVo`]
        """
        self._option_vos = option_vos

    @property
    def custom_field_id(self):
        r"""Gets the custom_field_id of this ProjectFieldConfigVo.

        项目用例自定义字段id（1-25数字）

        :return: The custom_field_id of this ProjectFieldConfigVo.
        :rtype: int
        """
        return self._custom_field_id

    @custom_field_id.setter
    def custom_field_id(self, custom_field_id):
        r"""Sets the custom_field_id of this ProjectFieldConfigVo.

        项目用例自定义字段id（1-25数字）

        :param custom_field_id: The custom_field_id of this ProjectFieldConfigVo.
        :type custom_field_id: int
        """
        self._custom_field_id = custom_field_id

    @property
    def custom_field_name(self):
        r"""Gets the custom_field_name of this ProjectFieldConfigVo.

        项目用例自定义字段名称

        :return: The custom_field_name of this ProjectFieldConfigVo.
        :rtype: str
        """
        return self._custom_field_name

    @custom_field_name.setter
    def custom_field_name(self, custom_field_name):
        r"""Sets the custom_field_name of this ProjectFieldConfigVo.

        项目用例自定义字段名称

        :param custom_field_name: The custom_field_name of this ProjectFieldConfigVo.
        :type custom_field_name: str
        """
        self._custom_field_name = custom_field_name

    @property
    def custom_field_param(self):
        r"""Gets the custom_field_param of this ProjectFieldConfigVo.

        项目用例自定义字段入参或者返回参数名称

        :return: The custom_field_param of this ProjectFieldConfigVo.
        :rtype: str
        """
        return self._custom_field_param

    @custom_field_param.setter
    def custom_field_param(self, custom_field_param):
        r"""Sets the custom_field_param of this ProjectFieldConfigVo.

        项目用例自定义字段入参或者返回参数名称

        :param custom_field_param: The custom_field_param of this ProjectFieldConfigVo.
        :type custom_field_param: str
        """
        self._custom_field_param = custom_field_param

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
        if not isinstance(other, ProjectFieldConfigVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
