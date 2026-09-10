# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsFailureSpan:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trace_id': 'str',
        'span_id': 'str',
        'error_sub_category_name': 'str',
        'evidence': 'str'
    }

    attribute_map = {
        'trace_id': 'trace_id',
        'span_id': 'span_id',
        'error_sub_category_name': 'error_sub_category_name',
        'evidence': 'evidence'
    }

    def __init__(self, trace_id=None, span_id=None, error_sub_category_name=None, evidence=None):
        r"""OpsFailureSpan

        The model defined in huaweicloud sdk

        :param trace_id: **参数解释：** 故障的trace ID。  **取值范围：** 长度1-64个字符。
        :type trace_id: str
        :param span_id: **参数解释：** 故障的span ID。  **取值范围：** 长度1-64个字符。
        :type span_id: str
        :param error_sub_category_name: **参数解释：** 故障类型。  **取值范围：** 长度1-128个字符。
        :type error_sub_category_name: str
        :param evidence: **参数解释：** 故障检测的证据。  **取值范围：** 不涉及。
        :type evidence: str
        """
        
        

        self._trace_id = None
        self._span_id = None
        self._error_sub_category_name = None
        self._evidence = None
        self.discriminator = None

        if trace_id is not None:
            self.trace_id = trace_id
        if span_id is not None:
            self.span_id = span_id
        if error_sub_category_name is not None:
            self.error_sub_category_name = error_sub_category_name
        if evidence is not None:
            self.evidence = evidence

    @property
    def trace_id(self):
        r"""Gets the trace_id of this OpsFailureSpan.

        **参数解释：** 故障的trace ID。  **取值范围：** 长度1-64个字符。

        :return: The trace_id of this OpsFailureSpan.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this OpsFailureSpan.

        **参数解释：** 故障的trace ID。  **取值范围：** 长度1-64个字符。

        :param trace_id: The trace_id of this OpsFailureSpan.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def span_id(self):
        r"""Gets the span_id of this OpsFailureSpan.

        **参数解释：** 故障的span ID。  **取值范围：** 长度1-64个字符。

        :return: The span_id of this OpsFailureSpan.
        :rtype: str
        """
        return self._span_id

    @span_id.setter
    def span_id(self, span_id):
        r"""Sets the span_id of this OpsFailureSpan.

        **参数解释：** 故障的span ID。  **取值范围：** 长度1-64个字符。

        :param span_id: The span_id of this OpsFailureSpan.
        :type span_id: str
        """
        self._span_id = span_id

    @property
    def error_sub_category_name(self):
        r"""Gets the error_sub_category_name of this OpsFailureSpan.

        **参数解释：** 故障类型。  **取值范围：** 长度1-128个字符。

        :return: The error_sub_category_name of this OpsFailureSpan.
        :rtype: str
        """
        return self._error_sub_category_name

    @error_sub_category_name.setter
    def error_sub_category_name(self, error_sub_category_name):
        r"""Sets the error_sub_category_name of this OpsFailureSpan.

        **参数解释：** 故障类型。  **取值范围：** 长度1-128个字符。

        :param error_sub_category_name: The error_sub_category_name of this OpsFailureSpan.
        :type error_sub_category_name: str
        """
        self._error_sub_category_name = error_sub_category_name

    @property
    def evidence(self):
        r"""Gets the evidence of this OpsFailureSpan.

        **参数解释：** 故障检测的证据。  **取值范围：** 不涉及。

        :return: The evidence of this OpsFailureSpan.
        :rtype: str
        """
        return self._evidence

    @evidence.setter
    def evidence(self, evidence):
        r"""Sets the evidence of this OpsFailureSpan.

        **参数解释：** 故障检测的证据。  **取值范围：** 不涉及。

        :param evidence: The evidence of this OpsFailureSpan.
        :type evidence: str
        """
        self._evidence = evidence

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
        if not isinstance(other, OpsFailureSpan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
