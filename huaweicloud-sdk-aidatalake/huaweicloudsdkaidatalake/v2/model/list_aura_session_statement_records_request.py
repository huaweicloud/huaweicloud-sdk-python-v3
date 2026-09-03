# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuraSessionStatementRecordsRequest:

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
        'session_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'statement_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'session_id': 'session_id',
        'limit': 'limit',
        'marker': 'marker',
        'statement_id': 'statement_id',
        'status': 'status'
    }

    def __init__(self, workspace_id=None, session_id=None, limit=None, marker=None, statement_id=None, status=None):
        r"""ListAuraSessionStatementRecordsRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type workspace_id: str
        :param session_id: **参数解释**：会话ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type session_id: str
        :param limit: **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。
        :type limit: int
        :param marker: **参数解释**：上一页中最后一条记录id，查询第一页时传空值。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type marker: str
        :param statement_id: **参数解释**：statement id。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type statement_id: str
        :param status: **参数解释**：状态过滤，支持一种状态查询，默认查询所有。 **约束限制**：不涉及。 **取值范围**：   - CANCELED：已取消。   - FAILED：失败。   - SUCCESSFUL：成功。   - RUNNING：运行中。   - SUBMITTED：已提交。   - ERROR：错误。 **默认取值**：不涉及。
        :type status: str
        """
        
        

        self._workspace_id = None
        self._session_id = None
        self._limit = None
        self._marker = None
        self._statement_id = None
        self._status = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.session_id = session_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if statement_id is not None:
            self.statement_id = statement_id
        if status is not None:
            self.status = status

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListAuraSessionStatementRecordsRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The workspace_id of this ListAuraSessionStatementRecordsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListAuraSessionStatementRecordsRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this ListAuraSessionStatementRecordsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def session_id(self):
        r"""Gets the session_id of this ListAuraSessionStatementRecordsRequest.

        **参数解释**：会话ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The session_id of this ListAuraSessionStatementRecordsRequest.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this ListAuraSessionStatementRecordsRequest.

        **参数解释**：会话ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param session_id: The session_id of this ListAuraSessionStatementRecordsRequest.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def limit(self):
        r"""Gets the limit of this ListAuraSessionStatementRecordsRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。

        :return: The limit of this ListAuraSessionStatementRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAuraSessionStatementRecordsRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。

        :param limit: The limit of this ListAuraSessionStatementRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListAuraSessionStatementRecordsRequest.

        **参数解释**：上一页中最后一条记录id，查询第一页时传空值。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The marker of this ListAuraSessionStatementRecordsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAuraSessionStatementRecordsRequest.

        **参数解释**：上一页中最后一条记录id，查询第一页时传空值。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param marker: The marker of this ListAuraSessionStatementRecordsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def statement_id(self):
        r"""Gets the statement_id of this ListAuraSessionStatementRecordsRequest.

        **参数解释**：statement id。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The statement_id of this ListAuraSessionStatementRecordsRequest.
        :rtype: str
        """
        return self._statement_id

    @statement_id.setter
    def statement_id(self, statement_id):
        r"""Sets the statement_id of this ListAuraSessionStatementRecordsRequest.

        **参数解释**：statement id。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param statement_id: The statement_id of this ListAuraSessionStatementRecordsRequest.
        :type statement_id: str
        """
        self._statement_id = statement_id

    @property
    def status(self):
        r"""Gets the status of this ListAuraSessionStatementRecordsRequest.

        **参数解释**：状态过滤，支持一种状态查询，默认查询所有。 **约束限制**：不涉及。 **取值范围**：   - CANCELED：已取消。   - FAILED：失败。   - SUCCESSFUL：成功。   - RUNNING：运行中。   - SUBMITTED：已提交。   - ERROR：错误。 **默认取值**：不涉及。

        :return: The status of this ListAuraSessionStatementRecordsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAuraSessionStatementRecordsRequest.

        **参数解释**：状态过滤，支持一种状态查询，默认查询所有。 **约束限制**：不涉及。 **取值范围**：   - CANCELED：已取消。   - FAILED：失败。   - SUCCESSFUL：成功。   - RUNNING：运行中。   - SUBMITTED：已提交。   - ERROR：错误。 **默认取值**：不涉及。

        :param status: The status of this ListAuraSessionStatementRecordsRequest.
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
        if not isinstance(other, ListAuraSessionStatementRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
