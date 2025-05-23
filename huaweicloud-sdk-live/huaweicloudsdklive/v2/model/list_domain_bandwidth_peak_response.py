# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainBandwidthPeakResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_list': 'list[PeakBandwidthData]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'bandwidth_list': 'bandwidth_list',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, bandwidth_list=None, x_request_id=None):
        r"""ListDomainBandwidthPeakResponse

        The model defined in huaweicloud sdk

        :param bandwidth_list: 域名对应的带宽峰值列表。
        :type bandwidth_list: list[:class:`huaweicloudsdklive.v2.PeakBandwidthData`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListDomainBandwidthPeakResponse, self).__init__()

        self._bandwidth_list = None
        self._x_request_id = None
        self.discriminator = None

        if bandwidth_list is not None:
            self.bandwidth_list = bandwidth_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def bandwidth_list(self):
        r"""Gets the bandwidth_list of this ListDomainBandwidthPeakResponse.

        域名对应的带宽峰值列表。

        :return: The bandwidth_list of this ListDomainBandwidthPeakResponse.
        :rtype: list[:class:`huaweicloudsdklive.v2.PeakBandwidthData`]
        """
        return self._bandwidth_list

    @bandwidth_list.setter
    def bandwidth_list(self, bandwidth_list):
        r"""Sets the bandwidth_list of this ListDomainBandwidthPeakResponse.

        域名对应的带宽峰值列表。

        :param bandwidth_list: The bandwidth_list of this ListDomainBandwidthPeakResponse.
        :type bandwidth_list: list[:class:`huaweicloudsdklive.v2.PeakBandwidthData`]
        """
        self._bandwidth_list = bandwidth_list

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListDomainBandwidthPeakResponse.

        :return: The x_request_id of this ListDomainBandwidthPeakResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListDomainBandwidthPeakResponse.

        :param x_request_id: The x_request_id of this ListDomainBandwidthPeakResponse.
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
        if not isinstance(other, ListDomainBandwidthPeakResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
