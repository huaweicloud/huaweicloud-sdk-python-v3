# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductQuotingItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item_id': 'str',
        'product_id': 'str',
        'product_spec_name': 'str',
        'cloud_service_type': 'str',
        'cloud_service_type_name': 'str',
        'site_code': 'str',
        'related_regions': 'list[RegionInfo]',
        'charge_event_code': 'str',
        'charging_mode': 'str',
        'preferential_category': 'int',
        'preferential_type': 'int',
        'sales_price': 'decimal.Decimal',
        'discount_ratio': 'decimal.Decimal',
        'pricing_basis': 'str',
        'effective_time': 'str',
        'expire_time': 'str',
        'product_quoting_item_steps': 'list[ProductQuotingItemStep]'
    }

    attribute_map = {
        'item_id': 'item_id',
        'product_id': 'product_id',
        'product_spec_name': 'product_spec_name',
        'cloud_service_type': 'cloud_service_type',
        'cloud_service_type_name': 'cloud_service_type_name',
        'site_code': 'site_code',
        'related_regions': 'related_regions',
        'charge_event_code': 'charge_event_code',
        'charging_mode': 'charging_mode',
        'preferential_category': 'preferential_category',
        'preferential_type': 'preferential_type',
        'sales_price': 'sales_price',
        'discount_ratio': 'discount_ratio',
        'pricing_basis': 'pricing_basis',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time',
        'product_quoting_item_steps': 'product_quoting_item_steps'
    }

    def __init__(self, item_id=None, product_id=None, product_spec_name=None, cloud_service_type=None, cloud_service_type_name=None, site_code=None, related_regions=None, charge_event_code=None, charging_mode=None, preferential_category=None, preferential_type=None, sales_price=None, discount_ratio=None, pricing_basis=None, effective_time=None, expire_time=None, product_quoting_item_steps=None):
        r"""ProductQuotingItem

        The model defined in huaweicloud sdk

        :param item_id: 报价项ID
        :type item_id: str
        :param product_id: 产品ID
        :type product_id: str
        :param product_spec_name: 产品规格名称
        :type product_spec_name: str
        :param cloud_service_type: 云服务编码
        :type cloud_service_type: str
        :param cloud_service_type_name: 云服务名称
        :type cloud_service_type_name: str
        :param site_code: 运营站点编码
        :type site_code: str
        :param related_regions: 产品关联的云服务区信息列表
        :type related_regions: list[:class:`huaweicloudsdkbss.v2.RegionInfo`]
        :param charge_event_code: 计费事件编码
        :type charge_event_code: str
        :param charging_mode: 计费模式，ONDEMAND：按需、ONETIME：一次性、DAILY：包天、MONTHLY：包月、1_YEARLY：包1年、2_YEARLY：包2年、3_YEARLY：包3年、4_YEARLY：包4年、5_YEARLY：包5年、1_YEARLY_RI：包1年预留实例、3_YEARLY_RI：包3年预留实例
        :type charging_mode: str
        :param preferential_category: 优惠分类：0：普通优惠，1：产品阶梯，2：分时优惠
        :type preferential_category: int
        :param preferential_type: 优惠方式：0：产品折扣，1：固定单价
        :type preferential_type: int
        :param sales_price: 固定单价（preferential_type&#x3D;1固定单价时有值）
        :type sales_price: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param discount_ratio: 折扣率（preferential_type&#x3D;0产品折扣时有值）
        :type discount_ratio: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param pricing_basis: 计费单位
        :type pricing_basis: str
        :param effective_time: 报价项生效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ
        :type effective_time: str
        :param expire_time: 报价项失效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ
        :type expire_time: str
        :param product_quoting_item_steps: 产品报价项阶梯列表，产品阶梯或分时优惠时有值返回，否则返回空列表
        :type product_quoting_item_steps: list[:class:`huaweicloudsdkbss.v2.ProductQuotingItemStep`]
        """
        
        

        self._item_id = None
        self._product_id = None
        self._product_spec_name = None
        self._cloud_service_type = None
        self._cloud_service_type_name = None
        self._site_code = None
        self._related_regions = None
        self._charge_event_code = None
        self._charging_mode = None
        self._preferential_category = None
        self._preferential_type = None
        self._sales_price = None
        self._discount_ratio = None
        self._pricing_basis = None
        self._effective_time = None
        self._expire_time = None
        self._product_quoting_item_steps = None
        self.discriminator = None

        if item_id is not None:
            self.item_id = item_id
        if product_id is not None:
            self.product_id = product_id
        if product_spec_name is not None:
            self.product_spec_name = product_spec_name
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if cloud_service_type_name is not None:
            self.cloud_service_type_name = cloud_service_type_name
        if site_code is not None:
            self.site_code = site_code
        if related_regions is not None:
            self.related_regions = related_regions
        if charge_event_code is not None:
            self.charge_event_code = charge_event_code
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if preferential_category is not None:
            self.preferential_category = preferential_category
        if preferential_type is not None:
            self.preferential_type = preferential_type
        if sales_price is not None:
            self.sales_price = sales_price
        if discount_ratio is not None:
            self.discount_ratio = discount_ratio
        if pricing_basis is not None:
            self.pricing_basis = pricing_basis
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time
        if product_quoting_item_steps is not None:
            self.product_quoting_item_steps = product_quoting_item_steps

    @property
    def item_id(self):
        r"""Gets the item_id of this ProductQuotingItem.

        报价项ID

        :return: The item_id of this ProductQuotingItem.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        r"""Sets the item_id of this ProductQuotingItem.

        报价项ID

        :param item_id: The item_id of this ProductQuotingItem.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def product_id(self):
        r"""Gets the product_id of this ProductQuotingItem.

        产品ID

        :return: The product_id of this ProductQuotingItem.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ProductQuotingItem.

        产品ID

        :param product_id: The product_id of this ProductQuotingItem.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def product_spec_name(self):
        r"""Gets the product_spec_name of this ProductQuotingItem.

        产品规格名称

        :return: The product_spec_name of this ProductQuotingItem.
        :rtype: str
        """
        return self._product_spec_name

    @product_spec_name.setter
    def product_spec_name(self, product_spec_name):
        r"""Sets the product_spec_name of this ProductQuotingItem.

        产品规格名称

        :param product_spec_name: The product_spec_name of this ProductQuotingItem.
        :type product_spec_name: str
        """
        self._product_spec_name = product_spec_name

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this ProductQuotingItem.

        云服务编码

        :return: The cloud_service_type of this ProductQuotingItem.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this ProductQuotingItem.

        云服务编码

        :param cloud_service_type: The cloud_service_type of this ProductQuotingItem.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def cloud_service_type_name(self):
        r"""Gets the cloud_service_type_name of this ProductQuotingItem.

        云服务名称

        :return: The cloud_service_type_name of this ProductQuotingItem.
        :rtype: str
        """
        return self._cloud_service_type_name

    @cloud_service_type_name.setter
    def cloud_service_type_name(self, cloud_service_type_name):
        r"""Sets the cloud_service_type_name of this ProductQuotingItem.

        云服务名称

        :param cloud_service_type_name: The cloud_service_type_name of this ProductQuotingItem.
        :type cloud_service_type_name: str
        """
        self._cloud_service_type_name = cloud_service_type_name

    @property
    def site_code(self):
        r"""Gets the site_code of this ProductQuotingItem.

        运营站点编码

        :return: The site_code of this ProductQuotingItem.
        :rtype: str
        """
        return self._site_code

    @site_code.setter
    def site_code(self, site_code):
        r"""Sets the site_code of this ProductQuotingItem.

        运营站点编码

        :param site_code: The site_code of this ProductQuotingItem.
        :type site_code: str
        """
        self._site_code = site_code

    @property
    def related_regions(self):
        r"""Gets the related_regions of this ProductQuotingItem.

        产品关联的云服务区信息列表

        :return: The related_regions of this ProductQuotingItem.
        :rtype: list[:class:`huaweicloudsdkbss.v2.RegionInfo`]
        """
        return self._related_regions

    @related_regions.setter
    def related_regions(self, related_regions):
        r"""Sets the related_regions of this ProductQuotingItem.

        产品关联的云服务区信息列表

        :param related_regions: The related_regions of this ProductQuotingItem.
        :type related_regions: list[:class:`huaweicloudsdkbss.v2.RegionInfo`]
        """
        self._related_regions = related_regions

    @property
    def charge_event_code(self):
        r"""Gets the charge_event_code of this ProductQuotingItem.

        计费事件编码

        :return: The charge_event_code of this ProductQuotingItem.
        :rtype: str
        """
        return self._charge_event_code

    @charge_event_code.setter
    def charge_event_code(self, charge_event_code):
        r"""Sets the charge_event_code of this ProductQuotingItem.

        计费事件编码

        :param charge_event_code: The charge_event_code of this ProductQuotingItem.
        :type charge_event_code: str
        """
        self._charge_event_code = charge_event_code

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ProductQuotingItem.

        计费模式，ONDEMAND：按需、ONETIME：一次性、DAILY：包天、MONTHLY：包月、1_YEARLY：包1年、2_YEARLY：包2年、3_YEARLY：包3年、4_YEARLY：包4年、5_YEARLY：包5年、1_YEARLY_RI：包1年预留实例、3_YEARLY_RI：包3年预留实例

        :return: The charging_mode of this ProductQuotingItem.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ProductQuotingItem.

        计费模式，ONDEMAND：按需、ONETIME：一次性、DAILY：包天、MONTHLY：包月、1_YEARLY：包1年、2_YEARLY：包2年、3_YEARLY：包3年、4_YEARLY：包4年、5_YEARLY：包5年、1_YEARLY_RI：包1年预留实例、3_YEARLY_RI：包3年预留实例

        :param charging_mode: The charging_mode of this ProductQuotingItem.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def preferential_category(self):
        r"""Gets the preferential_category of this ProductQuotingItem.

        优惠分类：0：普通优惠，1：产品阶梯，2：分时优惠

        :return: The preferential_category of this ProductQuotingItem.
        :rtype: int
        """
        return self._preferential_category

    @preferential_category.setter
    def preferential_category(self, preferential_category):
        r"""Sets the preferential_category of this ProductQuotingItem.

        优惠分类：0：普通优惠，1：产品阶梯，2：分时优惠

        :param preferential_category: The preferential_category of this ProductQuotingItem.
        :type preferential_category: int
        """
        self._preferential_category = preferential_category

    @property
    def preferential_type(self):
        r"""Gets the preferential_type of this ProductQuotingItem.

        优惠方式：0：产品折扣，1：固定单价

        :return: The preferential_type of this ProductQuotingItem.
        :rtype: int
        """
        return self._preferential_type

    @preferential_type.setter
    def preferential_type(self, preferential_type):
        r"""Sets the preferential_type of this ProductQuotingItem.

        优惠方式：0：产品折扣，1：固定单价

        :param preferential_type: The preferential_type of this ProductQuotingItem.
        :type preferential_type: int
        """
        self._preferential_type = preferential_type

    @property
    def sales_price(self):
        r"""Gets the sales_price of this ProductQuotingItem.

        固定单价（preferential_type=1固定单价时有值）

        :return: The sales_price of this ProductQuotingItem.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._sales_price

    @sales_price.setter
    def sales_price(self, sales_price):
        r"""Sets the sales_price of this ProductQuotingItem.

        固定单价（preferential_type=1固定单价时有值）

        :param sales_price: The sales_price of this ProductQuotingItem.
        :type sales_price: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._sales_price = sales_price

    @property
    def discount_ratio(self):
        r"""Gets the discount_ratio of this ProductQuotingItem.

        折扣率（preferential_type=0产品折扣时有值）

        :return: The discount_ratio of this ProductQuotingItem.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._discount_ratio

    @discount_ratio.setter
    def discount_ratio(self, discount_ratio):
        r"""Sets the discount_ratio of this ProductQuotingItem.

        折扣率（preferential_type=0产品折扣时有值）

        :param discount_ratio: The discount_ratio of this ProductQuotingItem.
        :type discount_ratio: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._discount_ratio = discount_ratio

    @property
    def pricing_basis(self):
        r"""Gets the pricing_basis of this ProductQuotingItem.

        计费单位

        :return: The pricing_basis of this ProductQuotingItem.
        :rtype: str
        """
        return self._pricing_basis

    @pricing_basis.setter
    def pricing_basis(self, pricing_basis):
        r"""Sets the pricing_basis of this ProductQuotingItem.

        计费单位

        :param pricing_basis: The pricing_basis of this ProductQuotingItem.
        :type pricing_basis: str
        """
        self._pricing_basis = pricing_basis

    @property
    def effective_time(self):
        r"""Gets the effective_time of this ProductQuotingItem.

        报价项生效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :return: The effective_time of this ProductQuotingItem.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        r"""Sets the effective_time of this ProductQuotingItem.

        报价项生效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :param effective_time: The effective_time of this ProductQuotingItem.
        :type effective_time: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ProductQuotingItem.

        报价项失效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :return: The expire_time of this ProductQuotingItem.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ProductQuotingItem.

        报价项失效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :param expire_time: The expire_time of this ProductQuotingItem.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def product_quoting_item_steps(self):
        r"""Gets the product_quoting_item_steps of this ProductQuotingItem.

        产品报价项阶梯列表，产品阶梯或分时优惠时有值返回，否则返回空列表

        :return: The product_quoting_item_steps of this ProductQuotingItem.
        :rtype: list[:class:`huaweicloudsdkbss.v2.ProductQuotingItemStep`]
        """
        return self._product_quoting_item_steps

    @product_quoting_item_steps.setter
    def product_quoting_item_steps(self, product_quoting_item_steps):
        r"""Sets the product_quoting_item_steps of this ProductQuotingItem.

        产品报价项阶梯列表，产品阶梯或分时优惠时有值返回，否则返回空列表

        :param product_quoting_item_steps: The product_quoting_item_steps of this ProductQuotingItem.
        :type product_quoting_item_steps: list[:class:`huaweicloudsdkbss.v2.ProductQuotingItemStep`]
        """
        self._product_quoting_item_steps = product_quoting_item_steps

    def to_dict(self):
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
        if not isinstance(other, ProductQuotingItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
