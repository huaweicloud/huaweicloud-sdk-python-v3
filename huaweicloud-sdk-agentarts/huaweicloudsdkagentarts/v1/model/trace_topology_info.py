# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TraceTopologyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topology_span_type': 'str',
        'total_request_times': 'int',
        'success_request_times': 'int',
        'error_request_times': 'int',
        'operation_response_time': 'int',
        'tokens': 'int',
        'input_tokens': 'int',
        'output_tokens': 'int',
        'span_list': 'list[SpanInfo]'
    }

    attribute_map = {
        'topology_span_type': 'topology_span_type',
        'total_request_times': 'total_request_times',
        'success_request_times': 'success_request_times',
        'error_request_times': 'error_request_times',
        'operation_response_time': 'operation_response_time',
        'tokens': 'tokens',
        'input_tokens': 'input_tokens',
        'output_tokens': 'output_tokens',
        'span_list': 'span_list'
    }

    def __init__(self, topology_span_type=None, total_request_times=None, success_request_times=None, error_request_times=None, operation_response_time=None, tokens=None, input_tokens=None, output_tokens=None, span_list=None):
        r"""TraceTopologyInfo

        The model defined in huaweicloud sdk

        :param topology_span_type: 拓扑节点类型
        :type topology_span_type: str
        :param total_request_times: 请求总数
        :type total_request_times: int
        :param success_request_times: 成功请求总数
        :type success_request_times: int
        :param error_request_times: 错误请求总数
        :type error_request_times: int
        :param operation_response_time: 平均响应时间
        :type operation_response_time: int
        :param tokens: tokens总数
        :type tokens: int
        :param input_tokens: 输入tokens总数
        :type input_tokens: int
        :param output_tokens: 响应tokens总数
        :type output_tokens: int
        :param span_list: span列表
        :type span_list: list[:class:`huaweicloudsdkagentarts.v1.SpanInfo`]
        """
        
        

        self._topology_span_type = None
        self._total_request_times = None
        self._success_request_times = None
        self._error_request_times = None
        self._operation_response_time = None
        self._tokens = None
        self._input_tokens = None
        self._output_tokens = None
        self._span_list = None
        self.discriminator = None

        if topology_span_type is not None:
            self.topology_span_type = topology_span_type
        if total_request_times is not None:
            self.total_request_times = total_request_times
        if success_request_times is not None:
            self.success_request_times = success_request_times
        if error_request_times is not None:
            self.error_request_times = error_request_times
        if operation_response_time is not None:
            self.operation_response_time = operation_response_time
        if tokens is not None:
            self.tokens = tokens
        if input_tokens is not None:
            self.input_tokens = input_tokens
        if output_tokens is not None:
            self.output_tokens = output_tokens
        if span_list is not None:
            self.span_list = span_list

    @property
    def topology_span_type(self):
        r"""Gets the topology_span_type of this TraceTopologyInfo.

        拓扑节点类型

        :return: The topology_span_type of this TraceTopologyInfo.
        :rtype: str
        """
        return self._topology_span_type

    @topology_span_type.setter
    def topology_span_type(self, topology_span_type):
        r"""Sets the topology_span_type of this TraceTopologyInfo.

        拓扑节点类型

        :param topology_span_type: The topology_span_type of this TraceTopologyInfo.
        :type topology_span_type: str
        """
        self._topology_span_type = topology_span_type

    @property
    def total_request_times(self):
        r"""Gets the total_request_times of this TraceTopologyInfo.

        请求总数

        :return: The total_request_times of this TraceTopologyInfo.
        :rtype: int
        """
        return self._total_request_times

    @total_request_times.setter
    def total_request_times(self, total_request_times):
        r"""Sets the total_request_times of this TraceTopologyInfo.

        请求总数

        :param total_request_times: The total_request_times of this TraceTopologyInfo.
        :type total_request_times: int
        """
        self._total_request_times = total_request_times

    @property
    def success_request_times(self):
        r"""Gets the success_request_times of this TraceTopologyInfo.

        成功请求总数

        :return: The success_request_times of this TraceTopologyInfo.
        :rtype: int
        """
        return self._success_request_times

    @success_request_times.setter
    def success_request_times(self, success_request_times):
        r"""Sets the success_request_times of this TraceTopologyInfo.

        成功请求总数

        :param success_request_times: The success_request_times of this TraceTopologyInfo.
        :type success_request_times: int
        """
        self._success_request_times = success_request_times

    @property
    def error_request_times(self):
        r"""Gets the error_request_times of this TraceTopologyInfo.

        错误请求总数

        :return: The error_request_times of this TraceTopologyInfo.
        :rtype: int
        """
        return self._error_request_times

    @error_request_times.setter
    def error_request_times(self, error_request_times):
        r"""Sets the error_request_times of this TraceTopologyInfo.

        错误请求总数

        :param error_request_times: The error_request_times of this TraceTopologyInfo.
        :type error_request_times: int
        """
        self._error_request_times = error_request_times

    @property
    def operation_response_time(self):
        r"""Gets the operation_response_time of this TraceTopologyInfo.

        平均响应时间

        :return: The operation_response_time of this TraceTopologyInfo.
        :rtype: int
        """
        return self._operation_response_time

    @operation_response_time.setter
    def operation_response_time(self, operation_response_time):
        r"""Sets the operation_response_time of this TraceTopologyInfo.

        平均响应时间

        :param operation_response_time: The operation_response_time of this TraceTopologyInfo.
        :type operation_response_time: int
        """
        self._operation_response_time = operation_response_time

    @property
    def tokens(self):
        r"""Gets the tokens of this TraceTopologyInfo.

        tokens总数

        :return: The tokens of this TraceTopologyInfo.
        :rtype: int
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        r"""Sets the tokens of this TraceTopologyInfo.

        tokens总数

        :param tokens: The tokens of this TraceTopologyInfo.
        :type tokens: int
        """
        self._tokens = tokens

    @property
    def input_tokens(self):
        r"""Gets the input_tokens of this TraceTopologyInfo.

        输入tokens总数

        :return: The input_tokens of this TraceTopologyInfo.
        :rtype: int
        """
        return self._input_tokens

    @input_tokens.setter
    def input_tokens(self, input_tokens):
        r"""Sets the input_tokens of this TraceTopologyInfo.

        输入tokens总数

        :param input_tokens: The input_tokens of this TraceTopologyInfo.
        :type input_tokens: int
        """
        self._input_tokens = input_tokens

    @property
    def output_tokens(self):
        r"""Gets the output_tokens of this TraceTopologyInfo.

        响应tokens总数

        :return: The output_tokens of this TraceTopologyInfo.
        :rtype: int
        """
        return self._output_tokens

    @output_tokens.setter
    def output_tokens(self, output_tokens):
        r"""Sets the output_tokens of this TraceTopologyInfo.

        响应tokens总数

        :param output_tokens: The output_tokens of this TraceTopologyInfo.
        :type output_tokens: int
        """
        self._output_tokens = output_tokens

    @property
    def span_list(self):
        r"""Gets the span_list of this TraceTopologyInfo.

        span列表

        :return: The span_list of this TraceTopologyInfo.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.SpanInfo`]
        """
        return self._span_list

    @span_list.setter
    def span_list(self, span_list):
        r"""Sets the span_list of this TraceTopologyInfo.

        span列表

        :param span_list: The span_list of this TraceTopologyInfo.
        :type span_list: list[:class:`huaweicloudsdkagentarts.v1.SpanInfo`]
        """
        self._span_list = span_list

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
        if not isinstance(other, TraceTopologyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
