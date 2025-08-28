# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MonthlyBillRecord:

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
        'customer_id': 'str',
        'service_type_code': 'str',
        'resource_type_code': 'str',
        'service_type_name': 'str',
        'resource_type_name': 'str',
        'region_code': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'charging_mode': 'int',
        'consume_time': 'str',
        'trade_time': 'str',
        'provider_type': 'int',
        'trade_id': 'str',
        'id': 'str',
        'bill_type': 'int',
        'status': 'int',
        'official_amount': 'decimal.Decimal',
        'official_discount_amount': 'decimal.Decimal',
        'erase_amount': 'decimal.Decimal',
        'consume_amount': 'decimal.Decimal',
        'cash_amount': 'decimal.Decimal',
        'credit_amount': 'decimal.Decimal',
        'coupon_amount': 'decimal.Decimal',
        'flexipurchase_coupon_amount': 'decimal.Decimal',
        'stored_value_card_amount': 'decimal.Decimal',
        'bonus_amount': 'decimal.Decimal',
        'debt_amount': 'decimal.Decimal',
        'writeoff_amount': 'decimal.Decimal',
        'region_name': 'str'
    }

    attribute_map = {
        'bill_cycle': 'bill_cycle',
        'customer_id': 'customer_id',
        'service_type_code': 'service_type_code',
        'resource_type_code': 'resource_type_code',
        'service_type_name': 'service_type_name',
        'resource_type_name': 'resource_type_name',
        'region_code': 'region_code',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'charging_mode': 'charging_mode',
        'consume_time': 'consume_time',
        'trade_time': 'trade_time',
        'provider_type': 'provider_type',
        'trade_id': 'trade_id',
        'id': 'id',
        'bill_type': 'bill_type',
        'status': 'status',
        'official_amount': 'official_amount',
        'official_discount_amount': 'official_discount_amount',
        'erase_amount': 'erase_amount',
        'consume_amount': 'consume_amount',
        'cash_amount': 'cash_amount',
        'credit_amount': 'credit_amount',
        'coupon_amount': 'coupon_amount',
        'flexipurchase_coupon_amount': 'flexipurchase_coupon_amount',
        'stored_value_card_amount': 'stored_value_card_amount',
        'bonus_amount': 'bonus_amount',
        'debt_amount': 'debt_amount',
        'writeoff_amount': 'writeoff_amount',
        'region_name': 'region_name'
    }

    def __init__(self, bill_cycle=None, customer_id=None, service_type_code=None, resource_type_code=None, service_type_name=None, resource_type_name=None, region_code=None, enterprise_project_id=None, enterprise_project_name=None, charging_mode=None, consume_time=None, trade_time=None, provider_type=None, trade_id=None, id=None, bill_type=None, status=None, official_amount=None, official_discount_amount=None, erase_amount=None, consume_amount=None, cash_amount=None, credit_amount=None, coupon_amount=None, flexipurchase_coupon_amount=None, stored_value_card_amount=None, bonus_amount=None, debt_amount=None, writeoff_amount=None, region_name=None):
        r"""MonthlyBillRecord

        The model defined in huaweicloud sdk

        :param bill_cycle: 流水账单所在账期，东八区时间，格式为YYYY-MM。
        :type bill_cycle: str
        :param customer_id: 消费的客户账号ID。 如果是普通客户或者企业子客户查询消费记录，只能查询到客户自己的消费记录，且此处显示的是客户自己的客户ID。如果是企业主查询消费记录，可以查询到企业主以及企业子客户的消费记录，此处为消费的实际客户ID。如果是企业主自己的消费记录，则为企业主ID；如果是某个企业子客户的消费记录，则此处为企业子账号ID。
        :type customer_id: str
        :param service_type_code: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。
        :type service_type_code: str
        :param resource_type_code: 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。
        :type resource_type_code: str
        :param service_type_name: 云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。
        :type service_type_name: str
        :param resource_type_name: 资源类型名称。例如ECS的资源类型名称为“云主机”。
        :type resource_type_name: str
        :param region_code: 云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。
        :type region_code: str
        :param enterprise_project_id: 企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业项目的名称。
        :type enterprise_project_name: str
        :param charging_mode: 计费模式。 1：包年/包月3：按需10：预留实例11：节省计划
        :type charging_mode: int
        :param consume_time: 消费时间。 计费模式为包年/包月和预留实例场景时为订单的支付时间。计费模式为按需场景时为话单的生/失效时间。
        :type consume_time: str
        :param trade_time: 交易时间，某条消费记录对应的扣费时间。
        :type trade_time: str
        :param provider_type: 服务商。 1：华为云2：云商店
        :type provider_type: int
        :param trade_id: 订单ID或交易ID，扣费维度的唯一标识。
        :type trade_id: str
        :param id: 唯一标识。 该字段为预留字段。
        :type id: str
        :param bill_type: 账单类型。1：消费-新购 2：消费-续订 3：消费-变更 4：退款-退订 5：消费-使用 8：消费-自动续订 9：调账-补偿 14：消费-服务支持计划月末扣费 16：调账-扣费 18：消费-按月付费 20：退款-变更 23：消费-节省计划抵扣 24：退款-包年/包月转按需 25：消费-抹零补扣 103：消费-按年付费
        :type bill_type: int
        :param status: 支付状态。 1：已支付2：未结清3：未结算
        :type status: int
        :param official_amount: 官网价。单位：元。  说明： official_amount &#x3D; official_discount_amount + erase_amount + consume_amount
        :type official_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param official_discount_amount: 折扣金额。单位：元。
        :type official_discount_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param erase_amount: 抹零金额。单位：元。
        :type erase_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param consume_amount: 应付金额，包括现金券和储值卡和代金券金额。单位：元。  说明： consume_amount的值等于cash_amount，credit_amount，coupon_amount，flexipurchase_coupon_amount，stored_value_card_amount，bonus_amount，debt_amount，writeoff_amount的总和。
        :type consume_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param cash_amount: 现金支付金额。单位：元.
        :type cash_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param credit_amount: 信用额度支付金额。单位：元。
        :type credit_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param coupon_amount: 代金券支付金额。单位：元。
        :type coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param flexipurchase_coupon_amount: 现金券支付金额。单位：元。
        :type flexipurchase_coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param stored_value_card_amount: 储值卡支付金额。单位：元。
        :type stored_value_card_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param bonus_amount: 奖励金支付金额（奖励金已经下线，目前用于现网客户未使用完的奖励金）。单位：元。
        :type bonus_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param debt_amount: 欠费金额。单位：元。  说明： 对于月结客户，欠费金额即页面上的月度结算金额。
        :type debt_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param writeoff_amount: 欠费核销金额。单位：元。
        :type writeoff_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param region_name: 云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。
        :type region_name: str
        """
        
        

        self._bill_cycle = None
        self._customer_id = None
        self._service_type_code = None
        self._resource_type_code = None
        self._service_type_name = None
        self._resource_type_name = None
        self._region_code = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._charging_mode = None
        self._consume_time = None
        self._trade_time = None
        self._provider_type = None
        self._trade_id = None
        self._id = None
        self._bill_type = None
        self._status = None
        self._official_amount = None
        self._official_discount_amount = None
        self._erase_amount = None
        self._consume_amount = None
        self._cash_amount = None
        self._credit_amount = None
        self._coupon_amount = None
        self._flexipurchase_coupon_amount = None
        self._stored_value_card_amount = None
        self._bonus_amount = None
        self._debt_amount = None
        self._writeoff_amount = None
        self._region_name = None
        self.discriminator = None

        if bill_cycle is not None:
            self.bill_cycle = bill_cycle
        if customer_id is not None:
            self.customer_id = customer_id
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if service_type_name is not None:
            self.service_type_name = service_type_name
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if region_code is not None:
            self.region_code = region_code
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if consume_time is not None:
            self.consume_time = consume_time
        if trade_time is not None:
            self.trade_time = trade_time
        if provider_type is not None:
            self.provider_type = provider_type
        if trade_id is not None:
            self.trade_id = trade_id
        if id is not None:
            self.id = id
        if bill_type is not None:
            self.bill_type = bill_type
        if status is not None:
            self.status = status
        if official_amount is not None:
            self.official_amount = official_amount
        if official_discount_amount is not None:
            self.official_discount_amount = official_discount_amount
        if erase_amount is not None:
            self.erase_amount = erase_amount
        if consume_amount is not None:
            self.consume_amount = consume_amount
        if cash_amount is not None:
            self.cash_amount = cash_amount
        if credit_amount is not None:
            self.credit_amount = credit_amount
        if coupon_amount is not None:
            self.coupon_amount = coupon_amount
        if flexipurchase_coupon_amount is not None:
            self.flexipurchase_coupon_amount = flexipurchase_coupon_amount
        if stored_value_card_amount is not None:
            self.stored_value_card_amount = stored_value_card_amount
        if bonus_amount is not None:
            self.bonus_amount = bonus_amount
        if debt_amount is not None:
            self.debt_amount = debt_amount
        if writeoff_amount is not None:
            self.writeoff_amount = writeoff_amount
        if region_name is not None:
            self.region_name = region_name

    @property
    def bill_cycle(self):
        r"""Gets the bill_cycle of this MonthlyBillRecord.

        流水账单所在账期，东八区时间，格式为YYYY-MM。

        :return: The bill_cycle of this MonthlyBillRecord.
        :rtype: str
        """
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, bill_cycle):
        r"""Sets the bill_cycle of this MonthlyBillRecord.

        流水账单所在账期，东八区时间，格式为YYYY-MM。

        :param bill_cycle: The bill_cycle of this MonthlyBillRecord.
        :type bill_cycle: str
        """
        self._bill_cycle = bill_cycle

    @property
    def customer_id(self):
        r"""Gets the customer_id of this MonthlyBillRecord.

        消费的客户账号ID。 如果是普通客户或者企业子客户查询消费记录，只能查询到客户自己的消费记录，且此处显示的是客户自己的客户ID。如果是企业主查询消费记录，可以查询到企业主以及企业子客户的消费记录，此处为消费的实际客户ID。如果是企业主自己的消费记录，则为企业主ID；如果是某个企业子客户的消费记录，则此处为企业子账号ID。

        :return: The customer_id of this MonthlyBillRecord.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this MonthlyBillRecord.

        消费的客户账号ID。 如果是普通客户或者企业子客户查询消费记录，只能查询到客户自己的消费记录，且此处显示的是客户自己的客户ID。如果是企业主查询消费记录，可以查询到企业主以及企业子客户的消费记录，此处为消费的实际客户ID。如果是企业主自己的消费记录，则为企业主ID；如果是某个企业子客户的消费记录，则此处为企业子账号ID。

        :param customer_id: The customer_id of this MonthlyBillRecord.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def service_type_code(self):
        r"""Gets the service_type_code of this MonthlyBillRecord.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :return: The service_type_code of this MonthlyBillRecord.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        r"""Sets the service_type_code of this MonthlyBillRecord.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :param service_type_code: The service_type_code of this MonthlyBillRecord.
        :type service_type_code: str
        """
        self._service_type_code = service_type_code

    @property
    def resource_type_code(self):
        r"""Gets the resource_type_code of this MonthlyBillRecord.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :return: The resource_type_code of this MonthlyBillRecord.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        r"""Sets the resource_type_code of this MonthlyBillRecord.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :param resource_type_code: The resource_type_code of this MonthlyBillRecord.
        :type resource_type_code: str
        """
        self._resource_type_code = resource_type_code

    @property
    def service_type_name(self):
        r"""Gets the service_type_name of this MonthlyBillRecord.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :return: The service_type_name of this MonthlyBillRecord.
        :rtype: str
        """
        return self._service_type_name

    @service_type_name.setter
    def service_type_name(self, service_type_name):
        r"""Sets the service_type_name of this MonthlyBillRecord.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :param service_type_name: The service_type_name of this MonthlyBillRecord.
        :type service_type_name: str
        """
        self._service_type_name = service_type_name

    @property
    def resource_type_name(self):
        r"""Gets the resource_type_name of this MonthlyBillRecord.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :return: The resource_type_name of this MonthlyBillRecord.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        r"""Sets the resource_type_name of this MonthlyBillRecord.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :param resource_type_name: The resource_type_name of this MonthlyBillRecord.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def region_code(self):
        r"""Gets the region_code of this MonthlyBillRecord.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :return: The region_code of this MonthlyBillRecord.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        r"""Sets the region_code of this MonthlyBillRecord.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :param region_code: The region_code of this MonthlyBillRecord.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this MonthlyBillRecord.

        企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :return: The enterprise_project_id of this MonthlyBillRecord.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this MonthlyBillRecord.

        企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :param enterprise_project_id: The enterprise_project_id of this MonthlyBillRecord.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this MonthlyBillRecord.

        企业项目的名称。

        :return: The enterprise_project_name of this MonthlyBillRecord.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this MonthlyBillRecord.

        企业项目的名称。

        :param enterprise_project_name: The enterprise_project_name of this MonthlyBillRecord.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this MonthlyBillRecord.

        计费模式。 1：包年/包月3：按需10：预留实例11：节省计划

        :return: The charging_mode of this MonthlyBillRecord.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this MonthlyBillRecord.

        计费模式。 1：包年/包月3：按需10：预留实例11：节省计划

        :param charging_mode: The charging_mode of this MonthlyBillRecord.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def consume_time(self):
        r"""Gets the consume_time of this MonthlyBillRecord.

        消费时间。 计费模式为包年/包月和预留实例场景时为订单的支付时间。计费模式为按需场景时为话单的生/失效时间。

        :return: The consume_time of this MonthlyBillRecord.
        :rtype: str
        """
        return self._consume_time

    @consume_time.setter
    def consume_time(self, consume_time):
        r"""Sets the consume_time of this MonthlyBillRecord.

        消费时间。 计费模式为包年/包月和预留实例场景时为订单的支付时间。计费模式为按需场景时为话单的生/失效时间。

        :param consume_time: The consume_time of this MonthlyBillRecord.
        :type consume_time: str
        """
        self._consume_time = consume_time

    @property
    def trade_time(self):
        r"""Gets the trade_time of this MonthlyBillRecord.

        交易时间，某条消费记录对应的扣费时间。

        :return: The trade_time of this MonthlyBillRecord.
        :rtype: str
        """
        return self._trade_time

    @trade_time.setter
    def trade_time(self, trade_time):
        r"""Sets the trade_time of this MonthlyBillRecord.

        交易时间，某条消费记录对应的扣费时间。

        :param trade_time: The trade_time of this MonthlyBillRecord.
        :type trade_time: str
        """
        self._trade_time = trade_time

    @property
    def provider_type(self):
        r"""Gets the provider_type of this MonthlyBillRecord.

        服务商。 1：华为云2：云商店

        :return: The provider_type of this MonthlyBillRecord.
        :rtype: int
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        r"""Sets the provider_type of this MonthlyBillRecord.

        服务商。 1：华为云2：云商店

        :param provider_type: The provider_type of this MonthlyBillRecord.
        :type provider_type: int
        """
        self._provider_type = provider_type

    @property
    def trade_id(self):
        r"""Gets the trade_id of this MonthlyBillRecord.

        订单ID或交易ID，扣费维度的唯一标识。

        :return: The trade_id of this MonthlyBillRecord.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        r"""Sets the trade_id of this MonthlyBillRecord.

        订单ID或交易ID，扣费维度的唯一标识。

        :param trade_id: The trade_id of this MonthlyBillRecord.
        :type trade_id: str
        """
        self._trade_id = trade_id

    @property
    def id(self):
        r"""Gets the id of this MonthlyBillRecord.

        唯一标识。 该字段为预留字段。

        :return: The id of this MonthlyBillRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MonthlyBillRecord.

        唯一标识。 该字段为预留字段。

        :param id: The id of this MonthlyBillRecord.
        :type id: str
        """
        self._id = id

    @property
    def bill_type(self):
        r"""Gets the bill_type of this MonthlyBillRecord.

        账单类型。1：消费-新购 2：消费-续订 3：消费-变更 4：退款-退订 5：消费-使用 8：消费-自动续订 9：调账-补偿 14：消费-服务支持计划月末扣费 16：调账-扣费 18：消费-按月付费 20：退款-变更 23：消费-节省计划抵扣 24：退款-包年/包月转按需 25：消费-抹零补扣 103：消费-按年付费

        :return: The bill_type of this MonthlyBillRecord.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        r"""Sets the bill_type of this MonthlyBillRecord.

        账单类型。1：消费-新购 2：消费-续订 3：消费-变更 4：退款-退订 5：消费-使用 8：消费-自动续订 9：调账-补偿 14：消费-服务支持计划月末扣费 16：调账-扣费 18：消费-按月付费 20：退款-变更 23：消费-节省计划抵扣 24：退款-包年/包月转按需 25：消费-抹零补扣 103：消费-按年付费

        :param bill_type: The bill_type of this MonthlyBillRecord.
        :type bill_type: int
        """
        self._bill_type = bill_type

    @property
    def status(self):
        r"""Gets the status of this MonthlyBillRecord.

        支付状态。 1：已支付2：未结清3：未结算

        :return: The status of this MonthlyBillRecord.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this MonthlyBillRecord.

        支付状态。 1：已支付2：未结清3：未结算

        :param status: The status of this MonthlyBillRecord.
        :type status: int
        """
        self._status = status

    @property
    def official_amount(self):
        r"""Gets the official_amount of this MonthlyBillRecord.

        官网价。单位：元。  说明： official_amount = official_discount_amount + erase_amount + consume_amount

        :return: The official_amount of this MonthlyBillRecord.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._official_amount

    @official_amount.setter
    def official_amount(self, official_amount):
        r"""Sets the official_amount of this MonthlyBillRecord.

        官网价。单位：元。  说明： official_amount = official_discount_amount + erase_amount + consume_amount

        :param official_amount: The official_amount of this MonthlyBillRecord.
        :type official_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._official_amount = official_amount

    @property
    def official_discount_amount(self):
        r"""Gets the official_discount_amount of this MonthlyBillRecord.

        折扣金额。单位：元。

        :return: The official_discount_amount of this MonthlyBillRecord.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._official_discount_amount

    @official_discount_amount.setter
    def official_discount_amount(self, official_discount_amount):
        r"""Sets the official_discount_amount of this MonthlyBillRecord.

        折扣金额。单位：元。

        :param official_discount_amount: The official_discount_amount of this MonthlyBillRecord.
        :type official_discount_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._official_discount_amount = official_discount_amount

    @property
    def erase_amount(self):
        r"""Gets the erase_amount of this MonthlyBillRecord.

        抹零金额。单位：元。

        :return: The erase_amount of this MonthlyBillRecord.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._erase_amount

    @erase_amount.setter
    def erase_amount(self, erase_amount):
        r"""Sets the erase_amount of this MonthlyBillRecord.

        抹零金额。单位：元。

        :param erase_amount: The erase_amount of this MonthlyBillRecord.
        :type erase_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._erase_amount = erase_amount

    @property
    def consume_amount(self):
        r"""Gets the consume_amount of this MonthlyBillRecord.

        应付金额，包括现金券和储值卡和代金券金额。单位：元。  说明： consume_amount的值等于cash_amount，credit_amount，coupon_amount，flexipurchase_coupon_amount，stored_value_card_amount，bonus_amount，debt_amount，writeoff_amount的总和。

        :return: The consume_amount of this MonthlyBillRecord.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._consume_amount

    @consume_amount.setter
    def consume_amount(self, consume_amount):
        r"""Sets the consume_amount of this MonthlyBillRecord.

        应付金额，包括现金券和储值卡和代金券金额。单位：元。  说明： consume_amount的值等于cash_amount，credit_amount，coupon_amount，flexipurchase_coupon_amount，stored_value_card_amount，bonus_amount，debt_amount，writeoff_amount的总和。

        :param consume_amount: The consume_amount of this MonthlyBillRecord.
        :type consume_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._consume_amount = consume_amount

    @property
    def cash_amount(self):
        r"""Gets the cash_amount of this MonthlyBillRecord.

        现金支付金额。单位：元.

        :return: The cash_amount of this MonthlyBillRecord.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._cash_amount

    @cash_amount.setter
    def cash_amount(self, cash_amount):
        r"""Sets the cash_amount of this MonthlyBillRecord.

        现金支付金额。单位：元.

        :param cash_amount: The cash_amount of this MonthlyBillRecord.
        :type cash_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._cash_amount = cash_amount

    @property
    def credit_amount(self):
        r"""Gets the credit_amount of this MonthlyBillRecord.

        信用额度支付金额。单位：元。

        :return: The credit_amount of this MonthlyBillRecord.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        r"""Sets the credit_amount of this MonthlyBillRecord.

        信用额度支付金额。单位：元。

        :param credit_amount: The credit_amount of this MonthlyBillRecord.
        :type credit_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._credit_amount = credit_amount

    @property
    def coupon_amount(self):
        r"""Gets the coupon_amount of this MonthlyBillRecord.

        代金券支付金额。单位：元。

        :return: The coupon_amount of this MonthlyBillRecord.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, coupon_amount):
        r"""Sets the coupon_amount of this MonthlyBillRecord.

        代金券支付金额。单位：元。

        :param coupon_amount: The coupon_amount of this MonthlyBillRecord.
        :type coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._coupon_amount = coupon_amount

    @property
    def flexipurchase_coupon_amount(self):
        r"""Gets the flexipurchase_coupon_amount of this MonthlyBillRecord.

        现金券支付金额。单位：元。

        :return: The flexipurchase_coupon_amount of this MonthlyBillRecord.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._flexipurchase_coupon_amount

    @flexipurchase_coupon_amount.setter
    def flexipurchase_coupon_amount(self, flexipurchase_coupon_amount):
        r"""Sets the flexipurchase_coupon_amount of this MonthlyBillRecord.

        现金券支付金额。单位：元。

        :param flexipurchase_coupon_amount: The flexipurchase_coupon_amount of this MonthlyBillRecord.
        :type flexipurchase_coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._flexipurchase_coupon_amount = flexipurchase_coupon_amount

    @property
    def stored_value_card_amount(self):
        r"""Gets the stored_value_card_amount of this MonthlyBillRecord.

        储值卡支付金额。单位：元。

        :return: The stored_value_card_amount of this MonthlyBillRecord.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._stored_value_card_amount

    @stored_value_card_amount.setter
    def stored_value_card_amount(self, stored_value_card_amount):
        r"""Sets the stored_value_card_amount of this MonthlyBillRecord.

        储值卡支付金额。单位：元。

        :param stored_value_card_amount: The stored_value_card_amount of this MonthlyBillRecord.
        :type stored_value_card_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._stored_value_card_amount = stored_value_card_amount

    @property
    def bonus_amount(self):
        r"""Gets the bonus_amount of this MonthlyBillRecord.

        奖励金支付金额（奖励金已经下线，目前用于现网客户未使用完的奖励金）。单位：元。

        :return: The bonus_amount of this MonthlyBillRecord.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._bonus_amount

    @bonus_amount.setter
    def bonus_amount(self, bonus_amount):
        r"""Sets the bonus_amount of this MonthlyBillRecord.

        奖励金支付金额（奖励金已经下线，目前用于现网客户未使用完的奖励金）。单位：元。

        :param bonus_amount: The bonus_amount of this MonthlyBillRecord.
        :type bonus_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._bonus_amount = bonus_amount

    @property
    def debt_amount(self):
        r"""Gets the debt_amount of this MonthlyBillRecord.

        欠费金额。单位：元。  说明： 对于月结客户，欠费金额即页面上的月度结算金额。

        :return: The debt_amount of this MonthlyBillRecord.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._debt_amount

    @debt_amount.setter
    def debt_amount(self, debt_amount):
        r"""Sets the debt_amount of this MonthlyBillRecord.

        欠费金额。单位：元。  说明： 对于月结客户，欠费金额即页面上的月度结算金额。

        :param debt_amount: The debt_amount of this MonthlyBillRecord.
        :type debt_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._debt_amount = debt_amount

    @property
    def writeoff_amount(self):
        r"""Gets the writeoff_amount of this MonthlyBillRecord.

        欠费核销金额。单位：元。

        :return: The writeoff_amount of this MonthlyBillRecord.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._writeoff_amount

    @writeoff_amount.setter
    def writeoff_amount(self, writeoff_amount):
        r"""Sets the writeoff_amount of this MonthlyBillRecord.

        欠费核销金额。单位：元。

        :param writeoff_amount: The writeoff_amount of this MonthlyBillRecord.
        :type writeoff_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._writeoff_amount = writeoff_amount

    @property
    def region_name(self):
        r"""Gets the region_name of this MonthlyBillRecord.

        云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。

        :return: The region_name of this MonthlyBillRecord.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this MonthlyBillRecord.

        云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。

        :param region_name: The region_name of this MonthlyBillRecord.
        :type region_name: str
        """
        self._region_name = region_name

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
        if not isinstance(other, MonthlyBillRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
