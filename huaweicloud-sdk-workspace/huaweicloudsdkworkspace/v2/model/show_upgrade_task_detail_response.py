# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUpgradeTaskDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'project_id': 'str',
        'task_name': 'str',
        'task_type': 'int',
        'scheduled_type': 'str',
        'timezone': 'str',
        'week_list': 'str',
        'month_list': 'str',
        'date_list': 'str',
        'day_interval': 'int',
        'scheduled_date': 'str',
        'scheduled_time': 'str',
        'cron_expression': 'str',
        'last_execute_status': 'str',
        'last_execute_time': 'str',
        'next_execute_time': 'str',
        'is_enable': 'int',
        'is_force_execute': 'int',
        'min_version': 'str',
        'target_version': 'str',
        'expire_enable': 'int',
        'expire_time': 'str',
        'is_notify': 'int',
        'extra_params': 'str',
        'execute_strategy': 'int',
        'grayscale_rule': 'int',
        'gray_object_ids': 'str',
        'random_first_batch_count': 'int',
        'gray_fail_threshold': 'int',
        'scheduled_end_time': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'task_name': 'task_name',
        'task_type': 'task_type',
        'scheduled_type': 'scheduled_type',
        'timezone': 'timezone',
        'week_list': 'week_list',
        'month_list': 'month_list',
        'date_list': 'date_list',
        'day_interval': 'day_interval',
        'scheduled_date': 'scheduled_date',
        'scheduled_time': 'scheduled_time',
        'cron_expression': 'cron_expression',
        'last_execute_status': 'last_execute_status',
        'last_execute_time': 'last_execute_time',
        'next_execute_time': 'next_execute_time',
        'is_enable': 'is_enable',
        'is_force_execute': 'is_force_execute',
        'min_version': 'min_version',
        'target_version': 'target_version',
        'expire_enable': 'expire_enable',
        'expire_time': 'expire_time',
        'is_notify': 'is_notify',
        'extra_params': 'extra_params',
        'execute_strategy': 'execute_strategy',
        'grayscale_rule': 'grayscale_rule',
        'gray_object_ids': 'gray_object_ids',
        'random_first_batch_count': 'random_first_batch_count',
        'gray_fail_threshold': 'gray_fail_threshold',
        'scheduled_end_time': 'scheduled_end_time',
        'description': 'description'
    }

    def __init__(self, id=None, project_id=None, task_name=None, task_type=None, scheduled_type=None, timezone=None, week_list=None, month_list=None, date_list=None, day_interval=None, scheduled_date=None, scheduled_time=None, cron_expression=None, last_execute_status=None, last_execute_time=None, next_execute_time=None, is_enable=None, is_force_execute=None, min_version=None, target_version=None, expire_enable=None, expire_time=None, is_notify=None, extra_params=None, execute_strategy=None, grayscale_rule=None, gray_object_ids=None, random_first_batch_count=None, gray_fail_threshold=None, scheduled_end_time=None, description=None):
        r"""ShowUpgradeTaskDetailResponse

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: str
        :param project_id: ID
        :type project_id: str
        :param task_name: 任务名称
        :type task_name: str
        :param task_type: 任务类型：0-云桌面 1-应用服务器 2-镜像
        :type task_type: int
        :param scheduled_type: 执行周期类型：FIXED_TIME-指定时间 DAY-按天 WEEK-按周 MONTH-按月
        :type scheduled_type: str
        :param timezone: 时区
        :type timezone: str
        :param week_list: 周期按周时：取值1~7，英文逗号分隔，如1,2,7
        :type week_list: str
        :param month_list: 周期按月时：取值1~12，英文逗号分隔
        :type month_list: str
        :param date_list: 周期按月时：取值1~31及L(代表当月最后一天)
        :type date_list: str
        :param day_interval: 按天跳过天数
        :type day_interval: int
        :param scheduled_date: 周期指定时间时：表示指定的日期
        :type scheduled_date: str
        :param scheduled_time: 指定的执行时间点
        :type scheduled_time: str
        :param cron_expression: Cron表达式
        :type cron_expression: str
        :param last_execute_status: 最近执行状态：SUCCESS-成功 FAILED-失败 RUNNING-执行中 WAITING-等待
        :type last_execute_status: str
        :param last_execute_time: 最近执行时间
        :type last_execute_time: str
        :param next_execute_time: 下次执行时间
        :type next_execute_time: str
        :param is_enable: 启用状态：0-未启用 1-启用
        :type is_enable: int
        :param is_force_execute: 是否强制升级：0-否 1-是
        :type is_force_execute: int
        :param min_version: 低于此版本升级
        :type min_version: str
        :param target_version: 升级目标版本
        :type target_version: str
        :param expire_enable: 过期时间开启：0-未开启 1-开启
        :type expire_enable: int
        :param expire_time: 过期时间
        :type expire_time: str
        :param is_notify: 是否通知：0-不通知 1-通知
        :type is_notify: int
        :param extra_params: 扩展参数（JSON格式）
        :type extra_params: str
        :param execute_strategy: 执行策略：0-全量下发 1-灰度下发
        :type execute_strategy: int
        :param grayscale_rule: 灰度规则：0-确定 1-随机（execute_strategy&#x3D;1时使用）
        :type grayscale_rule: int
        :param gray_object_ids: 灰度对象id列表
        :type gray_object_ids: str
        :param random_first_batch_count: 随机首批执行数
        :type random_first_batch_count: int
        :param gray_fail_threshold: 首批执行失败阈值
        :type gray_fail_threshold: int
        :param scheduled_end_time: 时间窗结束时间
        :type scheduled_end_time: str
        :param description: 任务描述
        :type description: str
        """
        
        super().__init__()

        self._id = None
        self._project_id = None
        self._task_name = None
        self._task_type = None
        self._scheduled_type = None
        self._timezone = None
        self._week_list = None
        self._month_list = None
        self._date_list = None
        self._day_interval = None
        self._scheduled_date = None
        self._scheduled_time = None
        self._cron_expression = None
        self._last_execute_status = None
        self._last_execute_time = None
        self._next_execute_time = None
        self._is_enable = None
        self._is_force_execute = None
        self._min_version = None
        self._target_version = None
        self._expire_enable = None
        self._expire_time = None
        self._is_notify = None
        self._extra_params = None
        self._execute_strategy = None
        self._grayscale_rule = None
        self._gray_object_ids = None
        self._random_first_batch_count = None
        self._gray_fail_threshold = None
        self._scheduled_end_time = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if task_name is not None:
            self.task_name = task_name
        if task_type is not None:
            self.task_type = task_type
        if scheduled_type is not None:
            self.scheduled_type = scheduled_type
        if timezone is not None:
            self.timezone = timezone
        if week_list is not None:
            self.week_list = week_list
        if month_list is not None:
            self.month_list = month_list
        if date_list is not None:
            self.date_list = date_list
        if day_interval is not None:
            self.day_interval = day_interval
        if scheduled_date is not None:
            self.scheduled_date = scheduled_date
        if scheduled_time is not None:
            self.scheduled_time = scheduled_time
        if cron_expression is not None:
            self.cron_expression = cron_expression
        if last_execute_status is not None:
            self.last_execute_status = last_execute_status
        if last_execute_time is not None:
            self.last_execute_time = last_execute_time
        if next_execute_time is not None:
            self.next_execute_time = next_execute_time
        if is_enable is not None:
            self.is_enable = is_enable
        if is_force_execute is not None:
            self.is_force_execute = is_force_execute
        if min_version is not None:
            self.min_version = min_version
        if target_version is not None:
            self.target_version = target_version
        if expire_enable is not None:
            self.expire_enable = expire_enable
        if expire_time is not None:
            self.expire_time = expire_time
        if is_notify is not None:
            self.is_notify = is_notify
        if extra_params is not None:
            self.extra_params = extra_params
        if execute_strategy is not None:
            self.execute_strategy = execute_strategy
        if grayscale_rule is not None:
            self.grayscale_rule = grayscale_rule
        if gray_object_ids is not None:
            self.gray_object_ids = gray_object_ids
        if random_first_batch_count is not None:
            self.random_first_batch_count = random_first_batch_count
        if gray_fail_threshold is not None:
            self.gray_fail_threshold = gray_fail_threshold
        if scheduled_end_time is not None:
            self.scheduled_end_time = scheduled_end_time
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this ShowUpgradeTaskDetailResponse.

        任务ID

        :return: The id of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowUpgradeTaskDetailResponse.

        任务ID

        :param id: The id of this ShowUpgradeTaskDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowUpgradeTaskDetailResponse.

        ID

        :return: The project_id of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowUpgradeTaskDetailResponse.

        ID

        :param project_id: The project_id of this ShowUpgradeTaskDetailResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def task_name(self):
        r"""Gets the task_name of this ShowUpgradeTaskDetailResponse.

        任务名称

        :return: The task_name of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ShowUpgradeTaskDetailResponse.

        任务名称

        :param task_name: The task_name of this ShowUpgradeTaskDetailResponse.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_type(self):
        r"""Gets the task_type of this ShowUpgradeTaskDetailResponse.

        任务类型：0-云桌面 1-应用服务器 2-镜像

        :return: The task_type of this ShowUpgradeTaskDetailResponse.
        :rtype: int
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ShowUpgradeTaskDetailResponse.

        任务类型：0-云桌面 1-应用服务器 2-镜像

        :param task_type: The task_type of this ShowUpgradeTaskDetailResponse.
        :type task_type: int
        """
        self._task_type = task_type

    @property
    def scheduled_type(self):
        r"""Gets the scheduled_type of this ShowUpgradeTaskDetailResponse.

        执行周期类型：FIXED_TIME-指定时间 DAY-按天 WEEK-按周 MONTH-按月

        :return: The scheduled_type of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._scheduled_type

    @scheduled_type.setter
    def scheduled_type(self, scheduled_type):
        r"""Sets the scheduled_type of this ShowUpgradeTaskDetailResponse.

        执行周期类型：FIXED_TIME-指定时间 DAY-按天 WEEK-按周 MONTH-按月

        :param scheduled_type: The scheduled_type of this ShowUpgradeTaskDetailResponse.
        :type scheduled_type: str
        """
        self._scheduled_type = scheduled_type

    @property
    def timezone(self):
        r"""Gets the timezone of this ShowUpgradeTaskDetailResponse.

        时区

        :return: The timezone of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        r"""Sets the timezone of this ShowUpgradeTaskDetailResponse.

        时区

        :param timezone: The timezone of this ShowUpgradeTaskDetailResponse.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def week_list(self):
        r"""Gets the week_list of this ShowUpgradeTaskDetailResponse.

        周期按周时：取值1~7，英文逗号分隔，如1,2,7

        :return: The week_list of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._week_list

    @week_list.setter
    def week_list(self, week_list):
        r"""Sets the week_list of this ShowUpgradeTaskDetailResponse.

        周期按周时：取值1~7，英文逗号分隔，如1,2,7

        :param week_list: The week_list of this ShowUpgradeTaskDetailResponse.
        :type week_list: str
        """
        self._week_list = week_list

    @property
    def month_list(self):
        r"""Gets the month_list of this ShowUpgradeTaskDetailResponse.

        周期按月时：取值1~12，英文逗号分隔

        :return: The month_list of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._month_list

    @month_list.setter
    def month_list(self, month_list):
        r"""Sets the month_list of this ShowUpgradeTaskDetailResponse.

        周期按月时：取值1~12，英文逗号分隔

        :param month_list: The month_list of this ShowUpgradeTaskDetailResponse.
        :type month_list: str
        """
        self._month_list = month_list

    @property
    def date_list(self):
        r"""Gets the date_list of this ShowUpgradeTaskDetailResponse.

        周期按月时：取值1~31及L(代表当月最后一天)

        :return: The date_list of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._date_list

    @date_list.setter
    def date_list(self, date_list):
        r"""Sets the date_list of this ShowUpgradeTaskDetailResponse.

        周期按月时：取值1~31及L(代表当月最后一天)

        :param date_list: The date_list of this ShowUpgradeTaskDetailResponse.
        :type date_list: str
        """
        self._date_list = date_list

    @property
    def day_interval(self):
        r"""Gets the day_interval of this ShowUpgradeTaskDetailResponse.

        按天跳过天数

        :return: The day_interval of this ShowUpgradeTaskDetailResponse.
        :rtype: int
        """
        return self._day_interval

    @day_interval.setter
    def day_interval(self, day_interval):
        r"""Sets the day_interval of this ShowUpgradeTaskDetailResponse.

        按天跳过天数

        :param day_interval: The day_interval of this ShowUpgradeTaskDetailResponse.
        :type day_interval: int
        """
        self._day_interval = day_interval

    @property
    def scheduled_date(self):
        r"""Gets the scheduled_date of this ShowUpgradeTaskDetailResponse.

        周期指定时间时：表示指定的日期

        :return: The scheduled_date of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._scheduled_date

    @scheduled_date.setter
    def scheduled_date(self, scheduled_date):
        r"""Sets the scheduled_date of this ShowUpgradeTaskDetailResponse.

        周期指定时间时：表示指定的日期

        :param scheduled_date: The scheduled_date of this ShowUpgradeTaskDetailResponse.
        :type scheduled_date: str
        """
        self._scheduled_date = scheduled_date

    @property
    def scheduled_time(self):
        r"""Gets the scheduled_time of this ShowUpgradeTaskDetailResponse.

        指定的执行时间点

        :return: The scheduled_time of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, scheduled_time):
        r"""Sets the scheduled_time of this ShowUpgradeTaskDetailResponse.

        指定的执行时间点

        :param scheduled_time: The scheduled_time of this ShowUpgradeTaskDetailResponse.
        :type scheduled_time: str
        """
        self._scheduled_time = scheduled_time

    @property
    def cron_expression(self):
        r"""Gets the cron_expression of this ShowUpgradeTaskDetailResponse.

        Cron表达式

        :return: The cron_expression of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._cron_expression

    @cron_expression.setter
    def cron_expression(self, cron_expression):
        r"""Sets the cron_expression of this ShowUpgradeTaskDetailResponse.

        Cron表达式

        :param cron_expression: The cron_expression of this ShowUpgradeTaskDetailResponse.
        :type cron_expression: str
        """
        self._cron_expression = cron_expression

    @property
    def last_execute_status(self):
        r"""Gets the last_execute_status of this ShowUpgradeTaskDetailResponse.

        最近执行状态：SUCCESS-成功 FAILED-失败 RUNNING-执行中 WAITING-等待

        :return: The last_execute_status of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._last_execute_status

    @last_execute_status.setter
    def last_execute_status(self, last_execute_status):
        r"""Sets the last_execute_status of this ShowUpgradeTaskDetailResponse.

        最近执行状态：SUCCESS-成功 FAILED-失败 RUNNING-执行中 WAITING-等待

        :param last_execute_status: The last_execute_status of this ShowUpgradeTaskDetailResponse.
        :type last_execute_status: str
        """
        self._last_execute_status = last_execute_status

    @property
    def last_execute_time(self):
        r"""Gets the last_execute_time of this ShowUpgradeTaskDetailResponse.

        最近执行时间

        :return: The last_execute_time of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._last_execute_time

    @last_execute_time.setter
    def last_execute_time(self, last_execute_time):
        r"""Sets the last_execute_time of this ShowUpgradeTaskDetailResponse.

        最近执行时间

        :param last_execute_time: The last_execute_time of this ShowUpgradeTaskDetailResponse.
        :type last_execute_time: str
        """
        self._last_execute_time = last_execute_time

    @property
    def next_execute_time(self):
        r"""Gets the next_execute_time of this ShowUpgradeTaskDetailResponse.

        下次执行时间

        :return: The next_execute_time of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._next_execute_time

    @next_execute_time.setter
    def next_execute_time(self, next_execute_time):
        r"""Sets the next_execute_time of this ShowUpgradeTaskDetailResponse.

        下次执行时间

        :param next_execute_time: The next_execute_time of this ShowUpgradeTaskDetailResponse.
        :type next_execute_time: str
        """
        self._next_execute_time = next_execute_time

    @property
    def is_enable(self):
        r"""Gets the is_enable of this ShowUpgradeTaskDetailResponse.

        启用状态：0-未启用 1-启用

        :return: The is_enable of this ShowUpgradeTaskDetailResponse.
        :rtype: int
        """
        return self._is_enable

    @is_enable.setter
    def is_enable(self, is_enable):
        r"""Sets the is_enable of this ShowUpgradeTaskDetailResponse.

        启用状态：0-未启用 1-启用

        :param is_enable: The is_enable of this ShowUpgradeTaskDetailResponse.
        :type is_enable: int
        """
        self._is_enable = is_enable

    @property
    def is_force_execute(self):
        r"""Gets the is_force_execute of this ShowUpgradeTaskDetailResponse.

        是否强制升级：0-否 1-是

        :return: The is_force_execute of this ShowUpgradeTaskDetailResponse.
        :rtype: int
        """
        return self._is_force_execute

    @is_force_execute.setter
    def is_force_execute(self, is_force_execute):
        r"""Sets the is_force_execute of this ShowUpgradeTaskDetailResponse.

        是否强制升级：0-否 1-是

        :param is_force_execute: The is_force_execute of this ShowUpgradeTaskDetailResponse.
        :type is_force_execute: int
        """
        self._is_force_execute = is_force_execute

    @property
    def min_version(self):
        r"""Gets the min_version of this ShowUpgradeTaskDetailResponse.

        低于此版本升级

        :return: The min_version of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._min_version

    @min_version.setter
    def min_version(self, min_version):
        r"""Sets the min_version of this ShowUpgradeTaskDetailResponse.

        低于此版本升级

        :param min_version: The min_version of this ShowUpgradeTaskDetailResponse.
        :type min_version: str
        """
        self._min_version = min_version

    @property
    def target_version(self):
        r"""Gets the target_version of this ShowUpgradeTaskDetailResponse.

        升级目标版本

        :return: The target_version of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this ShowUpgradeTaskDetailResponse.

        升级目标版本

        :param target_version: The target_version of this ShowUpgradeTaskDetailResponse.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def expire_enable(self):
        r"""Gets the expire_enable of this ShowUpgradeTaskDetailResponse.

        过期时间开启：0-未开启 1-开启

        :return: The expire_enable of this ShowUpgradeTaskDetailResponse.
        :rtype: int
        """
        return self._expire_enable

    @expire_enable.setter
    def expire_enable(self, expire_enable):
        r"""Sets the expire_enable of this ShowUpgradeTaskDetailResponse.

        过期时间开启：0-未开启 1-开启

        :param expire_enable: The expire_enable of this ShowUpgradeTaskDetailResponse.
        :type expire_enable: int
        """
        self._expire_enable = expire_enable

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ShowUpgradeTaskDetailResponse.

        过期时间

        :return: The expire_time of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ShowUpgradeTaskDetailResponse.

        过期时间

        :param expire_time: The expire_time of this ShowUpgradeTaskDetailResponse.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def is_notify(self):
        r"""Gets the is_notify of this ShowUpgradeTaskDetailResponse.

        是否通知：0-不通知 1-通知

        :return: The is_notify of this ShowUpgradeTaskDetailResponse.
        :rtype: int
        """
        return self._is_notify

    @is_notify.setter
    def is_notify(self, is_notify):
        r"""Sets the is_notify of this ShowUpgradeTaskDetailResponse.

        是否通知：0-不通知 1-通知

        :param is_notify: The is_notify of this ShowUpgradeTaskDetailResponse.
        :type is_notify: int
        """
        self._is_notify = is_notify

    @property
    def extra_params(self):
        r"""Gets the extra_params of this ShowUpgradeTaskDetailResponse.

        扩展参数（JSON格式）

        :return: The extra_params of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._extra_params

    @extra_params.setter
    def extra_params(self, extra_params):
        r"""Sets the extra_params of this ShowUpgradeTaskDetailResponse.

        扩展参数（JSON格式）

        :param extra_params: The extra_params of this ShowUpgradeTaskDetailResponse.
        :type extra_params: str
        """
        self._extra_params = extra_params

    @property
    def execute_strategy(self):
        r"""Gets the execute_strategy of this ShowUpgradeTaskDetailResponse.

        执行策略：0-全量下发 1-灰度下发

        :return: The execute_strategy of this ShowUpgradeTaskDetailResponse.
        :rtype: int
        """
        return self._execute_strategy

    @execute_strategy.setter
    def execute_strategy(self, execute_strategy):
        r"""Sets the execute_strategy of this ShowUpgradeTaskDetailResponse.

        执行策略：0-全量下发 1-灰度下发

        :param execute_strategy: The execute_strategy of this ShowUpgradeTaskDetailResponse.
        :type execute_strategy: int
        """
        self._execute_strategy = execute_strategy

    @property
    def grayscale_rule(self):
        r"""Gets the grayscale_rule of this ShowUpgradeTaskDetailResponse.

        灰度规则：0-确定 1-随机（execute_strategy=1时使用）

        :return: The grayscale_rule of this ShowUpgradeTaskDetailResponse.
        :rtype: int
        """
        return self._grayscale_rule

    @grayscale_rule.setter
    def grayscale_rule(self, grayscale_rule):
        r"""Sets the grayscale_rule of this ShowUpgradeTaskDetailResponse.

        灰度规则：0-确定 1-随机（execute_strategy=1时使用）

        :param grayscale_rule: The grayscale_rule of this ShowUpgradeTaskDetailResponse.
        :type grayscale_rule: int
        """
        self._grayscale_rule = grayscale_rule

    @property
    def gray_object_ids(self):
        r"""Gets the gray_object_ids of this ShowUpgradeTaskDetailResponse.

        灰度对象id列表

        :return: The gray_object_ids of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._gray_object_ids

    @gray_object_ids.setter
    def gray_object_ids(self, gray_object_ids):
        r"""Sets the gray_object_ids of this ShowUpgradeTaskDetailResponse.

        灰度对象id列表

        :param gray_object_ids: The gray_object_ids of this ShowUpgradeTaskDetailResponse.
        :type gray_object_ids: str
        """
        self._gray_object_ids = gray_object_ids

    @property
    def random_first_batch_count(self):
        r"""Gets the random_first_batch_count of this ShowUpgradeTaskDetailResponse.

        随机首批执行数

        :return: The random_first_batch_count of this ShowUpgradeTaskDetailResponse.
        :rtype: int
        """
        return self._random_first_batch_count

    @random_first_batch_count.setter
    def random_first_batch_count(self, random_first_batch_count):
        r"""Sets the random_first_batch_count of this ShowUpgradeTaskDetailResponse.

        随机首批执行数

        :param random_first_batch_count: The random_first_batch_count of this ShowUpgradeTaskDetailResponse.
        :type random_first_batch_count: int
        """
        self._random_first_batch_count = random_first_batch_count

    @property
    def gray_fail_threshold(self):
        r"""Gets the gray_fail_threshold of this ShowUpgradeTaskDetailResponse.

        首批执行失败阈值

        :return: The gray_fail_threshold of this ShowUpgradeTaskDetailResponse.
        :rtype: int
        """
        return self._gray_fail_threshold

    @gray_fail_threshold.setter
    def gray_fail_threshold(self, gray_fail_threshold):
        r"""Sets the gray_fail_threshold of this ShowUpgradeTaskDetailResponse.

        首批执行失败阈值

        :param gray_fail_threshold: The gray_fail_threshold of this ShowUpgradeTaskDetailResponse.
        :type gray_fail_threshold: int
        """
        self._gray_fail_threshold = gray_fail_threshold

    @property
    def scheduled_end_time(self):
        r"""Gets the scheduled_end_time of this ShowUpgradeTaskDetailResponse.

        时间窗结束时间

        :return: The scheduled_end_time of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._scheduled_end_time

    @scheduled_end_time.setter
    def scheduled_end_time(self, scheduled_end_time):
        r"""Sets the scheduled_end_time of this ShowUpgradeTaskDetailResponse.

        时间窗结束时间

        :param scheduled_end_time: The scheduled_end_time of this ShowUpgradeTaskDetailResponse.
        :type scheduled_end_time: str
        """
        self._scheduled_end_time = scheduled_end_time

    @property
    def description(self):
        r"""Gets the description of this ShowUpgradeTaskDetailResponse.

        任务描述

        :return: The description of this ShowUpgradeTaskDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowUpgradeTaskDetailResponse.

        任务描述

        :param description: The description of this ShowUpgradeTaskDetailResponse.
        :type description: str
        """
        self._description = description

    def to_dict(self):
        import warnings
        warnings.warn("ShowUpgradeTaskDetailResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowUpgradeTaskDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
