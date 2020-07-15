# coding: utf-8

import pprint
import re

import six





class BatchUpdateDevicesStatusRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_request_id': 'str',
        'accept_language': 'str',
        'value': 'int',
        'body': 'list[str]'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'accept_language': 'Accept-Language',
        'value': 'value',
        'body': 'body'
    }

    def __init__(self, x_request_id=None, accept_language=None, value=None, body=None):
        """BatchUpdateDevicesStatusRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_request_id = None
        self._accept_language = None
        self._value = None
        self._body = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        if accept_language is not None:
            self.accept_language = accept_language
        self.value = value
        if body is not None:
            self.body = body

    @property
    def x_request_id(self):
        """Gets the x_request_id of this BatchUpdateDevicesStatusRequest.


        :return: The x_request_id of this BatchUpdateDevicesStatusRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this BatchUpdateDevicesStatusRequest.


        :param x_request_id: The x_request_id of this BatchUpdateDevicesStatusRequest.
        :type: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        """Gets the accept_language of this BatchUpdateDevicesStatusRequest.


        :return: The accept_language of this BatchUpdateDevicesStatusRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this BatchUpdateDevicesStatusRequest.


        :param accept_language: The accept_language of this BatchUpdateDevicesStatusRequest.
        :type: str
        """
        self._accept_language = accept_language

    @property
    def value(self):
        """Gets the value of this BatchUpdateDevicesStatusRequest.


        :return: The value of this BatchUpdateDevicesStatusRequest.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BatchUpdateDevicesStatusRequest.


        :param value: The value of this BatchUpdateDevicesStatusRequest.
        :type: int
        """
        self._value = value

    @property
    def body(self):
        """Gets the body of this BatchUpdateDevicesStatusRequest.

        终端序列号列表，当SN对应的终端状态一致的，则忽略该记录 maxLength：100 minLength：1

        :return: The body of this BatchUpdateDevicesStatusRequest.
        :rtype: list[str]
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchUpdateDevicesStatusRequest.

        终端序列号列表，当SN对应的终端状态一致的，则忽略该记录 maxLength：100 minLength：1

        :param body: The body of this BatchUpdateDevicesStatusRequest.
        :type: list[str]
        """
        self._body = body

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
        if not isinstance(other, BatchUpdateDevicesStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
