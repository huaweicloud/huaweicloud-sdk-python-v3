# coding: utf-8

import pprint
import re

import six





class ApplyConfigurationRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_ids': 'list[str]'
    }

    attribute_map = {
        'instance_ids': 'instance_ids'
    }

    def __init__(self, instance_ids=None):
        """ApplyConfigurationRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_ids = None
        self.discriminator = None

        self.instance_ids = instance_ids

    @property
    def instance_ids(self):
        """Gets the instance_ids of this ApplyConfigurationRequest.

        实例ID列表。

        :return: The instance_ids of this ApplyConfigurationRequest.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        """Sets the instance_ids of this ApplyConfigurationRequest.

        实例ID列表。

        :param instance_ids: The instance_ids of this ApplyConfigurationRequest.
        :type: list[str]
        """
        self._instance_ids = instance_ids

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
        if not isinstance(other, ApplyConfigurationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
