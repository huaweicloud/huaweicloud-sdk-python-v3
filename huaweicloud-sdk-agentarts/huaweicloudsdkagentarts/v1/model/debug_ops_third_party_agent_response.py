# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugOpsThirdPartyAgentResponse(SdkResponse):

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
        'response_time': 'int',
        'output': 'str',
        'raw_response': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'status_code': 'status_code',
        'response_time': 'response_time',
        'output': 'output',
        'raw_response': 'raw_response',
        'error_message': 'error_message'
    }

    def __init__(self, status_code=None, response_time=None, output=None, raw_response=None, error_message=None):
        r"""DebugOpsThirdPartyAgentResponse

        The model defined in huaweicloud sdk

        :param status_code: **参数解释：** HTTP响应状态码。 **取值范围：** 不涉及。
        :type status_code: int
        :param response_time: **参数解释：** 响应时间，单位毫秒。 **取值范围：** 不涉及。
        :type response_time: int
        :param output: **参数解释：** 提取后的Agent输出内容。 **取值范围：** 不涉及。
        :type output: str
        :param raw_response: **参数解释：** 原始响应内容。 **取值范围：** 不涉及。
        :type raw_response: str
        :param error_message: **参数解释：** 错误信息，调用失败时返回。 **取值范围：** 不涉及。
        :type error_message: str
        """
        
        super().__init__()

        self._status_code = None
        self._response_time = None
        self._output = None
        self._raw_response = None
        self._error_message = None
        self.discriminator = None

        if status_code is not None:
            self.status_code = status_code
        if response_time is not None:
            self.response_time = response_time
        if output is not None:
            self.output = output
        if raw_response is not None:
            self.raw_response = raw_response
        if error_message is not None:
            self.error_message = error_message

    @property
    def status_code(self):
        r"""Gets the status_code of this DebugOpsThirdPartyAgentResponse.

        **参数解释：** HTTP响应状态码。 **取值范围：** 不涉及。

        :return: The status_code of this DebugOpsThirdPartyAgentResponse.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this DebugOpsThirdPartyAgentResponse.

        **参数解释：** HTTP响应状态码。 **取值范围：** 不涉及。

        :param status_code: The status_code of this DebugOpsThirdPartyAgentResponse.
        :type status_code: int
        """
        self._status_code = status_code

    @property
    def response_time(self):
        r"""Gets the response_time of this DebugOpsThirdPartyAgentResponse.

        **参数解释：** 响应时间，单位毫秒。 **取值范围：** 不涉及。

        :return: The response_time of this DebugOpsThirdPartyAgentResponse.
        :rtype: int
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        r"""Sets the response_time of this DebugOpsThirdPartyAgentResponse.

        **参数解释：** 响应时间，单位毫秒。 **取值范围：** 不涉及。

        :param response_time: The response_time of this DebugOpsThirdPartyAgentResponse.
        :type response_time: int
        """
        self._response_time = response_time

    @property
    def output(self):
        r"""Gets the output of this DebugOpsThirdPartyAgentResponse.

        **参数解释：** 提取后的Agent输出内容。 **取值范围：** 不涉及。

        :return: The output of this DebugOpsThirdPartyAgentResponse.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this DebugOpsThirdPartyAgentResponse.

        **参数解释：** 提取后的Agent输出内容。 **取值范围：** 不涉及。

        :param output: The output of this DebugOpsThirdPartyAgentResponse.
        :type output: str
        """
        self._output = output

    @property
    def raw_response(self):
        r"""Gets the raw_response of this DebugOpsThirdPartyAgentResponse.

        **参数解释：** 原始响应内容。 **取值范围：** 不涉及。

        :return: The raw_response of this DebugOpsThirdPartyAgentResponse.
        :rtype: str
        """
        return self._raw_response

    @raw_response.setter
    def raw_response(self, raw_response):
        r"""Sets the raw_response of this DebugOpsThirdPartyAgentResponse.

        **参数解释：** 原始响应内容。 **取值范围：** 不涉及。

        :param raw_response: The raw_response of this DebugOpsThirdPartyAgentResponse.
        :type raw_response: str
        """
        self._raw_response = raw_response

    @property
    def error_message(self):
        r"""Gets the error_message of this DebugOpsThirdPartyAgentResponse.

        **参数解释：** 错误信息，调用失败时返回。 **取值范围：** 不涉及。

        :return: The error_message of this DebugOpsThirdPartyAgentResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this DebugOpsThirdPartyAgentResponse.

        **参数解释：** 错误信息，调用失败时返回。 **取值范围：** 不涉及。

        :param error_message: The error_message of this DebugOpsThirdPartyAgentResponse.
        :type error_message: str
        """
        self._error_message = error_message

    def to_dict(self):
        import warnings
        warnings.warn("DebugOpsThirdPartyAgentResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DebugOpsThirdPartyAgentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
