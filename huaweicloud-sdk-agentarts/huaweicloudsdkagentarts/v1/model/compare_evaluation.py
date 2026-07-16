# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareEvaluation:

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
        'evaluator_version': 'str',
        'score': 'float',
        'reason': 'str',
        'latency_s': 'int',
        'status_code': 'str',
        'error': 'str',
        'input_token_usage': 'int',
        'output_token_usage': 'int',
        'correction': 'dict(str, object)',
        'retry_count': 'int',
        'created_at': 'datetime',
        'evaluator_name': 'str'
    }

    attribute_map = {
        'evaluator_id': 'evaluator_id',
        'evaluator_version': 'evaluator_version',
        'score': 'score',
        'reason': 'reason',
        'latency_s': 'latency_s',
        'status_code': 'status_code',
        'error': 'error',
        'input_token_usage': 'input_token_usage',
        'output_token_usage': 'output_token_usage',
        'correction': 'correction',
        'retry_count': 'retry_count',
        'created_at': 'created_at',
        'evaluator_name': 'evaluator_name'
    }

    def __init__(self, evaluator_id=None, evaluator_version=None, score=None, reason=None, latency_s=None, status_code=None, error=None, input_token_usage=None, output_token_usage=None, correction=None, retry_count=None, created_at=None, evaluator_name=None):
        r"""CompareEvaluation

        The model defined in huaweicloud sdk

        :param evaluator_id: 评估器的唯一标识符，如TaskCompletion、TurnRelevancy等。
        :type evaluator_id: str
        :param evaluator_version: 评估器的版本号，如“1.0.0”。
        :type evaluator_version: str
        :param score: 评估得分，通常在0到1之间；若评估失败，该值可能为0。
        :type score: float
        :param reason: 评估得分的详细理由文本，失败时可为空字符串。
        :type reason: str
        :param latency_s: 评估器执行的耗时，单位为秒。
        :type latency_s: int
        :param status_code: 评估执行状态：SUCCESS表示成功，FAILED表示失败（如超时、网络错误等）。
        :type status_code: str
        :param error: 失败时的详细错误信息；成功时为空字符串。
        :type error: str
        :param input_token_usage: 评估器处理输入时消耗的 token 数量。
        :type input_token_usage: int
        :param output_token_usage: 评估器生成输出时消耗的 token 数量。
        :type output_token_usage: int
        :param correction: 纠正信息字段，通常为null；预留用于自动纠错或人工校正结果。
        :type correction: dict(str, object)
        :param retry_count: 评估器失败后重试的次数。
        :type retry_count: int
        :param created_at: 评估记录创建时间，ISO 8601格式（UTC）。
        :type created_at: datetime
        :param evaluator_name: 评估器的人类可读名称，如“任务完成度”、“相关性”。
        :type evaluator_name: str
        """
        
        

        self._evaluator_id = None
        self._evaluator_version = None
        self._score = None
        self._reason = None
        self._latency_s = None
        self._status_code = None
        self._error = None
        self._input_token_usage = None
        self._output_token_usage = None
        self._correction = None
        self._retry_count = None
        self._created_at = None
        self._evaluator_name = None
        self.discriminator = None

        if evaluator_id is not None:
            self.evaluator_id = evaluator_id
        if evaluator_version is not None:
            self.evaluator_version = evaluator_version
        if score is not None:
            self.score = score
        if reason is not None:
            self.reason = reason
        if latency_s is not None:
            self.latency_s = latency_s
        if status_code is not None:
            self.status_code = status_code
        if error is not None:
            self.error = error
        if input_token_usage is not None:
            self.input_token_usage = input_token_usage
        if output_token_usage is not None:
            self.output_token_usage = output_token_usage
        if correction is not None:
            self.correction = correction
        if retry_count is not None:
            self.retry_count = retry_count
        if created_at is not None:
            self.created_at = created_at
        if evaluator_name is not None:
            self.evaluator_name = evaluator_name

    @property
    def evaluator_id(self):
        r"""Gets the evaluator_id of this CompareEvaluation.

        评估器的唯一标识符，如TaskCompletion、TurnRelevancy等。

        :return: The evaluator_id of this CompareEvaluation.
        :rtype: str
        """
        return self._evaluator_id

    @evaluator_id.setter
    def evaluator_id(self, evaluator_id):
        r"""Sets the evaluator_id of this CompareEvaluation.

        评估器的唯一标识符，如TaskCompletion、TurnRelevancy等。

        :param evaluator_id: The evaluator_id of this CompareEvaluation.
        :type evaluator_id: str
        """
        self._evaluator_id = evaluator_id

    @property
    def evaluator_version(self):
        r"""Gets the evaluator_version of this CompareEvaluation.

        评估器的版本号，如“1.0.0”。

        :return: The evaluator_version of this CompareEvaluation.
        :rtype: str
        """
        return self._evaluator_version

    @evaluator_version.setter
    def evaluator_version(self, evaluator_version):
        r"""Sets the evaluator_version of this CompareEvaluation.

        评估器的版本号，如“1.0.0”。

        :param evaluator_version: The evaluator_version of this CompareEvaluation.
        :type evaluator_version: str
        """
        self._evaluator_version = evaluator_version

    @property
    def score(self):
        r"""Gets the score of this CompareEvaluation.

        评估得分，通常在0到1之间；若评估失败，该值可能为0。

        :return: The score of this CompareEvaluation.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this CompareEvaluation.

        评估得分，通常在0到1之间；若评估失败，该值可能为0。

        :param score: The score of this CompareEvaluation.
        :type score: float
        """
        self._score = score

    @property
    def reason(self):
        r"""Gets the reason of this CompareEvaluation.

        评估得分的详细理由文本，失败时可为空字符串。

        :return: The reason of this CompareEvaluation.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this CompareEvaluation.

        评估得分的详细理由文本，失败时可为空字符串。

        :param reason: The reason of this CompareEvaluation.
        :type reason: str
        """
        self._reason = reason

    @property
    def latency_s(self):
        r"""Gets the latency_s of this CompareEvaluation.

        评估器执行的耗时，单位为秒。

        :return: The latency_s of this CompareEvaluation.
        :rtype: int
        """
        return self._latency_s

    @latency_s.setter
    def latency_s(self, latency_s):
        r"""Sets the latency_s of this CompareEvaluation.

        评估器执行的耗时，单位为秒。

        :param latency_s: The latency_s of this CompareEvaluation.
        :type latency_s: int
        """
        self._latency_s = latency_s

    @property
    def status_code(self):
        r"""Gets the status_code of this CompareEvaluation.

        评估执行状态：SUCCESS表示成功，FAILED表示失败（如超时、网络错误等）。

        :return: The status_code of this CompareEvaluation.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this CompareEvaluation.

        评估执行状态：SUCCESS表示成功，FAILED表示失败（如超时、网络错误等）。

        :param status_code: The status_code of this CompareEvaluation.
        :type status_code: str
        """
        self._status_code = status_code

    @property
    def error(self):
        r"""Gets the error of this CompareEvaluation.

        失败时的详细错误信息；成功时为空字符串。

        :return: The error of this CompareEvaluation.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this CompareEvaluation.

        失败时的详细错误信息；成功时为空字符串。

        :param error: The error of this CompareEvaluation.
        :type error: str
        """
        self._error = error

    @property
    def input_token_usage(self):
        r"""Gets the input_token_usage of this CompareEvaluation.

        评估器处理输入时消耗的 token 数量。

        :return: The input_token_usage of this CompareEvaluation.
        :rtype: int
        """
        return self._input_token_usage

    @input_token_usage.setter
    def input_token_usage(self, input_token_usage):
        r"""Sets the input_token_usage of this CompareEvaluation.

        评估器处理输入时消耗的 token 数量。

        :param input_token_usage: The input_token_usage of this CompareEvaluation.
        :type input_token_usage: int
        """
        self._input_token_usage = input_token_usage

    @property
    def output_token_usage(self):
        r"""Gets the output_token_usage of this CompareEvaluation.

        评估器生成输出时消耗的 token 数量。

        :return: The output_token_usage of this CompareEvaluation.
        :rtype: int
        """
        return self._output_token_usage

    @output_token_usage.setter
    def output_token_usage(self, output_token_usage):
        r"""Sets the output_token_usage of this CompareEvaluation.

        评估器生成输出时消耗的 token 数量。

        :param output_token_usage: The output_token_usage of this CompareEvaluation.
        :type output_token_usage: int
        """
        self._output_token_usage = output_token_usage

    @property
    def correction(self):
        r"""Gets the correction of this CompareEvaluation.

        纠正信息字段，通常为null；预留用于自动纠错或人工校正结果。

        :return: The correction of this CompareEvaluation.
        :rtype: dict(str, object)
        """
        return self._correction

    @correction.setter
    def correction(self, correction):
        r"""Sets the correction of this CompareEvaluation.

        纠正信息字段，通常为null；预留用于自动纠错或人工校正结果。

        :param correction: The correction of this CompareEvaluation.
        :type correction: dict(str, object)
        """
        self._correction = correction

    @property
    def retry_count(self):
        r"""Gets the retry_count of this CompareEvaluation.

        评估器失败后重试的次数。

        :return: The retry_count of this CompareEvaluation.
        :rtype: int
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        r"""Sets the retry_count of this CompareEvaluation.

        评估器失败后重试的次数。

        :param retry_count: The retry_count of this CompareEvaluation.
        :type retry_count: int
        """
        self._retry_count = retry_count

    @property
    def created_at(self):
        r"""Gets the created_at of this CompareEvaluation.

        评估记录创建时间，ISO 8601格式（UTC）。

        :return: The created_at of this CompareEvaluation.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CompareEvaluation.

        评估记录创建时间，ISO 8601格式（UTC）。

        :param created_at: The created_at of this CompareEvaluation.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def evaluator_name(self):
        r"""Gets the evaluator_name of this CompareEvaluation.

        评估器的人类可读名称，如“任务完成度”、“相关性”。

        :return: The evaluator_name of this CompareEvaluation.
        :rtype: str
        """
        return self._evaluator_name

    @evaluator_name.setter
    def evaluator_name(self, evaluator_name):
        r"""Sets the evaluator_name of this CompareEvaluation.

        评估器的人类可读名称，如“任务完成度”、“相关性”。

        :param evaluator_name: The evaluator_name of this CompareEvaluation.
        :type evaluator_name: str
        """
        self._evaluator_name = evaluator_name

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
        if not isinstance(other, CompareEvaluation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
