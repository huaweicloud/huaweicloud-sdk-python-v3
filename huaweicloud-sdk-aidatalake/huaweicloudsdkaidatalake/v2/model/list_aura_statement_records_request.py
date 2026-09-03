# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuraStatementRecordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'endpoint_id': 'str',
        'endpoint_name': 'str',
        'session_id': 'str',
        'statement_id': 'str',
        'source': 'int',
        'status': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'endpoint_id': 'endpoint_id',
        'endpoint_name': 'endpoint_name',
        'session_id': 'session_id',
        'statement_id': 'statement_id',
        'source': 'source',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, workspace_id=None, endpoint_id=None, endpoint_name=None, session_id=None, statement_id=None, source=None, status=None, start_time=None, end_time=None, marker=None, limit=None):
        r"""ListAuraStatementRecordsRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type workspace_id: str
        :param endpoint_id: **参数解释**：通过ID检索Endpoint的参数。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type endpoint_id: str
        :param endpoint_name: **参数解释**：通过name检索Endpoint的参数。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type endpoint_name: str
        :param session_id: **参数解释**：Session的ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type session_id: str
        :param statement_id: **参数解释**：statement id。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type statement_id: str
        :param source: **参数解释**：执行sql来源。 **约束限制**：不涉及。 **取值范围**：   - 0：API。   - 1：Console。 **默认取值**：不涉及。
        :type source: int
        :param status: **参数解释**：状态过滤，支持一种状态查询，默认查询所有。 **约束限制**：不涉及。 **取值范围**：   - CANCELED：已取消。   - FAILED：失败。   - SUCCESSFUL：成功。   - RUNNING：运行中。   - SUBMITTED：已提交。   - ERROR：错误。 **默认取值**：不涉及。
        :type status: str
        :param start_time: **参数解释**： statement记录列表查询起始时间，该时间为statement创建时间，时间戳，单位：秒。 **约束限制**：不涉及。 **取值范围**：1~2147483647。 **默认取值**：不涉及。 
        :type start_time: int
        :param end_time: **参数解释**：statement记录列表查询结束时间，该时间为statement创建时间，时间戳，单位：秒。 **约束限制**：不涉及。 **取值范围**：1~2147483647。 **默认取值**：不涉及。
        :type end_time: int
        :param marker: **参数解释**：上一页中最后一条记录id，查询第一页时传空值。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type marker: str
        :param limit: **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。
        :type limit: int
        """
        
        

        self._workspace_id = None
        self._endpoint_id = None
        self._endpoint_name = None
        self._session_id = None
        self._statement_id = None
        self._source = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        self.workspace_id = workspace_id
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        self.endpoint_name = endpoint_name
        if session_id is not None:
            self.session_id = session_id
        if statement_id is not None:
            self.statement_id = statement_id
        if source is not None:
            self.source = source
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListAuraStatementRecordsRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The workspace_id of this ListAuraStatementRecordsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListAuraStatementRecordsRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this ListAuraStatementRecordsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this ListAuraStatementRecordsRequest.

        **参数解释**：通过ID检索Endpoint的参数。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The endpoint_id of this ListAuraStatementRecordsRequest.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this ListAuraStatementRecordsRequest.

        **参数解释**：通过ID检索Endpoint的参数。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param endpoint_id: The endpoint_id of this ListAuraStatementRecordsRequest.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this ListAuraStatementRecordsRequest.

        **参数解释**：通过name检索Endpoint的参数。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The endpoint_name of this ListAuraStatementRecordsRequest.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this ListAuraStatementRecordsRequest.

        **参数解释**：通过name检索Endpoint的参数。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param endpoint_name: The endpoint_name of this ListAuraStatementRecordsRequest.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def session_id(self):
        r"""Gets the session_id of this ListAuraStatementRecordsRequest.

        **参数解释**：Session的ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The session_id of this ListAuraStatementRecordsRequest.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this ListAuraStatementRecordsRequest.

        **参数解释**：Session的ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param session_id: The session_id of this ListAuraStatementRecordsRequest.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def statement_id(self):
        r"""Gets the statement_id of this ListAuraStatementRecordsRequest.

        **参数解释**：statement id。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The statement_id of this ListAuraStatementRecordsRequest.
        :rtype: str
        """
        return self._statement_id

    @statement_id.setter
    def statement_id(self, statement_id):
        r"""Sets the statement_id of this ListAuraStatementRecordsRequest.

        **参数解释**：statement id。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param statement_id: The statement_id of this ListAuraStatementRecordsRequest.
        :type statement_id: str
        """
        self._statement_id = statement_id

    @property
    def source(self):
        r"""Gets the source of this ListAuraStatementRecordsRequest.

        **参数解释**：执行sql来源。 **约束限制**：不涉及。 **取值范围**：   - 0：API。   - 1：Console。 **默认取值**：不涉及。

        :return: The source of this ListAuraStatementRecordsRequest.
        :rtype: int
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ListAuraStatementRecordsRequest.

        **参数解释**：执行sql来源。 **约束限制**：不涉及。 **取值范围**：   - 0：API。   - 1：Console。 **默认取值**：不涉及。

        :param source: The source of this ListAuraStatementRecordsRequest.
        :type source: int
        """
        self._source = source

    @property
    def status(self):
        r"""Gets the status of this ListAuraStatementRecordsRequest.

        **参数解释**：状态过滤，支持一种状态查询，默认查询所有。 **约束限制**：不涉及。 **取值范围**：   - CANCELED：已取消。   - FAILED：失败。   - SUCCESSFUL：成功。   - RUNNING：运行中。   - SUBMITTED：已提交。   - ERROR：错误。 **默认取值**：不涉及。

        :return: The status of this ListAuraStatementRecordsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAuraStatementRecordsRequest.

        **参数解释**：状态过滤，支持一种状态查询，默认查询所有。 **约束限制**：不涉及。 **取值范围**：   - CANCELED：已取消。   - FAILED：失败。   - SUCCESSFUL：成功。   - RUNNING：运行中。   - SUBMITTED：已提交。   - ERROR：错误。 **默认取值**：不涉及。

        :param status: The status of this ListAuraStatementRecordsRequest.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this ListAuraStatementRecordsRequest.

        **参数解释**： statement记录列表查询起始时间，该时间为statement创建时间，时间戳，单位：秒。 **约束限制**：不涉及。 **取值范围**：1~2147483647。 **默认取值**：不涉及。 

        :return: The start_time of this ListAuraStatementRecordsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListAuraStatementRecordsRequest.

        **参数解释**： statement记录列表查询起始时间，该时间为statement创建时间，时间戳，单位：秒。 **约束限制**：不涉及。 **取值范围**：1~2147483647。 **默认取值**：不涉及。 

        :param start_time: The start_time of this ListAuraStatementRecordsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListAuraStatementRecordsRequest.

        **参数解释**：statement记录列表查询结束时间，该时间为statement创建时间，时间戳，单位：秒。 **约束限制**：不涉及。 **取值范围**：1~2147483647。 **默认取值**：不涉及。

        :return: The end_time of this ListAuraStatementRecordsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListAuraStatementRecordsRequest.

        **参数解释**：statement记录列表查询结束时间，该时间为statement创建时间，时间戳，单位：秒。 **约束限制**：不涉及。 **取值范围**：1~2147483647。 **默认取值**：不涉及。

        :param end_time: The end_time of this ListAuraStatementRecordsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def marker(self):
        r"""Gets the marker of this ListAuraStatementRecordsRequest.

        **参数解释**：上一页中最后一条记录id，查询第一页时传空值。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The marker of this ListAuraStatementRecordsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAuraStatementRecordsRequest.

        **参数解释**：上一页中最后一条记录id，查询第一页时传空值。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param marker: The marker of this ListAuraStatementRecordsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListAuraStatementRecordsRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。

        :return: The limit of this ListAuraStatementRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAuraStatementRecordsRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。

        :param limit: The limit of this ListAuraStatementRecordsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAuraStatementRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
