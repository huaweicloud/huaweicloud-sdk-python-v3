# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudServersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'servers': 'list[CloudServer]',
        'servers_links': 'list[PageLink]',
        'request_id': 'str'
    }

    attribute_map = {
        'servers': 'servers',
        'servers_links': 'servers_links',
        'request_id': 'request_id'
    }

    def __init__(self, servers=None, servers_links=None, request_id=None):
        r"""ListCloudServersResponse

        The model defined in huaweicloud sdk

        :param servers: 查询云服务器信息列表。
        :type servers: list[:class:`huaweicloudsdkecs.v2.CloudServer`]
        :param servers_links: 分页查询时，查询下一页数据链接。
        :type servers_links: list[:class:`huaweicloudsdkecs.v2.PageLink`]
        :param request_id: 
        :type request_id: str
        """
        
        super(ListCloudServersResponse, self).__init__()

        self._servers = None
        self._servers_links = None
        self._request_id = None
        self.discriminator = None

        if servers is not None:
            self.servers = servers
        if servers_links is not None:
            self.servers_links = servers_links
        if request_id is not None:
            self.request_id = request_id

    @property
    def servers(self):
        r"""Gets the servers of this ListCloudServersResponse.

        查询云服务器信息列表。

        :return: The servers of this ListCloudServersResponse.
        :rtype: list[:class:`huaweicloudsdkecs.v2.CloudServer`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        r"""Sets the servers of this ListCloudServersResponse.

        查询云服务器信息列表。

        :param servers: The servers of this ListCloudServersResponse.
        :type servers: list[:class:`huaweicloudsdkecs.v2.CloudServer`]
        """
        self._servers = servers

    @property
    def servers_links(self):
        r"""Gets the servers_links of this ListCloudServersResponse.

        分页查询时，查询下一页数据链接。

        :return: The servers_links of this ListCloudServersResponse.
        :rtype: list[:class:`huaweicloudsdkecs.v2.PageLink`]
        """
        return self._servers_links

    @servers_links.setter
    def servers_links(self, servers_links):
        r"""Sets the servers_links of this ListCloudServersResponse.

        分页查询时，查询下一页数据链接。

        :param servers_links: The servers_links of this ListCloudServersResponse.
        :type servers_links: list[:class:`huaweicloudsdkecs.v2.PageLink`]
        """
        self._servers_links = servers_links

    @property
    def request_id(self):
        r"""Gets the request_id of this ListCloudServersResponse.

        :return: The request_id of this ListCloudServersResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListCloudServersResponse.

        :param request_id: The request_id of this ListCloudServersResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ListCloudServersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
