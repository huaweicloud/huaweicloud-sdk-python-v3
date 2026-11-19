# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlSessionInfo:

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
        'status': 'SqlSessionStatusAdmin',
        'create_time': 'datetime',
        'error': 'ErrorMessage',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'wait_timeout': 'int',
        'max_retry_times': 'int',
        'priority': 'int',
        'endpoint_info': 'object'
    }

    attribute_map = {
        'session_id': 'session_id',
        'status': 'status',
        'create_time': 'create_time',
        'error': 'error',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'wait_timeout': 'wait_timeout',
        'max_retry_times': 'max_retry_times',
        'priority': 'priority',
        'endpoint_info': 'endpoint_info'
    }

    def __init__(self, session_id=None, status=None, create_time=None, error=None, start_time=None, end_time=None, wait_timeout=None, max_retry_times=None, priority=None, endpoint_info=None):
        r"""SqlSessionInfo

        The model defined in huaweicloud sdk

        :param session_id: **参数解释**：Session的ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。
        :type session_id: str
        :param status: 
        :type status: :class:`huaweicloudsdkaidatalake.v2.SqlSessionStatusAdmin`
        :param create_time: **参数解释**：session创建时间。 **取值范围**：不涉及。
        :type create_time: datetime
        :param error: 
        :type error: :class:`huaweicloudsdkaidatalake.v2.ErrorMessage`
        :param start_time: **参数解释**：开始时间。 **取值范围**：不涉及。
        :type start_time: datetime
        :param end_time: **参数解释**：结束时间。 **取值范围**：不涉及。
        :type end_time: datetime
        :param wait_timeout: **参数解释**：会话排队超时时间（秒）。 **取值范围**：不涉及。
        :type wait_timeout: int
        :param max_retry_times: **参数解释**：异步创建会话最大重试次数。 **取值范围**：不涉及。
        :type max_retry_times: int
        :param priority: **参数解释**：会话优先级。 **取值范围**：不涉及。
        :type priority: int
        :param endpoint_info: **参数解释**：端点信息。
        :type endpoint_info: :class:`huaweicloudsdkaidatalake.v2.object`
        """
        
        

        self._session_id = None
        self._status = None
        self._create_time = None
        self._error = None
        self._start_time = None
        self._end_time = None
        self._wait_timeout = None
        self._max_retry_times = None
        self._priority = None
        self._endpoint_info = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if error is not None:
            self.error = error
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if wait_timeout is not None:
            self.wait_timeout = wait_timeout
        if max_retry_times is not None:
            self.max_retry_times = max_retry_times
        if priority is not None:
            self.priority = priority
        if endpoint_info is not None:
            self.endpoint_info = endpoint_info

    @property
    def session_id(self):
        r"""Gets the session_id of this SqlSessionInfo.

        **参数解释**：Session的ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :return: The session_id of this SqlSessionInfo.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this SqlSessionInfo.

        **参数解释**：Session的ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :param session_id: The session_id of this SqlSessionInfo.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def status(self):
        r"""Gets the status of this SqlSessionInfo.

        :return: The status of this SqlSessionInfo.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.SqlSessionStatusAdmin`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SqlSessionInfo.

        :param status: The status of this SqlSessionInfo.
        :type status: :class:`huaweicloudsdkaidatalake.v2.SqlSessionStatusAdmin`
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this SqlSessionInfo.

        **参数解释**：session创建时间。 **取值范围**：不涉及。

        :return: The create_time of this SqlSessionInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SqlSessionInfo.

        **参数解释**：session创建时间。 **取值范围**：不涉及。

        :param create_time: The create_time of this SqlSessionInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def error(self):
        r"""Gets the error of this SqlSessionInfo.

        :return: The error of this SqlSessionInfo.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ErrorMessage`
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this SqlSessionInfo.

        :param error: The error of this SqlSessionInfo.
        :type error: :class:`huaweicloudsdkaidatalake.v2.ErrorMessage`
        """
        self._error = error

    @property
    def start_time(self):
        r"""Gets the start_time of this SqlSessionInfo.

        **参数解释**：开始时间。 **取值范围**：不涉及。

        :return: The start_time of this SqlSessionInfo.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SqlSessionInfo.

        **参数解释**：开始时间。 **取值范围**：不涉及。

        :param start_time: The start_time of this SqlSessionInfo.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this SqlSessionInfo.

        **参数解释**：结束时间。 **取值范围**：不涉及。

        :return: The end_time of this SqlSessionInfo.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SqlSessionInfo.

        **参数解释**：结束时间。 **取值范围**：不涉及。

        :param end_time: The end_time of this SqlSessionInfo.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def wait_timeout(self):
        r"""Gets the wait_timeout of this SqlSessionInfo.

        **参数解释**：会话排队超时时间（秒）。 **取值范围**：不涉及。

        :return: The wait_timeout of this SqlSessionInfo.
        :rtype: int
        """
        return self._wait_timeout

    @wait_timeout.setter
    def wait_timeout(self, wait_timeout):
        r"""Sets the wait_timeout of this SqlSessionInfo.

        **参数解释**：会话排队超时时间（秒）。 **取值范围**：不涉及。

        :param wait_timeout: The wait_timeout of this SqlSessionInfo.
        :type wait_timeout: int
        """
        self._wait_timeout = wait_timeout

    @property
    def max_retry_times(self):
        r"""Gets the max_retry_times of this SqlSessionInfo.

        **参数解释**：异步创建会话最大重试次数。 **取值范围**：不涉及。

        :return: The max_retry_times of this SqlSessionInfo.
        :rtype: int
        """
        return self._max_retry_times

    @max_retry_times.setter
    def max_retry_times(self, max_retry_times):
        r"""Sets the max_retry_times of this SqlSessionInfo.

        **参数解释**：异步创建会话最大重试次数。 **取值范围**：不涉及。

        :param max_retry_times: The max_retry_times of this SqlSessionInfo.
        :type max_retry_times: int
        """
        self._max_retry_times = max_retry_times

    @property
    def priority(self):
        r"""Gets the priority of this SqlSessionInfo.

        **参数解释**：会话优先级。 **取值范围**：不涉及。

        :return: The priority of this SqlSessionInfo.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this SqlSessionInfo.

        **参数解释**：会话优先级。 **取值范围**：不涉及。

        :param priority: The priority of this SqlSessionInfo.
        :type priority: int
        """
        self._priority = priority

    @property
    def endpoint_info(self):
        r"""Gets the endpoint_info of this SqlSessionInfo.

        **参数解释**：端点信息。

        :return: The endpoint_info of this SqlSessionInfo.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.object`
        """
        return self._endpoint_info

    @endpoint_info.setter
    def endpoint_info(self, endpoint_info):
        r"""Sets the endpoint_info of this SqlSessionInfo.

        **参数解释**：端点信息。

        :param endpoint_info: The endpoint_info of this SqlSessionInfo.
        :type endpoint_info: :class:`huaweicloudsdkaidatalake.v2.object`
        """
        self._endpoint_info = endpoint_info

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
        if not isinstance(other, SqlSessionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
