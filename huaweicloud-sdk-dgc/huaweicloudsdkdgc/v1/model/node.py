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
        'type': 'str',
        'location': 'Location',
        'pre_node_name': 'list[str]',
        'conditions': 'list[Condition]',
        'properties': 'list[ModelProperty]',
        'polling_interval': 'int',
        'exec_time_out_retry': 'str',
        'max_execution_time': 'int',
        'retry_times': 'int',
        'retry_interval': 'int',
        'fail_policy': 'str',
        'event_trigger': 'Event',
        'cron_trigger': 'CronTrigger'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'location': 'location',
        'pre_node_name': 'preNodeName',
        'conditions': 'conditions',
        'properties': 'properties',
        'polling_interval': 'pollingInterval',
        'exec_time_out_retry': 'execTimeOutRetry',
        'max_execution_time': 'maxExecutionTime',
        'retry_times': 'retryTimes',
        'retry_interval': 'retryInterval',
        'fail_policy': 'failPolicy',
        'event_trigger': 'eventTrigger',
        'cron_trigger': 'cronTrigger'
    }

    def __init__(self, name=None, type=None, location=None, pre_node_name=None, conditions=None, properties=None, polling_interval=None, exec_time_out_retry=None, max_execution_time=None, retry_times=None, retry_interval=None, fail_policy=None, event_trigger=None, cron_trigger=None):
        """Node

        The model defined in huaweicloud sdk

        :param name: 节点名称，只能包含六种字符：英文字母、数字、中文、中划线、下划线和点号，且长度小于等于128个字符。同一个作业中节点名称不能重复。
        :type name: str
        :param type: 节点的类型
        :type type: str
        :param location: 
        :type location: :class:`huaweicloudsdkdgc.v1.Location`
        :param pre_node_name: 本本节点依赖的前面的节点名称列表
        :type pre_node_name: list[str]
        :param conditions: 节点执行条件，如果配置此参数，本节点是否执行由condition的字段expression所保存的EL表达式计算结果决定
        :type conditions: list[:class:`huaweicloudsdkdgc.v1.Condition`]
        :param properties: 节点属性
        :type properties: list[:class:`huaweicloudsdkdgc.v1.ModelProperty`]
        :param polling_interval: 轮询节点执行结果时间间隔
        :type polling_interval: int
        :param exec_time_out_retry: 节点是否超时重试
        :type exec_time_out_retry: str
        :param max_execution_time: 节点最大执行时间
        :type max_execution_time: int
        :param retry_times: 节点失败重试次数
        :type retry_times: int
        :param retry_interval: 失败重试时间间隔
        :type retry_interval: int
        :param fail_policy: 作业失败策略
        :type fail_policy: str
        :param event_trigger: 
        :type event_trigger: :class:`huaweicloudsdkdgc.v1.Event`
        :param cron_trigger: 
        :type cron_trigger: :class:`huaweicloudsdkdgc.v1.CronTrigger`
        """
        
        

        self._name = None
        self._type = None
        self._location = None
        self._pre_node_name = None
        self._conditions = None
        self._properties = None
        self._polling_interval = None
        self._exec_time_out_retry = None
        self._max_execution_time = None
        self._retry_times = None
        self._retry_interval = None
        self._fail_policy = None
        self._event_trigger = None
        self._cron_trigger = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.location = location
        if pre_node_name is not None:
            self.pre_node_name = pre_node_name
        if conditions is not None:
            self.conditions = conditions
        self.properties = properties
        if polling_interval is not None:
            self.polling_interval = polling_interval
        if exec_time_out_retry is not None:
            self.exec_time_out_retry = exec_time_out_retry
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

        节点名称，只能包含六种字符：英文字母、数字、中文、中划线、下划线和点号，且长度小于等于128个字符。同一个作业中节点名称不能重复。

        :return: The name of this Node.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Node.

        节点名称，只能包含六种字符：英文字母、数字、中文、中划线、下划线和点号，且长度小于等于128个字符。同一个作业中节点名称不能重复。

        :param name: The name of this Node.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this Node.

        节点的类型

        :return: The type of this Node.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Node.

        节点的类型

        :param type: The type of this Node.
        :type type: str
        """
        self._type = type

    @property
    def location(self):
        """Gets the location of this Node.

        :return: The location of this Node.
        :rtype: :class:`huaweicloudsdkdgc.v1.Location`
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Node.

        :param location: The location of this Node.
        :type location: :class:`huaweicloudsdkdgc.v1.Location`
        """
        self._location = location

    @property
    def pre_node_name(self):
        """Gets the pre_node_name of this Node.

        本本节点依赖的前面的节点名称列表

        :return: The pre_node_name of this Node.
        :rtype: list[str]
        """
        return self._pre_node_name

    @pre_node_name.setter
    def pre_node_name(self, pre_node_name):
        """Sets the pre_node_name of this Node.

        本本节点依赖的前面的节点名称列表

        :param pre_node_name: The pre_node_name of this Node.
        :type pre_node_name: list[str]
        """
        self._pre_node_name = pre_node_name

    @property
    def conditions(self):
        """Gets the conditions of this Node.

        节点执行条件，如果配置此参数，本节点是否执行由condition的字段expression所保存的EL表达式计算结果决定

        :return: The conditions of this Node.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.Condition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this Node.

        节点执行条件，如果配置此参数，本节点是否执行由condition的字段expression所保存的EL表达式计算结果决定

        :param conditions: The conditions of this Node.
        :type conditions: list[:class:`huaweicloudsdkdgc.v1.Condition`]
        """
        self._conditions = conditions

    @property
    def properties(self):
        """Gets the properties of this Node.

        节点属性

        :return: The properties of this Node.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.ModelProperty`]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Node.

        节点属性

        :param properties: The properties of this Node.
        :type properties: list[:class:`huaweicloudsdkdgc.v1.ModelProperty`]
        """
        self._properties = properties

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
    def exec_time_out_retry(self):
        """Gets the exec_time_out_retry of this Node.

        节点是否超时重试

        :return: The exec_time_out_retry of this Node.
        :rtype: str
        """
        return self._exec_time_out_retry

    @exec_time_out_retry.setter
    def exec_time_out_retry(self, exec_time_out_retry):
        """Sets the exec_time_out_retry of this Node.

        节点是否超时重试

        :param exec_time_out_retry: The exec_time_out_retry of this Node.
        :type exec_time_out_retry: str
        """
        self._exec_time_out_retry = exec_time_out_retry

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
        :rtype: :class:`huaweicloudsdkdgc.v1.Event`
        """
        return self._event_trigger

    @event_trigger.setter
    def event_trigger(self, event_trigger):
        """Sets the event_trigger of this Node.

        :param event_trigger: The event_trigger of this Node.
        :type event_trigger: :class:`huaweicloudsdkdgc.v1.Event`
        """
        self._event_trigger = event_trigger

    @property
    def cron_trigger(self):
        """Gets the cron_trigger of this Node.

        :return: The cron_trigger of this Node.
        :rtype: :class:`huaweicloudsdkdgc.v1.CronTrigger`
        """
        return self._cron_trigger

    @cron_trigger.setter
    def cron_trigger(self, cron_trigger):
        """Sets the cron_trigger of this Node.

        :param cron_trigger: The cron_trigger of this Node.
        :type cron_trigger: :class:`huaweicloudsdkdgc.v1.CronTrigger`
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
