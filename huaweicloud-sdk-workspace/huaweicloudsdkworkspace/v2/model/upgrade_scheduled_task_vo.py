# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeScheduledTaskVO:

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
        'task_name': 'str',
        'task_type': 'int',
        'scheduled_type': 'str',
        'timezone': 'str',
        'last_execute_status': 'str',
        'next_execute_time': 'str',
        'is_enable': 'int',
        'target_version': 'str',
        'execute_strategy': 'int',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'task_name': 'task_name',
        'task_type': 'task_type',
        'scheduled_type': 'scheduled_type',
        'timezone': 'timezone',
        'last_execute_status': 'last_execute_status',
        'next_execute_time': 'next_execute_time',
        'is_enable': 'is_enable',
        'target_version': 'target_version',
        'execute_strategy': 'execute_strategy',
        'description': 'description'
    }

    def __init__(self, id=None, task_name=None, task_type=None, scheduled_type=None, timezone=None, last_execute_status=None, next_execute_time=None, is_enable=None, target_version=None, execute_strategy=None, description=None):
        r"""UpgradeScheduledTaskVO

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: str
        :param task_name: 任务名称
        :type task_name: str
        :param task_type: 任务类型：0-云桌面 1-应用服务器 2-镜像
        :type task_type: int
        :param scheduled_type: 执行周期类型：FIXED_TIME-指定时间 DAY-按天 WEEK-按周 MONTH-按月
        :type scheduled_type: str
        :param timezone: 时区
        :type timezone: str
        :param last_execute_status: 最近一次执行情况：SUCCESS-成功 FAILED-失败 RUNNING-执行中 WAITING-等待
        :type last_execute_status: str
        :param next_execute_time: 下次执行时间
        :type next_execute_time: str
        :param is_enable: 启用状态：0-未启用 1-启用
        :type is_enable: int
        :param target_version: 目标版本
        :type target_version: str
        :param execute_strategy: 执行策略：0-全量下发 1-灰度下发
        :type execute_strategy: int
        :param description: 任务描述
        :type description: str
        """
        
        

        self._id = None
        self._task_name = None
        self._task_type = None
        self._scheduled_type = None
        self._timezone = None
        self._last_execute_status = None
        self._next_execute_time = None
        self._is_enable = None
        self._target_version = None
        self._execute_strategy = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_name is not None:
            self.task_name = task_name
        if task_type is not None:
            self.task_type = task_type
        if scheduled_type is not None:
            self.scheduled_type = scheduled_type
        if timezone is not None:
            self.timezone = timezone
        if last_execute_status is not None:
            self.last_execute_status = last_execute_status
        if next_execute_time is not None:
            self.next_execute_time = next_execute_time
        if is_enable is not None:
            self.is_enable = is_enable
        if target_version is not None:
            self.target_version = target_version
        if execute_strategy is not None:
            self.execute_strategy = execute_strategy
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this UpgradeScheduledTaskVO.

        任务ID

        :return: The id of this UpgradeScheduledTaskVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpgradeScheduledTaskVO.

        任务ID

        :param id: The id of this UpgradeScheduledTaskVO.
        :type id: str
        """
        self._id = id

    @property
    def task_name(self):
        r"""Gets the task_name of this UpgradeScheduledTaskVO.

        任务名称

        :return: The task_name of this UpgradeScheduledTaskVO.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this UpgradeScheduledTaskVO.

        任务名称

        :param task_name: The task_name of this UpgradeScheduledTaskVO.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_type(self):
        r"""Gets the task_type of this UpgradeScheduledTaskVO.

        任务类型：0-云桌面 1-应用服务器 2-镜像

        :return: The task_type of this UpgradeScheduledTaskVO.
        :rtype: int
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this UpgradeScheduledTaskVO.

        任务类型：0-云桌面 1-应用服务器 2-镜像

        :param task_type: The task_type of this UpgradeScheduledTaskVO.
        :type task_type: int
        """
        self._task_type = task_type

    @property
    def scheduled_type(self):
        r"""Gets the scheduled_type of this UpgradeScheduledTaskVO.

        执行周期类型：FIXED_TIME-指定时间 DAY-按天 WEEK-按周 MONTH-按月

        :return: The scheduled_type of this UpgradeScheduledTaskVO.
        :rtype: str
        """
        return self._scheduled_type

    @scheduled_type.setter
    def scheduled_type(self, scheduled_type):
        r"""Sets the scheduled_type of this UpgradeScheduledTaskVO.

        执行周期类型：FIXED_TIME-指定时间 DAY-按天 WEEK-按周 MONTH-按月

        :param scheduled_type: The scheduled_type of this UpgradeScheduledTaskVO.
        :type scheduled_type: str
        """
        self._scheduled_type = scheduled_type

    @property
    def timezone(self):
        r"""Gets the timezone of this UpgradeScheduledTaskVO.

        时区

        :return: The timezone of this UpgradeScheduledTaskVO.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        r"""Sets the timezone of this UpgradeScheduledTaskVO.

        时区

        :param timezone: The timezone of this UpgradeScheduledTaskVO.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def last_execute_status(self):
        r"""Gets the last_execute_status of this UpgradeScheduledTaskVO.

        最近一次执行情况：SUCCESS-成功 FAILED-失败 RUNNING-执行中 WAITING-等待

        :return: The last_execute_status of this UpgradeScheduledTaskVO.
        :rtype: str
        """
        return self._last_execute_status

    @last_execute_status.setter
    def last_execute_status(self, last_execute_status):
        r"""Sets the last_execute_status of this UpgradeScheduledTaskVO.

        最近一次执行情况：SUCCESS-成功 FAILED-失败 RUNNING-执行中 WAITING-等待

        :param last_execute_status: The last_execute_status of this UpgradeScheduledTaskVO.
        :type last_execute_status: str
        """
        self._last_execute_status = last_execute_status

    @property
    def next_execute_time(self):
        r"""Gets the next_execute_time of this UpgradeScheduledTaskVO.

        下次执行时间

        :return: The next_execute_time of this UpgradeScheduledTaskVO.
        :rtype: str
        """
        return self._next_execute_time

    @next_execute_time.setter
    def next_execute_time(self, next_execute_time):
        r"""Sets the next_execute_time of this UpgradeScheduledTaskVO.

        下次执行时间

        :param next_execute_time: The next_execute_time of this UpgradeScheduledTaskVO.
        :type next_execute_time: str
        """
        self._next_execute_time = next_execute_time

    @property
    def is_enable(self):
        r"""Gets the is_enable of this UpgradeScheduledTaskVO.

        启用状态：0-未启用 1-启用

        :return: The is_enable of this UpgradeScheduledTaskVO.
        :rtype: int
        """
        return self._is_enable

    @is_enable.setter
    def is_enable(self, is_enable):
        r"""Sets the is_enable of this UpgradeScheduledTaskVO.

        启用状态：0-未启用 1-启用

        :param is_enable: The is_enable of this UpgradeScheduledTaskVO.
        :type is_enable: int
        """
        self._is_enable = is_enable

    @property
    def target_version(self):
        r"""Gets the target_version of this UpgradeScheduledTaskVO.

        目标版本

        :return: The target_version of this UpgradeScheduledTaskVO.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this UpgradeScheduledTaskVO.

        目标版本

        :param target_version: The target_version of this UpgradeScheduledTaskVO.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def execute_strategy(self):
        r"""Gets the execute_strategy of this UpgradeScheduledTaskVO.

        执行策略：0-全量下发 1-灰度下发

        :return: The execute_strategy of this UpgradeScheduledTaskVO.
        :rtype: int
        """
        return self._execute_strategy

    @execute_strategy.setter
    def execute_strategy(self, execute_strategy):
        r"""Sets the execute_strategy of this UpgradeScheduledTaskVO.

        执行策略：0-全量下发 1-灰度下发

        :param execute_strategy: The execute_strategy of this UpgradeScheduledTaskVO.
        :type execute_strategy: int
        """
        self._execute_strategy = execute_strategy

    @property
    def description(self):
        r"""Gets the description of this UpgradeScheduledTaskVO.

        任务描述

        :return: The description of this UpgradeScheduledTaskVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpgradeScheduledTaskVO.

        任务描述

        :param description: The description of this UpgradeScheduledTaskVO.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UpgradeScheduledTaskVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
