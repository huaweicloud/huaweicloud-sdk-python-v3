# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SessionStatementRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'statement_id': 'str',
        'statement_content': 'str',
        'create_time': 'datetime',
        'status': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'statement_id': 'statement_id',
        'statement_content': 'statement_content',
        'create_time': 'create_time',
        'status': 'status',
        'user_name': 'user_name'
    }

    def __init__(self, statement_id=None, statement_content=None, create_time=None, status=None, user_name=None):
        r"""SessionStatementRecord

        The model defined in huaweicloud sdk

        :param statement_id: **参数解释**：statement id。 **取值范围**：长度为1~36的英文字母、数字、连字符和下划线的组合。
        :type statement_id: str
        :param statement_content: **参数解释**：查询语句。 **取值范围**：不涉及。
        :type statement_content: str
        :param create_time: **参数解释**：创建时间，时间戳，单位：毫秒。 **取值范围**：不涉及。
        :type create_time: datetime
        :param status: **参数解释**：状态。 **取值范围**：    - CANCELED：取消。   - FAILED：失败。   - SUCCESSFUL：成功。   - RUNNING：运行中。   - SUBMITTED：提交。   - ERROR：错误。
        :type status: str
        :param user_name: **参数解释**：用户名称。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、下划线。
        :type user_name: str
        """
        
        

        self._statement_id = None
        self._statement_content = None
        self._create_time = None
        self._status = None
        self._user_name = None
        self.discriminator = None

        if statement_id is not None:
            self.statement_id = statement_id
        if statement_content is not None:
            self.statement_content = statement_content
        if create_time is not None:
            self.create_time = create_time
        if status is not None:
            self.status = status
        if user_name is not None:
            self.user_name = user_name

    @property
    def statement_id(self):
        r"""Gets the statement_id of this SessionStatementRecord.

        **参数解释**：statement id。 **取值范围**：长度为1~36的英文字母、数字、连字符和下划线的组合。

        :return: The statement_id of this SessionStatementRecord.
        :rtype: str
        """
        return self._statement_id

    @statement_id.setter
    def statement_id(self, statement_id):
        r"""Sets the statement_id of this SessionStatementRecord.

        **参数解释**：statement id。 **取值范围**：长度为1~36的英文字母、数字、连字符和下划线的组合。

        :param statement_id: The statement_id of this SessionStatementRecord.
        :type statement_id: str
        """
        self._statement_id = statement_id

    @property
    def statement_content(self):
        r"""Gets the statement_content of this SessionStatementRecord.

        **参数解释**：查询语句。 **取值范围**：不涉及。

        :return: The statement_content of this SessionStatementRecord.
        :rtype: str
        """
        return self._statement_content

    @statement_content.setter
    def statement_content(self, statement_content):
        r"""Sets the statement_content of this SessionStatementRecord.

        **参数解释**：查询语句。 **取值范围**：不涉及。

        :param statement_content: The statement_content of this SessionStatementRecord.
        :type statement_content: str
        """
        self._statement_content = statement_content

    @property
    def create_time(self):
        r"""Gets the create_time of this SessionStatementRecord.

        **参数解释**：创建时间，时间戳，单位：毫秒。 **取值范围**：不涉及。

        :return: The create_time of this SessionStatementRecord.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SessionStatementRecord.

        **参数解释**：创建时间，时间戳，单位：毫秒。 **取值范围**：不涉及。

        :param create_time: The create_time of this SessionStatementRecord.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def status(self):
        r"""Gets the status of this SessionStatementRecord.

        **参数解释**：状态。 **取值范围**：    - CANCELED：取消。   - FAILED：失败。   - SUCCESSFUL：成功。   - RUNNING：运行中。   - SUBMITTED：提交。   - ERROR：错误。

        :return: The status of this SessionStatementRecord.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SessionStatementRecord.

        **参数解释**：状态。 **取值范围**：    - CANCELED：取消。   - FAILED：失败。   - SUCCESSFUL：成功。   - RUNNING：运行中。   - SUBMITTED：提交。   - ERROR：错误。

        :param status: The status of this SessionStatementRecord.
        :type status: str
        """
        self._status = status

    @property
    def user_name(self):
        r"""Gets the user_name of this SessionStatementRecord.

        **参数解释**：用户名称。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、下划线。

        :return: The user_name of this SessionStatementRecord.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this SessionStatementRecord.

        **参数解释**：用户名称。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、下划线。

        :param user_name: The user_name of this SessionStatementRecord.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, SessionStatementRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
