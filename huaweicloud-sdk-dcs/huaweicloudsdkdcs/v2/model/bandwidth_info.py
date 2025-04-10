# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandwidthInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'begin_time': 'int',
        'end_time': 'int',
        'current_time': 'int',
        'bandwidth': 'int',
        'next_expand_time': 'int',
        'expand_count': 'int',
        'expand_effect_time': 'int',
        'expand_interval_time': 'int',
        'max_expand_count': 'int',
        'task_running': 'bool',
        'assured_bandwidth': 'int',
        'max_bandwidth_for_node': 'int'
    }

    attribute_map = {
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'current_time': 'current_time',
        'bandwidth': 'bandwidth',
        'next_expand_time': 'next_expand_time',
        'expand_count': 'expand_count',
        'expand_effect_time': 'expand_effect_time',
        'expand_interval_time': 'expand_interval_time',
        'max_expand_count': 'max_expand_count',
        'task_running': 'task_running',
        'assured_bandwidth': 'assured_bandwidth',
        'max_bandwidth_for_node': 'max_bandwidth_for_node'
    }

    def __init__(self, begin_time=None, end_time=None, current_time=None, bandwidth=None, next_expand_time=None, expand_count=None, expand_effect_time=None, expand_interval_time=None, max_expand_count=None, task_running=None, assured_bandwidth=None, max_bandwidth_for_node=None):
        r"""BandwidthInfo

        The model defined in huaweicloud sdk

        :param begin_time: 临时扩容开始时间
        :type begin_time: int
        :param end_time: 临时扩容结束时间
        :type end_time: int
        :param current_time: 当前时间
        :type current_time: int
        :param bandwidth: 当前带宽，单位为GB
        :type bandwidth: int
        :param next_expand_time: 下一个扩容时间
        :type next_expand_time: int
        :param expand_count: 扩容数量
        :type expand_count: int
        :param expand_effect_time: 临时扩容时间间隔
        :type expand_effect_time: int
        :param expand_interval_time: 下一次可以扩容间隔时间
        :type expand_interval_time: int
        :param max_expand_count: 最大扩容数量
        :type max_expand_count: int
        :param task_running: 任务是否运行
        :type task_running: bool
        :param assured_bandwidth: **参数解释**： 实例基准带宽。 **取值范围**： 不涉及。 
        :type assured_bandwidth: int
        :param max_bandwidth_for_node: **参数解释**： 节点最大带宽。 **取值范围**： 不涉及。 
        :type max_bandwidth_for_node: int
        """
        
        

        self._begin_time = None
        self._end_time = None
        self._current_time = None
        self._bandwidth = None
        self._next_expand_time = None
        self._expand_count = None
        self._expand_effect_time = None
        self._expand_interval_time = None
        self._max_expand_count = None
        self._task_running = None
        self._assured_bandwidth = None
        self._max_bandwidth_for_node = None
        self.discriminator = None

        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if current_time is not None:
            self.current_time = current_time
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if next_expand_time is not None:
            self.next_expand_time = next_expand_time
        if expand_count is not None:
            self.expand_count = expand_count
        if expand_effect_time is not None:
            self.expand_effect_time = expand_effect_time
        if expand_interval_time is not None:
            self.expand_interval_time = expand_interval_time
        if max_expand_count is not None:
            self.max_expand_count = max_expand_count
        if task_running is not None:
            self.task_running = task_running
        if assured_bandwidth is not None:
            self.assured_bandwidth = assured_bandwidth
        if max_bandwidth_for_node is not None:
            self.max_bandwidth_for_node = max_bandwidth_for_node

    @property
    def begin_time(self):
        r"""Gets the begin_time of this BandwidthInfo.

        临时扩容开始时间

        :return: The begin_time of this BandwidthInfo.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this BandwidthInfo.

        临时扩容开始时间

        :param begin_time: The begin_time of this BandwidthInfo.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this BandwidthInfo.

        临时扩容结束时间

        :return: The end_time of this BandwidthInfo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this BandwidthInfo.

        临时扩容结束时间

        :param end_time: The end_time of this BandwidthInfo.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def current_time(self):
        r"""Gets the current_time of this BandwidthInfo.

        当前时间

        :return: The current_time of this BandwidthInfo.
        :rtype: int
        """
        return self._current_time

    @current_time.setter
    def current_time(self, current_time):
        r"""Sets the current_time of this BandwidthInfo.

        当前时间

        :param current_time: The current_time of this BandwidthInfo.
        :type current_time: int
        """
        self._current_time = current_time

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this BandwidthInfo.

        当前带宽，单位为GB

        :return: The bandwidth of this BandwidthInfo.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this BandwidthInfo.

        当前带宽，单位为GB

        :param bandwidth: The bandwidth of this BandwidthInfo.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def next_expand_time(self):
        r"""Gets the next_expand_time of this BandwidthInfo.

        下一个扩容时间

        :return: The next_expand_time of this BandwidthInfo.
        :rtype: int
        """
        return self._next_expand_time

    @next_expand_time.setter
    def next_expand_time(self, next_expand_time):
        r"""Sets the next_expand_time of this BandwidthInfo.

        下一个扩容时间

        :param next_expand_time: The next_expand_time of this BandwidthInfo.
        :type next_expand_time: int
        """
        self._next_expand_time = next_expand_time

    @property
    def expand_count(self):
        r"""Gets the expand_count of this BandwidthInfo.

        扩容数量

        :return: The expand_count of this BandwidthInfo.
        :rtype: int
        """
        return self._expand_count

    @expand_count.setter
    def expand_count(self, expand_count):
        r"""Sets the expand_count of this BandwidthInfo.

        扩容数量

        :param expand_count: The expand_count of this BandwidthInfo.
        :type expand_count: int
        """
        self._expand_count = expand_count

    @property
    def expand_effect_time(self):
        r"""Gets the expand_effect_time of this BandwidthInfo.

        临时扩容时间间隔

        :return: The expand_effect_time of this BandwidthInfo.
        :rtype: int
        """
        return self._expand_effect_time

    @expand_effect_time.setter
    def expand_effect_time(self, expand_effect_time):
        r"""Sets the expand_effect_time of this BandwidthInfo.

        临时扩容时间间隔

        :param expand_effect_time: The expand_effect_time of this BandwidthInfo.
        :type expand_effect_time: int
        """
        self._expand_effect_time = expand_effect_time

    @property
    def expand_interval_time(self):
        r"""Gets the expand_interval_time of this BandwidthInfo.

        下一次可以扩容间隔时间

        :return: The expand_interval_time of this BandwidthInfo.
        :rtype: int
        """
        return self._expand_interval_time

    @expand_interval_time.setter
    def expand_interval_time(self, expand_interval_time):
        r"""Sets the expand_interval_time of this BandwidthInfo.

        下一次可以扩容间隔时间

        :param expand_interval_time: The expand_interval_time of this BandwidthInfo.
        :type expand_interval_time: int
        """
        self._expand_interval_time = expand_interval_time

    @property
    def max_expand_count(self):
        r"""Gets the max_expand_count of this BandwidthInfo.

        最大扩容数量

        :return: The max_expand_count of this BandwidthInfo.
        :rtype: int
        """
        return self._max_expand_count

    @max_expand_count.setter
    def max_expand_count(self, max_expand_count):
        r"""Sets the max_expand_count of this BandwidthInfo.

        最大扩容数量

        :param max_expand_count: The max_expand_count of this BandwidthInfo.
        :type max_expand_count: int
        """
        self._max_expand_count = max_expand_count

    @property
    def task_running(self):
        r"""Gets the task_running of this BandwidthInfo.

        任务是否运行

        :return: The task_running of this BandwidthInfo.
        :rtype: bool
        """
        return self._task_running

    @task_running.setter
    def task_running(self, task_running):
        r"""Sets the task_running of this BandwidthInfo.

        任务是否运行

        :param task_running: The task_running of this BandwidthInfo.
        :type task_running: bool
        """
        self._task_running = task_running

    @property
    def assured_bandwidth(self):
        r"""Gets the assured_bandwidth of this BandwidthInfo.

        **参数解释**： 实例基准带宽。 **取值范围**： 不涉及。 

        :return: The assured_bandwidth of this BandwidthInfo.
        :rtype: int
        """
        return self._assured_bandwidth

    @assured_bandwidth.setter
    def assured_bandwidth(self, assured_bandwidth):
        r"""Sets the assured_bandwidth of this BandwidthInfo.

        **参数解释**： 实例基准带宽。 **取值范围**： 不涉及。 

        :param assured_bandwidth: The assured_bandwidth of this BandwidthInfo.
        :type assured_bandwidth: int
        """
        self._assured_bandwidth = assured_bandwidth

    @property
    def max_bandwidth_for_node(self):
        r"""Gets the max_bandwidth_for_node of this BandwidthInfo.

        **参数解释**： 节点最大带宽。 **取值范围**： 不涉及。 

        :return: The max_bandwidth_for_node of this BandwidthInfo.
        :rtype: int
        """
        return self._max_bandwidth_for_node

    @max_bandwidth_for_node.setter
    def max_bandwidth_for_node(self, max_bandwidth_for_node):
        r"""Sets the max_bandwidth_for_node of this BandwidthInfo.

        **参数解释**： 节点最大带宽。 **取值范围**： 不涉及。 

        :param max_bandwidth_for_node: The max_bandwidth_for_node of this BandwidthInfo.
        :type max_bandwidth_for_node: int
        """
        self._max_bandwidth_for_node = max_bandwidth_for_node

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
        if not isinstance(other, BandwidthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
