# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalConnectionBandwidthSpecCodesResponse(SdkResponse):

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
        'spec_codes': 'list[GlobalConnectionBandwidthSpecCode]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'page_info': 'page_info',
        'spec_codes': 'spec_codes'
    }

    def __init__(self, request_id=None, page_info=None, spec_codes=None):
        r"""ListGlobalConnectionBandwidthSpecCodesResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        :param spec_codes: 线路规格列表响应体。
        :type spec_codes: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidthSpecCode`]
        """
        
        super(ListGlobalConnectionBandwidthSpecCodesResponse, self).__init__()

        self._request_id = None
        self._page_info = None
        self._spec_codes = None
        self.discriminator = None

        self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info
        self.spec_codes = spec_codes

    @property
    def request_id(self):
        r"""Gets the request_id of this ListGlobalConnectionBandwidthSpecCodesResponse.

        请求ID。

        :return: The request_id of this ListGlobalConnectionBandwidthSpecCodesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListGlobalConnectionBandwidthSpecCodesResponse.

        请求ID。

        :param request_id: The request_id of this ListGlobalConnectionBandwidthSpecCodesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        r"""Gets the page_info of this ListGlobalConnectionBandwidthSpecCodesResponse.

        :return: The page_info of this ListGlobalConnectionBandwidthSpecCodesResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListGlobalConnectionBandwidthSpecCodesResponse.

        :param page_info: The page_info of this ListGlobalConnectionBandwidthSpecCodesResponse.
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def spec_codes(self):
        r"""Gets the spec_codes of this ListGlobalConnectionBandwidthSpecCodesResponse.

        线路规格列表响应体。

        :return: The spec_codes of this ListGlobalConnectionBandwidthSpecCodesResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidthSpecCode`]
        """
        return self._spec_codes

    @spec_codes.setter
    def spec_codes(self, spec_codes):
        r"""Sets the spec_codes of this ListGlobalConnectionBandwidthSpecCodesResponse.

        线路规格列表响应体。

        :param spec_codes: The spec_codes of this ListGlobalConnectionBandwidthSpecCodesResponse.
        :type spec_codes: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidthSpecCode`]
        """
        self._spec_codes = spec_codes

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
        if not isinstance(other, ListGlobalConnectionBandwidthSpecCodesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
