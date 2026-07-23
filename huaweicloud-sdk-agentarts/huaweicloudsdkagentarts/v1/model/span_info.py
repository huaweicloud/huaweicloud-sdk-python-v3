# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpanInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trace_id': 'str',
        'parent_span_id': 'str',
        'span_id': 'str',
        'span_type': 'str',
        'span_name': 'str',
        'status_code': 'str',
        'status_message': 'str',
        'input': 'str',
        'output': 'str',
        'duration': 'int',
        'session_id': 'str',
        'tokens': 'int',
        'input_tokens': 'int',
        'output_tokens': 'int',
        'start_time': 'int',
        'call_type': 'str',
        'metadata': 'str',
        'feedback_operation': 'str',
        'label': 'list[Label]',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'model_name': 'str',
        'is_error': 'bool'
    }

    attribute_map = {
        'trace_id': 'trace_id',
        'parent_span_id': 'parent_span_id',
        'span_id': 'span_id',
        'span_type': 'span_type',
        'span_name': 'span_name',
        'status_code': 'status_code',
        'status_message': 'status_message',
        'input': 'input',
        'output': 'output',
        'duration': 'duration',
        'session_id': 'session_id',
        'tokens': 'tokens',
        'input_tokens': 'input_tokens',
        'output_tokens': 'output_tokens',
        'start_time': 'start_time',
        'call_type': 'call_type',
        'metadata': 'metadata',
        'feedback_operation': 'feedback_operation',
        'label': 'label',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'model_name': 'model_name',
        'is_error': 'is_error'
    }

    def __init__(self, trace_id=None, parent_span_id=None, span_id=None, span_type=None, span_name=None, status_code=None, status_message=None, input=None, output=None, duration=None, session_id=None, tokens=None, input_tokens=None, output_tokens=None, start_time=None, call_type=None, metadata=None, feedback_operation=None, label=None, resource_id=None, resource_name=None, resource_type=None, model_name=None, is_error=None):
        r"""SpanInfo

        The model defined in huaweicloud sdk

        :param trace_id: trace id
        :type trace_id: str
        :param parent_span_id: 父span id
        :type parent_span_id: str
        :param span_id: spn id
        :type span_id: str
        :param span_type: span 类型
        :type span_type: str
        :param span_name: span名称
        :type span_name: str
        :param status_code: 状态码
        :type status_code: str
        :param status_message: 状态信息
        :type status_message: str
        :param input: 输入
        :type input: str
        :param output: 输出
        :type output: str
        :param duration: 时延
        :type duration: int
        :param session_id: 会话id
        :type session_id: str
        :param tokens: tokens消耗
        :type tokens: int
        :param input_tokens: 输入tokens
        :type input_tokens: int
        :param output_tokens: 输出tokens
        :type output_tokens: int
        :param start_time: 开始时间
        :type start_time: int
        :param call_type: 触发类型
        :type call_type: str
        :param metadata: 元数据
        :type metadata: str
        :param feedback_operation: 点赞点睬, cancel为未点赞，like为点赞，unlike为点睬
        :type feedback_operation: str
        :param label: label标签组
        :type label: list[:class:`huaweicloudsdkagentarts.v1.Label`]
        :param resource_id: 应用id
        :type resource_id: str
        :param resource_name: 应用名称
        :type resource_name: str
        :param resource_type: 应用类型
        :type resource_type: str
        :param model_name: 模型名称
        :type model_name: str
        :param is_error: 是否失败
        :type is_error: bool
        """
        
        

        self._trace_id = None
        self._parent_span_id = None
        self._span_id = None
        self._span_type = None
        self._span_name = None
        self._status_code = None
        self._status_message = None
        self._input = None
        self._output = None
        self._duration = None
        self._session_id = None
        self._tokens = None
        self._input_tokens = None
        self._output_tokens = None
        self._start_time = None
        self._call_type = None
        self._metadata = None
        self._feedback_operation = None
        self._label = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._model_name = None
        self._is_error = None
        self.discriminator = None

        if trace_id is not None:
            self.trace_id = trace_id
        if parent_span_id is not None:
            self.parent_span_id = parent_span_id
        if span_id is not None:
            self.span_id = span_id
        if span_type is not None:
            self.span_type = span_type
        if span_name is not None:
            self.span_name = span_name
        if status_code is not None:
            self.status_code = status_code
        if status_message is not None:
            self.status_message = status_message
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if duration is not None:
            self.duration = duration
        if session_id is not None:
            self.session_id = session_id
        if tokens is not None:
            self.tokens = tokens
        if input_tokens is not None:
            self.input_tokens = input_tokens
        if output_tokens is not None:
            self.output_tokens = output_tokens
        if start_time is not None:
            self.start_time = start_time
        if call_type is not None:
            self.call_type = call_type
        if metadata is not None:
            self.metadata = metadata
        if feedback_operation is not None:
            self.feedback_operation = feedback_operation
        if label is not None:
            self.label = label
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if model_name is not None:
            self.model_name = model_name
        if is_error is not None:
            self.is_error = is_error

    @property
    def trace_id(self):
        r"""Gets the trace_id of this SpanInfo.

        trace id

        :return: The trace_id of this SpanInfo.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this SpanInfo.

        trace id

        :param trace_id: The trace_id of this SpanInfo.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def parent_span_id(self):
        r"""Gets the parent_span_id of this SpanInfo.

        父span id

        :return: The parent_span_id of this SpanInfo.
        :rtype: str
        """
        return self._parent_span_id

    @parent_span_id.setter
    def parent_span_id(self, parent_span_id):
        r"""Sets the parent_span_id of this SpanInfo.

        父span id

        :param parent_span_id: The parent_span_id of this SpanInfo.
        :type parent_span_id: str
        """
        self._parent_span_id = parent_span_id

    @property
    def span_id(self):
        r"""Gets the span_id of this SpanInfo.

        spn id

        :return: The span_id of this SpanInfo.
        :rtype: str
        """
        return self._span_id

    @span_id.setter
    def span_id(self, span_id):
        r"""Sets the span_id of this SpanInfo.

        spn id

        :param span_id: The span_id of this SpanInfo.
        :type span_id: str
        """
        self._span_id = span_id

    @property
    def span_type(self):
        r"""Gets the span_type of this SpanInfo.

        span 类型

        :return: The span_type of this SpanInfo.
        :rtype: str
        """
        return self._span_type

    @span_type.setter
    def span_type(self, span_type):
        r"""Sets the span_type of this SpanInfo.

        span 类型

        :param span_type: The span_type of this SpanInfo.
        :type span_type: str
        """
        self._span_type = span_type

    @property
    def span_name(self):
        r"""Gets the span_name of this SpanInfo.

        span名称

        :return: The span_name of this SpanInfo.
        :rtype: str
        """
        return self._span_name

    @span_name.setter
    def span_name(self, span_name):
        r"""Sets the span_name of this SpanInfo.

        span名称

        :param span_name: The span_name of this SpanInfo.
        :type span_name: str
        """
        self._span_name = span_name

    @property
    def status_code(self):
        r"""Gets the status_code of this SpanInfo.

        状态码

        :return: The status_code of this SpanInfo.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this SpanInfo.

        状态码

        :param status_code: The status_code of this SpanInfo.
        :type status_code: str
        """
        self._status_code = status_code

    @property
    def status_message(self):
        r"""Gets the status_message of this SpanInfo.

        状态信息

        :return: The status_message of this SpanInfo.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        r"""Sets the status_message of this SpanInfo.

        状态信息

        :param status_message: The status_message of this SpanInfo.
        :type status_message: str
        """
        self._status_message = status_message

    @property
    def input(self):
        r"""Gets the input of this SpanInfo.

        输入

        :return: The input of this SpanInfo.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this SpanInfo.

        输入

        :param input: The input of this SpanInfo.
        :type input: str
        """
        self._input = input

    @property
    def output(self):
        r"""Gets the output of this SpanInfo.

        输出

        :return: The output of this SpanInfo.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this SpanInfo.

        输出

        :param output: The output of this SpanInfo.
        :type output: str
        """
        self._output = output

    @property
    def duration(self):
        r"""Gets the duration of this SpanInfo.

        时延

        :return: The duration of this SpanInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this SpanInfo.

        时延

        :param duration: The duration of this SpanInfo.
        :type duration: int
        """
        self._duration = duration

    @property
    def session_id(self):
        r"""Gets the session_id of this SpanInfo.

        会话id

        :return: The session_id of this SpanInfo.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this SpanInfo.

        会话id

        :param session_id: The session_id of this SpanInfo.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def tokens(self):
        r"""Gets the tokens of this SpanInfo.

        tokens消耗

        :return: The tokens of this SpanInfo.
        :rtype: int
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        r"""Sets the tokens of this SpanInfo.

        tokens消耗

        :param tokens: The tokens of this SpanInfo.
        :type tokens: int
        """
        self._tokens = tokens

    @property
    def input_tokens(self):
        r"""Gets the input_tokens of this SpanInfo.

        输入tokens

        :return: The input_tokens of this SpanInfo.
        :rtype: int
        """
        return self._input_tokens

    @input_tokens.setter
    def input_tokens(self, input_tokens):
        r"""Sets the input_tokens of this SpanInfo.

        输入tokens

        :param input_tokens: The input_tokens of this SpanInfo.
        :type input_tokens: int
        """
        self._input_tokens = input_tokens

    @property
    def output_tokens(self):
        r"""Gets the output_tokens of this SpanInfo.

        输出tokens

        :return: The output_tokens of this SpanInfo.
        :rtype: int
        """
        return self._output_tokens

    @output_tokens.setter
    def output_tokens(self, output_tokens):
        r"""Sets the output_tokens of this SpanInfo.

        输出tokens

        :param output_tokens: The output_tokens of this SpanInfo.
        :type output_tokens: int
        """
        self._output_tokens = output_tokens

    @property
    def start_time(self):
        r"""Gets the start_time of this SpanInfo.

        开始时间

        :return: The start_time of this SpanInfo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SpanInfo.

        开始时间

        :param start_time: The start_time of this SpanInfo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def call_type(self):
        r"""Gets the call_type of this SpanInfo.

        触发类型

        :return: The call_type of this SpanInfo.
        :rtype: str
        """
        return self._call_type

    @call_type.setter
    def call_type(self, call_type):
        r"""Sets the call_type of this SpanInfo.

        触发类型

        :param call_type: The call_type of this SpanInfo.
        :type call_type: str
        """
        self._call_type = call_type

    @property
    def metadata(self):
        r"""Gets the metadata of this SpanInfo.

        元数据

        :return: The metadata of this SpanInfo.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this SpanInfo.

        元数据

        :param metadata: The metadata of this SpanInfo.
        :type metadata: str
        """
        self._metadata = metadata

    @property
    def feedback_operation(self):
        r"""Gets the feedback_operation of this SpanInfo.

        点赞点睬, cancel为未点赞，like为点赞，unlike为点睬

        :return: The feedback_operation of this SpanInfo.
        :rtype: str
        """
        return self._feedback_operation

    @feedback_operation.setter
    def feedback_operation(self, feedback_operation):
        r"""Sets the feedback_operation of this SpanInfo.

        点赞点睬, cancel为未点赞，like为点赞，unlike为点睬

        :param feedback_operation: The feedback_operation of this SpanInfo.
        :type feedback_operation: str
        """
        self._feedback_operation = feedback_operation

    @property
    def label(self):
        r"""Gets the label of this SpanInfo.

        label标签组

        :return: The label of this SpanInfo.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.Label`]
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this SpanInfo.

        label标签组

        :param label: The label of this SpanInfo.
        :type label: list[:class:`huaweicloudsdkagentarts.v1.Label`]
        """
        self._label = label

    @property
    def resource_id(self):
        r"""Gets the resource_id of this SpanInfo.

        应用id

        :return: The resource_id of this SpanInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this SpanInfo.

        应用id

        :param resource_id: The resource_id of this SpanInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this SpanInfo.

        应用名称

        :return: The resource_name of this SpanInfo.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this SpanInfo.

        应用名称

        :param resource_name: The resource_name of this SpanInfo.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this SpanInfo.

        应用类型

        :return: The resource_type of this SpanInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this SpanInfo.

        应用类型

        :param resource_type: The resource_type of this SpanInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def model_name(self):
        r"""Gets the model_name of this SpanInfo.

        模型名称

        :return: The model_name of this SpanInfo.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this SpanInfo.

        模型名称

        :param model_name: The model_name of this SpanInfo.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def is_error(self):
        r"""Gets the is_error of this SpanInfo.

        是否失败

        :return: The is_error of this SpanInfo.
        :rtype: bool
        """
        return self._is_error

    @is_error.setter
    def is_error(self, is_error):
        r"""Sets the is_error of this SpanInfo.

        是否失败

        :param is_error: The is_error of this SpanInfo.
        :type is_error: bool
        """
        self._is_error = is_error

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
        if not isinstance(other, SpanInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
