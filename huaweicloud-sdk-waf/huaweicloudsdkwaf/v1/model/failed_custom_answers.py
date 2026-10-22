# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailedCustomAnswers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'answer_id': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'answer_id': 'answer_id',
        'reason': 'reason'
    }

    def __init__(self, answer_id=None, reason=None):
        r"""FailedCustomAnswers

        The model defined in huaweicloud sdk

        :param answer_id: 代答库ID
        :type answer_id: str
        :param reason: 失败原因
        :type reason: str
        """
        
        

        self._answer_id = None
        self._reason = None
        self.discriminator = None

        if answer_id is not None:
            self.answer_id = answer_id
        if reason is not None:
            self.reason = reason

    @property
    def answer_id(self):
        r"""Gets the answer_id of this FailedCustomAnswers.

        代答库ID

        :return: The answer_id of this FailedCustomAnswers.
        :rtype: str
        """
        return self._answer_id

    @answer_id.setter
    def answer_id(self, answer_id):
        r"""Sets the answer_id of this FailedCustomAnswers.

        代答库ID

        :param answer_id: The answer_id of this FailedCustomAnswers.
        :type answer_id: str
        """
        self._answer_id = answer_id

    @property
    def reason(self):
        r"""Gets the reason of this FailedCustomAnswers.

        失败原因

        :return: The reason of this FailedCustomAnswers.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this FailedCustomAnswers.

        失败原因

        :param reason: The reason of this FailedCustomAnswers.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, FailedCustomAnswers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
