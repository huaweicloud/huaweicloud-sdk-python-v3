# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleRecordTasks:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'app': 'str',
        'stream': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'template_id': 'str',
        'stop_time': 'int',
        'task_id': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'app': 'app',
        'stream': 'stream',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'template_id': 'template_id',
        'stop_time': 'stop_time',
        'task_id': 'task_id'
    }

    def __init__(self, domain=None, app=None, stream=None, start_time=None, end_time=None, template_id=None, stop_time=None, task_id=None):
        r"""ScheduleRecordTasks

        The model defined in huaweicloud sdk

        :param domain: 推流域名
        :type domain: str
        :param app: 应用名称
        :type app: str
        :param stream: 流名称
        :type stream: str
        :param start_time: 录制任务开始时间，Unix时间戳。如果不填表示立即启动录制。EndTime - StartTime不能超过24小时。
        :type start_time: int
        :param end_time: 录制任务结束时间，Unix时间戳。设置时间必须大于StartTime及当前时间，且小于当前时间+7天。
        :type end_time: int
        :param template_id: 录制模板ID，对应模板必须存在否则会启动失败。
        :type template_id: str
        :param stop_time: 任务停止时间，当前还在生效的任务此值为0，任务未被停止但是超过了end_time后此值为自动停止时间。
        :type stop_time: int
        :param task_id: 录制任务ID
        :type task_id: str
        """
        
        

        self._domain = None
        self._app = None
        self._stream = None
        self._start_time = None
        self._end_time = None
        self._template_id = None
        self._stop_time = None
        self._task_id = None
        self.discriminator = None

        self.domain = domain
        self.app = app
        self.stream = stream
        if start_time is not None:
            self.start_time = start_time
        self.end_time = end_time
        self.template_id = template_id
        if stop_time is not None:
            self.stop_time = stop_time
        if task_id is not None:
            self.task_id = task_id

    @property
    def domain(self):
        r"""Gets the domain of this ScheduleRecordTasks.

        推流域名

        :return: The domain of this ScheduleRecordTasks.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ScheduleRecordTasks.

        推流域名

        :param domain: The domain of this ScheduleRecordTasks.
        :type domain: str
        """
        self._domain = domain

    @property
    def app(self):
        r"""Gets the app of this ScheduleRecordTasks.

        应用名称

        :return: The app of this ScheduleRecordTasks.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this ScheduleRecordTasks.

        应用名称

        :param app: The app of this ScheduleRecordTasks.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        r"""Gets the stream of this ScheduleRecordTasks.

        流名称

        :return: The stream of this ScheduleRecordTasks.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        r"""Sets the stream of this ScheduleRecordTasks.

        流名称

        :param stream: The stream of this ScheduleRecordTasks.
        :type stream: str
        """
        self._stream = stream

    @property
    def start_time(self):
        r"""Gets the start_time of this ScheduleRecordTasks.

        录制任务开始时间，Unix时间戳。如果不填表示立即启动录制。EndTime - StartTime不能超过24小时。

        :return: The start_time of this ScheduleRecordTasks.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ScheduleRecordTasks.

        录制任务开始时间，Unix时间戳。如果不填表示立即启动录制。EndTime - StartTime不能超过24小时。

        :param start_time: The start_time of this ScheduleRecordTasks.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ScheduleRecordTasks.

        录制任务结束时间，Unix时间戳。设置时间必须大于StartTime及当前时间，且小于当前时间+7天。

        :return: The end_time of this ScheduleRecordTasks.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ScheduleRecordTasks.

        录制任务结束时间，Unix时间戳。设置时间必须大于StartTime及当前时间，且小于当前时间+7天。

        :param end_time: The end_time of this ScheduleRecordTasks.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def template_id(self):
        r"""Gets the template_id of this ScheduleRecordTasks.

        录制模板ID，对应模板必须存在否则会启动失败。

        :return: The template_id of this ScheduleRecordTasks.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ScheduleRecordTasks.

        录制模板ID，对应模板必须存在否则会启动失败。

        :param template_id: The template_id of this ScheduleRecordTasks.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def stop_time(self):
        r"""Gets the stop_time of this ScheduleRecordTasks.

        任务停止时间，当前还在生效的任务此值为0，任务未被停止但是超过了end_time后此值为自动停止时间。

        :return: The stop_time of this ScheduleRecordTasks.
        :rtype: int
        """
        return self._stop_time

    @stop_time.setter
    def stop_time(self, stop_time):
        r"""Sets the stop_time of this ScheduleRecordTasks.

        任务停止时间，当前还在生效的任务此值为0，任务未被停止但是超过了end_time后此值为自动停止时间。

        :param stop_time: The stop_time of this ScheduleRecordTasks.
        :type stop_time: int
        """
        self._stop_time = stop_time

    @property
    def task_id(self):
        r"""Gets the task_id of this ScheduleRecordTasks.

        录制任务ID

        :return: The task_id of this ScheduleRecordTasks.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ScheduleRecordTasks.

        录制任务ID

        :param task_id: The task_id of this ScheduleRecordTasks.
        :type task_id: str
        """
        self._task_id = task_id

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
        if not isinstance(other, ScheduleRecordTasks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
