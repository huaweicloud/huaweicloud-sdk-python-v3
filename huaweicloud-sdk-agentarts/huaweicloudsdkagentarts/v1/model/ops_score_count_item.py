# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsScoreCountItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'score': 'str',
        'count': 'int'
    }

    attribute_map = {
        'score': 'score',
        'count': 'count'
    }

    def __init__(self, score=None, count=None):
        r"""OpsScoreCountItem

        The model defined in huaweicloud sdk

        :param score: **参数解释：** 评估得分值，保留两位小数。 **取值范围：** 0.00-1.00之间的字符串。 
        :type score: str
        :param count: **参数解释：** 该得分对应的样本数量。 **取值范围：** 大于等于0的整数。 
        :type count: int
        """
        
        

        self._score = None
        self._count = None
        self.discriminator = None

        if score is not None:
            self.score = score
        if count is not None:
            self.count = count

    @property
    def score(self):
        r"""Gets the score of this OpsScoreCountItem.

        **参数解释：** 评估得分值，保留两位小数。 **取值范围：** 0.00-1.00之间的字符串。 

        :return: The score of this OpsScoreCountItem.
        :rtype: str
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this OpsScoreCountItem.

        **参数解释：** 评估得分值，保留两位小数。 **取值范围：** 0.00-1.00之间的字符串。 

        :param score: The score of this OpsScoreCountItem.
        :type score: str
        """
        self._score = score

    @property
    def count(self):
        r"""Gets the count of this OpsScoreCountItem.

        **参数解释：** 该得分对应的样本数量。 **取值范围：** 大于等于0的整数。 

        :return: The count of this OpsScoreCountItem.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this OpsScoreCountItem.

        **参数解释：** 该得分对应的样本数量。 **取值范围：** 大于等于0的整数。 

        :param count: The count of this OpsScoreCountItem.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, OpsScoreCountItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
