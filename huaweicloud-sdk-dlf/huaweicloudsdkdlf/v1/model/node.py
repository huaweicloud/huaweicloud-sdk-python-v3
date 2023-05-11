# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Node:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'node_type': 'str',
        'location': 'Location',
        'pre_node_names': 'str',
        'condition': 'list[Condition]',
        'node_properties': 'str',
        'polling_interval': 'int',
        'max_execution_time': 'int',
        'retry_times': 'int',
        'retry_interval': 'int',
        'fail_policy': 'str',
        'event_trigger': 'Event',
        'cron_trigger': 'Cron'
    }

    attribute_map = {
        'name': 'name',
        'node_type': 'nodeType',
        'location': 'location',
        'pre_node_names': 'preNodeNames',
        'condition': 'condition',
        'node_properties': 'nodeProperties',
        'polling_interval': 'pollingInterval',
        'max_execution_time': 'maxExecutionTime',
        'retry_times': 'retryTimes',
        'retry_interval': 'retryInterval',
        'fail_policy': 'failPolicy',
        'event_trigger': 'eventTrigger',
        'cron_trigger': 'cronTrigger'
    }

    def __init__(self, name=None, node_type=None, location=None, pre_node_names=None, condition=None, node_properties=None, polling_interval=None, max_execution_time=None, retry_times=None, retry_interval=None, fail_policy=None, event_trigger=None, cron_trigger=None):
        """Node

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param node_type: 节点的类型
        :type node_type: str
        :param location: 
        :type location: :class:`huaweicloudsdkdlf.v1.Location`
        :param pre_node_names: 本节点依赖的前一个节点名称
        :type pre_node_names: str
        :param condition: 节点执行条件
        :type condition: list[:class:`huaweicloudsdkdlf.v1.Condition`]
        :param node_properties: 节点的属性
        :type node_properties: str
        :param polling_interval: 轮询节点执行结果时间间隔
        :type polling_interval: int
        :param max_execution_time: 节点最大执行时间
        :type max_execution_time: int
        :param retry_times: 节点失败重试次数
        :type retry_times: int
        :param retry_interval: 失败重试时间间隔
        :type retry_interval: int
        :param fail_policy: 作业失败策略
        :type fail_policy: str
        :param event_trigger: 
        :type event_trigger: :class:`huaweicloudsdkdlf.v1.Event`
        :param cron_trigger: 
        :type cron_trigger: :class:`huaweicloudsdkdlf.v1.Cron`
        """
        
        

        self._name = None
        self._node_type = None
        self._location = None
        self._pre_node_names = None
        self._condition = None
        self._node_properties = None
        self._polling_interval = None
        self._max_execution_time = None
        self._retry_times = None
        self._retry_interval = None
        self._fail_policy = None
        self._event_trigger = None
        self._cron_trigger = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if node_type is not None:
            self.node_type = node_type
        if location is not None:
            self.location = location
        if pre_node_names is not None:
            self.pre_node_names = pre_node_names
        if condition is not None:
            self.condition = condition
        if node_properties is not None:
            self.node_properties = node_properties
        if polling_interval is not None:
            self.polling_interval = polling_interval
        if max_execution_time is not None:
            self.max_execution_time = max_execution_time
        if retry_times is not None:
            self.retry_times = retry_times
        if retry_interval is not None:
            self.retry_interval = retry_interval
        if fail_policy is not None:
            self.fail_policy = fail_policy
        if event_trigger is not None:
            self.event_trigger = event_trigger
        if cron_trigger is not None:
            self.cron_trigger = cron_trigger

    @property
    def name(self):
        """Gets the name of this Node.

        :return: The name of this Node.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Node.

        :param name: The name of this Node.
        :type name: str
        """
        self._name = name

    @property
    def node_type(self):
        """Gets the node_type of this Node.

        节点的类型

        :return: The node_type of this Node.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this Node.

        节点的类型

        :param node_type: The node_type of this Node.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def location(self):
        """Gets the location of this Node.

        :return: The location of this Node.
        :rtype: :class:`huaweicloudsdkdlf.v1.Location`
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Node.

        :param location: The location of this Node.
        :type location: :class:`huaweicloudsdkdlf.v1.Location`
        """
        self._location = location

    @property
    def pre_node_names(self):
        """Gets the pre_node_names of this Node.

        本节点依赖的前一个节点名称

        :return: The pre_node_names of this Node.
        :rtype: str
        """
        return self._pre_node_names

    @pre_node_names.setter
    def pre_node_names(self, pre_node_names):
        """Sets the pre_node_names of this Node.

        本节点依赖的前一个节点名称

        :param pre_node_names: The pre_node_names of this Node.
        :type pre_node_names: str
        """
        self._pre_node_names = pre_node_names

    @property
    def condition(self):
        """Gets the condition of this Node.

        节点执行条件

        :return: The condition of this Node.
        :rtype: list[:class:`huaweicloudsdkdlf.v1.Condition`]
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this Node.

        节点执行条件

        :param condition: The condition of this Node.
        :type condition: list[:class:`huaweicloudsdkdlf.v1.Condition`]
        """
        self._condition = condition

    @property
    def node_properties(self):
        """Gets the node_properties of this Node.

        节点的属性

        :return: The node_properties of this Node.
        :rtype: str
        """
        return self._node_properties

    @node_properties.setter
    def node_properties(self, node_properties):
        """Sets the node_properties of this Node.

        节点的属性

        :param node_properties: The node_properties of this Node.
        :type node_properties: str
        """
        self._node_properties = node_properties

    @property
    def polling_interval(self):
        """Gets the polling_interval of this Node.

        轮询节点执行结果时间间隔

        :return: The polling_interval of this Node.
        :rtype: int
        """
        return self._polling_interval

    @polling_interval.setter
    def polling_interval(self, polling_interval):
        """Sets the polling_interval of this Node.

        轮询节点执行结果时间间隔

        :param polling_interval: The polling_interval of this Node.
        :type polling_interval: int
        """
        self._polling_interval = polling_interval

    @property
    def max_execution_time(self):
        """Gets the max_execution_time of this Node.

        节点最大执行时间

        :return: The max_execution_time of this Node.
        :rtype: int
        """
        return self._max_execution_time

    @max_execution_time.setter
    def max_execution_time(self, max_execution_time):
        """Sets the max_execution_time of this Node.

        节点最大执行时间

        :param max_execution_time: The max_execution_time of this Node.
        :type max_execution_time: int
        """
        self._max_execution_time = max_execution_time

    @property
    def retry_times(self):
        """Gets the retry_times of this Node.

        节点失败重试次数

        :return: The retry_times of this Node.
        :rtype: int
        """
        return self._retry_times

    @retry_times.setter
    def retry_times(self, retry_times):
        """Sets the retry_times of this Node.

        节点失败重试次数

        :param retry_times: The retry_times of this Node.
        :type retry_times: int
        """
        self._retry_times = retry_times

    @property
    def retry_interval(self):
        """Gets the retry_interval of this Node.

        失败重试时间间隔

        :return: The retry_interval of this Node.
        :rtype: int
        """
        return self._retry_interval

    @retry_interval.setter
    def retry_interval(self, retry_interval):
        """Sets the retry_interval of this Node.

        失败重试时间间隔

        :param retry_interval: The retry_interval of this Node.
        :type retry_interval: int
        """
        self._retry_interval = retry_interval

    @property
    def fail_policy(self):
        """Gets the fail_policy of this Node.

        作业失败策略

        :return: The fail_policy of this Node.
        :rtype: str
        """
        return self._fail_policy

    @fail_policy.setter
    def fail_policy(self, fail_policy):
        """Sets the fail_policy of this Node.

        作业失败策略

        :param fail_policy: The fail_policy of this Node.
        :type fail_policy: str
        """
        self._fail_policy = fail_policy

    @property
    def event_trigger(self):
        """Gets the event_trigger of this Node.

        :return: The event_trigger of this Node.
        :rtype: :class:`huaweicloudsdkdlf.v1.Event`
        """
        return self._event_trigger

    @event_trigger.setter
    def event_trigger(self, event_trigger):
        """Sets the event_trigger of this Node.

        :param event_trigger: The event_trigger of this Node.
        :type event_trigger: :class:`huaweicloudsdkdlf.v1.Event`
        """
        self._event_trigger = event_trigger

    @property
    def cron_trigger(self):
        """Gets the cron_trigger of this Node.

        :return: The cron_trigger of this Node.
        :rtype: :class:`huaweicloudsdkdlf.v1.Cron`
        """
        return self._cron_trigger

    @cron_trigger.setter
    def cron_trigger(self, cron_trigger):
        """Sets the cron_trigger of this Node.

        :param cron_trigger: The cron_trigger of this Node.
        :type cron_trigger: :class:`huaweicloudsdkdlf.v1.Cron`
        """
        self._cron_trigger = cron_trigger

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
        if not isinstance(other, Node):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
