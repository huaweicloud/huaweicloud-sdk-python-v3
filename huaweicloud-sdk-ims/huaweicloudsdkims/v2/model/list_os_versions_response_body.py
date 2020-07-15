# coding: utf-8

import pprint
import re

import six





class ListOsVersionsResponseBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'platform': 'str',
        'version_list': 'list[OsVersionInfo]'
    }

    attribute_map = {
        'platform': 'platform',
        'version_list': 'version_list'
    }

    def __init__(self, platform=None, version_list=None):
        """ListOsVersionsResponseBody - a model defined in huaweicloud sdk"""
        
        

        self._platform = None
        self._version_list = None
        self.discriminator = None

        self.platform = platform
        self.version_list = version_list

    @property
    def platform(self):
        """Gets the platform of this ListOsVersionsResponseBody.

        操作系统的平台值，如RedHat等

        :return: The platform of this ListOsVersionsResponseBody.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ListOsVersionsResponseBody.

        操作系统的平台值，如RedHat等

        :param platform: The platform of this ListOsVersionsResponseBody.
        :type: str
        """
        self._platform = platform

    @property
    def version_list(self):
        """Gets the version_list of this ListOsVersionsResponseBody.

        操作系统的详情值

        :return: The version_list of this ListOsVersionsResponseBody.
        :rtype: list[OsVersionInfo]
        """
        return self._version_list

    @version_list.setter
    def version_list(self, version_list):
        """Sets the version_list of this ListOsVersionsResponseBody.

        操作系统的详情值

        :param version_list: The version_list of this ListOsVersionsResponseBody.
        :type: list[OsVersionInfo]
        """
        self._version_list = version_list

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
        if not isinstance(other, ListOsVersionsResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
