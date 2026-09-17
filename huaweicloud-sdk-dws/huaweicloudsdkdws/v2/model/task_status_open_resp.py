# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskStatusOpenResp:

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
        'task_dead_line': 'str',
        'category': 'str',
        'status': 'str',
        'time_left': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'finished_percentage': 'str',
        'vacuumed_space': 'str',
        'table_vacuum_info': 'TableVacuumInfoOpen',
        'vacuum_info': 'list[object]',
        'table_vacuum_num_info': 'TableVacuumNumInfo'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_dead_line': 'task_dead_line',
        'category': 'category',
        'status': 'status',
        'time_left': 'time_left',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'finished_percentage': 'finished_percentage',
        'vacuumed_space': 'vacuumed_space',
        'table_vacuum_info': 'table_vacuum_info',
        'vacuum_info': 'vacuum_info',
        'table_vacuum_num_info': 'table_vacuum_num_info'
    }

    def __init__(self, task_id=None, task_dead_line=None, category=None, status=None, time_left=None, start_time=None, end_time=None, finished_percentage=None, vacuumed_space=None, table_vacuum_info=None, vacuum_info=None, table_vacuum_num_info=None):
        r"""TaskStatusOpenResp

        The model defined in huaweicloud sdk

        :param task_id: **参数解释**： 任务ID。 **默认取值**： 不涉及。
        :type task_id: str
        :param task_dead_line: **参数解释**： 任务截止时间。 **默认取值**： 不涉及。
        :type task_dead_line: str
        :param category: **参数解释**： 分类信息。 **默认取值**： VacuumFull
        :type category: str
        :param status: **参数解释**： 状态。 **默认取值**： 不涉及。
        :type status: str
        :param time_left: **参数解释**： 剩余时间。 **默认取值**： 不涉及。
        :type time_left: str
        :param start_time: **参数解释**： 开始时间。 **默认取值**： 不涉及。
        :type start_time: str
        :param end_time: **参数解释**： 结束时间。 **默认取值**： 不涉及。
        :type end_time: str
        :param finished_percentage: **参数解释**： 完成百分比。 **默认取值**： 不涉及。
        :type finished_percentage: str
        :param vacuumed_space: **参数解释**： 任务ID。 **默认取值**： 不涉及。
        :type vacuumed_space: str
        :param table_vacuum_info: 
        :type table_vacuum_info: :class:`huaweicloudsdkdws.v2.TableVacuumInfoOpen`
        :param vacuum_info: **参数解释**： Vacuum信息。 **默认取值**： 不涉及。
        :type vacuum_info: list[object]
        :param table_vacuum_num_info: 
        :type table_vacuum_num_info: :class:`huaweicloudsdkdws.v2.TableVacuumNumInfo`
        """
        
        

        self._task_id = None
        self._task_dead_line = None
        self._category = None
        self._status = None
        self._time_left = None
        self._start_time = None
        self._end_time = None
        self._finished_percentage = None
        self._vacuumed_space = None
        self._table_vacuum_info = None
        self._vacuum_info = None
        self._table_vacuum_num_info = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_dead_line is not None:
            self.task_dead_line = task_dead_line
        if category is not None:
            self.category = category
        if status is not None:
            self.status = status
        if time_left is not None:
            self.time_left = time_left
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if finished_percentage is not None:
            self.finished_percentage = finished_percentage
        if vacuumed_space is not None:
            self.vacuumed_space = vacuumed_space
        if table_vacuum_info is not None:
            self.table_vacuum_info = table_vacuum_info
        if vacuum_info is not None:
            self.vacuum_info = vacuum_info
        if table_vacuum_num_info is not None:
            self.table_vacuum_num_info = table_vacuum_num_info

    @property
    def task_id(self):
        r"""Gets the task_id of this TaskStatusOpenResp.

        **参数解释**： 任务ID。 **默认取值**： 不涉及。

        :return: The task_id of this TaskStatusOpenResp.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this TaskStatusOpenResp.

        **参数解释**： 任务ID。 **默认取值**： 不涉及。

        :param task_id: The task_id of this TaskStatusOpenResp.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_dead_line(self):
        r"""Gets the task_dead_line of this TaskStatusOpenResp.

        **参数解释**： 任务截止时间。 **默认取值**： 不涉及。

        :return: The task_dead_line of this TaskStatusOpenResp.
        :rtype: str
        """
        return self._task_dead_line

    @task_dead_line.setter
    def task_dead_line(self, task_dead_line):
        r"""Sets the task_dead_line of this TaskStatusOpenResp.

        **参数解释**： 任务截止时间。 **默认取值**： 不涉及。

        :param task_dead_line: The task_dead_line of this TaskStatusOpenResp.
        :type task_dead_line: str
        """
        self._task_dead_line = task_dead_line

    @property
    def category(self):
        r"""Gets the category of this TaskStatusOpenResp.

        **参数解释**： 分类信息。 **默认取值**： VacuumFull

        :return: The category of this TaskStatusOpenResp.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this TaskStatusOpenResp.

        **参数解释**： 分类信息。 **默认取值**： VacuumFull

        :param category: The category of this TaskStatusOpenResp.
        :type category: str
        """
        self._category = category

    @property
    def status(self):
        r"""Gets the status of this TaskStatusOpenResp.

        **参数解释**： 状态。 **默认取值**： 不涉及。

        :return: The status of this TaskStatusOpenResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TaskStatusOpenResp.

        **参数解释**： 状态。 **默认取值**： 不涉及。

        :param status: The status of this TaskStatusOpenResp.
        :type status: str
        """
        self._status = status

    @property
    def time_left(self):
        r"""Gets the time_left of this TaskStatusOpenResp.

        **参数解释**： 剩余时间。 **默认取值**： 不涉及。

        :return: The time_left of this TaskStatusOpenResp.
        :rtype: str
        """
        return self._time_left

    @time_left.setter
    def time_left(self, time_left):
        r"""Sets the time_left of this TaskStatusOpenResp.

        **参数解释**： 剩余时间。 **默认取值**： 不涉及。

        :param time_left: The time_left of this TaskStatusOpenResp.
        :type time_left: str
        """
        self._time_left = time_left

    @property
    def start_time(self):
        r"""Gets the start_time of this TaskStatusOpenResp.

        **参数解释**： 开始时间。 **默认取值**： 不涉及。

        :return: The start_time of this TaskStatusOpenResp.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TaskStatusOpenResp.

        **参数解释**： 开始时间。 **默认取值**： 不涉及。

        :param start_time: The start_time of this TaskStatusOpenResp.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this TaskStatusOpenResp.

        **参数解释**： 结束时间。 **默认取值**： 不涉及。

        :return: The end_time of this TaskStatusOpenResp.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this TaskStatusOpenResp.

        **参数解释**： 结束时间。 **默认取值**： 不涉及。

        :param end_time: The end_time of this TaskStatusOpenResp.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def finished_percentage(self):
        r"""Gets the finished_percentage of this TaskStatusOpenResp.

        **参数解释**： 完成百分比。 **默认取值**： 不涉及。

        :return: The finished_percentage of this TaskStatusOpenResp.
        :rtype: str
        """
        return self._finished_percentage

    @finished_percentage.setter
    def finished_percentage(self, finished_percentage):
        r"""Sets the finished_percentage of this TaskStatusOpenResp.

        **参数解释**： 完成百分比。 **默认取值**： 不涉及。

        :param finished_percentage: The finished_percentage of this TaskStatusOpenResp.
        :type finished_percentage: str
        """
        self._finished_percentage = finished_percentage

    @property
    def vacuumed_space(self):
        r"""Gets the vacuumed_space of this TaskStatusOpenResp.

        **参数解释**： 任务ID。 **默认取值**： 不涉及。

        :return: The vacuumed_space of this TaskStatusOpenResp.
        :rtype: str
        """
        return self._vacuumed_space

    @vacuumed_space.setter
    def vacuumed_space(self, vacuumed_space):
        r"""Sets the vacuumed_space of this TaskStatusOpenResp.

        **参数解释**： 任务ID。 **默认取值**： 不涉及。

        :param vacuumed_space: The vacuumed_space of this TaskStatusOpenResp.
        :type vacuumed_space: str
        """
        self._vacuumed_space = vacuumed_space

    @property
    def table_vacuum_info(self):
        r"""Gets the table_vacuum_info of this TaskStatusOpenResp.

        :return: The table_vacuum_info of this TaskStatusOpenResp.
        :rtype: :class:`huaweicloudsdkdws.v2.TableVacuumInfoOpen`
        """
        return self._table_vacuum_info

    @table_vacuum_info.setter
    def table_vacuum_info(self, table_vacuum_info):
        r"""Sets the table_vacuum_info of this TaskStatusOpenResp.

        :param table_vacuum_info: The table_vacuum_info of this TaskStatusOpenResp.
        :type table_vacuum_info: :class:`huaweicloudsdkdws.v2.TableVacuumInfoOpen`
        """
        self._table_vacuum_info = table_vacuum_info

    @property
    def vacuum_info(self):
        r"""Gets the vacuum_info of this TaskStatusOpenResp.

        **参数解释**： Vacuum信息。 **默认取值**： 不涉及。

        :return: The vacuum_info of this TaskStatusOpenResp.
        :rtype: list[object]
        """
        return self._vacuum_info

    @vacuum_info.setter
    def vacuum_info(self, vacuum_info):
        r"""Sets the vacuum_info of this TaskStatusOpenResp.

        **参数解释**： Vacuum信息。 **默认取值**： 不涉及。

        :param vacuum_info: The vacuum_info of this TaskStatusOpenResp.
        :type vacuum_info: list[object]
        """
        self._vacuum_info = vacuum_info

    @property
    def table_vacuum_num_info(self):
        r"""Gets the table_vacuum_num_info of this TaskStatusOpenResp.

        :return: The table_vacuum_num_info of this TaskStatusOpenResp.
        :rtype: :class:`huaweicloudsdkdws.v2.TableVacuumNumInfo`
        """
        return self._table_vacuum_num_info

    @table_vacuum_num_info.setter
    def table_vacuum_num_info(self, table_vacuum_num_info):
        r"""Sets the table_vacuum_num_info of this TaskStatusOpenResp.

        :param table_vacuum_num_info: The table_vacuum_num_info of this TaskStatusOpenResp.
        :type table_vacuum_num_info: :class:`huaweicloudsdkdws.v2.TableVacuumNumInfo`
        """
        self._table_vacuum_num_info = table_vacuum_num_info

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
        if not isinstance(other, TaskStatusOpenResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
