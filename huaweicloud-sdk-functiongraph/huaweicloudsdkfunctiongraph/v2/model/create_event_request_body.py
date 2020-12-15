# coding: utf-8

import pprint
import re

import six





class CreateEventRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'content': 'str'
    }

    attribute_map = {
        'name': 'name',
        'content': 'content'
    }

    def __init__(self, name=None, content=None):
        """CreateEventRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._content = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if content is not None:
            self.content = content

    @property
    def name(self):
        """Gets the name of this CreateEventRequestBody.

        测试事件名称。只能由字母、数字、中划线和下划线组成，且必须以大写或小写字母开头。

        :return: The name of this CreateEventRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateEventRequestBody.

        测试事件名称。只能由字母、数字、中划线和下划线组成，且必须以大写或小写字母开头。

        :param name: The name of this CreateEventRequestBody.
        :type: str
        """
        self._name = name

    @property
    def content(self):
        """Gets the content of this CreateEventRequestBody.

        测试事件content。

        :return: The content of this CreateEventRequestBody.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CreateEventRequestBody.

        测试事件content。

        :param content: The content of this CreateEventRequestBody.
        :type: str
        """
        self._content = content

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
        if not isinstance(other, CreateEventRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
