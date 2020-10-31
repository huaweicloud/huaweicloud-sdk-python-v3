# coding: utf-8

import pprint
import re

import six





class Reference:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'url': 'str',
        'type': 'int',
        'productshort': 'str'
    }

    attribute_map = {
        'title': 'title',
        'url': 'url',
        'type': 'type',
        'productshort': 'productshort'
    }

    def __init__(self, title=None, url=None, type=None, productshort=None):
        """Reference - a model defined in huaweicloud sdk"""
        
        

        self._title = None
        self._url = None
        self._type = None
        self._productshort = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if url is not None:
            self.url = url
        if type is not None:
            self.type = type
        if productshort is not None:
            self.productshort = productshort

    @property
    def title(self):
        """Gets the title of this Reference.

        标题名称

        :return: The title of this Reference.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Reference.

        标题名称

        :param title: The title of this Reference.
        :type: str
        """
        self._title = title

    @property
    def url(self):
        """Gets the url of this Reference.

        链接地址

        :return: The url of this Reference.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Reference.

        链接地址

        :param url: The url of this Reference.
        :type: str
        """
        self._url = url

    @property
    def type(self):
        """Gets the type of this Reference.

        关联类型

        :return: The type of this Reference.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Reference.

        关联类型

        :param type: The type of this Reference.
        :type: int
        """
        self._type = type

    @property
    def productshort(self):
        """Gets the productshort of this Reference.

        产品短名

        :return: The productshort of this Reference.
        :rtype: str
        """
        return self._productshort

    @productshort.setter
    def productshort(self, productshort):
        """Sets the productshort of this Reference.

        产品短名

        :param productshort: The productshort of this Reference.
        :type: str
        """
        self._productshort = productshort

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
        if not isinstance(other, Reference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
