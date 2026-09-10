# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsCorrection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reason': 'str',
        'score': 'float',
        'updated_user_id': 'str'
    }

    attribute_map = {
        'reason': 'reason',
        'score': 'score',
        'updated_user_id': 'updated_user_id'
    }

    def __init__(self, reason=None, score=None, updated_user_id=None):
        r"""OpsCorrection

        The model defined in huaweicloud sdk

        :param reason: 纠正原因。
        :type reason: str
        :param score: 纠正后的得分，通常在0到1之间。
        :type score: float
        :param updated_user_id: 纠正者的用户ID。
        :type updated_user_id: str
        """
        
        

        self._reason = None
        self._score = None
        self._updated_user_id = None
        self.discriminator = None

        if reason is not None:
            self.reason = reason
        if score is not None:
            self.score = score
        if updated_user_id is not None:
            self.updated_user_id = updated_user_id

    @property
    def reason(self):
        r"""Gets the reason of this OpsCorrection.

        纠正原因。

        :return: The reason of this OpsCorrection.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this OpsCorrection.

        纠正原因。

        :param reason: The reason of this OpsCorrection.
        :type reason: str
        """
        self._reason = reason

    @property
    def score(self):
        r"""Gets the score of this OpsCorrection.

        纠正后的得分，通常在0到1之间。

        :return: The score of this OpsCorrection.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this OpsCorrection.

        纠正后的得分，通常在0到1之间。

        :param score: The score of this OpsCorrection.
        :type score: float
        """
        self._score = score

    @property
    def updated_user_id(self):
        r"""Gets the updated_user_id of this OpsCorrection.

        纠正者的用户ID。

        :return: The updated_user_id of this OpsCorrection.
        :rtype: str
        """
        return self._updated_user_id

    @updated_user_id.setter
    def updated_user_id(self, updated_user_id):
        r"""Sets the updated_user_id of this OpsCorrection.

        纠正者的用户ID。

        :param updated_user_id: The updated_user_id of this OpsCorrection.
        :type updated_user_id: str
        """
        self._updated_user_id = updated_user_id

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
        if not isinstance(other, OpsCorrection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
