# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class State:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start': 'bool',
        'type': 'str',
        'payload_filter_in': 'str',
        'payload_filter_out': 'str',
        'state_name': 'str',
        'action_mode': 'str',
        'actions': 'list[Action]',
        'next_state': 'str',
        'time_delay': 'int'
    }

    attribute_map = {
        'start': 'start',
        'type': 'type',
        'payload_filter_in': 'payload_filter_in',
        'payload_filter_out': 'payload_filter_out',
        'state_name': 'state_name',
        'action_mode': 'action_mode',
        'actions': 'actions',
        'next_state': 'next_state',
        'time_delay': 'time_delay'
    }

    def __init__(self, start=None, type=None, payload_filter_in=None, payload_filter_out=None, state_name=None, action_mode=None, actions=None, next_state=None, time_delay=None):
        r"""State

        The model defined in huaweicloud sdk

        :param start: 标识开始的state，图中必须且只有一个start为true的state。
        :type start: bool
        :param type: 必须有TYPE，TYPE值必须是3种State（DELAY，OPERATION，END）中一种。
        :type type: str
        :param payload_filter_in: 过滤输入参数，默认值是\&quot;$\&quot;，表示不过滤。必须是合法的JSONPath格式。 说明 END State没有payload_filter_in属性。
        :type payload_filter_in: str
        :param payload_filter_out: 过滤state的输出结果，默认值是\&quot;$\&quot;，表示不过滤。 必须是合法的JSONPath格式。 说明 END State没有payload_filter_out属性。
        :type payload_filter_out: str
        :param state_name: state的名字定义。 由小写字母、数字和中划线“-”组成，长度为[1, 20]。
        :type state_name: str
        :param action_mode: Action执行模式，支持串行，并行两种模式，默认串行  最小长度：1  最大长度：32  枚举值：  sequential  parallel
        :type action_mode: str
        :param actions: 节点中要执行的操作列表
        :type actions: list[:class:`huaweicloudsdkdwr.v3.Action`]
        :param next_state: 创建工作流指定的下一个节点名称
        :type next_state: str
        :param time_delay: 当节点类型为事件延迟时填入需要延迟的时间，单位为秒
        :type time_delay: int
        """
        
        

        self._start = None
        self._type = None
        self._payload_filter_in = None
        self._payload_filter_out = None
        self._state_name = None
        self._action_mode = None
        self._actions = None
        self._next_state = None
        self._time_delay = None
        self.discriminator = None

        if start is not None:
            self.start = start
        self.type = type
        if payload_filter_in is not None:
            self.payload_filter_in = payload_filter_in
        if payload_filter_out is not None:
            self.payload_filter_out = payload_filter_out
        self.state_name = state_name
        if action_mode is not None:
            self.action_mode = action_mode
        if actions is not None:
            self.actions = actions
        if next_state is not None:
            self.next_state = next_state
        if time_delay is not None:
            self.time_delay = time_delay

    @property
    def start(self):
        r"""Gets the start of this State.

        标识开始的state，图中必须且只有一个start为true的state。

        :return: The start of this State.
        :rtype: bool
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this State.

        标识开始的state，图中必须且只有一个start为true的state。

        :param start: The start of this State.
        :type start: bool
        """
        self._start = start

    @property
    def type(self):
        r"""Gets the type of this State.

        必须有TYPE，TYPE值必须是3种State（DELAY，OPERATION，END）中一种。

        :return: The type of this State.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this State.

        必须有TYPE，TYPE值必须是3种State（DELAY，OPERATION，END）中一种。

        :param type: The type of this State.
        :type type: str
        """
        self._type = type

    @property
    def payload_filter_in(self):
        r"""Gets the payload_filter_in of this State.

        过滤输入参数，默认值是\"$\"，表示不过滤。必须是合法的JSONPath格式。 说明 END State没有payload_filter_in属性。

        :return: The payload_filter_in of this State.
        :rtype: str
        """
        return self._payload_filter_in

    @payload_filter_in.setter
    def payload_filter_in(self, payload_filter_in):
        r"""Sets the payload_filter_in of this State.

        过滤输入参数，默认值是\"$\"，表示不过滤。必须是合法的JSONPath格式。 说明 END State没有payload_filter_in属性。

        :param payload_filter_in: The payload_filter_in of this State.
        :type payload_filter_in: str
        """
        self._payload_filter_in = payload_filter_in

    @property
    def payload_filter_out(self):
        r"""Gets the payload_filter_out of this State.

        过滤state的输出结果，默认值是\"$\"，表示不过滤。 必须是合法的JSONPath格式。 说明 END State没有payload_filter_out属性。

        :return: The payload_filter_out of this State.
        :rtype: str
        """
        return self._payload_filter_out

    @payload_filter_out.setter
    def payload_filter_out(self, payload_filter_out):
        r"""Sets the payload_filter_out of this State.

        过滤state的输出结果，默认值是\"$\"，表示不过滤。 必须是合法的JSONPath格式。 说明 END State没有payload_filter_out属性。

        :param payload_filter_out: The payload_filter_out of this State.
        :type payload_filter_out: str
        """
        self._payload_filter_out = payload_filter_out

    @property
    def state_name(self):
        r"""Gets the state_name of this State.

        state的名字定义。 由小写字母、数字和中划线“-”组成，长度为[1, 20]。

        :return: The state_name of this State.
        :rtype: str
        """
        return self._state_name

    @state_name.setter
    def state_name(self, state_name):
        r"""Sets the state_name of this State.

        state的名字定义。 由小写字母、数字和中划线“-”组成，长度为[1, 20]。

        :param state_name: The state_name of this State.
        :type state_name: str
        """
        self._state_name = state_name

    @property
    def action_mode(self):
        r"""Gets the action_mode of this State.

        Action执行模式，支持串行，并行两种模式，默认串行  最小长度：1  最大长度：32  枚举值：  sequential  parallel

        :return: The action_mode of this State.
        :rtype: str
        """
        return self._action_mode

    @action_mode.setter
    def action_mode(self, action_mode):
        r"""Sets the action_mode of this State.

        Action执行模式，支持串行，并行两种模式，默认串行  最小长度：1  最大长度：32  枚举值：  sequential  parallel

        :param action_mode: The action_mode of this State.
        :type action_mode: str
        """
        self._action_mode = action_mode

    @property
    def actions(self):
        r"""Gets the actions of this State.

        节点中要执行的操作列表

        :return: The actions of this State.
        :rtype: list[:class:`huaweicloudsdkdwr.v3.Action`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this State.

        节点中要执行的操作列表

        :param actions: The actions of this State.
        :type actions: list[:class:`huaweicloudsdkdwr.v3.Action`]
        """
        self._actions = actions

    @property
    def next_state(self):
        r"""Gets the next_state of this State.

        创建工作流指定的下一个节点名称

        :return: The next_state of this State.
        :rtype: str
        """
        return self._next_state

    @next_state.setter
    def next_state(self, next_state):
        r"""Sets the next_state of this State.

        创建工作流指定的下一个节点名称

        :param next_state: The next_state of this State.
        :type next_state: str
        """
        self._next_state = next_state

    @property
    def time_delay(self):
        r"""Gets the time_delay of this State.

        当节点类型为事件延迟时填入需要延迟的时间，单位为秒

        :return: The time_delay of this State.
        :rtype: int
        """
        return self._time_delay

    @time_delay.setter
    def time_delay(self, time_delay):
        r"""Sets the time_delay of this State.

        当节点类型为事件延迟时填入需要延迟的时间，单位为秒

        :param time_delay: The time_delay of this State.
        :type time_delay: int
        """
        self._time_delay = time_delay

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
        if not isinstance(other, State):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
