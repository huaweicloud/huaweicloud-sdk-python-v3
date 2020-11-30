# coding: utf-8

import pprint
import re

import six





class UpdateResourceGroupRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'resources': 'list[CreateResourceGroup]'
    }

    attribute_map = {
        'group_name': 'group_name',
        'resources': 'resources'
    }

    def __init__(self, group_name=None, resources=None):
        """UpdateResourceGroupRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._group_name = None
        self._resources = None
        self.discriminator = None

        self.group_name = group_name
        self.resources = resources

    @property
    def group_name(self):
        """Gets the group_name of this UpdateResourceGroupRequestBody.

        资源分组的名称；长度为1-128，只能包含0-9/a-z/A-Z/_/-或汉字；如：ResourceGroup-Test01。

        :return: The group_name of this UpdateResourceGroupRequestBody.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this UpdateResourceGroupRequestBody.

        资源分组的名称；长度为1-128，只能包含0-9/a-z/A-Z/_/-或汉字；如：ResourceGroup-Test01。

        :param group_name: The group_name of this UpdateResourceGroupRequestBody.
        :type: str
        """
        self._group_name = group_name

    @property
    def resources(self):
        """Gets the resources of this UpdateResourceGroupRequestBody.

        更新资源分组选择一个或者多个资源。

        :return: The resources of this UpdateResourceGroupRequestBody.
        :rtype: list[CreateResourceGroup]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this UpdateResourceGroupRequestBody.

        更新资源分组选择一个或者多个资源。

        :param resources: The resources of this UpdateResourceGroupRequestBody.
        :type: list[CreateResourceGroup]
        """
        self._resources = resources

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
        if not isinstance(other, UpdateResourceGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
