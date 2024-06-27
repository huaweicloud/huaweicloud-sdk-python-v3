# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskVo:

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
        'name': 'str',
        'stage': 'str',
        'number': 'str',
        'tags': 'str',
        'description': 'str',
        'region': 'str',
        'author_id': 'str',
        'author_name': 'str',
        'owner_id': 'str',
        'owner_name': 'str',
        'parent_uri': 'str',
        'parent_path': 'str',
        'origin_uri': 'str',
        'version_uri': 'str',
        'branch_uri': 'str',
        'version_name': 'str',
        'creation_date': 'datetime',
        'create_date_timestamp': 'int',
        'update_time': 'datetime',
        'update_time_timestamp': 'int',
        'relation_change_time': 'datetime',
        'relation_change_time_timestamp': 'int',
        'test_case_condition': 'str',
        'updator_id': 'str',
        'updator_name': 'str',
        'relation_changer_id': 'str',
        'service_type': 'int',
        'service_type_name': 'str',
        'tag_list': 'list[str]',
        'module_id': 'str',
        'module_name': 'str',
        'module_path': 'str',
        'module_path_name': 'str',
        'release_dev': 'str',
        'ext_param': 'str',
        'execute_way': 'int',
        'execute_type': 'int',
        'status_code': 'int',
        'status_name': 'str',
        'result_code': 'int',
        'result_name': 'str',
        'execute_status_code': 'int',
        'execute_status_name': 'str',
        'executor_id': 'str',
        'executor_name': 'str',
        'execute_latest_time': 'datetime',
        'execute_latest_time_timestamp': 'int',
        'execute_duration': 'str',
        'execute_times': 'int',
        'project_uuid': 'str',
        'case_operation_info': 'CaseOperationVo',
        'assign_case_num': 'int',
        'finish_case_num': 'int',
        'assign_defect_num': 'int',
        'task_assign_msg': 'str',
        'iterator_version_uri': 'str',
        'result_number_list': 'list[NameAndValueAndCodeVo]',
        'finish_date': 'datetime',
        'finish_date_timestamp': 'int',
        'plan_start_date': 'datetime',
        'plan_start_timestamp': 'int',
        'plan_end_date': 'datetime',
        'plan_end_timestamp': 'int',
        'expiration_status': 'int',
        'expiration_status_name': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'stage': 'stage',
        'number': 'number',
        'tags': 'tags',
        'description': 'description',
        'region': 'region',
        'author_id': 'author_id',
        'author_name': 'author_name',
        'owner_id': 'owner_id',
        'owner_name': 'owner_name',
        'parent_uri': 'parent_uri',
        'parent_path': 'parent_path',
        'origin_uri': 'origin_uri',
        'version_uri': 'version_uri',
        'branch_uri': 'branch_uri',
        'version_name': 'version_name',
        'creation_date': 'creation_date',
        'create_date_timestamp': 'create_date_timestamp',
        'update_time': 'update_time',
        'update_time_timestamp': 'update_time_timestamp',
        'relation_change_time': 'relation_change_time',
        'relation_change_time_timestamp': 'relation_change_time_timestamp',
        'test_case_condition': 'test_case_condition',
        'updator_id': 'updator_id',
        'updator_name': 'updator_name',
        'relation_changer_id': 'relation_changer_id',
        'service_type': 'service_type',
        'service_type_name': 'service_type_name',
        'tag_list': 'tag_list',
        'module_id': 'module_id',
        'module_name': 'module_name',
        'module_path': 'module_path',
        'module_path_name': 'module_path_name',
        'release_dev': 'release_dev',
        'ext_param': 'ext_param',
        'execute_way': 'execute_way',
        'execute_type': 'execute_type',
        'status_code': 'status_code',
        'status_name': 'status_name',
        'result_code': 'result_code',
        'result_name': 'result_name',
        'execute_status_code': 'execute_status_code',
        'execute_status_name': 'execute_status_name',
        'executor_id': 'executor_id',
        'executor_name': 'executor_name',
        'execute_latest_time': 'execute_latest_time',
        'execute_latest_time_timestamp': 'execute_latest_time_timestamp',
        'execute_duration': 'execute_duration',
        'execute_times': 'execute_times',
        'project_uuid': 'project_uuid',
        'case_operation_info': 'case_operation_info',
        'assign_case_num': 'assign_case_num',
        'finish_case_num': 'finish_case_num',
        'assign_defect_num': 'assign_defect_num',
        'task_assign_msg': 'task_assign_msg',
        'iterator_version_uri': 'iterator_version_uri',
        'result_number_list': 'result_number_list',
        'finish_date': 'finish_date',
        'finish_date_timestamp': 'finish_date_timestamp',
        'plan_start_date': 'plan_start_date',
        'plan_start_timestamp': 'plan_start_timestamp',
        'plan_end_date': 'plan_end_date',
        'plan_end_timestamp': 'plan_end_timestamp',
        'expiration_status': 'expiration_status',
        'expiration_status_name': 'expiration_status_name'
    }

    def __init__(self, uri=None, name=None, stage=None, number=None, tags=None, description=None, region=None, author_id=None, author_name=None, owner_id=None, owner_name=None, parent_uri=None, parent_path=None, origin_uri=None, version_uri=None, branch_uri=None, version_name=None, creation_date=None, create_date_timestamp=None, update_time=None, update_time_timestamp=None, relation_change_time=None, relation_change_time_timestamp=None, test_case_condition=None, updator_id=None, updator_name=None, relation_changer_id=None, service_type=None, service_type_name=None, tag_list=None, module_id=None, module_name=None, module_path=None, module_path_name=None, release_dev=None, ext_param=None, execute_way=None, execute_type=None, status_code=None, status_name=None, result_code=None, result_name=None, execute_status_code=None, execute_status_name=None, executor_id=None, executor_name=None, execute_latest_time=None, execute_latest_time_timestamp=None, execute_duration=None, execute_times=None, project_uuid=None, case_operation_info=None, assign_case_num=None, finish_case_num=None, assign_defect_num=None, task_assign_msg=None, iterator_version_uri=None, result_number_list=None, finish_date=None, finish_date_timestamp=None, plan_start_date=None, plan_start_timestamp=None, plan_end_date=None, plan_end_timestamp=None, expiration_status=None, expiration_status_name=None):
        """TaskVo

        The model defined in huaweicloud sdk

        :param uri: 测试任务URI
        :type uri: str
        :param name: 测试任务名称
        :type name: str
        :param stage: 测试阶段
        :type stage: str
        :param number: 编号
        :type number: str
        :param tags: 标签
        :type tags: str
        :param description: 描述
        :type description: str
        :param region: 区域
        :type region: str
        :param author_id: 创建人ID
        :type author_id: str
        :param author_name: 创建人名称
        :type author_name: str
        :param owner_id: 责任人ID
        :type owner_id: str
        :param owner_name: 责任人名称
        :type owner_name: str
        :param parent_uri: 父任务URI
        :type parent_uri: str
        :param parent_path: 父任务路径
        :type parent_path: str
        :param origin_uri: 源任务URI
        :type origin_uri: str
        :param version_uri: 版本URI
        :type version_uri: str
        :param branch_uri: 分支URI
        :type branch_uri: str
        :param version_name: 版本名称
        :type version_name: str
        :param creation_date: 创建时间
        :type creation_date: datetime
        :param create_date_timestamp: 创建时间时间戳
        :type create_date_timestamp: int
        :param update_time: 更新时间
        :type update_time: datetime
        :param update_time_timestamp: 更新时间时间戳
        :type update_time_timestamp: int
        :param relation_change_time: 关联关系修改时时间
        :type relation_change_time: datetime
        :param relation_change_time_timestamp: 关联关系修改时间时间戳
        :type relation_change_time_timestamp: int
        :param test_case_condition: 动态任务用例过滤条件
        :type test_case_condition: str
        :param updator_id: 修改人Id
        :type updator_id: str
        :param updator_name: 修改人名称
        :type updator_name: str
        :param relation_changer_id: 关联关系修改人Id
        :type relation_changer_id: str
        :param service_type: 服务类型ID
        :type service_type: int
        :param service_type_name: 服务类型名称
        :type service_type_name: str
        :param tag_list: 标签名称集合
        :type tag_list: list[str]
        :param module_id: 模块ID
        :type module_id: str
        :param module_name: 模块名称
        :type module_name: str
        :param module_path: 模块path
        :type module_path: str
        :param module_path_name: 模块路径名称
        :type module_path_name: str
        :param release_dev: 发布版本号
        :type release_dev: str
        :param ext_param: 扩展参数
        :type ext_param: str
        :param execute_way: 执行方式（1：串行，2：并行）
        :type execute_way: int
        :param execute_type: 执行类型（0：冒烟，1：定时）
        :type execute_type: int
        :param status_code: 生命周期状态Code
        :type status_code: int
        :param status_name: 生命周期状态名称
        :type status_name: str
        :param result_code: 执行结果Code
        :type result_code: int
        :param result_name: 执行状态名称
        :type result_name: str
        :param execute_status_code: Echo执行状态Code
        :type execute_status_code: int
        :param execute_status_name: Echo执行状态名称
        :type execute_status_name: str
        :param executor_id: 执行人ID
        :type executor_id: str
        :param executor_name: 执行人名称
        :type executor_name: str
        :param execute_latest_time: 最近执行时间
        :type execute_latest_time: datetime
        :param execute_latest_time_timestamp: 最近执行时间时间戳
        :type execute_latest_time_timestamp: int
        :param execute_duration: 执行时长
        :type execute_duration: str
        :param execute_times: 执行次数
        :type execute_times: int
        :param project_uuid: 项目ID
        :type project_uuid: str
        :param case_operation_info: 
        :type case_operation_info: :class:`huaweicloudsdkcloudtest.v1.CaseOperationVo`
        :param assign_case_num: 关联用例数
        :type assign_case_num: int
        :param finish_case_num: 已完成用例数量
        :type finish_case_num: int
        :param assign_defect_num: 关联缺陷数量
        :type assign_defect_num: int
        :param task_assign_msg: 任务关联用例变更提示信息
        :type task_assign_msg: str
        :param iterator_version_uri: 测试套所属迭代uri，非迭代下创建的测试套返回null
        :type iterator_version_uri: str
        :param result_number_list: 用户自定义结果对应的用例数目
        :type result_number_list: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueAndCodeVo`]
        :param finish_date: 测试套完成时间
        :type finish_date: datetime
        :param finish_date_timestamp: 测试套完成时间戳
        :type finish_date_timestamp: int
        :param plan_start_date: 计划开始时间
        :type plan_start_date: datetime
        :param plan_start_timestamp: 计划开始时间戳
        :type plan_start_timestamp: int
        :param plan_end_date: 计划结束时间
        :type plan_end_date: datetime
        :param plan_end_timestamp: 计划结束时间戳
        :type plan_end_timestamp: int
        :param expiration_status: 测试套超期状态值，分别为：无状态(null)、未超期(0)、即将超期(1)、已超期(2)、延期完成(3)、按期完成(4)
        :type expiration_status: int
        :param expiration_status_name: 测试套超期状态名称，分别为：无状态(不显示状态)、未超期(Unexpired)、即将超期(About to expire)、已超期(Expired)、延期完成(Delayed completion)、按期完成(On schedule completion)
        :type expiration_status_name: str
        """
        
        

        self._uri = None
        self._name = None
        self._stage = None
        self._number = None
        self._tags = None
        self._description = None
        self._region = None
        self._author_id = None
        self._author_name = None
        self._owner_id = None
        self._owner_name = None
        self._parent_uri = None
        self._parent_path = None
        self._origin_uri = None
        self._version_uri = None
        self._branch_uri = None
        self._version_name = None
        self._creation_date = None
        self._create_date_timestamp = None
        self._update_time = None
        self._update_time_timestamp = None
        self._relation_change_time = None
        self._relation_change_time_timestamp = None
        self._test_case_condition = None
        self._updator_id = None
        self._updator_name = None
        self._relation_changer_id = None
        self._service_type = None
        self._service_type_name = None
        self._tag_list = None
        self._module_id = None
        self._module_name = None
        self._module_path = None
        self._module_path_name = None
        self._release_dev = None
        self._ext_param = None
        self._execute_way = None
        self._execute_type = None
        self._status_code = None
        self._status_name = None
        self._result_code = None
        self._result_name = None
        self._execute_status_code = None
        self._execute_status_name = None
        self._executor_id = None
        self._executor_name = None
        self._execute_latest_time = None
        self._execute_latest_time_timestamp = None
        self._execute_duration = None
        self._execute_times = None
        self._project_uuid = None
        self._case_operation_info = None
        self._assign_case_num = None
        self._finish_case_num = None
        self._assign_defect_num = None
        self._task_assign_msg = None
        self._iterator_version_uri = None
        self._result_number_list = None
        self._finish_date = None
        self._finish_date_timestamp = None
        self._plan_start_date = None
        self._plan_start_timestamp = None
        self._plan_end_date = None
        self._plan_end_timestamp = None
        self._expiration_status = None
        self._expiration_status_name = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if stage is not None:
            self.stage = stage
        if number is not None:
            self.number = number
        if tags is not None:
            self.tags = tags
        if description is not None:
            self.description = description
        if region is not None:
            self.region = region
        if author_id is not None:
            self.author_id = author_id
        if author_name is not None:
            self.author_name = author_name
        if owner_id is not None:
            self.owner_id = owner_id
        if owner_name is not None:
            self.owner_name = owner_name
        if parent_uri is not None:
            self.parent_uri = parent_uri
        if parent_path is not None:
            self.parent_path = parent_path
        if origin_uri is not None:
            self.origin_uri = origin_uri
        if version_uri is not None:
            self.version_uri = version_uri
        if branch_uri is not None:
            self.branch_uri = branch_uri
        if version_name is not None:
            self.version_name = version_name
        if creation_date is not None:
            self.creation_date = creation_date
        if create_date_timestamp is not None:
            self.create_date_timestamp = create_date_timestamp
        if update_time is not None:
            self.update_time = update_time
        if update_time_timestamp is not None:
            self.update_time_timestamp = update_time_timestamp
        if relation_change_time is not None:
            self.relation_change_time = relation_change_time
        if relation_change_time_timestamp is not None:
            self.relation_change_time_timestamp = relation_change_time_timestamp
        if test_case_condition is not None:
            self.test_case_condition = test_case_condition
        if updator_id is not None:
            self.updator_id = updator_id
        if updator_name is not None:
            self.updator_name = updator_name
        if relation_changer_id is not None:
            self.relation_changer_id = relation_changer_id
        if service_type is not None:
            self.service_type = service_type
        if service_type_name is not None:
            self.service_type_name = service_type_name
        if tag_list is not None:
            self.tag_list = tag_list
        if module_id is not None:
            self.module_id = module_id
        if module_name is not None:
            self.module_name = module_name
        if module_path is not None:
            self.module_path = module_path
        if module_path_name is not None:
            self.module_path_name = module_path_name
        if release_dev is not None:
            self.release_dev = release_dev
        if ext_param is not None:
            self.ext_param = ext_param
        if execute_way is not None:
            self.execute_way = execute_way
        if execute_type is not None:
            self.execute_type = execute_type
        if status_code is not None:
            self.status_code = status_code
        if status_name is not None:
            self.status_name = status_name
        if result_code is not None:
            self.result_code = result_code
        if result_name is not None:
            self.result_name = result_name
        if execute_status_code is not None:
            self.execute_status_code = execute_status_code
        if execute_status_name is not None:
            self.execute_status_name = execute_status_name
        if executor_id is not None:
            self.executor_id = executor_id
        if executor_name is not None:
            self.executor_name = executor_name
        if execute_latest_time is not None:
            self.execute_latest_time = execute_latest_time
        if execute_latest_time_timestamp is not None:
            self.execute_latest_time_timestamp = execute_latest_time_timestamp
        if execute_duration is not None:
            self.execute_duration = execute_duration
        if execute_times is not None:
            self.execute_times = execute_times
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if case_operation_info is not None:
            self.case_operation_info = case_operation_info
        if assign_case_num is not None:
            self.assign_case_num = assign_case_num
        if finish_case_num is not None:
            self.finish_case_num = finish_case_num
        if assign_defect_num is not None:
            self.assign_defect_num = assign_defect_num
        if task_assign_msg is not None:
            self.task_assign_msg = task_assign_msg
        if iterator_version_uri is not None:
            self.iterator_version_uri = iterator_version_uri
        if result_number_list is not None:
            self.result_number_list = result_number_list
        if finish_date is not None:
            self.finish_date = finish_date
        if finish_date_timestamp is not None:
            self.finish_date_timestamp = finish_date_timestamp
        if plan_start_date is not None:
            self.plan_start_date = plan_start_date
        if plan_start_timestamp is not None:
            self.plan_start_timestamp = plan_start_timestamp
        if plan_end_date is not None:
            self.plan_end_date = plan_end_date
        if plan_end_timestamp is not None:
            self.plan_end_timestamp = plan_end_timestamp
        if expiration_status is not None:
            self.expiration_status = expiration_status
        if expiration_status_name is not None:
            self.expiration_status_name = expiration_status_name

    @property
    def uri(self):
        """Gets the uri of this TaskVo.

        测试任务URI

        :return: The uri of this TaskVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this TaskVo.

        测试任务URI

        :param uri: The uri of this TaskVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def name(self):
        """Gets the name of this TaskVo.

        测试任务名称

        :return: The name of this TaskVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskVo.

        测试任务名称

        :param name: The name of this TaskVo.
        :type name: str
        """
        self._name = name

    @property
    def stage(self):
        """Gets the stage of this TaskVo.

        测试阶段

        :return: The stage of this TaskVo.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this TaskVo.

        测试阶段

        :param stage: The stage of this TaskVo.
        :type stage: str
        """
        self._stage = stage

    @property
    def number(self):
        """Gets the number of this TaskVo.

        编号

        :return: The number of this TaskVo.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this TaskVo.

        编号

        :param number: The number of this TaskVo.
        :type number: str
        """
        self._number = number

    @property
    def tags(self):
        """Gets the tags of this TaskVo.

        标签

        :return: The tags of this TaskVo.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TaskVo.

        标签

        :param tags: The tags of this TaskVo.
        :type tags: str
        """
        self._tags = tags

    @property
    def description(self):
        """Gets the description of this TaskVo.

        描述

        :return: The description of this TaskVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskVo.

        描述

        :param description: The description of this TaskVo.
        :type description: str
        """
        self._description = description

    @property
    def region(self):
        """Gets the region of this TaskVo.

        区域

        :return: The region of this TaskVo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TaskVo.

        区域

        :param region: The region of this TaskVo.
        :type region: str
        """
        self._region = region

    @property
    def author_id(self):
        """Gets the author_id of this TaskVo.

        创建人ID

        :return: The author_id of this TaskVo.
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this TaskVo.

        创建人ID

        :param author_id: The author_id of this TaskVo.
        :type author_id: str
        """
        self._author_id = author_id

    @property
    def author_name(self):
        """Gets the author_name of this TaskVo.

        创建人名称

        :return: The author_name of this TaskVo.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """Sets the author_name of this TaskVo.

        创建人名称

        :param author_name: The author_name of this TaskVo.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def owner_id(self):
        """Gets the owner_id of this TaskVo.

        责任人ID

        :return: The owner_id of this TaskVo.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this TaskVo.

        责任人ID

        :param owner_id: The owner_id of this TaskVo.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def owner_name(self):
        """Gets the owner_name of this TaskVo.

        责任人名称

        :return: The owner_name of this TaskVo.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this TaskVo.

        责任人名称

        :param owner_name: The owner_name of this TaskVo.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def parent_uri(self):
        """Gets the parent_uri of this TaskVo.

        父任务URI

        :return: The parent_uri of this TaskVo.
        :rtype: str
        """
        return self._parent_uri

    @parent_uri.setter
    def parent_uri(self, parent_uri):
        """Sets the parent_uri of this TaskVo.

        父任务URI

        :param parent_uri: The parent_uri of this TaskVo.
        :type parent_uri: str
        """
        self._parent_uri = parent_uri

    @property
    def parent_path(self):
        """Gets the parent_path of this TaskVo.

        父任务路径

        :return: The parent_path of this TaskVo.
        :rtype: str
        """
        return self._parent_path

    @parent_path.setter
    def parent_path(self, parent_path):
        """Sets the parent_path of this TaskVo.

        父任务路径

        :param parent_path: The parent_path of this TaskVo.
        :type parent_path: str
        """
        self._parent_path = parent_path

    @property
    def origin_uri(self):
        """Gets the origin_uri of this TaskVo.

        源任务URI

        :return: The origin_uri of this TaskVo.
        :rtype: str
        """
        return self._origin_uri

    @origin_uri.setter
    def origin_uri(self, origin_uri):
        """Sets the origin_uri of this TaskVo.

        源任务URI

        :param origin_uri: The origin_uri of this TaskVo.
        :type origin_uri: str
        """
        self._origin_uri = origin_uri

    @property
    def version_uri(self):
        """Gets the version_uri of this TaskVo.

        版本URI

        :return: The version_uri of this TaskVo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        """Sets the version_uri of this TaskVo.

        版本URI

        :param version_uri: The version_uri of this TaskVo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def branch_uri(self):
        """Gets the branch_uri of this TaskVo.

        分支URI

        :return: The branch_uri of this TaskVo.
        :rtype: str
        """
        return self._branch_uri

    @branch_uri.setter
    def branch_uri(self, branch_uri):
        """Sets the branch_uri of this TaskVo.

        分支URI

        :param branch_uri: The branch_uri of this TaskVo.
        :type branch_uri: str
        """
        self._branch_uri = branch_uri

    @property
    def version_name(self):
        """Gets the version_name of this TaskVo.

        版本名称

        :return: The version_name of this TaskVo.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this TaskVo.

        版本名称

        :param version_name: The version_name of this TaskVo.
        :type version_name: str
        """
        self._version_name = version_name

    @property
    def creation_date(self):
        """Gets the creation_date of this TaskVo.

        创建时间

        :return: The creation_date of this TaskVo.
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this TaskVo.

        创建时间

        :param creation_date: The creation_date of this TaskVo.
        :type creation_date: datetime
        """
        self._creation_date = creation_date

    @property
    def create_date_timestamp(self):
        """Gets the create_date_timestamp of this TaskVo.

        创建时间时间戳

        :return: The create_date_timestamp of this TaskVo.
        :rtype: int
        """
        return self._create_date_timestamp

    @create_date_timestamp.setter
    def create_date_timestamp(self, create_date_timestamp):
        """Sets the create_date_timestamp of this TaskVo.

        创建时间时间戳

        :param create_date_timestamp: The create_date_timestamp of this TaskVo.
        :type create_date_timestamp: int
        """
        self._create_date_timestamp = create_date_timestamp

    @property
    def update_time(self):
        """Gets the update_time of this TaskVo.

        更新时间

        :return: The update_time of this TaskVo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TaskVo.

        更新时间

        :param update_time: The update_time of this TaskVo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def update_time_timestamp(self):
        """Gets the update_time_timestamp of this TaskVo.

        更新时间时间戳

        :return: The update_time_timestamp of this TaskVo.
        :rtype: int
        """
        return self._update_time_timestamp

    @update_time_timestamp.setter
    def update_time_timestamp(self, update_time_timestamp):
        """Sets the update_time_timestamp of this TaskVo.

        更新时间时间戳

        :param update_time_timestamp: The update_time_timestamp of this TaskVo.
        :type update_time_timestamp: int
        """
        self._update_time_timestamp = update_time_timestamp

    @property
    def relation_change_time(self):
        """Gets the relation_change_time of this TaskVo.

        关联关系修改时时间

        :return: The relation_change_time of this TaskVo.
        :rtype: datetime
        """
        return self._relation_change_time

    @relation_change_time.setter
    def relation_change_time(self, relation_change_time):
        """Sets the relation_change_time of this TaskVo.

        关联关系修改时时间

        :param relation_change_time: The relation_change_time of this TaskVo.
        :type relation_change_time: datetime
        """
        self._relation_change_time = relation_change_time

    @property
    def relation_change_time_timestamp(self):
        """Gets the relation_change_time_timestamp of this TaskVo.

        关联关系修改时间时间戳

        :return: The relation_change_time_timestamp of this TaskVo.
        :rtype: int
        """
        return self._relation_change_time_timestamp

    @relation_change_time_timestamp.setter
    def relation_change_time_timestamp(self, relation_change_time_timestamp):
        """Sets the relation_change_time_timestamp of this TaskVo.

        关联关系修改时间时间戳

        :param relation_change_time_timestamp: The relation_change_time_timestamp of this TaskVo.
        :type relation_change_time_timestamp: int
        """
        self._relation_change_time_timestamp = relation_change_time_timestamp

    @property
    def test_case_condition(self):
        """Gets the test_case_condition of this TaskVo.

        动态任务用例过滤条件

        :return: The test_case_condition of this TaskVo.
        :rtype: str
        """
        return self._test_case_condition

    @test_case_condition.setter
    def test_case_condition(self, test_case_condition):
        """Sets the test_case_condition of this TaskVo.

        动态任务用例过滤条件

        :param test_case_condition: The test_case_condition of this TaskVo.
        :type test_case_condition: str
        """
        self._test_case_condition = test_case_condition

    @property
    def updator_id(self):
        """Gets the updator_id of this TaskVo.

        修改人Id

        :return: The updator_id of this TaskVo.
        :rtype: str
        """
        return self._updator_id

    @updator_id.setter
    def updator_id(self, updator_id):
        """Sets the updator_id of this TaskVo.

        修改人Id

        :param updator_id: The updator_id of this TaskVo.
        :type updator_id: str
        """
        self._updator_id = updator_id

    @property
    def updator_name(self):
        """Gets the updator_name of this TaskVo.

        修改人名称

        :return: The updator_name of this TaskVo.
        :rtype: str
        """
        return self._updator_name

    @updator_name.setter
    def updator_name(self, updator_name):
        """Sets the updator_name of this TaskVo.

        修改人名称

        :param updator_name: The updator_name of this TaskVo.
        :type updator_name: str
        """
        self._updator_name = updator_name

    @property
    def relation_changer_id(self):
        """Gets the relation_changer_id of this TaskVo.

        关联关系修改人Id

        :return: The relation_changer_id of this TaskVo.
        :rtype: str
        """
        return self._relation_changer_id

    @relation_changer_id.setter
    def relation_changer_id(self, relation_changer_id):
        """Sets the relation_changer_id of this TaskVo.

        关联关系修改人Id

        :param relation_changer_id: The relation_changer_id of this TaskVo.
        :type relation_changer_id: str
        """
        self._relation_changer_id = relation_changer_id

    @property
    def service_type(self):
        """Gets the service_type of this TaskVo.

        服务类型ID

        :return: The service_type of this TaskVo.
        :rtype: int
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this TaskVo.

        服务类型ID

        :param service_type: The service_type of this TaskVo.
        :type service_type: int
        """
        self._service_type = service_type

    @property
    def service_type_name(self):
        """Gets the service_type_name of this TaskVo.

        服务类型名称

        :return: The service_type_name of this TaskVo.
        :rtype: str
        """
        return self._service_type_name

    @service_type_name.setter
    def service_type_name(self, service_type_name):
        """Sets the service_type_name of this TaskVo.

        服务类型名称

        :param service_type_name: The service_type_name of this TaskVo.
        :type service_type_name: str
        """
        self._service_type_name = service_type_name

    @property
    def tag_list(self):
        """Gets the tag_list of this TaskVo.

        标签名称集合

        :return: The tag_list of this TaskVo.
        :rtype: list[str]
        """
        return self._tag_list

    @tag_list.setter
    def tag_list(self, tag_list):
        """Sets the tag_list of this TaskVo.

        标签名称集合

        :param tag_list: The tag_list of this TaskVo.
        :type tag_list: list[str]
        """
        self._tag_list = tag_list

    @property
    def module_id(self):
        """Gets the module_id of this TaskVo.

        模块ID

        :return: The module_id of this TaskVo.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        """Sets the module_id of this TaskVo.

        模块ID

        :param module_id: The module_id of this TaskVo.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def module_name(self):
        """Gets the module_name of this TaskVo.

        模块名称

        :return: The module_name of this TaskVo.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """Sets the module_name of this TaskVo.

        模块名称

        :param module_name: The module_name of this TaskVo.
        :type module_name: str
        """
        self._module_name = module_name

    @property
    def module_path(self):
        """Gets the module_path of this TaskVo.

        模块path

        :return: The module_path of this TaskVo.
        :rtype: str
        """
        return self._module_path

    @module_path.setter
    def module_path(self, module_path):
        """Sets the module_path of this TaskVo.

        模块path

        :param module_path: The module_path of this TaskVo.
        :type module_path: str
        """
        self._module_path = module_path

    @property
    def module_path_name(self):
        """Gets the module_path_name of this TaskVo.

        模块路径名称

        :return: The module_path_name of this TaskVo.
        :rtype: str
        """
        return self._module_path_name

    @module_path_name.setter
    def module_path_name(self, module_path_name):
        """Sets the module_path_name of this TaskVo.

        模块路径名称

        :param module_path_name: The module_path_name of this TaskVo.
        :type module_path_name: str
        """
        self._module_path_name = module_path_name

    @property
    def release_dev(self):
        """Gets the release_dev of this TaskVo.

        发布版本号

        :return: The release_dev of this TaskVo.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        """Sets the release_dev of this TaskVo.

        发布版本号

        :param release_dev: The release_dev of this TaskVo.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def ext_param(self):
        """Gets the ext_param of this TaskVo.

        扩展参数

        :return: The ext_param of this TaskVo.
        :rtype: str
        """
        return self._ext_param

    @ext_param.setter
    def ext_param(self, ext_param):
        """Sets the ext_param of this TaskVo.

        扩展参数

        :param ext_param: The ext_param of this TaskVo.
        :type ext_param: str
        """
        self._ext_param = ext_param

    @property
    def execute_way(self):
        """Gets the execute_way of this TaskVo.

        执行方式（1：串行，2：并行）

        :return: The execute_way of this TaskVo.
        :rtype: int
        """
        return self._execute_way

    @execute_way.setter
    def execute_way(self, execute_way):
        """Sets the execute_way of this TaskVo.

        执行方式（1：串行，2：并行）

        :param execute_way: The execute_way of this TaskVo.
        :type execute_way: int
        """
        self._execute_way = execute_way

    @property
    def execute_type(self):
        """Gets the execute_type of this TaskVo.

        执行类型（0：冒烟，1：定时）

        :return: The execute_type of this TaskVo.
        :rtype: int
        """
        return self._execute_type

    @execute_type.setter
    def execute_type(self, execute_type):
        """Sets the execute_type of this TaskVo.

        执行类型（0：冒烟，1：定时）

        :param execute_type: The execute_type of this TaskVo.
        :type execute_type: int
        """
        self._execute_type = execute_type

    @property
    def status_code(self):
        """Gets the status_code of this TaskVo.

        生命周期状态Code

        :return: The status_code of this TaskVo.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this TaskVo.

        生命周期状态Code

        :param status_code: The status_code of this TaskVo.
        :type status_code: int
        """
        self._status_code = status_code

    @property
    def status_name(self):
        """Gets the status_name of this TaskVo.

        生命周期状态名称

        :return: The status_name of this TaskVo.
        :rtype: str
        """
        return self._status_name

    @status_name.setter
    def status_name(self, status_name):
        """Sets the status_name of this TaskVo.

        生命周期状态名称

        :param status_name: The status_name of this TaskVo.
        :type status_name: str
        """
        self._status_name = status_name

    @property
    def result_code(self):
        """Gets the result_code of this TaskVo.

        执行结果Code

        :return: The result_code of this TaskVo.
        :rtype: int
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this TaskVo.

        执行结果Code

        :param result_code: The result_code of this TaskVo.
        :type result_code: int
        """
        self._result_code = result_code

    @property
    def result_name(self):
        """Gets the result_name of this TaskVo.

        执行状态名称

        :return: The result_name of this TaskVo.
        :rtype: str
        """
        return self._result_name

    @result_name.setter
    def result_name(self, result_name):
        """Sets the result_name of this TaskVo.

        执行状态名称

        :param result_name: The result_name of this TaskVo.
        :type result_name: str
        """
        self._result_name = result_name

    @property
    def execute_status_code(self):
        """Gets the execute_status_code of this TaskVo.

        Echo执行状态Code

        :return: The execute_status_code of this TaskVo.
        :rtype: int
        """
        return self._execute_status_code

    @execute_status_code.setter
    def execute_status_code(self, execute_status_code):
        """Sets the execute_status_code of this TaskVo.

        Echo执行状态Code

        :param execute_status_code: The execute_status_code of this TaskVo.
        :type execute_status_code: int
        """
        self._execute_status_code = execute_status_code

    @property
    def execute_status_name(self):
        """Gets the execute_status_name of this TaskVo.

        Echo执行状态名称

        :return: The execute_status_name of this TaskVo.
        :rtype: str
        """
        return self._execute_status_name

    @execute_status_name.setter
    def execute_status_name(self, execute_status_name):
        """Sets the execute_status_name of this TaskVo.

        Echo执行状态名称

        :param execute_status_name: The execute_status_name of this TaskVo.
        :type execute_status_name: str
        """
        self._execute_status_name = execute_status_name

    @property
    def executor_id(self):
        """Gets the executor_id of this TaskVo.

        执行人ID

        :return: The executor_id of this TaskVo.
        :rtype: str
        """
        return self._executor_id

    @executor_id.setter
    def executor_id(self, executor_id):
        """Sets the executor_id of this TaskVo.

        执行人ID

        :param executor_id: The executor_id of this TaskVo.
        :type executor_id: str
        """
        self._executor_id = executor_id

    @property
    def executor_name(self):
        """Gets the executor_name of this TaskVo.

        执行人名称

        :return: The executor_name of this TaskVo.
        :rtype: str
        """
        return self._executor_name

    @executor_name.setter
    def executor_name(self, executor_name):
        """Sets the executor_name of this TaskVo.

        执行人名称

        :param executor_name: The executor_name of this TaskVo.
        :type executor_name: str
        """
        self._executor_name = executor_name

    @property
    def execute_latest_time(self):
        """Gets the execute_latest_time of this TaskVo.

        最近执行时间

        :return: The execute_latest_time of this TaskVo.
        :rtype: datetime
        """
        return self._execute_latest_time

    @execute_latest_time.setter
    def execute_latest_time(self, execute_latest_time):
        """Sets the execute_latest_time of this TaskVo.

        最近执行时间

        :param execute_latest_time: The execute_latest_time of this TaskVo.
        :type execute_latest_time: datetime
        """
        self._execute_latest_time = execute_latest_time

    @property
    def execute_latest_time_timestamp(self):
        """Gets the execute_latest_time_timestamp of this TaskVo.

        最近执行时间时间戳

        :return: The execute_latest_time_timestamp of this TaskVo.
        :rtype: int
        """
        return self._execute_latest_time_timestamp

    @execute_latest_time_timestamp.setter
    def execute_latest_time_timestamp(self, execute_latest_time_timestamp):
        """Sets the execute_latest_time_timestamp of this TaskVo.

        最近执行时间时间戳

        :param execute_latest_time_timestamp: The execute_latest_time_timestamp of this TaskVo.
        :type execute_latest_time_timestamp: int
        """
        self._execute_latest_time_timestamp = execute_latest_time_timestamp

    @property
    def execute_duration(self):
        """Gets the execute_duration of this TaskVo.

        执行时长

        :return: The execute_duration of this TaskVo.
        :rtype: str
        """
        return self._execute_duration

    @execute_duration.setter
    def execute_duration(self, execute_duration):
        """Sets the execute_duration of this TaskVo.

        执行时长

        :param execute_duration: The execute_duration of this TaskVo.
        :type execute_duration: str
        """
        self._execute_duration = execute_duration

    @property
    def execute_times(self):
        """Gets the execute_times of this TaskVo.

        执行次数

        :return: The execute_times of this TaskVo.
        :rtype: int
        """
        return self._execute_times

    @execute_times.setter
    def execute_times(self, execute_times):
        """Sets the execute_times of this TaskVo.

        执行次数

        :param execute_times: The execute_times of this TaskVo.
        :type execute_times: int
        """
        self._execute_times = execute_times

    @property
    def project_uuid(self):
        """Gets the project_uuid of this TaskVo.

        项目ID

        :return: The project_uuid of this TaskVo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this TaskVo.

        项目ID

        :param project_uuid: The project_uuid of this TaskVo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def case_operation_info(self):
        """Gets the case_operation_info of this TaskVo.

        :return: The case_operation_info of this TaskVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CaseOperationVo`
        """
        return self._case_operation_info

    @case_operation_info.setter
    def case_operation_info(self, case_operation_info):
        """Sets the case_operation_info of this TaskVo.

        :param case_operation_info: The case_operation_info of this TaskVo.
        :type case_operation_info: :class:`huaweicloudsdkcloudtest.v1.CaseOperationVo`
        """
        self._case_operation_info = case_operation_info

    @property
    def assign_case_num(self):
        """Gets the assign_case_num of this TaskVo.

        关联用例数

        :return: The assign_case_num of this TaskVo.
        :rtype: int
        """
        return self._assign_case_num

    @assign_case_num.setter
    def assign_case_num(self, assign_case_num):
        """Sets the assign_case_num of this TaskVo.

        关联用例数

        :param assign_case_num: The assign_case_num of this TaskVo.
        :type assign_case_num: int
        """
        self._assign_case_num = assign_case_num

    @property
    def finish_case_num(self):
        """Gets the finish_case_num of this TaskVo.

        已完成用例数量

        :return: The finish_case_num of this TaskVo.
        :rtype: int
        """
        return self._finish_case_num

    @finish_case_num.setter
    def finish_case_num(self, finish_case_num):
        """Sets the finish_case_num of this TaskVo.

        已完成用例数量

        :param finish_case_num: The finish_case_num of this TaskVo.
        :type finish_case_num: int
        """
        self._finish_case_num = finish_case_num

    @property
    def assign_defect_num(self):
        """Gets the assign_defect_num of this TaskVo.

        关联缺陷数量

        :return: The assign_defect_num of this TaskVo.
        :rtype: int
        """
        return self._assign_defect_num

    @assign_defect_num.setter
    def assign_defect_num(self, assign_defect_num):
        """Sets the assign_defect_num of this TaskVo.

        关联缺陷数量

        :param assign_defect_num: The assign_defect_num of this TaskVo.
        :type assign_defect_num: int
        """
        self._assign_defect_num = assign_defect_num

    @property
    def task_assign_msg(self):
        """Gets the task_assign_msg of this TaskVo.

        任务关联用例变更提示信息

        :return: The task_assign_msg of this TaskVo.
        :rtype: str
        """
        return self._task_assign_msg

    @task_assign_msg.setter
    def task_assign_msg(self, task_assign_msg):
        """Sets the task_assign_msg of this TaskVo.

        任务关联用例变更提示信息

        :param task_assign_msg: The task_assign_msg of this TaskVo.
        :type task_assign_msg: str
        """
        self._task_assign_msg = task_assign_msg

    @property
    def iterator_version_uri(self):
        """Gets the iterator_version_uri of this TaskVo.

        测试套所属迭代uri，非迭代下创建的测试套返回null

        :return: The iterator_version_uri of this TaskVo.
        :rtype: str
        """
        return self._iterator_version_uri

    @iterator_version_uri.setter
    def iterator_version_uri(self, iterator_version_uri):
        """Sets the iterator_version_uri of this TaskVo.

        测试套所属迭代uri，非迭代下创建的测试套返回null

        :param iterator_version_uri: The iterator_version_uri of this TaskVo.
        :type iterator_version_uri: str
        """
        self._iterator_version_uri = iterator_version_uri

    @property
    def result_number_list(self):
        """Gets the result_number_list of this TaskVo.

        用户自定义结果对应的用例数目

        :return: The result_number_list of this TaskVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueAndCodeVo`]
        """
        return self._result_number_list

    @result_number_list.setter
    def result_number_list(self, result_number_list):
        """Sets the result_number_list of this TaskVo.

        用户自定义结果对应的用例数目

        :param result_number_list: The result_number_list of this TaskVo.
        :type result_number_list: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueAndCodeVo`]
        """
        self._result_number_list = result_number_list

    @property
    def finish_date(self):
        """Gets the finish_date of this TaskVo.

        测试套完成时间

        :return: The finish_date of this TaskVo.
        :rtype: datetime
        """
        return self._finish_date

    @finish_date.setter
    def finish_date(self, finish_date):
        """Sets the finish_date of this TaskVo.

        测试套完成时间

        :param finish_date: The finish_date of this TaskVo.
        :type finish_date: datetime
        """
        self._finish_date = finish_date

    @property
    def finish_date_timestamp(self):
        """Gets the finish_date_timestamp of this TaskVo.

        测试套完成时间戳

        :return: The finish_date_timestamp of this TaskVo.
        :rtype: int
        """
        return self._finish_date_timestamp

    @finish_date_timestamp.setter
    def finish_date_timestamp(self, finish_date_timestamp):
        """Sets the finish_date_timestamp of this TaskVo.

        测试套完成时间戳

        :param finish_date_timestamp: The finish_date_timestamp of this TaskVo.
        :type finish_date_timestamp: int
        """
        self._finish_date_timestamp = finish_date_timestamp

    @property
    def plan_start_date(self):
        """Gets the plan_start_date of this TaskVo.

        计划开始时间

        :return: The plan_start_date of this TaskVo.
        :rtype: datetime
        """
        return self._plan_start_date

    @plan_start_date.setter
    def plan_start_date(self, plan_start_date):
        """Sets the plan_start_date of this TaskVo.

        计划开始时间

        :param plan_start_date: The plan_start_date of this TaskVo.
        :type plan_start_date: datetime
        """
        self._plan_start_date = plan_start_date

    @property
    def plan_start_timestamp(self):
        """Gets the plan_start_timestamp of this TaskVo.

        计划开始时间戳

        :return: The plan_start_timestamp of this TaskVo.
        :rtype: int
        """
        return self._plan_start_timestamp

    @plan_start_timestamp.setter
    def plan_start_timestamp(self, plan_start_timestamp):
        """Sets the plan_start_timestamp of this TaskVo.

        计划开始时间戳

        :param plan_start_timestamp: The plan_start_timestamp of this TaskVo.
        :type plan_start_timestamp: int
        """
        self._plan_start_timestamp = plan_start_timestamp

    @property
    def plan_end_date(self):
        """Gets the plan_end_date of this TaskVo.

        计划结束时间

        :return: The plan_end_date of this TaskVo.
        :rtype: datetime
        """
        return self._plan_end_date

    @plan_end_date.setter
    def plan_end_date(self, plan_end_date):
        """Sets the plan_end_date of this TaskVo.

        计划结束时间

        :param plan_end_date: The plan_end_date of this TaskVo.
        :type plan_end_date: datetime
        """
        self._plan_end_date = plan_end_date

    @property
    def plan_end_timestamp(self):
        """Gets the plan_end_timestamp of this TaskVo.

        计划结束时间戳

        :return: The plan_end_timestamp of this TaskVo.
        :rtype: int
        """
        return self._plan_end_timestamp

    @plan_end_timestamp.setter
    def plan_end_timestamp(self, plan_end_timestamp):
        """Sets the plan_end_timestamp of this TaskVo.

        计划结束时间戳

        :param plan_end_timestamp: The plan_end_timestamp of this TaskVo.
        :type plan_end_timestamp: int
        """
        self._plan_end_timestamp = plan_end_timestamp

    @property
    def expiration_status(self):
        """Gets the expiration_status of this TaskVo.

        测试套超期状态值，分别为：无状态(null)、未超期(0)、即将超期(1)、已超期(2)、延期完成(3)、按期完成(4)

        :return: The expiration_status of this TaskVo.
        :rtype: int
        """
        return self._expiration_status

    @expiration_status.setter
    def expiration_status(self, expiration_status):
        """Sets the expiration_status of this TaskVo.

        测试套超期状态值，分别为：无状态(null)、未超期(0)、即将超期(1)、已超期(2)、延期完成(3)、按期完成(4)

        :param expiration_status: The expiration_status of this TaskVo.
        :type expiration_status: int
        """
        self._expiration_status = expiration_status

    @property
    def expiration_status_name(self):
        """Gets the expiration_status_name of this TaskVo.

        测试套超期状态名称，分别为：无状态(不显示状态)、未超期(Unexpired)、即将超期(About to expire)、已超期(Expired)、延期完成(Delayed completion)、按期完成(On schedule completion)

        :return: The expiration_status_name of this TaskVo.
        :rtype: str
        """
        return self._expiration_status_name

    @expiration_status_name.setter
    def expiration_status_name(self, expiration_status_name):
        """Sets the expiration_status_name of this TaskVo.

        测试套超期状态名称，分别为：无状态(不显示状态)、未超期(Unexpired)、即将超期(About to expire)、已超期(Expired)、延期完成(Delayed completion)、按期完成(On schedule completion)

        :param expiration_status_name: The expiration_status_name of this TaskVo.
        :type expiration_status_name: str
        """
        self._expiration_status_name = expiration_status_name

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
        if not isinstance(other, TaskVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
