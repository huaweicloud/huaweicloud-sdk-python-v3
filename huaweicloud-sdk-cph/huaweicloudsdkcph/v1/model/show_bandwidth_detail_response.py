# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBandwidthDetailResponse(SdkResponse):

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
        'band_widths': 'list[object]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'band_widths': 'band_widths'
    }

    def __init__(self, request_id=None, band_widths=None):
        """ShowBandwidthDetailResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID
        :type request_id: str
        :param band_widths: 带宽信息
        :type band_widths: list[object]
        """
        
        super(ShowBandwidthDetailResponse, self).__init__()

        self._request_id = None
        self._band_widths = None
        self.discriminator = None

        self.request_id = request_id
        self.band_widths = band_widths

    @property
    def request_id(self):
        """Gets the request_id of this ShowBandwidthDetailResponse.

        请求的唯一标识ID

        :return: The request_id of this ShowBandwidthDetailResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowBandwidthDetailResponse.

        请求的唯一标识ID

        :param request_id: The request_id of this ShowBandwidthDetailResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def band_widths(self):
        """Gets the band_widths of this ShowBandwidthDetailResponse.

        带宽信息

        :return: The band_widths of this ShowBandwidthDetailResponse.
        :rtype: list[object]
        """
        return self._band_widths

    @band_widths.setter
    def band_widths(self, band_widths):
        """Sets the band_widths of this ShowBandwidthDetailResponse.

        带宽信息

        :param band_widths: The band_widths of this ShowBandwidthDetailResponse.
        :type band_widths: list[object]
        """
        self._band_widths = band_widths

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
        if not isinstance(other, ShowBandwidthDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
