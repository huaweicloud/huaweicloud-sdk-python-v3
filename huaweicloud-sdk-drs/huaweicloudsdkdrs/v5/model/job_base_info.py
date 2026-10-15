# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobBaseInfo:

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
        'job_type': 'str',
        'multi_write': 'bool',
        'engine_type': 'str',
        'job_direction': 'str',
        'task_type': 'str',
        'net_type': 'str',
        'charging_mode': 'str',
        'enterprise_project_id': 'str',
        'description': 'str',
        'start_time': 'str',
        'expired_days': 'str',
        'tags': 'list[ResourceTag]',
        'is_open_fast_clean': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'job_type': 'job_type',
        'multi_write': 'multi_write',
        'engine_type': 'engine_type',
        'job_direction': 'job_direction',
        'task_type': 'task_type',
        'net_type': 'net_type',
        'charging_mode': 'charging_mode',
        'enterprise_project_id': 'enterprise_project_id',
        'description': 'description',
        'start_time': 'start_time',
        'expired_days': 'expired_days',
        'tags': 'tags',
        'is_open_fast_clean': 'is_open_fast_clean'
    }

    def __init__(self, name=None, job_type=None, multi_write=None, engine_type=None, job_direction=None, task_type=None, net_type=None, charging_mode=None, enterprise_project_id=None, description=None, start_time=None, expired_days=None, tags=None, is_open_fast_clean=None):
        r"""JobBaseInfo

        The model defined in huaweicloud sdk

        :param name: **参数解释**：  任务名称，用于标识和区分不同的数据复制任务。  **约束限制**：  - 长度在4到50位之间，不区分大小写。 - 可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type name: str
        :param job_type: **参数解释**：  DRS任务场景类型，用于区分不同的数据复制场景。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步  **默认取值**：  不涉及
        :type job_type: str
        :param multi_write: **参数解释**：  灾备类型是否双主灾备，指定灾备场景下是否启用双向写入功能。  **约束限制**：  - job_type为cloudDataGuard时必填。  **取值范围**：  - true：双主灾备 - false：非双主灾备  **默认取值**：  false
        :type multi_write: bool
        :param engine_type: **参数解释**：  DRS任务引擎类型。  **约束限制**：  不涉及。  **取值范围**：  - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用 - redis-to-gaussredis：Redis同步到GeminiDB Redis，实时迁移场景使用 - rediscluster-to-gaussredis：Redis集群同步到GeminiDB Redis，实时迁移场景使用 - mysql-to-mysql：MySQL同步到MySQL，实时同步场景使用  **默认取值**：  不涉及
        :type engine_type: str
        :param job_direction: **参数解释**：  任务的迁移方向。  **约束限制**：  不涉及。  **取值范围**：  - up：入云，灾备场景时对应本云为备 - down：出云，灾备场景时对应本云为主 - non-dbs：自建  **默认取值**：  不涉及
        :type job_direction: str
        :param task_type: **参数解释**：  任务迁移模式，指定数据复制任务的执行方式。  **约束限制**：  不涉及。  **取值范围**：  - FULL_TRANS：全量迁移，仅迁移历史数据 - FULL_INCR_TRANS：全量+增量迁移，先迁移历史数据再持续同步增量 - INCR_TRANS：增量迁移，仅同步数据变更  **默认取值**：  不涉及
        :type task_type: str
        :param net_type: **参数解释**：  任务使用的网络类型。  **约束限制**：  - 灾备场景不支持选择VPC网络。  **取值范围**：  - eip：公网网络 - vpc：VPC网络 - vpn：VPN、专线网络  **默认取值**：  不涉及
        :type net_type: str
        :param charging_mode: **参数解释**：  任务的计费模式，指定数据复制任务的付费方式。  **约束限制**：  不涉及。  **取值范围**：  - period：包周期 - on_demand：按需  **默认取值**：  on_demand
        :type charging_mode: str
        :param enterprise_project_id: **参数解释**：  企业项目ID，用于按企业项目过滤查询结果。  **约束限制**：  - 不传值时设置为null，不能设置为空字符串。 - 当企业项目开关打开时，可以传值。  **取值范围**：  不涉及。  **默认取值**：  \&quot;0\&quot;，表示default企业项目
        :type enterprise_project_id: str
        :param description: **参数解释**：  任务描述，用于对数据复制任务添加补充说明信息。  **约束限制**：  - 长度不能超过256位。 - 不能包含!&lt;&gt;&amp;&#39;\&quot;\\特殊字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type description: str
        :param start_time: **参数解释**：  任务定时启动时间，设置后任务将在指定时间自动启动。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type start_time: str
        :param expired_days: 任务处于异常状态一段时间后，将会自动结束。单位为天。(范围14-100)，不传默认为14天。
        :type expired_days: str
        :param tags: **参数解释**：  标签信息，用于为数据复制任务添加标签以便分类管理。  **约束限制**：  - 最多添加10个标签。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type tags: list[:class:`huaweicloudsdkdrs.v5.ResourceTag`]
        :param is_open_fast_clean: **参数解释**：  是否开启云数据库RDS for MySQL/MariaDB的binlog快速清理，开启后可自动清理已同步的binlog以释放磁盘空间。  **约束限制**：  - 仅MySQL/MariaDB引擎类型适用。  **取值范围**：  - true：开启binlog快速清理 - false：不开启binlog快速清理  **默认取值**：  false
        :type is_open_fast_clean: bool
        """
        
        

        self._name = None
        self._job_type = None
        self._multi_write = None
        self._engine_type = None
        self._job_direction = None
        self._task_type = None
        self._net_type = None
        self._charging_mode = None
        self._enterprise_project_id = None
        self._description = None
        self._start_time = None
        self._expired_days = None
        self._tags = None
        self._is_open_fast_clean = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if job_type is not None:
            self.job_type = job_type
        if multi_write is not None:
            self.multi_write = multi_write
        if engine_type is not None:
            self.engine_type = engine_type
        if job_direction is not None:
            self.job_direction = job_direction
        if task_type is not None:
            self.task_type = task_type
        if net_type is not None:
            self.net_type = net_type
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if description is not None:
            self.description = description
        if start_time is not None:
            self.start_time = start_time
        if expired_days is not None:
            self.expired_days = expired_days
        if tags is not None:
            self.tags = tags
        if is_open_fast_clean is not None:
            self.is_open_fast_clean = is_open_fast_clean

    @property
    def name(self):
        r"""Gets the name of this JobBaseInfo.

        **参数解释**：  任务名称，用于标识和区分不同的数据复制任务。  **约束限制**：  - 长度在4到50位之间，不区分大小写。 - 可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The name of this JobBaseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobBaseInfo.

        **参数解释**：  任务名称，用于标识和区分不同的数据复制任务。  **约束限制**：  - 长度在4到50位之间，不区分大小写。 - 可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param name: The name of this JobBaseInfo.
        :type name: str
        """
        self._name = name

    @property
    def job_type(self):
        r"""Gets the job_type of this JobBaseInfo.

        **参数解释**：  DRS任务场景类型，用于区分不同的数据复制场景。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步  **默认取值**：  不涉及

        :return: The job_type of this JobBaseInfo.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this JobBaseInfo.

        **参数解释**：  DRS任务场景类型，用于区分不同的数据复制场景。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步  **默认取值**：  不涉及

        :param job_type: The job_type of this JobBaseInfo.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def multi_write(self):
        r"""Gets the multi_write of this JobBaseInfo.

        **参数解释**：  灾备类型是否双主灾备，指定灾备场景下是否启用双向写入功能。  **约束限制**：  - job_type为cloudDataGuard时必填。  **取值范围**：  - true：双主灾备 - false：非双主灾备  **默认取值**：  false

        :return: The multi_write of this JobBaseInfo.
        :rtype: bool
        """
        return self._multi_write

    @multi_write.setter
    def multi_write(self, multi_write):
        r"""Sets the multi_write of this JobBaseInfo.

        **参数解释**：  灾备类型是否双主灾备，指定灾备场景下是否启用双向写入功能。  **约束限制**：  - job_type为cloudDataGuard时必填。  **取值范围**：  - true：双主灾备 - false：非双主灾备  **默认取值**：  false

        :param multi_write: The multi_write of this JobBaseInfo.
        :type multi_write: bool
        """
        self._multi_write = multi_write

    @property
    def engine_type(self):
        r"""Gets the engine_type of this JobBaseInfo.

        **参数解释**：  DRS任务引擎类型。  **约束限制**：  不涉及。  **取值范围**：  - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用 - redis-to-gaussredis：Redis同步到GeminiDB Redis，实时迁移场景使用 - rediscluster-to-gaussredis：Redis集群同步到GeminiDB Redis，实时迁移场景使用 - mysql-to-mysql：MySQL同步到MySQL，实时同步场景使用  **默认取值**：  不涉及

        :return: The engine_type of this JobBaseInfo.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this JobBaseInfo.

        **参数解释**：  DRS任务引擎类型。  **约束限制**：  不涉及。  **取值范围**：  - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用 - redis-to-gaussredis：Redis同步到GeminiDB Redis，实时迁移场景使用 - rediscluster-to-gaussredis：Redis集群同步到GeminiDB Redis，实时迁移场景使用 - mysql-to-mysql：MySQL同步到MySQL，实时同步场景使用  **默认取值**：  不涉及

        :param engine_type: The engine_type of this JobBaseInfo.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def job_direction(self):
        r"""Gets the job_direction of this JobBaseInfo.

        **参数解释**：  任务的迁移方向。  **约束限制**：  不涉及。  **取值范围**：  - up：入云，灾备场景时对应本云为备 - down：出云，灾备场景时对应本云为主 - non-dbs：自建  **默认取值**：  不涉及

        :return: The job_direction of this JobBaseInfo.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        r"""Sets the job_direction of this JobBaseInfo.

        **参数解释**：  任务的迁移方向。  **约束限制**：  不涉及。  **取值范围**：  - up：入云，灾备场景时对应本云为备 - down：出云，灾备场景时对应本云为主 - non-dbs：自建  **默认取值**：  不涉及

        :param job_direction: The job_direction of this JobBaseInfo.
        :type job_direction: str
        """
        self._job_direction = job_direction

    @property
    def task_type(self):
        r"""Gets the task_type of this JobBaseInfo.

        **参数解释**：  任务迁移模式，指定数据复制任务的执行方式。  **约束限制**：  不涉及。  **取值范围**：  - FULL_TRANS：全量迁移，仅迁移历史数据 - FULL_INCR_TRANS：全量+增量迁移，先迁移历史数据再持续同步增量 - INCR_TRANS：增量迁移，仅同步数据变更  **默认取值**：  不涉及

        :return: The task_type of this JobBaseInfo.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this JobBaseInfo.

        **参数解释**：  任务迁移模式，指定数据复制任务的执行方式。  **约束限制**：  不涉及。  **取值范围**：  - FULL_TRANS：全量迁移，仅迁移历史数据 - FULL_INCR_TRANS：全量+增量迁移，先迁移历史数据再持续同步增量 - INCR_TRANS：增量迁移，仅同步数据变更  **默认取值**：  不涉及

        :param task_type: The task_type of this JobBaseInfo.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def net_type(self):
        r"""Gets the net_type of this JobBaseInfo.

        **参数解释**：  任务使用的网络类型。  **约束限制**：  - 灾备场景不支持选择VPC网络。  **取值范围**：  - eip：公网网络 - vpc：VPC网络 - vpn：VPN、专线网络  **默认取值**：  不涉及

        :return: The net_type of this JobBaseInfo.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        r"""Sets the net_type of this JobBaseInfo.

        **参数解释**：  任务使用的网络类型。  **约束限制**：  - 灾备场景不支持选择VPC网络。  **取值范围**：  - eip：公网网络 - vpc：VPC网络 - vpn：VPN、专线网络  **默认取值**：  不涉及

        :param net_type: The net_type of this JobBaseInfo.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this JobBaseInfo.

        **参数解释**：  任务的计费模式，指定数据复制任务的付费方式。  **约束限制**：  不涉及。  **取值范围**：  - period：包周期 - on_demand：按需  **默认取值**：  on_demand

        :return: The charging_mode of this JobBaseInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this JobBaseInfo.

        **参数解释**：  任务的计费模式，指定数据复制任务的付费方式。  **约束限制**：  不涉及。  **取值范围**：  - period：包周期 - on_demand：按需  **默认取值**：  on_demand

        :param charging_mode: The charging_mode of this JobBaseInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this JobBaseInfo.

        **参数解释**：  企业项目ID，用于按企业项目过滤查询结果。  **约束限制**：  - 不传值时设置为null，不能设置为空字符串。 - 当企业项目开关打开时，可以传值。  **取值范围**：  不涉及。  **默认取值**：  \"0\"，表示default企业项目

        :return: The enterprise_project_id of this JobBaseInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this JobBaseInfo.

        **参数解释**：  企业项目ID，用于按企业项目过滤查询结果。  **约束限制**：  - 不传值时设置为null，不能设置为空字符串。 - 当企业项目开关打开时，可以传值。  **取值范围**：  不涉及。  **默认取值**：  \"0\"，表示default企业项目

        :param enterprise_project_id: The enterprise_project_id of this JobBaseInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def description(self):
        r"""Gets the description of this JobBaseInfo.

        **参数解释**：  任务描述，用于对数据复制任务添加补充说明信息。  **约束限制**：  - 长度不能超过256位。 - 不能包含!<>&'\"\\特殊字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The description of this JobBaseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this JobBaseInfo.

        **参数解释**：  任务描述，用于对数据复制任务添加补充说明信息。  **约束限制**：  - 长度不能超过256位。 - 不能包含!<>&'\"\\特殊字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param description: The description of this JobBaseInfo.
        :type description: str
        """
        self._description = description

    @property
    def start_time(self):
        r"""Gets the start_time of this JobBaseInfo.

        **参数解释**：  任务定时启动时间，设置后任务将在指定时间自动启动。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The start_time of this JobBaseInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this JobBaseInfo.

        **参数解释**：  任务定时启动时间，设置后任务将在指定时间自动启动。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param start_time: The start_time of this JobBaseInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def expired_days(self):
        r"""Gets the expired_days of this JobBaseInfo.

        任务处于异常状态一段时间后，将会自动结束。单位为天。(范围14-100)，不传默认为14天。

        :return: The expired_days of this JobBaseInfo.
        :rtype: str
        """
        return self._expired_days

    @expired_days.setter
    def expired_days(self, expired_days):
        r"""Sets the expired_days of this JobBaseInfo.

        任务处于异常状态一段时间后，将会自动结束。单位为天。(范围14-100)，不传默认为14天。

        :param expired_days: The expired_days of this JobBaseInfo.
        :type expired_days: str
        """
        self._expired_days = expired_days

    @property
    def tags(self):
        r"""Gets the tags of this JobBaseInfo.

        **参数解释**：  标签信息，用于为数据复制任务添加标签以便分类管理。  **约束限制**：  - 最多添加10个标签。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The tags of this JobBaseInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this JobBaseInfo.

        **参数解释**：  标签信息，用于为数据复制任务添加标签以便分类管理。  **约束限制**：  - 最多添加10个标签。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param tags: The tags of this JobBaseInfo.
        :type tags: list[:class:`huaweicloudsdkdrs.v5.ResourceTag`]
        """
        self._tags = tags

    @property
    def is_open_fast_clean(self):
        r"""Gets the is_open_fast_clean of this JobBaseInfo.

        **参数解释**：  是否开启云数据库RDS for MySQL/MariaDB的binlog快速清理，开启后可自动清理已同步的binlog以释放磁盘空间。  **约束限制**：  - 仅MySQL/MariaDB引擎类型适用。  **取值范围**：  - true：开启binlog快速清理 - false：不开启binlog快速清理  **默认取值**：  false

        :return: The is_open_fast_clean of this JobBaseInfo.
        :rtype: bool
        """
        return self._is_open_fast_clean

    @is_open_fast_clean.setter
    def is_open_fast_clean(self, is_open_fast_clean):
        r"""Sets the is_open_fast_clean of this JobBaseInfo.

        **参数解释**：  是否开启云数据库RDS for MySQL/MariaDB的binlog快速清理，开启后可自动清理已同步的binlog以释放磁盘空间。  **约束限制**：  - 仅MySQL/MariaDB引擎类型适用。  **取值范围**：  - true：开启binlog快速清理 - false：不开启binlog快速清理  **默认取值**：  false

        :param is_open_fast_clean: The is_open_fast_clean of this JobBaseInfo.
        :type is_open_fast_clean: bool
        """
        self._is_open_fast_clean = is_open_fast_clean

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
        if not isinstance(other, JobBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
