# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduledTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'task_name': 'str',
        'task_type': 'str',
        'scheduled_type': 'str',
        'life_cycle_type': 'str',
        'last_status': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'task_name': 'task_name',
        'task_type': 'task_type',
        'scheduled_type': 'scheduled_type',
        'life_cycle_type': 'life_cycle_type',
        'last_status': 'last_status'
    }

    def __init__(self, offset=None, limit=None, task_name=None, task_type=None, scheduled_type=None, life_cycle_type=None, last_status=None):
        r"""ListScheduledTasksRequest

        The model defined in huaweicloud sdk

        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param limit: 用于分页查询，每页返回的个数，取值范围0~50。
        :type limit: int
        :param task_name: 任务名称。
        :type task_name: str
        :param task_type: 任务类型。START：开机，STOP：关机，REBOOT：重启，HIBERNATE：休眠，REBUILD：重建系统盘，EXECUTE_SCRIPT：执行脚本，CREATE_SNAPSHOT：创建EVS镜像。
        :type task_type: str
        :param scheduled_type: 执行周期类型。FIXED_TIME：指定时间，DAY：按天，WEEK：按周，MONTH：按月，LIFE_CYCLE：触发式。指定LIFE_CYCLE时，才返回触发式任务。
        :type scheduled_type: str
        :param life_cycle_type: 触发场景类型。POST_CREATE_DESKTOP_SUCCESS：创建桌面成功后，POST_REBUILD_DESKTOP_SUCCESS：重建桌面成功后，POST_REATTACH_DESKTOP_SUCCESS：触发重建的分配用户任务成功后，POST_DESKTOP_DISCONNECTED：桌面断开连接后。
        :type life_cycle_type: str
        :param last_status: 最近一次执行状态。SUCCESS：成功，SKIP：跳过，FAIL：失败。
        :type last_status: str
        """
        
        

        self._offset = None
        self._limit = None
        self._task_name = None
        self._task_type = None
        self._scheduled_type = None
        self._life_cycle_type = None
        self._last_status = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        if task_name is not None:
            self.task_name = task_name
        if task_type is not None:
            self.task_type = task_type
        if scheduled_type is not None:
            self.scheduled_type = scheduled_type
        if life_cycle_type is not None:
            self.life_cycle_type = life_cycle_type
        if last_status is not None:
            self.last_status = last_status

    @property
    def offset(self):
        r"""Gets the offset of this ListScheduledTasksRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListScheduledTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListScheduledTasksRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListScheduledTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListScheduledTasksRequest.

        用于分页查询，每页返回的个数，取值范围0~50。

        :return: The limit of this ListScheduledTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScheduledTasksRequest.

        用于分页查询，每页返回的个数，取值范围0~50。

        :param limit: The limit of this ListScheduledTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def task_name(self):
        r"""Gets the task_name of this ListScheduledTasksRequest.

        任务名称。

        :return: The task_name of this ListScheduledTasksRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ListScheduledTasksRequest.

        任务名称。

        :param task_name: The task_name of this ListScheduledTasksRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_type(self):
        r"""Gets the task_type of this ListScheduledTasksRequest.

        任务类型。START：开机，STOP：关机，REBOOT：重启，HIBERNATE：休眠，REBUILD：重建系统盘，EXECUTE_SCRIPT：执行脚本，CREATE_SNAPSHOT：创建EVS镜像。

        :return: The task_type of this ListScheduledTasksRequest.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ListScheduledTasksRequest.

        任务类型。START：开机，STOP：关机，REBOOT：重启，HIBERNATE：休眠，REBUILD：重建系统盘，EXECUTE_SCRIPT：执行脚本，CREATE_SNAPSHOT：创建EVS镜像。

        :param task_type: The task_type of this ListScheduledTasksRequest.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def scheduled_type(self):
        r"""Gets the scheduled_type of this ListScheduledTasksRequest.

        执行周期类型。FIXED_TIME：指定时间，DAY：按天，WEEK：按周，MONTH：按月，LIFE_CYCLE：触发式。指定LIFE_CYCLE时，才返回触发式任务。

        :return: The scheduled_type of this ListScheduledTasksRequest.
        :rtype: str
        """
        return self._scheduled_type

    @scheduled_type.setter
    def scheduled_type(self, scheduled_type):
        r"""Sets the scheduled_type of this ListScheduledTasksRequest.

        执行周期类型。FIXED_TIME：指定时间，DAY：按天，WEEK：按周，MONTH：按月，LIFE_CYCLE：触发式。指定LIFE_CYCLE时，才返回触发式任务。

        :param scheduled_type: The scheduled_type of this ListScheduledTasksRequest.
        :type scheduled_type: str
        """
        self._scheduled_type = scheduled_type

    @property
    def life_cycle_type(self):
        r"""Gets the life_cycle_type of this ListScheduledTasksRequest.

        触发场景类型。POST_CREATE_DESKTOP_SUCCESS：创建桌面成功后，POST_REBUILD_DESKTOP_SUCCESS：重建桌面成功后，POST_REATTACH_DESKTOP_SUCCESS：触发重建的分配用户任务成功后，POST_DESKTOP_DISCONNECTED：桌面断开连接后。

        :return: The life_cycle_type of this ListScheduledTasksRequest.
        :rtype: str
        """
        return self._life_cycle_type

    @life_cycle_type.setter
    def life_cycle_type(self, life_cycle_type):
        r"""Sets the life_cycle_type of this ListScheduledTasksRequest.

        触发场景类型。POST_CREATE_DESKTOP_SUCCESS：创建桌面成功后，POST_REBUILD_DESKTOP_SUCCESS：重建桌面成功后，POST_REATTACH_DESKTOP_SUCCESS：触发重建的分配用户任务成功后，POST_DESKTOP_DISCONNECTED：桌面断开连接后。

        :param life_cycle_type: The life_cycle_type of this ListScheduledTasksRequest.
        :type life_cycle_type: str
        """
        self._life_cycle_type = life_cycle_type

    @property
    def last_status(self):
        r"""Gets the last_status of this ListScheduledTasksRequest.

        最近一次执行状态。SUCCESS：成功，SKIP：跳过，FAIL：失败。

        :return: The last_status of this ListScheduledTasksRequest.
        :rtype: str
        """
        return self._last_status

    @last_status.setter
    def last_status(self, last_status):
        r"""Sets the last_status of this ListScheduledTasksRequest.

        最近一次执行状态。SUCCESS：成功，SKIP：跳过，FAIL：失败。

        :param last_status: The last_status of this ListScheduledTasksRequest.
        :type last_status: str
        """
        self._last_status = last_status

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
        if not isinstance(other, ListScheduledTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
