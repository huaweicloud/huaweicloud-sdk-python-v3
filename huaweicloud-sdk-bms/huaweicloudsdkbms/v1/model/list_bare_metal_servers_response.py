# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListBareMetalServersResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'servers': 'list[ServerDetails]',
        'count': 'int'
    }

    attribute_map = {
        'servers': 'servers',
        'count': 'count'
    }

    def __init__(self, servers=None, count=None):
        """ListBareMetalServersResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._servers = None
        self._count = None
        self.discriminator = None

        if servers is not None:
            self.servers = servers
        if count is not None:
            self.count = count

    @property
    def servers(self):
        """Gets the servers of this ListBareMetalServersResponse.

        裸金属服务器详情列表

        :return: The servers of this ListBareMetalServersResponse.
        :rtype: list[ServerDetails]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this ListBareMetalServersResponse.

        裸金属服务器详情列表

        :param servers: The servers of this ListBareMetalServersResponse.
        :type: list[ServerDetails]
        """
        self._servers = servers

    @property
    def count(self):
        """Gets the count of this ListBareMetalServersResponse.

        裸金属服务器的列表总数

        :return: The count of this ListBareMetalServersResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListBareMetalServersResponse.

        裸金属服务器的列表总数

        :param count: The count of this ListBareMetalServersResponse.
        :type: int
        """
        self._count = count

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
        if not isinstance(other, ListBareMetalServersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
