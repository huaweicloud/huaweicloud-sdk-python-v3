# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListResourceGroupResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_groups': 'list[ResourceGroupInfo]',
        'meta_data': 'TotalMetaData'
    }

    attribute_map = {
        'resource_groups': 'resource_groups',
        'meta_data': 'meta_data'
    }

    def __init__(self, resource_groups=None, meta_data=None):
        """ListResourceGroupResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._resource_groups = None
        self._meta_data = None
        self.discriminator = None

        if resource_groups is not None:
            self.resource_groups = resource_groups
        if meta_data is not None:
            self.meta_data = meta_data

    @property
    def resource_groups(self):
        """Gets the resource_groups of this ListResourceGroupResponse.

        一个或者多个资源分组信息。

        :return: The resource_groups of this ListResourceGroupResponse.
        :rtype: list[ResourceGroupInfo]
        """
        return self._resource_groups

    @resource_groups.setter
    def resource_groups(self, resource_groups):
        """Sets the resource_groups of this ListResourceGroupResponse.

        一个或者多个资源分组信息。

        :param resource_groups: The resource_groups of this ListResourceGroupResponse.
        :type: list[ResourceGroupInfo]
        """
        self._resource_groups = resource_groups

    @property
    def meta_data(self):
        """Gets the meta_data of this ListResourceGroupResponse.


        :return: The meta_data of this ListResourceGroupResponse.
        :rtype: TotalMetaData
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this ListResourceGroupResponse.


        :param meta_data: The meta_data of this ListResourceGroupResponse.
        :type: TotalMetaData
        """
        self._meta_data = meta_data

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
        if not isinstance(other, ListResourceGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
