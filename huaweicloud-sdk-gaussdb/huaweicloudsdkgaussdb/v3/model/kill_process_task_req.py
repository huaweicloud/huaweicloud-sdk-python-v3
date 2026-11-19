# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KillProcessTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user': 'str',
        'host': 'str',
        'db': 'str',
        'command': 'str',
        'info': 'str',
        'time': 'str',
        'end_time': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'user': 'user',
        'host': 'host',
        'db': 'db',
        'command': 'command',
        'info': 'info',
        'time': 'time',
        'end_time': 'end_time',
        'mode': 'mode'
    }

    def __init__(self, user=None, host=None, db=None, command=None, info=None, time=None, end_time=None, mode=None):
        r"""KillProcessTaskReq

        The model defined in huaweicloud sdk

        :param user: **参数解释**：  用户名。  **约束限制**：  不涉及。  **取值范围**：  1到32个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符。  **默认取值**：  不涉及。
        :type user: str
        :param host: **参数解释**：  主机。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type host: str
        :param db: **参数解释**：  数据库名。  **约束限制**：  不涉及。  **取值范围**：  1到64个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符。   **默认取值**：  不涉及。
        :type db: str
        :param command: **参数解释**：  命令。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type command: str
        :param info: **参数解释**：  SQL语句。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type info: str
        :param time: **参数解释**：  持续时间，单位为秒。持续时间大于等于该值的会话满足Kill条件。  **约束限制**：  必须是整数。  **取值范围**：  1-2147483647。  **默认取值**：  不涉及。
        :type time: str
        :param end_time: **参数解释**：  任务持续时间，单位为秒。  **约束限制**：  执行方式为auto时必填。  **取值范围**：  10-31535999。  **默认取值**：  不涉及。
        :type end_time: str
        :param mode: **参数解释**：  执行方式。  **约束限制**：  不涉及。  **取值范围**：  - auto：定时关闭，任务持续时长等于end_time参数值。 - manual：手动关闭。  **默认取值**：  不涉及。
        :type mode: str
        """
        
        

        self._user = None
        self._host = None
        self._db = None
        self._command = None
        self._info = None
        self._time = None
        self._end_time = None
        self._mode = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if host is not None:
            self.host = host
        if db is not None:
            self.db = db
        if command is not None:
            self.command = command
        if info is not None:
            self.info = info
        self.time = time
        if end_time is not None:
            self.end_time = end_time
        self.mode = mode

    @property
    def user(self):
        r"""Gets the user of this KillProcessTaskReq.

        **参数解释**：  用户名。  **约束限制**：  不涉及。  **取值范围**：  1到32个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符。  **默认取值**：  不涉及。

        :return: The user of this KillProcessTaskReq.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this KillProcessTaskReq.

        **参数解释**：  用户名。  **约束限制**：  不涉及。  **取值范围**：  1到32个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符。  **默认取值**：  不涉及。

        :param user: The user of this KillProcessTaskReq.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this KillProcessTaskReq.

        **参数解释**：  主机。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The host of this KillProcessTaskReq.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this KillProcessTaskReq.

        **参数解释**：  主机。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param host: The host of this KillProcessTaskReq.
        :type host: str
        """
        self._host = host

    @property
    def db(self):
        r"""Gets the db of this KillProcessTaskReq.

        **参数解释**：  数据库名。  **约束限制**：  不涉及。  **取值范围**：  1到64个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符。   **默认取值**：  不涉及。

        :return: The db of this KillProcessTaskReq.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this KillProcessTaskReq.

        **参数解释**：  数据库名。  **约束限制**：  不涉及。  **取值范围**：  1到64个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符。   **默认取值**：  不涉及。

        :param db: The db of this KillProcessTaskReq.
        :type db: str
        """
        self._db = db

    @property
    def command(self):
        r"""Gets the command of this KillProcessTaskReq.

        **参数解释**：  命令。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The command of this KillProcessTaskReq.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this KillProcessTaskReq.

        **参数解释**：  命令。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param command: The command of this KillProcessTaskReq.
        :type command: str
        """
        self._command = command

    @property
    def info(self):
        r"""Gets the info of this KillProcessTaskReq.

        **参数解释**：  SQL语句。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The info of this KillProcessTaskReq.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this KillProcessTaskReq.

        **参数解释**：  SQL语句。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param info: The info of this KillProcessTaskReq.
        :type info: str
        """
        self._info = info

    @property
    def time(self):
        r"""Gets the time of this KillProcessTaskReq.

        **参数解释**：  持续时间，单位为秒。持续时间大于等于该值的会话满足Kill条件。  **约束限制**：  必须是整数。  **取值范围**：  1-2147483647。  **默认取值**：  不涉及。

        :return: The time of this KillProcessTaskReq.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this KillProcessTaskReq.

        **参数解释**：  持续时间，单位为秒。持续时间大于等于该值的会话满足Kill条件。  **约束限制**：  必须是整数。  **取值范围**：  1-2147483647。  **默认取值**：  不涉及。

        :param time: The time of this KillProcessTaskReq.
        :type time: str
        """
        self._time = time

    @property
    def end_time(self):
        r"""Gets the end_time of this KillProcessTaskReq.

        **参数解释**：  任务持续时间，单位为秒。  **约束限制**：  执行方式为auto时必填。  **取值范围**：  10-31535999。  **默认取值**：  不涉及。

        :return: The end_time of this KillProcessTaskReq.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this KillProcessTaskReq.

        **参数解释**：  任务持续时间，单位为秒。  **约束限制**：  执行方式为auto时必填。  **取值范围**：  10-31535999。  **默认取值**：  不涉及。

        :param end_time: The end_time of this KillProcessTaskReq.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def mode(self):
        r"""Gets the mode of this KillProcessTaskReq.

        **参数解释**：  执行方式。  **约束限制**：  不涉及。  **取值范围**：  - auto：定时关闭，任务持续时长等于end_time参数值。 - manual：手动关闭。  **默认取值**：  不涉及。

        :return: The mode of this KillProcessTaskReq.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this KillProcessTaskReq.

        **参数解释**：  执行方式。  **约束限制**：  不涉及。  **取值范围**：  - auto：定时关闭，任务持续时长等于end_time参数值。 - manual：手动关闭。  **默认取值**：  不涉及。

        :param mode: The mode of this KillProcessTaskReq.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, KillProcessTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
