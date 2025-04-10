# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AwInstanceRes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alias_runaw': 'str',
        'authentication_info': 'AuthInfo',
        'authentication_type': 'str',
        'aw_description': 'str',
        'aw_id': 'str',
        'aw_type': 'int',
        'basic_aw': 'BasicAwRes',
        'body_param_type': 'str',
        'by_order': 'int',
        'change_sign': 'int',
        'check_point_list': 'list[CheckPoint]',
        'children': 'list[AwInstanceRes]',
        'condition_statement': 'str',
        'condition_type': 'int',
        'create_time': 'str',
        'create_time_stamp': 'int',
        'create_time_string': 'str',
        'create_user': 'str',
        'custom_header': 'list[AwParam]',
        'description': 'str',
        'error_info': 'ErrorInfo',
        'extra_info': 'ExtraInfo',
        'from_outside': 'int',
        'has_level': 'int',
        'header_array': 'list[ArrayNode]',
        'his_script': 'str',
        'id': 'str',
        'is_basic': 'int',
        'is_contract_aw': 'int',
        'is_disabled': 'int',
        'is_sectest_aw': 'int',
        'level': 'int',
        'name': 'str',
        'param_dependent': 'str',
        'param_dependent_enabled': 'int',
        'param_type_and_value': 'list[AwParam]',
        'project_id': 'str',
        'region': 'str',
        'relation': 'str',
        'relation_id': 'str',
        'relation_type': 'int',
        'retry_interval': 'str',
        'retry_times': 'str',
        'script_name': 'str',
        'service_and_stage': 'str',
        'special_type': 'int',
        'update_time': 'str',
        'update_time_stamp': 'int',
        'update_time_string': 'str',
        'update_user': 'str',
        'user_id': 'str',
        'variable_list': 'list[AwVariable]'
    }

    attribute_map = {
        'alias_runaw': 'alias_runaw',
        'authentication_info': 'authentication_info',
        'authentication_type': 'authentication_type',
        'aw_description': 'aw_description',
        'aw_id': 'aw_id',
        'aw_type': 'aw_type',
        'basic_aw': 'basic_aw',
        'body_param_type': 'body_param_type',
        'by_order': 'by_order',
        'change_sign': 'changeSign',
        'check_point_list': 'check_point_list',
        'children': 'children',
        'condition_statement': 'condition_statement',
        'condition_type': 'condition_type',
        'create_time': 'create_time',
        'create_time_stamp': 'create_time_stamp',
        'create_time_string': 'create_time_string',
        'create_user': 'create_user',
        'custom_header': 'custom_header',
        'description': 'description',
        'error_info': 'error_info',
        'extra_info': 'extra_info',
        'from_outside': 'from_outside',
        'has_level': 'hasLevel',
        'header_array': 'header_array',
        'his_script': 'his_script',
        'id': 'id',
        'is_basic': 'is_basic',
        'is_contract_aw': 'is_contract_aw',
        'is_disabled': 'is_disabled',
        'is_sectest_aw': 'is_sectest_aw',
        'level': 'level',
        'name': 'name',
        'param_dependent': 'param_dependent',
        'param_dependent_enabled': 'param_dependent_enabled',
        'param_type_and_value': 'param_type_and_value',
        'project_id': 'projectId',
        'region': 'region',
        'relation': 'relation',
        'relation_id': 'relation_id',
        'relation_type': 'relation_type',
        'retry_interval': 'retry_interval',
        'retry_times': 'retry_times',
        'script_name': 'scriptName',
        'service_and_stage': 'service_and_stage',
        'special_type': 'special_type',
        'update_time': 'update_time',
        'update_time_stamp': 'update_time_stamp',
        'update_time_string': 'update_time_string',
        'update_user': 'update_user',
        'user_id': 'user_id',
        'variable_list': 'variable_list'
    }

    def __init__(self, alias_runaw=None, authentication_info=None, authentication_type=None, aw_description=None, aw_id=None, aw_type=None, basic_aw=None, body_param_type=None, by_order=None, change_sign=None, check_point_list=None, children=None, condition_statement=None, condition_type=None, create_time=None, create_time_stamp=None, create_time_string=None, create_user=None, custom_header=None, description=None, error_info=None, extra_info=None, from_outside=None, has_level=None, header_array=None, his_script=None, id=None, is_basic=None, is_contract_aw=None, is_disabled=None, is_sectest_aw=None, level=None, name=None, param_dependent=None, param_dependent_enabled=None, param_type_and_value=None, project_id=None, region=None, relation=None, relation_id=None, relation_type=None, retry_interval=None, retry_times=None, script_name=None, service_and_stage=None, special_type=None, update_time=None, update_time_stamp=None, update_time_string=None, update_user=None, user_id=None, variable_list=None):
        r"""AwInstanceRes

        The model defined in huaweicloud sdk

        :param alias_runaw: AW内容描述字段
        :type alias_runaw: str
        :param authentication_info: 
        :type authentication_info: :class:`huaweicloudsdkcloudtest.v1.AuthInfo`
        :param authentication_type: 认证类型,0-无认证;1-aksk认证
        :type authentication_type: str
        :param aw_description: 脚本模板描述信息，在用例更新时添加
        :type aw_description: str
        :param aw_id: aw id
        :type aw_id: str
        :param aw_type: aw类型 0-setup;1-test;2-teardown
        :type aw_type: int
        :param basic_aw: 
        :type basic_aw: :class:`huaweicloudsdkcloudtest.v1.BasicAwRes`
        :param body_param_type: instance的参数body体类型：form/text
        :type body_param_type: str
        :param by_order: 顺序
        :type by_order: int
        :param change_sign: change sign
        :type change_sign: int
        :param check_point_list: 检查点List
        :type check_point_list: list[:class:`huaweicloudsdkcloudtest.v1.CheckPoint`]
        :param children: aw实例
        :type children: list[:class:`huaweicloudsdkcloudtest.v1.AwInstanceRes`]
        :param condition_statement: 条件语句
        :type condition_statement: str
        :param condition_type: 条件类型 0-not condition;1-if begin;2-if
        :type condition_type: int
        :param create_time: 创建时间
        :type create_time: str
        :param create_time_stamp: 创建时间戳
        :type create_time_stamp: int
        :param create_time_string: 创建时间字符串
        :type create_time_string: str
        :param create_user: 创建人
        :type create_user: str
        :param custom_header: 测试步骤自定义请求头List；后续自定义URL请求头不再使用该字段
        :type custom_header: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        :param description: 描述
        :type description: str
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkcloudtest.v1.ErrorInfo`
        :param extra_info: 
        :type extra_info: :class:`huaweicloudsdkcloudtest.v1.ExtraInfo`
        :param from_outside: 该aw是否来自外部工程 0-no;1-yes
        :type from_outside: int
        :param has_level: level
        :type has_level: int
        :param header_array: 
        :type header_array: list[:class:`huaweicloudsdkcloudtest.v1.ArrayNode`]
        :param his_script: 值不为null表示老的IF判断语句；值为null表示新的IF判断语句
        :type his_script: str
        :param id: id
        :type id: str
        :param is_basic: 是否模板类型测试步骤 0：自定义URL配置类型；1：模板类型测试步骤
        :type is_basic: int
        :param is_contract_aw: 是否是契约AW 0-否；1-yes
        :type is_contract_aw: int
        :param is_disabled: 是否被禁用 0-否；1-yes
        :type is_disabled: int
        :param is_sectest_aw: 是否是安全测试aw
        :type is_sectest_aw: int
        :param level: 用例级别
        :type level: int
        :param name: 名称
        :type name: str
        :param param_dependent: 参数依赖规则
        :type param_dependent: str
        :param param_dependent_enabled: 是否启用参数依赖
        :type param_dependent_enabled: int
        :param param_type_and_value: 参数类型和参数值对应List
        :type param_type_and_value: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        :param project_id: awinstance所在的用例\\逻辑用例\\组合aw所属项目,该字段是新增字段,因此部分awinstance是无值的,所以只可写该值,而不能读取该值
        :type project_id: str
        :param region: 区域名称
        :type region: str
        :param relation: awId层级关系
        :type relation: str
        :param relation_id: relation id
        :type relation_id: str
        :param relation_type: 映射类型 1-反向删除映射;2-用例自动添加的方向删除步骤
        :type relation_type: int
        :param retry_interval: 重试间隔时间 (ms) 为空表示不等待
        :type retry_interval: str
        :param retry_times: 重试次数
        :type retry_times: str
        :param script_name: 获取脚本生成时，要使用的步骤名称
        :type script_name: str
        :param service_and_stage: aw所来自工程的服务名和阶段名 fromOutside为1时该值有效
        :type service_and_stage: str
        :param special_type: 测试步骤来源
        :type special_type: int
        :param update_time: 更新时间
        :type update_time: str
        :param update_time_stamp: 更新时间戳
        :type update_time_stamp: int
        :param update_time_string: 更新时间字符串
        :type update_time_string: str
        :param update_user: 更新人
        :type update_user: str
        :param user_id: user id
        :type user_id: str
        :param variable_list: 定义的变量信息
        :type variable_list: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        """
        
        

        self._alias_runaw = None
        self._authentication_info = None
        self._authentication_type = None
        self._aw_description = None
        self._aw_id = None
        self._aw_type = None
        self._basic_aw = None
        self._body_param_type = None
        self._by_order = None
        self._change_sign = None
        self._check_point_list = None
        self._children = None
        self._condition_statement = None
        self._condition_type = None
        self._create_time = None
        self._create_time_stamp = None
        self._create_time_string = None
        self._create_user = None
        self._custom_header = None
        self._description = None
        self._error_info = None
        self._extra_info = None
        self._from_outside = None
        self._has_level = None
        self._header_array = None
        self._his_script = None
        self._id = None
        self._is_basic = None
        self._is_contract_aw = None
        self._is_disabled = None
        self._is_sectest_aw = None
        self._level = None
        self._name = None
        self._param_dependent = None
        self._param_dependent_enabled = None
        self._param_type_and_value = None
        self._project_id = None
        self._region = None
        self._relation = None
        self._relation_id = None
        self._relation_type = None
        self._retry_interval = None
        self._retry_times = None
        self._script_name = None
        self._service_and_stage = None
        self._special_type = None
        self._update_time = None
        self._update_time_stamp = None
        self._update_time_string = None
        self._update_user = None
        self._user_id = None
        self._variable_list = None
        self.discriminator = None

        if alias_runaw is not None:
            self.alias_runaw = alias_runaw
        if authentication_info is not None:
            self.authentication_info = authentication_info
        if authentication_type is not None:
            self.authentication_type = authentication_type
        if aw_description is not None:
            self.aw_description = aw_description
        if aw_id is not None:
            self.aw_id = aw_id
        if aw_type is not None:
            self.aw_type = aw_type
        if basic_aw is not None:
            self.basic_aw = basic_aw
        if body_param_type is not None:
            self.body_param_type = body_param_type
        if by_order is not None:
            self.by_order = by_order
        if change_sign is not None:
            self.change_sign = change_sign
        if check_point_list is not None:
            self.check_point_list = check_point_list
        if children is not None:
            self.children = children
        if condition_statement is not None:
            self.condition_statement = condition_statement
        if condition_type is not None:
            self.condition_type = condition_type
        if create_time is not None:
            self.create_time = create_time
        if create_time_stamp is not None:
            self.create_time_stamp = create_time_stamp
        if create_time_string is not None:
            self.create_time_string = create_time_string
        if create_user is not None:
            self.create_user = create_user
        if custom_header is not None:
            self.custom_header = custom_header
        if description is not None:
            self.description = description
        if error_info is not None:
            self.error_info = error_info
        if extra_info is not None:
            self.extra_info = extra_info
        if from_outside is not None:
            self.from_outside = from_outside
        if has_level is not None:
            self.has_level = has_level
        if header_array is not None:
            self.header_array = header_array
        if his_script is not None:
            self.his_script = his_script
        if id is not None:
            self.id = id
        if is_basic is not None:
            self.is_basic = is_basic
        if is_contract_aw is not None:
            self.is_contract_aw = is_contract_aw
        if is_disabled is not None:
            self.is_disabled = is_disabled
        if is_sectest_aw is not None:
            self.is_sectest_aw = is_sectest_aw
        if level is not None:
            self.level = level
        if name is not None:
            self.name = name
        if param_dependent is not None:
            self.param_dependent = param_dependent
        if param_dependent_enabled is not None:
            self.param_dependent_enabled = param_dependent_enabled
        if param_type_and_value is not None:
            self.param_type_and_value = param_type_and_value
        if project_id is not None:
            self.project_id = project_id
        if region is not None:
            self.region = region
        if relation is not None:
            self.relation = relation
        if relation_id is not None:
            self.relation_id = relation_id
        if relation_type is not None:
            self.relation_type = relation_type
        if retry_interval is not None:
            self.retry_interval = retry_interval
        if retry_times is not None:
            self.retry_times = retry_times
        if script_name is not None:
            self.script_name = script_name
        if service_and_stage is not None:
            self.service_and_stage = service_and_stage
        if special_type is not None:
            self.special_type = special_type
        if update_time is not None:
            self.update_time = update_time
        if update_time_stamp is not None:
            self.update_time_stamp = update_time_stamp
        if update_time_string is not None:
            self.update_time_string = update_time_string
        if update_user is not None:
            self.update_user = update_user
        if user_id is not None:
            self.user_id = user_id
        if variable_list is not None:
            self.variable_list = variable_list

    @property
    def alias_runaw(self):
        r"""Gets the alias_runaw of this AwInstanceRes.

        AW内容描述字段

        :return: The alias_runaw of this AwInstanceRes.
        :rtype: str
        """
        return self._alias_runaw

    @alias_runaw.setter
    def alias_runaw(self, alias_runaw):
        r"""Sets the alias_runaw of this AwInstanceRes.

        AW内容描述字段

        :param alias_runaw: The alias_runaw of this AwInstanceRes.
        :type alias_runaw: str
        """
        self._alias_runaw = alias_runaw

    @property
    def authentication_info(self):
        r"""Gets the authentication_info of this AwInstanceRes.

        :return: The authentication_info of this AwInstanceRes.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AuthInfo`
        """
        return self._authentication_info

    @authentication_info.setter
    def authentication_info(self, authentication_info):
        r"""Sets the authentication_info of this AwInstanceRes.

        :param authentication_info: The authentication_info of this AwInstanceRes.
        :type authentication_info: :class:`huaweicloudsdkcloudtest.v1.AuthInfo`
        """
        self._authentication_info = authentication_info

    @property
    def authentication_type(self):
        r"""Gets the authentication_type of this AwInstanceRes.

        认证类型,0-无认证;1-aksk认证

        :return: The authentication_type of this AwInstanceRes.
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        r"""Sets the authentication_type of this AwInstanceRes.

        认证类型,0-无认证;1-aksk认证

        :param authentication_type: The authentication_type of this AwInstanceRes.
        :type authentication_type: str
        """
        self._authentication_type = authentication_type

    @property
    def aw_description(self):
        r"""Gets the aw_description of this AwInstanceRes.

        脚本模板描述信息，在用例更新时添加

        :return: The aw_description of this AwInstanceRes.
        :rtype: str
        """
        return self._aw_description

    @aw_description.setter
    def aw_description(self, aw_description):
        r"""Sets the aw_description of this AwInstanceRes.

        脚本模板描述信息，在用例更新时添加

        :param aw_description: The aw_description of this AwInstanceRes.
        :type aw_description: str
        """
        self._aw_description = aw_description

    @property
    def aw_id(self):
        r"""Gets the aw_id of this AwInstanceRes.

        aw id

        :return: The aw_id of this AwInstanceRes.
        :rtype: str
        """
        return self._aw_id

    @aw_id.setter
    def aw_id(self, aw_id):
        r"""Sets the aw_id of this AwInstanceRes.

        aw id

        :param aw_id: The aw_id of this AwInstanceRes.
        :type aw_id: str
        """
        self._aw_id = aw_id

    @property
    def aw_type(self):
        r"""Gets the aw_type of this AwInstanceRes.

        aw类型 0-setup;1-test;2-teardown

        :return: The aw_type of this AwInstanceRes.
        :rtype: int
        """
        return self._aw_type

    @aw_type.setter
    def aw_type(self, aw_type):
        r"""Sets the aw_type of this AwInstanceRes.

        aw类型 0-setup;1-test;2-teardown

        :param aw_type: The aw_type of this AwInstanceRes.
        :type aw_type: int
        """
        self._aw_type = aw_type

    @property
    def basic_aw(self):
        r"""Gets the basic_aw of this AwInstanceRes.

        :return: The basic_aw of this AwInstanceRes.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.BasicAwRes`
        """
        return self._basic_aw

    @basic_aw.setter
    def basic_aw(self, basic_aw):
        r"""Sets the basic_aw of this AwInstanceRes.

        :param basic_aw: The basic_aw of this AwInstanceRes.
        :type basic_aw: :class:`huaweicloudsdkcloudtest.v1.BasicAwRes`
        """
        self._basic_aw = basic_aw

    @property
    def body_param_type(self):
        r"""Gets the body_param_type of this AwInstanceRes.

        instance的参数body体类型：form/text

        :return: The body_param_type of this AwInstanceRes.
        :rtype: str
        """
        return self._body_param_type

    @body_param_type.setter
    def body_param_type(self, body_param_type):
        r"""Sets the body_param_type of this AwInstanceRes.

        instance的参数body体类型：form/text

        :param body_param_type: The body_param_type of this AwInstanceRes.
        :type body_param_type: str
        """
        self._body_param_type = body_param_type

    @property
    def by_order(self):
        r"""Gets the by_order of this AwInstanceRes.

        顺序

        :return: The by_order of this AwInstanceRes.
        :rtype: int
        """
        return self._by_order

    @by_order.setter
    def by_order(self, by_order):
        r"""Sets the by_order of this AwInstanceRes.

        顺序

        :param by_order: The by_order of this AwInstanceRes.
        :type by_order: int
        """
        self._by_order = by_order

    @property
    def change_sign(self):
        r"""Gets the change_sign of this AwInstanceRes.

        change sign

        :return: The change_sign of this AwInstanceRes.
        :rtype: int
        """
        return self._change_sign

    @change_sign.setter
    def change_sign(self, change_sign):
        r"""Sets the change_sign of this AwInstanceRes.

        change sign

        :param change_sign: The change_sign of this AwInstanceRes.
        :type change_sign: int
        """
        self._change_sign = change_sign

    @property
    def check_point_list(self):
        r"""Gets the check_point_list of this AwInstanceRes.

        检查点List

        :return: The check_point_list of this AwInstanceRes.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.CheckPoint`]
        """
        return self._check_point_list

    @check_point_list.setter
    def check_point_list(self, check_point_list):
        r"""Sets the check_point_list of this AwInstanceRes.

        检查点List

        :param check_point_list: The check_point_list of this AwInstanceRes.
        :type check_point_list: list[:class:`huaweicloudsdkcloudtest.v1.CheckPoint`]
        """
        self._check_point_list = check_point_list

    @property
    def children(self):
        r"""Gets the children of this AwInstanceRes.

        aw实例

        :return: The children of this AwInstanceRes.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwInstanceRes`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this AwInstanceRes.

        aw实例

        :param children: The children of this AwInstanceRes.
        :type children: list[:class:`huaweicloudsdkcloudtest.v1.AwInstanceRes`]
        """
        self._children = children

    @property
    def condition_statement(self):
        r"""Gets the condition_statement of this AwInstanceRes.

        条件语句

        :return: The condition_statement of this AwInstanceRes.
        :rtype: str
        """
        return self._condition_statement

    @condition_statement.setter
    def condition_statement(self, condition_statement):
        r"""Sets the condition_statement of this AwInstanceRes.

        条件语句

        :param condition_statement: The condition_statement of this AwInstanceRes.
        :type condition_statement: str
        """
        self._condition_statement = condition_statement

    @property
    def condition_type(self):
        r"""Gets the condition_type of this AwInstanceRes.

        条件类型 0-not condition;1-if begin;2-if

        :return: The condition_type of this AwInstanceRes.
        :rtype: int
        """
        return self._condition_type

    @condition_type.setter
    def condition_type(self, condition_type):
        r"""Sets the condition_type of this AwInstanceRes.

        条件类型 0-not condition;1-if begin;2-if

        :param condition_type: The condition_type of this AwInstanceRes.
        :type condition_type: int
        """
        self._condition_type = condition_type

    @property
    def create_time(self):
        r"""Gets the create_time of this AwInstanceRes.

        创建时间

        :return: The create_time of this AwInstanceRes.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AwInstanceRes.

        创建时间

        :param create_time: The create_time of this AwInstanceRes.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def create_time_stamp(self):
        r"""Gets the create_time_stamp of this AwInstanceRes.

        创建时间戳

        :return: The create_time_stamp of this AwInstanceRes.
        :rtype: int
        """
        return self._create_time_stamp

    @create_time_stamp.setter
    def create_time_stamp(self, create_time_stamp):
        r"""Sets the create_time_stamp of this AwInstanceRes.

        创建时间戳

        :param create_time_stamp: The create_time_stamp of this AwInstanceRes.
        :type create_time_stamp: int
        """
        self._create_time_stamp = create_time_stamp

    @property
    def create_time_string(self):
        r"""Gets the create_time_string of this AwInstanceRes.

        创建时间字符串

        :return: The create_time_string of this AwInstanceRes.
        :rtype: str
        """
        return self._create_time_string

    @create_time_string.setter
    def create_time_string(self, create_time_string):
        r"""Sets the create_time_string of this AwInstanceRes.

        创建时间字符串

        :param create_time_string: The create_time_string of this AwInstanceRes.
        :type create_time_string: str
        """
        self._create_time_string = create_time_string

    @property
    def create_user(self):
        r"""Gets the create_user of this AwInstanceRes.

        创建人

        :return: The create_user of this AwInstanceRes.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this AwInstanceRes.

        创建人

        :param create_user: The create_user of this AwInstanceRes.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def custom_header(self):
        r"""Gets the custom_header of this AwInstanceRes.

        测试步骤自定义请求头List；后续自定义URL请求头不再使用该字段

        :return: The custom_header of this AwInstanceRes.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        return self._custom_header

    @custom_header.setter
    def custom_header(self, custom_header):
        r"""Sets the custom_header of this AwInstanceRes.

        测试步骤自定义请求头List；后续自定义URL请求头不再使用该字段

        :param custom_header: The custom_header of this AwInstanceRes.
        :type custom_header: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        self._custom_header = custom_header

    @property
    def description(self):
        r"""Gets the description of this AwInstanceRes.

        描述

        :return: The description of this AwInstanceRes.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AwInstanceRes.

        描述

        :param description: The description of this AwInstanceRes.
        :type description: str
        """
        self._description = description

    @property
    def error_info(self):
        r"""Gets the error_info of this AwInstanceRes.

        :return: The error_info of this AwInstanceRes.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ErrorInfo`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this AwInstanceRes.

        :param error_info: The error_info of this AwInstanceRes.
        :type error_info: :class:`huaweicloudsdkcloudtest.v1.ErrorInfo`
        """
        self._error_info = error_info

    @property
    def extra_info(self):
        r"""Gets the extra_info of this AwInstanceRes.

        :return: The extra_info of this AwInstanceRes.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ExtraInfo`
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        r"""Sets the extra_info of this AwInstanceRes.

        :param extra_info: The extra_info of this AwInstanceRes.
        :type extra_info: :class:`huaweicloudsdkcloudtest.v1.ExtraInfo`
        """
        self._extra_info = extra_info

    @property
    def from_outside(self):
        r"""Gets the from_outside of this AwInstanceRes.

        该aw是否来自外部工程 0-no;1-yes

        :return: The from_outside of this AwInstanceRes.
        :rtype: int
        """
        return self._from_outside

    @from_outside.setter
    def from_outside(self, from_outside):
        r"""Sets the from_outside of this AwInstanceRes.

        该aw是否来自外部工程 0-no;1-yes

        :param from_outside: The from_outside of this AwInstanceRes.
        :type from_outside: int
        """
        self._from_outside = from_outside

    @property
    def has_level(self):
        r"""Gets the has_level of this AwInstanceRes.

        level

        :return: The has_level of this AwInstanceRes.
        :rtype: int
        """
        return self._has_level

    @has_level.setter
    def has_level(self, has_level):
        r"""Sets the has_level of this AwInstanceRes.

        level

        :param has_level: The has_level of this AwInstanceRes.
        :type has_level: int
        """
        self._has_level = has_level

    @property
    def header_array(self):
        r"""Gets the header_array of this AwInstanceRes.

        :return: The header_array of this AwInstanceRes.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.ArrayNode`]
        """
        return self._header_array

    @header_array.setter
    def header_array(self, header_array):
        r"""Sets the header_array of this AwInstanceRes.

        :param header_array: The header_array of this AwInstanceRes.
        :type header_array: list[:class:`huaweicloudsdkcloudtest.v1.ArrayNode`]
        """
        self._header_array = header_array

    @property
    def his_script(self):
        r"""Gets the his_script of this AwInstanceRes.

        值不为null表示老的IF判断语句；值为null表示新的IF判断语句

        :return: The his_script of this AwInstanceRes.
        :rtype: str
        """
        return self._his_script

    @his_script.setter
    def his_script(self, his_script):
        r"""Sets the his_script of this AwInstanceRes.

        值不为null表示老的IF判断语句；值为null表示新的IF判断语句

        :param his_script: The his_script of this AwInstanceRes.
        :type his_script: str
        """
        self._his_script = his_script

    @property
    def id(self):
        r"""Gets the id of this AwInstanceRes.

        id

        :return: The id of this AwInstanceRes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AwInstanceRes.

        id

        :param id: The id of this AwInstanceRes.
        :type id: str
        """
        self._id = id

    @property
    def is_basic(self):
        r"""Gets the is_basic of this AwInstanceRes.

        是否模板类型测试步骤 0：自定义URL配置类型；1：模板类型测试步骤

        :return: The is_basic of this AwInstanceRes.
        :rtype: int
        """
        return self._is_basic

    @is_basic.setter
    def is_basic(self, is_basic):
        r"""Sets the is_basic of this AwInstanceRes.

        是否模板类型测试步骤 0：自定义URL配置类型；1：模板类型测试步骤

        :param is_basic: The is_basic of this AwInstanceRes.
        :type is_basic: int
        """
        self._is_basic = is_basic

    @property
    def is_contract_aw(self):
        r"""Gets the is_contract_aw of this AwInstanceRes.

        是否是契约AW 0-否；1-yes

        :return: The is_contract_aw of this AwInstanceRes.
        :rtype: int
        """
        return self._is_contract_aw

    @is_contract_aw.setter
    def is_contract_aw(self, is_contract_aw):
        r"""Sets the is_contract_aw of this AwInstanceRes.

        是否是契约AW 0-否；1-yes

        :param is_contract_aw: The is_contract_aw of this AwInstanceRes.
        :type is_contract_aw: int
        """
        self._is_contract_aw = is_contract_aw

    @property
    def is_disabled(self):
        r"""Gets the is_disabled of this AwInstanceRes.

        是否被禁用 0-否；1-yes

        :return: The is_disabled of this AwInstanceRes.
        :rtype: int
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        r"""Sets the is_disabled of this AwInstanceRes.

        是否被禁用 0-否；1-yes

        :param is_disabled: The is_disabled of this AwInstanceRes.
        :type is_disabled: int
        """
        self._is_disabled = is_disabled

    @property
    def is_sectest_aw(self):
        r"""Gets the is_sectest_aw of this AwInstanceRes.

        是否是安全测试aw

        :return: The is_sectest_aw of this AwInstanceRes.
        :rtype: int
        """
        return self._is_sectest_aw

    @is_sectest_aw.setter
    def is_sectest_aw(self, is_sectest_aw):
        r"""Sets the is_sectest_aw of this AwInstanceRes.

        是否是安全测试aw

        :param is_sectest_aw: The is_sectest_aw of this AwInstanceRes.
        :type is_sectest_aw: int
        """
        self._is_sectest_aw = is_sectest_aw

    @property
    def level(self):
        r"""Gets the level of this AwInstanceRes.

        用例级别

        :return: The level of this AwInstanceRes.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this AwInstanceRes.

        用例级别

        :param level: The level of this AwInstanceRes.
        :type level: int
        """
        self._level = level

    @property
    def name(self):
        r"""Gets the name of this AwInstanceRes.

        名称

        :return: The name of this AwInstanceRes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AwInstanceRes.

        名称

        :param name: The name of this AwInstanceRes.
        :type name: str
        """
        self._name = name

    @property
    def param_dependent(self):
        r"""Gets the param_dependent of this AwInstanceRes.

        参数依赖规则

        :return: The param_dependent of this AwInstanceRes.
        :rtype: str
        """
        return self._param_dependent

    @param_dependent.setter
    def param_dependent(self, param_dependent):
        r"""Sets the param_dependent of this AwInstanceRes.

        参数依赖规则

        :param param_dependent: The param_dependent of this AwInstanceRes.
        :type param_dependent: str
        """
        self._param_dependent = param_dependent

    @property
    def param_dependent_enabled(self):
        r"""Gets the param_dependent_enabled of this AwInstanceRes.

        是否启用参数依赖

        :return: The param_dependent_enabled of this AwInstanceRes.
        :rtype: int
        """
        return self._param_dependent_enabled

    @param_dependent_enabled.setter
    def param_dependent_enabled(self, param_dependent_enabled):
        r"""Sets the param_dependent_enabled of this AwInstanceRes.

        是否启用参数依赖

        :param param_dependent_enabled: The param_dependent_enabled of this AwInstanceRes.
        :type param_dependent_enabled: int
        """
        self._param_dependent_enabled = param_dependent_enabled

    @property
    def param_type_and_value(self):
        r"""Gets the param_type_and_value of this AwInstanceRes.

        参数类型和参数值对应List

        :return: The param_type_and_value of this AwInstanceRes.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        return self._param_type_and_value

    @param_type_and_value.setter
    def param_type_and_value(self, param_type_and_value):
        r"""Sets the param_type_and_value of this AwInstanceRes.

        参数类型和参数值对应List

        :param param_type_and_value: The param_type_and_value of this AwInstanceRes.
        :type param_type_and_value: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        self._param_type_and_value = param_type_and_value

    @property
    def project_id(self):
        r"""Gets the project_id of this AwInstanceRes.

        awinstance所在的用例\\逻辑用例\\组合aw所属项目,该字段是新增字段,因此部分awinstance是无值的,所以只可写该值,而不能读取该值

        :return: The project_id of this AwInstanceRes.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AwInstanceRes.

        awinstance所在的用例\\逻辑用例\\组合aw所属项目,该字段是新增字段,因此部分awinstance是无值的,所以只可写该值,而不能读取该值

        :param project_id: The project_id of this AwInstanceRes.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region(self):
        r"""Gets the region of this AwInstanceRes.

        区域名称

        :return: The region of this AwInstanceRes.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this AwInstanceRes.

        区域名称

        :param region: The region of this AwInstanceRes.
        :type region: str
        """
        self._region = region

    @property
    def relation(self):
        r"""Gets the relation of this AwInstanceRes.

        awId层级关系

        :return: The relation of this AwInstanceRes.
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        r"""Sets the relation of this AwInstanceRes.

        awId层级关系

        :param relation: The relation of this AwInstanceRes.
        :type relation: str
        """
        self._relation = relation

    @property
    def relation_id(self):
        r"""Gets the relation_id of this AwInstanceRes.

        relation id

        :return: The relation_id of this AwInstanceRes.
        :rtype: str
        """
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        r"""Sets the relation_id of this AwInstanceRes.

        relation id

        :param relation_id: The relation_id of this AwInstanceRes.
        :type relation_id: str
        """
        self._relation_id = relation_id

    @property
    def relation_type(self):
        r"""Gets the relation_type of this AwInstanceRes.

        映射类型 1-反向删除映射;2-用例自动添加的方向删除步骤

        :return: The relation_type of this AwInstanceRes.
        :rtype: int
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        r"""Sets the relation_type of this AwInstanceRes.

        映射类型 1-反向删除映射;2-用例自动添加的方向删除步骤

        :param relation_type: The relation_type of this AwInstanceRes.
        :type relation_type: int
        """
        self._relation_type = relation_type

    @property
    def retry_interval(self):
        r"""Gets the retry_interval of this AwInstanceRes.

        重试间隔时间 (ms) 为空表示不等待

        :return: The retry_interval of this AwInstanceRes.
        :rtype: str
        """
        return self._retry_interval

    @retry_interval.setter
    def retry_interval(self, retry_interval):
        r"""Sets the retry_interval of this AwInstanceRes.

        重试间隔时间 (ms) 为空表示不等待

        :param retry_interval: The retry_interval of this AwInstanceRes.
        :type retry_interval: str
        """
        self._retry_interval = retry_interval

    @property
    def retry_times(self):
        r"""Gets the retry_times of this AwInstanceRes.

        重试次数

        :return: The retry_times of this AwInstanceRes.
        :rtype: str
        """
        return self._retry_times

    @retry_times.setter
    def retry_times(self, retry_times):
        r"""Sets the retry_times of this AwInstanceRes.

        重试次数

        :param retry_times: The retry_times of this AwInstanceRes.
        :type retry_times: str
        """
        self._retry_times = retry_times

    @property
    def script_name(self):
        r"""Gets the script_name of this AwInstanceRes.

        获取脚本生成时，要使用的步骤名称

        :return: The script_name of this AwInstanceRes.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        r"""Sets the script_name of this AwInstanceRes.

        获取脚本生成时，要使用的步骤名称

        :param script_name: The script_name of this AwInstanceRes.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def service_and_stage(self):
        r"""Gets the service_and_stage of this AwInstanceRes.

        aw所来自工程的服务名和阶段名 fromOutside为1时该值有效

        :return: The service_and_stage of this AwInstanceRes.
        :rtype: str
        """
        return self._service_and_stage

    @service_and_stage.setter
    def service_and_stage(self, service_and_stage):
        r"""Sets the service_and_stage of this AwInstanceRes.

        aw所来自工程的服务名和阶段名 fromOutside为1时该值有效

        :param service_and_stage: The service_and_stage of this AwInstanceRes.
        :type service_and_stage: str
        """
        self._service_and_stage = service_and_stage

    @property
    def special_type(self):
        r"""Gets the special_type of this AwInstanceRes.

        测试步骤来源

        :return: The special_type of this AwInstanceRes.
        :rtype: int
        """
        return self._special_type

    @special_type.setter
    def special_type(self, special_type):
        r"""Sets the special_type of this AwInstanceRes.

        测试步骤来源

        :param special_type: The special_type of this AwInstanceRes.
        :type special_type: int
        """
        self._special_type = special_type

    @property
    def update_time(self):
        r"""Gets the update_time of this AwInstanceRes.

        更新时间

        :return: The update_time of this AwInstanceRes.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AwInstanceRes.

        更新时间

        :param update_time: The update_time of this AwInstanceRes.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def update_time_stamp(self):
        r"""Gets the update_time_stamp of this AwInstanceRes.

        更新时间戳

        :return: The update_time_stamp of this AwInstanceRes.
        :rtype: int
        """
        return self._update_time_stamp

    @update_time_stamp.setter
    def update_time_stamp(self, update_time_stamp):
        r"""Sets the update_time_stamp of this AwInstanceRes.

        更新时间戳

        :param update_time_stamp: The update_time_stamp of this AwInstanceRes.
        :type update_time_stamp: int
        """
        self._update_time_stamp = update_time_stamp

    @property
    def update_time_string(self):
        r"""Gets the update_time_string of this AwInstanceRes.

        更新时间字符串

        :return: The update_time_string of this AwInstanceRes.
        :rtype: str
        """
        return self._update_time_string

    @update_time_string.setter
    def update_time_string(self, update_time_string):
        r"""Sets the update_time_string of this AwInstanceRes.

        更新时间字符串

        :param update_time_string: The update_time_string of this AwInstanceRes.
        :type update_time_string: str
        """
        self._update_time_string = update_time_string

    @property
    def update_user(self):
        r"""Gets the update_user of this AwInstanceRes.

        更新人

        :return: The update_user of this AwInstanceRes.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this AwInstanceRes.

        更新人

        :param update_user: The update_user of this AwInstanceRes.
        :type update_user: str
        """
        self._update_user = update_user

    @property
    def user_id(self):
        r"""Gets the user_id of this AwInstanceRes.

        user id

        :return: The user_id of this AwInstanceRes.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this AwInstanceRes.

        user id

        :param user_id: The user_id of this AwInstanceRes.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def variable_list(self):
        r"""Gets the variable_list of this AwInstanceRes.

        定义的变量信息

        :return: The variable_list of this AwInstanceRes.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        """
        return self._variable_list

    @variable_list.setter
    def variable_list(self, variable_list):
        r"""Sets the variable_list of this AwInstanceRes.

        定义的变量信息

        :param variable_list: The variable_list of this AwInstanceRes.
        :type variable_list: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        """
        self._variable_list = variable_list

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
        if not isinstance(other, AwInstanceRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
