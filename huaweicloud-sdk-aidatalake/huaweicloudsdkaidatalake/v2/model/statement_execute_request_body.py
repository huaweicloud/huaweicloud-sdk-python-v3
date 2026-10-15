# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatementExecuteRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_id': 'str',
        'statement': 'str',
        'limit': 'int',
        'bindings': 'list[list[str]]',
        'is_sync': 'bool',
        'is_maintain_statement': 'bool',
        'resultset_fetch_mode': 'str',
        'wait_timeout': 'int',
        'max_retry_times': 'int',
        'statement_type': 'str',
        'statement_name': 'str'
    }

    attribute_map = {
        'session_id': 'session_id',
        'statement': 'statement',
        'limit': 'limit',
        'bindings': 'bindings',
        'is_sync': 'is_sync',
        'is_maintain_statement': 'is_maintain_statement',
        'resultset_fetch_mode': 'resultset_fetch_mode',
        'wait_timeout': 'wait_timeout',
        'max_retry_times': 'max_retry_times',
        'statement_type': 'statement_type',
        'statement_name': 'statement_name'
    }

    def __init__(self, session_id=None, statement=None, limit=None, bindings=None, is_sync=None, is_maintain_statement=None, resultset_fetch_mode=None, wait_timeout=None, max_retry_times=None, statement_type=None, statement_name=None):
        r"""StatementExecuteRequestBody

        The model defined in huaweicloud sdk

        :param session_id: **参数解释**：Session的ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。
        :type session_id: str
        :param statement: **参数解释**：SQL statement信息。 **约束限制**：不涉及。 **取值范围**：长度为1~10000000个字符。 **默认取值**：不涉及。
        :type statement: str
        :param limit: **参数解释**：返回结果集的最大行数限制。 **约束限制**：不涉及。 **取值范围**：1~2147483647，单位：行。 **默认取值**：不涉及。
        :type limit: int
        :param bindings: **参数解释**：SQL语句的参数绑定列表，用于绑定变量传参。外层数组为绑定集合（实际使用首个元素 bindings[0]），内层数组为单条SQL的参数值列表，每个字符串元素为单个参数值。 **约束限制**：   - 外层数组元素个数：0~1。   - 内层数组元素个数：0~200。   - 每个参数值字符串长度：0~500个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type bindings: list[list[str]]
        :param is_sync: **参数解释**：同步执行或异步执行。 **约束限制**：不涉及。 **取值范围**：   - true：同步。   - false：异步。 **默认取值**：true（未传时默认同步执行）。
        :type is_sync: bool
        :param is_maintain_statement: **参数解释**：是否来自运维通道。 **约束限制**：不涉及。 **取值范围**：  - true：运维通道语句。  - false：不是运维通道语句。 **默认取值**：false
        :type is_maintain_statement: bool
        :param resultset_fetch_mode: **参数解释**：获取结果集的方式。 **约束限制**：不涉及。 **取值范围**：   - DEFAULT：直接返回结果集。   - READ_OBS：返回结果集在桶上的路径，而不是直接返回结果集。 **默认取值**：DEFAULT。
        :type resultset_fetch_mode: str
        :param wait_timeout: **参数解释**：SQL排队等待时间，单位：秒。 **约束限制**：不涉及。 **取值范围**：300~86400。 **默认取值**：不涉及。
        :type wait_timeout: int
        :param max_retry_times: **参数解释**：资源不足时重试次数。 **约束限制**：不涉及。 **取值范围**：1~6000。 **默认取值**：不涉及。
        :type max_retry_times: int
        :param statement_type: **参数解释**：作业类型。 **约束限制**：不涉及。 **取值范围**：   - SQL：SQL查询。   - JOB：作业。 **默认取值**：SQL。
        :type statement_type: str
        :param statement_name: **参数解释**：作业名称。 **约束限制**：长度不超过64个字符，仅允许字母、数字、中文、下划线和连字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type statement_name: str
        """
        
        

        self._session_id = None
        self._statement = None
        self._limit = None
        self._bindings = None
        self._is_sync = None
        self._is_maintain_statement = None
        self._resultset_fetch_mode = None
        self._wait_timeout = None
        self._max_retry_times = None
        self._statement_type = None
        self._statement_name = None
        self.discriminator = None

        self.session_id = session_id
        self.statement = statement
        if limit is not None:
            self.limit = limit
        if bindings is not None:
            self.bindings = bindings
        if is_sync is not None:
            self.is_sync = is_sync
        if is_maintain_statement is not None:
            self.is_maintain_statement = is_maintain_statement
        if resultset_fetch_mode is not None:
            self.resultset_fetch_mode = resultset_fetch_mode
        if wait_timeout is not None:
            self.wait_timeout = wait_timeout
        if max_retry_times is not None:
            self.max_retry_times = max_retry_times
        if statement_type is not None:
            self.statement_type = statement_type
        if statement_name is not None:
            self.statement_name = statement_name

    @property
    def session_id(self):
        r"""Gets the session_id of this StatementExecuteRequestBody.

        **参数解释**：Session的ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :return: The session_id of this StatementExecuteRequestBody.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this StatementExecuteRequestBody.

        **参数解释**：Session的ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :param session_id: The session_id of this StatementExecuteRequestBody.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def statement(self):
        r"""Gets the statement of this StatementExecuteRequestBody.

        **参数解释**：SQL statement信息。 **约束限制**：不涉及。 **取值范围**：长度为1~10000000个字符。 **默认取值**：不涉及。

        :return: The statement of this StatementExecuteRequestBody.
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        r"""Sets the statement of this StatementExecuteRequestBody.

        **参数解释**：SQL statement信息。 **约束限制**：不涉及。 **取值范围**：长度为1~10000000个字符。 **默认取值**：不涉及。

        :param statement: The statement of this StatementExecuteRequestBody.
        :type statement: str
        """
        self._statement = statement

    @property
    def limit(self):
        r"""Gets the limit of this StatementExecuteRequestBody.

        **参数解释**：返回结果集的最大行数限制。 **约束限制**：不涉及。 **取值范围**：1~2147483647，单位：行。 **默认取值**：不涉及。

        :return: The limit of this StatementExecuteRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this StatementExecuteRequestBody.

        **参数解释**：返回结果集的最大行数限制。 **约束限制**：不涉及。 **取值范围**：1~2147483647，单位：行。 **默认取值**：不涉及。

        :param limit: The limit of this StatementExecuteRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def bindings(self):
        r"""Gets the bindings of this StatementExecuteRequestBody.

        **参数解释**：SQL语句的参数绑定列表，用于绑定变量传参。外层数组为绑定集合（实际使用首个元素 bindings[0]），内层数组为单条SQL的参数值列表，每个字符串元素为单个参数值。 **约束限制**：   - 外层数组元素个数：0~1。   - 内层数组元素个数：0~200。   - 每个参数值字符串长度：0~500个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The bindings of this StatementExecuteRequestBody.
        :rtype: list[list[str]]
        """
        return self._bindings

    @bindings.setter
    def bindings(self, bindings):
        r"""Sets the bindings of this StatementExecuteRequestBody.

        **参数解释**：SQL语句的参数绑定列表，用于绑定变量传参。外层数组为绑定集合（实际使用首个元素 bindings[0]），内层数组为单条SQL的参数值列表，每个字符串元素为单个参数值。 **约束限制**：   - 外层数组元素个数：0~1。   - 内层数组元素个数：0~200。   - 每个参数值字符串长度：0~500个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param bindings: The bindings of this StatementExecuteRequestBody.
        :type bindings: list[list[str]]
        """
        self._bindings = bindings

    @property
    def is_sync(self):
        r"""Gets the is_sync of this StatementExecuteRequestBody.

        **参数解释**：同步执行或异步执行。 **约束限制**：不涉及。 **取值范围**：   - true：同步。   - false：异步。 **默认取值**：true（未传时默认同步执行）。

        :return: The is_sync of this StatementExecuteRequestBody.
        :rtype: bool
        """
        return self._is_sync

    @is_sync.setter
    def is_sync(self, is_sync):
        r"""Sets the is_sync of this StatementExecuteRequestBody.

        **参数解释**：同步执行或异步执行。 **约束限制**：不涉及。 **取值范围**：   - true：同步。   - false：异步。 **默认取值**：true（未传时默认同步执行）。

        :param is_sync: The is_sync of this StatementExecuteRequestBody.
        :type is_sync: bool
        """
        self._is_sync = is_sync

    @property
    def is_maintain_statement(self):
        r"""Gets the is_maintain_statement of this StatementExecuteRequestBody.

        **参数解释**：是否来自运维通道。 **约束限制**：不涉及。 **取值范围**：  - true：运维通道语句。  - false：不是运维通道语句。 **默认取值**：false

        :return: The is_maintain_statement of this StatementExecuteRequestBody.
        :rtype: bool
        """
        return self._is_maintain_statement

    @is_maintain_statement.setter
    def is_maintain_statement(self, is_maintain_statement):
        r"""Sets the is_maintain_statement of this StatementExecuteRequestBody.

        **参数解释**：是否来自运维通道。 **约束限制**：不涉及。 **取值范围**：  - true：运维通道语句。  - false：不是运维通道语句。 **默认取值**：false

        :param is_maintain_statement: The is_maintain_statement of this StatementExecuteRequestBody.
        :type is_maintain_statement: bool
        """
        self._is_maintain_statement = is_maintain_statement

    @property
    def resultset_fetch_mode(self):
        r"""Gets the resultset_fetch_mode of this StatementExecuteRequestBody.

        **参数解释**：获取结果集的方式。 **约束限制**：不涉及。 **取值范围**：   - DEFAULT：直接返回结果集。   - READ_OBS：返回结果集在桶上的路径，而不是直接返回结果集。 **默认取值**：DEFAULT。

        :return: The resultset_fetch_mode of this StatementExecuteRequestBody.
        :rtype: str
        """
        return self._resultset_fetch_mode

    @resultset_fetch_mode.setter
    def resultset_fetch_mode(self, resultset_fetch_mode):
        r"""Sets the resultset_fetch_mode of this StatementExecuteRequestBody.

        **参数解释**：获取结果集的方式。 **约束限制**：不涉及。 **取值范围**：   - DEFAULT：直接返回结果集。   - READ_OBS：返回结果集在桶上的路径，而不是直接返回结果集。 **默认取值**：DEFAULT。

        :param resultset_fetch_mode: The resultset_fetch_mode of this StatementExecuteRequestBody.
        :type resultset_fetch_mode: str
        """
        self._resultset_fetch_mode = resultset_fetch_mode

    @property
    def wait_timeout(self):
        r"""Gets the wait_timeout of this StatementExecuteRequestBody.

        **参数解释**：SQL排队等待时间，单位：秒。 **约束限制**：不涉及。 **取值范围**：300~86400。 **默认取值**：不涉及。

        :return: The wait_timeout of this StatementExecuteRequestBody.
        :rtype: int
        """
        return self._wait_timeout

    @wait_timeout.setter
    def wait_timeout(self, wait_timeout):
        r"""Sets the wait_timeout of this StatementExecuteRequestBody.

        **参数解释**：SQL排队等待时间，单位：秒。 **约束限制**：不涉及。 **取值范围**：300~86400。 **默认取值**：不涉及。

        :param wait_timeout: The wait_timeout of this StatementExecuteRequestBody.
        :type wait_timeout: int
        """
        self._wait_timeout = wait_timeout

    @property
    def max_retry_times(self):
        r"""Gets the max_retry_times of this StatementExecuteRequestBody.

        **参数解释**：资源不足时重试次数。 **约束限制**：不涉及。 **取值范围**：1~6000。 **默认取值**：不涉及。

        :return: The max_retry_times of this StatementExecuteRequestBody.
        :rtype: int
        """
        return self._max_retry_times

    @max_retry_times.setter
    def max_retry_times(self, max_retry_times):
        r"""Sets the max_retry_times of this StatementExecuteRequestBody.

        **参数解释**：资源不足时重试次数。 **约束限制**：不涉及。 **取值范围**：1~6000。 **默认取值**：不涉及。

        :param max_retry_times: The max_retry_times of this StatementExecuteRequestBody.
        :type max_retry_times: int
        """
        self._max_retry_times = max_retry_times

    @property
    def statement_type(self):
        r"""Gets the statement_type of this StatementExecuteRequestBody.

        **参数解释**：作业类型。 **约束限制**：不涉及。 **取值范围**：   - SQL：SQL查询。   - JOB：作业。 **默认取值**：SQL。

        :return: The statement_type of this StatementExecuteRequestBody.
        :rtype: str
        """
        return self._statement_type

    @statement_type.setter
    def statement_type(self, statement_type):
        r"""Sets the statement_type of this StatementExecuteRequestBody.

        **参数解释**：作业类型。 **约束限制**：不涉及。 **取值范围**：   - SQL：SQL查询。   - JOB：作业。 **默认取值**：SQL。

        :param statement_type: The statement_type of this StatementExecuteRequestBody.
        :type statement_type: str
        """
        self._statement_type = statement_type

    @property
    def statement_name(self):
        r"""Gets the statement_name of this StatementExecuteRequestBody.

        **参数解释**：作业名称。 **约束限制**：长度不超过64个字符，仅允许字母、数字、中文、下划线和连字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The statement_name of this StatementExecuteRequestBody.
        :rtype: str
        """
        return self._statement_name

    @statement_name.setter
    def statement_name(self, statement_name):
        r"""Sets the statement_name of this StatementExecuteRequestBody.

        **参数解释**：作业名称。 **约束限制**：长度不超过64个字符，仅允许字母、数字、中文、下划线和连字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param statement_name: The statement_name of this StatementExecuteRequestBody.
        :type statement_name: str
        """
        self._statement_name = statement_name

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
        if not isinstance(other, StatementExecuteRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
