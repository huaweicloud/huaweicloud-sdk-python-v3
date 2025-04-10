# coding: utf-8

import six

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
        'pipe_id': 'str',
        'query': 'str',
        'query_type': 'str',
        '_from': 'int',
        'to': 'int',
        'event_grouping': 'bool',
        'triggers': 'list[AlertRuleTrigger]'
    }

    attribute_map = {
        'pipe_id': 'pipe_id',
        'query': 'query',
        'query_type': 'query_type',
        '_from': 'from',
        'to': 'to',
        'event_grouping': 'event_grouping',
        'triggers': 'triggers'
    }

    def __init__(self, pipe_id=None, query=None, query_type=None, _from=None, to=None, event_grouping=None, triggers=None):
        r"""CreateAlertRuleSimulationRequestBody

        The model defined in huaweicloud sdk

        :param pipe_id: pipe_id
        :type pipe_id: str
        :param query: query
        :type query: str
        :param query_type: query_type. SQL, CBSL.
        :type query_type: str
        :param _from: from
        :type _from: int
        :param to: from
        :type to: int
        :param event_grouping: event_grouping
        :type event_grouping: bool
        :param triggers: triggers
        :type triggers: list[:class:`huaweicloudsdksa.v2.AlertRuleTrigger`]
        """
        
        

        self._pipe_id = None
        self._query = None
        self._query_type = None
        self.__from = None
        self._to = None
        self._event_grouping = None
        self._triggers = None
        self.discriminator = None

        self.pipe_id = pipe_id
        self.query = query
        if query_type is not None:
            self.query_type = query_type
        self._from = _from
        self.to = to
        if event_grouping is not None:
            self.event_grouping = event_grouping
        self.triggers = triggers

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this CreateAlertRuleSimulationRequestBody.

        pipe_id

        :return: The pipe_id of this CreateAlertRuleSimulationRequestBody.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this CreateAlertRuleSimulationRequestBody.

        pipe_id

        :param pipe_id: The pipe_id of this CreateAlertRuleSimulationRequestBody.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def query(self):
        r"""Gets the query of this CreateAlertRuleSimulationRequestBody.

        query

        :return: The query of this CreateAlertRuleSimulationRequestBody.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this CreateAlertRuleSimulationRequestBody.

        query

        :param query: The query of this CreateAlertRuleSimulationRequestBody.
        :type query: str
        """
        self._query = query

    @property
    def query_type(self):
        r"""Gets the query_type of this CreateAlertRuleSimulationRequestBody.

        query_type. SQL, CBSL.

        :return: The query_type of this CreateAlertRuleSimulationRequestBody.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this CreateAlertRuleSimulationRequestBody.

        query_type. SQL, CBSL.

        :param query_type: The query_type of this CreateAlertRuleSimulationRequestBody.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def _from(self):
        r"""Gets the _from of this CreateAlertRuleSimulationRequestBody.

        from

        :return: The _from of this CreateAlertRuleSimulationRequestBody.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this CreateAlertRuleSimulationRequestBody.

        from

        :param _from: The _from of this CreateAlertRuleSimulationRequestBody.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this CreateAlertRuleSimulationRequestBody.

        from

        :return: The to of this CreateAlertRuleSimulationRequestBody.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this CreateAlertRuleSimulationRequestBody.

        from

        :param to: The to of this CreateAlertRuleSimulationRequestBody.
        :type to: int
        """
        self._to = to

    @property
    def event_grouping(self):
        r"""Gets the event_grouping of this CreateAlertRuleSimulationRequestBody.

        event_grouping

        :return: The event_grouping of this CreateAlertRuleSimulationRequestBody.
        :rtype: bool
        """
        return self._event_grouping

    @event_grouping.setter
    def event_grouping(self, event_grouping):
        r"""Sets the event_grouping of this CreateAlertRuleSimulationRequestBody.

        event_grouping

        :param event_grouping: The event_grouping of this CreateAlertRuleSimulationRequestBody.
        :type event_grouping: bool
        """
        self._event_grouping = event_grouping

    @property
    def triggers(self):
        r"""Gets the triggers of this CreateAlertRuleSimulationRequestBody.

        triggers

        :return: The triggers of this CreateAlertRuleSimulationRequestBody.
        :rtype: list[:class:`huaweicloudsdksa.v2.AlertRuleTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        r"""Sets the triggers of this CreateAlertRuleSimulationRequestBody.

        triggers

        :param triggers: The triggers of this CreateAlertRuleSimulationRequestBody.
        :type triggers: list[:class:`huaweicloudsdksa.v2.AlertRuleTrigger`]
        """
        self._triggers = triggers

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
        if not isinstance(other, CreateAlertRuleSimulationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
