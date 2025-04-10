# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkJobExecutionGraph:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'jid': 'str',
        'name': 'str',
        'is_stoppable': 'bool',
        'state': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'duration': 'int'
    }

    attribute_map = {
        'jid': 'jid',
        'name': 'name',
        'is_stoppable': 'isStoppable',
        'state': 'state',
        'start_time': 'start-time',
        'end_time': 'end-time',
        'duration': 'duration'
    }

    def __init__(self, jid=None, name=None, is_stoppable=None, state=None, start_time=None, end_time=None, duration=None):
        r"""FlinkJobExecutionGraph

        The model defined in huaweicloud sdk

        :param jid: flink作业id。
        :type jid: str
        :param name: flink作业名字。
        :type name: str
        :param is_stoppable: 是否可停止。
        :type is_stoppable: bool
        :param state: 作业运行状态。
        :type state: str
        :param start_time: 作业启动时间。
        :type start_time: int
        :param end_time: 作业停止时间。
        :type end_time: int
        :param duration: 作业运行时长。
        :type duration: int
        """
        
        

        self._jid = None
        self._name = None
        self._is_stoppable = None
        self._state = None
        self._start_time = None
        self._end_time = None
        self._duration = None
        self.discriminator = None

        if jid is not None:
            self.jid = jid
        if name is not None:
            self.name = name
        if is_stoppable is not None:
            self.is_stoppable = is_stoppable
        if state is not None:
            self.state = state
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if duration is not None:
            self.duration = duration

    @property
    def jid(self):
        r"""Gets the jid of this FlinkJobExecutionGraph.

        flink作业id。

        :return: The jid of this FlinkJobExecutionGraph.
        :rtype: str
        """
        return self._jid

    @jid.setter
    def jid(self, jid):
        r"""Sets the jid of this FlinkJobExecutionGraph.

        flink作业id。

        :param jid: The jid of this FlinkJobExecutionGraph.
        :type jid: str
        """
        self._jid = jid

    @property
    def name(self):
        r"""Gets the name of this FlinkJobExecutionGraph.

        flink作业名字。

        :return: The name of this FlinkJobExecutionGraph.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FlinkJobExecutionGraph.

        flink作业名字。

        :param name: The name of this FlinkJobExecutionGraph.
        :type name: str
        """
        self._name = name

    @property
    def is_stoppable(self):
        r"""Gets the is_stoppable of this FlinkJobExecutionGraph.

        是否可停止。

        :return: The is_stoppable of this FlinkJobExecutionGraph.
        :rtype: bool
        """
        return self._is_stoppable

    @is_stoppable.setter
    def is_stoppable(self, is_stoppable):
        r"""Sets the is_stoppable of this FlinkJobExecutionGraph.

        是否可停止。

        :param is_stoppable: The is_stoppable of this FlinkJobExecutionGraph.
        :type is_stoppable: bool
        """
        self._is_stoppable = is_stoppable

    @property
    def state(self):
        r"""Gets the state of this FlinkJobExecutionGraph.

        作业运行状态。

        :return: The state of this FlinkJobExecutionGraph.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this FlinkJobExecutionGraph.

        作业运行状态。

        :param state: The state of this FlinkJobExecutionGraph.
        :type state: str
        """
        self._state = state

    @property
    def start_time(self):
        r"""Gets the start_time of this FlinkJobExecutionGraph.

        作业启动时间。

        :return: The start_time of this FlinkJobExecutionGraph.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this FlinkJobExecutionGraph.

        作业启动时间。

        :param start_time: The start_time of this FlinkJobExecutionGraph.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this FlinkJobExecutionGraph.

        作业停止时间。

        :return: The end_time of this FlinkJobExecutionGraph.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this FlinkJobExecutionGraph.

        作业停止时间。

        :param end_time: The end_time of this FlinkJobExecutionGraph.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def duration(self):
        r"""Gets the duration of this FlinkJobExecutionGraph.

        作业运行时长。

        :return: The duration of this FlinkJobExecutionGraph.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this FlinkJobExecutionGraph.

        作业运行时长。

        :param duration: The duration of this FlinkJobExecutionGraph.
        :type duration: int
        """
        self._duration = duration

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
        if not isinstance(other, FlinkJobExecutionGraph):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
