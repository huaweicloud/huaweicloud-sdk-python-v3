# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudTestSuiteBasicInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_operation_info': 'CloudTestCaseOperationInfo',
        'create_time': 'str',
        'create_user': 'str',
        'create_user_id': 'str',
        'description': 'str',
        'doc_type': 'int',
        'execute_status': 'int',
        'execute_times': 'int',
        'execute_type': 'int',
        'execute_way': 'str',
        'expiration_status': 'int',
        'ext_param': 'str',
        'id': 'str',
        'iterator_version_uri': 'str',
        'module_id': 'str',
        'module_name': 'str',
        'name': 'str',
        'node_id': 'str',
        'owner_id': 'str',
        'plan_id': 'str',
        'plan_end_timestamp': 'int',
        'plan_start_timestamp': 'int',
        'project_id': 'int',
        'project_uu_id': 'str',
        'release_dev': 'str',
        'result': 'int',
        'status': 'int',
        'tags': 'list[str]',
        'test_suite_id': 'str',
        'test_suite_number': 'str',
        'type': 'int',
        'update_time': 'str',
        'update_user': 'str',
        'update_user_id': 'str'
    }

    attribute_map = {
        'case_operation_info': 'caseOperationInfo',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'create_user_id': 'create_user_id',
        'description': 'description',
        'doc_type': 'doc_type',
        'execute_status': 'execute_status',
        'execute_times': 'execute_times',
        'execute_type': 'execute_type',
        'execute_way': 'execute_way',
        'expiration_status': 'expiration_status',
        'ext_param': 'extParam',
        'id': 'id',
        'iterator_version_uri': 'iterator_version_uri',
        'module_id': 'moduleId',
        'module_name': 'moduleName',
        'name': 'name',
        'node_id': 'nodeId',
        'owner_id': 'ownerId',
        'plan_id': 'planId',
        'plan_end_timestamp': 'plan_end_timestamp',
        'plan_start_timestamp': 'plan_start_timestamp',
        'project_id': 'projectId',
        'project_uu_id': 'projectUUId',
        'release_dev': 'releaseDev',
        'result': 'result',
        'status': 'status',
        'tags': 'tags',
        'test_suite_id': 'testSuiteId',
        'test_suite_number': 'testSuiteNumber',
        'type': 'type',
        'update_time': 'update_time',
        'update_user': 'update_user',
        'update_user_id': 'update_user_id'
    }

    def __init__(self, case_operation_info=None, create_time=None, create_user=None, create_user_id=None, description=None, doc_type=None, execute_status=None, execute_times=None, execute_type=None, execute_way=None, expiration_status=None, ext_param=None, id=None, iterator_version_uri=None, module_id=None, module_name=None, name=None, node_id=None, owner_id=None, plan_id=None, plan_end_timestamp=None, plan_start_timestamp=None, project_id=None, project_uu_id=None, release_dev=None, result=None, status=None, tags=None, test_suite_id=None, test_suite_number=None, type=None, update_time=None, update_user=None, update_user_id=None):
        r"""CloudTestSuiteBasicInfo

        The model defined in huaweicloud sdk

        :param case_operation_info: 
        :type case_operation_info: :class:`huaweicloudsdkcloudtest.v1.CloudTestCaseOperationInfo`
        :param create_time: 创建时间
        :type create_time: str
        :param create_user: 创建人
        :type create_user: str
        :param create_user_id: 创建人ID
        :type create_user_id: str
        :param description: 描述信息
        :type description: str
        :param doc_type: 数据类型：0为测试套，1为文件夹，cloudTest前台传入
        :type doc_type: int
        :param execute_status: 测试套状态
        :type execute_status: int
        :param execute_times: 执行总次数
        :type execute_times: int
        :param execute_type: 执行类型：0为冒烟测试，1为定时执行
        :type execute_type: int
        :param execute_way: 执行方式：1为串行，2为并行，与echo的executeModel字段相同
        :type execute_way: str
        :param expiration_status: 测试套超期状态
        :type expiration_status: int
        :param ext_param: 参数配置
        :type ext_param: str
        :param id: 唯一ID，主键
        :type id: str
        :param iterator_version_uri: 测试计划Uri，TMSS需要此值
        :type iterator_version_uri: str
        :param module_id: 模块Id
        :type module_id: str
        :param module_name: 模块名称
        :type module_name: str
        :param name: 测试套名称，与echo的name字段相同
        :type name: str
        :param node_id: 目录Id
        :type node_id: str
        :param owner_id: 处理者ID
        :type owner_id: str
        :param plan_id: 测试计划id，可为空
        :type plan_id: str
        :param plan_end_timestamp: 计划结束时间
        :type plan_end_timestamp: int
        :param plan_start_timestamp: 计划开始时间
        :type plan_start_timestamp: int
        :param project_id: 项目ID
        :type project_id: int
        :param project_uu_id: 项目UUID，与echo的testServiceId字段相同
        :type project_uu_id: str
        :param release_dev: 版本号
        :type release_dev: str
        :param result: 测试套执行结果
        :type result: int
        :param status: 测试套状态
        :type status: int
        :param tags: 标签
        :type tags: list[str]
        :param test_suite_id: 测试套id，更新时需要同时传id、testSuiteId，2个字段值相同，与echo的taskId字段相同
        :type test_suite_id: str
        :param test_suite_number: 编号
        :type test_suite_number: str
        :param type: 测试套类型：0为功能测试，1为接口测试，6为Pistar，cloudTest前台传入
        :type type: int
        :param update_time: 更新时间
        :type update_time: str
        :param update_user: 更新人
        :type update_user: str
        :param update_user_id: 更新人ID
        :type update_user_id: str
        """
        
        

        self._case_operation_info = None
        self._create_time = None
        self._create_user = None
        self._create_user_id = None
        self._description = None
        self._doc_type = None
        self._execute_status = None
        self._execute_times = None
        self._execute_type = None
        self._execute_way = None
        self._expiration_status = None
        self._ext_param = None
        self._id = None
        self._iterator_version_uri = None
        self._module_id = None
        self._module_name = None
        self._name = None
        self._node_id = None
        self._owner_id = None
        self._plan_id = None
        self._plan_end_timestamp = None
        self._plan_start_timestamp = None
        self._project_id = None
        self._project_uu_id = None
        self._release_dev = None
        self._result = None
        self._status = None
        self._tags = None
        self._test_suite_id = None
        self._test_suite_number = None
        self._type = None
        self._update_time = None
        self._update_user = None
        self._update_user_id = None
        self.discriminator = None

        if case_operation_info is not None:
            self.case_operation_info = case_operation_info
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if create_user_id is not None:
            self.create_user_id = create_user_id
        if description is not None:
            self.description = description
        if doc_type is not None:
            self.doc_type = doc_type
        if execute_status is not None:
            self.execute_status = execute_status
        if execute_times is not None:
            self.execute_times = execute_times
        if execute_type is not None:
            self.execute_type = execute_type
        if execute_way is not None:
            self.execute_way = execute_way
        if expiration_status is not None:
            self.expiration_status = expiration_status
        if ext_param is not None:
            self.ext_param = ext_param
        if id is not None:
            self.id = id
        if iterator_version_uri is not None:
            self.iterator_version_uri = iterator_version_uri
        if module_id is not None:
            self.module_id = module_id
        if module_name is not None:
            self.module_name = module_name
        if name is not None:
            self.name = name
        if node_id is not None:
            self.node_id = node_id
        if owner_id is not None:
            self.owner_id = owner_id
        if plan_id is not None:
            self.plan_id = plan_id
        if plan_end_timestamp is not None:
            self.plan_end_timestamp = plan_end_timestamp
        if plan_start_timestamp is not None:
            self.plan_start_timestamp = plan_start_timestamp
        if project_id is not None:
            self.project_id = project_id
        if project_uu_id is not None:
            self.project_uu_id = project_uu_id
        if release_dev is not None:
            self.release_dev = release_dev
        if result is not None:
            self.result = result
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if test_suite_id is not None:
            self.test_suite_id = test_suite_id
        if test_suite_number is not None:
            self.test_suite_number = test_suite_number
        if type is not None:
            self.type = type
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user
        if update_user_id is not None:
            self.update_user_id = update_user_id

    @property
    def case_operation_info(self):
        r"""Gets the case_operation_info of this CloudTestSuiteBasicInfo.

        :return: The case_operation_info of this CloudTestSuiteBasicInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CloudTestCaseOperationInfo`
        """
        return self._case_operation_info

    @case_operation_info.setter
    def case_operation_info(self, case_operation_info):
        r"""Sets the case_operation_info of this CloudTestSuiteBasicInfo.

        :param case_operation_info: The case_operation_info of this CloudTestSuiteBasicInfo.
        :type case_operation_info: :class:`huaweicloudsdkcloudtest.v1.CloudTestCaseOperationInfo`
        """
        self._case_operation_info = case_operation_info

    @property
    def create_time(self):
        r"""Gets the create_time of this CloudTestSuiteBasicInfo.

        创建时间

        :return: The create_time of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CloudTestSuiteBasicInfo.

        创建时间

        :param create_time: The create_time of this CloudTestSuiteBasicInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def create_user(self):
        r"""Gets the create_user of this CloudTestSuiteBasicInfo.

        创建人

        :return: The create_user of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this CloudTestSuiteBasicInfo.

        创建人

        :param create_user: The create_user of this CloudTestSuiteBasicInfo.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def create_user_id(self):
        r"""Gets the create_user_id of this CloudTestSuiteBasicInfo.

        创建人ID

        :return: The create_user_id of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, create_user_id):
        r"""Sets the create_user_id of this CloudTestSuiteBasicInfo.

        创建人ID

        :param create_user_id: The create_user_id of this CloudTestSuiteBasicInfo.
        :type create_user_id: str
        """
        self._create_user_id = create_user_id

    @property
    def description(self):
        r"""Gets the description of this CloudTestSuiteBasicInfo.

        描述信息

        :return: The description of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CloudTestSuiteBasicInfo.

        描述信息

        :param description: The description of this CloudTestSuiteBasicInfo.
        :type description: str
        """
        self._description = description

    @property
    def doc_type(self):
        r"""Gets the doc_type of this CloudTestSuiteBasicInfo.

        数据类型：0为测试套，1为文件夹，cloudTest前台传入

        :return: The doc_type of this CloudTestSuiteBasicInfo.
        :rtype: int
        """
        return self._doc_type

    @doc_type.setter
    def doc_type(self, doc_type):
        r"""Sets the doc_type of this CloudTestSuiteBasicInfo.

        数据类型：0为测试套，1为文件夹，cloudTest前台传入

        :param doc_type: The doc_type of this CloudTestSuiteBasicInfo.
        :type doc_type: int
        """
        self._doc_type = doc_type

    @property
    def execute_status(self):
        r"""Gets the execute_status of this CloudTestSuiteBasicInfo.

        测试套状态

        :return: The execute_status of this CloudTestSuiteBasicInfo.
        :rtype: int
        """
        return self._execute_status

    @execute_status.setter
    def execute_status(self, execute_status):
        r"""Sets the execute_status of this CloudTestSuiteBasicInfo.

        测试套状态

        :param execute_status: The execute_status of this CloudTestSuiteBasicInfo.
        :type execute_status: int
        """
        self._execute_status = execute_status

    @property
    def execute_times(self):
        r"""Gets the execute_times of this CloudTestSuiteBasicInfo.

        执行总次数

        :return: The execute_times of this CloudTestSuiteBasicInfo.
        :rtype: int
        """
        return self._execute_times

    @execute_times.setter
    def execute_times(self, execute_times):
        r"""Sets the execute_times of this CloudTestSuiteBasicInfo.

        执行总次数

        :param execute_times: The execute_times of this CloudTestSuiteBasicInfo.
        :type execute_times: int
        """
        self._execute_times = execute_times

    @property
    def execute_type(self):
        r"""Gets the execute_type of this CloudTestSuiteBasicInfo.

        执行类型：0为冒烟测试，1为定时执行

        :return: The execute_type of this CloudTestSuiteBasicInfo.
        :rtype: int
        """
        return self._execute_type

    @execute_type.setter
    def execute_type(self, execute_type):
        r"""Sets the execute_type of this CloudTestSuiteBasicInfo.

        执行类型：0为冒烟测试，1为定时执行

        :param execute_type: The execute_type of this CloudTestSuiteBasicInfo.
        :type execute_type: int
        """
        self._execute_type = execute_type

    @property
    def execute_way(self):
        r"""Gets the execute_way of this CloudTestSuiteBasicInfo.

        执行方式：1为串行，2为并行，与echo的executeModel字段相同

        :return: The execute_way of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._execute_way

    @execute_way.setter
    def execute_way(self, execute_way):
        r"""Sets the execute_way of this CloudTestSuiteBasicInfo.

        执行方式：1为串行，2为并行，与echo的executeModel字段相同

        :param execute_way: The execute_way of this CloudTestSuiteBasicInfo.
        :type execute_way: str
        """
        self._execute_way = execute_way

    @property
    def expiration_status(self):
        r"""Gets the expiration_status of this CloudTestSuiteBasicInfo.

        测试套超期状态

        :return: The expiration_status of this CloudTestSuiteBasicInfo.
        :rtype: int
        """
        return self._expiration_status

    @expiration_status.setter
    def expiration_status(self, expiration_status):
        r"""Sets the expiration_status of this CloudTestSuiteBasicInfo.

        测试套超期状态

        :param expiration_status: The expiration_status of this CloudTestSuiteBasicInfo.
        :type expiration_status: int
        """
        self._expiration_status = expiration_status

    @property
    def ext_param(self):
        r"""Gets the ext_param of this CloudTestSuiteBasicInfo.

        参数配置

        :return: The ext_param of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._ext_param

    @ext_param.setter
    def ext_param(self, ext_param):
        r"""Sets the ext_param of this CloudTestSuiteBasicInfo.

        参数配置

        :param ext_param: The ext_param of this CloudTestSuiteBasicInfo.
        :type ext_param: str
        """
        self._ext_param = ext_param

    @property
    def id(self):
        r"""Gets the id of this CloudTestSuiteBasicInfo.

        唯一ID，主键

        :return: The id of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CloudTestSuiteBasicInfo.

        唯一ID，主键

        :param id: The id of this CloudTestSuiteBasicInfo.
        :type id: str
        """
        self._id = id

    @property
    def iterator_version_uri(self):
        r"""Gets the iterator_version_uri of this CloudTestSuiteBasicInfo.

        测试计划Uri，TMSS需要此值

        :return: The iterator_version_uri of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._iterator_version_uri

    @iterator_version_uri.setter
    def iterator_version_uri(self, iterator_version_uri):
        r"""Sets the iterator_version_uri of this CloudTestSuiteBasicInfo.

        测试计划Uri，TMSS需要此值

        :param iterator_version_uri: The iterator_version_uri of this CloudTestSuiteBasicInfo.
        :type iterator_version_uri: str
        """
        self._iterator_version_uri = iterator_version_uri

    @property
    def module_id(self):
        r"""Gets the module_id of this CloudTestSuiteBasicInfo.

        模块Id

        :return: The module_id of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this CloudTestSuiteBasicInfo.

        模块Id

        :param module_id: The module_id of this CloudTestSuiteBasicInfo.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def module_name(self):
        r"""Gets the module_name of this CloudTestSuiteBasicInfo.

        模块名称

        :return: The module_name of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        r"""Sets the module_name of this CloudTestSuiteBasicInfo.

        模块名称

        :param module_name: The module_name of this CloudTestSuiteBasicInfo.
        :type module_name: str
        """
        self._module_name = module_name

    @property
    def name(self):
        r"""Gets the name of this CloudTestSuiteBasicInfo.

        测试套名称，与echo的name字段相同

        :return: The name of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CloudTestSuiteBasicInfo.

        测试套名称，与echo的name字段相同

        :param name: The name of this CloudTestSuiteBasicInfo.
        :type name: str
        """
        self._name = name

    @property
    def node_id(self):
        r"""Gets the node_id of this CloudTestSuiteBasicInfo.

        目录Id

        :return: The node_id of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this CloudTestSuiteBasicInfo.

        目录Id

        :param node_id: The node_id of this CloudTestSuiteBasicInfo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def owner_id(self):
        r"""Gets the owner_id of this CloudTestSuiteBasicInfo.

        处理者ID

        :return: The owner_id of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this CloudTestSuiteBasicInfo.

        处理者ID

        :param owner_id: The owner_id of this CloudTestSuiteBasicInfo.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def plan_id(self):
        r"""Gets the plan_id of this CloudTestSuiteBasicInfo.

        测试计划id，可为空

        :return: The plan_id of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this CloudTestSuiteBasicInfo.

        测试计划id，可为空

        :param plan_id: The plan_id of this CloudTestSuiteBasicInfo.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def plan_end_timestamp(self):
        r"""Gets the plan_end_timestamp of this CloudTestSuiteBasicInfo.

        计划结束时间

        :return: The plan_end_timestamp of this CloudTestSuiteBasicInfo.
        :rtype: int
        """
        return self._plan_end_timestamp

    @plan_end_timestamp.setter
    def plan_end_timestamp(self, plan_end_timestamp):
        r"""Sets the plan_end_timestamp of this CloudTestSuiteBasicInfo.

        计划结束时间

        :param plan_end_timestamp: The plan_end_timestamp of this CloudTestSuiteBasicInfo.
        :type plan_end_timestamp: int
        """
        self._plan_end_timestamp = plan_end_timestamp

    @property
    def plan_start_timestamp(self):
        r"""Gets the plan_start_timestamp of this CloudTestSuiteBasicInfo.

        计划开始时间

        :return: The plan_start_timestamp of this CloudTestSuiteBasicInfo.
        :rtype: int
        """
        return self._plan_start_timestamp

    @plan_start_timestamp.setter
    def plan_start_timestamp(self, plan_start_timestamp):
        r"""Sets the plan_start_timestamp of this CloudTestSuiteBasicInfo.

        计划开始时间

        :param plan_start_timestamp: The plan_start_timestamp of this CloudTestSuiteBasicInfo.
        :type plan_start_timestamp: int
        """
        self._plan_start_timestamp = plan_start_timestamp

    @property
    def project_id(self):
        r"""Gets the project_id of this CloudTestSuiteBasicInfo.

        项目ID

        :return: The project_id of this CloudTestSuiteBasicInfo.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CloudTestSuiteBasicInfo.

        项目ID

        :param project_id: The project_id of this CloudTestSuiteBasicInfo.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def project_uu_id(self):
        r"""Gets the project_uu_id of this CloudTestSuiteBasicInfo.

        项目UUID，与echo的testServiceId字段相同

        :return: The project_uu_id of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._project_uu_id

    @project_uu_id.setter
    def project_uu_id(self, project_uu_id):
        r"""Sets the project_uu_id of this CloudTestSuiteBasicInfo.

        项目UUID，与echo的testServiceId字段相同

        :param project_uu_id: The project_uu_id of this CloudTestSuiteBasicInfo.
        :type project_uu_id: str
        """
        self._project_uu_id = project_uu_id

    @property
    def release_dev(self):
        r"""Gets the release_dev of this CloudTestSuiteBasicInfo.

        版本号

        :return: The release_dev of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        r"""Sets the release_dev of this CloudTestSuiteBasicInfo.

        版本号

        :param release_dev: The release_dev of this CloudTestSuiteBasicInfo.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def result(self):
        r"""Gets the result of this CloudTestSuiteBasicInfo.

        测试套执行结果

        :return: The result of this CloudTestSuiteBasicInfo.
        :rtype: int
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this CloudTestSuiteBasicInfo.

        测试套执行结果

        :param result: The result of this CloudTestSuiteBasicInfo.
        :type result: int
        """
        self._result = result

    @property
    def status(self):
        r"""Gets the status of this CloudTestSuiteBasicInfo.

        测试套状态

        :return: The status of this CloudTestSuiteBasicInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CloudTestSuiteBasicInfo.

        测试套状态

        :param status: The status of this CloudTestSuiteBasicInfo.
        :type status: int
        """
        self._status = status

    @property
    def tags(self):
        r"""Gets the tags of this CloudTestSuiteBasicInfo.

        标签

        :return: The tags of this CloudTestSuiteBasicInfo.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CloudTestSuiteBasicInfo.

        标签

        :param tags: The tags of this CloudTestSuiteBasicInfo.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def test_suite_id(self):
        r"""Gets the test_suite_id of this CloudTestSuiteBasicInfo.

        测试套id，更新时需要同时传id、testSuiteId，2个字段值相同，与echo的taskId字段相同

        :return: The test_suite_id of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._test_suite_id

    @test_suite_id.setter
    def test_suite_id(self, test_suite_id):
        r"""Sets the test_suite_id of this CloudTestSuiteBasicInfo.

        测试套id，更新时需要同时传id、testSuiteId，2个字段值相同，与echo的taskId字段相同

        :param test_suite_id: The test_suite_id of this CloudTestSuiteBasicInfo.
        :type test_suite_id: str
        """
        self._test_suite_id = test_suite_id

    @property
    def test_suite_number(self):
        r"""Gets the test_suite_number of this CloudTestSuiteBasicInfo.

        编号

        :return: The test_suite_number of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._test_suite_number

    @test_suite_number.setter
    def test_suite_number(self, test_suite_number):
        r"""Sets the test_suite_number of this CloudTestSuiteBasicInfo.

        编号

        :param test_suite_number: The test_suite_number of this CloudTestSuiteBasicInfo.
        :type test_suite_number: str
        """
        self._test_suite_number = test_suite_number

    @property
    def type(self):
        r"""Gets the type of this CloudTestSuiteBasicInfo.

        测试套类型：0为功能测试，1为接口测试，6为Pistar，cloudTest前台传入

        :return: The type of this CloudTestSuiteBasicInfo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CloudTestSuiteBasicInfo.

        测试套类型：0为功能测试，1为接口测试，6为Pistar，cloudTest前台传入

        :param type: The type of this CloudTestSuiteBasicInfo.
        :type type: int
        """
        self._type = type

    @property
    def update_time(self):
        r"""Gets the update_time of this CloudTestSuiteBasicInfo.

        更新时间

        :return: The update_time of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CloudTestSuiteBasicInfo.

        更新时间

        :param update_time: The update_time of this CloudTestSuiteBasicInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def update_user(self):
        r"""Gets the update_user of this CloudTestSuiteBasicInfo.

        更新人

        :return: The update_user of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this CloudTestSuiteBasicInfo.

        更新人

        :param update_user: The update_user of this CloudTestSuiteBasicInfo.
        :type update_user: str
        """
        self._update_user = update_user

    @property
    def update_user_id(self):
        r"""Gets the update_user_id of this CloudTestSuiteBasicInfo.

        更新人ID

        :return: The update_user_id of this CloudTestSuiteBasicInfo.
        :rtype: str
        """
        return self._update_user_id

    @update_user_id.setter
    def update_user_id(self, update_user_id):
        r"""Sets the update_user_id of this CloudTestSuiteBasicInfo.

        更新人ID

        :param update_user_id: The update_user_id of this CloudTestSuiteBasicInfo.
        :type update_user_id: str
        """
        self._update_user_id = update_user_id

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
        if not isinstance(other, CloudTestSuiteBasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
