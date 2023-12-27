# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Event:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_type': 'str',
        'channel': 'str',
        'fail_policy': 'str',
        'concurrent': 'int',
        'read_policy': 'str'
    }

    attribute_map = {
        'event_type': 'event_type',
        'channel': 'channel',
        'fail_policy': 'fail_policy',
        'concurrent': 'concurrent',
        'read_policy': 'read_policy'
    }

    def __init__(self, event_type=None, channel=None, fail_policy=None, concurrent=None, read_policy=None):
        """Event

        The model defined in huaweicloud sdk

        :param event_type: 事件类型。 - KAFKA: 选择对应的连接名称与topic，当有新的kafka消息时将会触发作业运行一次 - DIS: 当前只支持监听DIS通道的新上报数据事件，每上报一条数据，触发作业运行一次。 - OBS: 选择要监听的OBS路径，如果该路径下有新增文件，则触发调度；新增的文件的路径名，可以通过变量Job.trigger.obsNewFiles引用。前提条件：该OBS路径已经配置DIS消息通知。
        :type event_type: str
        :param channel: DIS通道名称。通过DIS管理控制台获取通道名称：登录管理控制台。单击“数据接入服务”，左侧列表选择“通道管理”。通道管理页面中列出了用户拥有的通道
        :type channel: str
        :param fail_policy: 执行失败处理策略。 - SUSPEND: 挂起 - IGNORE：忽略失败，读取下一事件
        :type fail_policy: str
        :param concurrent: 调度并发数
        :type concurrent: int
        :param read_policy: 读取策略。 - LAST: 从上次位置读取 - NEW：从最新位置读取
        :type read_policy: str
        """
        
        

        self._event_type = None
        self._channel = None
        self._fail_policy = None
        self._concurrent = None
        self._read_policy = None
        self.discriminator = None

        self.event_type = event_type
        self.channel = channel
        if fail_policy is not None:
            self.fail_policy = fail_policy
        if concurrent is not None:
            self.concurrent = concurrent
        if read_policy is not None:
            self.read_policy = read_policy

    @property
    def event_type(self):
        """Gets the event_type of this Event.

        事件类型。 - KAFKA: 选择对应的连接名称与topic，当有新的kafka消息时将会触发作业运行一次 - DIS: 当前只支持监听DIS通道的新上报数据事件，每上报一条数据，触发作业运行一次。 - OBS: 选择要监听的OBS路径，如果该路径下有新增文件，则触发调度；新增的文件的路径名，可以通过变量Job.trigger.obsNewFiles引用。前提条件：该OBS路径已经配置DIS消息通知。

        :return: The event_type of this Event.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this Event.

        事件类型。 - KAFKA: 选择对应的连接名称与topic，当有新的kafka消息时将会触发作业运行一次 - DIS: 当前只支持监听DIS通道的新上报数据事件，每上报一条数据，触发作业运行一次。 - OBS: 选择要监听的OBS路径，如果该路径下有新增文件，则触发调度；新增的文件的路径名，可以通过变量Job.trigger.obsNewFiles引用。前提条件：该OBS路径已经配置DIS消息通知。

        :param event_type: The event_type of this Event.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def channel(self):
        """Gets the channel of this Event.

        DIS通道名称。通过DIS管理控制台获取通道名称：登录管理控制台。单击“数据接入服务”，左侧列表选择“通道管理”。通道管理页面中列出了用户拥有的通道

        :return: The channel of this Event.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this Event.

        DIS通道名称。通过DIS管理控制台获取通道名称：登录管理控制台。单击“数据接入服务”，左侧列表选择“通道管理”。通道管理页面中列出了用户拥有的通道

        :param channel: The channel of this Event.
        :type channel: str
        """
        self._channel = channel

    @property
    def fail_policy(self):
        """Gets the fail_policy of this Event.

        执行失败处理策略。 - SUSPEND: 挂起 - IGNORE：忽略失败，读取下一事件

        :return: The fail_policy of this Event.
        :rtype: str
        """
        return self._fail_policy

    @fail_policy.setter
    def fail_policy(self, fail_policy):
        """Sets the fail_policy of this Event.

        执行失败处理策略。 - SUSPEND: 挂起 - IGNORE：忽略失败，读取下一事件

        :param fail_policy: The fail_policy of this Event.
        :type fail_policy: str
        """
        self._fail_policy = fail_policy

    @property
    def concurrent(self):
        """Gets the concurrent of this Event.

        调度并发数

        :return: The concurrent of this Event.
        :rtype: int
        """
        return self._concurrent

    @concurrent.setter
    def concurrent(self, concurrent):
        """Sets the concurrent of this Event.

        调度并发数

        :param concurrent: The concurrent of this Event.
        :type concurrent: int
        """
        self._concurrent = concurrent

    @property
    def read_policy(self):
        """Gets the read_policy of this Event.

        读取策略。 - LAST: 从上次位置读取 - NEW：从最新位置读取

        :return: The read_policy of this Event.
        :rtype: str
        """
        return self._read_policy

    @read_policy.setter
    def read_policy(self, read_policy):
        """Sets the read_policy of this Event.

        读取策略。 - LAST: 从上次位置读取 - NEW：从最新位置读取

        :param read_policy: The read_policy of this Event.
        :type read_policy: str
        """
        self._read_policy = read_policy

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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
