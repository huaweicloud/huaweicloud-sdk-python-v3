# coding: utf-8

import pprint
import re

import six





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

    def __init__(self, order_line_item_id=None, service_type_code=None, product_id=None, product_spec_desc=None, period_type=None, period_num=None, effective_time=None, expire_time=None, subscription_num=None, amount_after_discount=None, official_amount=None, amount_info=None, currency=None, category_code=None, product_owner_service=None, commercial_resource=None):
        """OrderLineItemEntityV2 - a model defined in huaweicloud sdk"""
        
        

        self._order_line_item_id = None
        self._service_type_code = None
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

        |参数名称：订单项Id。| |参数约束及描述：订单项Id。|

        :return: The order_line_item_id of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._order_line_item_id

    @order_line_item_id.setter
    def order_line_item_id(self, order_line_item_id):
        """Sets the order_line_item_id of this OrderLineItemEntityV2.

        |参数名称：订单项Id。| |参数约束及描述：订单项Id。|

        :param order_line_item_id: The order_line_item_id of this OrderLineItemEntityV2.
        :type: str
        """
        self._order_line_item_id = order_line_item_id

    @property
    def service_type_code(self):
        """Gets the service_type_code of this OrderLineItemEntityV2.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。| |参数约束及描述：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。|

        :return: The service_type_code of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this OrderLineItemEntityV2.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。| |参数约束及描述：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。|

        :param service_type_code: The service_type_code of this OrderLineItemEntityV2.
        :type: str
        """
        self._service_type_code = service_type_code

    @property
    def product_id(self):
        """Gets the product_id of this OrderLineItemEntityV2.

        |参数名称：产品ID。| |参数约束及描述：产品ID。|

        :return: The product_id of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this OrderLineItemEntityV2.

        |参数名称：产品ID。| |参数约束及描述：产品ID。|

        :param product_id: The product_id of this OrderLineItemEntityV2.
        :type: str
        """
        self._product_id = product_id

    @property
    def product_spec_desc(self):
        """Gets the product_spec_desc of this OrderLineItemEntityV2.

        |参数名称：产品规格描述。| |参数约束及描述：产品规格描述。|

        :return: The product_spec_desc of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._product_spec_desc

    @product_spec_desc.setter
    def product_spec_desc(self, product_spec_desc):
        """Sets the product_spec_desc of this OrderLineItemEntityV2.

        |参数名称：产品规格描述。| |参数约束及描述：产品规格描述。|

        :param product_spec_desc: The product_spec_desc of this OrderLineItemEntityV2.
        :type: str
        """
        self._product_spec_desc = product_spec_desc

    @property
    def period_type(self):
        """Gets the period_type of this OrderLineItemEntityV2.

        |参数名称：周期类型。0：天；1：周；2：月；3：年；4：小时；5：一次性；6：按需（预留）；7：按用量报表使用（预留）。| |参数的约束及描述：周期类型。0：天；1：周；2：月；3：年；4：小时；5：一次性；6：按需（预留）；7：按用量报表使用（预留）。|

        :return: The period_type of this OrderLineItemEntityV2.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this OrderLineItemEntityV2.

        |参数名称：周期类型。0：天；1：周；2：月；3：年；4：小时；5：一次性；6：按需（预留）；7：按用量报表使用（预留）。| |参数的约束及描述：周期类型。0：天；1：周；2：月；3：年；4：小时；5：一次性；6：按需（预留）；7：按用量报表使用（预留）。|

        :param period_type: The period_type of this OrderLineItemEntityV2.
        :type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this OrderLineItemEntityV2.

        |参数名称：周期数量。| |参数的约束及描述：周期数量。|

        :return: The period_num of this OrderLineItemEntityV2.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this OrderLineItemEntityV2.

        |参数名称：周期数量。| |参数的约束及描述：周期数量。|

        :param period_num: The period_num of this OrderLineItemEntityV2.
        :type: int
        """
        self._period_num = period_num

    @property
    def effective_time(self):
        """Gets the effective_time of this OrderLineItemEntityV2.

        |参数名称：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数约束及描述：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。|

        :return: The effective_time of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        """Sets the effective_time of this OrderLineItemEntityV2.

        |参数名称：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数约束及描述：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。|

        :param effective_time: The effective_time of this OrderLineItemEntityV2.
        :type: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        """Gets the expire_time of this OrderLineItemEntityV2.

        |参数名称：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数约束及描述：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。|

        :return: The expire_time of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this OrderLineItemEntityV2.

        |参数名称：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数约束及描述：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。|

        :param expire_time: The expire_time of this OrderLineItemEntityV2.
        :type: str
        """
        self._expire_time = expire_time

    @property
    def subscription_num(self):
        """Gets the subscription_num of this OrderLineItemEntityV2.

        |参数名称：订购数量。| |参数的约束及描述：订购数量。|

        :return: The subscription_num of this OrderLineItemEntityV2.
        :rtype: int
        """
        return self._subscription_num

    @subscription_num.setter
    def subscription_num(self, subscription_num):
        """Sets the subscription_num of this OrderLineItemEntityV2.

        |参数名称：订购数量。| |参数的约束及描述：订购数量。|

        :param subscription_num: The subscription_num of this OrderLineItemEntityV2.
        :type: int
        """
        self._subscription_num = subscription_num

    @property
    def amount_after_discount(self):
        """Gets the amount_after_discount of this OrderLineItemEntityV2.

        |参数名称：订单优惠后金额（实付价格，不含券不含卡）。| |参数的约束及描述：订单优惠后金额（实付价格，不含券不含卡）。|

        :return: The amount_after_discount of this OrderLineItemEntityV2.
        :rtype: float
        """
        return self._amount_after_discount

    @amount_after_discount.setter
    def amount_after_discount(self, amount_after_discount):
        """Sets the amount_after_discount of this OrderLineItemEntityV2.

        |参数名称：订单优惠后金额（实付价格，不含券不含卡）。| |参数的约束及描述：订单优惠后金额（实付价格，不含券不含卡）。|

        :param amount_after_discount: The amount_after_discount of this OrderLineItemEntityV2.
        :type: float
        """
        self._amount_after_discount = amount_after_discount

    @property
    def official_amount(self):
        """Gets the official_amount of this OrderLineItemEntityV2.

        |参数名称：订单金额（官网价）。退订订单中，该金额等于currencyAfterDiscount。| |参数的约束及描述：订单金额（官网价）。退订订单中，该金额等于currencyAfterDiscount。|

        :return: The official_amount of this OrderLineItemEntityV2.
        :rtype: float
        """
        return self._official_amount

    @official_amount.setter
    def official_amount(self, official_amount):
        """Sets the official_amount of this OrderLineItemEntityV2.

        |参数名称：订单金额（官网价）。退订订单中，该金额等于currencyAfterDiscount。| |参数的约束及描述：订单金额（官网价）。退订订单中，该金额等于currencyAfterDiscount。|

        :param official_amount: The official_amount of this OrderLineItemEntityV2.
        :type: float
        """
        self._official_amount = official_amount

    @property
    def amount_info(self):
        """Gets the amount_info of this OrderLineItemEntityV2.


        :return: The amount_info of this OrderLineItemEntityV2.
        :rtype: AmountInfomationV2
        """
        return self._amount_info

    @amount_info.setter
    def amount_info(self, amount_info):
        """Sets the amount_info of this OrderLineItemEntityV2.


        :param amount_info: The amount_info of this OrderLineItemEntityV2.
        :type: AmountInfomationV2
        """
        self._amount_info = amount_info

    @property
    def currency(self):
        """Gets the currency of this OrderLineItemEntityV2.

        |参数名称：货币编码。| |参数约束及描述：货币编码。如CNY|

        :return: The currency of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this OrderLineItemEntityV2.

        |参数名称：货币编码。| |参数约束及描述：货币编码。如CNY|

        :param currency: The currency of this OrderLineItemEntityV2.
        :type: str
        """
        self._currency = currency

    @property
    def category_code(self):
        """Gets the category_code of this OrderLineItemEntityV2.

        |参数名称：产品目录编码。| |参数约束及描述：产品目录编码。|

        :return: The category_code of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._category_code

    @category_code.setter
    def category_code(self, category_code):
        """Sets the category_code of this OrderLineItemEntityV2.

        |参数名称：产品目录编码。| |参数约束及描述：产品目录编码。|

        :param category_code: The category_code of this OrderLineItemEntityV2.
        :type: str
        """
        self._category_code = category_code

    @property
    def product_owner_service(self):
        """Gets the product_owner_service of this OrderLineItemEntityV2.

        |参数名称：产品归属的云服务类型编码。| |参数约束及描述：产品归属的云服务类型编码。|

        :return: The product_owner_service of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._product_owner_service

    @product_owner_service.setter
    def product_owner_service(self, product_owner_service):
        """Sets the product_owner_service of this OrderLineItemEntityV2.

        |参数名称：产品归属的云服务类型编码。| |参数约束及描述：产品归属的云服务类型编码。|

        :param product_owner_service: The product_owner_service of this OrderLineItemEntityV2.
        :type: str
        """
        self._product_owner_service = product_owner_service

    @property
    def commercial_resource(self):
        """Gets the commercial_resource of this OrderLineItemEntityV2.

        |参数名称：商务归属的资源类型编码。| |参数约束及描述：商务归属的资源类型编码。|

        :return: The commercial_resource of this OrderLineItemEntityV2.
        :rtype: str
        """
        return self._commercial_resource

    @commercial_resource.setter
    def commercial_resource(self, commercial_resource):
        """Sets the commercial_resource of this OrderLineItemEntityV2.

        |参数名称：商务归属的资源类型编码。| |参数约束及描述：商务归属的资源类型编码。|

        :param commercial_resource: The commercial_resource of this OrderLineItemEntityV2.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrderLineItemEntityV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
