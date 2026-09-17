# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskInfo:

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
        'version_uri': 'str',
        'name': 'str',
        'owner_id': 'str',
        'parent_uri': 'str',
        'test_case_condition': 'str',
        'stage': 'str',
        'service_type': 'int',
        'number': 'str',
        'tags': 'list[str]',
        'module_id': 'str',
        'module_name': 'str',
        'release_dev': 'str',
        'status_code': 'int',
        'ext_param': 'str',
        'execute_way': 'int',
        'execute_type': 'int',
        'description': 'str',
        'plan_start_timestamp': 'int',
        'plan_end_timestamp': 'int',
        'region': 'str',
        'assign_case_uris': 'list[str]',
        'case_operation_info': 'CaseOperationInfo',
        'only_update_status': 'bool',
        'is_async': 'bool'
    }

    attribute_map = {
        'uri': 'uri',
        'version_uri': 'version_uri',
        'name': 'name',
        'owner_id': 'owner_id',
        'parent_uri': 'parent_uri',
        'test_case_condition': 'test_case_condition',
        'stage': 'stage',
        'service_type': 'service_type',
        'number': 'number',
        'tags': 'tags',
        'module_id': 'module_id',
        'module_name': 'module_name',
        'release_dev': 'release_dev',
        'status_code': 'status_code',
        'ext_param': 'ext_param',
        'execute_way': 'execute_way',
        'execute_type': 'execute_type',
        'description': 'description',
        'plan_start_timestamp': 'plan_start_timestamp',
        'plan_end_timestamp': 'plan_end_timestamp',
        'region': 'region',
        'assign_case_uris': 'assign_case_uris',
        'case_operation_info': 'case_operation_info',
        'only_update_status': 'only_update_status',
        'is_async': 'is_async'
    }

    def __init__(self, uri=None, version_uri=None, name=None, owner_id=None, parent_uri=None, test_case_condition=None, stage=None, service_type=None, number=None, tags=None, module_id=None, module_name=None, release_dev=None, status_code=None, ext_param=None, execute_way=None, execute_type=None, description=None, plan_start_timestamp=None, plan_end_timestamp=None, region=None, assign_case_uris=None, case_operation_info=None, only_update_status=None, is_async=None):
        r"""TaskInfo

        The model defined in huaweicloud sdk

        :param uri: 指定创建任务的uri
        :type uri: str
        :param version_uri: 分支/迭代uri
        :type version_uri: str
        :param name: 名称
        :type name: str
        :param owner_id: 处理人/责任人id
        :type owner_id: str
        :param parent_uri: 父任务uri
        :type parent_uri: str
        :param test_case_condition: 动态任务用例过滤条件
        :type test_case_condition: str
        :param stage: 测试阶段
        :type stage: str
        :param service_type: 服务类型0:功能测试 1:接口测试 11:性能测试
        :type service_type: int
        :param number: 编号
        :type number: str
        :param tags: 标记id
        :type tags: list[str]
        :param module_id: 模块id
        :type module_id: str
        :param module_name: 模块名称
        :type module_name: str
        :param release_dev: 发布版本号
        :type release_dev: str
        :param status_code: 状态code
        :type status_code: int
        :param ext_param: 扩展参数
        :type ext_param: str
        :param execute_way: 执行方式 1：串行，2：并行
        :type execute_way: int
        :param execute_type: 执行类型（0：冒烟，1：定时）
        :type execute_type: int
        :param description: 描述
        :type description: str
        :param plan_start_timestamp: 计划开始时间戳，当传入-1时，时间置为空
        :type plan_start_timestamp: int
        :param plan_end_timestamp: 计划结束时间戳，当传入-1时，时间置为空
        :type plan_end_timestamp: int
        :param region: 区域
        :type region: str
        :param assign_case_uris: 任务关联用例uri数组，CloudDragon环境
        :type assign_case_uris: list[str]
        :param case_operation_info: 
        :type case_operation_info: :class:`huaweicloudsdkcloudtest.v1.CaseOperationInfo`
        :param only_update_status: 是否只需要修改测试套状态
        :type only_update_status: bool
        :param is_async: 是否异步
        :type is_async: bool
        """
        
        

        self._uri = None
        self._version_uri = None
        self._name = None
        self._owner_id = None
        self._parent_uri = None
        self._test_case_condition = None
        self._stage = None
        self._service_type = None
        self._number = None
        self._tags = None
        self._module_id = None
        self._module_name = None
        self._release_dev = None
        self._status_code = None
        self._ext_param = None
        self._execute_way = None
        self._execute_type = None
        self._description = None
        self._plan_start_timestamp = None
        self._plan_end_timestamp = None
        self._region = None
        self._assign_case_uris = None
        self._case_operation_info = None
        self._only_update_status = None
        self._is_async = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if version_uri is not None:
            self.version_uri = version_uri
        if name is not None:
            self.name = name
        if owner_id is not None:
            self.owner_id = owner_id
        if parent_uri is not None:
            self.parent_uri = parent_uri
        if test_case_condition is not None:
            self.test_case_condition = test_case_condition
        if stage is not None:
            self.stage = stage
        if service_type is not None:
            self.service_type = service_type
        if number is not None:
            self.number = number
        if tags is not None:
            self.tags = tags
        if module_id is not None:
            self.module_id = module_id
        if module_name is not None:
            self.module_name = module_name
        if release_dev is not None:
            self.release_dev = release_dev
        if status_code is not None:
            self.status_code = status_code
        if ext_param is not None:
            self.ext_param = ext_param
        if execute_way is not None:
            self.execute_way = execute_way
        if execute_type is not None:
            self.execute_type = execute_type
        if description is not None:
            self.description = description
        if plan_start_timestamp is not None:
            self.plan_start_timestamp = plan_start_timestamp
        if plan_end_timestamp is not None:
            self.plan_end_timestamp = plan_end_timestamp
        if region is not None:
            self.region = region
        if assign_case_uris is not None:
            self.assign_case_uris = assign_case_uris
        if case_operation_info is not None:
            self.case_operation_info = case_operation_info
        if only_update_status is not None:
            self.only_update_status = only_update_status
        if is_async is not None:
            self.is_async = is_async

    @property
    def uri(self):
        r"""Gets the uri of this TaskInfo.

        指定创建任务的uri

        :return: The uri of this TaskInfo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this TaskInfo.

        指定创建任务的uri

        :param uri: The uri of this TaskInfo.
        :type uri: str
        """
        self._uri = uri

    @property
    def version_uri(self):
        r"""Gets the version_uri of this TaskInfo.

        分支/迭代uri

        :return: The version_uri of this TaskInfo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this TaskInfo.

        分支/迭代uri

        :param version_uri: The version_uri of this TaskInfo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def name(self):
        r"""Gets the name of this TaskInfo.

        名称

        :return: The name of this TaskInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TaskInfo.

        名称

        :param name: The name of this TaskInfo.
        :type name: str
        """
        self._name = name

    @property
    def owner_id(self):
        r"""Gets the owner_id of this TaskInfo.

        处理人/责任人id

        :return: The owner_id of this TaskInfo.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this TaskInfo.

        处理人/责任人id

        :param owner_id: The owner_id of this TaskInfo.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def parent_uri(self):
        r"""Gets the parent_uri of this TaskInfo.

        父任务uri

        :return: The parent_uri of this TaskInfo.
        :rtype: str
        """
        return self._parent_uri

    @parent_uri.setter
    def parent_uri(self, parent_uri):
        r"""Sets the parent_uri of this TaskInfo.

        父任务uri

        :param parent_uri: The parent_uri of this TaskInfo.
        :type parent_uri: str
        """
        self._parent_uri = parent_uri

    @property
    def test_case_condition(self):
        r"""Gets the test_case_condition of this TaskInfo.

        动态任务用例过滤条件

        :return: The test_case_condition of this TaskInfo.
        :rtype: str
        """
        return self._test_case_condition

    @test_case_condition.setter
    def test_case_condition(self, test_case_condition):
        r"""Sets the test_case_condition of this TaskInfo.

        动态任务用例过滤条件

        :param test_case_condition: The test_case_condition of this TaskInfo.
        :type test_case_condition: str
        """
        self._test_case_condition = test_case_condition

    @property
    def stage(self):
        r"""Gets the stage of this TaskInfo.

        测试阶段

        :return: The stage of this TaskInfo.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        r"""Sets the stage of this TaskInfo.

        测试阶段

        :param stage: The stage of this TaskInfo.
        :type stage: str
        """
        self._stage = stage

    @property
    def service_type(self):
        r"""Gets the service_type of this TaskInfo.

        服务类型0:功能测试 1:接口测试 11:性能测试

        :return: The service_type of this TaskInfo.
        :rtype: int
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this TaskInfo.

        服务类型0:功能测试 1:接口测试 11:性能测试

        :param service_type: The service_type of this TaskInfo.
        :type service_type: int
        """
        self._service_type = service_type

    @property
    def number(self):
        r"""Gets the number of this TaskInfo.

        编号

        :return: The number of this TaskInfo.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this TaskInfo.

        编号

        :param number: The number of this TaskInfo.
        :type number: str
        """
        self._number = number

    @property
    def tags(self):
        r"""Gets the tags of this TaskInfo.

        标记id

        :return: The tags of this TaskInfo.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this TaskInfo.

        标记id

        :param tags: The tags of this TaskInfo.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def module_id(self):
        r"""Gets the module_id of this TaskInfo.

        模块id

        :return: The module_id of this TaskInfo.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this TaskInfo.

        模块id

        :param module_id: The module_id of this TaskInfo.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def module_name(self):
        r"""Gets the module_name of this TaskInfo.

        模块名称

        :return: The module_name of this TaskInfo.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        r"""Sets the module_name of this TaskInfo.

        模块名称

        :param module_name: The module_name of this TaskInfo.
        :type module_name: str
        """
        self._module_name = module_name

    @property
    def release_dev(self):
        r"""Gets the release_dev of this TaskInfo.

        发布版本号

        :return: The release_dev of this TaskInfo.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        r"""Sets the release_dev of this TaskInfo.

        发布版本号

        :param release_dev: The release_dev of this TaskInfo.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def status_code(self):
        r"""Gets the status_code of this TaskInfo.

        状态code

        :return: The status_code of this TaskInfo.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this TaskInfo.

        状态code

        :param status_code: The status_code of this TaskInfo.
        :type status_code: int
        """
        self._status_code = status_code

    @property
    def ext_param(self):
        r"""Gets the ext_param of this TaskInfo.

        扩展参数

        :return: The ext_param of this TaskInfo.
        :rtype: str
        """
        return self._ext_param

    @ext_param.setter
    def ext_param(self, ext_param):
        r"""Sets the ext_param of this TaskInfo.

        扩展参数

        :param ext_param: The ext_param of this TaskInfo.
        :type ext_param: str
        """
        self._ext_param = ext_param

    @property
    def execute_way(self):
        r"""Gets the execute_way of this TaskInfo.

        执行方式 1：串行，2：并行

        :return: The execute_way of this TaskInfo.
        :rtype: int
        """
        return self._execute_way

    @execute_way.setter
    def execute_way(self, execute_way):
        r"""Sets the execute_way of this TaskInfo.

        执行方式 1：串行，2：并行

        :param execute_way: The execute_way of this TaskInfo.
        :type execute_way: int
        """
        self._execute_way = execute_way

    @property
    def execute_type(self):
        r"""Gets the execute_type of this TaskInfo.

        执行类型（0：冒烟，1：定时）

        :return: The execute_type of this TaskInfo.
        :rtype: int
        """
        return self._execute_type

    @execute_type.setter
    def execute_type(self, execute_type):
        r"""Sets the execute_type of this TaskInfo.

        执行类型（0：冒烟，1：定时）

        :param execute_type: The execute_type of this TaskInfo.
        :type execute_type: int
        """
        self._execute_type = execute_type

    @property
    def description(self):
        r"""Gets the description of this TaskInfo.

        描述

        :return: The description of this TaskInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TaskInfo.

        描述

        :param description: The description of this TaskInfo.
        :type description: str
        """
        self._description = description

    @property
    def plan_start_timestamp(self):
        r"""Gets the plan_start_timestamp of this TaskInfo.

        计划开始时间戳，当传入-1时，时间置为空

        :return: The plan_start_timestamp of this TaskInfo.
        :rtype: int
        """
        return self._plan_start_timestamp

    @plan_start_timestamp.setter
    def plan_start_timestamp(self, plan_start_timestamp):
        r"""Sets the plan_start_timestamp of this TaskInfo.

        计划开始时间戳，当传入-1时，时间置为空

        :param plan_start_timestamp: The plan_start_timestamp of this TaskInfo.
        :type plan_start_timestamp: int
        """
        self._plan_start_timestamp = plan_start_timestamp

    @property
    def plan_end_timestamp(self):
        r"""Gets the plan_end_timestamp of this TaskInfo.

        计划结束时间戳，当传入-1时，时间置为空

        :return: The plan_end_timestamp of this TaskInfo.
        :rtype: int
        """
        return self._plan_end_timestamp

    @plan_end_timestamp.setter
    def plan_end_timestamp(self, plan_end_timestamp):
        r"""Sets the plan_end_timestamp of this TaskInfo.

        计划结束时间戳，当传入-1时，时间置为空

        :param plan_end_timestamp: The plan_end_timestamp of this TaskInfo.
        :type plan_end_timestamp: int
        """
        self._plan_end_timestamp = plan_end_timestamp

    @property
    def region(self):
        r"""Gets the region of this TaskInfo.

        区域

        :return: The region of this TaskInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this TaskInfo.

        区域

        :param region: The region of this TaskInfo.
        :type region: str
        """
        self._region = region

    @property
    def assign_case_uris(self):
        r"""Gets the assign_case_uris of this TaskInfo.

        任务关联用例uri数组，CloudDragon环境

        :return: The assign_case_uris of this TaskInfo.
        :rtype: list[str]
        """
        return self._assign_case_uris

    @assign_case_uris.setter
    def assign_case_uris(self, assign_case_uris):
        r"""Sets the assign_case_uris of this TaskInfo.

        任务关联用例uri数组，CloudDragon环境

        :param assign_case_uris: The assign_case_uris of this TaskInfo.
        :type assign_case_uris: list[str]
        """
        self._assign_case_uris = assign_case_uris

    @property
    def case_operation_info(self):
        r"""Gets the case_operation_info of this TaskInfo.

        :return: The case_operation_info of this TaskInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CaseOperationInfo`
        """
        return self._case_operation_info

    @case_operation_info.setter
    def case_operation_info(self, case_operation_info):
        r"""Sets the case_operation_info of this TaskInfo.

        :param case_operation_info: The case_operation_info of this TaskInfo.
        :type case_operation_info: :class:`huaweicloudsdkcloudtest.v1.CaseOperationInfo`
        """
        self._case_operation_info = case_operation_info

    @property
    def only_update_status(self):
        r"""Gets the only_update_status of this TaskInfo.

        是否只需要修改测试套状态

        :return: The only_update_status of this TaskInfo.
        :rtype: bool
        """
        return self._only_update_status

    @only_update_status.setter
    def only_update_status(self, only_update_status):
        r"""Sets the only_update_status of this TaskInfo.

        是否只需要修改测试套状态

        :param only_update_status: The only_update_status of this TaskInfo.
        :type only_update_status: bool
        """
        self._only_update_status = only_update_status

    @property
    def is_async(self):
        r"""Gets the is_async of this TaskInfo.

        是否异步

        :return: The is_async of this TaskInfo.
        :rtype: bool
        """
        return self._is_async

    @is_async.setter
    def is_async(self, is_async):
        r"""Sets the is_async of this TaskInfo.

        是否异步

        :param is_async: The is_async of this TaskInfo.
        :type is_async: bool
        """
        self._is_async = is_async

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
        if not isinstance(other, TaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
