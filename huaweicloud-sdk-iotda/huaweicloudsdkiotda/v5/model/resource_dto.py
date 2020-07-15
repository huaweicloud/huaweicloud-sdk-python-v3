# coding: utf-8

import pprint
import re

import six





class ResourceDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_id': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id'
    }

    def __init__(self, resource_id=None):
        """ResourceDTO - a model defined in huaweicloud sdk"""
        
        

        self._resource_id = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id

    @property
    def resource_id(self):
        """Gets the resource_id of this ResourceDTO.

        资源id。例如，要查询的资源类型为device，那么对应的资源id就是device_id。

        :return: The resource_id of this ResourceDTO.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ResourceDTO.

        资源id。例如，要查询的资源类型为device，那么对应的资源id就是device_id。

        :param resource_id: The resource_id of this ResourceDTO.
        :type: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, ResourceDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
