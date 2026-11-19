# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataframeJobStatementResp:

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
        'status': 'str',
        'statement_content': 'str',
        'tuple_processed': 'int',
        'create_time': 'datetime',
        'finish_time': 'datetime'
    }

    attribute_map = {
        'statement_id': 'statement_id',
        'status': 'status',
        'statement_content': 'statement_content',
        'tuple_processed': 'tuple_processed',
        'create_time': 'create_time',
        'finish_time': 'finish_time'
    }

    def __init__(self, statement_id=None, status=None, statement_content=None, tuple_processed=None, create_time=None, finish_time=None):
        r"""DataframeJobStatementResp

        The model defined in huaweicloud sdk

        :param statement_id: **参数解释**：Statement ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type statement_id: str
        :param status: **参数解释**：执行状态。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type status: str
        :param statement_content: **参数解释**：SQL 执行内容。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type statement_content: str
        :param tuple_processed: **参数解释**：已处理条数。 **约束限制**：由 operator_realtime 上报更新。 **取值范围**：不涉及。 **默认取值**：0。
        :type tuple_processed: int
        :param create_time: **参数解释**：资源创建时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。 **取值范围**：不涉及。 
        :type create_time: datetime
        :param finish_time: **参数解释**：结束时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type finish_time: datetime
        """
        
        

        self._statement_id = None
        self._status = None
        self._statement_content = None
        self._tuple_processed = None
        self._create_time = None
        self._finish_time = None
        self.discriminator = None

        if statement_id is not None:
            self.statement_id = statement_id
        if status is not None:
            self.status = status
        if statement_content is not None:
            self.statement_content = statement_content
        if tuple_processed is not None:
            self.tuple_processed = tuple_processed
        if create_time is not None:
            self.create_time = create_time
        if finish_time is not None:
            self.finish_time = finish_time

    @property
    def statement_id(self):
        r"""Gets the statement_id of this DataframeJobStatementResp.

        **参数解释**：Statement ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The statement_id of this DataframeJobStatementResp.
        :rtype: str
        """
        return self._statement_id

    @statement_id.setter
    def statement_id(self, statement_id):
        r"""Sets the statement_id of this DataframeJobStatementResp.

        **参数解释**：Statement ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param statement_id: The statement_id of this DataframeJobStatementResp.
        :type statement_id: str
        """
        self._statement_id = statement_id

    @property
    def status(self):
        r"""Gets the status of this DataframeJobStatementResp.

        **参数解释**：执行状态。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The status of this DataframeJobStatementResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DataframeJobStatementResp.

        **参数解释**：执行状态。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param status: The status of this DataframeJobStatementResp.
        :type status: str
        """
        self._status = status

    @property
    def statement_content(self):
        r"""Gets the statement_content of this DataframeJobStatementResp.

        **参数解释**：SQL 执行内容。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The statement_content of this DataframeJobStatementResp.
        :rtype: str
        """
        return self._statement_content

    @statement_content.setter
    def statement_content(self, statement_content):
        r"""Sets the statement_content of this DataframeJobStatementResp.

        **参数解释**：SQL 执行内容。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param statement_content: The statement_content of this DataframeJobStatementResp.
        :type statement_content: str
        """
        self._statement_content = statement_content

    @property
    def tuple_processed(self):
        r"""Gets the tuple_processed of this DataframeJobStatementResp.

        **参数解释**：已处理条数。 **约束限制**：由 operator_realtime 上报更新。 **取值范围**：不涉及。 **默认取值**：0。

        :return: The tuple_processed of this DataframeJobStatementResp.
        :rtype: int
        """
        return self._tuple_processed

    @tuple_processed.setter
    def tuple_processed(self, tuple_processed):
        r"""Sets the tuple_processed of this DataframeJobStatementResp.

        **参数解释**：已处理条数。 **约束限制**：由 operator_realtime 上报更新。 **取值范围**：不涉及。 **默认取值**：0。

        :param tuple_processed: The tuple_processed of this DataframeJobStatementResp.
        :type tuple_processed: int
        """
        self._tuple_processed = tuple_processed

    @property
    def create_time(self):
        r"""Gets the create_time of this DataframeJobStatementResp.

        **参数解释**：资源创建时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。 **取值范围**：不涉及。 

        :return: The create_time of this DataframeJobStatementResp.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DataframeJobStatementResp.

        **参数解释**：资源创建时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。 **取值范围**：不涉及。 

        :param create_time: The create_time of this DataframeJobStatementResp.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this DataframeJobStatementResp.

        **参数解释**：结束时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The finish_time of this DataframeJobStatementResp.
        :rtype: datetime
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this DataframeJobStatementResp.

        **参数解释**：结束时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param finish_time: The finish_time of this DataframeJobStatementResp.
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
        if not isinstance(other, DataframeJobStatementResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
