# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HtapProcessInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'user': 'str',
        'host': 'str',
        'state': 'str',
        'database': 'str',
        'sql_statement': 'str',
        'duration': 'str',
        'command': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'host': 'host',
        'state': 'state',
        'database': 'database',
        'sql_statement': 'sql_statement',
        'duration': 'duration',
        'command': 'command'
    }

    def __init__(self, id=None, user=None, host=None, state=None, database=None, sql_statement=None, duration=None, command=None):
        r"""HtapProcessInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  会话ID。    **取值范围**：  不涉及。
        :type id: str
        :param user: **参数解释**：  会话用户名。    **取值范围**：  不涉及。
        :type user: str
        :param host: **参数解释**：  会话主机。    **取值范围**：  不涉及。
        :type host: str
        :param state: **参数解释**：  会话状态。  **取值范围**：  不涉及。
        :type state: str
        :param database: **参数解释**：  会话对应数据库。    **取值范围**：  不涉及。
        :type database: str
        :param sql_statement: **参数解释**：  会话执行的SQL语句。    **取值范围**：  不涉及。
        :type sql_statement: str
        :param duration: **参数解释**：  会话持续时间，单位是秒。  **取值范围**：  不涉及。
        :type duration: str
        :param command: **参数解释**：  会话命令类型。    **取值范围**：  不涉及。
        :type command: str
        """
        
        

        self._id = None
        self._user = None
        self._host = None
        self._state = None
        self._database = None
        self._sql_statement = None
        self._duration = None
        self._command = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user is not None:
            self.user = user
        if host is not None:
            self.host = host
        if state is not None:
            self.state = state
        if database is not None:
            self.database = database
        if sql_statement is not None:
            self.sql_statement = sql_statement
        if duration is not None:
            self.duration = duration
        if command is not None:
            self.command = command

    @property
    def id(self):
        r"""Gets the id of this HtapProcessInfo.

        **参数解释**：  会话ID。    **取值范围**：  不涉及。

        :return: The id of this HtapProcessInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HtapProcessInfo.

        **参数解释**：  会话ID。    **取值范围**：  不涉及。

        :param id: The id of this HtapProcessInfo.
        :type id: str
        """
        self._id = id

    @property
    def user(self):
        r"""Gets the user of this HtapProcessInfo.

        **参数解释**：  会话用户名。    **取值范围**：  不涉及。

        :return: The user of this HtapProcessInfo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this HtapProcessInfo.

        **参数解释**：  会话用户名。    **取值范围**：  不涉及。

        :param user: The user of this HtapProcessInfo.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this HtapProcessInfo.

        **参数解释**：  会话主机。    **取值范围**：  不涉及。

        :return: The host of this HtapProcessInfo.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this HtapProcessInfo.

        **参数解释**：  会话主机。    **取值范围**：  不涉及。

        :param host: The host of this HtapProcessInfo.
        :type host: str
        """
        self._host = host

    @property
    def state(self):
        r"""Gets the state of this HtapProcessInfo.

        **参数解释**：  会话状态。  **取值范围**：  不涉及。

        :return: The state of this HtapProcessInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this HtapProcessInfo.

        **参数解释**：  会话状态。  **取值范围**：  不涉及。

        :param state: The state of this HtapProcessInfo.
        :type state: str
        """
        self._state = state

    @property
    def database(self):
        r"""Gets the database of this HtapProcessInfo.

        **参数解释**：  会话对应数据库。    **取值范围**：  不涉及。

        :return: The database of this HtapProcessInfo.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this HtapProcessInfo.

        **参数解释**：  会话对应数据库。    **取值范围**：  不涉及。

        :param database: The database of this HtapProcessInfo.
        :type database: str
        """
        self._database = database

    @property
    def sql_statement(self):
        r"""Gets the sql_statement of this HtapProcessInfo.

        **参数解释**：  会话执行的SQL语句。    **取值范围**：  不涉及。

        :return: The sql_statement of this HtapProcessInfo.
        :rtype: str
        """
        return self._sql_statement

    @sql_statement.setter
    def sql_statement(self, sql_statement):
        r"""Sets the sql_statement of this HtapProcessInfo.

        **参数解释**：  会话执行的SQL语句。    **取值范围**：  不涉及。

        :param sql_statement: The sql_statement of this HtapProcessInfo.
        :type sql_statement: str
        """
        self._sql_statement = sql_statement

    @property
    def duration(self):
        r"""Gets the duration of this HtapProcessInfo.

        **参数解释**：  会话持续时间，单位是秒。  **取值范围**：  不涉及。

        :return: The duration of this HtapProcessInfo.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this HtapProcessInfo.

        **参数解释**：  会话持续时间，单位是秒。  **取值范围**：  不涉及。

        :param duration: The duration of this HtapProcessInfo.
        :type duration: str
        """
        self._duration = duration

    @property
    def command(self):
        r"""Gets the command of this HtapProcessInfo.

        **参数解释**：  会话命令类型。    **取值范围**：  不涉及。

        :return: The command of this HtapProcessInfo.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this HtapProcessInfo.

        **参数解释**：  会话命令类型。    **取值范围**：  不涉及。

        :param command: The command of this HtapProcessInfo.
        :type command: str
        """
        self._command = command

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
        if not isinstance(other, HtapProcessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
