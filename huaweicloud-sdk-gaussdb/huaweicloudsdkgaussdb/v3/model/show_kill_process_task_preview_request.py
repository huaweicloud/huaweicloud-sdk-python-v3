# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKillProcessTaskPreviewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'time': 'str',
        'user': 'str',
        'host': 'str',
        'db': 'str',
        'command': 'str',
        'info': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'time': 'time',
        'user': 'user',
        'host': 'host',
        'db': 'db',
        'command': 'command',
        'info': 'info'
    }

    def __init__(self, x_language=None, instance_id=None, time=None, user=None, host=None, db=None, command=None, info=None):
        r"""ShowKillProcessTaskPreviewRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文。 - zh-cn：中文。  **默认取值**：  en-us。
        :type x_language: str
        :param instance_id: **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。
        :type instance_id: str
        :param time: **参数解释**：    持续时间，单位为秒。持续时间大于等于该值的会话满足Kill条件。  **约束限制**：    整数。  **取值范围**：    由数字组成，其中数字表示的范围应为1-2147483647。  **默认取值**：    不涉及。
        :type time: str
        :param user: **参数解释**：  用户名。  **约束限制**：  不涉及。  **取值范围**：  名称在1到32个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符。  **默认取值**：  不涉及。
        :type user: str
        :param host: **参数解释**：    主机。    **约束限制**：    不涉及。    **取值范围**：    不涉及。  **默认取值**：    不涉及。
        :type host: str
        :param db: **参数解释**：    数据库名。    **约束限制**：    不涉及。   **取值范围**：    1到64个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符。   **默认取值**：    不涉及。
        :type db: str
        :param command: **参数解释**：    命令。    **约束限制**：    不涉及。    **取值范围**：    不涉及。  **默认取值**：    不涉及。
        :type command: str
        :param info: **参数解释**：    SQL语句。    **约束限制**：    不涉及。  **取值范围**：    不涉及。  **默认取值**：    不涉及。
        :type info: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._time = None
        self._user = None
        self._host = None
        self._db = None
        self._command = None
        self._info = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.time = time
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

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowKillProcessTaskPreviewRequest.

        **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文。 - zh-cn：中文。  **默认取值**：  en-us。

        :return: The x_language of this ShowKillProcessTaskPreviewRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowKillProcessTaskPreviewRequest.

        **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文。 - zh-cn：中文。  **默认取值**：  en-us。

        :param x_language: The x_language of this ShowKillProcessTaskPreviewRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowKillProcessTaskPreviewRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :return: The instance_id of this ShowKillProcessTaskPreviewRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowKillProcessTaskPreviewRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this ShowKillProcessTaskPreviewRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def time(self):
        r"""Gets the time of this ShowKillProcessTaskPreviewRequest.

        **参数解释**：    持续时间，单位为秒。持续时间大于等于该值的会话满足Kill条件。  **约束限制**：    整数。  **取值范围**：    由数字组成，其中数字表示的范围应为1-2147483647。  **默认取值**：    不涉及。

        :return: The time of this ShowKillProcessTaskPreviewRequest.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ShowKillProcessTaskPreviewRequest.

        **参数解释**：    持续时间，单位为秒。持续时间大于等于该值的会话满足Kill条件。  **约束限制**：    整数。  **取值范围**：    由数字组成，其中数字表示的范围应为1-2147483647。  **默认取值**：    不涉及。

        :param time: The time of this ShowKillProcessTaskPreviewRequest.
        :type time: str
        """
        self._time = time

    @property
    def user(self):
        r"""Gets the user of this ShowKillProcessTaskPreviewRequest.

        **参数解释**：  用户名。  **约束限制**：  不涉及。  **取值范围**：  名称在1到32个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符。  **默认取值**：  不涉及。

        :return: The user of this ShowKillProcessTaskPreviewRequest.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this ShowKillProcessTaskPreviewRequest.

        **参数解释**：  用户名。  **约束限制**：  不涉及。  **取值范围**：  名称在1到32个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符。  **默认取值**：  不涉及。

        :param user: The user of this ShowKillProcessTaskPreviewRequest.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this ShowKillProcessTaskPreviewRequest.

        **参数解释**：    主机。    **约束限制**：    不涉及。    **取值范围**：    不涉及。  **默认取值**：    不涉及。

        :return: The host of this ShowKillProcessTaskPreviewRequest.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this ShowKillProcessTaskPreviewRequest.

        **参数解释**：    主机。    **约束限制**：    不涉及。    **取值范围**：    不涉及。  **默认取值**：    不涉及。

        :param host: The host of this ShowKillProcessTaskPreviewRequest.
        :type host: str
        """
        self._host = host

    @property
    def db(self):
        r"""Gets the db of this ShowKillProcessTaskPreviewRequest.

        **参数解释**：    数据库名。    **约束限制**：    不涉及。   **取值范围**：    1到64个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符。   **默认取值**：    不涉及。

        :return: The db of this ShowKillProcessTaskPreviewRequest.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this ShowKillProcessTaskPreviewRequest.

        **参数解释**：    数据库名。    **约束限制**：    不涉及。   **取值范围**：    1到64个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符。   **默认取值**：    不涉及。

        :param db: The db of this ShowKillProcessTaskPreviewRequest.
        :type db: str
        """
        self._db = db

    @property
    def command(self):
        r"""Gets the command of this ShowKillProcessTaskPreviewRequest.

        **参数解释**：    命令。    **约束限制**：    不涉及。    **取值范围**：    不涉及。  **默认取值**：    不涉及。

        :return: The command of this ShowKillProcessTaskPreviewRequest.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this ShowKillProcessTaskPreviewRequest.

        **参数解释**：    命令。    **约束限制**：    不涉及。    **取值范围**：    不涉及。  **默认取值**：    不涉及。

        :param command: The command of this ShowKillProcessTaskPreviewRequest.
        :type command: str
        """
        self._command = command

    @property
    def info(self):
        r"""Gets the info of this ShowKillProcessTaskPreviewRequest.

        **参数解释**：    SQL语句。    **约束限制**：    不涉及。  **取值范围**：    不涉及。  **默认取值**：    不涉及。

        :return: The info of this ShowKillProcessTaskPreviewRequest.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this ShowKillProcessTaskPreviewRequest.

        **参数解释**：    SQL语句。    **约束限制**：    不涉及。  **取值范围**：    不涉及。  **默认取值**：    不涉及。

        :param info: The info of this ShowKillProcessTaskPreviewRequest.
        :type info: str
        """
        self._info = info

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
        if not isinstance(other, ShowKillProcessTaskPreviewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
