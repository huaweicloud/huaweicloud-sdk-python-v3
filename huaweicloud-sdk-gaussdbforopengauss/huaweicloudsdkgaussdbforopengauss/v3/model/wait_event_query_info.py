# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WaitEventQueryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'user_name': 'str',
        'waiting': 'str',
        'session_id': 'str',
        'block_session_id': 'str',
        'block_count': 'str',
        'unique_sql_id': 'str',
        'query_id': 'str',
        'state': 'str',
        'wait_event': 'str',
        'wait_status': 'str'
    }

    attribute_map = {
        'database_name': 'database_name',
        'user_name': 'user_name',
        'waiting': 'waiting',
        'session_id': 'session_id',
        'block_session_id': 'block_session_id',
        'block_count': 'block_count',
        'unique_sql_id': 'unique_sql_id',
        'query_id': 'query_id',
        'state': 'state',
        'wait_event': 'wait_event',
        'wait_status': 'wait_status'
    }

    def __init__(self, database_name=None, user_name=None, waiting=None, session_id=None, block_session_id=None, block_count=None, unique_sql_id=None, query_id=None, state=None, wait_event=None, wait_status=None):
        r"""WaitEventQueryInfo

        The model defined in huaweicloud sdk

        :param database_name: **参数解释**: 数据库名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type database_name: str
        :param user_name: **参数解释**: 用户名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type user_name: str
        :param waiting: **参数解释**: 是否在等待状态。 **约束限制**: 不涉及。 **取值范围**: -t：是。 -f：否。 **默认取值**: 不涉及。
        :type waiting: str
        :param session_id: **参数解释**: 会话ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type session_id: str
        :param block_session_id: **参数解释**: 阻塞当前会话的会话ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type block_session_id: str
        :param block_count: **参数解释**: 阻塞当前会话的会话数。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type block_count: str
        :param unique_sql_id: **参数解释**: 唯一的SQL ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type unique_sql_id: str
        :param query_id: **参数解释**: SQL查询ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type query_id: str
        :param state: **参数解释**: 该会话当前整体状态。 **约束限制**: 不涉及。 **取值范围**: -active：后台正在执行一个查询。 -idle：后台正在等待一个新的客户端命令。 -idle in transaction：后台在事务中，但事务中没有语句在执行。 -fastpath function call：后台正在执行一个fast-path函数。 -disabled：如果后台禁用track_activities，则事务显示此状态。 **默认取值**: 不涉及。
        :type state: str
        :param wait_event: **参数解释**: 等待事件。 参见“开发指南 &gt; 系统表和系统视图 &gt; 系统视图 &gt; 其他系统视图 &gt; PG_THREAD_WAIT_STATUS”中的wait_event字段。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type wait_event: str
        :param wait_status: **参数解释**: 等待状态。 参见“开发指南 &gt; 系统表和系统视图 &gt; 系统视图 &gt; 其他系统视图 &gt; PG_THREAD_WAIT_STATUS”中的wait_status列表。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type wait_status: str
        """
        
        

        self._database_name = None
        self._user_name = None
        self._waiting = None
        self._session_id = None
        self._block_session_id = None
        self._block_count = None
        self._unique_sql_id = None
        self._query_id = None
        self._state = None
        self._wait_event = None
        self._wait_status = None
        self.discriminator = None

        if database_name is not None:
            self.database_name = database_name
        if user_name is not None:
            self.user_name = user_name
        if waiting is not None:
            self.waiting = waiting
        if session_id is not None:
            self.session_id = session_id
        if block_session_id is not None:
            self.block_session_id = block_session_id
        if block_count is not None:
            self.block_count = block_count
        if unique_sql_id is not None:
            self.unique_sql_id = unique_sql_id
        if query_id is not None:
            self.query_id = query_id
        if state is not None:
            self.state = state
        if wait_event is not None:
            self.wait_event = wait_event
        if wait_status is not None:
            self.wait_status = wait_status

    @property
    def database_name(self):
        r"""Gets the database_name of this WaitEventQueryInfo.

        **参数解释**: 数据库名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The database_name of this WaitEventQueryInfo.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this WaitEventQueryInfo.

        **参数解释**: 数据库名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param database_name: The database_name of this WaitEventQueryInfo.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def user_name(self):
        r"""Gets the user_name of this WaitEventQueryInfo.

        **参数解释**: 用户名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The user_name of this WaitEventQueryInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this WaitEventQueryInfo.

        **参数解释**: 用户名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param user_name: The user_name of this WaitEventQueryInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def waiting(self):
        r"""Gets the waiting of this WaitEventQueryInfo.

        **参数解释**: 是否在等待状态。 **约束限制**: 不涉及。 **取值范围**: -t：是。 -f：否。 **默认取值**: 不涉及。

        :return: The waiting of this WaitEventQueryInfo.
        :rtype: str
        """
        return self._waiting

    @waiting.setter
    def waiting(self, waiting):
        r"""Sets the waiting of this WaitEventQueryInfo.

        **参数解释**: 是否在等待状态。 **约束限制**: 不涉及。 **取值范围**: -t：是。 -f：否。 **默认取值**: 不涉及。

        :param waiting: The waiting of this WaitEventQueryInfo.
        :type waiting: str
        """
        self._waiting = waiting

    @property
    def session_id(self):
        r"""Gets the session_id of this WaitEventQueryInfo.

        **参数解释**: 会话ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The session_id of this WaitEventQueryInfo.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this WaitEventQueryInfo.

        **参数解释**: 会话ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param session_id: The session_id of this WaitEventQueryInfo.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def block_session_id(self):
        r"""Gets the block_session_id of this WaitEventQueryInfo.

        **参数解释**: 阻塞当前会话的会话ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The block_session_id of this WaitEventQueryInfo.
        :rtype: str
        """
        return self._block_session_id

    @block_session_id.setter
    def block_session_id(self, block_session_id):
        r"""Sets the block_session_id of this WaitEventQueryInfo.

        **参数解释**: 阻塞当前会话的会话ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param block_session_id: The block_session_id of this WaitEventQueryInfo.
        :type block_session_id: str
        """
        self._block_session_id = block_session_id

    @property
    def block_count(self):
        r"""Gets the block_count of this WaitEventQueryInfo.

        **参数解释**: 阻塞当前会话的会话数。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The block_count of this WaitEventQueryInfo.
        :rtype: str
        """
        return self._block_count

    @block_count.setter
    def block_count(self, block_count):
        r"""Sets the block_count of this WaitEventQueryInfo.

        **参数解释**: 阻塞当前会话的会话数。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param block_count: The block_count of this WaitEventQueryInfo.
        :type block_count: str
        """
        self._block_count = block_count

    @property
    def unique_sql_id(self):
        r"""Gets the unique_sql_id of this WaitEventQueryInfo.

        **参数解释**: 唯一的SQL ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The unique_sql_id of this WaitEventQueryInfo.
        :rtype: str
        """
        return self._unique_sql_id

    @unique_sql_id.setter
    def unique_sql_id(self, unique_sql_id):
        r"""Sets the unique_sql_id of this WaitEventQueryInfo.

        **参数解释**: 唯一的SQL ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param unique_sql_id: The unique_sql_id of this WaitEventQueryInfo.
        :type unique_sql_id: str
        """
        self._unique_sql_id = unique_sql_id

    @property
    def query_id(self):
        r"""Gets the query_id of this WaitEventQueryInfo.

        **参数解释**: SQL查询ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The query_id of this WaitEventQueryInfo.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        r"""Sets the query_id of this WaitEventQueryInfo.

        **参数解释**: SQL查询ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param query_id: The query_id of this WaitEventQueryInfo.
        :type query_id: str
        """
        self._query_id = query_id

    @property
    def state(self):
        r"""Gets the state of this WaitEventQueryInfo.

        **参数解释**: 该会话当前整体状态。 **约束限制**: 不涉及。 **取值范围**: -active：后台正在执行一个查询。 -idle：后台正在等待一个新的客户端命令。 -idle in transaction：后台在事务中，但事务中没有语句在执行。 -fastpath function call：后台正在执行一个fast-path函数。 -disabled：如果后台禁用track_activities，则事务显示此状态。 **默认取值**: 不涉及。

        :return: The state of this WaitEventQueryInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this WaitEventQueryInfo.

        **参数解释**: 该会话当前整体状态。 **约束限制**: 不涉及。 **取值范围**: -active：后台正在执行一个查询。 -idle：后台正在等待一个新的客户端命令。 -idle in transaction：后台在事务中，但事务中没有语句在执行。 -fastpath function call：后台正在执行一个fast-path函数。 -disabled：如果后台禁用track_activities，则事务显示此状态。 **默认取值**: 不涉及。

        :param state: The state of this WaitEventQueryInfo.
        :type state: str
        """
        self._state = state

    @property
    def wait_event(self):
        r"""Gets the wait_event of this WaitEventQueryInfo.

        **参数解释**: 等待事件。 参见“开发指南 > 系统表和系统视图 > 系统视图 > 其他系统视图 > PG_THREAD_WAIT_STATUS”中的wait_event字段。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The wait_event of this WaitEventQueryInfo.
        :rtype: str
        """
        return self._wait_event

    @wait_event.setter
    def wait_event(self, wait_event):
        r"""Sets the wait_event of this WaitEventQueryInfo.

        **参数解释**: 等待事件。 参见“开发指南 > 系统表和系统视图 > 系统视图 > 其他系统视图 > PG_THREAD_WAIT_STATUS”中的wait_event字段。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param wait_event: The wait_event of this WaitEventQueryInfo.
        :type wait_event: str
        """
        self._wait_event = wait_event

    @property
    def wait_status(self):
        r"""Gets the wait_status of this WaitEventQueryInfo.

        **参数解释**: 等待状态。 参见“开发指南 > 系统表和系统视图 > 系统视图 > 其他系统视图 > PG_THREAD_WAIT_STATUS”中的wait_status列表。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The wait_status of this WaitEventQueryInfo.
        :rtype: str
        """
        return self._wait_status

    @wait_status.setter
    def wait_status(self, wait_status):
        r"""Sets the wait_status of this WaitEventQueryInfo.

        **参数解释**: 等待状态。 参见“开发指南 > 系统表和系统视图 > 系统视图 > 其他系统视图 > PG_THREAD_WAIT_STATUS”中的wait_status列表。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param wait_status: The wait_status of this WaitEventQueryInfo.
        :type wait_status: str
        """
        self._wait_status = wait_status

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
        if not isinstance(other, WaitEventQueryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
