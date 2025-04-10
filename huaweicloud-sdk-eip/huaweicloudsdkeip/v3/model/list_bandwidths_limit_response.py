# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBandwidthsLimitResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eip_bandwidth_limits': 'list[ShowTenantDict]',
        'page_info': 'PageInfoDict',
        'request_id': 'str'
    }

    attribute_map = {
        'eip_bandwidth_limits': 'eip_bandwidth_limits',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, eip_bandwidth_limits=None, page_info=None, request_id=None):
        r"""ListBandwidthsLimitResponse

        The model defined in huaweicloud sdk

        :param eip_bandwidth_limits: 带宽限制列表
        :type eip_bandwidth_limits: list[:class:`huaweicloudsdkeip.v3.ShowTenantDict`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkeip.v3.PageInfoDict`
        :param request_id: 本次请求编号
        :type request_id: str
        """
        
        super(ListBandwidthsLimitResponse, self).__init__()

        self._eip_bandwidth_limits = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if eip_bandwidth_limits is not None:
            self.eip_bandwidth_limits = eip_bandwidth_limits
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def eip_bandwidth_limits(self):
        r"""Gets the eip_bandwidth_limits of this ListBandwidthsLimitResponse.

        带宽限制列表

        :return: The eip_bandwidth_limits of this ListBandwidthsLimitResponse.
        :rtype: list[:class:`huaweicloudsdkeip.v3.ShowTenantDict`]
        """
        return self._eip_bandwidth_limits

    @eip_bandwidth_limits.setter
    def eip_bandwidth_limits(self, eip_bandwidth_limits):
        r"""Sets the eip_bandwidth_limits of this ListBandwidthsLimitResponse.

        带宽限制列表

        :param eip_bandwidth_limits: The eip_bandwidth_limits of this ListBandwidthsLimitResponse.
        :type eip_bandwidth_limits: list[:class:`huaweicloudsdkeip.v3.ShowTenantDict`]
        """
        self._eip_bandwidth_limits = eip_bandwidth_limits

    @property
    def page_info(self):
        r"""Gets the page_info of this ListBandwidthsLimitResponse.

        :return: The page_info of this ListBandwidthsLimitResponse.
        :rtype: :class:`huaweicloudsdkeip.v3.PageInfoDict`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListBandwidthsLimitResponse.

        :param page_info: The page_info of this ListBandwidthsLimitResponse.
        :type page_info: :class:`huaweicloudsdkeip.v3.PageInfoDict`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        r"""Gets the request_id of this ListBandwidthsLimitResponse.

        本次请求编号

        :return: The request_id of this ListBandwidthsLimitResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListBandwidthsLimitResponse.

        本次请求编号

        :param request_id: The request_id of this ListBandwidthsLimitResponse.
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
        if not isinstance(other, ListBandwidthsLimitResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
