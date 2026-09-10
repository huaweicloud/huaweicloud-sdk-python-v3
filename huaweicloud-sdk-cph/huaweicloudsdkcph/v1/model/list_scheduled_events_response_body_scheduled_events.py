# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduledEventsResponseBodyScheduledEvents:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_id': 'str',
        'server_id': 'str',
        'server_name': 'str',
        'server_model_name': 'str',
        'server_state': 'int',
        'type': 'str',
        'authorization_type': 'str',
        'state': 'str',
        'publish_time': 'str',
        'start_time': 'str',
        'finish_time': 'str',
        'not_before': 'str',
        'not_after': 'str',
        'not_before_deadline': 'str',
        'description': 'str'
    }

    attribute_map = {
        'event_id': 'event_id',
        'server_id': 'server_id',
        'server_name': 'server_name',
        'server_model_name': 'server_model_name',
        'server_state': 'server_state',
        'type': 'type',
        'authorization_type': 'authorization_type',
        'state': 'state',
        'publish_time': 'publish_time',
        'start_time': 'start_time',
        'finish_time': 'finish_time',
        'not_before': 'not_before',
        'not_after': 'not_after',
        'not_before_deadline': 'not_before_deadline',
        'description': 'description'
    }

    def __init__(self, event_id=None, server_id=None, server_name=None, server_model_name=None, server_state=None, type=None, authorization_type=None, state=None, publish_time=None, start_time=None, finish_time=None, not_before=None, not_after=None, not_before_deadline=None, description=None):
        r"""ListScheduledEventsResponseBodyScheduledEvents

        The model defined in huaweicloud sdk

        :param event_id: 计划事件唯一标识，不超过36个字节
        :type event_id: str
        :param server_id: 云手机服务器的唯一标识，不超过32个字节。
        :type server_id: str
        :param server_name: 云手机服务器名称， 不超过65字符，只支持英文字母、数字、汉字、下划线和中划线。
        :type server_name: str
        :param server_model_name: 云手机服务器规格名称，不超过64个字节。
        :type server_model_name: str
        :param server_state: 服务器状态。 - 0、1、3、4：创建中 - 2：异常 - 5：正常 - 8：冻结 - 10：关机 - 11：关机中 - 12：关机失败 - 13：开机中
        :type server_state: int
        :param type: 计划事件类型，取值范围： localdisk-recovery：本地盘换盘、 system-maintenance：系统维护
        :type type: str
        :param authorization_type: 授权类型，取值范围：maintenance：授权维修、redeploy：授权重部署
        :type authorization_type: str
        :param state: 计划事件状态， 取值范围： inquiring: 待授权、 scheduled：待执行、 executing：执行中、 completed：执行成功、 failed：执行失败、 canceled：取消
        :type state: str
        :param publish_time: 事件发布时间
        :type publish_time: str
        :param start_time: 事件开始时间
        :type start_time: str
        :param finish_time: 事件完成时间
        :type finish_time: str
        :param not_before: 计划执行开始时间
        :type not_before: str
        :param not_after: 计划执行完成时间
        :type not_after: str
        :param not_before_deadline: 计划执行开始时间deadline
        :type not_before_deadline: str
        :param description: 计划事件描述
        :type description: str
        """
        
        

        self._event_id = None
        self._server_id = None
        self._server_name = None
        self._server_model_name = None
        self._server_state = None
        self._type = None
        self._authorization_type = None
        self._state = None
        self._publish_time = None
        self._start_time = None
        self._finish_time = None
        self._not_before = None
        self._not_after = None
        self._not_before_deadline = None
        self._description = None
        self.discriminator = None

        if event_id is not None:
            self.event_id = event_id
        if server_id is not None:
            self.server_id = server_id
        if server_name is not None:
            self.server_name = server_name
        if server_model_name is not None:
            self.server_model_name = server_model_name
        if server_state is not None:
            self.server_state = server_state
        if type is not None:
            self.type = type
        if authorization_type is not None:
            self.authorization_type = authorization_type
        if state is not None:
            self.state = state
        if publish_time is not None:
            self.publish_time = publish_time
        if start_time is not None:
            self.start_time = start_time
        if finish_time is not None:
            self.finish_time = finish_time
        if not_before is not None:
            self.not_before = not_before
        if not_after is not None:
            self.not_after = not_after
        if not_before_deadline is not None:
            self.not_before_deadline = not_before_deadline
        if description is not None:
            self.description = description

    @property
    def event_id(self):
        r"""Gets the event_id of this ListScheduledEventsResponseBodyScheduledEvents.

        计划事件唯一标识，不超过36个字节

        :return: The event_id of this ListScheduledEventsResponseBodyScheduledEvents.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this ListScheduledEventsResponseBodyScheduledEvents.

        计划事件唯一标识，不超过36个字节

        :param event_id: The event_id of this ListScheduledEventsResponseBodyScheduledEvents.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def server_id(self):
        r"""Gets the server_id of this ListScheduledEventsResponseBodyScheduledEvents.

        云手机服务器的唯一标识，不超过32个字节。

        :return: The server_id of this ListScheduledEventsResponseBodyScheduledEvents.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ListScheduledEventsResponseBodyScheduledEvents.

        云手机服务器的唯一标识，不超过32个字节。

        :param server_id: The server_id of this ListScheduledEventsResponseBodyScheduledEvents.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def server_name(self):
        r"""Gets the server_name of this ListScheduledEventsResponseBodyScheduledEvents.

        云手机服务器名称， 不超过65字符，只支持英文字母、数字、汉字、下划线和中划线。

        :return: The server_name of this ListScheduledEventsResponseBodyScheduledEvents.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        r"""Sets the server_name of this ListScheduledEventsResponseBodyScheduledEvents.

        云手机服务器名称， 不超过65字符，只支持英文字母、数字、汉字、下划线和中划线。

        :param server_name: The server_name of this ListScheduledEventsResponseBodyScheduledEvents.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def server_model_name(self):
        r"""Gets the server_model_name of this ListScheduledEventsResponseBodyScheduledEvents.

        云手机服务器规格名称，不超过64个字节。

        :return: The server_model_name of this ListScheduledEventsResponseBodyScheduledEvents.
        :rtype: str
        """
        return self._server_model_name

    @server_model_name.setter
    def server_model_name(self, server_model_name):
        r"""Sets the server_model_name of this ListScheduledEventsResponseBodyScheduledEvents.

        云手机服务器规格名称，不超过64个字节。

        :param server_model_name: The server_model_name of this ListScheduledEventsResponseBodyScheduledEvents.
        :type server_model_name: str
        """
        self._server_model_name = server_model_name

    @property
    def server_state(self):
        r"""Gets the server_state of this ListScheduledEventsResponseBodyScheduledEvents.

        服务器状态。 - 0、1、3、4：创建中 - 2：异常 - 5：正常 - 8：冻结 - 10：关机 - 11：关机中 - 12：关机失败 - 13：开机中

        :return: The server_state of this ListScheduledEventsResponseBodyScheduledEvents.
        :rtype: int
        """
        return self._server_state

    @server_state.setter
    def server_state(self, server_state):
        r"""Sets the server_state of this ListScheduledEventsResponseBodyScheduledEvents.

        服务器状态。 - 0、1、3、4：创建中 - 2：异常 - 5：正常 - 8：冻结 - 10：关机 - 11：关机中 - 12：关机失败 - 13：开机中

        :param server_state: The server_state of this ListScheduledEventsResponseBodyScheduledEvents.
        :type server_state: int
        """
        self._server_state = server_state

    @property
    def type(self):
        r"""Gets the type of this ListScheduledEventsResponseBodyScheduledEvents.

        计划事件类型，取值范围： localdisk-recovery：本地盘换盘、 system-maintenance：系统维护

        :return: The type of this ListScheduledEventsResponseBodyScheduledEvents.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListScheduledEventsResponseBodyScheduledEvents.

        计划事件类型，取值范围： localdisk-recovery：本地盘换盘、 system-maintenance：系统维护

        :param type: The type of this ListScheduledEventsResponseBodyScheduledEvents.
        :type type: str
        """
        self._type = type

    @property
    def authorization_type(self):
        r"""Gets the authorization_type of this ListScheduledEventsResponseBodyScheduledEvents.

        授权类型，取值范围：maintenance：授权维修、redeploy：授权重部署

        :return: The authorization_type of this ListScheduledEventsResponseBodyScheduledEvents.
        :rtype: str
        """
        return self._authorization_type

    @authorization_type.setter
    def authorization_type(self, authorization_type):
        r"""Sets the authorization_type of this ListScheduledEventsResponseBodyScheduledEvents.

        授权类型，取值范围：maintenance：授权维修、redeploy：授权重部署

        :param authorization_type: The authorization_type of this ListScheduledEventsResponseBodyScheduledEvents.
        :type authorization_type: str
        """
        self._authorization_type = authorization_type

    @property
    def state(self):
        r"""Gets the state of this ListScheduledEventsResponseBodyScheduledEvents.

        计划事件状态， 取值范围： inquiring: 待授权、 scheduled：待执行、 executing：执行中、 completed：执行成功、 failed：执行失败、 canceled：取消

        :return: The state of this ListScheduledEventsResponseBodyScheduledEvents.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListScheduledEventsResponseBodyScheduledEvents.

        计划事件状态， 取值范围： inquiring: 待授权、 scheduled：待执行、 executing：执行中、 completed：执行成功、 failed：执行失败、 canceled：取消

        :param state: The state of this ListScheduledEventsResponseBodyScheduledEvents.
        :type state: str
        """
        self._state = state

    @property
    def publish_time(self):
        r"""Gets the publish_time of this ListScheduledEventsResponseBodyScheduledEvents.

        事件发布时间

        :return: The publish_time of this ListScheduledEventsResponseBodyScheduledEvents.
        :rtype: str
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        r"""Sets the publish_time of this ListScheduledEventsResponseBodyScheduledEvents.

        事件发布时间

        :param publish_time: The publish_time of this ListScheduledEventsResponseBodyScheduledEvents.
        :type publish_time: str
        """
        self._publish_time = publish_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ListScheduledEventsResponseBodyScheduledEvents.

        事件开始时间

        :return: The start_time of this ListScheduledEventsResponseBodyScheduledEvents.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListScheduledEventsResponseBodyScheduledEvents.

        事件开始时间

        :param start_time: The start_time of this ListScheduledEventsResponseBodyScheduledEvents.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this ListScheduledEventsResponseBodyScheduledEvents.

        事件完成时间

        :return: The finish_time of this ListScheduledEventsResponseBodyScheduledEvents.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this ListScheduledEventsResponseBodyScheduledEvents.

        事件完成时间

        :param finish_time: The finish_time of this ListScheduledEventsResponseBodyScheduledEvents.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def not_before(self):
        r"""Gets the not_before of this ListScheduledEventsResponseBodyScheduledEvents.

        计划执行开始时间

        :return: The not_before of this ListScheduledEventsResponseBodyScheduledEvents.
        :rtype: str
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        r"""Sets the not_before of this ListScheduledEventsResponseBodyScheduledEvents.

        计划执行开始时间

        :param not_before: The not_before of this ListScheduledEventsResponseBodyScheduledEvents.
        :type not_before: str
        """
        self._not_before = not_before

    @property
    def not_after(self):
        r"""Gets the not_after of this ListScheduledEventsResponseBodyScheduledEvents.

        计划执行完成时间

        :return: The not_after of this ListScheduledEventsResponseBodyScheduledEvents.
        :rtype: str
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        r"""Sets the not_after of this ListScheduledEventsResponseBodyScheduledEvents.

        计划执行完成时间

        :param not_after: The not_after of this ListScheduledEventsResponseBodyScheduledEvents.
        :type not_after: str
        """
        self._not_after = not_after

    @property
    def not_before_deadline(self):
        r"""Gets the not_before_deadline of this ListScheduledEventsResponseBodyScheduledEvents.

        计划执行开始时间deadline

        :return: The not_before_deadline of this ListScheduledEventsResponseBodyScheduledEvents.
        :rtype: str
        """
        return self._not_before_deadline

    @not_before_deadline.setter
    def not_before_deadline(self, not_before_deadline):
        r"""Sets the not_before_deadline of this ListScheduledEventsResponseBodyScheduledEvents.

        计划执行开始时间deadline

        :param not_before_deadline: The not_before_deadline of this ListScheduledEventsResponseBodyScheduledEvents.
        :type not_before_deadline: str
        """
        self._not_before_deadline = not_before_deadline

    @property
    def description(self):
        r"""Gets the description of this ListScheduledEventsResponseBodyScheduledEvents.

        计划事件描述

        :return: The description of this ListScheduledEventsResponseBodyScheduledEvents.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListScheduledEventsResponseBodyScheduledEvents.

        计划事件描述

        :param description: The description of this ListScheduledEventsResponseBodyScheduledEvents.
        :type description: str
        """
        self._description = description

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListScheduledEventsResponseBodyScheduledEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
