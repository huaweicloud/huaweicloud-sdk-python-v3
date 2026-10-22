# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCustomAnswersRequest:

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
        'body': 'AiguardCustomAnswersUpdateBody'
    }

    attribute_map = {
        'answer_id': 'answer_id',
        'body': 'body'
    }

    def __init__(self, answer_id=None, body=None):
        r"""UpdateCustomAnswersRequest

        The model defined in huaweicloud sdk

        :param answer_id: **参数解释：** 代答库ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type answer_id: str
        :param body: Body of the UpdateCustomAnswersRequest
        :type body: :class:`huaweicloudsdkwaf.v1.AiguardCustomAnswersUpdateBody`
        """
        
        

        self._answer_id = None
        self._body = None
        self.discriminator = None

        self.answer_id = answer_id
        if body is not None:
            self.body = body

    @property
    def answer_id(self):
        r"""Gets the answer_id of this UpdateCustomAnswersRequest.

        **参数解释：** 代答库ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The answer_id of this UpdateCustomAnswersRequest.
        :rtype: str
        """
        return self._answer_id

    @answer_id.setter
    def answer_id(self, answer_id):
        r"""Sets the answer_id of this UpdateCustomAnswersRequest.

        **参数解释：** 代答库ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param answer_id: The answer_id of this UpdateCustomAnswersRequest.
        :type answer_id: str
        """
        self._answer_id = answer_id

    @property
    def body(self):
        r"""Gets the body of this UpdateCustomAnswersRequest.

        :return: The body of this UpdateCustomAnswersRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.AiguardCustomAnswersUpdateBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateCustomAnswersRequest.

        :param body: The body of this UpdateCustomAnswersRequest.
        :type body: :class:`huaweicloudsdkwaf.v1.AiguardCustomAnswersUpdateBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateCustomAnswersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
