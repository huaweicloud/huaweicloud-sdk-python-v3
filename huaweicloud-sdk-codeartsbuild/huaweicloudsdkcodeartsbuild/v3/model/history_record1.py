# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HistoryRecord1:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_id': 'str',
        'job_id': 'str',
        'build_number': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'result': 'str',
        'branch': 'str',
        'commit_id': 'str',
        'commit_message': 'str',
        'executor': 'str',
        'trigger_type': 'str'
    }

    attribute_map = {
        'record_id': 'record_id',
        'job_id': 'job_id',
        'build_number': 'build_number',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'result': 'result',
        'branch': 'branch',
        'commit_id': 'commit_id',
        'commit_message': 'commit_message',
        'executor': 'executor',
        'trigger_type': 'trigger_type'
    }

    def __init__(self, record_id=None, job_id=None, build_number=None, start_time=None, end_time=None, result=None, branch=None, commit_id=None, commit_message=None, executor=None, trigger_type=None):
        """HistoryRecord1

        The model defined in huaweicloud sdk

        :param record_id: 构建记录id--唯一key
        :type record_id: str
        :param job_id: 任务id
        :type job_id: str
        :param build_number: 构建编号
        :type build_number: int
        :param start_time: 构建开始时间
        :type start_time: str
        :param end_time: 构建结束时间
        :type end_time: str
        :param result: 构建结果
        :type result: str
        :param branch: 代码分支
        :type branch: str
        :param commit_id: 代码提交的commit id
        :type commit_id: str
        :param commit_message: 代码提交时用户输入的提交信息，只有使用codehub仓库时有值
        :type commit_message: str
        :param executor: 执行构建任务的用户的用户名
        :type executor: str
        :param trigger_type: 触发方式，可选值：手工触发，定时触发，代码更新触发，流水线触发
        :type trigger_type: str
        """
        
        

        self._record_id = None
        self._job_id = None
        self._build_number = None
        self._start_time = None
        self._end_time = None
        self._result = None
        self._branch = None
        self._commit_id = None
        self._commit_message = None
        self._executor = None
        self._trigger_type = None
        self.discriminator = None

        if record_id is not None:
            self.record_id = record_id
        if job_id is not None:
            self.job_id = job_id
        if build_number is not None:
            self.build_number = build_number
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if result is not None:
            self.result = result
        if branch is not None:
            self.branch = branch
        if commit_id is not None:
            self.commit_id = commit_id
        if commit_message is not None:
            self.commit_message = commit_message
        if executor is not None:
            self.executor = executor
        if trigger_type is not None:
            self.trigger_type = trigger_type

    @property
    def record_id(self):
        """Gets the record_id of this HistoryRecord1.

        构建记录id--唯一key

        :return: The record_id of this HistoryRecord1.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this HistoryRecord1.

        构建记录id--唯一key

        :param record_id: The record_id of this HistoryRecord1.
        :type record_id: str
        """
        self._record_id = record_id

    @property
    def job_id(self):
        """Gets the job_id of this HistoryRecord1.

        任务id

        :return: The job_id of this HistoryRecord1.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this HistoryRecord1.

        任务id

        :param job_id: The job_id of this HistoryRecord1.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def build_number(self):
        """Gets the build_number of this HistoryRecord1.

        构建编号

        :return: The build_number of this HistoryRecord1.
        :rtype: int
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        """Sets the build_number of this HistoryRecord1.

        构建编号

        :param build_number: The build_number of this HistoryRecord1.
        :type build_number: int
        """
        self._build_number = build_number

    @property
    def start_time(self):
        """Gets the start_time of this HistoryRecord1.

        构建开始时间

        :return: The start_time of this HistoryRecord1.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this HistoryRecord1.

        构建开始时间

        :param start_time: The start_time of this HistoryRecord1.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this HistoryRecord1.

        构建结束时间

        :return: The end_time of this HistoryRecord1.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this HistoryRecord1.

        构建结束时间

        :param end_time: The end_time of this HistoryRecord1.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def result(self):
        """Gets the result of this HistoryRecord1.

        构建结果

        :return: The result of this HistoryRecord1.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this HistoryRecord1.

        构建结果

        :param result: The result of this HistoryRecord1.
        :type result: str
        """
        self._result = result

    @property
    def branch(self):
        """Gets the branch of this HistoryRecord1.

        代码分支

        :return: The branch of this HistoryRecord1.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this HistoryRecord1.

        代码分支

        :param branch: The branch of this HistoryRecord1.
        :type branch: str
        """
        self._branch = branch

    @property
    def commit_id(self):
        """Gets the commit_id of this HistoryRecord1.

        代码提交的commit id

        :return: The commit_id of this HistoryRecord1.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this HistoryRecord1.

        代码提交的commit id

        :param commit_id: The commit_id of this HistoryRecord1.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def commit_message(self):
        """Gets the commit_message of this HistoryRecord1.

        代码提交时用户输入的提交信息，只有使用codehub仓库时有值

        :return: The commit_message of this HistoryRecord1.
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        """Sets the commit_message of this HistoryRecord1.

        代码提交时用户输入的提交信息，只有使用codehub仓库时有值

        :param commit_message: The commit_message of this HistoryRecord1.
        :type commit_message: str
        """
        self._commit_message = commit_message

    @property
    def executor(self):
        """Gets the executor of this HistoryRecord1.

        执行构建任务的用户的用户名

        :return: The executor of this HistoryRecord1.
        :rtype: str
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        """Sets the executor of this HistoryRecord1.

        执行构建任务的用户的用户名

        :param executor: The executor of this HistoryRecord1.
        :type executor: str
        """
        self._executor = executor

    @property
    def trigger_type(self):
        """Gets the trigger_type of this HistoryRecord1.

        触发方式，可选值：手工触发，定时触发，代码更新触发，流水线触发

        :return: The trigger_type of this HistoryRecord1.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this HistoryRecord1.

        触发方式，可选值：手工触发，定时触发，代码更新触发，流水线触发

        :param trigger_type: The trigger_type of this HistoryRecord1.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

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
        if not isinstance(other, HistoryRecord1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
