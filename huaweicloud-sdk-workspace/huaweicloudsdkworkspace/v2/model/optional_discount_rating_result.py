# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OptionalDiscountRatingResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'discount_id': 'str',
        'amount': 'float',
        'official_website_amount': 'float',
        'original_amount': 'float',
        'official_website_discount_amount': 'float',
        'optional_discount_amount': 'float',
        'discount_amount': 'float',
        'per_amount': 'float',
        'per_discount_amount': 'float',
        'per_original_amount': 'float',
        'per_official_website_amount': 'float',
        'per_official_website_discount_amount': 'float',
        'per_optional_discount_amount': 'float',
        'per_period_type': 'int',
        'measure_id': 'int',
        'discount_type': 'int',
        'discount_name': 'str',
        'best_offer': 'int',
        'same_ratio_flag': 'int',
        'discount_ratio': 'float',
        'promotion_info': 'str',
        'product_rating_results': 'list[ProductResult]'
    }

    attribute_map = {
        'discount_id': 'discount_id',
        'amount': 'amount',
        'official_website_amount': 'official_website_amount',
        'original_amount': 'original_amount',
        'official_website_discount_amount': 'official_website_discount_amount',
        'optional_discount_amount': 'optional_discount_amount',
        'discount_amount': 'discount_amount',
        'per_amount': 'per_amount',
        'per_discount_amount': 'per_discount_amount',
        'per_original_amount': 'per_original_amount',
        'per_official_website_amount': 'per_official_website_amount',
        'per_official_website_discount_amount': 'per_official_website_discount_amount',
        'per_optional_discount_amount': 'per_optional_discount_amount',
        'per_period_type': 'per_period_type',
        'measure_id': 'measure_id',
        'discount_type': 'discount_type',
        'discount_name': 'discount_name',
        'best_offer': 'best_offer',
        'same_ratio_flag': 'same_ratio_flag',
        'discount_ratio': 'discount_ratio',
        'promotion_info': 'promotion_info',
        'product_rating_results': 'product_rating_results'
    }

    def __init__(self, discount_id=None, amount=None, official_website_amount=None, original_amount=None, official_website_discount_amount=None, optional_discount_amount=None, discount_amount=None, per_amount=None, per_discount_amount=None, per_original_amount=None, per_official_website_amount=None, per_official_website_discount_amount=None, per_optional_discount_amount=None, per_period_type=None, measure_id=None, discount_type=None, discount_name=None, best_offer=None, same_ratio_flag=None, discount_ratio=None, promotion_info=None, product_rating_results=None):
        r"""OptionalDiscountRatingResult

        The model defined in huaweicloud sdk

        :param discount_id: 折扣优惠Id。
        :type discount_id: str
        :param amount: 订单总额，即最终优惠后的订单金额(预留实例只包含预付部分)。
        :type amount: float
        :param official_website_amount: 官网价(预留实例只包含预付部分)。
        :type official_website_amount: float
        :param original_amount: 订单原总额，即优惠前订单总额(预留实例只包含预付部分)。
        :type original_amount: float
        :param official_website_discount_amount: 官网价优惠额(预留实例只包含预付部分)。
        :type official_website_discount_amount: float
        :param optional_discount_amount: 可选折扣优惠额(预留实例只包含预付部分)。
        :type optional_discount_amount: float
        :param discount_amount: 总优惠额(预留实例只包含预付部分)。
        :type discount_amount: float
        :param per_amount: 总分期金额(批量询价的商品分期周期类型一致，才会有总分期金额，分期周期类型不一致，该信息没有)。
        :type per_amount: float
        :param per_discount_amount: 总分期金额的优惠额(perDiscountAmount &#x3D; perOriginalAmount - perAmount)。
        :type per_discount_amount: float
        :param per_original_amount: 总分期金额原价。
        :type per_original_amount: float
        :param per_official_website_amount: 总分期金额的官网价(批量询价的商品分期周期类型一致，才会有总分期金额的官网价，分期周期类型不一致，该信息没有)。
        :type per_official_website_amount: float
        :param per_official_website_discount_amount: 总分期金额的官网价官网价优惠额，即： perOfficialWebsiteDiscountAmount &#x3D;perOriginalAmount-perOfficialWebsiteAmount (批量询价的商品分期周期类型一致，才会有总分期金额的官网价，分期周期类型不一致，该信息没有)。
        :type per_official_website_discount_amount: float
        :param per_optional_discount_amount: 总分期金额的可选折扣优惠额，如商务折扣、伙伴折扣、促销折扣和折扣券选用时的优惠额 perOptionalDiscountAmount&#x3D; perOfficialWebsiteAmount- perAmount (批量询价的商品分期周期类型一致，才会有总分期金额的官网价，分期周期类型不一致，该信息没有)。
        :type per_optional_discount_amount: float
        :param per_period_type: 分期周期类型 2:月 4:小时。
        :type per_period_type: int
        :param measure_id: 度量单位。
        :type measure_id: int
        :param discount_type: 折扣优惠类型。
        :type discount_type: int
        :param discount_name: 折扣名称。
        :type discount_name: str
        :param best_offer: 是否为最优折扣0：不是最优折扣；为缺省值。1：是最优折扣；最优折扣：在商务折扣、伙伴折扣和促销折扣中选择（优惠金额相等则按此顺序排优先级），折扣券不参与最优折扣的计算。
        :type best_offer: int
        :param same_ratio_flag: sameRatioFlag。
        :type same_ratio_flag: int
        :param discount_ratio: sameRatioFlag为1时有值，表示该折扣的折扣率。
        :type discount_ratio: float
        :param promotion_info: 折扣优惠基本信息；调用者在确定好折扣优惠后、下单时，使用此字段值，填入到订购/变更接口中的promotionInfo字段。
        :type promotion_info: str
        :param product_rating_results: 产品询价结果。
        :type product_rating_results: list[:class:`huaweicloudsdkworkspace.v2.ProductResult`]
        """
        
        

        self._discount_id = None
        self._amount = None
        self._official_website_amount = None
        self._original_amount = None
        self._official_website_discount_amount = None
        self._optional_discount_amount = None
        self._discount_amount = None
        self._per_amount = None
        self._per_discount_amount = None
        self._per_original_amount = None
        self._per_official_website_amount = None
        self._per_official_website_discount_amount = None
        self._per_optional_discount_amount = None
        self._per_period_type = None
        self._measure_id = None
        self._discount_type = None
        self._discount_name = None
        self._best_offer = None
        self._same_ratio_flag = None
        self._discount_ratio = None
        self._promotion_info = None
        self._product_rating_results = None
        self.discriminator = None

        if discount_id is not None:
            self.discount_id = discount_id
        if amount is not None:
            self.amount = amount
        if official_website_amount is not None:
            self.official_website_amount = official_website_amount
        if original_amount is not None:
            self.original_amount = original_amount
        if official_website_discount_amount is not None:
            self.official_website_discount_amount = official_website_discount_amount
        if optional_discount_amount is not None:
            self.optional_discount_amount = optional_discount_amount
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if per_amount is not None:
            self.per_amount = per_amount
        if per_discount_amount is not None:
            self.per_discount_amount = per_discount_amount
        if per_original_amount is not None:
            self.per_original_amount = per_original_amount
        if per_official_website_amount is not None:
            self.per_official_website_amount = per_official_website_amount
        if per_official_website_discount_amount is not None:
            self.per_official_website_discount_amount = per_official_website_discount_amount
        if per_optional_discount_amount is not None:
            self.per_optional_discount_amount = per_optional_discount_amount
        if per_period_type is not None:
            self.per_period_type = per_period_type
        if measure_id is not None:
            self.measure_id = measure_id
        if discount_type is not None:
            self.discount_type = discount_type
        if discount_name is not None:
            self.discount_name = discount_name
        if best_offer is not None:
            self.best_offer = best_offer
        if same_ratio_flag is not None:
            self.same_ratio_flag = same_ratio_flag
        if discount_ratio is not None:
            self.discount_ratio = discount_ratio
        if promotion_info is not None:
            self.promotion_info = promotion_info
        if product_rating_results is not None:
            self.product_rating_results = product_rating_results

    @property
    def discount_id(self):
        r"""Gets the discount_id of this OptionalDiscountRatingResult.

        折扣优惠Id。

        :return: The discount_id of this OptionalDiscountRatingResult.
        :rtype: str
        """
        return self._discount_id

    @discount_id.setter
    def discount_id(self, discount_id):
        r"""Sets the discount_id of this OptionalDiscountRatingResult.

        折扣优惠Id。

        :param discount_id: The discount_id of this OptionalDiscountRatingResult.
        :type discount_id: str
        """
        self._discount_id = discount_id

    @property
    def amount(self):
        r"""Gets the amount of this OptionalDiscountRatingResult.

        订单总额，即最终优惠后的订单金额(预留实例只包含预付部分)。

        :return: The amount of this OptionalDiscountRatingResult.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this OptionalDiscountRatingResult.

        订单总额，即最终优惠后的订单金额(预留实例只包含预付部分)。

        :param amount: The amount of this OptionalDiscountRatingResult.
        :type amount: float
        """
        self._amount = amount

    @property
    def official_website_amount(self):
        r"""Gets the official_website_amount of this OptionalDiscountRatingResult.

        官网价(预留实例只包含预付部分)。

        :return: The official_website_amount of this OptionalDiscountRatingResult.
        :rtype: float
        """
        return self._official_website_amount

    @official_website_amount.setter
    def official_website_amount(self, official_website_amount):
        r"""Sets the official_website_amount of this OptionalDiscountRatingResult.

        官网价(预留实例只包含预付部分)。

        :param official_website_amount: The official_website_amount of this OptionalDiscountRatingResult.
        :type official_website_amount: float
        """
        self._official_website_amount = official_website_amount

    @property
    def original_amount(self):
        r"""Gets the original_amount of this OptionalDiscountRatingResult.

        订单原总额，即优惠前订单总额(预留实例只包含预付部分)。

        :return: The original_amount of this OptionalDiscountRatingResult.
        :rtype: float
        """
        return self._original_amount

    @original_amount.setter
    def original_amount(self, original_amount):
        r"""Sets the original_amount of this OptionalDiscountRatingResult.

        订单原总额，即优惠前订单总额(预留实例只包含预付部分)。

        :param original_amount: The original_amount of this OptionalDiscountRatingResult.
        :type original_amount: float
        """
        self._original_amount = original_amount

    @property
    def official_website_discount_amount(self):
        r"""Gets the official_website_discount_amount of this OptionalDiscountRatingResult.

        官网价优惠额(预留实例只包含预付部分)。

        :return: The official_website_discount_amount of this OptionalDiscountRatingResult.
        :rtype: float
        """
        return self._official_website_discount_amount

    @official_website_discount_amount.setter
    def official_website_discount_amount(self, official_website_discount_amount):
        r"""Sets the official_website_discount_amount of this OptionalDiscountRatingResult.

        官网价优惠额(预留实例只包含预付部分)。

        :param official_website_discount_amount: The official_website_discount_amount of this OptionalDiscountRatingResult.
        :type official_website_discount_amount: float
        """
        self._official_website_discount_amount = official_website_discount_amount

    @property
    def optional_discount_amount(self):
        r"""Gets the optional_discount_amount of this OptionalDiscountRatingResult.

        可选折扣优惠额(预留实例只包含预付部分)。

        :return: The optional_discount_amount of this OptionalDiscountRatingResult.
        :rtype: float
        """
        return self._optional_discount_amount

    @optional_discount_amount.setter
    def optional_discount_amount(self, optional_discount_amount):
        r"""Sets the optional_discount_amount of this OptionalDiscountRatingResult.

        可选折扣优惠额(预留实例只包含预付部分)。

        :param optional_discount_amount: The optional_discount_amount of this OptionalDiscountRatingResult.
        :type optional_discount_amount: float
        """
        self._optional_discount_amount = optional_discount_amount

    @property
    def discount_amount(self):
        r"""Gets the discount_amount of this OptionalDiscountRatingResult.

        总优惠额(预留实例只包含预付部分)。

        :return: The discount_amount of this OptionalDiscountRatingResult.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        r"""Sets the discount_amount of this OptionalDiscountRatingResult.

        总优惠额(预留实例只包含预付部分)。

        :param discount_amount: The discount_amount of this OptionalDiscountRatingResult.
        :type discount_amount: float
        """
        self._discount_amount = discount_amount

    @property
    def per_amount(self):
        r"""Gets the per_amount of this OptionalDiscountRatingResult.

        总分期金额(批量询价的商品分期周期类型一致，才会有总分期金额，分期周期类型不一致，该信息没有)。

        :return: The per_amount of this OptionalDiscountRatingResult.
        :rtype: float
        """
        return self._per_amount

    @per_amount.setter
    def per_amount(self, per_amount):
        r"""Sets the per_amount of this OptionalDiscountRatingResult.

        总分期金额(批量询价的商品分期周期类型一致，才会有总分期金额，分期周期类型不一致，该信息没有)。

        :param per_amount: The per_amount of this OptionalDiscountRatingResult.
        :type per_amount: float
        """
        self._per_amount = per_amount

    @property
    def per_discount_amount(self):
        r"""Gets the per_discount_amount of this OptionalDiscountRatingResult.

        总分期金额的优惠额(perDiscountAmount = perOriginalAmount - perAmount)。

        :return: The per_discount_amount of this OptionalDiscountRatingResult.
        :rtype: float
        """
        return self._per_discount_amount

    @per_discount_amount.setter
    def per_discount_amount(self, per_discount_amount):
        r"""Sets the per_discount_amount of this OptionalDiscountRatingResult.

        总分期金额的优惠额(perDiscountAmount = perOriginalAmount - perAmount)。

        :param per_discount_amount: The per_discount_amount of this OptionalDiscountRatingResult.
        :type per_discount_amount: float
        """
        self._per_discount_amount = per_discount_amount

    @property
    def per_original_amount(self):
        r"""Gets the per_original_amount of this OptionalDiscountRatingResult.

        总分期金额原价。

        :return: The per_original_amount of this OptionalDiscountRatingResult.
        :rtype: float
        """
        return self._per_original_amount

    @per_original_amount.setter
    def per_original_amount(self, per_original_amount):
        r"""Sets the per_original_amount of this OptionalDiscountRatingResult.

        总分期金额原价。

        :param per_original_amount: The per_original_amount of this OptionalDiscountRatingResult.
        :type per_original_amount: float
        """
        self._per_original_amount = per_original_amount

    @property
    def per_official_website_amount(self):
        r"""Gets the per_official_website_amount of this OptionalDiscountRatingResult.

        总分期金额的官网价(批量询价的商品分期周期类型一致，才会有总分期金额的官网价，分期周期类型不一致，该信息没有)。

        :return: The per_official_website_amount of this OptionalDiscountRatingResult.
        :rtype: float
        """
        return self._per_official_website_amount

    @per_official_website_amount.setter
    def per_official_website_amount(self, per_official_website_amount):
        r"""Sets the per_official_website_amount of this OptionalDiscountRatingResult.

        总分期金额的官网价(批量询价的商品分期周期类型一致，才会有总分期金额的官网价，分期周期类型不一致，该信息没有)。

        :param per_official_website_amount: The per_official_website_amount of this OptionalDiscountRatingResult.
        :type per_official_website_amount: float
        """
        self._per_official_website_amount = per_official_website_amount

    @property
    def per_official_website_discount_amount(self):
        r"""Gets the per_official_website_discount_amount of this OptionalDiscountRatingResult.

        总分期金额的官网价官网价优惠额，即： perOfficialWebsiteDiscountAmount =perOriginalAmount-perOfficialWebsiteAmount (批量询价的商品分期周期类型一致，才会有总分期金额的官网价，分期周期类型不一致，该信息没有)。

        :return: The per_official_website_discount_amount of this OptionalDiscountRatingResult.
        :rtype: float
        """
        return self._per_official_website_discount_amount

    @per_official_website_discount_amount.setter
    def per_official_website_discount_amount(self, per_official_website_discount_amount):
        r"""Sets the per_official_website_discount_amount of this OptionalDiscountRatingResult.

        总分期金额的官网价官网价优惠额，即： perOfficialWebsiteDiscountAmount =perOriginalAmount-perOfficialWebsiteAmount (批量询价的商品分期周期类型一致，才会有总分期金额的官网价，分期周期类型不一致，该信息没有)。

        :param per_official_website_discount_amount: The per_official_website_discount_amount of this OptionalDiscountRatingResult.
        :type per_official_website_discount_amount: float
        """
        self._per_official_website_discount_amount = per_official_website_discount_amount

    @property
    def per_optional_discount_amount(self):
        r"""Gets the per_optional_discount_amount of this OptionalDiscountRatingResult.

        总分期金额的可选折扣优惠额，如商务折扣、伙伴折扣、促销折扣和折扣券选用时的优惠额 perOptionalDiscountAmount= perOfficialWebsiteAmount- perAmount (批量询价的商品分期周期类型一致，才会有总分期金额的官网价，分期周期类型不一致，该信息没有)。

        :return: The per_optional_discount_amount of this OptionalDiscountRatingResult.
        :rtype: float
        """
        return self._per_optional_discount_amount

    @per_optional_discount_amount.setter
    def per_optional_discount_amount(self, per_optional_discount_amount):
        r"""Sets the per_optional_discount_amount of this OptionalDiscountRatingResult.

        总分期金额的可选折扣优惠额，如商务折扣、伙伴折扣、促销折扣和折扣券选用时的优惠额 perOptionalDiscountAmount= perOfficialWebsiteAmount- perAmount (批量询价的商品分期周期类型一致，才会有总分期金额的官网价，分期周期类型不一致，该信息没有)。

        :param per_optional_discount_amount: The per_optional_discount_amount of this OptionalDiscountRatingResult.
        :type per_optional_discount_amount: float
        """
        self._per_optional_discount_amount = per_optional_discount_amount

    @property
    def per_period_type(self):
        r"""Gets the per_period_type of this OptionalDiscountRatingResult.

        分期周期类型 2:月 4:小时。

        :return: The per_period_type of this OptionalDiscountRatingResult.
        :rtype: int
        """
        return self._per_period_type

    @per_period_type.setter
    def per_period_type(self, per_period_type):
        r"""Sets the per_period_type of this OptionalDiscountRatingResult.

        分期周期类型 2:月 4:小时。

        :param per_period_type: The per_period_type of this OptionalDiscountRatingResult.
        :type per_period_type: int
        """
        self._per_period_type = per_period_type

    @property
    def measure_id(self):
        r"""Gets the measure_id of this OptionalDiscountRatingResult.

        度量单位。

        :return: The measure_id of this OptionalDiscountRatingResult.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        r"""Sets the measure_id of this OptionalDiscountRatingResult.

        度量单位。

        :param measure_id: The measure_id of this OptionalDiscountRatingResult.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def discount_type(self):
        r"""Gets the discount_type of this OptionalDiscountRatingResult.

        折扣优惠类型。

        :return: The discount_type of this OptionalDiscountRatingResult.
        :rtype: int
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        r"""Sets the discount_type of this OptionalDiscountRatingResult.

        折扣优惠类型。

        :param discount_type: The discount_type of this OptionalDiscountRatingResult.
        :type discount_type: int
        """
        self._discount_type = discount_type

    @property
    def discount_name(self):
        r"""Gets the discount_name of this OptionalDiscountRatingResult.

        折扣名称。

        :return: The discount_name of this OptionalDiscountRatingResult.
        :rtype: str
        """
        return self._discount_name

    @discount_name.setter
    def discount_name(self, discount_name):
        r"""Sets the discount_name of this OptionalDiscountRatingResult.

        折扣名称。

        :param discount_name: The discount_name of this OptionalDiscountRatingResult.
        :type discount_name: str
        """
        self._discount_name = discount_name

    @property
    def best_offer(self):
        r"""Gets the best_offer of this OptionalDiscountRatingResult.

        是否为最优折扣0：不是最优折扣；为缺省值。1：是最优折扣；最优折扣：在商务折扣、伙伴折扣和促销折扣中选择（优惠金额相等则按此顺序排优先级），折扣券不参与最优折扣的计算。

        :return: The best_offer of this OptionalDiscountRatingResult.
        :rtype: int
        """
        return self._best_offer

    @best_offer.setter
    def best_offer(self, best_offer):
        r"""Sets the best_offer of this OptionalDiscountRatingResult.

        是否为最优折扣0：不是最优折扣；为缺省值。1：是最优折扣；最优折扣：在商务折扣、伙伴折扣和促销折扣中选择（优惠金额相等则按此顺序排优先级），折扣券不参与最优折扣的计算。

        :param best_offer: The best_offer of this OptionalDiscountRatingResult.
        :type best_offer: int
        """
        self._best_offer = best_offer

    @property
    def same_ratio_flag(self):
        r"""Gets the same_ratio_flag of this OptionalDiscountRatingResult.

        sameRatioFlag。

        :return: The same_ratio_flag of this OptionalDiscountRatingResult.
        :rtype: int
        """
        return self._same_ratio_flag

    @same_ratio_flag.setter
    def same_ratio_flag(self, same_ratio_flag):
        r"""Sets the same_ratio_flag of this OptionalDiscountRatingResult.

        sameRatioFlag。

        :param same_ratio_flag: The same_ratio_flag of this OptionalDiscountRatingResult.
        :type same_ratio_flag: int
        """
        self._same_ratio_flag = same_ratio_flag

    @property
    def discount_ratio(self):
        r"""Gets the discount_ratio of this OptionalDiscountRatingResult.

        sameRatioFlag为1时有值，表示该折扣的折扣率。

        :return: The discount_ratio of this OptionalDiscountRatingResult.
        :rtype: float
        """
        return self._discount_ratio

    @discount_ratio.setter
    def discount_ratio(self, discount_ratio):
        r"""Sets the discount_ratio of this OptionalDiscountRatingResult.

        sameRatioFlag为1时有值，表示该折扣的折扣率。

        :param discount_ratio: The discount_ratio of this OptionalDiscountRatingResult.
        :type discount_ratio: float
        """
        self._discount_ratio = discount_ratio

    @property
    def promotion_info(self):
        r"""Gets the promotion_info of this OptionalDiscountRatingResult.

        折扣优惠基本信息；调用者在确定好折扣优惠后、下单时，使用此字段值，填入到订购/变更接口中的promotionInfo字段。

        :return: The promotion_info of this OptionalDiscountRatingResult.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        r"""Sets the promotion_info of this OptionalDiscountRatingResult.

        折扣优惠基本信息；调用者在确定好折扣优惠后、下单时，使用此字段值，填入到订购/变更接口中的promotionInfo字段。

        :param promotion_info: The promotion_info of this OptionalDiscountRatingResult.
        :type promotion_info: str
        """
        self._promotion_info = promotion_info

    @property
    def product_rating_results(self):
        r"""Gets the product_rating_results of this OptionalDiscountRatingResult.

        产品询价结果。

        :return: The product_rating_results of this OptionalDiscountRatingResult.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ProductResult`]
        """
        return self._product_rating_results

    @product_rating_results.setter
    def product_rating_results(self, product_rating_results):
        r"""Sets the product_rating_results of this OptionalDiscountRatingResult.

        产品询价结果。

        :param product_rating_results: The product_rating_results of this OptionalDiscountRatingResult.
        :type product_rating_results: list[:class:`huaweicloudsdkworkspace.v2.ProductResult`]
        """
        self._product_rating_results = product_rating_results

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
        if not isinstance(other, OptionalDiscountRatingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
