# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOpsTraceFeedbackRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'feedback_operation': 'str',
        'span_id': 'str'
    }

    attribute_map = {
        'feedback_operation': 'feedback_operation',
        'span_id': 'span_id'
    }

    def __init__(self, feedback_operation=None, span_id=None):
        r"""UpdateOpsTraceFeedbackRequestBody

        The model defined in huaweicloud sdk

        :param feedback_operation: like点赞或unlike点踩或cancel取消点赞点踩
        :type feedback_operation: str
        :param span_id: span ID
        :type span_id: str
        """
        
        

        self._feedback_operation = None
        self._span_id = None
        self.discriminator = None

        if feedback_operation is not None:
            self.feedback_operation = feedback_operation
        if span_id is not None:
            self.span_id = span_id

    @property
    def feedback_operation(self):
        r"""Gets the feedback_operation of this UpdateOpsTraceFeedbackRequestBody.

        like点赞或unlike点踩或cancel取消点赞点踩

        :return: The feedback_operation of this UpdateOpsTraceFeedbackRequestBody.
        :rtype: str
        """
        return self._feedback_operation

    @feedback_operation.setter
    def feedback_operation(self, feedback_operation):
        r"""Sets the feedback_operation of this UpdateOpsTraceFeedbackRequestBody.

        like点赞或unlike点踩或cancel取消点赞点踩

        :param feedback_operation: The feedback_operation of this UpdateOpsTraceFeedbackRequestBody.
        :type feedback_operation: str
        """
        self._feedback_operation = feedback_operation

    @property
    def span_id(self):
        r"""Gets the span_id of this UpdateOpsTraceFeedbackRequestBody.

        span ID

        :return: The span_id of this UpdateOpsTraceFeedbackRequestBody.
        :rtype: str
        """
        return self._span_id

    @span_id.setter
    def span_id(self, span_id):
        r"""Sets the span_id of this UpdateOpsTraceFeedbackRequestBody.

        span ID

        :param span_id: The span_id of this UpdateOpsTraceFeedbackRequestBody.
        :type span_id: str
        """
        self._span_id = span_id

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
        if not isinstance(other, UpdateOpsTraceFeedbackRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
