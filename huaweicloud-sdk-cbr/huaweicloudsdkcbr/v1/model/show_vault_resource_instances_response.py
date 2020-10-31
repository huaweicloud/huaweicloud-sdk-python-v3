# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowVaultResourceInstancesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resources': 'list[TagResource]',
        'total_count': 'int'
    }

    attribute_map = {
        'resources': 'resources',
        'total_count': 'total_count'
    }

    def __init__(self, resources=None, total_count=None):
        """ShowVaultResourceInstancesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._resources = None
        self._total_count = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if total_count is not None:
            self.total_count = total_count

    @property
    def resources(self):
        """Gets the resources of this ShowVaultResourceInstancesResponse.

        符合查询条件的资源列表（action为count时无此参数）。

        :return: The resources of this ShowVaultResourceInstancesResponse.
        :rtype: list[TagResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ShowVaultResourceInstancesResponse.

        符合查询条件的资源列表（action为count时无此参数）。

        :param resources: The resources of this ShowVaultResourceInstancesResponse.
        :type: list[TagResource]
        """
        self._resources = resources

    @property
    def total_count(self):
        """Gets the total_count of this ShowVaultResourceInstancesResponse.

        符合查询条件的资源总个数

        :return: The total_count of this ShowVaultResourceInstancesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ShowVaultResourceInstancesResponse.

        符合查询条件的资源总个数

        :param total_count: The total_count of this ShowVaultResourceInstancesResponse.
        :type: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ShowVaultResourceInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
