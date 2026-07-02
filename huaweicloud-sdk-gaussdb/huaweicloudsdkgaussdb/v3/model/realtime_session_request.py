# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RealtimeSessionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filter': 'str',
        'slow_process_threshold': 'int',
        'user': 'str',
        'host': 'str',
        'db': 'str',
        'command': 'str',
        'sql_key': 'str',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'filter': 'filter',
        'slow_process_threshold': 'slow_process_threshold',
        'user': 'user',
        'host': 'host',
        'db': 'db',
        'command': 'command',
        'sql_key': 'sql_key',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, filter=None, slow_process_threshold=None, user=None, host=None, db=None, command=None, sql_key=None, sort_key=None, sort_dir=None):
        r"""RealtimeSessionRequest

        The model defined in huaweicloud sdk

        :param filter: **参数解释**：  需要收集的实时会话类型。  **约束限制**：  不涉及。  **取值范围**：  - slow：慢会话。 - active：活跃会话。 - total：会话总数。 - long：长事务会话。  **默认取值**：  total。
        :type filter: str
        :param slow_process_threshold: **参数解释**：  慢会话阈值，单位是秒。  **约束限制**：  不涉及。  **取值范围**：  1-86400。  **默认取值**：  10。
        :type slow_process_threshold: int
        :param user: **参数解释**：  实时会话的用户。 获取方法请参见[查询数据库用户](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlDatabaseUser.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type user: str
        :param host: **参数解释**：  实时会话的主机。 获取方法请参见[查询数据库用户](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlDatabaseUser.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type host: str
        :param db: **参数解释**：  实时会话的数据库。 获取方法请参见[查询数据库用户](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlDatabaseUser.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type db: str
        :param command: **参数解释**：  实时会话的命令类型。  **约束限制**：  不涉及。  **取值范围**：  - Sleep：空闲连接，无任何操作。 - Query：正在执行查询。 - Connect：建立连接。 - Init DB：切换数据库。 - Field List：获取表字段列表。 - Processlist：查看会话列表。  **默认取值**：  不涉及。
        :type command: str
        :param sql_key: **参数解释**：  实时会话的SQL语句。 您可以通过登录管理控制台，选择智能DBA助手下的实时会话，在会话列表中获取。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type sql_key: str
        :param sort_key: **参数解释**：  实时会话的排序列。  **约束限制**：  不涉及。  **取值范围**：  - id：会话ID。 - state_duration：状态持续时间。 - trx_executed_time：事务持续时间。 - trx_id：事务ID。 - trx_lock_duration：事务锁等待时长。 - trx_lock_rows：事务锁定行数。 - trx_lock_tables：事务锁定表数量。 - trx_update_rows：事务更新行数。  **默认取值**：  id。
        :type sort_key: str
        :param sort_dir: **参数解释**：  实时会话的排序方向。  **约束限制**：  不涉及。  **取值范围**：  - desc：降序排列。 - asc：升序排列。  **默认取值**：  asc。
        :type sort_dir: str
        """
        
        

        self._filter = None
        self._slow_process_threshold = None
        self._user = None
        self._host = None
        self._db = None
        self._command = None
        self._sql_key = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if slow_process_threshold is not None:
            self.slow_process_threshold = slow_process_threshold
        if user is not None:
            self.user = user
        if host is not None:
            self.host = host
        if db is not None:
            self.db = db
        if command is not None:
            self.command = command
        if sql_key is not None:
            self.sql_key = sql_key
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def filter(self):
        r"""Gets the filter of this RealtimeSessionRequest.

        **参数解释**：  需要收集的实时会话类型。  **约束限制**：  不涉及。  **取值范围**：  - slow：慢会话。 - active：活跃会话。 - total：会话总数。 - long：长事务会话。  **默认取值**：  total。

        :return: The filter of this RealtimeSessionRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this RealtimeSessionRequest.

        **参数解释**：  需要收集的实时会话类型。  **约束限制**：  不涉及。  **取值范围**：  - slow：慢会话。 - active：活跃会话。 - total：会话总数。 - long：长事务会话。  **默认取值**：  total。

        :param filter: The filter of this RealtimeSessionRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def slow_process_threshold(self):
        r"""Gets the slow_process_threshold of this RealtimeSessionRequest.

        **参数解释**：  慢会话阈值，单位是秒。  **约束限制**：  不涉及。  **取值范围**：  1-86400。  **默认取值**：  10。

        :return: The slow_process_threshold of this RealtimeSessionRequest.
        :rtype: int
        """
        return self._slow_process_threshold

    @slow_process_threshold.setter
    def slow_process_threshold(self, slow_process_threshold):
        r"""Sets the slow_process_threshold of this RealtimeSessionRequest.

        **参数解释**：  慢会话阈值，单位是秒。  **约束限制**：  不涉及。  **取值范围**：  1-86400。  **默认取值**：  10。

        :param slow_process_threshold: The slow_process_threshold of this RealtimeSessionRequest.
        :type slow_process_threshold: int
        """
        self._slow_process_threshold = slow_process_threshold

    @property
    def user(self):
        r"""Gets the user of this RealtimeSessionRequest.

        **参数解释**：  实时会话的用户。 获取方法请参见[查询数据库用户](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlDatabaseUser.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The user of this RealtimeSessionRequest.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this RealtimeSessionRequest.

        **参数解释**：  实时会话的用户。 获取方法请参见[查询数据库用户](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlDatabaseUser.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param user: The user of this RealtimeSessionRequest.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this RealtimeSessionRequest.

        **参数解释**：  实时会话的主机。 获取方法请参见[查询数据库用户](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlDatabaseUser.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The host of this RealtimeSessionRequest.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this RealtimeSessionRequest.

        **参数解释**：  实时会话的主机。 获取方法请参见[查询数据库用户](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlDatabaseUser.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param host: The host of this RealtimeSessionRequest.
        :type host: str
        """
        self._host = host

    @property
    def db(self):
        r"""Gets the db of this RealtimeSessionRequest.

        **参数解释**：  实时会话的数据库。 获取方法请参见[查询数据库用户](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlDatabaseUser.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The db of this RealtimeSessionRequest.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this RealtimeSessionRequest.

        **参数解释**：  实时会话的数据库。 获取方法请参见[查询数据库用户](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlDatabaseUser.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param db: The db of this RealtimeSessionRequest.
        :type db: str
        """
        self._db = db

    @property
    def command(self):
        r"""Gets the command of this RealtimeSessionRequest.

        **参数解释**：  实时会话的命令类型。  **约束限制**：  不涉及。  **取值范围**：  - Sleep：空闲连接，无任何操作。 - Query：正在执行查询。 - Connect：建立连接。 - Init DB：切换数据库。 - Field List：获取表字段列表。 - Processlist：查看会话列表。  **默认取值**：  不涉及。

        :return: The command of this RealtimeSessionRequest.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this RealtimeSessionRequest.

        **参数解释**：  实时会话的命令类型。  **约束限制**：  不涉及。  **取值范围**：  - Sleep：空闲连接，无任何操作。 - Query：正在执行查询。 - Connect：建立连接。 - Init DB：切换数据库。 - Field List：获取表字段列表。 - Processlist：查看会话列表。  **默认取值**：  不涉及。

        :param command: The command of this RealtimeSessionRequest.
        :type command: str
        """
        self._command = command

    @property
    def sql_key(self):
        r"""Gets the sql_key of this RealtimeSessionRequest.

        **参数解释**：  实时会话的SQL语句。 您可以通过登录管理控制台，选择智能DBA助手下的实时会话，在会话列表中获取。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The sql_key of this RealtimeSessionRequest.
        :rtype: str
        """
        return self._sql_key

    @sql_key.setter
    def sql_key(self, sql_key):
        r"""Sets the sql_key of this RealtimeSessionRequest.

        **参数解释**：  实时会话的SQL语句。 您可以通过登录管理控制台，选择智能DBA助手下的实时会话，在会话列表中获取。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param sql_key: The sql_key of this RealtimeSessionRequest.
        :type sql_key: str
        """
        self._sql_key = sql_key

    @property
    def sort_key(self):
        r"""Gets the sort_key of this RealtimeSessionRequest.

        **参数解释**：  实时会话的排序列。  **约束限制**：  不涉及。  **取值范围**：  - id：会话ID。 - state_duration：状态持续时间。 - trx_executed_time：事务持续时间。 - trx_id：事务ID。 - trx_lock_duration：事务锁等待时长。 - trx_lock_rows：事务锁定行数。 - trx_lock_tables：事务锁定表数量。 - trx_update_rows：事务更新行数。  **默认取值**：  id。

        :return: The sort_key of this RealtimeSessionRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this RealtimeSessionRequest.

        **参数解释**：  实时会话的排序列。  **约束限制**：  不涉及。  **取值范围**：  - id：会话ID。 - state_duration：状态持续时间。 - trx_executed_time：事务持续时间。 - trx_id：事务ID。 - trx_lock_duration：事务锁等待时长。 - trx_lock_rows：事务锁定行数。 - trx_lock_tables：事务锁定表数量。 - trx_update_rows：事务更新行数。  **默认取值**：  id。

        :param sort_key: The sort_key of this RealtimeSessionRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this RealtimeSessionRequest.

        **参数解释**：  实时会话的排序方向。  **约束限制**：  不涉及。  **取值范围**：  - desc：降序排列。 - asc：升序排列。  **默认取值**：  asc。

        :return: The sort_dir of this RealtimeSessionRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this RealtimeSessionRequest.

        **参数解释**：  实时会话的排序方向。  **约束限制**：  不涉及。  **取值范围**：  - desc：降序排列。 - asc：升序排列。  **默认取值**：  asc。

        :param sort_dir: The sort_dir of this RealtimeSessionRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, RealtimeSessionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
