# coding: utf-8

import six

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
        """ShowInstanceMessagesResponse

        The model defined in huaweicloud sdk

        :param messages: 消息列表。
        :type messages: list[:class:`huaweicloudsdkkafka.v2.MessagesEntity`]
        :param total: 消息总条数。
        :type total: int
        :param size: 每页消息条数。
        :type size: int
        """
        
        super(ShowInstanceMessagesResponse, self).__init__()

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
        """Gets the messages of this ShowInstanceMessagesResponse.

        消息列表。

        :return: The messages of this ShowInstanceMessagesResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.MessagesEntity`]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this ShowInstanceMessagesResponse.

        消息列表。

        :param messages: The messages of this ShowInstanceMessagesResponse.
        :type messages: list[:class:`huaweicloudsdkkafka.v2.MessagesEntity`]
        """
        self._messages = messages

    @property
    def total(self):
        """Gets the total of this ShowInstanceMessagesResponse.

        消息总条数。

        :return: The total of this ShowInstanceMessagesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowInstanceMessagesResponse.

        消息总条数。

        :param total: The total of this ShowInstanceMessagesResponse.
        :type total: int
        """
        self._total = total

    @property
    def size(self):
        """Gets the size of this ShowInstanceMessagesResponse.

        每页消息条数。

        :return: The size of this ShowInstanceMessagesResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ShowInstanceMessagesResponse.

        每页消息条数。

        :param size: The size of this ShowInstanceMessagesResponse.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, ShowInstanceMessagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
