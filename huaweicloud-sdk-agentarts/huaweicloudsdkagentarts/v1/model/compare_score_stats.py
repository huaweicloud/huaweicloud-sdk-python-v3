# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareScoreStats:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluators': 'list[CompareEvaluatorStat]'
    }

    attribute_map = {
        'evaluators': 'evaluators'
    }

    def __init__(self, evaluators=None):
        r"""CompareScoreStats

        The model defined in huaweicloud sdk

        :param evaluators: 各个评估器的详细统计列表。
        :type evaluators: list[:class:`huaweicloudsdkagentarts.v1.CompareEvaluatorStat`]
        """
        
        

        self._evaluators = None
        self.discriminator = None

        if evaluators is not None:
            self.evaluators = evaluators

    @property
    def evaluators(self):
        r"""Gets the evaluators of this CompareScoreStats.

        各个评估器的详细统计列表。

        :return: The evaluators of this CompareScoreStats.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CompareEvaluatorStat`]
        """
        return self._evaluators

    @evaluators.setter
    def evaluators(self, evaluators):
        r"""Sets the evaluators of this CompareScoreStats.

        各个评估器的详细统计列表。

        :param evaluators: The evaluators of this CompareScoreStats.
        :type evaluators: list[:class:`huaweicloudsdkagentarts.v1.CompareEvaluatorStat`]
        """
        self._evaluators = evaluators

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
        if not isinstance(other, CompareScoreStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
