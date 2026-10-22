# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiguardCustomAnswersBatchDeleteBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'answer_ids': 'list[str]'
    }

    attribute_map = {
        'answer_ids': 'answer_ids'
    }

    def __init__(self, answer_ids=None):
        r"""AiguardCustomAnswersBatchDeleteBody

        The model defined in huaweicloud sdk

        :param answer_ids: 代答库ID列表
        :type answer_ids: list[str]
        """
        
        

        self._answer_ids = None
        self.discriminator = None

        self.answer_ids = answer_ids

    @property
    def answer_ids(self):
        r"""Gets the answer_ids of this AiguardCustomAnswersBatchDeleteBody.

        代答库ID列表

        :return: The answer_ids of this AiguardCustomAnswersBatchDeleteBody.
        :rtype: list[str]
        """
        return self._answer_ids

    @answer_ids.setter
    def answer_ids(self, answer_ids):
        r"""Sets the answer_ids of this AiguardCustomAnswersBatchDeleteBody.

        代答库ID列表

        :param answer_ids: The answer_ids of this AiguardCustomAnswersBatchDeleteBody.
        :type answer_ids: list[str]
        """
        self._answer_ids = answer_ids

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
        if not isinstance(other, AiguardCustomAnswersBatchDeleteBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
