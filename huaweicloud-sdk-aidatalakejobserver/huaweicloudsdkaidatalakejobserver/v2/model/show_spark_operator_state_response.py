# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSparkOperatorStateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'operator_info': 'object',
        'message': 'str',
        'create_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'status': 'status',
        'operator_info': 'operator_info',
        'message': 'message',
        'create_time': 'create_time',
        'end_time': 'end_time'
    }

    def __init__(self, status=None, operator_info=None, message=None, create_time=None, end_time=None):
        r"""ShowSparkOperatorStateResponse

        The model defined in huaweicloud sdk

        :param status: **参数解释**：操作状态，用于标识异步操作的当前执行状态。 **取值范围**：   - RUNNING：运行中。   - FAILED：失败。   - SUCCESS：成功。
        :type status: str
        :param operator_info: **参数解释**：操作详情描述。
        :type operator_info: :class:`huaweicloudsdkaidatalakejobserver.v2.object`
        :param message: **参数解释**：操作描述信息，包含操作状态描述或失败时的错误信息。 **取值范围**：长度为0~1024个字符。
        :type message: str
        :param create_time: **参数解释**：操作创建时间，用于记录操作提交的时间。 **取值范围**：Unix时间戳，单位为毫秒，取值范围为0~9223372036854775807。
        :type create_time: int
        :param end_time: **参数解释**：操作结束时间，用于记录操作完成的时间。 **取值范围**：Unix时间戳，单位为毫秒，取值范围为0~9223372036854775807。
        :type end_time: int
        """
        
        super().__init__()

        self._status = None
        self._operator_info = None
        self._message = None
        self._create_time = None
        self._end_time = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if operator_info is not None:
            self.operator_info = operator_info
        if message is not None:
            self.message = message
        if create_time is not None:
            self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this ShowSparkOperatorStateResponse.

        **参数解释**：操作状态，用于标识异步操作的当前执行状态。 **取值范围**：   - RUNNING：运行中。   - FAILED：失败。   - SUCCESS：成功。

        :return: The status of this ShowSparkOperatorStateResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowSparkOperatorStateResponse.

        **参数解释**：操作状态，用于标识异步操作的当前执行状态。 **取值范围**：   - RUNNING：运行中。   - FAILED：失败。   - SUCCESS：成功。

        :param status: The status of this ShowSparkOperatorStateResponse.
        :type status: str
        """
        self._status = status

    @property
    def operator_info(self):
        r"""Gets the operator_info of this ShowSparkOperatorStateResponse.

        **参数解释**：操作详情描述。

        :return: The operator_info of this ShowSparkOperatorStateResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.object`
        """
        return self._operator_info

    @operator_info.setter
    def operator_info(self, operator_info):
        r"""Sets the operator_info of this ShowSparkOperatorStateResponse.

        **参数解释**：操作详情描述。

        :param operator_info: The operator_info of this ShowSparkOperatorStateResponse.
        :type operator_info: :class:`huaweicloudsdkaidatalakejobserver.v2.object`
        """
        self._operator_info = operator_info

    @property
    def message(self):
        r"""Gets the message of this ShowSparkOperatorStateResponse.

        **参数解释**：操作描述信息，包含操作状态描述或失败时的错误信息。 **取值范围**：长度为0~1024个字符。

        :return: The message of this ShowSparkOperatorStateResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowSparkOperatorStateResponse.

        **参数解释**：操作描述信息，包含操作状态描述或失败时的错误信息。 **取值范围**：长度为0~1024个字符。

        :param message: The message of this ShowSparkOperatorStateResponse.
        :type message: str
        """
        self._message = message

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowSparkOperatorStateResponse.

        **参数解释**：操作创建时间，用于记录操作提交的时间。 **取值范围**：Unix时间戳，单位为毫秒，取值范围为0~9223372036854775807。

        :return: The create_time of this ShowSparkOperatorStateResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowSparkOperatorStateResponse.

        **参数解释**：操作创建时间，用于记录操作提交的时间。 **取值范围**：Unix时间戳，单位为毫秒，取值范围为0~9223372036854775807。

        :param create_time: The create_time of this ShowSparkOperatorStateResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowSparkOperatorStateResponse.

        **参数解释**：操作结束时间，用于记录操作完成的时间。 **取值范围**：Unix时间戳，单位为毫秒，取值范围为0~9223372036854775807。

        :return: The end_time of this ShowSparkOperatorStateResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowSparkOperatorStateResponse.

        **参数解释**：操作结束时间，用于记录操作完成的时间。 **取值范围**：Unix时间戳，单位为毫秒，取值范围为0~9223372036854775807。

        :param end_time: The end_time of this ShowSparkOperatorStateResponse.
        :type end_time: int
        """
        self._end_time = end_time

    def to_dict(self):
        import warnings
        warnings.warn("ShowSparkOperatorStateResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSparkOperatorStateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
