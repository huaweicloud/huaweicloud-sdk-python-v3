# coding: utf-8

import pprint
import re

import six





class ListAddonTemplatesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'content_type': 'str',
        'addon_template_name': 'str'
    }

    attribute_map = {
        'content_type': 'Content-Type',
        'addon_template_name': 'addon_template_name'
    }

    def __init__(self, content_type='application/json', addon_template_name=None):
        """ListAddonTemplatesRequest - a model defined in huaweicloud sdk"""
        
        

        self._content_type = None
        self._addon_template_name = None
        self.discriminator = None

        self.content_type = content_type
        if addon_template_name is not None:
            self.addon_template_name = addon_template_name

    @property
    def content_type(self):
        """Gets the content_type of this ListAddonTemplatesRequest.


        :return: The content_type of this ListAddonTemplatesRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ListAddonTemplatesRequest.


        :param content_type: The content_type of this ListAddonTemplatesRequest.
        :type: str
        """
        self._content_type = content_type

    @property
    def addon_template_name(self):
        """Gets the addon_template_name of this ListAddonTemplatesRequest.


        :return: The addon_template_name of this ListAddonTemplatesRequest.
        :rtype: str
        """
        return self._addon_template_name

    @addon_template_name.setter
    def addon_template_name(self, addon_template_name):
        """Sets the addon_template_name of this ListAddonTemplatesRequest.


        :param addon_template_name: The addon_template_name of this ListAddonTemplatesRequest.
        :type: str
        """
        self._addon_template_name = addon_template_name

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
        if not isinstance(other, ListAddonTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
