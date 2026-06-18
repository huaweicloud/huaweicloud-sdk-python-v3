# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RebuildRepositoryNavigationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'message': 'str',
        'duration': 'str',
        'size': 'int'
    }

    attribute_map = {
        'result': 'result',
        'message': 'message',
        'duration': 'duration',
        'size': 'size'
    }

    def __init__(self, result=None, message=None, duration=None, size=None):
        r"""RebuildRepositoryNavigationResponse

        The model defined in huaweicloud sdk

        :param result: **参数解释：** 结果标识。 **约束限制：** 不涉及。
        :type result: str
        :param message: **参数解释：** 结果消息。 **约束限制：** 不涉及。
        :type message: str
        :param duration: **参数解释：** 触发任务耗时（毫秒）。 **约束限制：** 不涉及。
        :type duration: str
        :param size: **参数解释：** 当前代码导航索引大小（字节）。 **约束限制：** 不涉及。
        :type size: int
        """
        
        super().__init__()

        self._result = None
        self._message = None
        self._duration = None
        self._size = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if message is not None:
            self.message = message
        if duration is not None:
            self.duration = duration
        if size is not None:
            self.size = size

    @property
    def result(self):
        r"""Gets the result of this RebuildRepositoryNavigationResponse.

        **参数解释：** 结果标识。 **约束限制：** 不涉及。

        :return: The result of this RebuildRepositoryNavigationResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this RebuildRepositoryNavigationResponse.

        **参数解释：** 结果标识。 **约束限制：** 不涉及。

        :param result: The result of this RebuildRepositoryNavigationResponse.
        :type result: str
        """
        self._result = result

    @property
    def message(self):
        r"""Gets the message of this RebuildRepositoryNavigationResponse.

        **参数解释：** 结果消息。 **约束限制：** 不涉及。

        :return: The message of this RebuildRepositoryNavigationResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this RebuildRepositoryNavigationResponse.

        **参数解释：** 结果消息。 **约束限制：** 不涉及。

        :param message: The message of this RebuildRepositoryNavigationResponse.
        :type message: str
        """
        self._message = message

    @property
    def duration(self):
        r"""Gets the duration of this RebuildRepositoryNavigationResponse.

        **参数解释：** 触发任务耗时（毫秒）。 **约束限制：** 不涉及。

        :return: The duration of this RebuildRepositoryNavigationResponse.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this RebuildRepositoryNavigationResponse.

        **参数解释：** 触发任务耗时（毫秒）。 **约束限制：** 不涉及。

        :param duration: The duration of this RebuildRepositoryNavigationResponse.
        :type duration: str
        """
        self._duration = duration

    @property
    def size(self):
        r"""Gets the size of this RebuildRepositoryNavigationResponse.

        **参数解释：** 当前代码导航索引大小（字节）。 **约束限制：** 不涉及。

        :return: The size of this RebuildRepositoryNavigationResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this RebuildRepositoryNavigationResponse.

        **参数解释：** 当前代码导航索引大小（字节）。 **约束限制：** 不涉及。

        :param size: The size of this RebuildRepositoryNavigationResponse.
        :type size: int
        """
        self._size = size

    def to_dict(self):
        import warnings
        warnings.warn("RebuildRepositoryNavigationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, RebuildRepositoryNavigationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
