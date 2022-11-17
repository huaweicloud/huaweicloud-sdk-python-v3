# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderLineItemEntityV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_line_item_id': 'str',
        'service_type_code': 'str',
        'service_type_name': 'str',
        'product_id': 'str',
        'product_spec_desc': 'str',
        'period_type': 'int',
        'period_num': 'int',
        'effective_time': 'str',
        'expire_time': 'str',
        'subscription_num': 'int',
        'amount_after_discount': 'float',
        'official_amount': 'float',
        'amount_info': 'AmountInfomationV2',
        'currency': 'str',
        'category_code': 'str',
        'product_owner_service': 'str',
        'commercial_resource': 'str'
    }

    attribute_map = {
        'order_line_item_id': 'order_line_item_id',
        'service_type_code': 'service_type_code',
        'service_type_name': 'service_type_name',
        'product_id': 'product_id',
        'product_spec_desc': 'product_spec_desc',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time',
        'subscription_num': 'subscription_num',
        'amount_after_discount': 'amount_after_discount',
        'official_amount': 'official_amount',
        'amount_info': 'amount_info',
        'currency': 'currency',
        'category_code': 'category_code',
        'product_owner_service': 'product_owner_service',
        'commercial_resource': 'commercial_resource'
    }

    def __init__(self, order_line_item_id=None, service_type_code=None, service_type_name=None, product_id=None, product_spec_desc=None, period_type=None, period_num=None, effective_time=None, expire_time=None, subscription_num=None, amount_after_discount=None, official_amount=None, amount_info=None, currency=None, category_code=None, product_owner_service=None, commercial_resource=None):
        """OrderLineItemEntityV2

        The model defined in huaweicloud sdk

        :param order_line_item_id: 订单项ID。
        :type order_line_item_id: str
        :param service_type_code: 云服务类型编码。例如OBS的云服务类型编码为“hws.service.type.obs”。
        :type service_type_code: str
        :param service_type_name: 云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。
        :type service_type_name: str
        :param product_id: 产品ID。
        :type product_id: str
        :param product_spec_desc: 产品规格描述。
        :type product_spec_desc: str
        :param period_type: 周期类型。 0：天1：周2：月3：年4：小时5：一次性6：按需（预留）7：按用量报表使用（预留）
        :type period_type: int
        :param period_num: 周期数量。  说明： 当订单为退订资源的订单时，参数取值为null。
        :type period_num: int
        :param effective_time: 生效时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。
        :type effective_time: str
        :param expire_time: 失效时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。
        :type expire_time: str
        :param subscription_num: 订购数量。
        :type subscription_num: int
        :param amount_after_discount: 订单优惠后金额（实付价格，不含券不含卡）。
        :type amount_after_discount: float
        :param official_amount: 订单金额（官网价）。 退订订单中，该金额等于currencyAfterDiscount。
        :type official_amount: float
        :param amount_info: 
        :type amount_info: :class:`huaweicloudsdkbssintl.v2.AmountInfomationV2`
        :param currency: 货币编码。
        :type currency: str
        :param category_code: 产品目录编码。
        :type category_code: str
        :param product_owner_service: 产品归属的云服务类型编码。 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。
        :type product_owner_service: str
        :param commercial_resource: 商务归属的资源类型编码。 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。
        :type commercial_resource: str
        """
        
        

        self._order_line_item_id = None
        self._service_type_code = None
        self._service_type_name = None
        self._product_id = None
        self._product_spec_desc = None
        self._period_type = None
        self._period_num = None
        self._effective_time = None
        self._expire_time = None
        self._subscription_num = None
        self._amount_after_discount = None
        self._official_amount = None
        self._amount_info = None
        self._currency = None
        self._category_code = None
        self._product_owner_service = None
        self._commercial_resource = None
        self.discriminator = None

        if order_line_item_id is not None:
            self.order_line_item_id = order_line_item_id
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if service_type_name is not None:
            self.service_type_name = service_type_name
        if product_id is not None:
            self.product_id = product_id
        if product_spec_desc is not None:
            self.product_spec_desc = product_spec_desc
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time
        if subscription_num is not None:
            self.subscription_num = subscription_num
        if amount_after_discount is not None:
            self.amount_after_discount = amount_after_discount
        if official_amount is not None:
            self.official_amount = official_amount
        if amount_info is not None:
            self.amount_info = amount_info
        if currency is not None:
            self.currency = currency
        if category_code is not None:
            self.category_code = category_code
        if product_owner_service is not None:
            self.product_owner_service = product_owner_service
        if commercial_resource is not None:
            self.commercial_resource = commercial_resource

    @property
    def order_line_item_id(self):
        """Gets the order_line_item_id of this OrderLineItemEntityV2.

        订单项ID。

        :return: The order_line_item_id of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._order_line_item_id

    @order_line_item_id.setter
    def order_line_item_id(self, order_line_item_id):
        """Sets the order_line_item_id of this OrderLineItemEntityV2.

        订单项ID。

        :param order_line_item_id: The order_line_item_id of this OrderLineItemEntityV2.
        :type order_line_item_id: str
        """
        self._order_line_item_id = order_line_item_id

    @property
    def service_type_code(self):
        """Gets the service_type_code of this OrderLineItemEntityV2.

        云服务类型编码。例如OBS的云服务类型编码为“hws.service.type.obs”。

        :return: The service_type_code of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this OrderLineItemEntityV2.

        云服务类型编码。例如OBS的云服务类型编码为“hws.service.type.obs”。

        :param service_type_code: The service_type_code of this OrderLineItemEntityV2.
        :type service_type_code: str
        """
        self._service_type_code = service_type_code

    @property
    def service_type_name(self):
        """Gets the service_type_name of this OrderLineItemEntityV2.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :return: The service_type_name of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._service_type_name

    @service_type_name.setter
    def service_type_name(self, service_type_name):
        """Sets the service_type_name of this OrderLineItemEntityV2.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :param service_type_name: The service_type_name of this OrderLineItemEntityV2.
        :type service_type_name: str
        """
        self._service_type_name = service_type_name

    @property
    def product_id(self):
        """Gets the product_id of this OrderLineItemEntityV2.

        产品ID。

        :return: The product_id of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this OrderLineItemEntityV2.

        产品ID。

        :param product_id: The product_id of this OrderLineItemEntityV2.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def product_spec_desc(self):
        """Gets the product_spec_desc of this OrderLineItemEntityV2.

        产品规格描述。

        :return: The product_spec_desc of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._product_spec_desc

    @product_spec_desc.setter
    def product_spec_desc(self, product_spec_desc):
        """Sets the product_spec_desc of this OrderLineItemEntityV2.

        产品规格描述。

        :param product_spec_desc: The product_spec_desc of this OrderLineItemEntityV2.
        :type product_spec_desc: str
        """
        self._product_spec_desc = product_spec_desc

    @property
    def period_type(self):
        """Gets the period_type of this OrderLineItemEntityV2.

        周期类型。 0：天1：周2：月3：年4：小时5：一次性6：按需（预留）7：按用量报表使用（预留）

        :return: The period_type of this OrderLineItemEntityV2.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this OrderLineItemEntityV2.

        周期类型。 0：天1：周2：月3：年4：小时5：一次性6：按需（预留）7：按用量报表使用（预留）

        :param period_type: The period_type of this OrderLineItemEntityV2.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this OrderLineItemEntityV2.

        周期数量。  说明： 当订单为退订资源的订单时，参数取值为null。

        :return: The period_num of this OrderLineItemEntityV2.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this OrderLineItemEntityV2.

        周期数量。  说明： 当订单为退订资源的订单时，参数取值为null。

        :param period_num: The period_num of this OrderLineItemEntityV2.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def effective_time(self):
        """Gets the effective_time of this OrderLineItemEntityV2.

        生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。

        :return: The effective_time of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        """Sets the effective_time of this OrderLineItemEntityV2.

        生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。

        :param effective_time: The effective_time of this OrderLineItemEntityV2.
        :type effective_time: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        """Gets the expire_time of this OrderLineItemEntityV2.

        失效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。

        :return: The expire_time of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this OrderLineItemEntityV2.

        失效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。

        :param expire_time: The expire_time of this OrderLineItemEntityV2.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def subscription_num(self):
        """Gets the subscription_num of this OrderLineItemEntityV2.

        订购数量。

        :return: The subscription_num of this OrderLineItemEntityV2.
        :rtype: int
        """
        return self._subscription_num

    @subscription_num.setter
    def subscription_num(self, subscription_num):
        """Sets the subscription_num of this OrderLineItemEntityV2.

        订购数量。

        :param subscription_num: The subscription_num of this OrderLineItemEntityV2.
        :type subscription_num: int
        """
        self._subscription_num = subscription_num

    @property
    def amount_after_discount(self):
        """Gets the amount_after_discount of this OrderLineItemEntityV2.

        订单优惠后金额（实付价格，不含券不含卡）。

        :return: The amount_after_discount of this OrderLineItemEntityV2.
        :rtype: float
        """
        return self._amount_after_discount

    @amount_after_discount.setter
    def amount_after_discount(self, amount_after_discount):
        """Sets the amount_after_discount of this OrderLineItemEntityV2.

        订单优惠后金额（实付价格，不含券不含卡）。

        :param amount_after_discount: The amount_after_discount of this OrderLineItemEntityV2.
        :type amount_after_discount: float
        """
        self._amount_after_discount = amount_after_discount

    @property
    def official_amount(self):
        """Gets the official_amount of this OrderLineItemEntityV2.

        订单金额（官网价）。 退订订单中，该金额等于currencyAfterDiscount。

        :return: The official_amount of this OrderLineItemEntityV2.
        :rtype: float
        """
        return self._official_amount

    @official_amount.setter
    def official_amount(self, official_amount):
        """Sets the official_amount of this OrderLineItemEntityV2.

        订单金额（官网价）。 退订订单中，该金额等于currencyAfterDiscount。

        :param official_amount: The official_amount of this OrderLineItemEntityV2.
        :type official_amount: float
        """
        self._official_amount = official_amount

    @property
    def amount_info(self):
        """Gets the amount_info of this OrderLineItemEntityV2.

        :return: The amount_info of this OrderLineItemEntityV2.
        :rtype: :class:`huaweicloudsdkbssintl.v2.AmountInfomationV2`
        """
        return self._amount_info

    @amount_info.setter
    def amount_info(self, amount_info):
        """Sets the amount_info of this OrderLineItemEntityV2.

        :param amount_info: The amount_info of this OrderLineItemEntityV2.
        :type amount_info: :class:`huaweicloudsdkbssintl.v2.AmountInfomationV2`
        """
        self._amount_info = amount_info

    @property
    def currency(self):
        """Gets the currency of this OrderLineItemEntityV2.

        货币编码。

        :return: The currency of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this OrderLineItemEntityV2.

        货币编码。

        :param currency: The currency of this OrderLineItemEntityV2.
        :type currency: str
        """
        self._currency = currency

    @property
    def category_code(self):
        """Gets the category_code of this OrderLineItemEntityV2.

        产品目录编码。

        :return: The category_code of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._category_code

    @category_code.setter
    def category_code(self, category_code):
        """Sets the category_code of this OrderLineItemEntityV2.

        产品目录编码。

        :param category_code: The category_code of this OrderLineItemEntityV2.
        :type category_code: str
        """
        self._category_code = category_code

    @property
    def product_owner_service(self):
        """Gets the product_owner_service of this OrderLineItemEntityV2.

        产品归属的云服务类型编码。 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :return: The product_owner_service of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._product_owner_service

    @product_owner_service.setter
    def product_owner_service(self, product_owner_service):
        """Sets the product_owner_service of this OrderLineItemEntityV2.

        产品归属的云服务类型编码。 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :param product_owner_service: The product_owner_service of this OrderLineItemEntityV2.
        :type product_owner_service: str
        """
        self._product_owner_service = product_owner_service

    @property
    def commercial_resource(self):
        """Gets the commercial_resource of this OrderLineItemEntityV2.

        商务归属的资源类型编码。 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :return: The commercial_resource of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._commercial_resource

    @commercial_resource.setter
    def commercial_resource(self, commercial_resource):
        """Sets the commercial_resource of this OrderLineItemEntityV2.

        商务归属的资源类型编码。 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :param commercial_resource: The commercial_resource of this OrderLineItemEntityV2.
        :type commercial_resource: str
        """
        self._commercial_resource = commercial_resource

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
        if not isinstance(other, OrderLineItemEntityV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
