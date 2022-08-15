# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomerOrderV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'order_id': 'str',
        'customer_id': 'str',
        'service_type_code': 'str',
        'service_type_name': 'str',
        'source_type': 'int',
        'status': 'int',
        'order_type': 'int',
        'amount_after_discount': 'float',
        'official_amount': 'float',
        'measure_id': 'int',
        'create_time': 'str',
        'payment_time': 'str',
        'currency': 'str',
        'contract_id': 'str',
        'amount_info': 'AmountInfomationV2'
    }

    attribute_map = {
        'order_id': 'order_id',
        'customer_id': 'customer_id',
        'service_type_code': 'service_type_code',
        'service_type_name': 'service_type_name',
        'source_type': 'source_type',
        'status': 'status',
        'order_type': 'order_type',
        'amount_after_discount': 'amount_after_discount',
        'official_amount': 'official_amount',
        'measure_id': 'measure_id',
        'create_time': 'create_time',
        'payment_time': 'payment_time',
        'currency': 'currency',
        'contract_id': 'contract_id',
        'amount_info': 'amount_info'
    }

    def __init__(self, order_id=None, customer_id=None, service_type_code=None, service_type_name=None, source_type=None, status=None, order_type=None, amount_after_discount=None, official_amount=None, measure_id=None, create_time=None, payment_time=None, currency=None, contract_id=None, amount_info=None):
        """CustomerOrderV2

        The model defined in huaweicloud sdk

        :param order_id: 订单ID。
        :type order_id: str
        :param customer_id: 客户账号ID。
        :type customer_id: str
        :param service_type_code: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。
        :type service_type_code: str
        :param service_type_name: 云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。
        :type service_type_name: str
        :param source_type: 客户订单订单来源类型： 1：客户2：代理3：合同4：分销商
        :type source_type: int
        :param status: 订单状态： 1：待审核2：待退款3：处理中4：已取消5：已完成6：待支付9：待确认10：待发货11：待收货12：待上门取货13：换新中
        :type status: int
        :param order_type: 订单类型： 1：开通2：续订3：变更4：退订11：按需转包年/包月13：试用14：转商用15：费用调整
        :type order_type: int
        :param amount_after_discount: 订单优惠后金额（不含券不含卡的实付价格）。
        :type amount_after_discount: float
        :param official_amount: 订单金额（官网价）。 退订订单中，该金额等于amount_after_discount。
        :type official_amount: float
        :param measure_id: 订单金额度量单位： 1：元
        :type measure_id: int
        :param create_time: 创建时间 。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。
        :type create_time: str
        :param payment_time: 支付时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。
        :type payment_time: str
        :param currency: 货币编码。
        :type currency: str
        :param contract_id: 合同ID。
        :type contract_id: str
        :param amount_info: 
        :type amount_info: :class:`huaweicloudsdkbss.v2.AmountInfomationV2`
        """
        
        

        self._order_id = None
        self._customer_id = None
        self._service_type_code = None
        self._service_type_name = None
        self._source_type = None
        self._status = None
        self._order_type = None
        self._amount_after_discount = None
        self._official_amount = None
        self._measure_id = None
        self._create_time = None
        self._payment_time = None
        self._currency = None
        self._contract_id = None
        self._amount_info = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if customer_id is not None:
            self.customer_id = customer_id
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if service_type_name is not None:
            self.service_type_name = service_type_name
        if source_type is not None:
            self.source_type = source_type
        if status is not None:
            self.status = status
        if order_type is not None:
            self.order_type = order_type
        if amount_after_discount is not None:
            self.amount_after_discount = amount_after_discount
        if official_amount is not None:
            self.official_amount = official_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if create_time is not None:
            self.create_time = create_time
        if payment_time is not None:
            self.payment_time = payment_time
        if currency is not None:
            self.currency = currency
        if contract_id is not None:
            self.contract_id = contract_id
        if amount_info is not None:
            self.amount_info = amount_info

    @property
    def order_id(self):
        """Gets the order_id of this CustomerOrderV2.

        订单ID。

        :return: The order_id of this CustomerOrderV2.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CustomerOrderV2.

        订单ID。

        :param order_id: The order_id of this CustomerOrderV2.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def customer_id(self):
        """Gets the customer_id of this CustomerOrderV2.

        客户账号ID。

        :return: The customer_id of this CustomerOrderV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CustomerOrderV2.

        客户账号ID。

        :param customer_id: The customer_id of this CustomerOrderV2.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def service_type_code(self):
        """Gets the service_type_code of this CustomerOrderV2.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :return: The service_type_code of this CustomerOrderV2.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this CustomerOrderV2.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :param service_type_code: The service_type_code of this CustomerOrderV2.
        :type service_type_code: str
        """
        self._service_type_code = service_type_code

    @property
    def service_type_name(self):
        """Gets the service_type_name of this CustomerOrderV2.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :return: The service_type_name of this CustomerOrderV2.
        :rtype: str
        """
        return self._service_type_name

    @service_type_name.setter
    def service_type_name(self, service_type_name):
        """Sets the service_type_name of this CustomerOrderV2.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :param service_type_name: The service_type_name of this CustomerOrderV2.
        :type service_type_name: str
        """
        self._service_type_name = service_type_name

    @property
    def source_type(self):
        """Gets the source_type of this CustomerOrderV2.

        客户订单订单来源类型： 1：客户2：代理3：合同4：分销商

        :return: The source_type of this CustomerOrderV2.
        :rtype: int
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this CustomerOrderV2.

        客户订单订单来源类型： 1：客户2：代理3：合同4：分销商

        :param source_type: The source_type of this CustomerOrderV2.
        :type source_type: int
        """
        self._source_type = source_type

    @property
    def status(self):
        """Gets the status of this CustomerOrderV2.

        订单状态： 1：待审核2：待退款3：处理中4：已取消5：已完成6：待支付9：待确认10：待发货11：待收货12：待上门取货13：换新中

        :return: The status of this CustomerOrderV2.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CustomerOrderV2.

        订单状态： 1：待审核2：待退款3：处理中4：已取消5：已完成6：待支付9：待确认10：待发货11：待收货12：待上门取货13：换新中

        :param status: The status of this CustomerOrderV2.
        :type status: int
        """
        self._status = status

    @property
    def order_type(self):
        """Gets the order_type of this CustomerOrderV2.

        订单类型： 1：开通2：续订3：变更4：退订11：按需转包年/包月13：试用14：转商用15：费用调整

        :return: The order_type of this CustomerOrderV2.
        :rtype: int
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this CustomerOrderV2.

        订单类型： 1：开通2：续订3：变更4：退订11：按需转包年/包月13：试用14：转商用15：费用调整

        :param order_type: The order_type of this CustomerOrderV2.
        :type order_type: int
        """
        self._order_type = order_type

    @property
    def amount_after_discount(self):
        """Gets the amount_after_discount of this CustomerOrderV2.

        订单优惠后金额（不含券不含卡的实付价格）。

        :return: The amount_after_discount of this CustomerOrderV2.
        :rtype: float
        """
        return self._amount_after_discount

    @amount_after_discount.setter
    def amount_after_discount(self, amount_after_discount):
        """Sets the amount_after_discount of this CustomerOrderV2.

        订单优惠后金额（不含券不含卡的实付价格）。

        :param amount_after_discount: The amount_after_discount of this CustomerOrderV2.
        :type amount_after_discount: float
        """
        self._amount_after_discount = amount_after_discount

    @property
    def official_amount(self):
        """Gets the official_amount of this CustomerOrderV2.

        订单金额（官网价）。 退订订单中，该金额等于amount_after_discount。

        :return: The official_amount of this CustomerOrderV2.
        :rtype: float
        """
        return self._official_amount

    @official_amount.setter
    def official_amount(self, official_amount):
        """Sets the official_amount of this CustomerOrderV2.

        订单金额（官网价）。 退订订单中，该金额等于amount_after_discount。

        :param official_amount: The official_amount of this CustomerOrderV2.
        :type official_amount: float
        """
        self._official_amount = official_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this CustomerOrderV2.

        订单金额度量单位： 1：元

        :return: The measure_id of this CustomerOrderV2.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this CustomerOrderV2.

        订单金额度量单位： 1：元

        :param measure_id: The measure_id of this CustomerOrderV2.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def create_time(self):
        """Gets the create_time of this CustomerOrderV2.

        创建时间 。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。

        :return: The create_time of this CustomerOrderV2.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CustomerOrderV2.

        创建时间 。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。

        :param create_time: The create_time of this CustomerOrderV2.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def payment_time(self):
        """Gets the payment_time of this CustomerOrderV2.

        支付时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。

        :return: The payment_time of this CustomerOrderV2.
        :rtype: str
        """
        return self._payment_time

    @payment_time.setter
    def payment_time(self, payment_time):
        """Sets the payment_time of this CustomerOrderV2.

        支付时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。

        :param payment_time: The payment_time of this CustomerOrderV2.
        :type payment_time: str
        """
        self._payment_time = payment_time

    @property
    def currency(self):
        """Gets the currency of this CustomerOrderV2.

        货币编码。

        :return: The currency of this CustomerOrderV2.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CustomerOrderV2.

        货币编码。

        :param currency: The currency of this CustomerOrderV2.
        :type currency: str
        """
        self._currency = currency

    @property
    def contract_id(self):
        """Gets the contract_id of this CustomerOrderV2.

        合同ID。

        :return: The contract_id of this CustomerOrderV2.
        :rtype: str
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this CustomerOrderV2.

        合同ID。

        :param contract_id: The contract_id of this CustomerOrderV2.
        :type contract_id: str
        """
        self._contract_id = contract_id

    @property
    def amount_info(self):
        """Gets the amount_info of this CustomerOrderV2.


        :return: The amount_info of this CustomerOrderV2.
        :rtype: :class:`huaweicloudsdkbss.v2.AmountInfomationV2`
        """
        return self._amount_info

    @amount_info.setter
    def amount_info(self, amount_info):
        """Sets the amount_info of this CustomerOrderV2.


        :param amount_info: The amount_info of this CustomerOrderV2.
        :type amount_info: :class:`huaweicloudsdkbss.v2.AmountInfomationV2`
        """
        self._amount_info = amount_info

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
        if not isinstance(other, CustomerOrderV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
