# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMultiAccountTransferCouponsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'avail_transfer_coupons': 'list[AvailTransferCoupon]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'avail_transfer_coupons': 'avail_transfer_coupons'
    }

    def __init__(self, total_count=None, avail_transfer_coupons=None):
        """ListMultiAccountTransferCouponsResponse

        The model defined in huaweicloud sdk

        :param total_count: 记录条数。
        :type total_count: int
        :param avail_transfer_coupons: 可拨款优惠券记录。 具体请参见表2。
        :type avail_transfer_coupons: list[:class:`huaweicloudsdkbss.v2.AvailTransferCoupon`]
        """
        
        super(ListMultiAccountTransferCouponsResponse, self).__init__()

        self._total_count = None
        self._avail_transfer_coupons = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if avail_transfer_coupons is not None:
            self.avail_transfer_coupons = avail_transfer_coupons

    @property
    def total_count(self):
        """Gets the total_count of this ListMultiAccountTransferCouponsResponse.

        记录条数。

        :return: The total_count of this ListMultiAccountTransferCouponsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListMultiAccountTransferCouponsResponse.

        记录条数。

        :param total_count: The total_count of this ListMultiAccountTransferCouponsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def avail_transfer_coupons(self):
        """Gets the avail_transfer_coupons of this ListMultiAccountTransferCouponsResponse.

        可拨款优惠券记录。 具体请参见表2。

        :return: The avail_transfer_coupons of this ListMultiAccountTransferCouponsResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.AvailTransferCoupon`]
        """
        return self._avail_transfer_coupons

    @avail_transfer_coupons.setter
    def avail_transfer_coupons(self, avail_transfer_coupons):
        """Sets the avail_transfer_coupons of this ListMultiAccountTransferCouponsResponse.

        可拨款优惠券记录。 具体请参见表2。

        :param avail_transfer_coupons: The avail_transfer_coupons of this ListMultiAccountTransferCouponsResponse.
        :type avail_transfer_coupons: list[:class:`huaweicloudsdkbss.v2.AvailTransferCoupon`]
        """
        self._avail_transfer_coupons = avail_transfer_coupons

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
        if not isinstance(other, ListMultiAccountTransferCouponsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
