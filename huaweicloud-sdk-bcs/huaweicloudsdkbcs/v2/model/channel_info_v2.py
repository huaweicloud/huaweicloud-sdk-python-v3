# coding: utf-8

import pprint
import re

import six





class ChannelInfoV2:


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
        'org_names': 'list[str]',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'org_names': 'org_names',
        'description': 'description'
    }

    def __init__(self, name=None, org_names=None, description=None):
        """ChannelInfoV2 - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._org_names = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if org_names is not None:
            self.org_names = org_names
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this ChannelInfoV2.

        通道名

        :return: The name of this ChannelInfoV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChannelInfoV2.

        通道名

        :param name: The name of this ChannelInfoV2.
        :type: str
        """
        self._name = name

    @property
    def org_names(self):
        """Gets the org_names of this ChannelInfoV2.

        通道中组织名

        :return: The org_names of this ChannelInfoV2.
        :rtype: list[str]
        """
        return self._org_names

    @org_names.setter
    def org_names(self, org_names):
        """Sets the org_names of this ChannelInfoV2.

        通道中组织名

        :param org_names: The org_names of this ChannelInfoV2.
        :type: list[str]
        """
        self._org_names = org_names

    @property
    def description(self):
        """Gets the description of this ChannelInfoV2.

        通道描述

        :return: The description of this ChannelInfoV2.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChannelInfoV2.

        通道描述

        :param description: The description of this ChannelInfoV2.
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
        if not isinstance(other, ChannelInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
