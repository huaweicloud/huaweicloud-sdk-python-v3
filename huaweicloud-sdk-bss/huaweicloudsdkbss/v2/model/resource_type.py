# coding: utf-8

import pprint
import re

import six





class ResourceType:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_type_code': 'str',
        'resource_type_name': 'str',
        'resource_type_desc': 'str'
    }

    attribute_map = {
        'resource_type_code': 'resource_type_code',
        'resource_type_name': 'resource_type_name',
        'resource_type_desc': 'resource_type_desc'
    }

    def __init__(self, resource_type_code=None, resource_type_name=None, resource_type_desc=None):
        """ResourceType - a model defined in huaweicloud sdk"""
        
        

        self._resource_type_code = None
        self._resource_type_name = None
        self._resource_type_desc = None
        self.discriminator = None

        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if resource_type_desc is not None:
            self.resource_type_desc = resource_type_desc

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this ResourceType.

        |参数名称：资源类型编码| |参数约束及描述：资源类型编码|

        :return: The resource_type_code of this ResourceType.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this ResourceType.

        |参数名称：资源类型编码| |参数约束及描述：资源类型编码|

        :param resource_type_code: The resource_type_code of this ResourceType.
        :type: str
        """
        self._resource_type_code = resource_type_code

    @property
    def resource_type_name(self):
        """Gets the resource_type_name of this ResourceType.

        |参数名称：资源类型名称| |参数约束及描述：资源类型名称|

        :return: The resource_type_name of this ResourceType.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        """Sets the resource_type_name of this ResourceType.

        |参数名称：资源类型名称| |参数约束及描述：资源类型名称|

        :param resource_type_name: The resource_type_name of this ResourceType.
        :type: str
        """
        self._resource_type_name = resource_type_name

    @property
    def resource_type_desc(self):
        """Gets the resource_type_desc of this ResourceType.

        |参数名称：资源类型描述| |参数约束及描述：资源类型描述|

        :return: The resource_type_desc of this ResourceType.
        :rtype: str
        """
        return self._resource_type_desc

    @resource_type_desc.setter
    def resource_type_desc(self, resource_type_desc):
        """Sets the resource_type_desc of this ResourceType.

        |参数名称：资源类型描述| |参数约束及描述：资源类型描述|

        :param resource_type_desc: The resource_type_desc of this ResourceType.
        :type: str
        """
        self._resource_type_desc = resource_type_desc

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
        if not isinstance(other, ResourceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
