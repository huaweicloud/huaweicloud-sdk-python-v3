# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchInquiryChangeRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ret_code': 'str',
        'error_txt': 'str',
        'amount': 'float',
        'coupon_results': 'list[CouponUnsubscribeResult]',
        'discount_amount': 'float',
        'original_amount': 'float',
        'measure_id': 'int',
        'currency': 'str',
        'product_rating_result': 'list[BatchResInquiryResult]',
        'extend_params': 'str'
    }

    attribute_map = {
        'ret_code': 'ret_code',
        'error_txt': 'error_txt',
        'amount': 'amount',
        'coupon_results': 'coupon_results',
        'discount_amount': 'discount_amount',
        'original_amount': 'original_amount',
        'measure_id': 'measure_id',
        'currency': 'currency',
        'product_rating_result': 'product_rating_result',
        'extend_params': 'extend_params'
    }

    def __init__(self, ret_code=None, error_txt=None, amount=None, coupon_results=None, discount_amount=None, original_amount=None, measure_id=None, currency=None, product_rating_result=None, extend_params=None):
        r"""BatchInquiryChangeRsp

        The model defined in huaweicloud sdk

        :param ret_code: 返回码，恒为0。
        :type ret_code: str
        :param error_txt: 返回信息。
        :type error_txt: str
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
        :param currency: 货币单位代码（遵循ISO 4217标准）。
        :type currency: str
        :param product_rating_result: 批价结果。
        :type product_rating_result: list[:class:`huaweicloudsdkworkspace.v2.BatchResInquiryResult`]
        :param extend_params: 扩展参数。
        :type extend_params: str
        """
        
        

        self._ret_code = None
        self._error_txt = None
        self._amount = None
        self._coupon_results = None
        self._discount_amount = None
        self._original_amount = None
        self._measure_id = None
        self._currency = None
        self._product_rating_result = None
        self._extend_params = None
        self.discriminator = None

        if ret_code is not None:
            self.ret_code = ret_code
        if error_txt is not None:
            self.error_txt = error_txt
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
        if currency is not None:
            self.currency = currency
        if product_rating_result is not None:
            self.product_rating_result = product_rating_result
        if extend_params is not None:
            self.extend_params = extend_params

    @property
    def ret_code(self):
        r"""Gets the ret_code of this BatchInquiryChangeRsp.

        返回码，恒为0。

        :return: The ret_code of this BatchInquiryChangeRsp.
        :rtype: str
        """
        return self._ret_code

    @ret_code.setter
    def ret_code(self, ret_code):
        r"""Sets the ret_code of this BatchInquiryChangeRsp.

        返回码，恒为0。

        :param ret_code: The ret_code of this BatchInquiryChangeRsp.
        :type ret_code: str
        """
        self._ret_code = ret_code

    @property
    def error_txt(self):
        r"""Gets the error_txt of this BatchInquiryChangeRsp.

        返回信息。

        :return: The error_txt of this BatchInquiryChangeRsp.
        :rtype: str
        """
        return self._error_txt

    @error_txt.setter
    def error_txt(self, error_txt):
        r"""Sets the error_txt of this BatchInquiryChangeRsp.

        返回信息。

        :param error_txt: The error_txt of this BatchInquiryChangeRsp.
        :type error_txt: str
        """
        self._error_txt = error_txt

    @property
    def amount(self):
        r"""Gets the amount of this BatchInquiryChangeRsp.

        总额，即最终优惠后的金额(降配场景下包含退还的现金、现金券、储值卡的总额)。

        :return: The amount of this BatchInquiryChangeRsp.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this BatchInquiryChangeRsp.

        总额，即最终优惠后的金额(降配场景下包含退还的现金、现金券、储值卡的总额)。

        :param amount: The amount of this BatchInquiryChangeRsp.
        :type amount: float
        """
        self._amount = amount

    @property
    def coupon_results(self):
        r"""Gets the coupon_results of this BatchInquiryChangeRsp.

        券的退订金额（降配存在）。

        :return: The coupon_results of this BatchInquiryChangeRsp.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.CouponUnsubscribeResult`]
        """
        return self._coupon_results

    @coupon_results.setter
    def coupon_results(self, coupon_results):
        r"""Sets the coupon_results of this BatchInquiryChangeRsp.

        券的退订金额（降配存在）。

        :param coupon_results: The coupon_results of this BatchInquiryChangeRsp.
        :type coupon_results: list[:class:`huaweicloudsdkworkspace.v2.CouponUnsubscribeResult`]
        """
        self._coupon_results = coupon_results

    @property
    def discount_amount(self):
        r"""Gets the discount_amount of this BatchInquiryChangeRsp.

        优惠额。

        :return: The discount_amount of this BatchInquiryChangeRsp.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        r"""Sets the discount_amount of this BatchInquiryChangeRsp.

        优惠额。

        :param discount_amount: The discount_amount of this BatchInquiryChangeRsp.
        :type discount_amount: float
        """
        self._discount_amount = discount_amount

    @property
    def original_amount(self):
        r"""Gets the original_amount of this BatchInquiryChangeRsp.

        原总额，即优惠前总额。

        :return: The original_amount of this BatchInquiryChangeRsp.
        :rtype: float
        """
        return self._original_amount

    @original_amount.setter
    def original_amount(self, original_amount):
        r"""Sets the original_amount of this BatchInquiryChangeRsp.

        原总额，即优惠前总额。

        :param original_amount: The original_amount of this BatchInquiryChangeRsp.
        :type original_amount: float
        """
        self._original_amount = original_amount

    @property
    def measure_id(self):
        r"""Gets the measure_id of this BatchInquiryChangeRsp.

        度量单位标识。

        :return: The measure_id of this BatchInquiryChangeRsp.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        r"""Sets the measure_id of this BatchInquiryChangeRsp.

        度量单位标识。

        :param measure_id: The measure_id of this BatchInquiryChangeRsp.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def currency(self):
        r"""Gets the currency of this BatchInquiryChangeRsp.

        货币单位代码（遵循ISO 4217标准）。

        :return: The currency of this BatchInquiryChangeRsp.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        r"""Sets the currency of this BatchInquiryChangeRsp.

        货币单位代码（遵循ISO 4217标准）。

        :param currency: The currency of this BatchInquiryChangeRsp.
        :type currency: str
        """
        self._currency = currency

    @property
    def product_rating_result(self):
        r"""Gets the product_rating_result of this BatchInquiryChangeRsp.

        批价结果。

        :return: The product_rating_result of this BatchInquiryChangeRsp.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.BatchResInquiryResult`]
        """
        return self._product_rating_result

    @product_rating_result.setter
    def product_rating_result(self, product_rating_result):
        r"""Sets the product_rating_result of this BatchInquiryChangeRsp.

        批价结果。

        :param product_rating_result: The product_rating_result of this BatchInquiryChangeRsp.
        :type product_rating_result: list[:class:`huaweicloudsdkworkspace.v2.BatchResInquiryResult`]
        """
        self._product_rating_result = product_rating_result

    @property
    def extend_params(self):
        r"""Gets the extend_params of this BatchInquiryChangeRsp.

        扩展参数。

        :return: The extend_params of this BatchInquiryChangeRsp.
        :rtype: str
        """
        return self._extend_params

    @extend_params.setter
    def extend_params(self, extend_params):
        r"""Sets the extend_params of this BatchInquiryChangeRsp.

        扩展参数。

        :param extend_params: The extend_params of this BatchInquiryChangeRsp.
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
        if not isinstance(other, BatchInquiryChangeRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
