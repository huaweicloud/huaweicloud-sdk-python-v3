# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DBMaskTaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_type': 'str',
        'end_time': 'int',
        'execute_line': 'int',
        'id': 'str',
        'progress': 'int',
        'run_status': 'str',
        'start_time': 'int',
        'task_template_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'db_type': 'db_type',
        'end_time': 'end_time',
        'execute_line': 'execute_line',
        'id': 'id',
        'progress': 'progress',
        'run_status': 'run_status',
        'start_time': 'start_time',
        'task_template_id': 'task_template_id',
        'type': 'type'
    }

    def __init__(self, db_type=None, end_time=None, execute_line=None, id=None, progress=None, run_status=None, start_time=None, task_template_id=None, type=None):
        """DBMaskTaskInfo

        The model defined in huaweicloud sdk

        :param db_type: DB类型
        :type db_type: str
        :param end_time: 任务结束时间
        :type end_time: int
        :param execute_line: 执行行数
        :type execute_line: int
        :param id: 任务ID
        :type id: str
        :param progress: 执行进度
        :type progress: int
        :param run_status: 任务运行状态
        :type run_status: str
        :param start_time: 任务开始时间
        :type start_time: int
        :param task_template_id: 任务模板ID
        :type task_template_id: str
        :param type: 任务类型
        :type type: str
        """
        
        

        self._db_type = None
        self._end_time = None
        self._execute_line = None
        self._id = None
        self._progress = None
        self._run_status = None
        self._start_time = None
        self._task_template_id = None
        self._type = None
        self.discriminator = None

        if db_type is not None:
            self.db_type = db_type
        if end_time is not None:
            self.end_time = end_time
        if execute_line is not None:
            self.execute_line = execute_line
        if id is not None:
            self.id = id
        if progress is not None:
            self.progress = progress
        if run_status is not None:
            self.run_status = run_status
        if start_time is not None:
            self.start_time = start_time
        if task_template_id is not None:
            self.task_template_id = task_template_id
        if type is not None:
            self.type = type

    @property
    def db_type(self):
        """Gets the db_type of this DBMaskTaskInfo.

        DB类型

        :return: The db_type of this DBMaskTaskInfo.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        """Sets the db_type of this DBMaskTaskInfo.

        DB类型

        :param db_type: The db_type of this DBMaskTaskInfo.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def end_time(self):
        """Gets the end_time of this DBMaskTaskInfo.

        任务结束时间

        :return: The end_time of this DBMaskTaskInfo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DBMaskTaskInfo.

        任务结束时间

        :param end_time: The end_time of this DBMaskTaskInfo.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def execute_line(self):
        """Gets the execute_line of this DBMaskTaskInfo.

        执行行数

        :return: The execute_line of this DBMaskTaskInfo.
        :rtype: int
        """
        return self._execute_line

    @execute_line.setter
    def execute_line(self, execute_line):
        """Sets the execute_line of this DBMaskTaskInfo.

        执行行数

        :param execute_line: The execute_line of this DBMaskTaskInfo.
        :type execute_line: int
        """
        self._execute_line = execute_line

    @property
    def id(self):
        """Gets the id of this DBMaskTaskInfo.

        任务ID

        :return: The id of this DBMaskTaskInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DBMaskTaskInfo.

        任务ID

        :param id: The id of this DBMaskTaskInfo.
        :type id: str
        """
        self._id = id

    @property
    def progress(self):
        """Gets the progress of this DBMaskTaskInfo.

        执行进度

        :return: The progress of this DBMaskTaskInfo.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this DBMaskTaskInfo.

        执行进度

        :param progress: The progress of this DBMaskTaskInfo.
        :type progress: int
        """
        self._progress = progress

    @property
    def run_status(self):
        """Gets the run_status of this DBMaskTaskInfo.

        任务运行状态

        :return: The run_status of this DBMaskTaskInfo.
        :rtype: str
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        """Sets the run_status of this DBMaskTaskInfo.

        任务运行状态

        :param run_status: The run_status of this DBMaskTaskInfo.
        :type run_status: str
        """
        self._run_status = run_status

    @property
    def start_time(self):
        """Gets the start_time of this DBMaskTaskInfo.

        任务开始时间

        :return: The start_time of this DBMaskTaskInfo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DBMaskTaskInfo.

        任务开始时间

        :param start_time: The start_time of this DBMaskTaskInfo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def task_template_id(self):
        """Gets the task_template_id of this DBMaskTaskInfo.

        任务模板ID

        :return: The task_template_id of this DBMaskTaskInfo.
        :rtype: str
        """
        return self._task_template_id

    @task_template_id.setter
    def task_template_id(self, task_template_id):
        """Sets the task_template_id of this DBMaskTaskInfo.

        任务模板ID

        :param task_template_id: The task_template_id of this DBMaskTaskInfo.
        :type task_template_id: str
        """
        self._task_template_id = task_template_id

    @property
    def type(self):
        """Gets the type of this DBMaskTaskInfo.

        任务类型

        :return: The type of this DBMaskTaskInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DBMaskTaskInfo.

        任务类型

        :param type: The type of this DBMaskTaskInfo.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, DBMaskTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
