# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSupportMasksResponse(SdkResponse):

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
        'support_masks': 'list[ListSupportMasks]',
        'page_info': 'ListGlobalEipsResponseBodyPageInfo',
        'x_request_id': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'support_masks': 'support_masks',
        'page_info': 'page_info',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, request_id=None, support_masks=None, page_info=None, x_request_id=None):
        r"""ListSupportMasksResponse

        The model defined in huaweicloud sdk

        :param request_id: 本次请求的编号
        :type request_id: str
        :param support_masks: 支持全域弹性公网IP段的掩码范围列表
        :type support_masks: list[:class:`huaweicloudsdkgeip.v3.ListSupportMasks`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkgeip.v3.ListGlobalEipsResponseBodyPageInfo`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListSupportMasksResponse, self).__init__()

        self._request_id = None
        self._support_masks = None
        self._page_info = None
        self._x_request_id = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if support_masks is not None:
            self.support_masks = support_masks
        if page_info is not None:
            self.page_info = page_info
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def request_id(self):
        r"""Gets the request_id of this ListSupportMasksResponse.

        本次请求的编号

        :return: The request_id of this ListSupportMasksResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListSupportMasksResponse.

        本次请求的编号

        :param request_id: The request_id of this ListSupportMasksResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def support_masks(self):
        r"""Gets the support_masks of this ListSupportMasksResponse.

        支持全域弹性公网IP段的掩码范围列表

        :return: The support_masks of this ListSupportMasksResponse.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.ListSupportMasks`]
        """
        return self._support_masks

    @support_masks.setter
    def support_masks(self, support_masks):
        r"""Sets the support_masks of this ListSupportMasksResponse.

        支持全域弹性公网IP段的掩码范围列表

        :param support_masks: The support_masks of this ListSupportMasksResponse.
        :type support_masks: list[:class:`huaweicloudsdkgeip.v3.ListSupportMasks`]
        """
        self._support_masks = support_masks

    @property
    def page_info(self):
        r"""Gets the page_info of this ListSupportMasksResponse.

        :return: The page_info of this ListSupportMasksResponse.
        :rtype: :class:`huaweicloudsdkgeip.v3.ListGlobalEipsResponseBodyPageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListSupportMasksResponse.

        :param page_info: The page_info of this ListSupportMasksResponse.
        :type page_info: :class:`huaweicloudsdkgeip.v3.ListGlobalEipsResponseBodyPageInfo`
        """
        self._page_info = page_info

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListSupportMasksResponse.

        :return: The x_request_id of this ListSupportMasksResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListSupportMasksResponse.

        :param x_request_id: The x_request_id of this ListSupportMasksResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListSupportMasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
