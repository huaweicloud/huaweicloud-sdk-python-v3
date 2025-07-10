# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmHandleHistory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'work_order_id': 'str',
        'create_name': 'str',
        'create_alias': 'str',
        'task_type': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'duration': 'int',
        'status': 'str',
        'associated_task_id': 'str',
        'associated_task_name': 'str',
        'sub_task_info': 'SubTaskInfoDTO'
    }

    attribute_map = {
        'work_order_id': 'work_order_id',
        'create_name': 'create_name',
        'create_alias': 'create_alias',
        'task_type': 'task_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'duration': 'duration',
        'status': 'status',
        'associated_task_id': 'associated_task_id',
        'associated_task_name': 'associated_task_name',
        'sub_task_info': 'sub_task_info'
    }

    def __init__(self, work_order_id=None, create_name=None, create_alias=None, task_type=None, start_time=None, end_time=None, duration=None, status=None, associated_task_id=None, associated_task_name=None, sub_task_info=None):
        r"""AlarmHandleHistory

        The model defined in huaweicloud sdk

        :param work_order_id: 执行工单id
        :type work_order_id: str
        :param create_name: 创建人名
        :type create_name: str
        :param create_alias: 创建人名
        :type create_alias: str
        :param task_type: 任务类型
        :type task_type: str
        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        :param duration: 总耗时
        :type duration: int
        :param status: 状态
        :type status: str
        :param associated_task_id: 脚本或作业id
        :type associated_task_id: str
        :param associated_task_name: 脚本或作业id
        :type associated_task_name: str
        :param sub_task_info: 
        :type sub_task_info: :class:`huaweicloudsdkcoc.v1.SubTaskInfoDTO`
        """
        
        

        self._work_order_id = None
        self._create_name = None
        self._create_alias = None
        self._task_type = None
        self._start_time = None
        self._end_time = None
        self._duration = None
        self._status = None
        self._associated_task_id = None
        self._associated_task_name = None
        self._sub_task_info = None
        self.discriminator = None

        if work_order_id is not None:
            self.work_order_id = work_order_id
        if create_name is not None:
            self.create_name = create_name
        if create_alias is not None:
            self.create_alias = create_alias
        if task_type is not None:
            self.task_type = task_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if duration is not None:
            self.duration = duration
        if status is not None:
            self.status = status
        if associated_task_id is not None:
            self.associated_task_id = associated_task_id
        if associated_task_name is not None:
            self.associated_task_name = associated_task_name
        if sub_task_info is not None:
            self.sub_task_info = sub_task_info

    @property
    def work_order_id(self):
        r"""Gets the work_order_id of this AlarmHandleHistory.

        执行工单id

        :return: The work_order_id of this AlarmHandleHistory.
        :rtype: str
        """
        return self._work_order_id

    @work_order_id.setter
    def work_order_id(self, work_order_id):
        r"""Sets the work_order_id of this AlarmHandleHistory.

        执行工单id

        :param work_order_id: The work_order_id of this AlarmHandleHistory.
        :type work_order_id: str
        """
        self._work_order_id = work_order_id

    @property
    def create_name(self):
        r"""Gets the create_name of this AlarmHandleHistory.

        创建人名

        :return: The create_name of this AlarmHandleHistory.
        :rtype: str
        """
        return self._create_name

    @create_name.setter
    def create_name(self, create_name):
        r"""Sets the create_name of this AlarmHandleHistory.

        创建人名

        :param create_name: The create_name of this AlarmHandleHistory.
        :type create_name: str
        """
        self._create_name = create_name

    @property
    def create_alias(self):
        r"""Gets the create_alias of this AlarmHandleHistory.

        创建人名

        :return: The create_alias of this AlarmHandleHistory.
        :rtype: str
        """
        return self._create_alias

    @create_alias.setter
    def create_alias(self, create_alias):
        r"""Sets the create_alias of this AlarmHandleHistory.

        创建人名

        :param create_alias: The create_alias of this AlarmHandleHistory.
        :type create_alias: str
        """
        self._create_alias = create_alias

    @property
    def task_type(self):
        r"""Gets the task_type of this AlarmHandleHistory.

        任务类型

        :return: The task_type of this AlarmHandleHistory.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this AlarmHandleHistory.

        任务类型

        :param task_type: The task_type of this AlarmHandleHistory.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def start_time(self):
        r"""Gets the start_time of this AlarmHandleHistory.

        开始时间

        :return: The start_time of this AlarmHandleHistory.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this AlarmHandleHistory.

        开始时间

        :param start_time: The start_time of this AlarmHandleHistory.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this AlarmHandleHistory.

        结束时间

        :return: The end_time of this AlarmHandleHistory.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this AlarmHandleHistory.

        结束时间

        :param end_time: The end_time of this AlarmHandleHistory.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def duration(self):
        r"""Gets the duration of this AlarmHandleHistory.

        总耗时

        :return: The duration of this AlarmHandleHistory.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this AlarmHandleHistory.

        总耗时

        :param duration: The duration of this AlarmHandleHistory.
        :type duration: int
        """
        self._duration = duration

    @property
    def status(self):
        r"""Gets the status of this AlarmHandleHistory.

        状态

        :return: The status of this AlarmHandleHistory.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AlarmHandleHistory.

        状态

        :param status: The status of this AlarmHandleHistory.
        :type status: str
        """
        self._status = status

    @property
    def associated_task_id(self):
        r"""Gets the associated_task_id of this AlarmHandleHistory.

        脚本或作业id

        :return: The associated_task_id of this AlarmHandleHistory.
        :rtype: str
        """
        return self._associated_task_id

    @associated_task_id.setter
    def associated_task_id(self, associated_task_id):
        r"""Sets the associated_task_id of this AlarmHandleHistory.

        脚本或作业id

        :param associated_task_id: The associated_task_id of this AlarmHandleHistory.
        :type associated_task_id: str
        """
        self._associated_task_id = associated_task_id

    @property
    def associated_task_name(self):
        r"""Gets the associated_task_name of this AlarmHandleHistory.

        脚本或作业id

        :return: The associated_task_name of this AlarmHandleHistory.
        :rtype: str
        """
        return self._associated_task_name

    @associated_task_name.setter
    def associated_task_name(self, associated_task_name):
        r"""Sets the associated_task_name of this AlarmHandleHistory.

        脚本或作业id

        :param associated_task_name: The associated_task_name of this AlarmHandleHistory.
        :type associated_task_name: str
        """
        self._associated_task_name = associated_task_name

    @property
    def sub_task_info(self):
        r"""Gets the sub_task_info of this AlarmHandleHistory.

        :return: The sub_task_info of this AlarmHandleHistory.
        :rtype: :class:`huaweicloudsdkcoc.v1.SubTaskInfoDTO`
        """
        return self._sub_task_info

    @sub_task_info.setter
    def sub_task_info(self, sub_task_info):
        r"""Sets the sub_task_info of this AlarmHandleHistory.

        :param sub_task_info: The sub_task_info of this AlarmHandleHistory.
        :type sub_task_info: :class:`huaweicloudsdkcoc.v1.SubTaskInfoDTO`
        """
        self._sub_task_info = sub_task_info

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
        if not isinstance(other, AlarmHandleHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
