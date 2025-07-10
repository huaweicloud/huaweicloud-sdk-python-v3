# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchResInquiryResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'product_id': 'str',
        'amount': 'float',
        'coupon_results': 'list[CouponUnsubscribeResult]',
        'discount_amount': 'float',
        'original_amount': 'float',
        'measure_id': 'int',
        'extend_params': 'str'
    }

    attribute_map = {
        'id': 'id',
        'product_id': 'product_id',
        'amount': 'amount',
        'coupon_results': 'coupon_results',
        'discount_amount': 'discount_amount',
        'original_amount': 'original_amount',
        'measure_id': 'measure_id',
        'extend_params': 'extend_params'
    }

    def __init__(self, id=None, product_id=None, amount=None, coupon_results=None, discount_amount=None, original_amount=None, measure_id=None, extend_params=None):
        r"""BatchResInquiryResult

        The model defined in huaweicloud sdk

        :param id: ID标识,同一次询价中不能重复。
        :type id: str
        :param product_id: 变更后的产品ID。
        :type product_id: str
        :param amount: 总额，即最终优惠后的金额(降配场景下包含退还的现金、现金券、储值卡的总额)。
        :type amount: float
        :param coupon_results: 券的退订金额（降配存在）。
        :type coupon_results: list[:class:`huaweicloudsdkworkspace.v2.CouponUnsubscribeResult`]
        :param discount_amount: 优惠额。
        :type discount_amount: float
        :param original_amount: 原总额，即优惠前总额。
        :type original_amount: float
        :param measure_id: 度量单位标识。
        :type measure_id: int
        :param extend_params: 扩展参数。
        :type extend_params: str
        """
        
        

        self._id = None
        self._product_id = None
        self._amount = None
        self._coupon_results = None
        self._discount_amount = None
        self._original_amount = None
        self._measure_id = None
        self._extend_params = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if product_id is not None:
            self.product_id = product_id
        if amount is not None:
            self.amount = amount
        if coupon_results is not None:
            self.coupon_results = coupon_results
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if original_amount is not None:
            self.original_amount = original_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if extend_params is not None:
            self.extend_params = extend_params

    @property
    def id(self):
        r"""Gets the id of this BatchResInquiryResult.

        ID标识,同一次询价中不能重复。

        :return: The id of this BatchResInquiryResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchResInquiryResult.

        ID标识,同一次询价中不能重复。

        :param id: The id of this BatchResInquiryResult.
        :type id: str
        """
        self._id = id

    @property
    def product_id(self):
        r"""Gets the product_id of this BatchResInquiryResult.

        变更后的产品ID。

        :return: The product_id of this BatchResInquiryResult.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this BatchResInquiryResult.

        变更后的产品ID。

        :param product_id: The product_id of this BatchResInquiryResult.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def amount(self):
        r"""Gets the amount of this BatchResInquiryResult.

        总额，即最终优惠后的金额(降配场景下包含退还的现金、现金券、储值卡的总额)。

        :return: The amount of this BatchResInquiryResult.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this BatchResInquiryResult.

        总额，即最终优惠后的金额(降配场景下包含退还的现金、现金券、储值卡的总额)。

        :param amount: The amount of this BatchResInquiryResult.
        :type amount: float
        """
        self._amount = amount

    @property
    def coupon_results(self):
        r"""Gets the coupon_results of this BatchResInquiryResult.

        券的退订金额（降配存在）。

        :return: The coupon_results of this BatchResInquiryResult.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.CouponUnsubscribeResult`]
        """
        return self._coupon_results

    @coupon_results.setter
    def coupon_results(self, coupon_results):
        r"""Sets the coupon_results of this BatchResInquiryResult.

        券的退订金额（降配存在）。

        :param coupon_results: The coupon_results of this BatchResInquiryResult.
        :type coupon_results: list[:class:`huaweicloudsdkworkspace.v2.CouponUnsubscribeResult`]
        """
        self._coupon_results = coupon_results

    @property
    def discount_amount(self):
        r"""Gets the discount_amount of this BatchResInquiryResult.

        优惠额。

        :return: The discount_amount of this BatchResInquiryResult.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        r"""Sets the discount_amount of this BatchResInquiryResult.

        优惠额。

        :param discount_amount: The discount_amount of this BatchResInquiryResult.
        :type discount_amount: float
        """
        self._discount_amount = discount_amount

    @property
    def original_amount(self):
        r"""Gets the original_amount of this BatchResInquiryResult.

        原总额，即优惠前总额。

        :return: The original_amount of this BatchResInquiryResult.
        :rtype: float
        """
        return self._original_amount

    @original_amount.setter
    def original_amount(self, original_amount):
        r"""Sets the original_amount of this BatchResInquiryResult.

        原总额，即优惠前总额。

        :param original_amount: The original_amount of this BatchResInquiryResult.
        :type original_amount: float
        """
        self._original_amount = original_amount

    @property
    def measure_id(self):
        r"""Gets the measure_id of this BatchResInquiryResult.

        度量单位标识。

        :return: The measure_id of this BatchResInquiryResult.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        r"""Sets the measure_id of this BatchResInquiryResult.

        度量单位标识。

        :param measure_id: The measure_id of this BatchResInquiryResult.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def extend_params(self):
        r"""Gets the extend_params of this BatchResInquiryResult.

        扩展参数。

        :return: The extend_params of this BatchResInquiryResult.
        :rtype: str
        """
        return self._extend_params

    @extend_params.setter
    def extend_params(self, extend_params):
        r"""Sets the extend_params of this BatchResInquiryResult.

        扩展参数。

        :param extend_params: The extend_params of this BatchResInquiryResult.
        :type extend_params: str
        """
        self._extend_params = extend_params

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
        if not isinstance(other, BatchResInquiryResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
