# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskInfoV4VoReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_action': 'str',
        'alert_config': 'object',
        'build_products': 'list[BuildProduct]',
        'case_package_env_name': 'str',
        'case_package_id': 'str',
        'case_package_name': 'str',
        'case_total': 'int',
        'client_type': 'str',
        'cloud_test_suite_basic_info': 'CloudTestSuiteBasicInfo',
        'comments': 'str',
        'create_time': 'datetime',
        'create_user': 'str',
        'env_type': 'int',
        'environment_group_id': 'str',
        'execute_strategies': 'ExecuteStrategiesVo',
        'executor_type': 'str',
        'ext_params': 'list[TaskExtParam]',
        'favorite': 'str',
        'id': 'str',
        'ip_group': 'IpGroup',
        'ip_key': 'str',
        'is_debug_task': 'int',
        'label': 'str',
        'label_name': 'str',
        'label_type': 'str',
        'last_stop_time': 'int',
        'location_ids': 'list[str]',
        'name': 'str',
        'plan_id': 'str',
        'pre_test_case_info': 'PreTestCaseInfo',
        'resource_pool': 'ResourcePool',
        'state': 'int',
        'subtask_id': 'str',
        'subtask_total': 'int',
        'task_type_id': 'str',
        'test_cases': 'list[TestCaseBasicInfo]',
        'test_service_id': 'str',
        'test_suite_type': 'int',
        'tip': 'str',
        'update_time': 'datetime',
        'update_user': 'str',
        'version': 'str'
    }

    attribute_map = {
        'alert_action': 'alert_action',
        'alert_config': 'alert_config',
        'build_products': 'build_products',
        'case_package_env_name': 'case_package_env_name',
        'case_package_id': 'case_package_id',
        'case_package_name': 'case_package_name',
        'case_total': 'case_total',
        'client_type': 'client_type',
        'cloud_test_suite_basic_info': 'cloudTestSuite_basicInfo',
        'comments': 'comments',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'env_type': 'env_type',
        'environment_group_id': 'environment_group_id',
        'execute_strategies': 'execute_strategies',
        'executor_type': 'executor_type',
        'ext_params': 'ext_params',
        'favorite': 'favorite',
        'id': 'id',
        'ip_group': 'ipGroup',
        'ip_key': 'ipKey',
        'is_debug_task': 'isDebugTask',
        'label': 'label',
        'label_name': 'labelName',
        'label_type': 'labelType',
        'last_stop_time': 'lastStopTime',
        'location_ids': 'location_ids',
        'name': 'name',
        'plan_id': 'planId',
        'pre_test_case_info': 'preTestCaseInfo',
        'resource_pool': 'resourcePool',
        'state': 'state',
        'subtask_id': 'subtask_id',
        'subtask_total': 'subtaskTotal',
        'task_type_id': 'taskTypeId',
        'test_cases': 'testCases',
        'test_service_id': 'test_service_id',
        'test_suite_type': 'testSuiteType',
        'tip': 'tip',
        'update_time': 'update_time',
        'update_user': 'update_user',
        'version': 'version'
    }

    def __init__(self, alert_action=None, alert_config=None, build_products=None, case_package_env_name=None, case_package_id=None, case_package_name=None, case_total=None, client_type=None, cloud_test_suite_basic_info=None, comments=None, create_time=None, create_user=None, env_type=None, environment_group_id=None, execute_strategies=None, executor_type=None, ext_params=None, favorite=None, id=None, ip_group=None, ip_key=None, is_debug_task=None, label=None, label_name=None, label_type=None, last_stop_time=None, location_ids=None, name=None, plan_id=None, pre_test_case_info=None, resource_pool=None, state=None, subtask_id=None, subtask_total=None, task_type_id=None, test_cases=None, test_service_id=None, test_suite_type=None, tip=None, update_time=None, update_user=None, version=None):
        r"""TaskInfoV4VoReq

        The model defined in huaweicloud sdk

        :param alert_action: 智能告警开关：0为置灰，1为可用
        :type alert_action: str
        :param alert_config: 告警配置
        :type alert_config: object
        :param build_products: 流水线启动测试套件，携带构建产物
        :type build_products: list[:class:`huaweicloudsdkcloudtest.v1.BuildProduct`]
        :param case_package_env_name: 用例环境参数
        :type case_package_env_name: str
        :param case_package_id: 用例包ID
        :type case_package_id: str
        :param case_package_name: 用例包名
        :type case_package_name: str
        :param case_total: 用例总数
        :type case_total: int
        :param client_type: 客户端类型，deviceTest使用
        :type client_type: str
        :param cloud_test_suite_basic_info: 
        :type cloud_test_suite_basic_info: :class:`huaweicloudsdkcloudtest.v1.CloudTestSuiteBasicInfo`
        :param comments: 
        :type comments: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param create_user: 创建人
        :type create_user: str
        :param env_type: 环境类型：0表示用例包环境，1表示全局环境
        :type env_type: int
        :param environment_group_id: environmentId环境信息
        :type environment_group_id: str
        :param execute_strategies: 
        :type execute_strategies: :class:`huaweicloudsdkcloudtest.v1.ExecuteStrategiesVo`
        :param executor_type: 用例类型
        :type executor_type: str
        :param ext_params: 扩展参数
        :type ext_params: list[:class:`huaweicloudsdkcloudtest.v1.TaskExtParam`]
        :param favorite: 
        :type favorite: str
        :param id: 唯一ID，主键
        :type id: str
        :param ip_group: 
        :type ip_group: :class:`huaweicloudsdkcloudtest.v1.IpGroup`
        :param ip_key: 小网拨测替换application的hostIP
        :type ip_key: str
        :param is_debug_task: 任务类型，是否debug任务
        :type is_debug_task: int
        :param label: 执行标签
        :type label: str
        :param label_name: 资源池名称
        :type label_name: str
        :param label_type: 资源池类型
        :type label_type: str
        :param last_stop_time: 最近一次停止时间 
        :type last_stop_time: int
        :param location_ids: 执行区域，冗余处理，修改更新在执行配置字段
        :type location_ids: list[str]
        :param name: 任务名
        :type name: str
        :param plan_id: 测试计划Id
        :type plan_id: str
        :param pre_test_case_info: 
        :type pre_test_case_info: :class:`huaweicloudsdkcloudtest.v1.PreTestCaseInfo`
        :param resource_pool: 
        :type resource_pool: :class:`huaweicloudsdkcloudtest.v1.ResourcePool`
        :param state: 任务状态
        :type state: int
        :param subtask_id: 
        :type subtask_id: str
        :param subtask_total: 子任务总数
        :type subtask_total: int
        :param task_type_id: 任务类型
        :type task_type_id: str
        :param test_cases: 测试用例列表
        :type test_cases: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseBasicInfo`]
        :param test_service_id: 项目id
        :type test_service_id: str
        :param test_suite_type: 测试套类型
        :type test_suite_type: int
        :param tip: 提示信息，用于任务操作过程中需要提供给前端的提示信息
        :type tip: str
        :param update_time: 创建时间
        :type update_time: datetime
        :param update_user: 更新人
        :type update_user: str
        :param version: 版本
        :type version: str
        """
        
        

        self._alert_action = None
        self._alert_config = None
        self._build_products = None
        self._case_package_env_name = None
        self._case_package_id = None
        self._case_package_name = None
        self._case_total = None
        self._client_type = None
        self._cloud_test_suite_basic_info = None
        self._comments = None
        self._create_time = None
        self._create_user = None
        self._env_type = None
        self._environment_group_id = None
        self._execute_strategies = None
        self._executor_type = None
        self._ext_params = None
        self._favorite = None
        self._id = None
        self._ip_group = None
        self._ip_key = None
        self._is_debug_task = None
        self._label = None
        self._label_name = None
        self._label_type = None
        self._last_stop_time = None
        self._location_ids = None
        self._name = None
        self._plan_id = None
        self._pre_test_case_info = None
        self._resource_pool = None
        self._state = None
        self._subtask_id = None
        self._subtask_total = None
        self._task_type_id = None
        self._test_cases = None
        self._test_service_id = None
        self._test_suite_type = None
        self._tip = None
        self._update_time = None
        self._update_user = None
        self._version = None
        self.discriminator = None

        if alert_action is not None:
            self.alert_action = alert_action
        if alert_config is not None:
            self.alert_config = alert_config
        if build_products is not None:
            self.build_products = build_products
        if case_package_env_name is not None:
            self.case_package_env_name = case_package_env_name
        if case_package_id is not None:
            self.case_package_id = case_package_id
        if case_package_name is not None:
            self.case_package_name = case_package_name
        if case_total is not None:
            self.case_total = case_total
        if client_type is not None:
            self.client_type = client_type
        if cloud_test_suite_basic_info is not None:
            self.cloud_test_suite_basic_info = cloud_test_suite_basic_info
        if comments is not None:
            self.comments = comments
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if env_type is not None:
            self.env_type = env_type
        if environment_group_id is not None:
            self.environment_group_id = environment_group_id
        if execute_strategies is not None:
            self.execute_strategies = execute_strategies
        if executor_type is not None:
            self.executor_type = executor_type
        if ext_params is not None:
            self.ext_params = ext_params
        if favorite is not None:
            self.favorite = favorite
        if id is not None:
            self.id = id
        if ip_group is not None:
            self.ip_group = ip_group
        if ip_key is not None:
            self.ip_key = ip_key
        if is_debug_task is not None:
            self.is_debug_task = is_debug_task
        if label is not None:
            self.label = label
        if label_name is not None:
            self.label_name = label_name
        if label_type is not None:
            self.label_type = label_type
        if last_stop_time is not None:
            self.last_stop_time = last_stop_time
        if location_ids is not None:
            self.location_ids = location_ids
        if name is not None:
            self.name = name
        if plan_id is not None:
            self.plan_id = plan_id
        if pre_test_case_info is not None:
            self.pre_test_case_info = pre_test_case_info
        if resource_pool is not None:
            self.resource_pool = resource_pool
        if state is not None:
            self.state = state
        if subtask_id is not None:
            self.subtask_id = subtask_id
        if subtask_total is not None:
            self.subtask_total = subtask_total
        if task_type_id is not None:
            self.task_type_id = task_type_id
        if test_cases is not None:
            self.test_cases = test_cases
        if test_service_id is not None:
            self.test_service_id = test_service_id
        if test_suite_type is not None:
            self.test_suite_type = test_suite_type
        if tip is not None:
            self.tip = tip
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user
        if version is not None:
            self.version = version

    @property
    def alert_action(self):
        r"""Gets the alert_action of this TaskInfoV4VoReq.

        智能告警开关：0为置灰，1为可用

        :return: The alert_action of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._alert_action

    @alert_action.setter
    def alert_action(self, alert_action):
        r"""Sets the alert_action of this TaskInfoV4VoReq.

        智能告警开关：0为置灰，1为可用

        :param alert_action: The alert_action of this TaskInfoV4VoReq.
        :type alert_action: str
        """
        self._alert_action = alert_action

    @property
    def alert_config(self):
        r"""Gets the alert_config of this TaskInfoV4VoReq.

        告警配置

        :return: The alert_config of this TaskInfoV4VoReq.
        :rtype: object
        """
        return self._alert_config

    @alert_config.setter
    def alert_config(self, alert_config):
        r"""Sets the alert_config of this TaskInfoV4VoReq.

        告警配置

        :param alert_config: The alert_config of this TaskInfoV4VoReq.
        :type alert_config: object
        """
        self._alert_config = alert_config

    @property
    def build_products(self):
        r"""Gets the build_products of this TaskInfoV4VoReq.

        流水线启动测试套件，携带构建产物

        :return: The build_products of this TaskInfoV4VoReq.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.BuildProduct`]
        """
        return self._build_products

    @build_products.setter
    def build_products(self, build_products):
        r"""Sets the build_products of this TaskInfoV4VoReq.

        流水线启动测试套件，携带构建产物

        :param build_products: The build_products of this TaskInfoV4VoReq.
        :type build_products: list[:class:`huaweicloudsdkcloudtest.v1.BuildProduct`]
        """
        self._build_products = build_products

    @property
    def case_package_env_name(self):
        r"""Gets the case_package_env_name of this TaskInfoV4VoReq.

        用例环境参数

        :return: The case_package_env_name of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._case_package_env_name

    @case_package_env_name.setter
    def case_package_env_name(self, case_package_env_name):
        r"""Sets the case_package_env_name of this TaskInfoV4VoReq.

        用例环境参数

        :param case_package_env_name: The case_package_env_name of this TaskInfoV4VoReq.
        :type case_package_env_name: str
        """
        self._case_package_env_name = case_package_env_name

    @property
    def case_package_id(self):
        r"""Gets the case_package_id of this TaskInfoV4VoReq.

        用例包ID

        :return: The case_package_id of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._case_package_id

    @case_package_id.setter
    def case_package_id(self, case_package_id):
        r"""Sets the case_package_id of this TaskInfoV4VoReq.

        用例包ID

        :param case_package_id: The case_package_id of this TaskInfoV4VoReq.
        :type case_package_id: str
        """
        self._case_package_id = case_package_id

    @property
    def case_package_name(self):
        r"""Gets the case_package_name of this TaskInfoV4VoReq.

        用例包名

        :return: The case_package_name of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._case_package_name

    @case_package_name.setter
    def case_package_name(self, case_package_name):
        r"""Sets the case_package_name of this TaskInfoV4VoReq.

        用例包名

        :param case_package_name: The case_package_name of this TaskInfoV4VoReq.
        :type case_package_name: str
        """
        self._case_package_name = case_package_name

    @property
    def case_total(self):
        r"""Gets the case_total of this TaskInfoV4VoReq.

        用例总数

        :return: The case_total of this TaskInfoV4VoReq.
        :rtype: int
        """
        return self._case_total

    @case_total.setter
    def case_total(self, case_total):
        r"""Sets the case_total of this TaskInfoV4VoReq.

        用例总数

        :param case_total: The case_total of this TaskInfoV4VoReq.
        :type case_total: int
        """
        self._case_total = case_total

    @property
    def client_type(self):
        r"""Gets the client_type of this TaskInfoV4VoReq.

        客户端类型，deviceTest使用

        :return: The client_type of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        r"""Sets the client_type of this TaskInfoV4VoReq.

        客户端类型，deviceTest使用

        :param client_type: The client_type of this TaskInfoV4VoReq.
        :type client_type: str
        """
        self._client_type = client_type

    @property
    def cloud_test_suite_basic_info(self):
        r"""Gets the cloud_test_suite_basic_info of this TaskInfoV4VoReq.

        :return: The cloud_test_suite_basic_info of this TaskInfoV4VoReq.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CloudTestSuiteBasicInfo`
        """
        return self._cloud_test_suite_basic_info

    @cloud_test_suite_basic_info.setter
    def cloud_test_suite_basic_info(self, cloud_test_suite_basic_info):
        r"""Sets the cloud_test_suite_basic_info of this TaskInfoV4VoReq.

        :param cloud_test_suite_basic_info: The cloud_test_suite_basic_info of this TaskInfoV4VoReq.
        :type cloud_test_suite_basic_info: :class:`huaweicloudsdkcloudtest.v1.CloudTestSuiteBasicInfo`
        """
        self._cloud_test_suite_basic_info = cloud_test_suite_basic_info

    @property
    def comments(self):
        r"""Gets the comments of this TaskInfoV4VoReq.

        :return: The comments of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        r"""Sets the comments of this TaskInfoV4VoReq.

        :param comments: The comments of this TaskInfoV4VoReq.
        :type comments: str
        """
        self._comments = comments

    @property
    def create_time(self):
        r"""Gets the create_time of this TaskInfoV4VoReq.

        创建时间

        :return: The create_time of this TaskInfoV4VoReq.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TaskInfoV4VoReq.

        创建时间

        :param create_time: The create_time of this TaskInfoV4VoReq.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def create_user(self):
        r"""Gets the create_user of this TaskInfoV4VoReq.

        创建人

        :return: The create_user of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this TaskInfoV4VoReq.

        创建人

        :param create_user: The create_user of this TaskInfoV4VoReq.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def env_type(self):
        r"""Gets the env_type of this TaskInfoV4VoReq.

        环境类型：0表示用例包环境，1表示全局环境

        :return: The env_type of this TaskInfoV4VoReq.
        :rtype: int
        """
        return self._env_type

    @env_type.setter
    def env_type(self, env_type):
        r"""Sets the env_type of this TaskInfoV4VoReq.

        环境类型：0表示用例包环境，1表示全局环境

        :param env_type: The env_type of this TaskInfoV4VoReq.
        :type env_type: int
        """
        self._env_type = env_type

    @property
    def environment_group_id(self):
        r"""Gets the environment_group_id of this TaskInfoV4VoReq.

        environmentId环境信息

        :return: The environment_group_id of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._environment_group_id

    @environment_group_id.setter
    def environment_group_id(self, environment_group_id):
        r"""Sets the environment_group_id of this TaskInfoV4VoReq.

        environmentId环境信息

        :param environment_group_id: The environment_group_id of this TaskInfoV4VoReq.
        :type environment_group_id: str
        """
        self._environment_group_id = environment_group_id

    @property
    def execute_strategies(self):
        r"""Gets the execute_strategies of this TaskInfoV4VoReq.

        :return: The execute_strategies of this TaskInfoV4VoReq.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ExecuteStrategiesVo`
        """
        return self._execute_strategies

    @execute_strategies.setter
    def execute_strategies(self, execute_strategies):
        r"""Sets the execute_strategies of this TaskInfoV4VoReq.

        :param execute_strategies: The execute_strategies of this TaskInfoV4VoReq.
        :type execute_strategies: :class:`huaweicloudsdkcloudtest.v1.ExecuteStrategiesVo`
        """
        self._execute_strategies = execute_strategies

    @property
    def executor_type(self):
        r"""Gets the executor_type of this TaskInfoV4VoReq.

        用例类型

        :return: The executor_type of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._executor_type

    @executor_type.setter
    def executor_type(self, executor_type):
        r"""Sets the executor_type of this TaskInfoV4VoReq.

        用例类型

        :param executor_type: The executor_type of this TaskInfoV4VoReq.
        :type executor_type: str
        """
        self._executor_type = executor_type

    @property
    def ext_params(self):
        r"""Gets the ext_params of this TaskInfoV4VoReq.

        扩展参数

        :return: The ext_params of this TaskInfoV4VoReq.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TaskExtParam`]
        """
        return self._ext_params

    @ext_params.setter
    def ext_params(self, ext_params):
        r"""Sets the ext_params of this TaskInfoV4VoReq.

        扩展参数

        :param ext_params: The ext_params of this TaskInfoV4VoReq.
        :type ext_params: list[:class:`huaweicloudsdkcloudtest.v1.TaskExtParam`]
        """
        self._ext_params = ext_params

    @property
    def favorite(self):
        r"""Gets the favorite of this TaskInfoV4VoReq.

        :return: The favorite of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        r"""Sets the favorite of this TaskInfoV4VoReq.

        :param favorite: The favorite of this TaskInfoV4VoReq.
        :type favorite: str
        """
        self._favorite = favorite

    @property
    def id(self):
        r"""Gets the id of this TaskInfoV4VoReq.

        唯一ID，主键

        :return: The id of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TaskInfoV4VoReq.

        唯一ID，主键

        :param id: The id of this TaskInfoV4VoReq.
        :type id: str
        """
        self._id = id

    @property
    def ip_group(self):
        r"""Gets the ip_group of this TaskInfoV4VoReq.

        :return: The ip_group of this TaskInfoV4VoReq.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.IpGroup`
        """
        return self._ip_group

    @ip_group.setter
    def ip_group(self, ip_group):
        r"""Sets the ip_group of this TaskInfoV4VoReq.

        :param ip_group: The ip_group of this TaskInfoV4VoReq.
        :type ip_group: :class:`huaweicloudsdkcloudtest.v1.IpGroup`
        """
        self._ip_group = ip_group

    @property
    def ip_key(self):
        r"""Gets the ip_key of this TaskInfoV4VoReq.

        小网拨测替换application的hostIP

        :return: The ip_key of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._ip_key

    @ip_key.setter
    def ip_key(self, ip_key):
        r"""Sets the ip_key of this TaskInfoV4VoReq.

        小网拨测替换application的hostIP

        :param ip_key: The ip_key of this TaskInfoV4VoReq.
        :type ip_key: str
        """
        self._ip_key = ip_key

    @property
    def is_debug_task(self):
        r"""Gets the is_debug_task of this TaskInfoV4VoReq.

        任务类型，是否debug任务

        :return: The is_debug_task of this TaskInfoV4VoReq.
        :rtype: int
        """
        return self._is_debug_task

    @is_debug_task.setter
    def is_debug_task(self, is_debug_task):
        r"""Sets the is_debug_task of this TaskInfoV4VoReq.

        任务类型，是否debug任务

        :param is_debug_task: The is_debug_task of this TaskInfoV4VoReq.
        :type is_debug_task: int
        """
        self._is_debug_task = is_debug_task

    @property
    def label(self):
        r"""Gets the label of this TaskInfoV4VoReq.

        执行标签

        :return: The label of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this TaskInfoV4VoReq.

        执行标签

        :param label: The label of this TaskInfoV4VoReq.
        :type label: str
        """
        self._label = label

    @property
    def label_name(self):
        r"""Gets the label_name of this TaskInfoV4VoReq.

        资源池名称

        :return: The label_name of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._label_name

    @label_name.setter
    def label_name(self, label_name):
        r"""Sets the label_name of this TaskInfoV4VoReq.

        资源池名称

        :param label_name: The label_name of this TaskInfoV4VoReq.
        :type label_name: str
        """
        self._label_name = label_name

    @property
    def label_type(self):
        r"""Gets the label_type of this TaskInfoV4VoReq.

        资源池类型

        :return: The label_type of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._label_type

    @label_type.setter
    def label_type(self, label_type):
        r"""Sets the label_type of this TaskInfoV4VoReq.

        资源池类型

        :param label_type: The label_type of this TaskInfoV4VoReq.
        :type label_type: str
        """
        self._label_type = label_type

    @property
    def last_stop_time(self):
        r"""Gets the last_stop_time of this TaskInfoV4VoReq.

        最近一次停止时间 

        :return: The last_stop_time of this TaskInfoV4VoReq.
        :rtype: int
        """
        return self._last_stop_time

    @last_stop_time.setter
    def last_stop_time(self, last_stop_time):
        r"""Sets the last_stop_time of this TaskInfoV4VoReq.

        最近一次停止时间 

        :param last_stop_time: The last_stop_time of this TaskInfoV4VoReq.
        :type last_stop_time: int
        """
        self._last_stop_time = last_stop_time

    @property
    def location_ids(self):
        r"""Gets the location_ids of this TaskInfoV4VoReq.

        执行区域，冗余处理，修改更新在执行配置字段

        :return: The location_ids of this TaskInfoV4VoReq.
        :rtype: list[str]
        """
        return self._location_ids

    @location_ids.setter
    def location_ids(self, location_ids):
        r"""Sets the location_ids of this TaskInfoV4VoReq.

        执行区域，冗余处理，修改更新在执行配置字段

        :param location_ids: The location_ids of this TaskInfoV4VoReq.
        :type location_ids: list[str]
        """
        self._location_ids = location_ids

    @property
    def name(self):
        r"""Gets the name of this TaskInfoV4VoReq.

        任务名

        :return: The name of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TaskInfoV4VoReq.

        任务名

        :param name: The name of this TaskInfoV4VoReq.
        :type name: str
        """
        self._name = name

    @property
    def plan_id(self):
        r"""Gets the plan_id of this TaskInfoV4VoReq.

        测试计划Id

        :return: The plan_id of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this TaskInfoV4VoReq.

        测试计划Id

        :param plan_id: The plan_id of this TaskInfoV4VoReq.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def pre_test_case_info(self):
        r"""Gets the pre_test_case_info of this TaskInfoV4VoReq.

        :return: The pre_test_case_info of this TaskInfoV4VoReq.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.PreTestCaseInfo`
        """
        return self._pre_test_case_info

    @pre_test_case_info.setter
    def pre_test_case_info(self, pre_test_case_info):
        r"""Sets the pre_test_case_info of this TaskInfoV4VoReq.

        :param pre_test_case_info: The pre_test_case_info of this TaskInfoV4VoReq.
        :type pre_test_case_info: :class:`huaweicloudsdkcloudtest.v1.PreTestCaseInfo`
        """
        self._pre_test_case_info = pre_test_case_info

    @property
    def resource_pool(self):
        r"""Gets the resource_pool of this TaskInfoV4VoReq.

        :return: The resource_pool of this TaskInfoV4VoReq.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ResourcePool`
        """
        return self._resource_pool

    @resource_pool.setter
    def resource_pool(self, resource_pool):
        r"""Sets the resource_pool of this TaskInfoV4VoReq.

        :param resource_pool: The resource_pool of this TaskInfoV4VoReq.
        :type resource_pool: :class:`huaweicloudsdkcloudtest.v1.ResourcePool`
        """
        self._resource_pool = resource_pool

    @property
    def state(self):
        r"""Gets the state of this TaskInfoV4VoReq.

        任务状态

        :return: The state of this TaskInfoV4VoReq.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this TaskInfoV4VoReq.

        任务状态

        :param state: The state of this TaskInfoV4VoReq.
        :type state: int
        """
        self._state = state

    @property
    def subtask_id(self):
        r"""Gets the subtask_id of this TaskInfoV4VoReq.

        :return: The subtask_id of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._subtask_id

    @subtask_id.setter
    def subtask_id(self, subtask_id):
        r"""Sets the subtask_id of this TaskInfoV4VoReq.

        :param subtask_id: The subtask_id of this TaskInfoV4VoReq.
        :type subtask_id: str
        """
        self._subtask_id = subtask_id

    @property
    def subtask_total(self):
        r"""Gets the subtask_total of this TaskInfoV4VoReq.

        子任务总数

        :return: The subtask_total of this TaskInfoV4VoReq.
        :rtype: int
        """
        return self._subtask_total

    @subtask_total.setter
    def subtask_total(self, subtask_total):
        r"""Sets the subtask_total of this TaskInfoV4VoReq.

        子任务总数

        :param subtask_total: The subtask_total of this TaskInfoV4VoReq.
        :type subtask_total: int
        """
        self._subtask_total = subtask_total

    @property
    def task_type_id(self):
        r"""Gets the task_type_id of this TaskInfoV4VoReq.

        任务类型

        :return: The task_type_id of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._task_type_id

    @task_type_id.setter
    def task_type_id(self, task_type_id):
        r"""Sets the task_type_id of this TaskInfoV4VoReq.

        任务类型

        :param task_type_id: The task_type_id of this TaskInfoV4VoReq.
        :type task_type_id: str
        """
        self._task_type_id = task_type_id

    @property
    def test_cases(self):
        r"""Gets the test_cases of this TaskInfoV4VoReq.

        测试用例列表

        :return: The test_cases of this TaskInfoV4VoReq.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseBasicInfo`]
        """
        return self._test_cases

    @test_cases.setter
    def test_cases(self, test_cases):
        r"""Sets the test_cases of this TaskInfoV4VoReq.

        测试用例列表

        :param test_cases: The test_cases of this TaskInfoV4VoReq.
        :type test_cases: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseBasicInfo`]
        """
        self._test_cases = test_cases

    @property
    def test_service_id(self):
        r"""Gets the test_service_id of this TaskInfoV4VoReq.

        项目id

        :return: The test_service_id of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._test_service_id

    @test_service_id.setter
    def test_service_id(self, test_service_id):
        r"""Sets the test_service_id of this TaskInfoV4VoReq.

        项目id

        :param test_service_id: The test_service_id of this TaskInfoV4VoReq.
        :type test_service_id: str
        """
        self._test_service_id = test_service_id

    @property
    def test_suite_type(self):
        r"""Gets the test_suite_type of this TaskInfoV4VoReq.

        测试套类型

        :return: The test_suite_type of this TaskInfoV4VoReq.
        :rtype: int
        """
        return self._test_suite_type

    @test_suite_type.setter
    def test_suite_type(self, test_suite_type):
        r"""Sets the test_suite_type of this TaskInfoV4VoReq.

        测试套类型

        :param test_suite_type: The test_suite_type of this TaskInfoV4VoReq.
        :type test_suite_type: int
        """
        self._test_suite_type = test_suite_type

    @property
    def tip(self):
        r"""Gets the tip of this TaskInfoV4VoReq.

        提示信息，用于任务操作过程中需要提供给前端的提示信息

        :return: The tip of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._tip

    @tip.setter
    def tip(self, tip):
        r"""Sets the tip of this TaskInfoV4VoReq.

        提示信息，用于任务操作过程中需要提供给前端的提示信息

        :param tip: The tip of this TaskInfoV4VoReq.
        :type tip: str
        """
        self._tip = tip

    @property
    def update_time(self):
        r"""Gets the update_time of this TaskInfoV4VoReq.

        创建时间

        :return: The update_time of this TaskInfoV4VoReq.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TaskInfoV4VoReq.

        创建时间

        :param update_time: The update_time of this TaskInfoV4VoReq.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def update_user(self):
        r"""Gets the update_user of this TaskInfoV4VoReq.

        更新人

        :return: The update_user of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this TaskInfoV4VoReq.

        更新人

        :param update_user: The update_user of this TaskInfoV4VoReq.
        :type update_user: str
        """
        self._update_user = update_user

    @property
    def version(self):
        r"""Gets the version of this TaskInfoV4VoReq.

        版本

        :return: The version of this TaskInfoV4VoReq.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this TaskInfoV4VoReq.

        版本

        :param version: The version of this TaskInfoV4VoReq.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, TaskInfoV4VoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
