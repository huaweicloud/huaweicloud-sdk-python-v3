# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'name': 'str',
        'task_type': 'str',
        'run_status': 'str',
        'notify_status': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'name': 'name',
        'task_type': 'task_type',
        'run_status': 'run_status',
        'notify_status': 'notify_status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, workspace=None, name=None, task_type=None, run_status=None, notify_status=None, start_time=None, end_time=None, limit=None, offset=None):
        """ListInstancesRequest

        The model defined in huaweicloud sdk

        :param workspace: workspace 信息
        :type workspace: str
        :param name: 规则名称
        :type name: str
        :param task_type: 任务实例类型 QUALITY_TASK:质量作业 CONSISTENCY_TASK:对账作业
        :type task_type: str
        :param run_status: 状态, RUNNING:运行中,FAILED:失败,ALARMING:报警,SUCCESS:正常,SUSPENDING:暂停中,UNKNOWN:未定义
        :type run_status: str
        :param notify_status: 通知状态 NOT_TRIGGERED:未触发,SUCCESS:成功,FAILED:失败
        :type notify_status: str
        :param start_time: 最近运行时间查询区间的开始时间,13位时间戳(精确到毫秒)
        :type start_time: int
        :param end_time: 最近运行时间查询区间的结束时间,13位时间戳(精确到毫秒)
        :type end_time: int
        :param limit: 每页显示的条目数量,最大值为100
        :type limit: int
        :param offset: 分页偏移量
        :type offset: int
        """
        
        

        self._workspace = None
        self._name = None
        self._task_type = None
        self._run_status = None
        self._notify_status = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.workspace = workspace
        if name is not None:
            self.name = name
        if task_type is not None:
            self.task_type = task_type
        if run_status is not None:
            self.run_status = run_status
        if notify_status is not None:
            self.notify_status = notify_status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def workspace(self):
        """Gets the workspace of this ListInstancesRequest.

        workspace 信息

        :return: The workspace of this ListInstancesRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListInstancesRequest.

        workspace 信息

        :param workspace: The workspace of this ListInstancesRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def name(self):
        """Gets the name of this ListInstancesRequest.

        规则名称

        :return: The name of this ListInstancesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListInstancesRequest.

        规则名称

        :param name: The name of this ListInstancesRequest.
        :type name: str
        """
        self._name = name

    @property
    def task_type(self):
        """Gets the task_type of this ListInstancesRequest.

        任务实例类型 QUALITY_TASK:质量作业 CONSISTENCY_TASK:对账作业

        :return: The task_type of this ListInstancesRequest.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this ListInstancesRequest.

        任务实例类型 QUALITY_TASK:质量作业 CONSISTENCY_TASK:对账作业

        :param task_type: The task_type of this ListInstancesRequest.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def run_status(self):
        """Gets the run_status of this ListInstancesRequest.

        状态, RUNNING:运行中,FAILED:失败,ALARMING:报警,SUCCESS:正常,SUSPENDING:暂停中,UNKNOWN:未定义

        :return: The run_status of this ListInstancesRequest.
        :rtype: str
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        """Sets the run_status of this ListInstancesRequest.

        状态, RUNNING:运行中,FAILED:失败,ALARMING:报警,SUCCESS:正常,SUSPENDING:暂停中,UNKNOWN:未定义

        :param run_status: The run_status of this ListInstancesRequest.
        :type run_status: str
        """
        self._run_status = run_status

    @property
    def notify_status(self):
        """Gets the notify_status of this ListInstancesRequest.

        通知状态 NOT_TRIGGERED:未触发,SUCCESS:成功,FAILED:失败

        :return: The notify_status of this ListInstancesRequest.
        :rtype: str
        """
        return self._notify_status

    @notify_status.setter
    def notify_status(self, notify_status):
        """Sets the notify_status of this ListInstancesRequest.

        通知状态 NOT_TRIGGERED:未触发,SUCCESS:成功,FAILED:失败

        :param notify_status: The notify_status of this ListInstancesRequest.
        :type notify_status: str
        """
        self._notify_status = notify_status

    @property
    def start_time(self):
        """Gets the start_time of this ListInstancesRequest.

        最近运行时间查询区间的开始时间,13位时间戳(精确到毫秒)

        :return: The start_time of this ListInstancesRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListInstancesRequest.

        最近运行时间查询区间的开始时间,13位时间戳(精确到毫秒)

        :param start_time: The start_time of this ListInstancesRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListInstancesRequest.

        最近运行时间查询区间的结束时间,13位时间戳(精确到毫秒)

        :return: The end_time of this ListInstancesRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListInstancesRequest.

        最近运行时间查询区间的结束时间,13位时间戳(精确到毫秒)

        :param end_time: The end_time of this ListInstancesRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this ListInstancesRequest.

        每页显示的条目数量,最大值为100

        :return: The limit of this ListInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListInstancesRequest.

        每页显示的条目数量,最大值为100

        :param limit: The limit of this ListInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListInstancesRequest.

        分页偏移量

        :return: The offset of this ListInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListInstancesRequest.

        分页偏移量

        :param offset: The offset of this ListInstancesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
