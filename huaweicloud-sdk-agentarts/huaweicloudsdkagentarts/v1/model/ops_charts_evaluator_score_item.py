# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsChartsEvaluatorScoreItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluator_id': 'str',
        'evaluator_name': 'str',
        'sum_score': 'float',
        'min_score': 'float',
        'max_score': 'float',
        'avg_score': 'float'
    }

    attribute_map = {
        'evaluator_id': 'evaluator_id',
        'evaluator_name': 'evaluator_name',
        'sum_score': 'sum_score',
        'min_score': 'min_score',
        'max_score': 'max_score',
        'avg_score': 'avg_score'
    }

    def __init__(self, evaluator_id=None, evaluator_name=None, sum_score=None, min_score=None, max_score=None, avg_score=None):
        r"""OpsChartsEvaluatorScoreItem

        The model defined in huaweicloud sdk

        :param evaluator_id: 评估器ID。
        :type evaluator_id: str
        :param evaluator_name: 评估器名称。
        :type evaluator_name: str
        :param sum_score: 总分。
        :type sum_score: float
        :param min_score: 最低分。
        :type min_score: float
        :param max_score: 最高分。
        :type max_score: float
        :param avg_score: 平均分。
        :type avg_score: float
        """
        
        

        self._evaluator_id = None
        self._evaluator_name = None
        self._sum_score = None
        self._min_score = None
        self._max_score = None
        self._avg_score = None
        self.discriminator = None

        if evaluator_id is not None:
            self.evaluator_id = evaluator_id
        if evaluator_name is not None:
            self.evaluator_name = evaluator_name
        if sum_score is not None:
            self.sum_score = sum_score
        if min_score is not None:
            self.min_score = min_score
        if max_score is not None:
            self.max_score = max_score
        if avg_score is not None:
            self.avg_score = avg_score

    @property
    def evaluator_id(self):
        r"""Gets the evaluator_id of this OpsChartsEvaluatorScoreItem.

        评估器ID。

        :return: The evaluator_id of this OpsChartsEvaluatorScoreItem.
        :rtype: str
        """
        return self._evaluator_id

    @evaluator_id.setter
    def evaluator_id(self, evaluator_id):
        r"""Sets the evaluator_id of this OpsChartsEvaluatorScoreItem.

        评估器ID。

        :param evaluator_id: The evaluator_id of this OpsChartsEvaluatorScoreItem.
        :type evaluator_id: str
        """
        self._evaluator_id = evaluator_id

    @property
    def evaluator_name(self):
        r"""Gets the evaluator_name of this OpsChartsEvaluatorScoreItem.

        评估器名称。

        :return: The evaluator_name of this OpsChartsEvaluatorScoreItem.
        :rtype: str
        """
        return self._evaluator_name

    @evaluator_name.setter
    def evaluator_name(self, evaluator_name):
        r"""Sets the evaluator_name of this OpsChartsEvaluatorScoreItem.

        评估器名称。

        :param evaluator_name: The evaluator_name of this OpsChartsEvaluatorScoreItem.
        :type evaluator_name: str
        """
        self._evaluator_name = evaluator_name

    @property
    def sum_score(self):
        r"""Gets the sum_score of this OpsChartsEvaluatorScoreItem.

        总分。

        :return: The sum_score of this OpsChartsEvaluatorScoreItem.
        :rtype: float
        """
        return self._sum_score

    @sum_score.setter
    def sum_score(self, sum_score):
        r"""Sets the sum_score of this OpsChartsEvaluatorScoreItem.

        总分。

        :param sum_score: The sum_score of this OpsChartsEvaluatorScoreItem.
        :type sum_score: float
        """
        self._sum_score = sum_score

    @property
    def min_score(self):
        r"""Gets the min_score of this OpsChartsEvaluatorScoreItem.

        最低分。

        :return: The min_score of this OpsChartsEvaluatorScoreItem.
        :rtype: float
        """
        return self._min_score

    @min_score.setter
    def min_score(self, min_score):
        r"""Sets the min_score of this OpsChartsEvaluatorScoreItem.

        最低分。

        :param min_score: The min_score of this OpsChartsEvaluatorScoreItem.
        :type min_score: float
        """
        self._min_score = min_score

    @property
    def max_score(self):
        r"""Gets the max_score of this OpsChartsEvaluatorScoreItem.

        最高分。

        :return: The max_score of this OpsChartsEvaluatorScoreItem.
        :rtype: float
        """
        return self._max_score

    @max_score.setter
    def max_score(self, max_score):
        r"""Sets the max_score of this OpsChartsEvaluatorScoreItem.

        最高分。

        :param max_score: The max_score of this OpsChartsEvaluatorScoreItem.
        :type max_score: float
        """
        self._max_score = max_score

    @property
    def avg_score(self):
        r"""Gets the avg_score of this OpsChartsEvaluatorScoreItem.

        平均分。

        :return: The avg_score of this OpsChartsEvaluatorScoreItem.
        :rtype: float
        """
        return self._avg_score

    @avg_score.setter
    def avg_score(self, avg_score):
        r"""Sets the avg_score of this OpsChartsEvaluatorScoreItem.

        平均分。

        :param avg_score: The avg_score of this OpsChartsEvaluatorScoreItem.
        :type avg_score: float
        """
        self._avg_score = avg_score

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
        if not isinstance(other, OpsChartsEvaluatorScoreItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
