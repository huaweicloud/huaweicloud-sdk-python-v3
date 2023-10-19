# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCentralNetworkAttachmentsResponse(SdkResponse):

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
        'central_network_attachments': 'list[CentralNetworkAttachment]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'page_info': 'page_info',
        'central_network_attachments': 'central_network_attachments'
    }

    def __init__(self, request_id=None, page_info=None, central_network_attachments=None):
        """ListCentralNetworkAttachmentsResponse

        The model defined in huaweicloud sdk

        :param request_id: 资源ID标识符。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        :param central_network_attachments: 接入网络实例连接列表。
        :type central_network_attachments: list[:class:`huaweicloudsdkcc.v3.CentralNetworkAttachment`]
        """
        
        super(ListCentralNetworkAttachmentsResponse, self).__init__()

        self._request_id = None
        self._page_info = None
        self._central_network_attachments = None
        self.discriminator = None

        self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info
        self.central_network_attachments = central_network_attachments

    @property
    def request_id(self):
        """Gets the request_id of this ListCentralNetworkAttachmentsResponse.

        资源ID标识符。

        :return: The request_id of this ListCentralNetworkAttachmentsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListCentralNetworkAttachmentsResponse.

        资源ID标识符。

        :param request_id: The request_id of this ListCentralNetworkAttachmentsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        """Gets the page_info of this ListCentralNetworkAttachmentsResponse.

        :return: The page_info of this ListCentralNetworkAttachmentsResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListCentralNetworkAttachmentsResponse.

        :param page_info: The page_info of this ListCentralNetworkAttachmentsResponse.
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def central_network_attachments(self):
        """Gets the central_network_attachments of this ListCentralNetworkAttachmentsResponse.

        接入网络实例连接列表。

        :return: The central_network_attachments of this ListCentralNetworkAttachmentsResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.CentralNetworkAttachment`]
        """
        return self._central_network_attachments

    @central_network_attachments.setter
    def central_network_attachments(self, central_network_attachments):
        """Sets the central_network_attachments of this ListCentralNetworkAttachmentsResponse.

        接入网络实例连接列表。

        :param central_network_attachments: The central_network_attachments of this ListCentralNetworkAttachmentsResponse.
        :type central_network_attachments: list[:class:`huaweicloudsdkcc.v3.CentralNetworkAttachment`]
        """
        self._central_network_attachments = central_network_attachments

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
        if not isinstance(other, ListCentralNetworkAttachmentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
