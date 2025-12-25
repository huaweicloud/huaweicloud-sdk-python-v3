# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAlertRuleSimulationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_grouping': 'bool',
        '_from': 'int',
        'pipe_id': 'str',
        'query': 'str',
        'query_type': 'str',
        'to': 'int',
        'triggers': 'list[AlertRuleTrigger]'
    }

    attribute_map = {
        'event_grouping': 'event_grouping',
        '_from': 'from',
        'pipe_id': 'pipe_id',
        'query': 'query',
        'query_type': 'query_type',
        'to': 'to',
        'triggers': 'triggers'
    }

    def __init__(self, event_grouping=None, _from=None, pipe_id=None, query=None, query_type=None, to=None, triggers=None):
        r"""CreateAlertRuleSimulationRequestBody

        The model defined in huaweicloud sdk

        :param event_grouping: 告警分组
        :type event_grouping: bool
        :param _from: 开始时间
        :type _from: int
        :param pipe_id: 数据管道 ID
        :type pipe_id: str
        :param query: 查询语句
        :type query: str
        :param query_type: **参数解释**: 查询语法类型 - SQL查询 **约束限制**: 不涉及  **取值范围**: - SQL **默认值**:  SQL
        :type query_type: str
        :param to: 结束时间
        :type to: int
        :param triggers: 告警触发规则
        :type triggers: list[:class:`huaweicloudsdksecmaster.v1.AlertRuleTrigger`]
        """
        
        

        self._event_grouping = None
        self.__from = None
        self._pipe_id = None
        self._query = None
        self._query_type = None
        self._to = None
        self._triggers = None
        self.discriminator = None

        if event_grouping is not None:
            self.event_grouping = event_grouping
        self._from = _from
        self.pipe_id = pipe_id
        self.query = query
        if query_type is not None:
            self.query_type = query_type
        self.to = to
        self.triggers = triggers

    @property
    def event_grouping(self):
        r"""Gets the event_grouping of this CreateAlertRuleSimulationRequestBody.

        告警分组

        :return: The event_grouping of this CreateAlertRuleSimulationRequestBody.
        :rtype: bool
        """
        return self._event_grouping

    @event_grouping.setter
    def event_grouping(self, event_grouping):
        r"""Sets the event_grouping of this CreateAlertRuleSimulationRequestBody.

        告警分组

        :param event_grouping: The event_grouping of this CreateAlertRuleSimulationRequestBody.
        :type event_grouping: bool
        """
        self._event_grouping = event_grouping

    @property
    def _from(self):
        r"""Gets the _from of this CreateAlertRuleSimulationRequestBody.

        开始时间

        :return: The _from of this CreateAlertRuleSimulationRequestBody.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this CreateAlertRuleSimulationRequestBody.

        开始时间

        :param _from: The _from of this CreateAlertRuleSimulationRequestBody.
        :type _from: int
        """
        self.__from = _from

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this CreateAlertRuleSimulationRequestBody.

        数据管道 ID

        :return: The pipe_id of this CreateAlertRuleSimulationRequestBody.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this CreateAlertRuleSimulationRequestBody.

        数据管道 ID

        :param pipe_id: The pipe_id of this CreateAlertRuleSimulationRequestBody.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def query(self):
        r"""Gets the query of this CreateAlertRuleSimulationRequestBody.

        查询语句

        :return: The query of this CreateAlertRuleSimulationRequestBody.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this CreateAlertRuleSimulationRequestBody.

        查询语句

        :param query: The query of this CreateAlertRuleSimulationRequestBody.
        :type query: str
        """
        self._query = query

    @property
    def query_type(self):
        r"""Gets the query_type of this CreateAlertRuleSimulationRequestBody.

        **参数解释**: 查询语法类型 - SQL查询 **约束限制**: 不涉及  **取值范围**: - SQL **默认值**:  SQL

        :return: The query_type of this CreateAlertRuleSimulationRequestBody.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this CreateAlertRuleSimulationRequestBody.

        **参数解释**: 查询语法类型 - SQL查询 **约束限制**: 不涉及  **取值范围**: - SQL **默认值**:  SQL

        :param query_type: The query_type of this CreateAlertRuleSimulationRequestBody.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def to(self):
        r"""Gets the to of this CreateAlertRuleSimulationRequestBody.

        结束时间

        :return: The to of this CreateAlertRuleSimulationRequestBody.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this CreateAlertRuleSimulationRequestBody.

        结束时间

        :param to: The to of this CreateAlertRuleSimulationRequestBody.
        :type to: int
        """
        self._to = to

    @property
    def triggers(self):
        r"""Gets the triggers of this CreateAlertRuleSimulationRequestBody.

        告警触发规则

        :return: The triggers of this CreateAlertRuleSimulationRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.AlertRuleTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        r"""Sets the triggers of this CreateAlertRuleSimulationRequestBody.

        告警触发规则

        :param triggers: The triggers of this CreateAlertRuleSimulationRequestBody.
        :type triggers: list[:class:`huaweicloudsdksecmaster.v1.AlertRuleTrigger`]
        """
        self._triggers = triggers

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
        if not isinstance(other, CreateAlertRuleSimulationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
