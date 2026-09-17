# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBusinessDiscountInfoResponse(SdkResponse):

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
        'commerce_id': 'str',
        'commerce_code': 'str',
        'effective_time': 'str',
        'expire_time': 'str',
        'product_quoting_items': 'list[ProductQuotingItem]',
        'category_quoting_items': 'list[CategoryQuotingItem]',
        'category_quoting_item_steps': 'list[CategoryQuotingItemStep]',
        'accumulation_cycle_type': 'str',
        'sites': 'list[SiteInfo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'commerce_id': 'commerce_id',
        'commerce_code': 'commerce_code',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time',
        'product_quoting_items': 'product_quoting_items',
        'category_quoting_items': 'category_quoting_items',
        'category_quoting_item_steps': 'category_quoting_item_steps',
        'accumulation_cycle_type': 'accumulation_cycle_type',
        'sites': 'sites'
    }

    def __init__(self, total_count=None, commerce_id=None, commerce_code=None, effective_time=None, expire_time=None, product_quoting_items=None, category_quoting_items=None, category_quoting_item_steps=None, accumulation_cycle_type=None, sites=None):
        r"""ListBusinessDiscountInfoResponse

        The model defined in huaweicloud sdk

        :param total_count: 总条数
        :type total_count: int
        :param commerce_id: 商务ID
        :type commerce_id: str
        :param commerce_code: 商务编号
        :type commerce_code: str
        :param effective_time: 商务生效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ
        :type effective_time: str
        :param expire_time: 商务失效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ
        :type expire_time: str
        :param product_quoting_items: 产品报价项列表（quoting_item_type&#x3D;PRODUCT_ITEM时有值返回，否则返回空列表）
        :type product_quoting_items: list[:class:`huaweicloudsdkbss.v2.ProductQuotingItem`]
        :param category_quoting_items: 分类报价项列表（quoting_item_type&#x3D;CATEGORY_ITEM时有值返回，否则返回空列表）
        :type category_quoting_items: list[:class:`huaweicloudsdkbss.v2.CategoryQuotingItem`]
        :param category_quoting_item_steps: 分类报价项阶梯列表（quoting_item_type&#x3D;CATEGORY_ITEM时有值返回，否则返回空列表）
        :type category_quoting_item_steps: list[:class:`huaweicloudsdkbss.v2.CategoryQuotingItemStep`]
        :param accumulation_cycle_type: 阶梯累计周期类型，category_quoting_item_steps有值返回时返回
        :type accumulation_cycle_type: str
        :param sites: 运营站点列表
        :type sites: list[:class:`huaweicloudsdkbss.v2.SiteInfo`]
        """
        
        super().__init__()

        self._total_count = None
        self._commerce_id = None
        self._commerce_code = None
        self._effective_time = None
        self._expire_time = None
        self._product_quoting_items = None
        self._category_quoting_items = None
        self._category_quoting_item_steps = None
        self._accumulation_cycle_type = None
        self._sites = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if commerce_id is not None:
            self.commerce_id = commerce_id
        if commerce_code is not None:
            self.commerce_code = commerce_code
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time
        if product_quoting_items is not None:
            self.product_quoting_items = product_quoting_items
        if category_quoting_items is not None:
            self.category_quoting_items = category_quoting_items
        if category_quoting_item_steps is not None:
            self.category_quoting_item_steps = category_quoting_item_steps
        if accumulation_cycle_type is not None:
            self.accumulation_cycle_type = accumulation_cycle_type
        if sites is not None:
            self.sites = sites

    @property
    def total_count(self):
        r"""Gets the total_count of this ListBusinessDiscountInfoResponse.

        总条数

        :return: The total_count of this ListBusinessDiscountInfoResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListBusinessDiscountInfoResponse.

        总条数

        :param total_count: The total_count of this ListBusinessDiscountInfoResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def commerce_id(self):
        r"""Gets the commerce_id of this ListBusinessDiscountInfoResponse.

        商务ID

        :return: The commerce_id of this ListBusinessDiscountInfoResponse.
        :rtype: str
        """
        return self._commerce_id

    @commerce_id.setter
    def commerce_id(self, commerce_id):
        r"""Sets the commerce_id of this ListBusinessDiscountInfoResponse.

        商务ID

        :param commerce_id: The commerce_id of this ListBusinessDiscountInfoResponse.
        :type commerce_id: str
        """
        self._commerce_id = commerce_id

    @property
    def commerce_code(self):
        r"""Gets the commerce_code of this ListBusinessDiscountInfoResponse.

        商务编号

        :return: The commerce_code of this ListBusinessDiscountInfoResponse.
        :rtype: str
        """
        return self._commerce_code

    @commerce_code.setter
    def commerce_code(self, commerce_code):
        r"""Sets the commerce_code of this ListBusinessDiscountInfoResponse.

        商务编号

        :param commerce_code: The commerce_code of this ListBusinessDiscountInfoResponse.
        :type commerce_code: str
        """
        self._commerce_code = commerce_code

    @property
    def effective_time(self):
        r"""Gets the effective_time of this ListBusinessDiscountInfoResponse.

        商务生效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :return: The effective_time of this ListBusinessDiscountInfoResponse.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        r"""Sets the effective_time of this ListBusinessDiscountInfoResponse.

        商务生效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :param effective_time: The effective_time of this ListBusinessDiscountInfoResponse.
        :type effective_time: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ListBusinessDiscountInfoResponse.

        商务失效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :return: The expire_time of this ListBusinessDiscountInfoResponse.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ListBusinessDiscountInfoResponse.

        商务失效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :param expire_time: The expire_time of this ListBusinessDiscountInfoResponse.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def product_quoting_items(self):
        r"""Gets the product_quoting_items of this ListBusinessDiscountInfoResponse.

        产品报价项列表（quoting_item_type=PRODUCT_ITEM时有值返回，否则返回空列表）

        :return: The product_quoting_items of this ListBusinessDiscountInfoResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.ProductQuotingItem`]
        """
        return self._product_quoting_items

    @product_quoting_items.setter
    def product_quoting_items(self, product_quoting_items):
        r"""Sets the product_quoting_items of this ListBusinessDiscountInfoResponse.

        产品报价项列表（quoting_item_type=PRODUCT_ITEM时有值返回，否则返回空列表）

        :param product_quoting_items: The product_quoting_items of this ListBusinessDiscountInfoResponse.
        :type product_quoting_items: list[:class:`huaweicloudsdkbss.v2.ProductQuotingItem`]
        """
        self._product_quoting_items = product_quoting_items

    @property
    def category_quoting_items(self):
        r"""Gets the category_quoting_items of this ListBusinessDiscountInfoResponse.

        分类报价项列表（quoting_item_type=CATEGORY_ITEM时有值返回，否则返回空列表）

        :return: The category_quoting_items of this ListBusinessDiscountInfoResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.CategoryQuotingItem`]
        """
        return self._category_quoting_items

    @category_quoting_items.setter
    def category_quoting_items(self, category_quoting_items):
        r"""Sets the category_quoting_items of this ListBusinessDiscountInfoResponse.

        分类报价项列表（quoting_item_type=CATEGORY_ITEM时有值返回，否则返回空列表）

        :param category_quoting_items: The category_quoting_items of this ListBusinessDiscountInfoResponse.
        :type category_quoting_items: list[:class:`huaweicloudsdkbss.v2.CategoryQuotingItem`]
        """
        self._category_quoting_items = category_quoting_items

    @property
    def category_quoting_item_steps(self):
        r"""Gets the category_quoting_item_steps of this ListBusinessDiscountInfoResponse.

        分类报价项阶梯列表（quoting_item_type=CATEGORY_ITEM时有值返回，否则返回空列表）

        :return: The category_quoting_item_steps of this ListBusinessDiscountInfoResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.CategoryQuotingItemStep`]
        """
        return self._category_quoting_item_steps

    @category_quoting_item_steps.setter
    def category_quoting_item_steps(self, category_quoting_item_steps):
        r"""Sets the category_quoting_item_steps of this ListBusinessDiscountInfoResponse.

        分类报价项阶梯列表（quoting_item_type=CATEGORY_ITEM时有值返回，否则返回空列表）

        :param category_quoting_item_steps: The category_quoting_item_steps of this ListBusinessDiscountInfoResponse.
        :type category_quoting_item_steps: list[:class:`huaweicloudsdkbss.v2.CategoryQuotingItemStep`]
        """
        self._category_quoting_item_steps = category_quoting_item_steps

    @property
    def accumulation_cycle_type(self):
        r"""Gets the accumulation_cycle_type of this ListBusinessDiscountInfoResponse.

        阶梯累计周期类型，category_quoting_item_steps有值返回时返回

        :return: The accumulation_cycle_type of this ListBusinessDiscountInfoResponse.
        :rtype: str
        """
        return self._accumulation_cycle_type

    @accumulation_cycle_type.setter
    def accumulation_cycle_type(self, accumulation_cycle_type):
        r"""Sets the accumulation_cycle_type of this ListBusinessDiscountInfoResponse.

        阶梯累计周期类型，category_quoting_item_steps有值返回时返回

        :param accumulation_cycle_type: The accumulation_cycle_type of this ListBusinessDiscountInfoResponse.
        :type accumulation_cycle_type: str
        """
        self._accumulation_cycle_type = accumulation_cycle_type

    @property
    def sites(self):
        r"""Gets the sites of this ListBusinessDiscountInfoResponse.

        运营站点列表

        :return: The sites of this ListBusinessDiscountInfoResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.SiteInfo`]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        r"""Sets the sites of this ListBusinessDiscountInfoResponse.

        运营站点列表

        :param sites: The sites of this ListBusinessDiscountInfoResponse.
        :type sites: list[:class:`huaweicloudsdkbss.v2.SiteInfo`]
        """
        self._sites = sites

    def to_dict(self):
        import warnings
        warnings.warn("ListBusinessDiscountInfoResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListBusinessDiscountInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
