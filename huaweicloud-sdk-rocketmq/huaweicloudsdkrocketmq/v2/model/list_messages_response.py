# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMessagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'messages': 'list[Message]',
        'total': 'float'
    }

    attribute_map = {
        'messages': 'messages',
        'total': 'total'
    }

    def __init__(self, messages=None, total=None):
        """ListMessagesResponse

        The model defined in huaweicloud sdk

        :param messages: 消息列表。
        :type messages: list[:class:`huaweicloudsdkrocketmq.v2.Message`]
        :param total: 消息总数。
        :type total: float
        """
        
        super(ListMessagesResponse, self).__init__()

        self._messages = None
        self._total = None
        self.discriminator = None

        if messages is not None:
            self.messages = messages
        if total is not None:
            self.total = total

    @property
    def messages(self):
        """Gets the messages of this ListMessagesResponse.

        消息列表。

        :return: The messages of this ListMessagesResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.Message`]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this ListMessagesResponse.

        消息列表。

        :param messages: The messages of this ListMessagesResponse.
        :type messages: list[:class:`huaweicloudsdkrocketmq.v2.Message`]
        """
        self._messages = messages

    @property
    def total(self):
        """Gets the total of this ListMessagesResponse.

        消息总数。

        :return: The total of this ListMessagesResponse.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListMessagesResponse.

        消息总数。

        :param total: The total of this ListMessagesResponse.
        :type total: float
        """
        self._total = total

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
        if not isinstance(other, ListMessagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
