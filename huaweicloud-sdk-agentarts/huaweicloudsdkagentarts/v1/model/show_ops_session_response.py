# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsSessionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_id': 'str',
        'latency': 'float',
        'tokens': 'float',
        'input_tokens': 'float',
        'output_tokens': 'float',
        'trace_num': 'float',
        'user_id': 'str',
        'call_type': 'str',
        'start_time': 'int',
        'domain_id': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'session_id': 'session_id',
        'latency': 'latency',
        'tokens': 'tokens',
        'input_tokens': 'input_tokens',
        'output_tokens': 'output_tokens',
        'trace_num': 'trace_num',
        'user_id': 'user_id',
        'call_type': 'call_type',
        'start_time': 'start_time',
        'domain_id': 'domain_id',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type'
    }

    def __init__(self, session_id=None, latency=None, tokens=None, input_tokens=None, output_tokens=None, trace_num=None, user_id=None, call_type=None, start_time=None, domain_id=None, resource_id=None, resource_name=None, resource_type=None):
        r"""ShowOpsSessionResponse

        The model defined in huaweicloud sdk

        :param session_id: 会话id
        :type session_id: str
        :param latency: 耗时
        :type latency: float
        :param tokens: tokens消耗
        :type tokens: float
        :param input_tokens: input tokens消耗
        :type input_tokens: float
        :param output_tokens: output tokens消耗
        :type output_tokens: float
        :param trace_num: trace数
        :type trace_num: float
        :param user_id: 用户id
        :type user_id: str
        :param call_type: 模式
        :type call_type: str
        :param start_time: 时间戳
        :type start_time: int
        :param domain_id: 租户domainId
        :type domain_id: str
        :param resource_id: 资源id
        :type resource_id: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_type: 资源类型
        :type resource_type: str
        """
        
        super().__init__()

        self._session_id = None
        self._latency = None
        self._tokens = None
        self._input_tokens = None
        self._output_tokens = None
        self._trace_num = None
        self._user_id = None
        self._call_type = None
        self._start_time = None
        self._domain_id = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if latency is not None:
            self.latency = latency
        if tokens is not None:
            self.tokens = tokens
        if input_tokens is not None:
            self.input_tokens = input_tokens
        if output_tokens is not None:
            self.output_tokens = output_tokens
        if trace_num is not None:
            self.trace_num = trace_num
        if user_id is not None:
            self.user_id = user_id
        if call_type is not None:
            self.call_type = call_type
        if start_time is not None:
            self.start_time = start_time
        if domain_id is not None:
            self.domain_id = domain_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def session_id(self):
        r"""Gets the session_id of this ShowOpsSessionResponse.

        会话id

        :return: The session_id of this ShowOpsSessionResponse.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this ShowOpsSessionResponse.

        会话id

        :param session_id: The session_id of this ShowOpsSessionResponse.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def latency(self):
        r"""Gets the latency of this ShowOpsSessionResponse.

        耗时

        :return: The latency of this ShowOpsSessionResponse.
        :rtype: float
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        r"""Sets the latency of this ShowOpsSessionResponse.

        耗时

        :param latency: The latency of this ShowOpsSessionResponse.
        :type latency: float
        """
        self._latency = latency

    @property
    def tokens(self):
        r"""Gets the tokens of this ShowOpsSessionResponse.

        tokens消耗

        :return: The tokens of this ShowOpsSessionResponse.
        :rtype: float
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        r"""Sets the tokens of this ShowOpsSessionResponse.

        tokens消耗

        :param tokens: The tokens of this ShowOpsSessionResponse.
        :type tokens: float
        """
        self._tokens = tokens

    @property
    def input_tokens(self):
        r"""Gets the input_tokens of this ShowOpsSessionResponse.

        input tokens消耗

        :return: The input_tokens of this ShowOpsSessionResponse.
        :rtype: float
        """
        return self._input_tokens

    @input_tokens.setter
    def input_tokens(self, input_tokens):
        r"""Sets the input_tokens of this ShowOpsSessionResponse.

        input tokens消耗

        :param input_tokens: The input_tokens of this ShowOpsSessionResponse.
        :type input_tokens: float
        """
        self._input_tokens = input_tokens

    @property
    def output_tokens(self):
        r"""Gets the output_tokens of this ShowOpsSessionResponse.

        output tokens消耗

        :return: The output_tokens of this ShowOpsSessionResponse.
        :rtype: float
        """
        return self._output_tokens

    @output_tokens.setter
    def output_tokens(self, output_tokens):
        r"""Sets the output_tokens of this ShowOpsSessionResponse.

        output tokens消耗

        :param output_tokens: The output_tokens of this ShowOpsSessionResponse.
        :type output_tokens: float
        """
        self._output_tokens = output_tokens

    @property
    def trace_num(self):
        r"""Gets the trace_num of this ShowOpsSessionResponse.

        trace数

        :return: The trace_num of this ShowOpsSessionResponse.
        :rtype: float
        """
        return self._trace_num

    @trace_num.setter
    def trace_num(self, trace_num):
        r"""Sets the trace_num of this ShowOpsSessionResponse.

        trace数

        :param trace_num: The trace_num of this ShowOpsSessionResponse.
        :type trace_num: float
        """
        self._trace_num = trace_num

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowOpsSessionResponse.

        用户id

        :return: The user_id of this ShowOpsSessionResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowOpsSessionResponse.

        用户id

        :param user_id: The user_id of this ShowOpsSessionResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def call_type(self):
        r"""Gets the call_type of this ShowOpsSessionResponse.

        模式

        :return: The call_type of this ShowOpsSessionResponse.
        :rtype: str
        """
        return self._call_type

    @call_type.setter
    def call_type(self, call_type):
        r"""Sets the call_type of this ShowOpsSessionResponse.

        模式

        :param call_type: The call_type of this ShowOpsSessionResponse.
        :type call_type: str
        """
        self._call_type = call_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowOpsSessionResponse.

        时间戳

        :return: The start_time of this ShowOpsSessionResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowOpsSessionResponse.

        时间戳

        :param start_time: The start_time of this ShowOpsSessionResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowOpsSessionResponse.

        租户domainId

        :return: The domain_id of this ShowOpsSessionResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowOpsSessionResponse.

        租户domainId

        :param domain_id: The domain_id of this ShowOpsSessionResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ShowOpsSessionResponse.

        资源id

        :return: The resource_id of this ShowOpsSessionResponse.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ShowOpsSessionResponse.

        资源id

        :param resource_id: The resource_id of this ShowOpsSessionResponse.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ShowOpsSessionResponse.

        资源名称

        :return: The resource_name of this ShowOpsSessionResponse.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ShowOpsSessionResponse.

        资源名称

        :param resource_name: The resource_name of this ShowOpsSessionResponse.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ShowOpsSessionResponse.

        资源类型

        :return: The resource_type of this ShowOpsSessionResponse.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ShowOpsSessionResponse.

        资源类型

        :param resource_type: The resource_type of this ShowOpsSessionResponse.
        :type resource_type: str
        """
        self._resource_type = resource_type

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpsSessionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowOpsSessionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
