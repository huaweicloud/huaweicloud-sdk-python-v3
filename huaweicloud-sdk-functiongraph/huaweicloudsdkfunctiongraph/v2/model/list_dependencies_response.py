# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListDependenciesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'dependencies': 'list[ListDependenciesResult]',
        'next_marker': 'int'
    }

    attribute_map = {
        'count': 'count',
        'dependencies': 'dependencies',
        'next_marker': 'next_marker'
    }

    def __init__(self, count=None, dependencies=None, next_marker=None):
        """ListDependenciesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._count = None
        self._dependencies = None
        self._next_marker = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if dependencies is not None:
            self.dependencies = dependencies
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def count(self):
        """Gets the count of this ListDependenciesResponse.

        依赖包总数。

        :return: The count of this ListDependenciesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListDependenciesResponse.

        依赖包总数。

        :param count: The count of this ListDependenciesResponse.
        :type: int
        """
        self._count = count

    @property
    def dependencies(self):
        """Gets the dependencies of this ListDependenciesResponse.

        依赖包列表。

        :return: The dependencies of this ListDependenciesResponse.
        :rtype: list[ListDependenciesResult]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this ListDependenciesResponse.

        依赖包列表。

        :param dependencies: The dependencies of this ListDependenciesResponse.
        :type: list[ListDependenciesResult]
        """
        self._dependencies = dependencies

    @property
    def next_marker(self):
        """Gets the next_marker of this ListDependenciesResponse.

        下次读取位置。

        :return: The next_marker of this ListDependenciesResponse.
        :rtype: int
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        """Sets the next_marker of this ListDependenciesResponse.

        下次读取位置。

        :param next_marker: The next_marker of this ListDependenciesResponse.
        :type: int
        """
        self._next_marker = next_marker

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
        if not isinstance(other, ListDependenciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
