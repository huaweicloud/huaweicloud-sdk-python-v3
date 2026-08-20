# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuraStatementOperatorMetrics:

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
        'statement_id': 'str',
        'endpoint_id': 'str',
        'operator_metrics': 'list[OperatorMetric]'
    }

    attribute_map = {
        'session_id': 'session_id',
        'statement_id': 'statement_id',
        'endpoint_id': 'endpoint_id',
        'operator_metrics': 'operator_metrics'
    }

    def __init__(self, session_id=None, statement_id=None, endpoint_id=None, operator_metrics=None):
        r"""AuraStatementOperatorMetrics

        The model defined in huaweicloud sdk

        :param session_id: **参数解释**：会话id。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。
        :type session_id: str
        :param statement_id: **参数解释**：语句id。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。
        :type statement_id: str
        :param endpoint_id: **参数解释**：端点id。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。
        :type endpoint_id: str
        :param operator_metrics: **参数解释**：算子监控信息。 **取值范围**：不涉及。
        :type operator_metrics: list[:class:`huaweicloudsdkaidatalakejobserver.v2.OperatorMetric`]
        """
        
        

        self._session_id = None
        self._statement_id = None
        self._endpoint_id = None
        self._operator_metrics = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if statement_id is not None:
            self.statement_id = statement_id
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if operator_metrics is not None:
            self.operator_metrics = operator_metrics

    @property
    def session_id(self):
        r"""Gets the session_id of this AuraStatementOperatorMetrics.

        **参数解释**：会话id。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :return: The session_id of this AuraStatementOperatorMetrics.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this AuraStatementOperatorMetrics.

        **参数解释**：会话id。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :param session_id: The session_id of this AuraStatementOperatorMetrics.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def statement_id(self):
        r"""Gets the statement_id of this AuraStatementOperatorMetrics.

        **参数解释**：语句id。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :return: The statement_id of this AuraStatementOperatorMetrics.
        :rtype: str
        """
        return self._statement_id

    @statement_id.setter
    def statement_id(self, statement_id):
        r"""Sets the statement_id of this AuraStatementOperatorMetrics.

        **参数解释**：语句id。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :param statement_id: The statement_id of this AuraStatementOperatorMetrics.
        :type statement_id: str
        """
        self._statement_id = statement_id

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this AuraStatementOperatorMetrics.

        **参数解释**：端点id。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :return: The endpoint_id of this AuraStatementOperatorMetrics.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this AuraStatementOperatorMetrics.

        **参数解释**：端点id。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :param endpoint_id: The endpoint_id of this AuraStatementOperatorMetrics.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def operator_metrics(self):
        r"""Gets the operator_metrics of this AuraStatementOperatorMetrics.

        **参数解释**：算子监控信息。 **取值范围**：不涉及。

        :return: The operator_metrics of this AuraStatementOperatorMetrics.
        :rtype: list[:class:`huaweicloudsdkaidatalakejobserver.v2.OperatorMetric`]
        """
        return self._operator_metrics

    @operator_metrics.setter
    def operator_metrics(self, operator_metrics):
        r"""Sets the operator_metrics of this AuraStatementOperatorMetrics.

        **参数解释**：算子监控信息。 **取值范围**：不涉及。

        :param operator_metrics: The operator_metrics of this AuraStatementOperatorMetrics.
        :type operator_metrics: list[:class:`huaweicloudsdkaidatalakejobserver.v2.OperatorMetric`]
        """
        self._operator_metrics = operator_metrics

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
        if not isinstance(other, AuraStatementOperatorMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
