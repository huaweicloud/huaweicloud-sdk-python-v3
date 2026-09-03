# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatementRecord:

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
        'workspace_id': 'str',
        'endpoint_id': 'str',
        'session_id': 'str',
        'database_name': 'str',
        'statement_content': 'str',
        'dpu_duration': 'str',
        'duration': 'str',
        'dpu_cost': 'str',
        'status': 'str',
        'user_name': 'str',
        'create_time': 'datetime',
        'start_time': 'datetime',
        'finish_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'workspace_id': 'workspace_id',
        'endpoint_id': 'endpoint_id',
        'session_id': 'session_id',
        'database_name': 'database_name',
        'statement_content': 'statement_content',
        'dpu_duration': 'dpu_duration',
        'duration': 'duration',
        'dpu_cost': 'dpu_cost',
        'status': 'status',
        'user_name': 'user_name',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'finish_time': 'finish_time'
    }

    def __init__(self, id=None, workspace_id=None, endpoint_id=None, session_id=None, database_name=None, statement_content=None, dpu_duration=None, duration=None, dpu_cost=None, status=None, user_name=None, create_time=None, start_time=None, finish_time=None):
        r"""StatementRecord

        The model defined in huaweicloud sdk

        :param id: **参数解释**：Sql执行StatementID。 **取值范围**：不涉及。
        :type id: str
        :param workspace_id: **参数解释**：工作空间ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。
        :type workspace_id: str
        :param endpoint_id: **参数解释**：端点ID。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、连字符。
        :type endpoint_id: str
        :param session_id: **参数解释**：Session的ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。
        :type session_id: str
        :param database_name: **参数解释**：数据库名称。 **取值范围**：长度为1~256个字符，支持大小写英文字母、数字、下划线。
        :type database_name: str
        :param statement_content: **参数解释**：sql脚本内容。 **取值范围**：长度为1~256个字符，支持大小写英文字母、数字、下划线。
        :type statement_content: str
        :param dpu_duration: **参数解释**：dpu时。 **取值范围**：不涉及。
        :type dpu_duration: str
        :param duration: **参数解释**：执行时长。 **取值范围**：不涉及。
        :type duration: str
        :param dpu_cost: **参数解释**：费用。 **取值范围**：不涉及。
        :type dpu_cost: str
        :param status: **参数解释**：Sql执行状态。 **取值范围**：   - CANCELED：取消。   - FAILED：失败。   - SUCCESSFUL：成功。   - RUNNING：运行中。   - SUBMITTED：提交。   - ERROR：错误。
        :type status: str
        :param user_name: **参数解释**：用户名称。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、下划线。
        :type user_name: str
        :param create_time: **参数解释**：sql创建时间，用于记录sql语句创建时间。 **取值范围**：unix时间戳，单位为毫秒。
        :type create_time: datetime
        :param start_time: **参数解释**：sql执行开始时间，时间戳，单位：毫秒。 **取值范围**：不涉及。
        :type start_time: datetime
        :param finish_time: **参数解释**：sql执行结束时间，时间戳，单位：毫秒。 **取值范围**：不涉及。
        :type finish_time: datetime
        """
        
        

        self._id = None
        self._workspace_id = None
        self._endpoint_id = None
        self._session_id = None
        self._database_name = None
        self._statement_content = None
        self._dpu_duration = None
        self._duration = None
        self._dpu_cost = None
        self._status = None
        self._user_name = None
        self._create_time = None
        self._start_time = None
        self._finish_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if session_id is not None:
            self.session_id = session_id
        if database_name is not None:
            self.database_name = database_name
        if statement_content is not None:
            self.statement_content = statement_content
        if dpu_duration is not None:
            self.dpu_duration = dpu_duration
        if duration is not None:
            self.duration = duration
        if dpu_cost is not None:
            self.dpu_cost = dpu_cost
        if status is not None:
            self.status = status
        if user_name is not None:
            self.user_name = user_name
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if finish_time is not None:
            self.finish_time = finish_time

    @property
    def id(self):
        r"""Gets the id of this StatementRecord.

        **参数解释**：Sql执行StatementID。 **取值范围**：不涉及。

        :return: The id of this StatementRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StatementRecord.

        **参数解释**：Sql执行StatementID。 **取值范围**：不涉及。

        :param id: The id of this StatementRecord.
        :type id: str
        """
        self._id = id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this StatementRecord.

        **参数解释**：工作空间ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :return: The workspace_id of this StatementRecord.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this StatementRecord.

        **参数解释**：工作空间ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :param workspace_id: The workspace_id of this StatementRecord.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this StatementRecord.

        **参数解释**：端点ID。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、连字符。

        :return: The endpoint_id of this StatementRecord.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this StatementRecord.

        **参数解释**：端点ID。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、连字符。

        :param endpoint_id: The endpoint_id of this StatementRecord.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def session_id(self):
        r"""Gets the session_id of this StatementRecord.

        **参数解释**：Session的ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :return: The session_id of this StatementRecord.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this StatementRecord.

        **参数解释**：Session的ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :param session_id: The session_id of this StatementRecord.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def database_name(self):
        r"""Gets the database_name of this StatementRecord.

        **参数解释**：数据库名称。 **取值范围**：长度为1~256个字符，支持大小写英文字母、数字、下划线。

        :return: The database_name of this StatementRecord.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this StatementRecord.

        **参数解释**：数据库名称。 **取值范围**：长度为1~256个字符，支持大小写英文字母、数字、下划线。

        :param database_name: The database_name of this StatementRecord.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def statement_content(self):
        r"""Gets the statement_content of this StatementRecord.

        **参数解释**：sql脚本内容。 **取值范围**：长度为1~256个字符，支持大小写英文字母、数字、下划线。

        :return: The statement_content of this StatementRecord.
        :rtype: str
        """
        return self._statement_content

    @statement_content.setter
    def statement_content(self, statement_content):
        r"""Sets the statement_content of this StatementRecord.

        **参数解释**：sql脚本内容。 **取值范围**：长度为1~256个字符，支持大小写英文字母、数字、下划线。

        :param statement_content: The statement_content of this StatementRecord.
        :type statement_content: str
        """
        self._statement_content = statement_content

    @property
    def dpu_duration(self):
        r"""Gets the dpu_duration of this StatementRecord.

        **参数解释**：dpu时。 **取值范围**：不涉及。

        :return: The dpu_duration of this StatementRecord.
        :rtype: str
        """
        return self._dpu_duration

    @dpu_duration.setter
    def dpu_duration(self, dpu_duration):
        r"""Sets the dpu_duration of this StatementRecord.

        **参数解释**：dpu时。 **取值范围**：不涉及。

        :param dpu_duration: The dpu_duration of this StatementRecord.
        :type dpu_duration: str
        """
        self._dpu_duration = dpu_duration

    @property
    def duration(self):
        r"""Gets the duration of this StatementRecord.

        **参数解释**：执行时长。 **取值范围**：不涉及。

        :return: The duration of this StatementRecord.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this StatementRecord.

        **参数解释**：执行时长。 **取值范围**：不涉及。

        :param duration: The duration of this StatementRecord.
        :type duration: str
        """
        self._duration = duration

    @property
    def dpu_cost(self):
        r"""Gets the dpu_cost of this StatementRecord.

        **参数解释**：费用。 **取值范围**：不涉及。

        :return: The dpu_cost of this StatementRecord.
        :rtype: str
        """
        return self._dpu_cost

    @dpu_cost.setter
    def dpu_cost(self, dpu_cost):
        r"""Sets the dpu_cost of this StatementRecord.

        **参数解释**：费用。 **取值范围**：不涉及。

        :param dpu_cost: The dpu_cost of this StatementRecord.
        :type dpu_cost: str
        """
        self._dpu_cost = dpu_cost

    @property
    def status(self):
        r"""Gets the status of this StatementRecord.

        **参数解释**：Sql执行状态。 **取值范围**：   - CANCELED：取消。   - FAILED：失败。   - SUCCESSFUL：成功。   - RUNNING：运行中。   - SUBMITTED：提交。   - ERROR：错误。

        :return: The status of this StatementRecord.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StatementRecord.

        **参数解释**：Sql执行状态。 **取值范围**：   - CANCELED：取消。   - FAILED：失败。   - SUCCESSFUL：成功。   - RUNNING：运行中。   - SUBMITTED：提交。   - ERROR：错误。

        :param status: The status of this StatementRecord.
        :type status: str
        """
        self._status = status

    @property
    def user_name(self):
        r"""Gets the user_name of this StatementRecord.

        **参数解释**：用户名称。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、下划线。

        :return: The user_name of this StatementRecord.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this StatementRecord.

        **参数解释**：用户名称。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、下划线。

        :param user_name: The user_name of this StatementRecord.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def create_time(self):
        r"""Gets the create_time of this StatementRecord.

        **参数解释**：sql创建时间，用于记录sql语句创建时间。 **取值范围**：unix时间戳，单位为毫秒。

        :return: The create_time of this StatementRecord.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this StatementRecord.

        **参数解释**：sql创建时间，用于记录sql语句创建时间。 **取值范围**：unix时间戳，单位为毫秒。

        :param create_time: The create_time of this StatementRecord.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def start_time(self):
        r"""Gets the start_time of this StatementRecord.

        **参数解释**：sql执行开始时间，时间戳，单位：毫秒。 **取值范围**：不涉及。

        :return: The start_time of this StatementRecord.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this StatementRecord.

        **参数解释**：sql执行开始时间，时间戳，单位：毫秒。 **取值范围**：不涉及。

        :param start_time: The start_time of this StatementRecord.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this StatementRecord.

        **参数解释**：sql执行结束时间，时间戳，单位：毫秒。 **取值范围**：不涉及。

        :return: The finish_time of this StatementRecord.
        :rtype: datetime
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this StatementRecord.

        **参数解释**：sql执行结束时间，时间戳，单位：毫秒。 **取值范围**：不涉及。

        :param finish_time: The finish_time of this StatementRecord.
        :type finish_time: datetime
        """
        self._finish_time = finish_time

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
        if not isinstance(other, StatementRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
