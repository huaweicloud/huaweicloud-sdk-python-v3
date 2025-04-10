# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTestCaseReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'activity_id': 'str',
        'add_to_plan': 'bool',
        'aw_cata_list': 'list[BasicAwCata]',
        'aw_instance': 'CaseAwInstance',
        'case_type': 'int',
        'case_variable_list': 'list[AwVariable]',
        'demo_flag': 'str',
        'error_step': 'list[int]',
        'id': 'str',
        'import_info_list': 'list[str]',
        'is_key_word': 'int',
        'is_sync': 'bool',
        'issue_id': 'str',
        'name': 'str',
        'old_tmss_case_uri': 'str',
        'old_tmss_case_uri_list': 'list[str]',
        'package_name': 'str',
        'plan_id': 'str',
        'project_id': 'str',
        'release_dev': 'str',
        'script_name': 'str',
        'script_path': 'str',
        'source': 'str',
        'source_way': 'str',
        'src_tmss_case_uri': 'str',
        'tmss_case_uri': 'str',
        'tmss_feature_uri': 'str',
        'tmss_property': 'TmssTestcase',
        'type': 'str',
        'variable_group_id': 'str'
    }

    attribute_map = {
        'activity_id': 'activity_id',
        'add_to_plan': 'addToPlan',
        'aw_cata_list': 'aw_cata_list',
        'aw_instance': 'aw_instance',
        'case_type': 'case_type',
        'case_variable_list': 'case_variable_list',
        'demo_flag': 'demoFlag',
        'error_step': 'errorStep',
        'id': 'id',
        'import_info_list': 'import_info_list',
        'is_key_word': 'isKeyWord',
        'is_sync': 'isSync',
        'issue_id': 'issueId',
        'name': 'name',
        'old_tmss_case_uri': 'old_tmss_case_uri',
        'old_tmss_case_uri_list': 'old_tmss_case_uri_list',
        'package_name': 'package_name',
        'plan_id': 'planId',
        'project_id': 'project_id',
        'release_dev': 'releaseDev',
        'script_name': 'script_name',
        'script_path': 'script_path',
        'source': 'source',
        'source_way': 'sourceWay',
        'src_tmss_case_uri': 'src_tmss_case_uri',
        'tmss_case_uri': 'tmss_case_uri',
        'tmss_feature_uri': 'tmss_feature_uri',
        'tmss_property': 'tmss_property',
        'type': 'type',
        'variable_group_id': 'variableGroupId'
    }

    def __init__(self, activity_id=None, add_to_plan=None, aw_cata_list=None, aw_instance=None, case_type=None, case_variable_list=None, demo_flag=None, error_step=None, id=None, import_info_list=None, is_key_word=None, is_sync=None, issue_id=None, name=None, old_tmss_case_uri=None, old_tmss_case_uri_list=None, package_name=None, plan_id=None, project_id=None, release_dev=None, script_name=None, script_path=None, source=None, source_way=None, src_tmss_case_uri=None, tmss_case_uri=None, tmss_feature_uri=None, tmss_property=None, type=None, variable_group_id=None):
        r"""CreateTestCaseReq

        The model defined in huaweicloud sdk

        :param activity_id: 活动id
        :type activity_id: str
        :param add_to_plan: 是否添加到计划
        :type add_to_plan: bool
        :param aw_cata_list: 创建时可选择导入的aw目录直接产生测试步骤
        :type aw_cata_list: list[:class:`huaweicloudsdkcloudtest.v1.BasicAwCata`]
        :param aw_instance: 
        :type aw_instance: :class:`huaweicloudsdkcloudtest.v1.CaseAwInstance`
        :param case_type: 用例类型：0商用现有类型，1从内部导过来的用例类型
        :type case_type: int
        :param case_variable_list: 用例局部变量
        :type case_variable_list: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        :param demo_flag: 演示标志
        :type demo_flag: str
        :param error_step: 错误测试阶段
        :type error_step: list[int]
        :param id: id
        :type id: str
        :param import_info_list: import信息List
        :type import_info_list: list[str]
        :param is_key_word: 是否设置为关键字操作
        :type is_key_word: int
        :param is_sync: 是否同步
        :type is_sync: bool
        :param issue_id: 问题ID
        :type issue_id: str
        :param name: 名称
        :type name: str
        :param old_tmss_case_uri: 被复制用例的tmsscaseuri
        :type old_tmss_case_uri: str
        :param old_tmss_case_uri_list: 被复制用例的tmsscaseuri列表，内部使用
        :type old_tmss_case_uri_list: list[str]
        :param package_name: 包名
        :type package_name: str
        :param plan_id: 计划ID
        :type plan_id: str
        :param project_id: 工程ID
        :type project_id: str
        :param release_dev: 新服务新建用例版本号
        :type release_dev: str
        :param script_name: 脚本名(类名)
        :type script_name: str
        :param script_path: 脚本路径
        :type script_path: str
        :param source: 来源
        :type source: str
        :param source_way: 来源的方式
        :type source_way: str
        :param src_tmss_case_uri: 选择用例中测试步骤生成关键字时的原用例tmssCaseUri
        :type src_tmss_case_uri: str
        :param tmss_case_uri: tmss用例uri
        :type tmss_case_uri: str
        :param tmss_feature_uri: tmss用例uri
        :type tmss_feature_uri: str
        :param tmss_property: 
        :type tmss_property: :class:`huaweicloudsdkcloudtest.v1.TmssTestcase`
        :param type: 类型
        :type type: str
        :param variable_group_id: 环境参数分组id
        :type variable_group_id: str
        """
        
        

        self._activity_id = None
        self._add_to_plan = None
        self._aw_cata_list = None
        self._aw_instance = None
        self._case_type = None
        self._case_variable_list = None
        self._demo_flag = None
        self._error_step = None
        self._id = None
        self._import_info_list = None
        self._is_key_word = None
        self._is_sync = None
        self._issue_id = None
        self._name = None
        self._old_tmss_case_uri = None
        self._old_tmss_case_uri_list = None
        self._package_name = None
        self._plan_id = None
        self._project_id = None
        self._release_dev = None
        self._script_name = None
        self._script_path = None
        self._source = None
        self._source_way = None
        self._src_tmss_case_uri = None
        self._tmss_case_uri = None
        self._tmss_feature_uri = None
        self._tmss_property = None
        self._type = None
        self._variable_group_id = None
        self.discriminator = None

        if activity_id is not None:
            self.activity_id = activity_id
        if add_to_plan is not None:
            self.add_to_plan = add_to_plan
        if aw_cata_list is not None:
            self.aw_cata_list = aw_cata_list
        if aw_instance is not None:
            self.aw_instance = aw_instance
        if case_type is not None:
            self.case_type = case_type
        if case_variable_list is not None:
            self.case_variable_list = case_variable_list
        if demo_flag is not None:
            self.demo_flag = demo_flag
        if error_step is not None:
            self.error_step = error_step
        if id is not None:
            self.id = id
        if import_info_list is not None:
            self.import_info_list = import_info_list
        if is_key_word is not None:
            self.is_key_word = is_key_word
        if is_sync is not None:
            self.is_sync = is_sync
        if issue_id is not None:
            self.issue_id = issue_id
        if name is not None:
            self.name = name
        if old_tmss_case_uri is not None:
            self.old_tmss_case_uri = old_tmss_case_uri
        if old_tmss_case_uri_list is not None:
            self.old_tmss_case_uri_list = old_tmss_case_uri_list
        if package_name is not None:
            self.package_name = package_name
        if plan_id is not None:
            self.plan_id = plan_id
        if project_id is not None:
            self.project_id = project_id
        if release_dev is not None:
            self.release_dev = release_dev
        if script_name is not None:
            self.script_name = script_name
        if script_path is not None:
            self.script_path = script_path
        if source is not None:
            self.source = source
        if source_way is not None:
            self.source_way = source_way
        if src_tmss_case_uri is not None:
            self.src_tmss_case_uri = src_tmss_case_uri
        if tmss_case_uri is not None:
            self.tmss_case_uri = tmss_case_uri
        if tmss_feature_uri is not None:
            self.tmss_feature_uri = tmss_feature_uri
        if tmss_property is not None:
            self.tmss_property = tmss_property
        if type is not None:
            self.type = type
        if variable_group_id is not None:
            self.variable_group_id = variable_group_id

    @property
    def activity_id(self):
        r"""Gets the activity_id of this CreateTestCaseReq.

        活动id

        :return: The activity_id of this CreateTestCaseReq.
        :rtype: str
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        r"""Sets the activity_id of this CreateTestCaseReq.

        活动id

        :param activity_id: The activity_id of this CreateTestCaseReq.
        :type activity_id: str
        """
        self._activity_id = activity_id

    @property
    def add_to_plan(self):
        r"""Gets the add_to_plan of this CreateTestCaseReq.

        是否添加到计划

        :return: The add_to_plan of this CreateTestCaseReq.
        :rtype: bool
        """
        return self._add_to_plan

    @add_to_plan.setter
    def add_to_plan(self, add_to_plan):
        r"""Sets the add_to_plan of this CreateTestCaseReq.

        是否添加到计划

        :param add_to_plan: The add_to_plan of this CreateTestCaseReq.
        :type add_to_plan: bool
        """
        self._add_to_plan = add_to_plan

    @property
    def aw_cata_list(self):
        r"""Gets the aw_cata_list of this CreateTestCaseReq.

        创建时可选择导入的aw目录直接产生测试步骤

        :return: The aw_cata_list of this CreateTestCaseReq.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.BasicAwCata`]
        """
        return self._aw_cata_list

    @aw_cata_list.setter
    def aw_cata_list(self, aw_cata_list):
        r"""Sets the aw_cata_list of this CreateTestCaseReq.

        创建时可选择导入的aw目录直接产生测试步骤

        :param aw_cata_list: The aw_cata_list of this CreateTestCaseReq.
        :type aw_cata_list: list[:class:`huaweicloudsdkcloudtest.v1.BasicAwCata`]
        """
        self._aw_cata_list = aw_cata_list

    @property
    def aw_instance(self):
        r"""Gets the aw_instance of this CreateTestCaseReq.

        :return: The aw_instance of this CreateTestCaseReq.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CaseAwInstance`
        """
        return self._aw_instance

    @aw_instance.setter
    def aw_instance(self, aw_instance):
        r"""Sets the aw_instance of this CreateTestCaseReq.

        :param aw_instance: The aw_instance of this CreateTestCaseReq.
        :type aw_instance: :class:`huaweicloudsdkcloudtest.v1.CaseAwInstance`
        """
        self._aw_instance = aw_instance

    @property
    def case_type(self):
        r"""Gets the case_type of this CreateTestCaseReq.

        用例类型：0商用现有类型，1从内部导过来的用例类型

        :return: The case_type of this CreateTestCaseReq.
        :rtype: int
        """
        return self._case_type

    @case_type.setter
    def case_type(self, case_type):
        r"""Sets the case_type of this CreateTestCaseReq.

        用例类型：0商用现有类型，1从内部导过来的用例类型

        :param case_type: The case_type of this CreateTestCaseReq.
        :type case_type: int
        """
        self._case_type = case_type

    @property
    def case_variable_list(self):
        r"""Gets the case_variable_list of this CreateTestCaseReq.

        用例局部变量

        :return: The case_variable_list of this CreateTestCaseReq.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        """
        return self._case_variable_list

    @case_variable_list.setter
    def case_variable_list(self, case_variable_list):
        r"""Sets the case_variable_list of this CreateTestCaseReq.

        用例局部变量

        :param case_variable_list: The case_variable_list of this CreateTestCaseReq.
        :type case_variable_list: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        """
        self._case_variable_list = case_variable_list

    @property
    def demo_flag(self):
        r"""Gets the demo_flag of this CreateTestCaseReq.

        演示标志

        :return: The demo_flag of this CreateTestCaseReq.
        :rtype: str
        """
        return self._demo_flag

    @demo_flag.setter
    def demo_flag(self, demo_flag):
        r"""Sets the demo_flag of this CreateTestCaseReq.

        演示标志

        :param demo_flag: The demo_flag of this CreateTestCaseReq.
        :type demo_flag: str
        """
        self._demo_flag = demo_flag

    @property
    def error_step(self):
        r"""Gets the error_step of this CreateTestCaseReq.

        错误测试阶段

        :return: The error_step of this CreateTestCaseReq.
        :rtype: list[int]
        """
        return self._error_step

    @error_step.setter
    def error_step(self, error_step):
        r"""Sets the error_step of this CreateTestCaseReq.

        错误测试阶段

        :param error_step: The error_step of this CreateTestCaseReq.
        :type error_step: list[int]
        """
        self._error_step = error_step

    @property
    def id(self):
        r"""Gets the id of this CreateTestCaseReq.

        id

        :return: The id of this CreateTestCaseReq.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateTestCaseReq.

        id

        :param id: The id of this CreateTestCaseReq.
        :type id: str
        """
        self._id = id

    @property
    def import_info_list(self):
        r"""Gets the import_info_list of this CreateTestCaseReq.

        import信息List

        :return: The import_info_list of this CreateTestCaseReq.
        :rtype: list[str]
        """
        return self._import_info_list

    @import_info_list.setter
    def import_info_list(self, import_info_list):
        r"""Sets the import_info_list of this CreateTestCaseReq.

        import信息List

        :param import_info_list: The import_info_list of this CreateTestCaseReq.
        :type import_info_list: list[str]
        """
        self._import_info_list = import_info_list

    @property
    def is_key_word(self):
        r"""Gets the is_key_word of this CreateTestCaseReq.

        是否设置为关键字操作

        :return: The is_key_word of this CreateTestCaseReq.
        :rtype: int
        """
        return self._is_key_word

    @is_key_word.setter
    def is_key_word(self, is_key_word):
        r"""Sets the is_key_word of this CreateTestCaseReq.

        是否设置为关键字操作

        :param is_key_word: The is_key_word of this CreateTestCaseReq.
        :type is_key_word: int
        """
        self._is_key_word = is_key_word

    @property
    def is_sync(self):
        r"""Gets the is_sync of this CreateTestCaseReq.

        是否同步

        :return: The is_sync of this CreateTestCaseReq.
        :rtype: bool
        """
        return self._is_sync

    @is_sync.setter
    def is_sync(self, is_sync):
        r"""Sets the is_sync of this CreateTestCaseReq.

        是否同步

        :param is_sync: The is_sync of this CreateTestCaseReq.
        :type is_sync: bool
        """
        self._is_sync = is_sync

    @property
    def issue_id(self):
        r"""Gets the issue_id of this CreateTestCaseReq.

        问题ID

        :return: The issue_id of this CreateTestCaseReq.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this CreateTestCaseReq.

        问题ID

        :param issue_id: The issue_id of this CreateTestCaseReq.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def name(self):
        r"""Gets the name of this CreateTestCaseReq.

        名称

        :return: The name of this CreateTestCaseReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateTestCaseReq.

        名称

        :param name: The name of this CreateTestCaseReq.
        :type name: str
        """
        self._name = name

    @property
    def old_tmss_case_uri(self):
        r"""Gets the old_tmss_case_uri of this CreateTestCaseReq.

        被复制用例的tmsscaseuri

        :return: The old_tmss_case_uri of this CreateTestCaseReq.
        :rtype: str
        """
        return self._old_tmss_case_uri

    @old_tmss_case_uri.setter
    def old_tmss_case_uri(self, old_tmss_case_uri):
        r"""Sets the old_tmss_case_uri of this CreateTestCaseReq.

        被复制用例的tmsscaseuri

        :param old_tmss_case_uri: The old_tmss_case_uri of this CreateTestCaseReq.
        :type old_tmss_case_uri: str
        """
        self._old_tmss_case_uri = old_tmss_case_uri

    @property
    def old_tmss_case_uri_list(self):
        r"""Gets the old_tmss_case_uri_list of this CreateTestCaseReq.

        被复制用例的tmsscaseuri列表，内部使用

        :return: The old_tmss_case_uri_list of this CreateTestCaseReq.
        :rtype: list[str]
        """
        return self._old_tmss_case_uri_list

    @old_tmss_case_uri_list.setter
    def old_tmss_case_uri_list(self, old_tmss_case_uri_list):
        r"""Sets the old_tmss_case_uri_list of this CreateTestCaseReq.

        被复制用例的tmsscaseuri列表，内部使用

        :param old_tmss_case_uri_list: The old_tmss_case_uri_list of this CreateTestCaseReq.
        :type old_tmss_case_uri_list: list[str]
        """
        self._old_tmss_case_uri_list = old_tmss_case_uri_list

    @property
    def package_name(self):
        r"""Gets the package_name of this CreateTestCaseReq.

        包名

        :return: The package_name of this CreateTestCaseReq.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        r"""Sets the package_name of this CreateTestCaseReq.

        包名

        :param package_name: The package_name of this CreateTestCaseReq.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def plan_id(self):
        r"""Gets the plan_id of this CreateTestCaseReq.

        计划ID

        :return: The plan_id of this CreateTestCaseReq.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this CreateTestCaseReq.

        计划ID

        :param plan_id: The plan_id of this CreateTestCaseReq.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateTestCaseReq.

        工程ID

        :return: The project_id of this CreateTestCaseReq.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateTestCaseReq.

        工程ID

        :param project_id: The project_id of this CreateTestCaseReq.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def release_dev(self):
        r"""Gets the release_dev of this CreateTestCaseReq.

        新服务新建用例版本号

        :return: The release_dev of this CreateTestCaseReq.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        r"""Sets the release_dev of this CreateTestCaseReq.

        新服务新建用例版本号

        :param release_dev: The release_dev of this CreateTestCaseReq.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def script_name(self):
        r"""Gets the script_name of this CreateTestCaseReq.

        脚本名(类名)

        :return: The script_name of this CreateTestCaseReq.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        r"""Sets the script_name of this CreateTestCaseReq.

        脚本名(类名)

        :param script_name: The script_name of this CreateTestCaseReq.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def script_path(self):
        r"""Gets the script_path of this CreateTestCaseReq.

        脚本路径

        :return: The script_path of this CreateTestCaseReq.
        :rtype: str
        """
        return self._script_path

    @script_path.setter
    def script_path(self, script_path):
        r"""Sets the script_path of this CreateTestCaseReq.

        脚本路径

        :param script_path: The script_path of this CreateTestCaseReq.
        :type script_path: str
        """
        self._script_path = script_path

    @property
    def source(self):
        r"""Gets the source of this CreateTestCaseReq.

        来源

        :return: The source of this CreateTestCaseReq.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CreateTestCaseReq.

        来源

        :param source: The source of this CreateTestCaseReq.
        :type source: str
        """
        self._source = source

    @property
    def source_way(self):
        r"""Gets the source_way of this CreateTestCaseReq.

        来源的方式

        :return: The source_way of this CreateTestCaseReq.
        :rtype: str
        """
        return self._source_way

    @source_way.setter
    def source_way(self, source_way):
        r"""Sets the source_way of this CreateTestCaseReq.

        来源的方式

        :param source_way: The source_way of this CreateTestCaseReq.
        :type source_way: str
        """
        self._source_way = source_way

    @property
    def src_tmss_case_uri(self):
        r"""Gets the src_tmss_case_uri of this CreateTestCaseReq.

        选择用例中测试步骤生成关键字时的原用例tmssCaseUri

        :return: The src_tmss_case_uri of this CreateTestCaseReq.
        :rtype: str
        """
        return self._src_tmss_case_uri

    @src_tmss_case_uri.setter
    def src_tmss_case_uri(self, src_tmss_case_uri):
        r"""Sets the src_tmss_case_uri of this CreateTestCaseReq.

        选择用例中测试步骤生成关键字时的原用例tmssCaseUri

        :param src_tmss_case_uri: The src_tmss_case_uri of this CreateTestCaseReq.
        :type src_tmss_case_uri: str
        """
        self._src_tmss_case_uri = src_tmss_case_uri

    @property
    def tmss_case_uri(self):
        r"""Gets the tmss_case_uri of this CreateTestCaseReq.

        tmss用例uri

        :return: The tmss_case_uri of this CreateTestCaseReq.
        :rtype: str
        """
        return self._tmss_case_uri

    @tmss_case_uri.setter
    def tmss_case_uri(self, tmss_case_uri):
        r"""Sets the tmss_case_uri of this CreateTestCaseReq.

        tmss用例uri

        :param tmss_case_uri: The tmss_case_uri of this CreateTestCaseReq.
        :type tmss_case_uri: str
        """
        self._tmss_case_uri = tmss_case_uri

    @property
    def tmss_feature_uri(self):
        r"""Gets the tmss_feature_uri of this CreateTestCaseReq.

        tmss用例uri

        :return: The tmss_feature_uri of this CreateTestCaseReq.
        :rtype: str
        """
        return self._tmss_feature_uri

    @tmss_feature_uri.setter
    def tmss_feature_uri(self, tmss_feature_uri):
        r"""Sets the tmss_feature_uri of this CreateTestCaseReq.

        tmss用例uri

        :param tmss_feature_uri: The tmss_feature_uri of this CreateTestCaseReq.
        :type tmss_feature_uri: str
        """
        self._tmss_feature_uri = tmss_feature_uri

    @property
    def tmss_property(self):
        r"""Gets the tmss_property of this CreateTestCaseReq.

        :return: The tmss_property of this CreateTestCaseReq.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TmssTestcase`
        """
        return self._tmss_property

    @tmss_property.setter
    def tmss_property(self, tmss_property):
        r"""Sets the tmss_property of this CreateTestCaseReq.

        :param tmss_property: The tmss_property of this CreateTestCaseReq.
        :type tmss_property: :class:`huaweicloudsdkcloudtest.v1.TmssTestcase`
        """
        self._tmss_property = tmss_property

    @property
    def type(self):
        r"""Gets the type of this CreateTestCaseReq.

        类型

        :return: The type of this CreateTestCaseReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateTestCaseReq.

        类型

        :param type: The type of this CreateTestCaseReq.
        :type type: str
        """
        self._type = type

    @property
    def variable_group_id(self):
        r"""Gets the variable_group_id of this CreateTestCaseReq.

        环境参数分组id

        :return: The variable_group_id of this CreateTestCaseReq.
        :rtype: str
        """
        return self._variable_group_id

    @variable_group_id.setter
    def variable_group_id(self, variable_group_id):
        r"""Sets the variable_group_id of this CreateTestCaseReq.

        环境参数分组id

        :param variable_group_id: The variable_group_id of this CreateTestCaseReq.
        :type variable_group_id: str
        """
        self._variable_group_id = variable_group_id

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
        if not isinstance(other, CreateTestCaseReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
