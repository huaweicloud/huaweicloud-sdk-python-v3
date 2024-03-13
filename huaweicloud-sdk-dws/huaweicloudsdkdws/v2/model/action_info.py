# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_name': 'str',
        'progress': 'int',
        'completed': 'bool',
        'start_time': 'str',
        'end_time': 'str',
        'result': 'str',
        'logs': 'str'
    }

    attribute_map = {
        'action_name': 'action_name',
        'progress': 'progress',
        'completed': 'completed',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'result': 'result',
        'logs': 'logs'
    }

    def __init__(self, action_name=None, progress=None, completed=None, start_time=None, end_time=None, result=None, logs=None):
        """ActionInfo

        The model defined in huaweicloud sdk

        :param action_name: 操作名称。当前只允许Create,Expand,Restart,Delete,Shrink
        :type action_name: str
        :param progress: 操作进度，默认10
        :type progress: int
        :param completed: 是否完成操作
        :type completed: bool
        :param start_time: 操作开始时间
        :type start_time: str
        :param end_time: 操作结束时间
        :type end_time: str
        :param result: 操作结果。success或者failed，默认空字符串
        :type result: str
        :param logs: 操作日志
        :type logs: str
        """
        
        

        self._action_name = None
        self._progress = None
        self._completed = None
        self._start_time = None
        self._end_time = None
        self._result = None
        self._logs = None
        self.discriminator = None

        if action_name is not None:
            self.action_name = action_name
        if progress is not None:
            self.progress = progress
        if completed is not None:
            self.completed = completed
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if result is not None:
            self.result = result
        if logs is not None:
            self.logs = logs

    @property
    def action_name(self):
        """Gets the action_name of this ActionInfo.

        操作名称。当前只允许Create,Expand,Restart,Delete,Shrink

        :return: The action_name of this ActionInfo.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        """Sets the action_name of this ActionInfo.

        操作名称。当前只允许Create,Expand,Restart,Delete,Shrink

        :param action_name: The action_name of this ActionInfo.
        :type action_name: str
        """
        self._action_name = action_name

    @property
    def progress(self):
        """Gets the progress of this ActionInfo.

        操作进度，默认10

        :return: The progress of this ActionInfo.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ActionInfo.

        操作进度，默认10

        :param progress: The progress of this ActionInfo.
        :type progress: int
        """
        self._progress = progress

    @property
    def completed(self):
        """Gets the completed of this ActionInfo.

        是否完成操作

        :return: The completed of this ActionInfo.
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this ActionInfo.

        是否完成操作

        :param completed: The completed of this ActionInfo.
        :type completed: bool
        """
        self._completed = completed

    @property
    def start_time(self):
        """Gets the start_time of this ActionInfo.

        操作开始时间

        :return: The start_time of this ActionInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ActionInfo.

        操作开始时间

        :param start_time: The start_time of this ActionInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ActionInfo.

        操作结束时间

        :return: The end_time of this ActionInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ActionInfo.

        操作结束时间

        :param end_time: The end_time of this ActionInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def result(self):
        """Gets the result of this ActionInfo.

        操作结果。success或者failed，默认空字符串

        :return: The result of this ActionInfo.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ActionInfo.

        操作结果。success或者failed，默认空字符串

        :param result: The result of this ActionInfo.
        :type result: str
        """
        self._result = result

    @property
    def logs(self):
        """Gets the logs of this ActionInfo.

        操作日志

        :return: The logs of this ActionInfo.
        :rtype: str
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this ActionInfo.

        操作日志

        :param logs: The logs of this ActionInfo.
        :type logs: str
        """
        self._logs = logs

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
        if not isinstance(other, ActionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
