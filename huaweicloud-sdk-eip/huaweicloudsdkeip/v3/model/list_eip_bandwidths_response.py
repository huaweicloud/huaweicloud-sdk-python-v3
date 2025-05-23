# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEipBandwidthsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eip_bandwidths': 'list[EipBandwidthResponseBody]',
        'page_info': 'PageInfoDict',
        'request_id': 'str'
    }

    attribute_map = {
        'eip_bandwidths': 'eip_bandwidths',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, eip_bandwidths=None, page_info=None, request_id=None):
        r"""ListEipBandwidthsResponse

        The model defined in huaweicloud sdk

        :param eip_bandwidths: 带宽列表对象
        :type eip_bandwidths: list[:class:`huaweicloudsdkeip.v3.EipBandwidthResponseBody`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkeip.v3.PageInfoDict`
        :param request_id: 本次请求的编号
        :type request_id: str
        """
        
        super(ListEipBandwidthsResponse, self).__init__()

        self._eip_bandwidths = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if eip_bandwidths is not None:
            self.eip_bandwidths = eip_bandwidths
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def eip_bandwidths(self):
        r"""Gets the eip_bandwidths of this ListEipBandwidthsResponse.

        带宽列表对象

        :return: The eip_bandwidths of this ListEipBandwidthsResponse.
        :rtype: list[:class:`huaweicloudsdkeip.v3.EipBandwidthResponseBody`]
        """
        return self._eip_bandwidths

    @eip_bandwidths.setter
    def eip_bandwidths(self, eip_bandwidths):
        r"""Sets the eip_bandwidths of this ListEipBandwidthsResponse.

        带宽列表对象

        :param eip_bandwidths: The eip_bandwidths of this ListEipBandwidthsResponse.
        :type eip_bandwidths: list[:class:`huaweicloudsdkeip.v3.EipBandwidthResponseBody`]
        """
        self._eip_bandwidths = eip_bandwidths

    @property
    def page_info(self):
        r"""Gets the page_info of this ListEipBandwidthsResponse.

        :return: The page_info of this ListEipBandwidthsResponse.
        :rtype: :class:`huaweicloudsdkeip.v3.PageInfoDict`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListEipBandwidthsResponse.

        :param page_info: The page_info of this ListEipBandwidthsResponse.
        :type page_info: :class:`huaweicloudsdkeip.v3.PageInfoDict`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        r"""Gets the request_id of this ListEipBandwidthsResponse.

        本次请求的编号

        :return: The request_id of this ListEipBandwidthsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListEipBandwidthsResponse.

        本次请求的编号

        :param request_id: The request_id of this ListEipBandwidthsResponse.
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
        if not isinstance(other, ListEipBandwidthsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
