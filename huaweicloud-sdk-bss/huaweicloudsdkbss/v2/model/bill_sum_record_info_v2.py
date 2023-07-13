# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BillSumRecordInfoV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bill_cycle': 'str',
        'resource_type_code': 'str',
        'service_type_code': 'str',
        'service_type_name': 'str',
        'resource_type_name': 'str',
        'charging_mode': 'int',
        'official_amount': 'decimal.Decimal',
        'official_discount_amount': 'decimal.Decimal',
        'truncated_amount': 'decimal.Decimal',
        'consume_amount': 'decimal.Decimal',
        'coupon_amount': 'decimal.Decimal',
        'flexipurchase_coupon_amount': 'decimal.Decimal',
        'stored_value_card_amount': 'decimal.Decimal',
        'debt_amount': 'decimal.Decimal',
        'writeoff_amount': 'decimal.Decimal',
        'cash_amount': 'decimal.Decimal',
        'credit_amount': 'decimal.Decimal',
        'measure_id': 'int',
        'bill_type': 'int',
        'customer_id': 'str'
    }

    attribute_map = {
        'bill_cycle': 'bill_cycle',
        'resource_type_code': 'resource_type_code',
        'service_type_code': 'service_type_code',
        'service_type_name': 'service_type_name',
        'resource_type_name': 'resource_type_name',
        'charging_mode': 'charging_mode',
        'official_amount': 'official_amount',
        'official_discount_amount': 'official_discount_amount',
        'truncated_amount': 'truncated_amount',
        'consume_amount': 'consume_amount',
        'coupon_amount': 'coupon_amount',
        'flexipurchase_coupon_amount': 'flexipurchase_coupon_amount',
        'stored_value_card_amount': 'stored_value_card_amount',
        'debt_amount': 'debt_amount',
        'writeoff_amount': 'writeoff_amount',
        'cash_amount': 'cash_amount',
        'credit_amount': 'credit_amount',
        'measure_id': 'measure_id',
        'bill_type': 'bill_type',
        'customer_id': 'customer_id'
    }

    def __init__(self, bill_cycle=None, resource_type_code=None, service_type_code=None, service_type_name=None, resource_type_name=None, charging_mode=None, official_amount=None, official_discount_amount=None, truncated_amount=None, consume_amount=None, coupon_amount=None, flexipurchase_coupon_amount=None, stored_value_card_amount=None, debt_amount=None, writeoff_amount=None, cash_amount=None, credit_amount=None, measure_id=None, bill_type=None, customer_id=None):
        """BillSumRecordInfoV2

        The model defined in huaweicloud sdk

        :param bill_cycle: 消费汇总数据所在账期，东八区时间，格式：YYYY-MM。
        :type bill_cycle: str
        :param resource_type_code: 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。
        :type resource_type_code: str
        :param service_type_code: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。
        :type service_type_code: str
        :param service_type_name: 云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。
        :type service_type_name: str
        :param resource_type_name: 资源类型名称。例如ECS的资源类型名称为“云主机”。
        :type resource_type_name: str
        :param charging_mode: 计费模式。 1：包年/包月3：按需10：预留实例
        :type charging_mode: int
        :param official_amount: 官网价。
        :type official_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param official_discount_amount: 折扣金额。
        :type official_discount_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param truncated_amount: 抹零金额。
        :type truncated_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param consume_amount: 应付金额。 应付金额&#x3D;官网价-折扣金额-抹零金额
        :type consume_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param coupon_amount: 代金券金额。
        :type coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param flexipurchase_coupon_amount: 现金券金额，预留。
        :type flexipurchase_coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param stored_value_card_amount: 储值卡金额，预留。
        :type stored_value_card_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param debt_amount: 欠费金额。即伙伴从客户账户扣费时，客户账户金额不足，欠费的金额。
        :type debt_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param writeoff_amount: 欠费核销金额。
        :type writeoff_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param cash_amount: 现金账户金额。
        :type cash_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param credit_amount: 信用账户金额。
        :type credit_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param measure_id: 金额单位。 1：元
        :type measure_id: int
        :param bill_type: 账单类型。 1：消费2：退款3：调账
        :type bill_type: int
        :param customer_id: 消费的客户账号ID。 如果是普通客户或者企业子客户查询消费记录，只能查询到客户自己的消费记录，且此处显示的是客户自己的客户ID。如果是企业主查询消费记录，可以查询到企业主以及企业子客户的消费记录，此处为消费的实际客户ID。如果是企业主自己的消费记录，则为企业主ID；如果是某个企业子客户的消费记录，则此处为企业子账号ID。
        :type customer_id: str
        """
        
        

        self._bill_cycle = None
        self._resource_type_code = None
        self._service_type_code = None
        self._service_type_name = None
        self._resource_type_name = None
        self._charging_mode = None
        self._official_amount = None
        self._official_discount_amount = None
        self._truncated_amount = None
        self._consume_amount = None
        self._coupon_amount = None
        self._flexipurchase_coupon_amount = None
        self._stored_value_card_amount = None
        self._debt_amount = None
        self._writeoff_amount = None
        self._cash_amount = None
        self._credit_amount = None
        self._measure_id = None
        self._bill_type = None
        self._customer_id = None
        self.discriminator = None

        if bill_cycle is not None:
            self.bill_cycle = bill_cycle
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if service_type_name is not None:
            self.service_type_name = service_type_name
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if official_amount is not None:
            self.official_amount = official_amount
        if official_discount_amount is not None:
            self.official_discount_amount = official_discount_amount
        if truncated_amount is not None:
            self.truncated_amount = truncated_amount
        if consume_amount is not None:
            self.consume_amount = consume_amount
        if coupon_amount is not None:
            self.coupon_amount = coupon_amount
        if flexipurchase_coupon_amount is not None:
            self.flexipurchase_coupon_amount = flexipurchase_coupon_amount
        if stored_value_card_amount is not None:
            self.stored_value_card_amount = stored_value_card_amount
        if debt_amount is not None:
            self.debt_amount = debt_amount
        if writeoff_amount is not None:
            self.writeoff_amount = writeoff_amount
        if cash_amount is not None:
            self.cash_amount = cash_amount
        if credit_amount is not None:
            self.credit_amount = credit_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if bill_type is not None:
            self.bill_type = bill_type
        if customer_id is not None:
            self.customer_id = customer_id

    @property
    def bill_cycle(self):
        """Gets the bill_cycle of this BillSumRecordInfoV2.

        消费汇总数据所在账期，东八区时间，格式：YYYY-MM。

        :return: The bill_cycle of this BillSumRecordInfoV2.
        :rtype: str
        """
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, bill_cycle):
        """Sets the bill_cycle of this BillSumRecordInfoV2.

        消费汇总数据所在账期，东八区时间，格式：YYYY-MM。

        :param bill_cycle: The bill_cycle of this BillSumRecordInfoV2.
        :type bill_cycle: str
        """
        self._bill_cycle = bill_cycle

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this BillSumRecordInfoV2.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :return: The resource_type_code of this BillSumRecordInfoV2.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this BillSumRecordInfoV2.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :param resource_type_code: The resource_type_code of this BillSumRecordInfoV2.
        :type resource_type_code: str
        """
        self._resource_type_code = resource_type_code

    @property
    def service_type_code(self):
        """Gets the service_type_code of this BillSumRecordInfoV2.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :return: The service_type_code of this BillSumRecordInfoV2.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this BillSumRecordInfoV2.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :param service_type_code: The service_type_code of this BillSumRecordInfoV2.
        :type service_type_code: str
        """
        self._service_type_code = service_type_code

    @property
    def service_type_name(self):
        """Gets the service_type_name of this BillSumRecordInfoV2.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :return: The service_type_name of this BillSumRecordInfoV2.
        :rtype: str
        """
        return self._service_type_name

    @service_type_name.setter
    def service_type_name(self, service_type_name):
        """Sets the service_type_name of this BillSumRecordInfoV2.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :param service_type_name: The service_type_name of this BillSumRecordInfoV2.
        :type service_type_name: str
        """
        self._service_type_name = service_type_name

    @property
    def resource_type_name(self):
        """Gets the resource_type_name of this BillSumRecordInfoV2.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :return: The resource_type_name of this BillSumRecordInfoV2.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        """Sets the resource_type_name of this BillSumRecordInfoV2.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :param resource_type_name: The resource_type_name of this BillSumRecordInfoV2.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def charging_mode(self):
        """Gets the charging_mode of this BillSumRecordInfoV2.

        计费模式。 1：包年/包月3：按需10：预留实例

        :return: The charging_mode of this BillSumRecordInfoV2.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this BillSumRecordInfoV2.

        计费模式。 1：包年/包月3：按需10：预留实例

        :param charging_mode: The charging_mode of this BillSumRecordInfoV2.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def official_amount(self):
        """Gets the official_amount of this BillSumRecordInfoV2.

        官网价。

        :return: The official_amount of this BillSumRecordInfoV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._official_amount

    @official_amount.setter
    def official_amount(self, official_amount):
        """Sets the official_amount of this BillSumRecordInfoV2.

        官网价。

        :param official_amount: The official_amount of this BillSumRecordInfoV2.
        :type official_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._official_amount = official_amount

    @property
    def official_discount_amount(self):
        """Gets the official_discount_amount of this BillSumRecordInfoV2.

        折扣金额。

        :return: The official_discount_amount of this BillSumRecordInfoV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._official_discount_amount

    @official_discount_amount.setter
    def official_discount_amount(self, official_discount_amount):
        """Sets the official_discount_amount of this BillSumRecordInfoV2.

        折扣金额。

        :param official_discount_amount: The official_discount_amount of this BillSumRecordInfoV2.
        :type official_discount_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._official_discount_amount = official_discount_amount

    @property
    def truncated_amount(self):
        """Gets the truncated_amount of this BillSumRecordInfoV2.

        抹零金额。

        :return: The truncated_amount of this BillSumRecordInfoV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._truncated_amount

    @truncated_amount.setter
    def truncated_amount(self, truncated_amount):
        """Sets the truncated_amount of this BillSumRecordInfoV2.

        抹零金额。

        :param truncated_amount: The truncated_amount of this BillSumRecordInfoV2.
        :type truncated_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._truncated_amount = truncated_amount

    @property
    def consume_amount(self):
        """Gets the consume_amount of this BillSumRecordInfoV2.

        应付金额。 应付金额=官网价-折扣金额-抹零金额

        :return: The consume_amount of this BillSumRecordInfoV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._consume_amount

    @consume_amount.setter
    def consume_amount(self, consume_amount):
        """Sets the consume_amount of this BillSumRecordInfoV2.

        应付金额。 应付金额=官网价-折扣金额-抹零金额

        :param consume_amount: The consume_amount of this BillSumRecordInfoV2.
        :type consume_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._consume_amount = consume_amount

    @property
    def coupon_amount(self):
        """Gets the coupon_amount of this BillSumRecordInfoV2.

        代金券金额。

        :return: The coupon_amount of this BillSumRecordInfoV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, coupon_amount):
        """Sets the coupon_amount of this BillSumRecordInfoV2.

        代金券金额。

        :param coupon_amount: The coupon_amount of this BillSumRecordInfoV2.
        :type coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._coupon_amount = coupon_amount

    @property
    def flexipurchase_coupon_amount(self):
        """Gets the flexipurchase_coupon_amount of this BillSumRecordInfoV2.

        现金券金额，预留。

        :return: The flexipurchase_coupon_amount of this BillSumRecordInfoV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._flexipurchase_coupon_amount

    @flexipurchase_coupon_amount.setter
    def flexipurchase_coupon_amount(self, flexipurchase_coupon_amount):
        """Sets the flexipurchase_coupon_amount of this BillSumRecordInfoV2.

        现金券金额，预留。

        :param flexipurchase_coupon_amount: The flexipurchase_coupon_amount of this BillSumRecordInfoV2.
        :type flexipurchase_coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._flexipurchase_coupon_amount = flexipurchase_coupon_amount

    @property
    def stored_value_card_amount(self):
        """Gets the stored_value_card_amount of this BillSumRecordInfoV2.

        储值卡金额，预留。

        :return: The stored_value_card_amount of this BillSumRecordInfoV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._stored_value_card_amount

    @stored_value_card_amount.setter
    def stored_value_card_amount(self, stored_value_card_amount):
        """Sets the stored_value_card_amount of this BillSumRecordInfoV2.

        储值卡金额，预留。

        :param stored_value_card_amount: The stored_value_card_amount of this BillSumRecordInfoV2.
        :type stored_value_card_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._stored_value_card_amount = stored_value_card_amount

    @property
    def debt_amount(self):
        """Gets the debt_amount of this BillSumRecordInfoV2.

        欠费金额。即伙伴从客户账户扣费时，客户账户金额不足，欠费的金额。

        :return: The debt_amount of this BillSumRecordInfoV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._debt_amount

    @debt_amount.setter
    def debt_amount(self, debt_amount):
        """Sets the debt_amount of this BillSumRecordInfoV2.

        欠费金额。即伙伴从客户账户扣费时，客户账户金额不足，欠费的金额。

        :param debt_amount: The debt_amount of this BillSumRecordInfoV2.
        :type debt_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._debt_amount = debt_amount

    @property
    def writeoff_amount(self):
        """Gets the writeoff_amount of this BillSumRecordInfoV2.

        欠费核销金额。

        :return: The writeoff_amount of this BillSumRecordInfoV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._writeoff_amount

    @writeoff_amount.setter
    def writeoff_amount(self, writeoff_amount):
        """Sets the writeoff_amount of this BillSumRecordInfoV2.

        欠费核销金额。

        :param writeoff_amount: The writeoff_amount of this BillSumRecordInfoV2.
        :type writeoff_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._writeoff_amount = writeoff_amount

    @property
    def cash_amount(self):
        """Gets the cash_amount of this BillSumRecordInfoV2.

        现金账户金额。

        :return: The cash_amount of this BillSumRecordInfoV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._cash_amount

    @cash_amount.setter
    def cash_amount(self, cash_amount):
        """Sets the cash_amount of this BillSumRecordInfoV2.

        现金账户金额。

        :param cash_amount: The cash_amount of this BillSumRecordInfoV2.
        :type cash_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._cash_amount = cash_amount

    @property
    def credit_amount(self):
        """Gets the credit_amount of this BillSumRecordInfoV2.

        信用账户金额。

        :return: The credit_amount of this BillSumRecordInfoV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        """Sets the credit_amount of this BillSumRecordInfoV2.

        信用账户金额。

        :param credit_amount: The credit_amount of this BillSumRecordInfoV2.
        :type credit_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._credit_amount = credit_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this BillSumRecordInfoV2.

        金额单位。 1：元

        :return: The measure_id of this BillSumRecordInfoV2.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this BillSumRecordInfoV2.

        金额单位。 1：元

        :param measure_id: The measure_id of this BillSumRecordInfoV2.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def bill_type(self):
        """Gets the bill_type of this BillSumRecordInfoV2.

        账单类型。 1：消费2：退款3：调账

        :return: The bill_type of this BillSumRecordInfoV2.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this BillSumRecordInfoV2.

        账单类型。 1：消费2：退款3：调账

        :param bill_type: The bill_type of this BillSumRecordInfoV2.
        :type bill_type: int
        """
        self._bill_type = bill_type

    @property
    def customer_id(self):
        """Gets the customer_id of this BillSumRecordInfoV2.

        消费的客户账号ID。 如果是普通客户或者企业子客户查询消费记录，只能查询到客户自己的消费记录，且此处显示的是客户自己的客户ID。如果是企业主查询消费记录，可以查询到企业主以及企业子客户的消费记录，此处为消费的实际客户ID。如果是企业主自己的消费记录，则为企业主ID；如果是某个企业子客户的消费记录，则此处为企业子账号ID。

        :return: The customer_id of this BillSumRecordInfoV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this BillSumRecordInfoV2.

        消费的客户账号ID。 如果是普通客户或者企业子客户查询消费记录，只能查询到客户自己的消费记录，且此处显示的是客户自己的客户ID。如果是企业主查询消费记录，可以查询到企业主以及企业子客户的消费记录，此处为消费的实际客户ID。如果是企业主自己的消费记录，则为企业主ID；如果是某个企业子客户的消费记录，则此处为企业子账号ID。

        :param customer_id: The customer_id of this BillSumRecordInfoV2.
        :type customer_id: str
        """
        self._customer_id = customer_id

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
        if not isinstance(other, BillSumRecordInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
