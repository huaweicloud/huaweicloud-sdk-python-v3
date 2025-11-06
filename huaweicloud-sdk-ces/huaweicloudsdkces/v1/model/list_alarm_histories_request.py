# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmHistoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'alarm_id': 'str',
        'alarm_name': 'str',
        'alarm_status': 'str',
        'alarm_level': 'int',
        'namespace': 'str',
        '_from': 'str',
        'to': 'str',
        'start': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'alarm_id': 'alarm_id',
        'alarm_name': 'alarm_name',
        'alarm_status': 'alarm_status',
        'alarm_level': 'alarm_level',
        'namespace': 'namespace',
        '_from': 'from',
        'to': 'to',
        'start': 'start',
        'limit': 'limit'
    }

    def __init__(self, group_id=None, alarm_id=None, alarm_name=None, alarm_status=None, alarm_level=None, namespace=None, _from=None, to=None, start=None, limit=None):
        r"""ListAlarmHistoriesRequest

        The model defined in huaweicloud sdk

        :param group_id: **参数解释**： 当前资源所在分组信息 **约束限制**： 不涉及。 **取值范围**： 以rg开头，后跟22位由字母或数字组成的字符串，字符长度为24 **默认取值**： 不涉及 
        :type group_id: str
        :param alarm_id: **参数解释**： 告警规则ID **约束限制**： 不涉及 **取值范围**： 以al开头，后跟22位由字母或数字组成的字符串，字符长度为24 **默认取值**： 不涉及 
        :type alarm_id: str
        :param alarm_name: **参数解释**： 告警规则名称 **约束限制**： 不涉及 **取值范围**： 只能包含0-9/a-z/A-Z/_/-或汉字，长度[1, 128]个字符 **默认取值**： 不涉及 
        :type alarm_name: str
        :param alarm_status: **参数解释**： 告警状态。 **约束限制**： 不涉及 **取值范围**： 枚举值： - ok：正常 - alarm：告警 - insufficient_data：数据不足 - invalid：已失效 **默认取值**： 不涉及 
        :type alarm_status: str
        :param alarm_level: **参数解释**： 告警历史的告警级别，值为1,2,3,4 **约束限制**： 不涉及 **取值范围**： 枚举值： - 1：紧急 - 2：重要 - 3：次要 - 4：提示 **默认取值**： 不涉及 
        :type alarm_level: int
        :param namespace: **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)” **约束限制**： 不涉及 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间 **默认取值**： 不涉及 
        :type namespace: str
        :param _from: **参数解释**： 通过时间筛选traces的起始时间(包括传入时间)，为timestamp **约束限制**： 不涉及 **取值范围**： 长度为[1,13]个字符 **默认取值**： 不涉及 
        :type _from: str
        :param to: **参数解释**： 通过时间筛选traces的终止时间(包括传入时间)，为timestamp **约束限制**： 不涉及 **取值范围**： 长度为[1,13]个字符 **默认取值**： 不涉及 
        :type to: str
        :param start: **参数解释**： 分页查询时查询的起始位置，表示从第几条数据开始 **约束限制**： 不涉及。 **取值范围**： 大于等于0的整数 **默认取值**： 0 
        :type start: str
        :param limit: **参数解释**： 本次查询的最大条目数 **约束限制**： 不涉及。 **取值范围**： 取值范围[1,100] **默认取值**： 100 
        :type limit: str
        """
        
        

        self._group_id = None
        self._alarm_id = None
        self._alarm_name = None
        self._alarm_status = None
        self._alarm_level = None
        self._namespace = None
        self.__from = None
        self._to = None
        self._start = None
        self._limit = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if alarm_id is not None:
            self.alarm_id = alarm_id
        if alarm_name is not None:
            self.alarm_name = alarm_name
        if alarm_status is not None:
            self.alarm_status = alarm_status
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if namespace is not None:
            self.namespace = namespace
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit

    @property
    def group_id(self):
        r"""Gets the group_id of this ListAlarmHistoriesRequest.

        **参数解释**： 当前资源所在分组信息 **约束限制**： 不涉及。 **取值范围**： 以rg开头，后跟22位由字母或数字组成的字符串，字符长度为24 **默认取值**： 不涉及 

        :return: The group_id of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListAlarmHistoriesRequest.

        **参数解释**： 当前资源所在分组信息 **约束限制**： 不涉及。 **取值范围**： 以rg开头，后跟22位由字母或数字组成的字符串，字符长度为24 **默认取值**： 不涉及 

        :param group_id: The group_id of this ListAlarmHistoriesRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def alarm_id(self):
        r"""Gets the alarm_id of this ListAlarmHistoriesRequest.

        **参数解释**： 告警规则ID **约束限制**： 不涉及 **取值范围**： 以al开头，后跟22位由字母或数字组成的字符串，字符长度为24 **默认取值**： 不涉及 

        :return: The alarm_id of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        r"""Sets the alarm_id of this ListAlarmHistoriesRequest.

        **参数解释**： 告警规则ID **约束限制**： 不涉及 **取值范围**： 以al开头，后跟22位由字母或数字组成的字符串，字符长度为24 **默认取值**： 不涉及 

        :param alarm_id: The alarm_id of this ListAlarmHistoriesRequest.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def alarm_name(self):
        r"""Gets the alarm_name of this ListAlarmHistoriesRequest.

        **参数解释**： 告警规则名称 **约束限制**： 不涉及 **取值范围**： 只能包含0-9/a-z/A-Z/_/-或汉字，长度[1, 128]个字符 **默认取值**： 不涉及 

        :return: The alarm_name of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._alarm_name

    @alarm_name.setter
    def alarm_name(self, alarm_name):
        r"""Sets the alarm_name of this ListAlarmHistoriesRequest.

        **参数解释**： 告警规则名称 **约束限制**： 不涉及 **取值范围**： 只能包含0-9/a-z/A-Z/_/-或汉字，长度[1, 128]个字符 **默认取值**： 不涉及 

        :param alarm_name: The alarm_name of this ListAlarmHistoriesRequest.
        :type alarm_name: str
        """
        self._alarm_name = alarm_name

    @property
    def alarm_status(self):
        r"""Gets the alarm_status of this ListAlarmHistoriesRequest.

        **参数解释**： 告警状态。 **约束限制**： 不涉及 **取值范围**： 枚举值： - ok：正常 - alarm：告警 - insufficient_data：数据不足 - invalid：已失效 **默认取值**： 不涉及 

        :return: The alarm_status of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._alarm_status

    @alarm_status.setter
    def alarm_status(self, alarm_status):
        r"""Sets the alarm_status of this ListAlarmHistoriesRequest.

        **参数解释**： 告警状态。 **约束限制**： 不涉及 **取值范围**： 枚举值： - ok：正常 - alarm：告警 - insufficient_data：数据不足 - invalid：已失效 **默认取值**： 不涉及 

        :param alarm_status: The alarm_status of this ListAlarmHistoriesRequest.
        :type alarm_status: str
        """
        self._alarm_status = alarm_status

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this ListAlarmHistoriesRequest.

        **参数解释**： 告警历史的告警级别，值为1,2,3,4 **约束限制**： 不涉及 **取值范围**： 枚举值： - 1：紧急 - 2：重要 - 3：次要 - 4：提示 **默认取值**： 不涉及 

        :return: The alarm_level of this ListAlarmHistoriesRequest.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this ListAlarmHistoriesRequest.

        **参数解释**： 告警历史的告警级别，值为1,2,3,4 **约束限制**： 不涉及 **取值范围**： 枚举值： - 1：紧急 - 2：重要 - 3：次要 - 4：提示 **默认取值**： 不涉及 

        :param alarm_level: The alarm_level of this ListAlarmHistoriesRequest.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

    @property
    def namespace(self):
        r"""Gets the namespace of this ListAlarmHistoriesRequest.

        **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)” **约束限制**： 不涉及 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间 **默认取值**： 不涉及 

        :return: The namespace of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListAlarmHistoriesRequest.

        **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)” **约束限制**： 不涉及 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间 **默认取值**： 不涉及 

        :param namespace: The namespace of this ListAlarmHistoriesRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def _from(self):
        r"""Gets the _from of this ListAlarmHistoriesRequest.

        **参数解释**： 通过时间筛选traces的起始时间(包括传入时间)，为timestamp **约束限制**： 不涉及 **取值范围**： 长度为[1,13]个字符 **默认取值**： 不涉及 

        :return: The _from of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListAlarmHistoriesRequest.

        **参数解释**： 通过时间筛选traces的起始时间(包括传入时间)，为timestamp **约束限制**： 不涉及 **取值范围**： 长度为[1,13]个字符 **默认取值**： 不涉及 

        :param _from: The _from of this ListAlarmHistoriesRequest.
        :type _from: str
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListAlarmHistoriesRequest.

        **参数解释**： 通过时间筛选traces的终止时间(包括传入时间)，为timestamp **约束限制**： 不涉及 **取值范围**： 长度为[1,13]个字符 **默认取值**： 不涉及 

        :return: The to of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListAlarmHistoriesRequest.

        **参数解释**： 通过时间筛选traces的终止时间(包括传入时间)，为timestamp **约束限制**： 不涉及 **取值范围**： 长度为[1,13]个字符 **默认取值**： 不涉及 

        :param to: The to of this ListAlarmHistoriesRequest.
        :type to: str
        """
        self._to = to

    @property
    def start(self):
        r"""Gets the start of this ListAlarmHistoriesRequest.

        **参数解释**： 分页查询时查询的起始位置，表示从第几条数据开始 **约束限制**： 不涉及。 **取值范围**： 大于等于0的整数 **默认取值**： 0 

        :return: The start of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this ListAlarmHistoriesRequest.

        **参数解释**： 分页查询时查询的起始位置，表示从第几条数据开始 **约束限制**： 不涉及。 **取值范围**： 大于等于0的整数 **默认取值**： 0 

        :param start: The start of this ListAlarmHistoriesRequest.
        :type start: str
        """
        self._start = start

    @property
    def limit(self):
        r"""Gets the limit of this ListAlarmHistoriesRequest.

        **参数解释**： 本次查询的最大条目数 **约束限制**： 不涉及。 **取值范围**： 取值范围[1,100] **默认取值**： 100 

        :return: The limit of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAlarmHistoriesRequest.

        **参数解释**： 本次查询的最大条目数 **约束限制**： 不涉及。 **取值范围**： 取值范围[1,100] **默认取值**： 100 

        :param limit: The limit of this ListAlarmHistoriesRequest.
        :type limit: str
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
        if not isinstance(other, ListAlarmHistoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
