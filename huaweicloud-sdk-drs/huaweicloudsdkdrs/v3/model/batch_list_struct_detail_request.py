# coding: utf-8

import pprint
import re

import six





class BatchListStructDetailRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'x_language': 'str',
        'body': 'BatchQueryJobReqPage'
    }

    attribute_map = {
        'type': 'type',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, type=None, x_language=None, body=None):
        """BatchListStructDetailRequest - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.type = type
        self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def type(self):
        """Gets the type of this BatchListStructDetailRequest.

        数据库支持迁移对象类型

        :return: The type of this BatchListStructDetailRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BatchListStructDetailRequest.

        数据库支持迁移对象类型

        :param type: The type of this BatchListStructDetailRequest.
        :type: str
        """
        self._type = type

    @property
    def x_language(self):
        """Gets the x_language of this BatchListStructDetailRequest.

        请求语言类型

        :return: The x_language of this BatchListStructDetailRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this BatchListStructDetailRequest.

        请求语言类型

        :param x_language: The x_language of this BatchListStructDetailRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def body(self):
        """Gets the body of this BatchListStructDetailRequest.


        :return: The body of this BatchListStructDetailRequest.
        :rtype: BatchQueryJobReqPage
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchListStructDetailRequest.


        :param body: The body of this BatchListStructDetailRequest.
        :type: BatchQueryJobReqPage
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
        if not isinstance(other, BatchListStructDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other