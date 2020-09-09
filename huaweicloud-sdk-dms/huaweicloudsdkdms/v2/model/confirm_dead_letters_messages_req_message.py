# coding: utf-8

import pprint
import re

import six





class ConfirmDeadLettersMessagesReqMessage:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'handler': 'str',
        'status': 'str'
    }

    attribute_map = {
        'handler': 'handler',
        'status': 'status'
    }

    def __init__(self, handler=None, status=None):
        """ConfirmDeadLettersMessagesReqMessage - a model defined in huaweicloud sdk"""
        
        

        self._handler = None
        self._status = None
        self.discriminator = None

        if handler is not None:
            self.handler = handler
        if status is not None:
            self.status = status

    @property
    def handler(self):
        """Gets the handler of this ConfirmDeadLettersMessagesReqMessage.

        消费时返回的ID。

        :return: The handler of this ConfirmDeadLettersMessagesReqMessage.
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        """Sets the handler of this ConfirmDeadLettersMessagesReqMessage.

        消费时返回的ID。

        :param handler: The handler of this ConfirmDeadLettersMessagesReqMessage.
        :type: str
        """
        self._handler = handler

    @property
    def status(self):
        """Gets the status of this ConfirmDeadLettersMessagesReqMessage.

        客户端处理数据的状态。 取值为“success”或者“fail”。

        :return: The status of this ConfirmDeadLettersMessagesReqMessage.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConfirmDeadLettersMessagesReqMessage.

        客户端处理数据的状态。 取值为“success”或者“fail”。

        :param status: The status of this ConfirmDeadLettersMessagesReqMessage.
        :type: str
        """
        self._status = status

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConfirmDeadLettersMessagesReqMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
