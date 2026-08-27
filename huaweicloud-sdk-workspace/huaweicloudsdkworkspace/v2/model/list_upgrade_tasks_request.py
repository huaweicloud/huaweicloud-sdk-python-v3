# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUpgradeTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_name': 'str',
        'task_type': 'int',
        'scheduled_type': 'str',
        'is_enable': 'int',
        'last_execute_status': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'task_type': 'task_type',
        'scheduled_type': 'scheduled_type',
        'is_enable': 'is_enable',
        'last_execute_status': 'last_execute_status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, task_id=None, task_name=None, task_type=None, scheduled_type=None, is_enable=None, last_execute_status=None, offset=None, limit=None):
        r"""ListUpgradeTasksRequest

        The model defined in huaweicloud sdk

        :param task_id: 任务id
        :type task_id: str
        :param task_name: 任务名称（支持模糊查询）
        :type task_name: str
        :param task_type: 任务类型：0-云桌面 1-应用服务器 2-镜像
        :type task_type: int
        :param scheduled_type: 执行周期类型：FIXED_TIME-指定时间 DAY-按天 WEEK-按周 MONTH-按月
        :type scheduled_type: str
        :param is_enable: 启用状态：0-未启用 1-启用
        :type is_enable: int
        :param last_execute_status: 上次执行状态
        :type last_execute_status: str
        :param offset: 偏移量，默认0
        :type offset: int
        :param limit: 每页数量，默认10，最大100
        :type limit: int
        """
        
        

        self._task_id = None
        self._task_name = None
        self._task_type = None
        self._scheduled_type = None
        self._is_enable = None
        self._last_execute_status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if task_type is not None:
            self.task_type = task_type
        if scheduled_type is not None:
            self.scheduled_type = scheduled_type
        if is_enable is not None:
            self.is_enable = is_enable
        if last_execute_status is not None:
            self.last_execute_status = last_execute_status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def task_id(self):
        r"""Gets the task_id of this ListUpgradeTasksRequest.

        任务id

        :return: The task_id of this ListUpgradeTasksRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListUpgradeTasksRequest.

        任务id

        :param task_id: The task_id of this ListUpgradeTasksRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this ListUpgradeTasksRequest.

        任务名称（支持模糊查询）

        :return: The task_name of this ListUpgradeTasksRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ListUpgradeTasksRequest.

        任务名称（支持模糊查询）

        :param task_name: The task_name of this ListUpgradeTasksRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_type(self):
        r"""Gets the task_type of this ListUpgradeTasksRequest.

        任务类型：0-云桌面 1-应用服务器 2-镜像

        :return: The task_type of this ListUpgradeTasksRequest.
        :rtype: int
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ListUpgradeTasksRequest.

        任务类型：0-云桌面 1-应用服务器 2-镜像

        :param task_type: The task_type of this ListUpgradeTasksRequest.
        :type task_type: int
        """
        self._task_type = task_type

    @property
    def scheduled_type(self):
        r"""Gets the scheduled_type of this ListUpgradeTasksRequest.

        执行周期类型：FIXED_TIME-指定时间 DAY-按天 WEEK-按周 MONTH-按月

        :return: The scheduled_type of this ListUpgradeTasksRequest.
        :rtype: str
        """
        return self._scheduled_type

    @scheduled_type.setter
    def scheduled_type(self, scheduled_type):
        r"""Sets the scheduled_type of this ListUpgradeTasksRequest.

        执行周期类型：FIXED_TIME-指定时间 DAY-按天 WEEK-按周 MONTH-按月

        :param scheduled_type: The scheduled_type of this ListUpgradeTasksRequest.
        :type scheduled_type: str
        """
        self._scheduled_type = scheduled_type

    @property
    def is_enable(self):
        r"""Gets the is_enable of this ListUpgradeTasksRequest.

        启用状态：0-未启用 1-启用

        :return: The is_enable of this ListUpgradeTasksRequest.
        :rtype: int
        """
        return self._is_enable

    @is_enable.setter
    def is_enable(self, is_enable):
        r"""Sets the is_enable of this ListUpgradeTasksRequest.

        启用状态：0-未启用 1-启用

        :param is_enable: The is_enable of this ListUpgradeTasksRequest.
        :type is_enable: int
        """
        self._is_enable = is_enable

    @property
    def last_execute_status(self):
        r"""Gets the last_execute_status of this ListUpgradeTasksRequest.

        上次执行状态

        :return: The last_execute_status of this ListUpgradeTasksRequest.
        :rtype: str
        """
        return self._last_execute_status

    @last_execute_status.setter
    def last_execute_status(self, last_execute_status):
        r"""Sets the last_execute_status of this ListUpgradeTasksRequest.

        上次执行状态

        :param last_execute_status: The last_execute_status of this ListUpgradeTasksRequest.
        :type last_execute_status: str
        """
        self._last_execute_status = last_execute_status

    @property
    def offset(self):
        r"""Gets the offset of this ListUpgradeTasksRequest.

        偏移量，默认0

        :return: The offset of this ListUpgradeTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListUpgradeTasksRequest.

        偏移量，默认0

        :param offset: The offset of this ListUpgradeTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListUpgradeTasksRequest.

        每页数量，默认10，最大100

        :return: The limit of this ListUpgradeTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUpgradeTasksRequest.

        每页数量，默认10，最大100

        :param limit: The limit of this ListUpgradeTasksRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListUpgradeTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
