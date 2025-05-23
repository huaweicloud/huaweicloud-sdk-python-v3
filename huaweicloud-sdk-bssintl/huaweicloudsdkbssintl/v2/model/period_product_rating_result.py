# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PeriodProductRatingResult:

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
        'amount': 'decimal.Decimal',
        'official_website_amount': 'decimal.Decimal',
        'discount_amount': 'decimal.Decimal',
        'measure_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'product_id': 'product_id',
        'amount': 'amount',
        'official_website_amount': 'official_website_amount',
        'discount_amount': 'discount_amount',
        'measure_id': 'measure_id'
    }

    def __init__(self, id=None, product_id=None, amount=None, official_website_amount=None, discount_amount=None, measure_id=None):
        r"""PeriodProductRatingResult

        The model defined in huaweicloud sdk

        :param id: ID标识，来源于请求中的ID。
        :type id: str
        :param product_id: 包年/包月产品的ID。
        :type product_id: str
        :param amount: 总额，即最终优惠后的金额。 amount&#x3D; official_website_amount - discountAmount。
        :type amount: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        :param official_website_amount: 包年/包月产品的官网价。
        :type official_website_amount: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        :param discount_amount: 可选折扣优惠额，如商务折扣、伙伴折扣、促销折扣和折扣券选用时的优惠额。
        :type discount_amount: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        :param measure_id: 价格度量单位标识。 1：元
        :type measure_id: int
        """
        
        

        self._id = None
        self._product_id = None
        self._amount = None
        self._official_website_amount = None
        self._discount_amount = None
        self._measure_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if product_id is not None:
            self.product_id = product_id
        if amount is not None:
            self.amount = amount
        if official_website_amount is not None:
            self.official_website_amount = official_website_amount
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if measure_id is not None:
            self.measure_id = measure_id

    @property
    def id(self):
        r"""Gets the id of this PeriodProductRatingResult.

        ID标识，来源于请求中的ID。

        :return: The id of this PeriodProductRatingResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PeriodProductRatingResult.

        ID标识，来源于请求中的ID。

        :param id: The id of this PeriodProductRatingResult.
        :type id: str
        """
        self._id = id

    @property
    def product_id(self):
        r"""Gets the product_id of this PeriodProductRatingResult.

        包年/包月产品的ID。

        :return: The product_id of this PeriodProductRatingResult.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this PeriodProductRatingResult.

        包年/包月产品的ID。

        :param product_id: The product_id of this PeriodProductRatingResult.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def amount(self):
        r"""Gets the amount of this PeriodProductRatingResult.

        总额，即最终优惠后的金额。 amount= official_website_amount - discountAmount。

        :return: The amount of this PeriodProductRatingResult.
        :rtype: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this PeriodProductRatingResult.

        总额，即最终优惠后的金额。 amount= official_website_amount - discountAmount。

        :param amount: The amount of this PeriodProductRatingResult.
        :type amount: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        self._amount = amount

    @property
    def official_website_amount(self):
        r"""Gets the official_website_amount of this PeriodProductRatingResult.

        包年/包月产品的官网价。

        :return: The official_website_amount of this PeriodProductRatingResult.
        :rtype: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        return self._official_website_amount

    @official_website_amount.setter
    def official_website_amount(self, official_website_amount):
        r"""Sets the official_website_amount of this PeriodProductRatingResult.

        包年/包月产品的官网价。

        :param official_website_amount: The official_website_amount of this PeriodProductRatingResult.
        :type official_website_amount: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        self._official_website_amount = official_website_amount

    @property
    def discount_amount(self):
        r"""Gets the discount_amount of this PeriodProductRatingResult.

        可选折扣优惠额，如商务折扣、伙伴折扣、促销折扣和折扣券选用时的优惠额。

        :return: The discount_amount of this PeriodProductRatingResult.
        :rtype: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        r"""Sets the discount_amount of this PeriodProductRatingResult.

        可选折扣优惠额，如商务折扣、伙伴折扣、促销折扣和折扣券选用时的优惠额。

        :param discount_amount: The discount_amount of this PeriodProductRatingResult.
        :type discount_amount: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        self._discount_amount = discount_amount

    @property
    def measure_id(self):
        r"""Gets the measure_id of this PeriodProductRatingResult.

        价格度量单位标识。 1：元

        :return: The measure_id of this PeriodProductRatingResult.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        r"""Sets the measure_id of this PeriodProductRatingResult.

        价格度量单位标识。 1：元

        :param measure_id: The measure_id of this PeriodProductRatingResult.
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
        if not isinstance(other, PeriodProductRatingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
