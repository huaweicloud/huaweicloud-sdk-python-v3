# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQueriesStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'average_query_waiting_time': 'float',
        'average_time_consumption_of_queries': 'float',
        'average_time_consumption_of_sessions': 'float',
        'queries_count': 'int',
        'session_count': 'int'
    }

    attribute_map = {
        'average_query_waiting_time': 'average_query_waiting_time',
        'average_time_consumption_of_queries': 'average_time_consumption_of_queries',
        'average_time_consumption_of_sessions': 'average_time_consumption_of_sessions',
        'queries_count': 'queries_count',
        'session_count': 'session_count'
    }

    def __init__(self, average_query_waiting_time=None, average_time_consumption_of_queries=None, average_time_consumption_of_sessions=None, queries_count=None, session_count=None):
        r"""ListQueriesStatus

        The model defined in huaweicloud sdk

        :param average_query_waiting_time: **参数解释**： 平均查询等待时间。 **取值范围**： 不涉及。
        :type average_query_waiting_time: float
        :param average_time_consumption_of_queries: **参数解释**： 平均查询耗时。 **取值范围**： 不涉及。
        :type average_time_consumption_of_queries: float
        :param average_time_consumption_of_sessions: **参数解释**： 平均会话耗时。 **取值范围**： 不涉及。
        :type average_time_consumption_of_sessions: float
        :param queries_count: **参数解释**： 查询数量。 **取值范围**： 不涉及。
        :type queries_count: int
        :param session_count: **参数解释**： 会话数量。 **取值范围**： 不涉及。
        :type session_count: int
        """
        
        

        self._average_query_waiting_time = None
        self._average_time_consumption_of_queries = None
        self._average_time_consumption_of_sessions = None
        self._queries_count = None
        self._session_count = None
        self.discriminator = None

        if average_query_waiting_time is not None:
            self.average_query_waiting_time = average_query_waiting_time
        if average_time_consumption_of_queries is not None:
            self.average_time_consumption_of_queries = average_time_consumption_of_queries
        if average_time_consumption_of_sessions is not None:
            self.average_time_consumption_of_sessions = average_time_consumption_of_sessions
        if queries_count is not None:
            self.queries_count = queries_count
        if session_count is not None:
            self.session_count = session_count

    @property
    def average_query_waiting_time(self):
        r"""Gets the average_query_waiting_time of this ListQueriesStatus.

        **参数解释**： 平均查询等待时间。 **取值范围**： 不涉及。

        :return: The average_query_waiting_time of this ListQueriesStatus.
        :rtype: float
        """
        return self._average_query_waiting_time

    @average_query_waiting_time.setter
    def average_query_waiting_time(self, average_query_waiting_time):
        r"""Sets the average_query_waiting_time of this ListQueriesStatus.

        **参数解释**： 平均查询等待时间。 **取值范围**： 不涉及。

        :param average_query_waiting_time: The average_query_waiting_time of this ListQueriesStatus.
        :type average_query_waiting_time: float
        """
        self._average_query_waiting_time = average_query_waiting_time

    @property
    def average_time_consumption_of_queries(self):
        r"""Gets the average_time_consumption_of_queries of this ListQueriesStatus.

        **参数解释**： 平均查询耗时。 **取值范围**： 不涉及。

        :return: The average_time_consumption_of_queries of this ListQueriesStatus.
        :rtype: float
        """
        return self._average_time_consumption_of_queries

    @average_time_consumption_of_queries.setter
    def average_time_consumption_of_queries(self, average_time_consumption_of_queries):
        r"""Sets the average_time_consumption_of_queries of this ListQueriesStatus.

        **参数解释**： 平均查询耗时。 **取值范围**： 不涉及。

        :param average_time_consumption_of_queries: The average_time_consumption_of_queries of this ListQueriesStatus.
        :type average_time_consumption_of_queries: float
        """
        self._average_time_consumption_of_queries = average_time_consumption_of_queries

    @property
    def average_time_consumption_of_sessions(self):
        r"""Gets the average_time_consumption_of_sessions of this ListQueriesStatus.

        **参数解释**： 平均会话耗时。 **取值范围**： 不涉及。

        :return: The average_time_consumption_of_sessions of this ListQueriesStatus.
        :rtype: float
        """
        return self._average_time_consumption_of_sessions

    @average_time_consumption_of_sessions.setter
    def average_time_consumption_of_sessions(self, average_time_consumption_of_sessions):
        r"""Sets the average_time_consumption_of_sessions of this ListQueriesStatus.

        **参数解释**： 平均会话耗时。 **取值范围**： 不涉及。

        :param average_time_consumption_of_sessions: The average_time_consumption_of_sessions of this ListQueriesStatus.
        :type average_time_consumption_of_sessions: float
        """
        self._average_time_consumption_of_sessions = average_time_consumption_of_sessions

    @property
    def queries_count(self):
        r"""Gets the queries_count of this ListQueriesStatus.

        **参数解释**： 查询数量。 **取值范围**： 不涉及。

        :return: The queries_count of this ListQueriesStatus.
        :rtype: int
        """
        return self._queries_count

    @queries_count.setter
    def queries_count(self, queries_count):
        r"""Sets the queries_count of this ListQueriesStatus.

        **参数解释**： 查询数量。 **取值范围**： 不涉及。

        :param queries_count: The queries_count of this ListQueriesStatus.
        :type queries_count: int
        """
        self._queries_count = queries_count

    @property
    def session_count(self):
        r"""Gets the session_count of this ListQueriesStatus.

        **参数解释**： 会话数量。 **取值范围**： 不涉及。

        :return: The session_count of this ListQueriesStatus.
        :rtype: int
        """
        return self._session_count

    @session_count.setter
    def session_count(self, session_count):
        r"""Sets the session_count of this ListQueriesStatus.

        **参数解释**： 会话数量。 **取值范围**： 不涉及。

        :param session_count: The session_count of this ListQueriesStatus.
        :type session_count: int
        """
        self._session_count = session_count

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
        if not isinstance(other, ListQueriesStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
