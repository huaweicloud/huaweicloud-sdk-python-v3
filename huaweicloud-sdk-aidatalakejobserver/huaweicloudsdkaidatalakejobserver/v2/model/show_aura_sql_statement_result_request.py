# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAuraSqlStatementResultRequest:

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
        'statement_id': 'str',
        'page_num': 'int',
        'is_enable_obs_path': 'bool'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'session_id': 'session_id',
        'statement_id': 'statement_id',
        'page_num': 'page_num',
        'is_enable_obs_path': 'is_enable_obs_path'
    }

    def __init__(self, workspace_id=None, session_id=None, statement_id=None, page_num=None, is_enable_obs_path=None):
        r"""ShowAuraSqlStatementResultRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type workspace_id: str
        :param session_id: **参数解释**：会话ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type session_id: str
        :param statement_id: **参数解释**：statement id。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、下划线。 **默认取值**：不涉及。
        :type statement_id: str
        :param page_num: **参数解释**：查询页码。 **约束限制**：不涉及。 **取值范围**：1~2147483647。 **默认取值**：不涉及。
        :type page_num: int
        :param is_enable_obs_path: **参数解释**：是否返回结果集的obs路径。 **约束限制**：不涉及。 **取值范围**：   - true：返回结果集的obs路径。   - false：返回结果集。 **默认取值**：不涉及。
        :type is_enable_obs_path: bool
        """
        
        

        self._workspace_id = None
        self._session_id = None
        self._statement_id = None
        self._page_num = None
        self._is_enable_obs_path = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.session_id = session_id
        self.statement_id = statement_id
        if page_num is not None:
            self.page_num = page_num
        if is_enable_obs_path is not None:
            self.is_enable_obs_path = is_enable_obs_path

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowAuraSqlStatementResultRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The workspace_id of this ShowAuraSqlStatementResultRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowAuraSqlStatementResultRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this ShowAuraSqlStatementResultRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def session_id(self):
        r"""Gets the session_id of this ShowAuraSqlStatementResultRequest.

        **参数解释**：会话ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The session_id of this ShowAuraSqlStatementResultRequest.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this ShowAuraSqlStatementResultRequest.

        **参数解释**：会话ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param session_id: The session_id of this ShowAuraSqlStatementResultRequest.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def statement_id(self):
        r"""Gets the statement_id of this ShowAuraSqlStatementResultRequest.

        **参数解释**：statement id。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、下划线。 **默认取值**：不涉及。

        :return: The statement_id of this ShowAuraSqlStatementResultRequest.
        :rtype: str
        """
        return self._statement_id

    @statement_id.setter
    def statement_id(self, statement_id):
        r"""Sets the statement_id of this ShowAuraSqlStatementResultRequest.

        **参数解释**：statement id。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、下划线。 **默认取值**：不涉及。

        :param statement_id: The statement_id of this ShowAuraSqlStatementResultRequest.
        :type statement_id: str
        """
        self._statement_id = statement_id

    @property
    def page_num(self):
        r"""Gets the page_num of this ShowAuraSqlStatementResultRequest.

        **参数解释**：查询页码。 **约束限制**：不涉及。 **取值范围**：1~2147483647。 **默认取值**：不涉及。

        :return: The page_num of this ShowAuraSqlStatementResultRequest.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this ShowAuraSqlStatementResultRequest.

        **参数解释**：查询页码。 **约束限制**：不涉及。 **取值范围**：1~2147483647。 **默认取值**：不涉及。

        :param page_num: The page_num of this ShowAuraSqlStatementResultRequest.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def is_enable_obs_path(self):
        r"""Gets the is_enable_obs_path of this ShowAuraSqlStatementResultRequest.

        **参数解释**：是否返回结果集的obs路径。 **约束限制**：不涉及。 **取值范围**：   - true：返回结果集的obs路径。   - false：返回结果集。 **默认取值**：不涉及。

        :return: The is_enable_obs_path of this ShowAuraSqlStatementResultRequest.
        :rtype: bool
        """
        return self._is_enable_obs_path

    @is_enable_obs_path.setter
    def is_enable_obs_path(self, is_enable_obs_path):
        r"""Sets the is_enable_obs_path of this ShowAuraSqlStatementResultRequest.

        **参数解释**：是否返回结果集的obs路径。 **约束限制**：不涉及。 **取值范围**：   - true：返回结果集的obs路径。   - false：返回结果集。 **默认取值**：不涉及。

        :param is_enable_obs_path: The is_enable_obs_path of this ShowAuraSqlStatementResultRequest.
        :type is_enable_obs_path: bool
        """
        self._is_enable_obs_path = is_enable_obs_path

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
        if not isinstance(other, ShowAuraSqlStatementResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
