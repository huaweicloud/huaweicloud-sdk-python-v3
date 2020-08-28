# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListTemplatesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'page_number': 'int',
        'page_size': 'int',
        'content': 'TemplateView'
    }

    attribute_map = {
        'total': 'total',
        'page_number': 'page_number',
        'page_size': 'page_size',
        'content': 'content'
    }

    def __init__(self, total=None, page_number=None, page_size=None, content=None):
        """ListTemplatesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._total = None
        self._page_number = None
        self._page_size = None
        self._content = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if content is not None:
            self.content = content

    @property
    def total(self):
        """Gets the total of this ListTemplatesResponse.

        总数

        :return: The total of this ListTemplatesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListTemplatesResponse.

        总数

        :param total: The total of this ListTemplatesResponse.
        :type: int
        """
        self._total = total

    @property
    def page_number(self):
        """Gets the page_number of this ListTemplatesResponse.

        页码数

        :return: The page_number of this ListTemplatesResponse.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListTemplatesResponse.

        页码数

        :param page_number: The page_number of this ListTemplatesResponse.
        :type: int
        """
        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this ListTemplatesResponse.

        每页显示数

        :return: The page_size of this ListTemplatesResponse.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListTemplatesResponse.

        每页显示数

        :param page_size: The page_size of this ListTemplatesResponse.
        :type: int
        """
        self._page_size = page_size

    @property
    def content(self):
        """Gets the content of this ListTemplatesResponse.


        :return: The content of this ListTemplatesResponse.
        :rtype: TemplateView
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ListTemplatesResponse.


        :param content: The content of this ListTemplatesResponse.
        :type: TemplateView
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
        if not isinstance(other, ListTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
