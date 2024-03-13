# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSupportBindingConnectionBandwidthsResponse(SdkResponse):

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
        'globalconnection_bandwidths': 'list[GlobalConnectionBandwidth]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'page_info': 'page_info',
        'globalconnection_bandwidths': 'globalconnection_bandwidths'
    }

    def __init__(self, request_id=None, page_info=None, globalconnection_bandwidths=None):
        """ListSupportBindingConnectionBandwidthsResponse

        The model defined in huaweicloud sdk

        :param request_id: 资源ID标识符。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        :param globalconnection_bandwidths: 全域互联带宽列表响应体。
        :type globalconnection_bandwidths: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidth`]
        """
        
        super(ListSupportBindingConnectionBandwidthsResponse, self).__init__()

        self._request_id = None
        self._page_info = None
        self._globalconnection_bandwidths = None
        self.discriminator = None

        self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info
        self.globalconnection_bandwidths = globalconnection_bandwidths

    @property
    def request_id(self):
        """Gets the request_id of this ListSupportBindingConnectionBandwidthsResponse.

        资源ID标识符。

        :return: The request_id of this ListSupportBindingConnectionBandwidthsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListSupportBindingConnectionBandwidthsResponse.

        资源ID标识符。

        :param request_id: The request_id of this ListSupportBindingConnectionBandwidthsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        """Gets the page_info of this ListSupportBindingConnectionBandwidthsResponse.

        :return: The page_info of this ListSupportBindingConnectionBandwidthsResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListSupportBindingConnectionBandwidthsResponse.

        :param page_info: The page_info of this ListSupportBindingConnectionBandwidthsResponse.
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def globalconnection_bandwidths(self):
        """Gets the globalconnection_bandwidths of this ListSupportBindingConnectionBandwidthsResponse.

        全域互联带宽列表响应体。

        :return: The globalconnection_bandwidths of this ListSupportBindingConnectionBandwidthsResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidth`]
        """
        return self._globalconnection_bandwidths

    @globalconnection_bandwidths.setter
    def globalconnection_bandwidths(self, globalconnection_bandwidths):
        """Sets the globalconnection_bandwidths of this ListSupportBindingConnectionBandwidthsResponse.

        全域互联带宽列表响应体。

        :param globalconnection_bandwidths: The globalconnection_bandwidths of this ListSupportBindingConnectionBandwidthsResponse.
        :type globalconnection_bandwidths: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidth`]
        """
        self._globalconnection_bandwidths = globalconnection_bandwidths

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
        if not isinstance(other, ListSupportBindingConnectionBandwidthsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
