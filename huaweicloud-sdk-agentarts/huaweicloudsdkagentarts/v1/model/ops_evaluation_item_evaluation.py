# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsEvaluationItemEvaluation:

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
        'evaluator_name': 'str',
        'score': 'float',
        'reason': 'str',
        'latency_s': 'int',
        'status_code': 'str',
        'error': 'str',
        'retry_count': 'int',
        'created_at': 'datetime',
        'correction': 'object'
    }

    attribute_map = {
        'evaluator_id': 'evaluator_id',
        'evaluator_version': 'evaluator_version',
        'evaluator_name': 'evaluator_name',
        'score': 'score',
        'reason': 'reason',
        'latency_s': 'latency_s',
        'status_code': 'status_code',
        'error': 'error',
        'retry_count': 'retry_count',
        'created_at': 'created_at',
        'correction': 'correction'
    }

    def __init__(self, evaluator_id=None, evaluator_version=None, evaluator_name=None, score=None, reason=None, latency_s=None, status_code=None, error=None, retry_count=None, created_at=None, correction=None):
        r"""OpsEvaluationItemEvaluation

        The model defined in huaweicloud sdk

        :param evaluator_id: 评估器ID。
        :type evaluator_id: str
        :param evaluator_version: 评估器版本。
        :type evaluator_version: str
        :param evaluator_name: 评估器名称。
        :type evaluator_name: str
        :param score: 评估得分。
        :type score: float
        :param reason: 评估理由。
        :type reason: str
        :param latency_s: 评估耗时（秒）。
        :type latency_s: int
        :param status_code: 评估状态码。
        :type status_code: str
        :param error: 错误信息。
        :type error: str
        :param retry_count: 重试次数。
        :type retry_count: int
        :param created_at: 评估时间。
        :type created_at: datetime
        :param correction: 人工校正信息。
        :type correction: object
        """
        
        

        self._evaluator_id = None
        self._evaluator_version = None
        self._evaluator_name = None
        self._score = None
        self._reason = None
        self._latency_s = None
        self._status_code = None
        self._error = None
        self._retry_count = None
        self._created_at = None
        self._correction = None
        self.discriminator = None

        if evaluator_id is not None:
            self.evaluator_id = evaluator_id
        if evaluator_version is not None:
            self.evaluator_version = evaluator_version
        if evaluator_name is not None:
            self.evaluator_name = evaluator_name
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
        if retry_count is not None:
            self.retry_count = retry_count
        if created_at is not None:
            self.created_at = created_at
        if correction is not None:
            self.correction = correction

    @property
    def evaluator_id(self):
        r"""Gets the evaluator_id of this OpsEvaluationItemEvaluation.

        评估器ID。

        :return: The evaluator_id of this OpsEvaluationItemEvaluation.
        :rtype: str
        """
        return self._evaluator_id

    @evaluator_id.setter
    def evaluator_id(self, evaluator_id):
        r"""Sets the evaluator_id of this OpsEvaluationItemEvaluation.

        评估器ID。

        :param evaluator_id: The evaluator_id of this OpsEvaluationItemEvaluation.
        :type evaluator_id: str
        """
        self._evaluator_id = evaluator_id

    @property
    def evaluator_version(self):
        r"""Gets the evaluator_version of this OpsEvaluationItemEvaluation.

        评估器版本。

        :return: The evaluator_version of this OpsEvaluationItemEvaluation.
        :rtype: str
        """
        return self._evaluator_version

    @evaluator_version.setter
    def evaluator_version(self, evaluator_version):
        r"""Sets the evaluator_version of this OpsEvaluationItemEvaluation.

        评估器版本。

        :param evaluator_version: The evaluator_version of this OpsEvaluationItemEvaluation.
        :type evaluator_version: str
        """
        self._evaluator_version = evaluator_version

    @property
    def evaluator_name(self):
        r"""Gets the evaluator_name of this OpsEvaluationItemEvaluation.

        评估器名称。

        :return: The evaluator_name of this OpsEvaluationItemEvaluation.
        :rtype: str
        """
        return self._evaluator_name

    @evaluator_name.setter
    def evaluator_name(self, evaluator_name):
        r"""Sets the evaluator_name of this OpsEvaluationItemEvaluation.

        评估器名称。

        :param evaluator_name: The evaluator_name of this OpsEvaluationItemEvaluation.
        :type evaluator_name: str
        """
        self._evaluator_name = evaluator_name

    @property
    def score(self):
        r"""Gets the score of this OpsEvaluationItemEvaluation.

        评估得分。

        :return: The score of this OpsEvaluationItemEvaluation.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this OpsEvaluationItemEvaluation.

        评估得分。

        :param score: The score of this OpsEvaluationItemEvaluation.
        :type score: float
        """
        self._score = score

    @property
    def reason(self):
        r"""Gets the reason of this OpsEvaluationItemEvaluation.

        评估理由。

        :return: The reason of this OpsEvaluationItemEvaluation.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this OpsEvaluationItemEvaluation.

        评估理由。

        :param reason: The reason of this OpsEvaluationItemEvaluation.
        :type reason: str
        """
        self._reason = reason

    @property
    def latency_s(self):
        r"""Gets the latency_s of this OpsEvaluationItemEvaluation.

        评估耗时（秒）。

        :return: The latency_s of this OpsEvaluationItemEvaluation.
        :rtype: int
        """
        return self._latency_s

    @latency_s.setter
    def latency_s(self, latency_s):
        r"""Sets the latency_s of this OpsEvaluationItemEvaluation.

        评估耗时（秒）。

        :param latency_s: The latency_s of this OpsEvaluationItemEvaluation.
        :type latency_s: int
        """
        self._latency_s = latency_s

    @property
    def status_code(self):
        r"""Gets the status_code of this OpsEvaluationItemEvaluation.

        评估状态码。

        :return: The status_code of this OpsEvaluationItemEvaluation.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this OpsEvaluationItemEvaluation.

        评估状态码。

        :param status_code: The status_code of this OpsEvaluationItemEvaluation.
        :type status_code: str
        """
        self._status_code = status_code

    @property
    def error(self):
        r"""Gets the error of this OpsEvaluationItemEvaluation.

        错误信息。

        :return: The error of this OpsEvaluationItemEvaluation.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this OpsEvaluationItemEvaluation.

        错误信息。

        :param error: The error of this OpsEvaluationItemEvaluation.
        :type error: str
        """
        self._error = error

    @property
    def retry_count(self):
        r"""Gets the retry_count of this OpsEvaluationItemEvaluation.

        重试次数。

        :return: The retry_count of this OpsEvaluationItemEvaluation.
        :rtype: int
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        r"""Sets the retry_count of this OpsEvaluationItemEvaluation.

        重试次数。

        :param retry_count: The retry_count of this OpsEvaluationItemEvaluation.
        :type retry_count: int
        """
        self._retry_count = retry_count

    @property
    def created_at(self):
        r"""Gets the created_at of this OpsEvaluationItemEvaluation.

        评估时间。

        :return: The created_at of this OpsEvaluationItemEvaluation.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this OpsEvaluationItemEvaluation.

        评估时间。

        :param created_at: The created_at of this OpsEvaluationItemEvaluation.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def correction(self):
        r"""Gets the correction of this OpsEvaluationItemEvaluation.

        人工校正信息。

        :return: The correction of this OpsEvaluationItemEvaluation.
        :rtype: object
        """
        return self._correction

    @correction.setter
    def correction(self, correction):
        r"""Sets the correction of this OpsEvaluationItemEvaluation.

        人工校正信息。

        :param correction: The correction of this OpsEvaluationItemEvaluation.
        :type correction: object
        """
        self._correction = correction

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
        if not isinstance(other, OpsEvaluationItemEvaluation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
