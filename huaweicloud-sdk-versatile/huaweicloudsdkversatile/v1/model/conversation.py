# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Conversation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'last_update_time': 'int',
        'message_list': 'list[Message]'
    }

    attribute_map = {
        'last_update_time': 'lastUpdateTime',
        'message_list': 'messageList'
    }

    def __init__(self, last_update_time=None, message_list=None):
        r"""Conversation

        The model defined in huaweicloud sdk

        :param last_update_time: 
        :type last_update_time: int
        :param message_list: 
        :type message_list: list[:class:`huaweicloudsdkversatile.v1.Message`]
        """
        
        

        self._last_update_time = None
        self._message_list = None
        self.discriminator = None

        if last_update_time is not None:
            self.last_update_time = last_update_time
        if message_list is not None:
            self.message_list = message_list

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this Conversation.

        :return: The last_update_time of this Conversation.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this Conversation.

        :param last_update_time: The last_update_time of this Conversation.
        :type last_update_time: int
        """
        self._last_update_time = last_update_time

    @property
    def message_list(self):
        r"""Gets the message_list of this Conversation.

        :return: The message_list of this Conversation.
        :rtype: list[:class:`huaweicloudsdkversatile.v1.Message`]
        """
        return self._message_list

    @message_list.setter
    def message_list(self, message_list):
        r"""Sets the message_list of this Conversation.

        :param message_list: The message_list of this Conversation.
        :type message_list: list[:class:`huaweicloudsdkversatile.v1.Message`]
        """
        self._message_list = message_list

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
        if not isinstance(other, Conversation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
