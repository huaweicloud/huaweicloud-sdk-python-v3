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
        r"""ActionInfo

        The model defined in huaweicloud sdk

        :param action_name: **参数解释**： 操作名称。 **取值范围**： Create：创建逻辑集群 Expand：扩容逻辑集群 Restart：重启逻辑集群 Delete：删除逻辑集群 Shrink：缩容逻辑集群
        :type action_name: str
        :param progress: **参数解释**： 操作进度，默认10。 **取值范围**： 0~100
        :type progress: int
        :param completed: **参数解释**： 操作是否完成。 **取值范围**： 不涉及。
        :type completed: bool
        :param start_time: **参数解释**： 操作开始时间。 **取值范围**： 不涉及。
        :type start_time: str
        :param end_time: **参数解释**： 操作结束时间。 **取值范围**： 不涉及。
        :type end_time: str
        :param result: **参数解释**： 操作结果。默认为空字符串。 **取值范围**： success：成功。 failed：失败。
        :type result: str
        :param logs: **参数解释**： 操作日志信息。 **取值范围**： 不涉及。
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
        r"""Gets the action_name of this ActionInfo.

        **参数解释**： 操作名称。 **取值范围**： Create：创建逻辑集群 Expand：扩容逻辑集群 Restart：重启逻辑集群 Delete：删除逻辑集群 Shrink：缩容逻辑集群

        :return: The action_name of this ActionInfo.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        r"""Sets the action_name of this ActionInfo.

        **参数解释**： 操作名称。 **取值范围**： Create：创建逻辑集群 Expand：扩容逻辑集群 Restart：重启逻辑集群 Delete：删除逻辑集群 Shrink：缩容逻辑集群

        :param action_name: The action_name of this ActionInfo.
        :type action_name: str
        """
        self._action_name = action_name

    @property
    def progress(self):
        r"""Gets the progress of this ActionInfo.

        **参数解释**： 操作进度，默认10。 **取值范围**： 0~100

        :return: The progress of this ActionInfo.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this ActionInfo.

        **参数解释**： 操作进度，默认10。 **取值范围**： 0~100

        :param progress: The progress of this ActionInfo.
        :type progress: int
        """
        self._progress = progress

    @property
    def completed(self):
        r"""Gets the completed of this ActionInfo.

        **参数解释**： 操作是否完成。 **取值范围**： 不涉及。

        :return: The completed of this ActionInfo.
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        r"""Sets the completed of this ActionInfo.

        **参数解释**： 操作是否完成。 **取值范围**： 不涉及。

        :param completed: The completed of this ActionInfo.
        :type completed: bool
        """
        self._completed = completed

    @property
    def start_time(self):
        r"""Gets the start_time of this ActionInfo.

        **参数解释**： 操作开始时间。 **取值范围**： 不涉及。

        :return: The start_time of this ActionInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ActionInfo.

        **参数解释**： 操作开始时间。 **取值范围**： 不涉及。

        :param start_time: The start_time of this ActionInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ActionInfo.

        **参数解释**： 操作结束时间。 **取值范围**： 不涉及。

        :return: The end_time of this ActionInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ActionInfo.

        **参数解释**： 操作结束时间。 **取值范围**： 不涉及。

        :param end_time: The end_time of this ActionInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def result(self):
        r"""Gets the result of this ActionInfo.

        **参数解释**： 操作结果。默认为空字符串。 **取值范围**： success：成功。 failed：失败。

        :return: The result of this ActionInfo.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ActionInfo.

        **参数解释**： 操作结果。默认为空字符串。 **取值范围**： success：成功。 failed：失败。

        :param result: The result of this ActionInfo.
        :type result: str
        """
        self._result = result

    @property
    def logs(self):
        r"""Gets the logs of this ActionInfo.

        **参数解释**： 操作日志信息。 **取值范围**： 不涉及。

        :return: The logs of this ActionInfo.
        :rtype: str
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        r"""Sets the logs of this ActionInfo.

        **参数解释**： 操作日志信息。 **取值范围**： 不涉及。

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
