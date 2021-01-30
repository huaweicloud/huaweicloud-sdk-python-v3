# coding: utf-8

import pprint
import re

import six





class PageLink:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        '_self': 'str',
        'next': 'str'
    }

    attribute_map = {
        '_self': 'self',
        'next': 'next'
    }

    def __init__(self, _self=None, next=None):
        """PageLink - a model defined in huaweicloud sdk"""
        
        

        self.__self = None
        self._next = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if next is not None:
            self.next = next

    @property
    def _self(self):
        """Gets the _self of this PageLink.

        当前资源的链接。

        :return: The _self of this PageLink.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this PageLink.

        当前资源的链接。

        :param _self: The _self of this PageLink.
        :type: str
        """
        self.__self = _self

    @property
    def next(self):
        """Gets the next of this PageLink.

        下一页资源的链接。

        :return: The next of this PageLink.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this PageLink.

        下一页资源的链接。

        :param next: The next of this PageLink.
        :type: str
        """
        self._next = next

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
        if not isinstance(other, PageLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
