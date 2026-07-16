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
        'latency': 'int'
    }

    attribute_map = {
        'status_code': 'status_code',
        'error': 'error',
        'score': 'score',
        'reason': 'reason',
        'input_token_usage': 'input_token_usage',
        'output_token_usage': 'output_token_usage',
        'latency': 'latency'
    }

    def __init__(self, status_code=None, error=None, score=None, reason=None, input_token_usage=None, output_token_usage=None, latency=None):
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
        """
        
        super().__init__()

        self._status_code = None
        self._error = None
        self._score = None
        self._reason = None
        self._input_token_usage = None
        self._output_token_usage = None
        self._latency = None
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
