# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataframeJobSessionResp:

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
        'status': 'str',
        'create_time': 'datetime',
        'end_time': 'datetime',
        'statements': 'list[DataframeJobStatementResp]'
    }

    attribute_map = {
        'session_id': 'session_id',
        'status': 'status',
        'create_time': 'create_time',
        'end_time': 'end_time',
        'statements': 'statements'
    }

    def __init__(self, session_id=None, status=None, create_time=None, end_time=None, statements=None):
        r"""DataframeJobSessionResp

        The model defined in huaweicloud sdk

        :param session_id: **参数解释**：Session ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type session_id: str
        :param status: **参数解释**：Session 状态。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type status: str
        :param create_time: **参数解释**：资源创建时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。 **取值范围**：不涉及。 
        :type create_time: datetime
        :param end_time: **参数解释**：结束时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type end_time: datetime
        :param statements: **参数解释**：该 session 下关联的 statement 列表。 **约束限制**：session 无 statement 时返回空数组。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type statements: list[:class:`huaweicloudsdkaidatalake.v2.DataframeJobStatementResp`]
        """
        
        

        self._session_id = None
        self._status = None
        self._create_time = None
        self._end_time = None
        self._statements = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time
        if statements is not None:
            self.statements = statements

    @property
    def session_id(self):
        r"""Gets the session_id of this DataframeJobSessionResp.

        **参数解释**：Session ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The session_id of this DataframeJobSessionResp.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this DataframeJobSessionResp.

        **参数解释**：Session ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param session_id: The session_id of this DataframeJobSessionResp.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def status(self):
        r"""Gets the status of this DataframeJobSessionResp.

        **参数解释**：Session 状态。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The status of this DataframeJobSessionResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DataframeJobSessionResp.

        **参数解释**：Session 状态。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param status: The status of this DataframeJobSessionResp.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this DataframeJobSessionResp.

        **参数解释**：资源创建时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。 **取值范围**：不涉及。 

        :return: The create_time of this DataframeJobSessionResp.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DataframeJobSessionResp.

        **参数解释**：资源创建时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。 **取值范围**：不涉及。 

        :param create_time: The create_time of this DataframeJobSessionResp.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def end_time(self):
        r"""Gets the end_time of this DataframeJobSessionResp.

        **参数解释**：结束时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The end_time of this DataframeJobSessionResp.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this DataframeJobSessionResp.

        **参数解释**：结束时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param end_time: The end_time of this DataframeJobSessionResp.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def statements(self):
        r"""Gets the statements of this DataframeJobSessionResp.

        **参数解释**：该 session 下关联的 statement 列表。 **约束限制**：session 无 statement 时返回空数组。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The statements of this DataframeJobSessionResp.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.DataframeJobStatementResp`]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        r"""Sets the statements of this DataframeJobSessionResp.

        **参数解释**：该 session 下关联的 statement 列表。 **约束限制**：session 无 statement 时返回空数组。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param statements: The statements of this DataframeJobSessionResp.
        :type statements: list[:class:`huaweicloudsdkaidatalake.v2.DataframeJobStatementResp`]
        """
        self._statements = statements

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
        if not isinstance(other, DataframeJobSessionResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
