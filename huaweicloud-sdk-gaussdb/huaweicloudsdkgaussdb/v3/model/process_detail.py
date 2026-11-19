# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'user': 'str',
        'db': 'str',
        'state': 'str',
        'command': 'str',
        'sql_info': 'str',
        'state_duration': 'int'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'db': 'db',
        'state': 'state',
        'command': 'command',
        'sql_info': 'sql_info',
        'state_duration': 'state_duration'
    }

    def __init__(self, id=None, user=None, db=None, state=None, command=None, sql_info=None, state_duration=None):
        r"""ProcessDetail

        The model defined in huaweicloud sdk

        :param id: **参数解释**  会话ID。  **取值范围**：  不涉及。
        :type id: int
        :param user: **参数解释**：  用户名。  **取值范围**：  不涉及。
        :type user: str
        :param db: **参数解释**：    数据库名。    **取值范围**：    不涉及。
        :type db: str
        :param state: **参数解释**：  执行状态。  **取值范围**：  不涉及。
        :type state: str
        :param command: **参数解释**：  命令。  **取值范围**：  不涉及。
        :type command: str
        :param sql_info: **参数解释**：  SQL语句。  **取值范围**：  不涉及。
        :type sql_info: str
        :param state_duration: **参数解释**：  状态持续时间，单位是秒。  **取值范围**：  不涉及。
        :type state_duration: int
        """
        
        

        self._id = None
        self._user = None
        self._db = None
        self._state = None
        self._command = None
        self._sql_info = None
        self._state_duration = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user is not None:
            self.user = user
        if db is not None:
            self.db = db
        if state is not None:
            self.state = state
        if command is not None:
            self.command = command
        if sql_info is not None:
            self.sql_info = sql_info
        if state_duration is not None:
            self.state_duration = state_duration

    @property
    def id(self):
        r"""Gets the id of this ProcessDetail.

        **参数解释**  会话ID。  **取值范围**：  不涉及。

        :return: The id of this ProcessDetail.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProcessDetail.

        **参数解释**  会话ID。  **取值范围**：  不涉及。

        :param id: The id of this ProcessDetail.
        :type id: int
        """
        self._id = id

    @property
    def user(self):
        r"""Gets the user of this ProcessDetail.

        **参数解释**：  用户名。  **取值范围**：  不涉及。

        :return: The user of this ProcessDetail.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this ProcessDetail.

        **参数解释**：  用户名。  **取值范围**：  不涉及。

        :param user: The user of this ProcessDetail.
        :type user: str
        """
        self._user = user

    @property
    def db(self):
        r"""Gets the db of this ProcessDetail.

        **参数解释**：    数据库名。    **取值范围**：    不涉及。

        :return: The db of this ProcessDetail.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this ProcessDetail.

        **参数解释**：    数据库名。    **取值范围**：    不涉及。

        :param db: The db of this ProcessDetail.
        :type db: str
        """
        self._db = db

    @property
    def state(self):
        r"""Gets the state of this ProcessDetail.

        **参数解释**：  执行状态。  **取值范围**：  不涉及。

        :return: The state of this ProcessDetail.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ProcessDetail.

        **参数解释**：  执行状态。  **取值范围**：  不涉及。

        :param state: The state of this ProcessDetail.
        :type state: str
        """
        self._state = state

    @property
    def command(self):
        r"""Gets the command of this ProcessDetail.

        **参数解释**：  命令。  **取值范围**：  不涉及。

        :return: The command of this ProcessDetail.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this ProcessDetail.

        **参数解释**：  命令。  **取值范围**：  不涉及。

        :param command: The command of this ProcessDetail.
        :type command: str
        """
        self._command = command

    @property
    def sql_info(self):
        r"""Gets the sql_info of this ProcessDetail.

        **参数解释**：  SQL语句。  **取值范围**：  不涉及。

        :return: The sql_info of this ProcessDetail.
        :rtype: str
        """
        return self._sql_info

    @sql_info.setter
    def sql_info(self, sql_info):
        r"""Sets the sql_info of this ProcessDetail.

        **参数解释**：  SQL语句。  **取值范围**：  不涉及。

        :param sql_info: The sql_info of this ProcessDetail.
        :type sql_info: str
        """
        self._sql_info = sql_info

    @property
    def state_duration(self):
        r"""Gets the state_duration of this ProcessDetail.

        **参数解释**：  状态持续时间，单位是秒。  **取值范围**：  不涉及。

        :return: The state_duration of this ProcessDetail.
        :rtype: int
        """
        return self._state_duration

    @state_duration.setter
    def state_duration(self, state_duration):
        r"""Sets the state_duration of this ProcessDetail.

        **参数解释**：  状态持续时间，单位是秒。  **取值范围**：  不涉及。

        :param state_duration: The state_duration of this ProcessDetail.
        :type state_duration: int
        """
        self._state_duration = state_duration

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
        if not isinstance(other, ProcessDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
