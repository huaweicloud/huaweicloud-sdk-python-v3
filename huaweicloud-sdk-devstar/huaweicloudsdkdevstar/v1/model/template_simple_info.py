# coding: utf-8

import pprint
import re

import six





class TemplateSimpleInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'title': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'description': 'description'
    }

    def __init__(self, id=None, title=None, description=None):
        """TemplateSimpleInfo - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._title = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this TemplateSimpleInfo.

        模板id

        :return: The id of this TemplateSimpleInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateSimpleInfo.

        模板id

        :param id: The id of this TemplateSimpleInfo.
        :type: str
        """
        self._id = id

    @property
    def title(self):
        """Gets the title of this TemplateSimpleInfo.

        模板名

        :return: The title of this TemplateSimpleInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TemplateSimpleInfo.

        模板名

        :param title: The title of this TemplateSimpleInfo.
        :type: str
        """
        self._title = title

    @property
    def description(self):
        """Gets the description of this TemplateSimpleInfo.

        模板描述

        :return: The description of this TemplateSimpleInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TemplateSimpleInfo.

        模板描述

        :param description: The description of this TemplateSimpleInfo.
        :type: str
        """
        self._description = description

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
        if not isinstance(other, TemplateSimpleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
