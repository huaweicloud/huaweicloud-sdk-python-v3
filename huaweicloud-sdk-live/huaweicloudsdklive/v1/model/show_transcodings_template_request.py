# coding: utf-8

import pprint
import re

import six





class ShowTranscodingsTemplateRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'app_name': 'str',
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'domain': 'domain',
        'app_name': 'app_name',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, domain=None, app_name=None, page=0, size=10):
        """ShowTranscodingsTemplateRequest - a model defined in huaweicloud sdk"""
        
        

        self._domain = None
        self._app_name = None
        self._page = None
        self._size = None
        self.discriminator = None

        self.domain = domain
        if app_name is not None:
            self.app_name = app_name
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size

    @property
    def domain(self):
        """Gets the domain of this ShowTranscodingsTemplateRequest.


        :return: The domain of this ShowTranscodingsTemplateRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ShowTranscodingsTemplateRequest.


        :param domain: The domain of this ShowTranscodingsTemplateRequest.
        :type: str
        """
        self._domain = domain

    @property
    def app_name(self):
        """Gets the app_name of this ShowTranscodingsTemplateRequest.


        :return: The app_name of this ShowTranscodingsTemplateRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ShowTranscodingsTemplateRequest.


        :param app_name: The app_name of this ShowTranscodingsTemplateRequest.
        :type: str
        """
        self._app_name = app_name

    @property
    def page(self):
        """Gets the page of this ShowTranscodingsTemplateRequest.


        :return: The page of this ShowTranscodingsTemplateRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ShowTranscodingsTemplateRequest.


        :param page: The page of this ShowTranscodingsTemplateRequest.
        :type: int
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this ShowTranscodingsTemplateRequest.


        :return: The size of this ShowTranscodingsTemplateRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ShowTranscodingsTemplateRequest.


        :param size: The size of this ShowTranscodingsTemplateRequest.
        :type: int
        """
        self._size = size

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
        if not isinstance(other, ShowTranscodingsTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
