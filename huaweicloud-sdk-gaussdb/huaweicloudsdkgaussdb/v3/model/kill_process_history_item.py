# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KillProcessHistoryItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'session_id': 'str',
        'kill_time': 'str',
        'mode': 'str',
        'user': 'str',
        'host': 'str',
        'db': 'str',
        'command': 'str',
        'time': 'str',
        'info': 'str',
        'state': 'str',
        'instance_id': 'str',
        'node_id': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'session_id': 'session_id',
        'kill_time': 'kill_time',
        'mode': 'mode',
        'user': 'user',
        'host': 'host',
        'db': 'db',
        'command': 'command',
        'time': 'time',
        'info': 'info',
        'state': 'state',
        'instance_id': 'instance_id',
        'node_id': 'node_id'
    }

    def __init__(self, task_id=None, session_id=None, kill_time=None, mode=None, user=None, host=None, db=None, command=None, time=None, info=None, state=None, instance_id=None, node_id=None):
        r"""KillProcessHistoryItem

        The model defined in huaweicloud sdk

        :param task_id: **参数解释**：  自动Kill会话任务ID。  **取值范围**：  不涉及。
        :type task_id: str
        :param session_id: **参数解释**：  会话ID。  **取值范围**：  不涉及。
        :type session_id: str
        :param kill_time: **参数解释**：  Kill会话的时间戳。  **取值范围**：  不涉及。
        :type kill_time: str
        :param mode: **参数解释**：  Kill会话方式。  **取值范围**：  - once：一键Kill会话。 - condition：条件Kill会话。
        :type mode: str
        :param user: **参数解释**：  用户。  **取值范围**：  不涉及。
        :type user: str
        :param host: **参数解释**：  主机。  **取值范围**：  不涉及。
        :type host: str
        :param db: **参数解释**：  数据库名。  **取值范围**：  不涉及。
        :type db: str
        :param command: **参数解释**：  命令。  **取值范围**：  不涉及。
        :type command: str
        :param time: **参数解释**：  会话持续时间，单位是秒。  **取值范围**：  不涉及。
        :type time: str
        :param info: **参数解释**：  SQL语句。  **取值范围**：  不涉及。
        :type info: str
        :param state: **参数解释**：  执行状态。  **取值范围**：  不涉及。
        :type state: str
        :param instance_id: **参数解释**：  实例ID。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。
        :type instance_id: str
        :param node_id: **参数解释**：  节点ID。  **取值范围**：  只能由英文字母、数字组成，后缀为no07，长度为36个字符。
        :type node_id: str
        """
        
        

        self._task_id = None
        self._session_id = None
        self._kill_time = None
        self._mode = None
        self._user = None
        self._host = None
        self._db = None
        self._command = None
        self._time = None
        self._info = None
        self._state = None
        self._instance_id = None
        self._node_id = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if session_id is not None:
            self.session_id = session_id
        if kill_time is not None:
            self.kill_time = kill_time
        if mode is not None:
            self.mode = mode
        if user is not None:
            self.user = user
        if host is not None:
            self.host = host
        if db is not None:
            self.db = db
        if command is not None:
            self.command = command
        if time is not None:
            self.time = time
        if info is not None:
            self.info = info
        if state is not None:
            self.state = state
        if instance_id is not None:
            self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id

    @property
    def task_id(self):
        r"""Gets the task_id of this KillProcessHistoryItem.

        **参数解释**：  自动Kill会话任务ID。  **取值范围**：  不涉及。

        :return: The task_id of this KillProcessHistoryItem.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this KillProcessHistoryItem.

        **参数解释**：  自动Kill会话任务ID。  **取值范围**：  不涉及。

        :param task_id: The task_id of this KillProcessHistoryItem.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def session_id(self):
        r"""Gets the session_id of this KillProcessHistoryItem.

        **参数解释**：  会话ID。  **取值范围**：  不涉及。

        :return: The session_id of this KillProcessHistoryItem.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this KillProcessHistoryItem.

        **参数解释**：  会话ID。  **取值范围**：  不涉及。

        :param session_id: The session_id of this KillProcessHistoryItem.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def kill_time(self):
        r"""Gets the kill_time of this KillProcessHistoryItem.

        **参数解释**：  Kill会话的时间戳。  **取值范围**：  不涉及。

        :return: The kill_time of this KillProcessHistoryItem.
        :rtype: str
        """
        return self._kill_time

    @kill_time.setter
    def kill_time(self, kill_time):
        r"""Sets the kill_time of this KillProcessHistoryItem.

        **参数解释**：  Kill会话的时间戳。  **取值范围**：  不涉及。

        :param kill_time: The kill_time of this KillProcessHistoryItem.
        :type kill_time: str
        """
        self._kill_time = kill_time

    @property
    def mode(self):
        r"""Gets the mode of this KillProcessHistoryItem.

        **参数解释**：  Kill会话方式。  **取值范围**：  - once：一键Kill会话。 - condition：条件Kill会话。

        :return: The mode of this KillProcessHistoryItem.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this KillProcessHistoryItem.

        **参数解释**：  Kill会话方式。  **取值范围**：  - once：一键Kill会话。 - condition：条件Kill会话。

        :param mode: The mode of this KillProcessHistoryItem.
        :type mode: str
        """
        self._mode = mode

    @property
    def user(self):
        r"""Gets the user of this KillProcessHistoryItem.

        **参数解释**：  用户。  **取值范围**：  不涉及。

        :return: The user of this KillProcessHistoryItem.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this KillProcessHistoryItem.

        **参数解释**：  用户。  **取值范围**：  不涉及。

        :param user: The user of this KillProcessHistoryItem.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this KillProcessHistoryItem.

        **参数解释**：  主机。  **取值范围**：  不涉及。

        :return: The host of this KillProcessHistoryItem.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this KillProcessHistoryItem.

        **参数解释**：  主机。  **取值范围**：  不涉及。

        :param host: The host of this KillProcessHistoryItem.
        :type host: str
        """
        self._host = host

    @property
    def db(self):
        r"""Gets the db of this KillProcessHistoryItem.

        **参数解释**：  数据库名。  **取值范围**：  不涉及。

        :return: The db of this KillProcessHistoryItem.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this KillProcessHistoryItem.

        **参数解释**：  数据库名。  **取值范围**：  不涉及。

        :param db: The db of this KillProcessHistoryItem.
        :type db: str
        """
        self._db = db

    @property
    def command(self):
        r"""Gets the command of this KillProcessHistoryItem.

        **参数解释**：  命令。  **取值范围**：  不涉及。

        :return: The command of this KillProcessHistoryItem.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this KillProcessHistoryItem.

        **参数解释**：  命令。  **取值范围**：  不涉及。

        :param command: The command of this KillProcessHistoryItem.
        :type command: str
        """
        self._command = command

    @property
    def time(self):
        r"""Gets the time of this KillProcessHistoryItem.

        **参数解释**：  会话持续时间，单位是秒。  **取值范围**：  不涉及。

        :return: The time of this KillProcessHistoryItem.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this KillProcessHistoryItem.

        **参数解释**：  会话持续时间，单位是秒。  **取值范围**：  不涉及。

        :param time: The time of this KillProcessHistoryItem.
        :type time: str
        """
        self._time = time

    @property
    def info(self):
        r"""Gets the info of this KillProcessHistoryItem.

        **参数解释**：  SQL语句。  **取值范围**：  不涉及。

        :return: The info of this KillProcessHistoryItem.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this KillProcessHistoryItem.

        **参数解释**：  SQL语句。  **取值范围**：  不涉及。

        :param info: The info of this KillProcessHistoryItem.
        :type info: str
        """
        self._info = info

    @property
    def state(self):
        r"""Gets the state of this KillProcessHistoryItem.

        **参数解释**：  执行状态。  **取值范围**：  不涉及。

        :return: The state of this KillProcessHistoryItem.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this KillProcessHistoryItem.

        **参数解释**：  执行状态。  **取值范围**：  不涉及。

        :param state: The state of this KillProcessHistoryItem.
        :type state: str
        """
        self._state = state

    @property
    def instance_id(self):
        r"""Gets the instance_id of this KillProcessHistoryItem.

        **参数解释**：  实例ID。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。

        :return: The instance_id of this KillProcessHistoryItem.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this KillProcessHistoryItem.

        **参数解释**：  实例ID。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。

        :param instance_id: The instance_id of this KillProcessHistoryItem.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this KillProcessHistoryItem.

        **参数解释**：  节点ID。  **取值范围**：  只能由英文字母、数字组成，后缀为no07，长度为36个字符。

        :return: The node_id of this KillProcessHistoryItem.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this KillProcessHistoryItem.

        **参数解释**：  节点ID。  **取值范围**：  只能由英文字母、数字组成，后缀为no07，长度为36个字符。

        :param node_id: The node_id of this KillProcessHistoryItem.
        :type node_id: str
        """
        self._node_id = node_id

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
        if not isinstance(other, KillProcessHistoryItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
