# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareTaskMetricsStat:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'ave_score': 'float',
        'ave_latency_s': 'int',
        'ave_input_token': 'int',
        'ave_output_token': 'int',
        'ave_total_token': 'int',
        'max_score': 'float',
        'max_latency_s': 'int',
        'max_input_token': 'int',
        'max_output_token': 'int',
        'max_total_token': 'int',
        'min_score': 'float',
        'min_latency_s': 'int',
        'min_input_token': 'int',
        'min_output_token': 'int',
        'min_total_token': 'int',
        'sum_score': 'float',
        'sum_latency_s': 'int',
        'sum_input_token': 'int',
        'sum_output_token': 'int',
        'sum_total_token': 'int',
        'score_stats': 'CompareScoreStats'
    }

    attribute_map = {
        'task_id': 'task_id',
        'ave_score': 'ave_score',
        'ave_latency_s': 'ave_latency_s',
        'ave_input_token': 'ave_input_token',
        'ave_output_token': 'ave_output_token',
        'ave_total_token': 'ave_total_token',
        'max_score': 'max_score',
        'max_latency_s': 'max_latency_s',
        'max_input_token': 'max_input_token',
        'max_output_token': 'max_output_token',
        'max_total_token': 'max_total_token',
        'min_score': 'min_score',
        'min_latency_s': 'min_latency_s',
        'min_input_token': 'min_input_token',
        'min_output_token': 'min_output_token',
        'min_total_token': 'min_total_token',
        'sum_score': 'sum_score',
        'sum_latency_s': 'sum_latency_s',
        'sum_input_token': 'sum_input_token',
        'sum_output_token': 'sum_output_token',
        'sum_total_token': 'sum_total_token',
        'score_stats': 'score_stats'
    }

    def __init__(self, task_id=None, ave_score=None, ave_latency_s=None, ave_input_token=None, ave_output_token=None, ave_total_token=None, max_score=None, max_latency_s=None, max_input_token=None, max_output_token=None, max_total_token=None, min_score=None, min_latency_s=None, min_input_token=None, min_output_token=None, min_total_token=None, sum_score=None, sum_latency_s=None, sum_input_token=None, sum_output_token=None, sum_total_token=None, score_stats=None):
        r"""CompareTaskMetricsStat

        The model defined in huaweicloud sdk

        :param task_id: 任务的唯一标识符（UUID格式）。
        :type task_id: str
        :param ave_score: 所有评估器得分的平均值（跨评估器、跨样本）。
        :type ave_score: float
        :param ave_latency_s: 所有评估的平均延迟（秒）。
        :type ave_latency_s: int
        :param ave_input_token: 所有评估的平均输入token数。
        :type ave_input_token: int
        :param ave_output_token: 所有评估的平均输出token数。
        :type ave_output_token: int
        :param ave_total_token: 所有评估的平均总token数（输入+输出）。
        :type ave_total_token: int
        :param max_score: 所有评估的最大得分。
        :type max_score: float
        :param max_latency_s: 所有评估的最大延迟（秒）。
        :type max_latency_s: int
        :param max_input_token: 所有评估的最大输入token数。
        :type max_input_token: int
        :param max_output_token: 所有评估的最大输出token数。
        :type max_output_token: int
        :param max_total_token: 所有评估的最大总token数。
        :type max_total_token: int
        :param min_score: 所有评估的最小得分。
        :type min_score: float
        :param min_latency_s: 所有评估的最小延迟（秒）。
        :type min_latency_s: int
        :param min_input_token: 所有评估的最小输入token数。
        :type min_input_token: int
        :param min_output_token: 所有评估的最小输出token数。
        :type min_output_token: int
        :param min_total_token: 所有评估的最小总token数。
        :type min_total_token: int
        :param sum_score: 所有评估的得分总和。
        :type sum_score: float
        :param sum_latency_s: 所有评估的延迟总和（秒）。
        :type sum_latency_s: int
        :param sum_input_token: 所有评估的输入token总和。
        :type sum_input_token: int
        :param sum_output_token: 所有评估的输出token总和。
        :type sum_output_token: int
        :param sum_total_token: 所有评估的总token总和。
        :type sum_total_token: int
        :param score_stats: 
        :type score_stats: :class:`huaweicloudsdkagentarts.v1.CompareScoreStats`
        """
        
        

        self._task_id = None
        self._ave_score = None
        self._ave_latency_s = None
        self._ave_input_token = None
        self._ave_output_token = None
        self._ave_total_token = None
        self._max_score = None
        self._max_latency_s = None
        self._max_input_token = None
        self._max_output_token = None
        self._max_total_token = None
        self._min_score = None
        self._min_latency_s = None
        self._min_input_token = None
        self._min_output_token = None
        self._min_total_token = None
        self._sum_score = None
        self._sum_latency_s = None
        self._sum_input_token = None
        self._sum_output_token = None
        self._sum_total_token = None
        self._score_stats = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if ave_score is not None:
            self.ave_score = ave_score
        if ave_latency_s is not None:
            self.ave_latency_s = ave_latency_s
        if ave_input_token is not None:
            self.ave_input_token = ave_input_token
        if ave_output_token is not None:
            self.ave_output_token = ave_output_token
        if ave_total_token is not None:
            self.ave_total_token = ave_total_token
        if max_score is not None:
            self.max_score = max_score
        if max_latency_s is not None:
            self.max_latency_s = max_latency_s
        if max_input_token is not None:
            self.max_input_token = max_input_token
        if max_output_token is not None:
            self.max_output_token = max_output_token
        if max_total_token is not None:
            self.max_total_token = max_total_token
        if min_score is not None:
            self.min_score = min_score
        if min_latency_s is not None:
            self.min_latency_s = min_latency_s
        if min_input_token is not None:
            self.min_input_token = min_input_token
        if min_output_token is not None:
            self.min_output_token = min_output_token
        if min_total_token is not None:
            self.min_total_token = min_total_token
        if sum_score is not None:
            self.sum_score = sum_score
        if sum_latency_s is not None:
            self.sum_latency_s = sum_latency_s
        if sum_input_token is not None:
            self.sum_input_token = sum_input_token
        if sum_output_token is not None:
            self.sum_output_token = sum_output_token
        if sum_total_token is not None:
            self.sum_total_token = sum_total_token
        if score_stats is not None:
            self.score_stats = score_stats

    @property
    def task_id(self):
        r"""Gets the task_id of this CompareTaskMetricsStat.

        任务的唯一标识符（UUID格式）。

        :return: The task_id of this CompareTaskMetricsStat.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this CompareTaskMetricsStat.

        任务的唯一标识符（UUID格式）。

        :param task_id: The task_id of this CompareTaskMetricsStat.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def ave_score(self):
        r"""Gets the ave_score of this CompareTaskMetricsStat.

        所有评估器得分的平均值（跨评估器、跨样本）。

        :return: The ave_score of this CompareTaskMetricsStat.
        :rtype: float
        """
        return self._ave_score

    @ave_score.setter
    def ave_score(self, ave_score):
        r"""Sets the ave_score of this CompareTaskMetricsStat.

        所有评估器得分的平均值（跨评估器、跨样本）。

        :param ave_score: The ave_score of this CompareTaskMetricsStat.
        :type ave_score: float
        """
        self._ave_score = ave_score

    @property
    def ave_latency_s(self):
        r"""Gets the ave_latency_s of this CompareTaskMetricsStat.

        所有评估的平均延迟（秒）。

        :return: The ave_latency_s of this CompareTaskMetricsStat.
        :rtype: int
        """
        return self._ave_latency_s

    @ave_latency_s.setter
    def ave_latency_s(self, ave_latency_s):
        r"""Sets the ave_latency_s of this CompareTaskMetricsStat.

        所有评估的平均延迟（秒）。

        :param ave_latency_s: The ave_latency_s of this CompareTaskMetricsStat.
        :type ave_latency_s: int
        """
        self._ave_latency_s = ave_latency_s

    @property
    def ave_input_token(self):
        r"""Gets the ave_input_token of this CompareTaskMetricsStat.

        所有评估的平均输入token数。

        :return: The ave_input_token of this CompareTaskMetricsStat.
        :rtype: int
        """
        return self._ave_input_token

    @ave_input_token.setter
    def ave_input_token(self, ave_input_token):
        r"""Sets the ave_input_token of this CompareTaskMetricsStat.

        所有评估的平均输入token数。

        :param ave_input_token: The ave_input_token of this CompareTaskMetricsStat.
        :type ave_input_token: int
        """
        self._ave_input_token = ave_input_token

    @property
    def ave_output_token(self):
        r"""Gets the ave_output_token of this CompareTaskMetricsStat.

        所有评估的平均输出token数。

        :return: The ave_output_token of this CompareTaskMetricsStat.
        :rtype: int
        """
        return self._ave_output_token

    @ave_output_token.setter
    def ave_output_token(self, ave_output_token):
        r"""Sets the ave_output_token of this CompareTaskMetricsStat.

        所有评估的平均输出token数。

        :param ave_output_token: The ave_output_token of this CompareTaskMetricsStat.
        :type ave_output_token: int
        """
        self._ave_output_token = ave_output_token

    @property
    def ave_total_token(self):
        r"""Gets the ave_total_token of this CompareTaskMetricsStat.

        所有评估的平均总token数（输入+输出）。

        :return: The ave_total_token of this CompareTaskMetricsStat.
        :rtype: int
        """
        return self._ave_total_token

    @ave_total_token.setter
    def ave_total_token(self, ave_total_token):
        r"""Sets the ave_total_token of this CompareTaskMetricsStat.

        所有评估的平均总token数（输入+输出）。

        :param ave_total_token: The ave_total_token of this CompareTaskMetricsStat.
        :type ave_total_token: int
        """
        self._ave_total_token = ave_total_token

    @property
    def max_score(self):
        r"""Gets the max_score of this CompareTaskMetricsStat.

        所有评估的最大得分。

        :return: The max_score of this CompareTaskMetricsStat.
        :rtype: float
        """
        return self._max_score

    @max_score.setter
    def max_score(self, max_score):
        r"""Sets the max_score of this CompareTaskMetricsStat.

        所有评估的最大得分。

        :param max_score: The max_score of this CompareTaskMetricsStat.
        :type max_score: float
        """
        self._max_score = max_score

    @property
    def max_latency_s(self):
        r"""Gets the max_latency_s of this CompareTaskMetricsStat.

        所有评估的最大延迟（秒）。

        :return: The max_latency_s of this CompareTaskMetricsStat.
        :rtype: int
        """
        return self._max_latency_s

    @max_latency_s.setter
    def max_latency_s(self, max_latency_s):
        r"""Sets the max_latency_s of this CompareTaskMetricsStat.

        所有评估的最大延迟（秒）。

        :param max_latency_s: The max_latency_s of this CompareTaskMetricsStat.
        :type max_latency_s: int
        """
        self._max_latency_s = max_latency_s

    @property
    def max_input_token(self):
        r"""Gets the max_input_token of this CompareTaskMetricsStat.

        所有评估的最大输入token数。

        :return: The max_input_token of this CompareTaskMetricsStat.
        :rtype: int
        """
        return self._max_input_token

    @max_input_token.setter
    def max_input_token(self, max_input_token):
        r"""Sets the max_input_token of this CompareTaskMetricsStat.

        所有评估的最大输入token数。

        :param max_input_token: The max_input_token of this CompareTaskMetricsStat.
        :type max_input_token: int
        """
        self._max_input_token = max_input_token

    @property
    def max_output_token(self):
        r"""Gets the max_output_token of this CompareTaskMetricsStat.

        所有评估的最大输出token数。

        :return: The max_output_token of this CompareTaskMetricsStat.
        :rtype: int
        """
        return self._max_output_token

    @max_output_token.setter
    def max_output_token(self, max_output_token):
        r"""Sets the max_output_token of this CompareTaskMetricsStat.

        所有评估的最大输出token数。

        :param max_output_token: The max_output_token of this CompareTaskMetricsStat.
        :type max_output_token: int
        """
        self._max_output_token = max_output_token

    @property
    def max_total_token(self):
        r"""Gets the max_total_token of this CompareTaskMetricsStat.

        所有评估的最大总token数。

        :return: The max_total_token of this CompareTaskMetricsStat.
        :rtype: int
        """
        return self._max_total_token

    @max_total_token.setter
    def max_total_token(self, max_total_token):
        r"""Sets the max_total_token of this CompareTaskMetricsStat.

        所有评估的最大总token数。

        :param max_total_token: The max_total_token of this CompareTaskMetricsStat.
        :type max_total_token: int
        """
        self._max_total_token = max_total_token

    @property
    def min_score(self):
        r"""Gets the min_score of this CompareTaskMetricsStat.

        所有评估的最小得分。

        :return: The min_score of this CompareTaskMetricsStat.
        :rtype: float
        """
        return self._min_score

    @min_score.setter
    def min_score(self, min_score):
        r"""Sets the min_score of this CompareTaskMetricsStat.

        所有评估的最小得分。

        :param min_score: The min_score of this CompareTaskMetricsStat.
        :type min_score: float
        """
        self._min_score = min_score

    @property
    def min_latency_s(self):
        r"""Gets the min_latency_s of this CompareTaskMetricsStat.

        所有评估的最小延迟（秒）。

        :return: The min_latency_s of this CompareTaskMetricsStat.
        :rtype: int
        """
        return self._min_latency_s

    @min_latency_s.setter
    def min_latency_s(self, min_latency_s):
        r"""Sets the min_latency_s of this CompareTaskMetricsStat.

        所有评估的最小延迟（秒）。

        :param min_latency_s: The min_latency_s of this CompareTaskMetricsStat.
        :type min_latency_s: int
        """
        self._min_latency_s = min_latency_s

    @property
    def min_input_token(self):
        r"""Gets the min_input_token of this CompareTaskMetricsStat.

        所有评估的最小输入token数。

        :return: The min_input_token of this CompareTaskMetricsStat.
        :rtype: int
        """
        return self._min_input_token

    @min_input_token.setter
    def min_input_token(self, min_input_token):
        r"""Sets the min_input_token of this CompareTaskMetricsStat.

        所有评估的最小输入token数。

        :param min_input_token: The min_input_token of this CompareTaskMetricsStat.
        :type min_input_token: int
        """
        self._min_input_token = min_input_token

    @property
    def min_output_token(self):
        r"""Gets the min_output_token of this CompareTaskMetricsStat.

        所有评估的最小输出token数。

        :return: The min_output_token of this CompareTaskMetricsStat.
        :rtype: int
        """
        return self._min_output_token

    @min_output_token.setter
    def min_output_token(self, min_output_token):
        r"""Sets the min_output_token of this CompareTaskMetricsStat.

        所有评估的最小输出token数。

        :param min_output_token: The min_output_token of this CompareTaskMetricsStat.
        :type min_output_token: int
        """
        self._min_output_token = min_output_token

    @property
    def min_total_token(self):
        r"""Gets the min_total_token of this CompareTaskMetricsStat.

        所有评估的最小总token数。

        :return: The min_total_token of this CompareTaskMetricsStat.
        :rtype: int
        """
        return self._min_total_token

    @min_total_token.setter
    def min_total_token(self, min_total_token):
        r"""Sets the min_total_token of this CompareTaskMetricsStat.

        所有评估的最小总token数。

        :param min_total_token: The min_total_token of this CompareTaskMetricsStat.
        :type min_total_token: int
        """
        self._min_total_token = min_total_token

    @property
    def sum_score(self):
        r"""Gets the sum_score of this CompareTaskMetricsStat.

        所有评估的得分总和。

        :return: The sum_score of this CompareTaskMetricsStat.
        :rtype: float
        """
        return self._sum_score

    @sum_score.setter
    def sum_score(self, sum_score):
        r"""Sets the sum_score of this CompareTaskMetricsStat.

        所有评估的得分总和。

        :param sum_score: The sum_score of this CompareTaskMetricsStat.
        :type sum_score: float
        """
        self._sum_score = sum_score

    @property
    def sum_latency_s(self):
        r"""Gets the sum_latency_s of this CompareTaskMetricsStat.

        所有评估的延迟总和（秒）。

        :return: The sum_latency_s of this CompareTaskMetricsStat.
        :rtype: int
        """
        return self._sum_latency_s

    @sum_latency_s.setter
    def sum_latency_s(self, sum_latency_s):
        r"""Sets the sum_latency_s of this CompareTaskMetricsStat.

        所有评估的延迟总和（秒）。

        :param sum_latency_s: The sum_latency_s of this CompareTaskMetricsStat.
        :type sum_latency_s: int
        """
        self._sum_latency_s = sum_latency_s

    @property
    def sum_input_token(self):
        r"""Gets the sum_input_token of this CompareTaskMetricsStat.

        所有评估的输入token总和。

        :return: The sum_input_token of this CompareTaskMetricsStat.
        :rtype: int
        """
        return self._sum_input_token

    @sum_input_token.setter
    def sum_input_token(self, sum_input_token):
        r"""Sets the sum_input_token of this CompareTaskMetricsStat.

        所有评估的输入token总和。

        :param sum_input_token: The sum_input_token of this CompareTaskMetricsStat.
        :type sum_input_token: int
        """
        self._sum_input_token = sum_input_token

    @property
    def sum_output_token(self):
        r"""Gets the sum_output_token of this CompareTaskMetricsStat.

        所有评估的输出token总和。

        :return: The sum_output_token of this CompareTaskMetricsStat.
        :rtype: int
        """
        return self._sum_output_token

    @sum_output_token.setter
    def sum_output_token(self, sum_output_token):
        r"""Sets the sum_output_token of this CompareTaskMetricsStat.

        所有评估的输出token总和。

        :param sum_output_token: The sum_output_token of this CompareTaskMetricsStat.
        :type sum_output_token: int
        """
        self._sum_output_token = sum_output_token

    @property
    def sum_total_token(self):
        r"""Gets the sum_total_token of this CompareTaskMetricsStat.

        所有评估的总token总和。

        :return: The sum_total_token of this CompareTaskMetricsStat.
        :rtype: int
        """
        return self._sum_total_token

    @sum_total_token.setter
    def sum_total_token(self, sum_total_token):
        r"""Sets the sum_total_token of this CompareTaskMetricsStat.

        所有评估的总token总和。

        :param sum_total_token: The sum_total_token of this CompareTaskMetricsStat.
        :type sum_total_token: int
        """
        self._sum_total_token = sum_total_token

    @property
    def score_stats(self):
        r"""Gets the score_stats of this CompareTaskMetricsStat.

        :return: The score_stats of this CompareTaskMetricsStat.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CompareScoreStats`
        """
        return self._score_stats

    @score_stats.setter
    def score_stats(self, score_stats):
        r"""Sets the score_stats of this CompareTaskMetricsStat.

        :param score_stats: The score_stats of this CompareTaskMetricsStat.
        :type score_stats: :class:`huaweicloudsdkagentarts.v1.CompareScoreStats`
        """
        self._score_stats = score_stats

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
        if not isinstance(other, CompareTaskMetricsStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
