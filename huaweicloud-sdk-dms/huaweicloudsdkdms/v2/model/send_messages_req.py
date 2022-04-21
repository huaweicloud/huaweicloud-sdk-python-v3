# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SendMessagesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'return_id': 'bool',
        'messages': 'list[SendMessageEntity]'
    }

    attribute_map = {
        'return_id': 'return_id',
        'messages': 'messages'
    }

    def __init__(self, return_id=None, messages=None):
        """SendMessagesReq

        The model defined in huaweicloud sdk

        :param return_id: 发送消息成功后，是否返回Message ID，默认为false，设置为true时，返回参数才有Message ID。
        :type return_id: bool
        :param messages: 消息列表。
        :type messages: list[:class:`huaweicloudsdkdms.v2.SendMessageEntity`]
        """
        
        

        self._return_id = None
        self._messages = None
        self.discriminator = None

        if return_id is not None:
            self.return_id = return_id
        self.messages = messages

    @property
    def return_id(self):
        """Gets the return_id of this SendMessagesReq.

        发送消息成功后，是否返回Message ID，默认为false，设置为true时，返回参数才有Message ID。

        :return: The return_id of this SendMessagesReq.
        :rtype: bool
        """
        return self._return_id

    @return_id.setter
    def return_id(self, return_id):
        """Sets the return_id of this SendMessagesReq.

        发送消息成功后，是否返回Message ID，默认为false，设置为true时，返回参数才有Message ID。

        :param return_id: The return_id of this SendMessagesReq.
        :type return_id: bool
        """
        self._return_id = return_id

    @property
    def messages(self):
        """Gets the messages of this SendMessagesReq.

        消息列表。

        :return: The messages of this SendMessagesReq.
        :rtype: list[:class:`huaweicloudsdkdms.v2.SendMessageEntity`]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this SendMessagesReq.

        消息列表。

        :param messages: The messages of this SendMessagesReq.
        :type messages: list[:class:`huaweicloudsdkdms.v2.SendMessageEntity`]
        """
        self._messages = messages

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
        if not isinstance(other, SendMessagesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
