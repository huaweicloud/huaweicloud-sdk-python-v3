# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KillProcessItem:

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
        'instance_id': 'str',
        'user': 'str',
        'host': 'str',
        'db': 'str',
        'command': 'str',
        'info': 'str',
        'time': 'str',
        'end_time': 'str',
        'mode': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'user': 'user',
        'host': 'host',
        'db': 'db',
        'command': 'command',
        'info': 'info',
        'time': 'time',
        'end_time': 'end_time',
        'mode': 'mode',
        'status': 'status'
    }

    def __init__(self, id=None, instance_id=None, user=None, host=None, db=None, command=None, info=None, time=None, end_time=None, mode=None, status=None):
        r"""KillProcessItem

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  任务ID。  **取值范围**：  不涉及。
        :type id: str
        :param instance_id: **参数解释**：  实例ID。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。
        :type instance_id: str
        :param user: **参数解释**：  用户名。  **取值范围**：  不涉及。
        :type user: str
        :param host: **参数解释**：  主机。  **取值范围**：  不涉及。
        :type host: str
        :param db: **参数解释**：  数据库名。  **取值范围**：  不涉及。
        :type db: str
        :param command: **参数解释**：  命令。  **取值范围**：  不涉及。
        :type command: str
        :param info: **参数解释**：  SQL语句。  **取值范围**：  不涉及。
        :type info: str
        :param time: **参数解释**：  持续时间，单位为秒。持续时间大于等于该值的会话满足Kill条件。  **取值范围**：  由数字组成，表示的范围应为1-2147483647。
        :type time: str
        :param end_time: **参数解释**：  任务结束时间戳。  **取值范围**：  不涉及。
        :type end_time: str
        :param mode: **参数解释**：  执行方式。  **取值范围**：  - auto：定时关闭，任务持续时长等于end_time参数值。 - manual：手动关闭。
        :type mode: str
        :param status: **参数解释**：  任务状态。  **取值范围**：  - 0：已结束。 - 1：运行中。
        :type status: str
        """
        
        

        self._id = None
        self._instance_id = None
        self._user = None
        self._host = None
        self._db = None
        self._command = None
        self._info = None
        self._time = None
        self._end_time = None
        self._mode = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
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
        if time is not None:
            self.time = time
        if end_time is not None:
            self.end_time = end_time
        if mode is not None:
            self.mode = mode
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this KillProcessItem.

        **参数解释**：  任务ID。  **取值范围**：  不涉及。

        :return: The id of this KillProcessItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this KillProcessItem.

        **参数解释**：  任务ID。  **取值范围**：  不涉及。

        :param id: The id of this KillProcessItem.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this KillProcessItem.

        **参数解释**：  实例ID。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。

        :return: The instance_id of this KillProcessItem.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this KillProcessItem.

        **参数解释**：  实例ID。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。

        :param instance_id: The instance_id of this KillProcessItem.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def user(self):
        r"""Gets the user of this KillProcessItem.

        **参数解释**：  用户名。  **取值范围**：  不涉及。

        :return: The user of this KillProcessItem.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this KillProcessItem.

        **参数解释**：  用户名。  **取值范围**：  不涉及。

        :param user: The user of this KillProcessItem.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this KillProcessItem.

        **参数解释**：  主机。  **取值范围**：  不涉及。

        :return: The host of this KillProcessItem.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this KillProcessItem.

        **参数解释**：  主机。  **取值范围**：  不涉及。

        :param host: The host of this KillProcessItem.
        :type host: str
        """
        self._host = host

    @property
    def db(self):
        r"""Gets the db of this KillProcessItem.

        **参数解释**：  数据库名。  **取值范围**：  不涉及。

        :return: The db of this KillProcessItem.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this KillProcessItem.

        **参数解释**：  数据库名。  **取值范围**：  不涉及。

        :param db: The db of this KillProcessItem.
        :type db: str
        """
        self._db = db

    @property
    def command(self):
        r"""Gets the command of this KillProcessItem.

        **参数解释**：  命令。  **取值范围**：  不涉及。

        :return: The command of this KillProcessItem.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this KillProcessItem.

        **参数解释**：  命令。  **取值范围**：  不涉及。

        :param command: The command of this KillProcessItem.
        :type command: str
        """
        self._command = command

    @property
    def info(self):
        r"""Gets the info of this KillProcessItem.

        **参数解释**：  SQL语句。  **取值范围**：  不涉及。

        :return: The info of this KillProcessItem.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this KillProcessItem.

        **参数解释**：  SQL语句。  **取值范围**：  不涉及。

        :param info: The info of this KillProcessItem.
        :type info: str
        """
        self._info = info

    @property
    def time(self):
        r"""Gets the time of this KillProcessItem.

        **参数解释**：  持续时间，单位为秒。持续时间大于等于该值的会话满足Kill条件。  **取值范围**：  由数字组成，表示的范围应为1-2147483647。

        :return: The time of this KillProcessItem.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this KillProcessItem.

        **参数解释**：  持续时间，单位为秒。持续时间大于等于该值的会话满足Kill条件。  **取值范围**：  由数字组成，表示的范围应为1-2147483647。

        :param time: The time of this KillProcessItem.
        :type time: str
        """
        self._time = time

    @property
    def end_time(self):
        r"""Gets the end_time of this KillProcessItem.

        **参数解释**：  任务结束时间戳。  **取值范围**：  不涉及。

        :return: The end_time of this KillProcessItem.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this KillProcessItem.

        **参数解释**：  任务结束时间戳。  **取值范围**：  不涉及。

        :param end_time: The end_time of this KillProcessItem.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def mode(self):
        r"""Gets the mode of this KillProcessItem.

        **参数解释**：  执行方式。  **取值范围**：  - auto：定时关闭，任务持续时长等于end_time参数值。 - manual：手动关闭。

        :return: The mode of this KillProcessItem.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this KillProcessItem.

        **参数解释**：  执行方式。  **取值范围**：  - auto：定时关闭，任务持续时长等于end_time参数值。 - manual：手动关闭。

        :param mode: The mode of this KillProcessItem.
        :type mode: str
        """
        self._mode = mode

    @property
    def status(self):
        r"""Gets the status of this KillProcessItem.

        **参数解释**：  任务状态。  **取值范围**：  - 0：已结束。 - 1：运行中。

        :return: The status of this KillProcessItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this KillProcessItem.

        **参数解释**：  任务状态。  **取值范围**：  - 0：已结束。 - 1：运行中。

        :param status: The status of this KillProcessItem.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, KillProcessItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
