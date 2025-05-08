# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMessagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'messages': 'list[ShowMessagesRespMessages]',
        'messages_count': 'int',
        'offsets_count': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'messages': 'messages',
        'messages_count': 'messages_count',
        'offsets_count': 'offsets_count',
        'offset': 'offset'
    }

    def __init__(self, messages=None, messages_count=None, offsets_count=None, offset=None):
        r"""ShowMessagesResponse

        The model defined in huaweicloud sdk

        :param messages: **参数解释**： 消息列表。
        :type messages: list[:class:`huaweicloudsdkkafka.v2.ShowMessagesRespMessages`]
        :param messages_count: **参数解释**： 消息总数。 **取值范围**： 不涉及。
        :type messages_count: int
        :param offsets_count: **参数解释**： 总页数。 **取值范围**： 不涉及。
        :type offsets_count: int
        :param offset: **参数解释**： 当前页数。 **取值范围**： 不涉及。
        :type offset: int
        """
        
        super(ShowMessagesResponse, self).__init__()

        self._messages = None
        self._messages_count = None
        self._offsets_count = None
        self._offset = None
        self.discriminator = None

        if messages is not None:
            self.messages = messages
        if messages_count is not None:
            self.messages_count = messages_count
        if offsets_count is not None:
            self.offsets_count = offsets_count
        if offset is not None:
            self.offset = offset

    @property
    def messages(self):
        r"""Gets the messages of this ShowMessagesResponse.

        **参数解释**： 消息列表。

        :return: The messages of this ShowMessagesResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ShowMessagesRespMessages`]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        r"""Sets the messages of this ShowMessagesResponse.

        **参数解释**： 消息列表。

        :param messages: The messages of this ShowMessagesResponse.
        :type messages: list[:class:`huaweicloudsdkkafka.v2.ShowMessagesRespMessages`]
        """
        self._messages = messages

    @property
    def messages_count(self):
        r"""Gets the messages_count of this ShowMessagesResponse.

        **参数解释**： 消息总数。 **取值范围**： 不涉及。

        :return: The messages_count of this ShowMessagesResponse.
        :rtype: int
        """
        return self._messages_count

    @messages_count.setter
    def messages_count(self, messages_count):
        r"""Sets the messages_count of this ShowMessagesResponse.

        **参数解释**： 消息总数。 **取值范围**： 不涉及。

        :param messages_count: The messages_count of this ShowMessagesResponse.
        :type messages_count: int
        """
        self._messages_count = messages_count

    @property
    def offsets_count(self):
        r"""Gets the offsets_count of this ShowMessagesResponse.

        **参数解释**： 总页数。 **取值范围**： 不涉及。

        :return: The offsets_count of this ShowMessagesResponse.
        :rtype: int
        """
        return self._offsets_count

    @offsets_count.setter
    def offsets_count(self, offsets_count):
        r"""Sets the offsets_count of this ShowMessagesResponse.

        **参数解释**： 总页数。 **取值范围**： 不涉及。

        :param offsets_count: The offsets_count of this ShowMessagesResponse.
        :type offsets_count: int
        """
        self._offsets_count = offsets_count

    @property
    def offset(self):
        r"""Gets the offset of this ShowMessagesResponse.

        **参数解释**： 当前页数。 **取值范围**： 不涉及。

        :return: The offset of this ShowMessagesResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowMessagesResponse.

        **参数解释**： 当前页数。 **取值范围**： 不涉及。

        :param offset: The offset of this ShowMessagesResponse.
        :type offset: int
        """
        self._offset = offset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowMessagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
