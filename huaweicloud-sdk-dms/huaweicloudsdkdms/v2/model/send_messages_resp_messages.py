# coding: utf-8

import pprint
import re

import six





class SendMessagesRespMessages:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'error': 'str',
        'error_code': 'int',
        'state': 'int',
        'id': 'str'
    }

    attribute_map = {
        'error': 'error',
        'error_code': 'error_code',
        'state': 'state',
        'id': 'id'
    }

    def __init__(self, error=None, error_code=None, state=None, id=None):
        """SendMessagesRespMessages - a model defined in huaweicloud sdk"""
        
        

        self._error = None
        self._error_code = None
        self._state = None
        self._id = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if error_code is not None:
            self.error_code = error_code
        if state is not None:
            self.state = state
        if id is not None:
            self.id = id

    @property
    def error(self):
        """Gets the error of this SendMessagesRespMessages.

        错误描述信息。

        :return: The error of this SendMessagesRespMessages.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this SendMessagesRespMessages.

        错误描述信息。

        :param error: The error of this SendMessagesRespMessages.
        :type: str
        """
        self._error = error

    @property
    def error_code(self):
        """Gets the error_code of this SendMessagesRespMessages.

        错误码。

        :return: The error_code of this SendMessagesRespMessages.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this SendMessagesRespMessages.

        错误码。

        :param error_code: The error_code of this SendMessagesRespMessages.
        :type: int
        """
        self._error_code = error_code

    @property
    def state(self):
        """Gets the state of this SendMessagesRespMessages.

        发送消息的状态。 0：表示发送成功。 1：表示发送失败，失败原因参考对应的error和error_code。 

        :return: The state of this SendMessagesRespMessages.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SendMessagesRespMessages.

        发送消息的状态。 0：表示发送成功。 1：表示发送失败，失败原因参考对应的error和error_code。 

        :param state: The state of this SendMessagesRespMessages.
        :type: int
        """
        self._state = state

    @property
    def id(self):
        """Gets the id of this SendMessagesRespMessages.

        消息ID。

        :return: The id of this SendMessagesRespMessages.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SendMessagesRespMessages.

        消息ID。

        :param id: The id of this SendMessagesRespMessages.
        :type: str
        """
        self._id = id

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
        if not isinstance(other, SendMessagesRespMessages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
