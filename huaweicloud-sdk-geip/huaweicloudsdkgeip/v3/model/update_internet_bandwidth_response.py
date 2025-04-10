# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInternetBandwidthResponse(SdkResponse):

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
        'internet_bandwidth': 'UpdateInternetBandwidth',
        'x_request_id': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'internet_bandwidth': 'internet_bandwidth',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, request_id=None, internet_bandwidth=None, x_request_id=None):
        r"""UpdateInternetBandwidthResponse

        The model defined in huaweicloud sdk

        :param request_id: 本次请求的编号
        :type request_id: str
        :param internet_bandwidth: 
        :type internet_bandwidth: :class:`huaweicloudsdkgeip.v3.UpdateInternetBandwidth`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(UpdateInternetBandwidthResponse, self).__init__()

        self._request_id = None
        self._internet_bandwidth = None
        self._x_request_id = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if internet_bandwidth is not None:
            self.internet_bandwidth = internet_bandwidth
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def request_id(self):
        r"""Gets the request_id of this UpdateInternetBandwidthResponse.

        本次请求的编号

        :return: The request_id of this UpdateInternetBandwidthResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this UpdateInternetBandwidthResponse.

        本次请求的编号

        :param request_id: The request_id of this UpdateInternetBandwidthResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def internet_bandwidth(self):
        r"""Gets the internet_bandwidth of this UpdateInternetBandwidthResponse.

        :return: The internet_bandwidth of this UpdateInternetBandwidthResponse.
        :rtype: :class:`huaweicloudsdkgeip.v3.UpdateInternetBandwidth`
        """
        return self._internet_bandwidth

    @internet_bandwidth.setter
    def internet_bandwidth(self, internet_bandwidth):
        r"""Sets the internet_bandwidth of this UpdateInternetBandwidthResponse.

        :param internet_bandwidth: The internet_bandwidth of this UpdateInternetBandwidthResponse.
        :type internet_bandwidth: :class:`huaweicloudsdkgeip.v3.UpdateInternetBandwidth`
        """
        self._internet_bandwidth = internet_bandwidth

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this UpdateInternetBandwidthResponse.

        :return: The x_request_id of this UpdateInternetBandwidthResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this UpdateInternetBandwidthResponse.

        :param x_request_id: The x_request_id of this UpdateInternetBandwidthResponse.
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
        if not isinstance(other, UpdateInternetBandwidthResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
