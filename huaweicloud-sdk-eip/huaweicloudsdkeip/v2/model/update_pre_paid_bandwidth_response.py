# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdatePrePaidBandwidthResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bandwidth': 'BandwidthResp',
        'order_id': 'str'
    }

    attribute_map = {
        'bandwidth': 'bandwidth',
        'order_id': 'order_id'
    }

    def __init__(self, bandwidth=None, order_id=None):
        """UpdatePrePaidBandwidthResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._bandwidth = None
        self._order_id = None
        self.discriminator = None

        if bandwidth is not None:
            self.bandwidth = bandwidth
        if order_id is not None:
            self.order_id = order_id

    @property
    def bandwidth(self):
        """Gets the bandwidth of this UpdatePrePaidBandwidthResponse.


        :return: The bandwidth of this UpdatePrePaidBandwidthResponse.
        :rtype: BandwidthResp
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this UpdatePrePaidBandwidthResponse.


        :param bandwidth: The bandwidth of this UpdatePrePaidBandwidthResponse.
        :type: BandwidthResp
        """
        self._bandwidth = bandwidth

    @property
    def order_id(self):
        """Gets the order_id of this UpdatePrePaidBandwidthResponse.

        订单号（包周期场景返回该字段）

        :return: The order_id of this UpdatePrePaidBandwidthResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this UpdatePrePaidBandwidthResponse.

        订单号（包周期场景返回该字段）

        :param order_id: The order_id of this UpdatePrePaidBandwidthResponse.
        :type: str
        """
        self._order_id = order_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdatePrePaidBandwidthResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
