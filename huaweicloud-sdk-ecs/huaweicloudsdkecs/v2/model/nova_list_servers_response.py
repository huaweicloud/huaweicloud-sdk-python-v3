# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaListServersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'servers': 'list[NovaSimpleServer]',
        'servers_links': 'list[PageLink]'
    }

    attribute_map = {
        'servers': 'servers',
        'servers_links': 'servers_links'
    }

    def __init__(self, servers=None, servers_links=None):
        r"""NovaListServersResponse

        The model defined in huaweicloud sdk

        :param servers: 查询云服务器信息列表
        :type servers: list[:class:`huaweicloudsdkecs.v2.NovaSimpleServer`]
        :param servers_links: 分页查询时，查询下一页数据链接。
        :type servers_links: list[:class:`huaweicloudsdkecs.v2.PageLink`]
        """
        
        super(NovaListServersResponse, self).__init__()

        self._servers = None
        self._servers_links = None
        self.discriminator = None

        if servers is not None:
            self.servers = servers
        if servers_links is not None:
            self.servers_links = servers_links

    @property
    def servers(self):
        r"""Gets the servers of this NovaListServersResponse.

        查询云服务器信息列表

        :return: The servers of this NovaListServersResponse.
        :rtype: list[:class:`huaweicloudsdkecs.v2.NovaSimpleServer`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        r"""Sets the servers of this NovaListServersResponse.

        查询云服务器信息列表

        :param servers: The servers of this NovaListServersResponse.
        :type servers: list[:class:`huaweicloudsdkecs.v2.NovaSimpleServer`]
        """
        self._servers = servers

    @property
    def servers_links(self):
        r"""Gets the servers_links of this NovaListServersResponse.

        分页查询时，查询下一页数据链接。

        :return: The servers_links of this NovaListServersResponse.
        :rtype: list[:class:`huaweicloudsdkecs.v2.PageLink`]
        """
        return self._servers_links

    @servers_links.setter
    def servers_links(self, servers_links):
        r"""Sets the servers_links of this NovaListServersResponse.

        分页查询时，查询下一页数据链接。

        :param servers_links: The servers_links of this NovaListServersResponse.
        :type servers_links: list[:class:`huaweicloudsdkecs.v2.PageLink`]
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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NovaListServersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
