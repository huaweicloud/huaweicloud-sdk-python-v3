# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceMessagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'messages': 'list[MessagesEntity]',
        'total': 'int',
        'size': 'int'
    }

    attribute_map = {
        'messages': 'messages',
        'total': 'total',
        'size': 'size'
    }

    def __init__(self, messages=None, total=None, size=None):
        r"""ShowInstanceMessagesResponse

        The model defined in huaweicloud sdk

        :param messages: **参数解释**： 消息列表。
        :type messages: list[:class:`huaweicloudsdkkafka.v2.MessagesEntity`]
        :param total: **参数解释**： 消息总条数。 **取值范围**： 不涉及。
        :type total: int
        :param size: **参数解释**： 每页消息条数。 **取值范围**： 不涉及。
        :type size: int
        """
        
        super().__init__()

        self._messages = None
        self._total = None
        self._size = None
        self.discriminator = None

        if messages is not None:
            self.messages = messages
        if total is not None:
            self.total = total
        if size is not None:
            self.size = size

    @property
    def messages(self):
        r"""Gets the messages of this ShowInstanceMessagesResponse.

        **参数解释**： 消息列表。

        :return: The messages of this ShowInstanceMessagesResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.MessagesEntity`]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        r"""Sets the messages of this ShowInstanceMessagesResponse.

        **参数解释**： 消息列表。

        :param messages: The messages of this ShowInstanceMessagesResponse.
        :type messages: list[:class:`huaweicloudsdkkafka.v2.MessagesEntity`]
        """
        self._messages = messages

    @property
    def total(self):
        r"""Gets the total of this ShowInstanceMessagesResponse.

        **参数解释**： 消息总条数。 **取值范围**： 不涉及。

        :return: The total of this ShowInstanceMessagesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowInstanceMessagesResponse.

        **参数解释**： 消息总条数。 **取值范围**： 不涉及。

        :param total: The total of this ShowInstanceMessagesResponse.
        :type total: int
        """
        self._total = total

    @property
    def size(self):
        r"""Gets the size of this ShowInstanceMessagesResponse.

        **参数解释**： 每页消息条数。 **取值范围**： 不涉及。

        :return: The size of this ShowInstanceMessagesResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowInstanceMessagesResponse.

        **参数解释**： 每页消息条数。 **取值范围**： 不涉及。

        :param size: The size of this ShowInstanceMessagesResponse.
        :type size: int
        """
        self._size = size

    def to_dict(self):
        import warnings
        warnings.warn("ShowInstanceMessagesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowInstanceMessagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
