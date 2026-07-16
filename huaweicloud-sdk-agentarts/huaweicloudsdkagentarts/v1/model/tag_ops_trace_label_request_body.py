# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagOpsTraceLabelRequestBody:

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
        'trace_type': 'str',
        'span_id': 'str',
        'label': 'dict(str, str)'
    }

    attribute_map = {
        'session_id': 'session_id',
        'trace_type': 'trace_type',
        'span_id': 'span_id',
        'label': 'label'
    }

    def __init__(self, session_id=None, trace_type=None, span_id=None, label=None):
        r"""TagOpsTraceLabelRequestBody

        The model defined in huaweicloud sdk

        :param session_id: 会话id
        :type session_id: str
        :param trace_type: trace类型
        :type trace_type: str
        :param span_id: span的id
        :type span_id: str
        :param label: 标注的过滤条件
        :type label: dict(str, str)
        """
        
        

        self._session_id = None
        self._trace_type = None
        self._span_id = None
        self._label = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if trace_type is not None:
            self.trace_type = trace_type
        if span_id is not None:
            self.span_id = span_id
        if label is not None:
            self.label = label

    @property
    def session_id(self):
        r"""Gets the session_id of this TagOpsTraceLabelRequestBody.

        会话id

        :return: The session_id of this TagOpsTraceLabelRequestBody.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this TagOpsTraceLabelRequestBody.

        会话id

        :param session_id: The session_id of this TagOpsTraceLabelRequestBody.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def trace_type(self):
        r"""Gets the trace_type of this TagOpsTraceLabelRequestBody.

        trace类型

        :return: The trace_type of this TagOpsTraceLabelRequestBody.
        :rtype: str
        """
        return self._trace_type

    @trace_type.setter
    def trace_type(self, trace_type):
        r"""Sets the trace_type of this TagOpsTraceLabelRequestBody.

        trace类型

        :param trace_type: The trace_type of this TagOpsTraceLabelRequestBody.
        :type trace_type: str
        """
        self._trace_type = trace_type

    @property
    def span_id(self):
        r"""Gets the span_id of this TagOpsTraceLabelRequestBody.

        span的id

        :return: The span_id of this TagOpsTraceLabelRequestBody.
        :rtype: str
        """
        return self._span_id

    @span_id.setter
    def span_id(self, span_id):
        r"""Sets the span_id of this TagOpsTraceLabelRequestBody.

        span的id

        :param span_id: The span_id of this TagOpsTraceLabelRequestBody.
        :type span_id: str
        """
        self._span_id = span_id

    @property
    def label(self):
        r"""Gets the label of this TagOpsTraceLabelRequestBody.

        标注的过滤条件

        :return: The label of this TagOpsTraceLabelRequestBody.
        :rtype: dict(str, str)
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this TagOpsTraceLabelRequestBody.

        标注的过滤条件

        :param label: The label of this TagOpsTraceLabelRequestBody.
        :type label: dict(str, str)
        """
        self._label = label

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
        if not isinstance(other, TagOpsTraceLabelRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
