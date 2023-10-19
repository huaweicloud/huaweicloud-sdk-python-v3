# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCentralNetworksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'page_info': 'PageInfo',
        'central_networks': 'list[CentralNetwork]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'page_info': 'page_info',
        'central_networks': 'central_networks'
    }

    def __init__(self, request_id=None, page_info=None, central_networks=None):
        """ListCentralNetworksResponse

        The model defined in huaweicloud sdk

        :param request_id: 资源ID标识符。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        :param central_networks: 中心网络列表。
        :type central_networks: list[:class:`huaweicloudsdkcc.v3.CentralNetwork`]
        """
        
        super(ListCentralNetworksResponse, self).__init__()

        self._request_id = None
        self._page_info = None
        self._central_networks = None
        self.discriminator = None

        self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info
        self.central_networks = central_networks

    @property
    def request_id(self):
        """Gets the request_id of this ListCentralNetworksResponse.

        资源ID标识符。

        :return: The request_id of this ListCentralNetworksResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListCentralNetworksResponse.

        资源ID标识符。

        :param request_id: The request_id of this ListCentralNetworksResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        """Gets the page_info of this ListCentralNetworksResponse.

        :return: The page_info of this ListCentralNetworksResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListCentralNetworksResponse.

        :param page_info: The page_info of this ListCentralNetworksResponse.
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def central_networks(self):
        """Gets the central_networks of this ListCentralNetworksResponse.

        中心网络列表。

        :return: The central_networks of this ListCentralNetworksResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.CentralNetwork`]
        """
        return self._central_networks

    @central_networks.setter
    def central_networks(self, central_networks):
        """Sets the central_networks of this ListCentralNetworksResponse.

        中心网络列表。

        :param central_networks: The central_networks of this ListCentralNetworksResponse.
        :type central_networks: list[:class:`huaweicloudsdkcc.v3.CentralNetwork`]
        """
        self._central_networks = central_networks

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
        if not isinstance(other, ListCentralNetworksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
