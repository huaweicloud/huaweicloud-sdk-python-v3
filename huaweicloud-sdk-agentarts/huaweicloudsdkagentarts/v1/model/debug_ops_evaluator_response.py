# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugOpsEvaluatorResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status_code': 'int',
        'error': 'str',
        'score': 'int',
        'reason': 'str',
        'input_token_usage': 'int',
        'output_token_usage': 'int',
        'latency': 'int',
        'id': 'str',
        'account_id': 'str',
        'task_id': 'str',
        'item_id': 'str',
        'session_id': 'str',
        'evaluator_id': 'str',
        'evaluator_version': 'str',
        'evaluator_type': 'int',
        'evaluator_turn_type': 'str',
        'evaluator_content_type': 'str',
        'is_free': 'bool'
    }

    attribute_map = {
        'status_code': 'status_code',
        'error': 'error',
        'score': 'score',
        'reason': 'reason',
        'input_token_usage': 'input_token_usage',
        'output_token_usage': 'output_token_usage',
        'latency': 'latency',
        'id': 'id',
        'account_id': 'account_id',
        'task_id': 'task_id',
        'item_id': 'item_id',
        'session_id': 'session_id',
        'evaluator_id': 'evaluator_id',
        'evaluator_version': 'evaluator_version',
        'evaluator_type': 'evaluator_type',
        'evaluator_turn_type': 'evaluator_turn_type',
        'evaluator_content_type': 'evaluator_content_type',
        'is_free': 'is_free'
    }

    def __init__(self, status_code=None, error=None, score=None, reason=None, input_token_usage=None, output_token_usage=None, latency=None, id=None, account_id=None, task_id=None, item_id=None, session_id=None, evaluator_id=None, evaluator_version=None, evaluator_type=None, evaluator_turn_type=None, evaluator_content_type=None, is_free=None):
        r"""DebugOpsEvaluatorResponse

        The model defined in huaweicloud sdk

        :param status_code: **参数解释：** 调试执行的状态码。 **取值范围：** 遵循 HTTP 状态码或自定义业务状态码。 
        :type status_code: int
        :param error: **参数解释：** 调试过程中产生的错误详细信息。 **取值范围：** 描述性错误字符串。 
        :type error: str
        :param score: **参数解释：** 评估器根据当前输入调试出的评分结果。 **取值范围：** 按评估逻辑定义的评分区间返回。 
        :type score: int
        :param reason: **参数解释：** 评估结果的详细理由或推导过程。 **取值范围：** 详细的描述性文本。 
        :type reason: str
        :param input_token_usage: **参数解释：** 调试请求中输入内容消耗的Token数量。 **取值范围：** 0到2,147,483,647之间的整数。 
        :type input_token_usage: int
        :param output_token_usage: **参数解释：** 调试请求中输出内容消耗的Token数量。 **取值范围：** 0到2,147,483,647之间的整数。 
        :type output_token_usage: int
        :param latency: **参数解释：** 本次调试操作的耗时。 **取值范围：** 0 - 2,147,483,647 之间的整数。 
        :type latency: int
        :param id: **参数解释：** 评估结果记录ID。 
        :type id: str
        :param account_id: **参数解释：** 租户账号ID。 
        :type account_id: str
        :param task_id: **参数解释：** 任务ID。 
        :type task_id: str
        :param item_id: **参数解释：** 条目ID。 
        :type item_id: str
        :param session_id: **参数解释：** 会话ID。 
        :type session_id: str
        :param evaluator_id: **参数解释：** 评估器ID。 
        :type evaluator_id: str
        :param evaluator_version: **参数解释：** 评估器版本号。 
        :type evaluator_version: str
        :param evaluator_type: **参数解释：** 评估器类型。 
        :type evaluator_type: int
        :param evaluator_turn_type: **参数解释：** 评估器轮次类型。 
        :type evaluator_turn_type: str
        :param evaluator_content_type: **参数解释：** 评估内容类型。 
        :type evaluator_content_type: str
        :param is_free: **参数解释：** 是否免费任务。 
        :type is_free: bool
        """
        
        super().__init__()

        self._status_code = None
        self._error = None
        self._score = None
        self._reason = None
        self._input_token_usage = None
        self._output_token_usage = None
        self._latency = None
        self._id = None
        self._account_id = None
        self._task_id = None
        self._item_id = None
        self._session_id = None
        self._evaluator_id = None
        self._evaluator_version = None
        self._evaluator_type = None
        self._evaluator_turn_type = None
        self._evaluator_content_type = None
        self._is_free = None
        self.discriminator = None

        if status_code is not None:
            self.status_code = status_code
        if error is not None:
            self.error = error
        if score is not None:
            self.score = score
        if reason is not None:
            self.reason = reason
        if input_token_usage is not None:
            self.input_token_usage = input_token_usage
        if output_token_usage is not None:
            self.output_token_usage = output_token_usage
        if latency is not None:
            self.latency = latency
        if id is not None:
            self.id = id
        if account_id is not None:
            self.account_id = account_id
        if task_id is not None:
            self.task_id = task_id
        if item_id is not None:
            self.item_id = item_id
        if session_id is not None:
            self.session_id = session_id
        if evaluator_id is not None:
            self.evaluator_id = evaluator_id
        if evaluator_version is not None:
            self.evaluator_version = evaluator_version
        if evaluator_type is not None:
            self.evaluator_type = evaluator_type
        if evaluator_turn_type is not None:
            self.evaluator_turn_type = evaluator_turn_type
        if evaluator_content_type is not None:
            self.evaluator_content_type = evaluator_content_type
        if is_free is not None:
            self.is_free = is_free

    @property
    def status_code(self):
        r"""Gets the status_code of this DebugOpsEvaluatorResponse.

        **参数解释：** 调试执行的状态码。 **取值范围：** 遵循 HTTP 状态码或自定义业务状态码。 

        :return: The status_code of this DebugOpsEvaluatorResponse.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this DebugOpsEvaluatorResponse.

        **参数解释：** 调试执行的状态码。 **取值范围：** 遵循 HTTP 状态码或自定义业务状态码。 

        :param status_code: The status_code of this DebugOpsEvaluatorResponse.
        :type status_code: int
        """
        self._status_code = status_code

    @property
    def error(self):
        r"""Gets the error of this DebugOpsEvaluatorResponse.

        **参数解释：** 调试过程中产生的错误详细信息。 **取值范围：** 描述性错误字符串。 

        :return: The error of this DebugOpsEvaluatorResponse.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this DebugOpsEvaluatorResponse.

        **参数解释：** 调试过程中产生的错误详细信息。 **取值范围：** 描述性错误字符串。 

        :param error: The error of this DebugOpsEvaluatorResponse.
        :type error: str
        """
        self._error = error

    @property
    def score(self):
        r"""Gets the score of this DebugOpsEvaluatorResponse.

        **参数解释：** 评估器根据当前输入调试出的评分结果。 **取值范围：** 按评估逻辑定义的评分区间返回。 

        :return: The score of this DebugOpsEvaluatorResponse.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this DebugOpsEvaluatorResponse.

        **参数解释：** 评估器根据当前输入调试出的评分结果。 **取值范围：** 按评估逻辑定义的评分区间返回。 

        :param score: The score of this DebugOpsEvaluatorResponse.
        :type score: int
        """
        self._score = score

    @property
    def reason(self):
        r"""Gets the reason of this DebugOpsEvaluatorResponse.

        **参数解释：** 评估结果的详细理由或推导过程。 **取值范围：** 详细的描述性文本。 

        :return: The reason of this DebugOpsEvaluatorResponse.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this DebugOpsEvaluatorResponse.

        **参数解释：** 评估结果的详细理由或推导过程。 **取值范围：** 详细的描述性文本。 

        :param reason: The reason of this DebugOpsEvaluatorResponse.
        :type reason: str
        """
        self._reason = reason

    @property
    def input_token_usage(self):
        r"""Gets the input_token_usage of this DebugOpsEvaluatorResponse.

        **参数解释：** 调试请求中输入内容消耗的Token数量。 **取值范围：** 0到2,147,483,647之间的整数。 

        :return: The input_token_usage of this DebugOpsEvaluatorResponse.
        :rtype: int
        """
        return self._input_token_usage

    @input_token_usage.setter
    def input_token_usage(self, input_token_usage):
        r"""Sets the input_token_usage of this DebugOpsEvaluatorResponse.

        **参数解释：** 调试请求中输入内容消耗的Token数量。 **取值范围：** 0到2,147,483,647之间的整数。 

        :param input_token_usage: The input_token_usage of this DebugOpsEvaluatorResponse.
        :type input_token_usage: int
        """
        self._input_token_usage = input_token_usage

    @property
    def output_token_usage(self):
        r"""Gets the output_token_usage of this DebugOpsEvaluatorResponse.

        **参数解释：** 调试请求中输出内容消耗的Token数量。 **取值范围：** 0到2,147,483,647之间的整数。 

        :return: The output_token_usage of this DebugOpsEvaluatorResponse.
        :rtype: int
        """
        return self._output_token_usage

    @output_token_usage.setter
    def output_token_usage(self, output_token_usage):
        r"""Sets the output_token_usage of this DebugOpsEvaluatorResponse.

        **参数解释：** 调试请求中输出内容消耗的Token数量。 **取值范围：** 0到2,147,483,647之间的整数。 

        :param output_token_usage: The output_token_usage of this DebugOpsEvaluatorResponse.
        :type output_token_usage: int
        """
        self._output_token_usage = output_token_usage

    @property
    def latency(self):
        r"""Gets the latency of this DebugOpsEvaluatorResponse.

        **参数解释：** 本次调试操作的耗时。 **取值范围：** 0 - 2,147,483,647 之间的整数。 

        :return: The latency of this DebugOpsEvaluatorResponse.
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        r"""Sets the latency of this DebugOpsEvaluatorResponse.

        **参数解释：** 本次调试操作的耗时。 **取值范围：** 0 - 2,147,483,647 之间的整数。 

        :param latency: The latency of this DebugOpsEvaluatorResponse.
        :type latency: int
        """
        self._latency = latency

    @property
    def id(self):
        r"""Gets the id of this DebugOpsEvaluatorResponse.

        **参数解释：** 评估结果记录ID。 

        :return: The id of this DebugOpsEvaluatorResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DebugOpsEvaluatorResponse.

        **参数解释：** 评估结果记录ID。 

        :param id: The id of this DebugOpsEvaluatorResponse.
        :type id: str
        """
        self._id = id

    @property
    def account_id(self):
        r"""Gets the account_id of this DebugOpsEvaluatorResponse.

        **参数解释：** 租户账号ID。 

        :return: The account_id of this DebugOpsEvaluatorResponse.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this DebugOpsEvaluatorResponse.

        **参数解释：** 租户账号ID。 

        :param account_id: The account_id of this DebugOpsEvaluatorResponse.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def task_id(self):
        r"""Gets the task_id of this DebugOpsEvaluatorResponse.

        **参数解释：** 任务ID。 

        :return: The task_id of this DebugOpsEvaluatorResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this DebugOpsEvaluatorResponse.

        **参数解释：** 任务ID。 

        :param task_id: The task_id of this DebugOpsEvaluatorResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def item_id(self):
        r"""Gets the item_id of this DebugOpsEvaluatorResponse.

        **参数解释：** 条目ID。 

        :return: The item_id of this DebugOpsEvaluatorResponse.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        r"""Sets the item_id of this DebugOpsEvaluatorResponse.

        **参数解释：** 条目ID。 

        :param item_id: The item_id of this DebugOpsEvaluatorResponse.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def session_id(self):
        r"""Gets the session_id of this DebugOpsEvaluatorResponse.

        **参数解释：** 会话ID。 

        :return: The session_id of this DebugOpsEvaluatorResponse.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this DebugOpsEvaluatorResponse.

        **参数解释：** 会话ID。 

        :param session_id: The session_id of this DebugOpsEvaluatorResponse.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def evaluator_id(self):
        r"""Gets the evaluator_id of this DebugOpsEvaluatorResponse.

        **参数解释：** 评估器ID。 

        :return: The evaluator_id of this DebugOpsEvaluatorResponse.
        :rtype: str
        """
        return self._evaluator_id

    @evaluator_id.setter
    def evaluator_id(self, evaluator_id):
        r"""Sets the evaluator_id of this DebugOpsEvaluatorResponse.

        **参数解释：** 评估器ID。 

        :param evaluator_id: The evaluator_id of this DebugOpsEvaluatorResponse.
        :type evaluator_id: str
        """
        self._evaluator_id = evaluator_id

    @property
    def evaluator_version(self):
        r"""Gets the evaluator_version of this DebugOpsEvaluatorResponse.

        **参数解释：** 评估器版本号。 

        :return: The evaluator_version of this DebugOpsEvaluatorResponse.
        :rtype: str
        """
        return self._evaluator_version

    @evaluator_version.setter
    def evaluator_version(self, evaluator_version):
        r"""Sets the evaluator_version of this DebugOpsEvaluatorResponse.

        **参数解释：** 评估器版本号。 

        :param evaluator_version: The evaluator_version of this DebugOpsEvaluatorResponse.
        :type evaluator_version: str
        """
        self._evaluator_version = evaluator_version

    @property
    def evaluator_type(self):
        r"""Gets the evaluator_type of this DebugOpsEvaluatorResponse.

        **参数解释：** 评估器类型。 

        :return: The evaluator_type of this DebugOpsEvaluatorResponse.
        :rtype: int
        """
        return self._evaluator_type

    @evaluator_type.setter
    def evaluator_type(self, evaluator_type):
        r"""Sets the evaluator_type of this DebugOpsEvaluatorResponse.

        **参数解释：** 评估器类型。 

        :param evaluator_type: The evaluator_type of this DebugOpsEvaluatorResponse.
        :type evaluator_type: int
        """
        self._evaluator_type = evaluator_type

    @property
    def evaluator_turn_type(self):
        r"""Gets the evaluator_turn_type of this DebugOpsEvaluatorResponse.

        **参数解释：** 评估器轮次类型。 

        :return: The evaluator_turn_type of this DebugOpsEvaluatorResponse.
        :rtype: str
        """
        return self._evaluator_turn_type

    @evaluator_turn_type.setter
    def evaluator_turn_type(self, evaluator_turn_type):
        r"""Sets the evaluator_turn_type of this DebugOpsEvaluatorResponse.

        **参数解释：** 评估器轮次类型。 

        :param evaluator_turn_type: The evaluator_turn_type of this DebugOpsEvaluatorResponse.
        :type evaluator_turn_type: str
        """
        self._evaluator_turn_type = evaluator_turn_type

    @property
    def evaluator_content_type(self):
        r"""Gets the evaluator_content_type of this DebugOpsEvaluatorResponse.

        **参数解释：** 评估内容类型。 

        :return: The evaluator_content_type of this DebugOpsEvaluatorResponse.
        :rtype: str
        """
        return self._evaluator_content_type

    @evaluator_content_type.setter
    def evaluator_content_type(self, evaluator_content_type):
        r"""Sets the evaluator_content_type of this DebugOpsEvaluatorResponse.

        **参数解释：** 评估内容类型。 

        :param evaluator_content_type: The evaluator_content_type of this DebugOpsEvaluatorResponse.
        :type evaluator_content_type: str
        """
        self._evaluator_content_type = evaluator_content_type

    @property
    def is_free(self):
        r"""Gets the is_free of this DebugOpsEvaluatorResponse.

        **参数解释：** 是否免费任务。 

        :return: The is_free of this DebugOpsEvaluatorResponse.
        :rtype: bool
        """
        return self._is_free

    @is_free.setter
    def is_free(self, is_free):
        r"""Sets the is_free of this DebugOpsEvaluatorResponse.

        **参数解释：** 是否免费任务。 

        :param is_free: The is_free of this DebugOpsEvaluatorResponse.
        :type is_free: bool
        """
        self._is_free = is_free

    def to_dict(self):
        import warnings
        warnings.warn("DebugOpsEvaluatorResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, DebugOpsEvaluatorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
