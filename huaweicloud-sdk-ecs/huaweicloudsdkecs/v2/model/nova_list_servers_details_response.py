# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class NovaListServersDetailsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'servers': 'list[NovaServer]',
        'servers_links': 'list[PageLink]'
    }

    attribute_map = {
        'servers': 'servers',
        'servers_links': 'servers_links'
    }

    def __init__(self, servers=None, servers_links=None):
        """NovaListServersDetailsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._servers = None
        self._servers_links = None
        self.discriminator = None

        if servers is not None:
            self.servers = servers
        if servers_links is not None:
            self.servers_links = servers_links

    @property
    def servers(self):
        """Gets the servers of this NovaListServersDetailsResponse.

        查询云服务器信息列表。

        :return: The servers of this NovaListServersDetailsResponse.
        :rtype: list[NovaServer]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this NovaListServersDetailsResponse.

        查询云服务器信息列表。

        :param servers: The servers of this NovaListServersDetailsResponse.
        :type: list[NovaServer]
        """
        self._servers = servers

    @property
    def servers_links(self):
        """Gets the servers_links of this NovaListServersDetailsResponse.

        分页查询时，查询下一页数据链接。

        :return: The servers_links of this NovaListServersDetailsResponse.
        :rtype: list[PageLink]
        """
        return self._servers_links

    @servers_links.setter
    def servers_links(self, servers_links):
        """Sets the servers_links of this NovaListServersDetailsResponse.

        分页查询时，查询下一页数据链接。

        :param servers_links: The servers_links of this NovaListServersDetailsResponse.
        :type: list[PageLink]
        """
        self._servers_links = servers_links

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
        if not isinstance(other, NovaListServersDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
