# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperationState:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_mode': 'str',
        'actions': 'list[Action]',
        'on_errors': 'list[OnError]',
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'end': 'bool',
        'transition': 'str',
        'state_data_filter': 'StateDataFilter',
        'duration': 'int'
    }

    attribute_map = {
        'action_mode': 'action_mode',
        'actions': 'actions',
        'on_errors': 'on_errors',
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'end': 'end',
        'transition': 'transition',
        'state_data_filter': 'state_data_filter',
        'duration': 'duration'
    }

    def __init__(self, action_mode=None, actions=None, on_errors=None, id=None, name=None, type=None, end=None, transition=None, state_data_filter=None, duration=None):
        r"""OperationState

        The model defined in huaweicloud sdk

        :param action_mode: Action执行模式，支持串行，并行两种模式，默认串行
        :type action_mode: str
        :param actions: 节点中要执行的操作列表
        :type actions: list[:class:`huaweicloudsdkfunctiongraph.v2.Action`]
        :param on_errors: 错误处理策略
        :type on_errors: list[:class:`huaweicloudsdkfunctiongraph.v2.OnError`]
        :param id: 节点ID，需要在当前函数流中唯一
        :type id: str
        :param name: 节点名称
        :type name: str
        :param type: 节点类型
        :type type: str
        :param end: 是否是结束节点
        :type end: bool
        :param transition: 下一步骤节点ID
        :type transition: str
        :param state_data_filter: 
        :type state_data_filter: :class:`huaweicloudsdkfunctiongraph.v2.StateDataFilter`
        :param duration: 时间等待节点等待时间（秒）,节点类型为Sleep时为必填，节点类型不为Sleep时无效
        :type duration: int
        """
        
        

        self._action_mode = None
        self._actions = None
        self._on_errors = None
        self._id = None
        self._name = None
        self._type = None
        self._end = None
        self._transition = None
        self._state_data_filter = None
        self._duration = None
        self.discriminator = None

        if action_mode is not None:
            self.action_mode = action_mode
        self.actions = actions
        if on_errors is not None:
            self.on_errors = on_errors
        self.id = id
        self.name = name
        self.type = type
        self.end = end
        self.transition = transition
        if state_data_filter is not None:
            self.state_data_filter = state_data_filter
        if duration is not None:
            self.duration = duration

    @property
    def action_mode(self):
        r"""Gets the action_mode of this OperationState.

        Action执行模式，支持串行，并行两种模式，默认串行

        :return: The action_mode of this OperationState.
        :rtype: str
        """
        return self._action_mode

    @action_mode.setter
    def action_mode(self, action_mode):
        r"""Sets the action_mode of this OperationState.

        Action执行模式，支持串行，并行两种模式，默认串行

        :param action_mode: The action_mode of this OperationState.
        :type action_mode: str
        """
        self._action_mode = action_mode

    @property
    def actions(self):
        r"""Gets the actions of this OperationState.

        节点中要执行的操作列表

        :return: The actions of this OperationState.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.Action`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this OperationState.

        节点中要执行的操作列表

        :param actions: The actions of this OperationState.
        :type actions: list[:class:`huaweicloudsdkfunctiongraph.v2.Action`]
        """
        self._actions = actions

    @property
    def on_errors(self):
        r"""Gets the on_errors of this OperationState.

        错误处理策略

        :return: The on_errors of this OperationState.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.OnError`]
        """
        return self._on_errors

    @on_errors.setter
    def on_errors(self, on_errors):
        r"""Sets the on_errors of this OperationState.

        错误处理策略

        :param on_errors: The on_errors of this OperationState.
        :type on_errors: list[:class:`huaweicloudsdkfunctiongraph.v2.OnError`]
        """
        self._on_errors = on_errors

    @property
    def id(self):
        r"""Gets the id of this OperationState.

        节点ID，需要在当前函数流中唯一

        :return: The id of this OperationState.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OperationState.

        节点ID，需要在当前函数流中唯一

        :param id: The id of this OperationState.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this OperationState.

        节点名称

        :return: The name of this OperationState.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OperationState.

        节点名称

        :param name: The name of this OperationState.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this OperationState.

        节点类型

        :return: The type of this OperationState.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OperationState.

        节点类型

        :param type: The type of this OperationState.
        :type type: str
        """
        self._type = type

    @property
    def end(self):
        r"""Gets the end of this OperationState.

        是否是结束节点

        :return: The end of this OperationState.
        :rtype: bool
        """
        return self._end

    @end.setter
    def end(self, end):
        r"""Sets the end of this OperationState.

        是否是结束节点

        :param end: The end of this OperationState.
        :type end: bool
        """
        self._end = end

    @property
    def transition(self):
        r"""Gets the transition of this OperationState.

        下一步骤节点ID

        :return: The transition of this OperationState.
        :rtype: str
        """
        return self._transition

    @transition.setter
    def transition(self, transition):
        r"""Sets the transition of this OperationState.

        下一步骤节点ID

        :param transition: The transition of this OperationState.
        :type transition: str
        """
        self._transition = transition

    @property
    def state_data_filter(self):
        r"""Gets the state_data_filter of this OperationState.

        :return: The state_data_filter of this OperationState.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.StateDataFilter`
        """
        return self._state_data_filter

    @state_data_filter.setter
    def state_data_filter(self, state_data_filter):
        r"""Sets the state_data_filter of this OperationState.

        :param state_data_filter: The state_data_filter of this OperationState.
        :type state_data_filter: :class:`huaweicloudsdkfunctiongraph.v2.StateDataFilter`
        """
        self._state_data_filter = state_data_filter

    @property
    def duration(self):
        r"""Gets the duration of this OperationState.

        时间等待节点等待时间（秒）,节点类型为Sleep时为必填，节点类型不为Sleep时无效

        :return: The duration of this OperationState.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this OperationState.

        时间等待节点等待时间（秒）,节点类型为Sleep时为必填，节点类型不为Sleep时无效

        :param duration: The duration of this OperationState.
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
        if not isinstance(other, OperationState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
