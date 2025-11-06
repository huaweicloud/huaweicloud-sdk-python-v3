# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_name': 'str',
        'event_type': 'str',
        'sub_event_type': 'str',
        'event_source': 'str',
        'event_level': 'str',
        'event_user': 'str',
        'event_state': 'str',
        '_from': 'int',
        'to': 'int',
        'start': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'event_name': 'event_name',
        'event_type': 'event_type',
        'sub_event_type': 'sub_event_type',
        'event_source': 'event_source',
        'event_level': 'event_level',
        'event_user': 'event_user',
        'event_state': 'event_state',
        '_from': 'from',
        'to': 'to',
        'start': 'start',
        'limit': 'limit'
    }

    def __init__(self, event_name=None, event_type=None, sub_event_type=None, event_source=None, event_level=None, event_user=None, event_state=None, _from=None, to=None, start=None, limit=None):
        r"""ListEventDetailRequest

        The model defined in huaweicloud sdk

        :param event_name: **参数解释**： 事件名称，值为系统产生的事件名称或用户自定义上报的事件名称。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符。 **默认取值**： 不涉及。
        :type event_name: str
        :param event_type: **参数解释**： 事件类型。 **约束限制**： 不涉及。 **取值范围**： 值为EVENT.SYS或EVENT.CUSTOM。 - EVENT.SYS：系统事件。 - EVENT.CUSTOM：自定义事件。 **默认取值**： 不涉及。
        :type event_type: str
        :param sub_event_type: **参数解释**： 事件子类。 **约束限制**： 不涉及。 **取值范围**： 枚举类型 - SUB_EVENT.OPS: 运维事件 - SUB_EVENT.PLAN: 计划事件 - SUB_EVENT.CUSTOM: 自定义事件 **默认取值**： 不涉及。
        :type sub_event_type: str
        :param event_source: **参数解释**： 事件来源，取值为各云服务的命名空间。云服务的命名空间请参考“[支持监控的服务列表](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 长度为[0,32]个字符。 正则匹配：以字母开头，中间有一个点，包含字母、数字、下划线的字符串。 **默认取值**： 不涉及。
        :type event_source: str
        :param event_level: **参数解释**： 事件的级别。 **约束限制**： 不涉及。 **取值范围**： 值为Critical、Major、Minor、Info。 - Critical: 紧急 - Major: 重要 - Minor: 次要 - Info: 提示 **默认取值**： 不涉及。
        :type event_level: str
        :param event_user: **参数解释**： 上报事件监控数据时用户的名称，也可为projectID。 **约束限制**： 不涉及。 **取值范围**： 长度为[0,64]个字符。 正则匹配：由零个或多个字母、数字、下划线、横线、斜杠、空格、@ 符号或点号组成的字符串。 **默认取值**： 不涉及。
        :type event_user: str
        :param event_state: **参数解释**： 事件的状态。 **约束限制**： 不涉及。 **取值范围**： 值为normal、warning、incident。 - normal: 正常 - warning: 警告 - incident: 故障 **默认取值**： 不涉及。
        :type event_state: str
        :param _from: **参数解释**： 查询数据起始时间，UNIX时间戳，单位毫秒。例如：1605952700911。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type _from: int
        :param to: **参数解释**： 查询数据截止时间，UNIX时间戳，单位毫秒。 **约束限制**： 其中from必须小于to。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type to: int
        :param start: **参数解释**： 分页起始值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0
        :type start: int
        :param limit: **参数解释**： 单次查询的条数限制，用于限制结果数据条数。 **约束限制**： 不涉及。 **取值范围**： 大小为[1,100]的整数 **默认取值**： 100
        :type limit: int
        """
        
        

        self._event_name = None
        self._event_type = None
        self._sub_event_type = None
        self._event_source = None
        self._event_level = None
        self._event_user = None
        self._event_state = None
        self.__from = None
        self._to = None
        self._start = None
        self._limit = None
        self.discriminator = None

        self.event_name = event_name
        self.event_type = event_type
        if sub_event_type is not None:
            self.sub_event_type = sub_event_type
        if event_source is not None:
            self.event_source = event_source
        if event_level is not None:
            self.event_level = event_level
        if event_user is not None:
            self.event_user = event_user
        if event_state is not None:
            self.event_state = event_state
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit

    @property
    def event_name(self):
        r"""Gets the event_name of this ListEventDetailRequest.

        **参数解释**： 事件名称，值为系统产生的事件名称或用户自定义上报的事件名称。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符。 **默认取值**： 不涉及。

        :return: The event_name of this ListEventDetailRequest.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this ListEventDetailRequest.

        **参数解释**： 事件名称，值为系统产生的事件名称或用户自定义上报的事件名称。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符。 **默认取值**： 不涉及。

        :param event_name: The event_name of this ListEventDetailRequest.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def event_type(self):
        r"""Gets the event_type of this ListEventDetailRequest.

        **参数解释**： 事件类型。 **约束限制**： 不涉及。 **取值范围**： 值为EVENT.SYS或EVENT.CUSTOM。 - EVENT.SYS：系统事件。 - EVENT.CUSTOM：自定义事件。 **默认取值**： 不涉及。

        :return: The event_type of this ListEventDetailRequest.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ListEventDetailRequest.

        **参数解释**： 事件类型。 **约束限制**： 不涉及。 **取值范围**： 值为EVENT.SYS或EVENT.CUSTOM。 - EVENT.SYS：系统事件。 - EVENT.CUSTOM：自定义事件。 **默认取值**： 不涉及。

        :param event_type: The event_type of this ListEventDetailRequest.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def sub_event_type(self):
        r"""Gets the sub_event_type of this ListEventDetailRequest.

        **参数解释**： 事件子类。 **约束限制**： 不涉及。 **取值范围**： 枚举类型 - SUB_EVENT.OPS: 运维事件 - SUB_EVENT.PLAN: 计划事件 - SUB_EVENT.CUSTOM: 自定义事件 **默认取值**： 不涉及。

        :return: The sub_event_type of this ListEventDetailRequest.
        :rtype: str
        """
        return self._sub_event_type

    @sub_event_type.setter
    def sub_event_type(self, sub_event_type):
        r"""Sets the sub_event_type of this ListEventDetailRequest.

        **参数解释**： 事件子类。 **约束限制**： 不涉及。 **取值范围**： 枚举类型 - SUB_EVENT.OPS: 运维事件 - SUB_EVENT.PLAN: 计划事件 - SUB_EVENT.CUSTOM: 自定义事件 **默认取值**： 不涉及。

        :param sub_event_type: The sub_event_type of this ListEventDetailRequest.
        :type sub_event_type: str
        """
        self._sub_event_type = sub_event_type

    @property
    def event_source(self):
        r"""Gets the event_source of this ListEventDetailRequest.

        **参数解释**： 事件来源，取值为各云服务的命名空间。云服务的命名空间请参考“[支持监控的服务列表](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 长度为[0,32]个字符。 正则匹配：以字母开头，中间有一个点，包含字母、数字、下划线的字符串。 **默认取值**： 不涉及。

        :return: The event_source of this ListEventDetailRequest.
        :rtype: str
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        r"""Sets the event_source of this ListEventDetailRequest.

        **参数解释**： 事件来源，取值为各云服务的命名空间。云服务的命名空间请参考“[支持监控的服务列表](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 长度为[0,32]个字符。 正则匹配：以字母开头，中间有一个点，包含字母、数字、下划线的字符串。 **默认取值**： 不涉及。

        :param event_source: The event_source of this ListEventDetailRequest.
        :type event_source: str
        """
        self._event_source = event_source

    @property
    def event_level(self):
        r"""Gets the event_level of this ListEventDetailRequest.

        **参数解释**： 事件的级别。 **约束限制**： 不涉及。 **取值范围**： 值为Critical、Major、Minor、Info。 - Critical: 紧急 - Major: 重要 - Minor: 次要 - Info: 提示 **默认取值**： 不涉及。

        :return: The event_level of this ListEventDetailRequest.
        :rtype: str
        """
        return self._event_level

    @event_level.setter
    def event_level(self, event_level):
        r"""Sets the event_level of this ListEventDetailRequest.

        **参数解释**： 事件的级别。 **约束限制**： 不涉及。 **取值范围**： 值为Critical、Major、Minor、Info。 - Critical: 紧急 - Major: 重要 - Minor: 次要 - Info: 提示 **默认取值**： 不涉及。

        :param event_level: The event_level of this ListEventDetailRequest.
        :type event_level: str
        """
        self._event_level = event_level

    @property
    def event_user(self):
        r"""Gets the event_user of this ListEventDetailRequest.

        **参数解释**： 上报事件监控数据时用户的名称，也可为projectID。 **约束限制**： 不涉及。 **取值范围**： 长度为[0,64]个字符。 正则匹配：由零个或多个字母、数字、下划线、横线、斜杠、空格、@ 符号或点号组成的字符串。 **默认取值**： 不涉及。

        :return: The event_user of this ListEventDetailRequest.
        :rtype: str
        """
        return self._event_user

    @event_user.setter
    def event_user(self, event_user):
        r"""Sets the event_user of this ListEventDetailRequest.

        **参数解释**： 上报事件监控数据时用户的名称，也可为projectID。 **约束限制**： 不涉及。 **取值范围**： 长度为[0,64]个字符。 正则匹配：由零个或多个字母、数字、下划线、横线、斜杠、空格、@ 符号或点号组成的字符串。 **默认取值**： 不涉及。

        :param event_user: The event_user of this ListEventDetailRequest.
        :type event_user: str
        """
        self._event_user = event_user

    @property
    def event_state(self):
        r"""Gets the event_state of this ListEventDetailRequest.

        **参数解释**： 事件的状态。 **约束限制**： 不涉及。 **取值范围**： 值为normal、warning、incident。 - normal: 正常 - warning: 警告 - incident: 故障 **默认取值**： 不涉及。

        :return: The event_state of this ListEventDetailRequest.
        :rtype: str
        """
        return self._event_state

    @event_state.setter
    def event_state(self, event_state):
        r"""Sets the event_state of this ListEventDetailRequest.

        **参数解释**： 事件的状态。 **约束限制**： 不涉及。 **取值范围**： 值为normal、warning、incident。 - normal: 正常 - warning: 警告 - incident: 故障 **默认取值**： 不涉及。

        :param event_state: The event_state of this ListEventDetailRequest.
        :type event_state: str
        """
        self._event_state = event_state

    @property
    def _from(self):
        r"""Gets the _from of this ListEventDetailRequest.

        **参数解释**： 查询数据起始时间，UNIX时间戳，单位毫秒。例如：1605952700911。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The _from of this ListEventDetailRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListEventDetailRequest.

        **参数解释**： 查询数据起始时间，UNIX时间戳，单位毫秒。例如：1605952700911。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param _from: The _from of this ListEventDetailRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListEventDetailRequest.

        **参数解释**： 查询数据截止时间，UNIX时间戳，单位毫秒。 **约束限制**： 其中from必须小于to。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The to of this ListEventDetailRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListEventDetailRequest.

        **参数解释**： 查询数据截止时间，UNIX时间戳，单位毫秒。 **约束限制**： 其中from必须小于to。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param to: The to of this ListEventDetailRequest.
        :type to: int
        """
        self._to = to

    @property
    def start(self):
        r"""Gets the start of this ListEventDetailRequest.

        **参数解释**： 分页起始值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0

        :return: The start of this ListEventDetailRequest.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this ListEventDetailRequest.

        **参数解释**： 分页起始值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0

        :param start: The start of this ListEventDetailRequest.
        :type start: int
        """
        self._start = start

    @property
    def limit(self):
        r"""Gets the limit of this ListEventDetailRequest.

        **参数解释**： 单次查询的条数限制，用于限制结果数据条数。 **约束限制**： 不涉及。 **取值范围**： 大小为[1,100]的整数 **默认取值**： 100

        :return: The limit of this ListEventDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEventDetailRequest.

        **参数解释**： 单次查询的条数限制，用于限制结果数据条数。 **约束限制**： 不涉及。 **取值范围**： 大小为[1,100]的整数 **默认取值**： 100

        :param limit: The limit of this ListEventDetailRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListEventDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
