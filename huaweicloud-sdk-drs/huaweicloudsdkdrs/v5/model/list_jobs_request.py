# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'job_type': 'str',
        'name': 'str',
        'status': 'str',
        'engine_type': 'str',
        'net_type': 'str',
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'instance_ids': 'list[str]',
        'instance_ip': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'job_type': 'job_type',
        'name': 'name',
        'status': 'status',
        'engine_type': 'engine_type',
        'net_type': 'net_type',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'instance_ids': 'instance_ids',
        'instance_ip': 'instance_ip'
    }

    def __init__(self, x_language=None, job_type=None, name=None, status=None, engine_type=None, net_type=None, enterprise_project_id=None, offset=None, limit=None, sort_key=None, sort_dir=None, instance_ids=None, instance_ip=None):
        r"""ListJobsRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文 - zh-cn：中文  **默认取值**：  en-us
        :type x_language: str
        :param job_type: **参数解释**：  DRS任务场景类型，用于区分不同的数据复制场景。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备 - replay：流量回放  **默认取值**：  不涉及
        :type job_type: str
        :param name: **参数解释**：  任务ID或名称，用于按任务ID或名称过滤查询结果。  **约束限制**：  - 支持输入多个任务ID，以逗号分隔，最多10个。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type name: str
        :param status: **参数解释**：  任务当前运行状态，用于按任务状态过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  - CREATING：创建中 - CREATE_FAILED：创建失败 - CONFIGURATION：配置中 - STARTJOBING：启动中 - WAITING_FOR_START：等待启动中 - START_JOB_FAILED：启动失败 - FULL_TRANSFER_STARTED：全量开始，灾备场景下为初始化 - FULL_TRANSFER_FAILED：全量失败，灾备场景下为初始化失败 - FULL_TRANSFER_COMPLETE：全量完成，灾备场景下为初始化完成 - INCRE_TRANSFER_STARTED：增量开始，灾备场景下为灾备中 - INCRE_TRANSFER_FAILED：增量失败，灾备场景下为灾备异常 - RELEASE_RESOURCE_STARTED：结束任务中 - RELEASE_RESOURCE_FAILED：结束任务失败 - RELEASE_RESOURCE_COMPLETE：已结束 - CHANGE_JOB_STARTED：任务变更中 - CHANGE_JOB_FAILED：任务变更失败 - CHILD_TRANSFER_STARTING：子任务启动中 - CHILD_TRANSFER_STARTED：子任务迁移中 - CHILD_TRANSFER_COMPLETE：子任务迁移完成 - CHILD_TRANSFER_FAILED：子任务迁移失败 - RELEASE_CHILD_TRANSFER_STARTED：子任务结束中 - RELEASE_CHILD_TRANSFER_COMPLETE：子任务已结束  **默认取值**：  不涉及
        :type status: str
        :param engine_type: **参数解释**：  DRS任务引擎类型，用于按引擎类型过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用 - redis-to-gaussredis：Redis迁移到GeminiDB Redis，实时迁移场景使用 - rediscluster-to-gaussredis：Redis集群迁移到GeminiDB Redis，实时迁移场景使用  **默认取值**：  不涉及
        :type engine_type: str
        :param net_type: **参数解释**：  任务使用的网络类型，用于按网络类型过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  - eip：公网网络 - vpc：VPC网络，灾备场景不支持选择VPC网络 - vpn：VPN、专线网络  **默认取值**：  不涉及
        :type net_type: str
        :param enterprise_project_id: **参数解释**：  企业项目ID，用于按企业项目过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  空字符串，表示查询所有企业项目任务
        :type enterprise_project_id: str
        :param offset: **参数解释**：  偏移量，表示查询该偏移量后面的记录，用于分页查询。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  0
        :type offset: int
        :param limit: **参数解释**：  查询返回记录的数量限制，用于分页查询时控制每页返回的数据条数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type limit: int
        :param sort_key: **参数解释**：  返回结果的排序关键字，指定任务列表的排序依据。  **约束限制**：  不涉及。  **取值范围**：  - name：按任务名称排序 - status：按任务状态排序 - create_time：按创建时间排序 - net_type：按网络类型排序 - job_direction：按任务方向排序 - pay_mode：按付费模式排序  **默认取值**：  create_time
        :type sort_key: str
        :param sort_dir: **参数解释**：  排序方向，指定返回结果按升序或降序排列。  **约束限制**：  不涉及。  **取值范围**：  - desc：降序 - asc：升序  **默认取值**：  desc
        :type sort_dir: str
        :param instance_ids: **参数解释**：  数据库实例ID列表，用于按数据库实例过滤查询结果。  **约束限制**：  - 最多支持10个实例ID。  **取值范围**：  不涉及。  **默认取值**：  null，表示不使用数据库实例ID过滤
        :type instance_ids: list[str]
        :param instance_ip: **参数解释**：  DRS绑定的数据库实例IP，用于按数据库实例IP过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  空字符串，表示不使用DRS绑定数据库IP过滤
        :type instance_ip: str
        """
        
        

        self._x_language = None
        self._job_type = None
        self._name = None
        self._status = None
        self._engine_type = None
        self._net_type = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self._instance_ids = None
        self._instance_ip = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.job_type = job_type
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if engine_type is not None:
            self.engine_type = engine_type
        if net_type is not None:
            self.net_type = net_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if instance_ids is not None:
            self.instance_ids = instance_ids
        if instance_ip is not None:
            self.instance_ip = instance_ip

    @property
    def x_language(self):
        r"""Gets the x_language of this ListJobsRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文 - zh-cn：中文  **默认取值**：  en-us

        :return: The x_language of this ListJobsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListJobsRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文 - zh-cn：中文  **默认取值**：  en-us

        :param x_language: The x_language of this ListJobsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def job_type(self):
        r"""Gets the job_type of this ListJobsRequest.

        **参数解释**：  DRS任务场景类型，用于区分不同的数据复制场景。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备 - replay：流量回放  **默认取值**：  不涉及

        :return: The job_type of this ListJobsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ListJobsRequest.

        **参数解释**：  DRS任务场景类型，用于区分不同的数据复制场景。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备 - replay：流量回放  **默认取值**：  不涉及

        :param job_type: The job_type of this ListJobsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def name(self):
        r"""Gets the name of this ListJobsRequest.

        **参数解释**：  任务ID或名称，用于按任务ID或名称过滤查询结果。  **约束限制**：  - 支持输入多个任务ID，以逗号分隔，最多10个。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The name of this ListJobsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListJobsRequest.

        **参数解释**：  任务ID或名称，用于按任务ID或名称过滤查询结果。  **约束限制**：  - 支持输入多个任务ID，以逗号分隔，最多10个。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param name: The name of this ListJobsRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListJobsRequest.

        **参数解释**：  任务当前运行状态，用于按任务状态过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  - CREATING：创建中 - CREATE_FAILED：创建失败 - CONFIGURATION：配置中 - STARTJOBING：启动中 - WAITING_FOR_START：等待启动中 - START_JOB_FAILED：启动失败 - FULL_TRANSFER_STARTED：全量开始，灾备场景下为初始化 - FULL_TRANSFER_FAILED：全量失败，灾备场景下为初始化失败 - FULL_TRANSFER_COMPLETE：全量完成，灾备场景下为初始化完成 - INCRE_TRANSFER_STARTED：增量开始，灾备场景下为灾备中 - INCRE_TRANSFER_FAILED：增量失败，灾备场景下为灾备异常 - RELEASE_RESOURCE_STARTED：结束任务中 - RELEASE_RESOURCE_FAILED：结束任务失败 - RELEASE_RESOURCE_COMPLETE：已结束 - CHANGE_JOB_STARTED：任务变更中 - CHANGE_JOB_FAILED：任务变更失败 - CHILD_TRANSFER_STARTING：子任务启动中 - CHILD_TRANSFER_STARTED：子任务迁移中 - CHILD_TRANSFER_COMPLETE：子任务迁移完成 - CHILD_TRANSFER_FAILED：子任务迁移失败 - RELEASE_CHILD_TRANSFER_STARTED：子任务结束中 - RELEASE_CHILD_TRANSFER_COMPLETE：子任务已结束  **默认取值**：  不涉及

        :return: The status of this ListJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListJobsRequest.

        **参数解释**：  任务当前运行状态，用于按任务状态过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  - CREATING：创建中 - CREATE_FAILED：创建失败 - CONFIGURATION：配置中 - STARTJOBING：启动中 - WAITING_FOR_START：等待启动中 - START_JOB_FAILED：启动失败 - FULL_TRANSFER_STARTED：全量开始，灾备场景下为初始化 - FULL_TRANSFER_FAILED：全量失败，灾备场景下为初始化失败 - FULL_TRANSFER_COMPLETE：全量完成，灾备场景下为初始化完成 - INCRE_TRANSFER_STARTED：增量开始，灾备场景下为灾备中 - INCRE_TRANSFER_FAILED：增量失败，灾备场景下为灾备异常 - RELEASE_RESOURCE_STARTED：结束任务中 - RELEASE_RESOURCE_FAILED：结束任务失败 - RELEASE_RESOURCE_COMPLETE：已结束 - CHANGE_JOB_STARTED：任务变更中 - CHANGE_JOB_FAILED：任务变更失败 - CHILD_TRANSFER_STARTING：子任务启动中 - CHILD_TRANSFER_STARTED：子任务迁移中 - CHILD_TRANSFER_COMPLETE：子任务迁移完成 - CHILD_TRANSFER_FAILED：子任务迁移失败 - RELEASE_CHILD_TRANSFER_STARTED：子任务结束中 - RELEASE_CHILD_TRANSFER_COMPLETE：子任务已结束  **默认取值**：  不涉及

        :param status: The status of this ListJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ListJobsRequest.

        **参数解释**：  DRS任务引擎类型，用于按引擎类型过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用 - redis-to-gaussredis：Redis迁移到GeminiDB Redis，实时迁移场景使用 - rediscluster-to-gaussredis：Redis集群迁移到GeminiDB Redis，实时迁移场景使用  **默认取值**：  不涉及

        :return: The engine_type of this ListJobsRequest.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ListJobsRequest.

        **参数解释**：  DRS任务引擎类型，用于按引擎类型过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用 - redis-to-gaussredis：Redis迁移到GeminiDB Redis，实时迁移场景使用 - rediscluster-to-gaussredis：Redis集群迁移到GeminiDB Redis，实时迁移场景使用  **默认取值**：  不涉及

        :param engine_type: The engine_type of this ListJobsRequest.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def net_type(self):
        r"""Gets the net_type of this ListJobsRequest.

        **参数解释**：  任务使用的网络类型，用于按网络类型过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  - eip：公网网络 - vpc：VPC网络，灾备场景不支持选择VPC网络 - vpn：VPN、专线网络  **默认取值**：  不涉及

        :return: The net_type of this ListJobsRequest.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        r"""Sets the net_type of this ListJobsRequest.

        **参数解释**：  任务使用的网络类型，用于按网络类型过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  - eip：公网网络 - vpc：VPC网络，灾备场景不支持选择VPC网络 - vpn：VPN、专线网络  **默认取值**：  不涉及

        :param net_type: The net_type of this ListJobsRequest.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListJobsRequest.

        **参数解释**：  企业项目ID，用于按企业项目过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  空字符串，表示查询所有企业项目任务

        :return: The enterprise_project_id of this ListJobsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListJobsRequest.

        **参数解释**：  企业项目ID，用于按企业项目过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  空字符串，表示查询所有企业项目任务

        :param enterprise_project_id: The enterprise_project_id of this ListJobsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListJobsRequest.

        **参数解释**：  偏移量，表示查询该偏移量后面的记录，用于分页查询。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  0

        :return: The offset of this ListJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListJobsRequest.

        **参数解释**：  偏移量，表示查询该偏移量后面的记录，用于分页查询。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  0

        :param offset: The offset of this ListJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListJobsRequest.

        **参数解释**：  查询返回记录的数量限制，用于分页查询时控制每页返回的数据条数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The limit of this ListJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListJobsRequest.

        **参数解释**：  查询返回记录的数量限制，用于分页查询时控制每页返回的数据条数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param limit: The limit of this ListJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListJobsRequest.

        **参数解释**：  返回结果的排序关键字，指定任务列表的排序依据。  **约束限制**：  不涉及。  **取值范围**：  - name：按任务名称排序 - status：按任务状态排序 - create_time：按创建时间排序 - net_type：按网络类型排序 - job_direction：按任务方向排序 - pay_mode：按付费模式排序  **默认取值**：  create_time

        :return: The sort_key of this ListJobsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListJobsRequest.

        **参数解释**：  返回结果的排序关键字，指定任务列表的排序依据。  **约束限制**：  不涉及。  **取值范围**：  - name：按任务名称排序 - status：按任务状态排序 - create_time：按创建时间排序 - net_type：按网络类型排序 - job_direction：按任务方向排序 - pay_mode：按付费模式排序  **默认取值**：  create_time

        :param sort_key: The sort_key of this ListJobsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListJobsRequest.

        **参数解释**：  排序方向，指定返回结果按升序或降序排列。  **约束限制**：  不涉及。  **取值范围**：  - desc：降序 - asc：升序  **默认取值**：  desc

        :return: The sort_dir of this ListJobsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListJobsRequest.

        **参数解释**：  排序方向，指定返回结果按升序或降序排列。  **约束限制**：  不涉及。  **取值范围**：  - desc：降序 - asc：升序  **默认取值**：  desc

        :param sort_dir: The sort_dir of this ListJobsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this ListJobsRequest.

        **参数解释**：  数据库实例ID列表，用于按数据库实例过滤查询结果。  **约束限制**：  - 最多支持10个实例ID。  **取值范围**：  不涉及。  **默认取值**：  null，表示不使用数据库实例ID过滤

        :return: The instance_ids of this ListJobsRequest.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this ListJobsRequest.

        **参数解释**：  数据库实例ID列表，用于按数据库实例过滤查询结果。  **约束限制**：  - 最多支持10个实例ID。  **取值范围**：  不涉及。  **默认取值**：  null，表示不使用数据库实例ID过滤

        :param instance_ids: The instance_ids of this ListJobsRequest.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def instance_ip(self):
        r"""Gets the instance_ip of this ListJobsRequest.

        **参数解释**：  DRS绑定的数据库实例IP，用于按数据库实例IP过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  空字符串，表示不使用DRS绑定数据库IP过滤

        :return: The instance_ip of this ListJobsRequest.
        :rtype: str
        """
        return self._instance_ip

    @instance_ip.setter
    def instance_ip(self, instance_ip):
        r"""Sets the instance_ip of this ListJobsRequest.

        **参数解释**：  DRS绑定的数据库实例IP，用于按数据库实例IP过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  空字符串，表示不使用DRS绑定数据库IP过滤

        :param instance_ip: The instance_ip of this ListJobsRequest.
        :type instance_ip: str
        """
        self._instance_ip = instance_ip

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
        if not isinstance(other, ListJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
