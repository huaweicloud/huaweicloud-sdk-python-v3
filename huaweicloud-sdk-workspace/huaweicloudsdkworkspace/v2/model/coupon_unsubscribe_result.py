# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CouponUnsubscribeResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'coupon_id': 'str',
        'coupon_type': 'str',
        'amount': 'float',
        'measure_id': 'int'
    }

    attribute_map = {
        'coupon_id': 'coupon_id',
        'coupon_type': 'coupon_type',
        'amount': 'amount',
        'measure_id': 'measure_id'
    }

    def __init__(self, coupon_id=None, coupon_type=None, amount=None, measure_id=None):
        r"""CouponUnsubscribeResult

        The model defined in huaweicloud sdk

        :param coupon_id: 券ID。
        :type coupon_id: str
        :param coupon_type: 券类型 302：现金券 303：储值卡。
        :type coupon_type: str
        :param amount: 券退的金额。
        :type amount: float
        :param measure_id: 度量单位。&#39;
        :type measure_id: int
        """
        
        

        self._coupon_id = None
        self._coupon_type = None
        self._amount = None
        self._measure_id = None
        self.discriminator = None

        if coupon_id is not None:
            self.coupon_id = coupon_id
        if coupon_type is not None:
            self.coupon_type = coupon_type
        if amount is not None:
            self.amount = amount
        if measure_id is not None:
            self.measure_id = measure_id

    @property
    def coupon_id(self):
        r"""Gets the coupon_id of this CouponUnsubscribeResult.

        券ID。

        :return: The coupon_id of this CouponUnsubscribeResult.
        :rtype: str
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        r"""Sets the coupon_id of this CouponUnsubscribeResult.

        券ID。

        :param coupon_id: The coupon_id of this CouponUnsubscribeResult.
        :type coupon_id: str
        """
        self._coupon_id = coupon_id

    @property
    def coupon_type(self):
        r"""Gets the coupon_type of this CouponUnsubscribeResult.

        券类型 302：现金券 303：储值卡。

        :return: The coupon_type of this CouponUnsubscribeResult.
        :rtype: str
        """
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, coupon_type):
        r"""Sets the coupon_type of this CouponUnsubscribeResult.

        券类型 302：现金券 303：储值卡。

        :param coupon_type: The coupon_type of this CouponUnsubscribeResult.
        :type coupon_type: str
        """
        self._coupon_type = coupon_type

    @property
    def amount(self):
        r"""Gets the amount of this CouponUnsubscribeResult.

        券退的金额。

        :return: The amount of this CouponUnsubscribeResult.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this CouponUnsubscribeResult.

        券退的金额。

        :param amount: The amount of this CouponUnsubscribeResult.
        :type amount: float
        """
        self._amount = amount

    @property
    def measure_id(self):
        r"""Gets the measure_id of this CouponUnsubscribeResult.

        度量单位。'

        :return: The measure_id of this CouponUnsubscribeResult.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        r"""Sets the measure_id of this CouponUnsubscribeResult.

        度量单位。'

        :param measure_id: The measure_id of this CouponUnsubscribeResult.
        :type measure_id: int
        """
        self._measure_id = measure_id

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
        if not isinstance(other, CouponUnsubscribeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
