# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NvlCostAnalysedBillDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'shared_month': 'str',
        'bill_cycle': 'str',
        'bill_type': 'int',
        'customer_id': 'str',
        'region_code': 'str',
        'region_name': 'str',
        'service_type_code': 'str',
        'resource_type_code': 'str',
        'service_type_name': 'str',
        'resource_type_name': 'str',
        'effective_time': 'str',
        'expire_time': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_tag': 'str',
        'product_spec_desc': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'charging_mode': 'int',
        'order_id': 'str',
        'period_type': 'int',
        'usage_type': 'str',
        'usage': 'decimal.Decimal',
        'usage_measure_id': 'int',
        'free_resource_usage': 'decimal.Decimal',
        'free_resource_measure_id': 'int',
        'ri_usage': 'decimal.Decimal',
        'ri_usage_measure_id': 'int',
        'consume_amount': 'decimal.Decimal',
        'past_months_amortized_amount': 'decimal.Decimal',
        'current_month_amortized_amount': 'decimal.Decimal',
        'future_months_amortized_amount': 'decimal.Decimal',
        'amortized_cash_amount': 'decimal.Decimal',
        'amortized_credit_amount': 'decimal.Decimal',
        'amortized_coupon_amount': 'decimal.Decimal',
        'amortized_flexipurchase_coupon_amount': 'decimal.Decimal',
        'amortized_stored_value_card_amount': 'decimal.Decimal',
        'amortized_bonus_amount': 'decimal.Decimal',
        'sub_service_type_code': 'str',
        'sub_service_type_name': 'str',
        'sub_resource_type_code': 'str',
        'sub_resource_type_name': 'str',
        'sub_resource_id': 'str',
        'sub_resource_name': 'str',
        'effective_tag_pairs': 'list[TagPair]',
        'cost_unit_pairs': 'list[CostUnitPair]'
    }

    attribute_map = {
        'shared_month': 'shared_month',
        'bill_cycle': 'bill_cycle',
        'bill_type': 'bill_type',
        'customer_id': 'customer_id',
        'region_code': 'region_code',
        'region_name': 'region_name',
        'service_type_code': 'service_type_code',
        'resource_type_code': 'resource_type_code',
        'service_type_name': 'service_type_name',
        'resource_type_name': 'resource_type_name',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_tag': 'resource_tag',
        'product_spec_desc': 'product_spec_desc',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'charging_mode': 'charging_mode',
        'order_id': 'order_id',
        'period_type': 'period_type',
        'usage_type': 'usage_type',
        'usage': 'usage',
        'usage_measure_id': 'usage_measure_id',
        'free_resource_usage': 'free_resource_usage',
        'free_resource_measure_id': 'free_resource_measure_id',
        'ri_usage': 'ri_usage',
        'ri_usage_measure_id': 'ri_usage_measure_id',
        'consume_amount': 'consume_amount',
        'past_months_amortized_amount': 'past_months_amortized_amount',
        'current_month_amortized_amount': 'current_month_amortized_amount',
        'future_months_amortized_amount': 'future_months_amortized_amount',
        'amortized_cash_amount': 'amortized_cash_amount',
        'amortized_credit_amount': 'amortized_credit_amount',
        'amortized_coupon_amount': 'amortized_coupon_amount',
        'amortized_flexipurchase_coupon_amount': 'amortized_flexipurchase_coupon_amount',
        'amortized_stored_value_card_amount': 'amortized_stored_value_card_amount',
        'amortized_bonus_amount': 'amortized_bonus_amount',
        'sub_service_type_code': 'sub_service_type_code',
        'sub_service_type_name': 'sub_service_type_name',
        'sub_resource_type_code': 'sub_resource_type_code',
        'sub_resource_type_name': 'sub_resource_type_name',
        'sub_resource_id': 'sub_resource_id',
        'sub_resource_name': 'sub_resource_name',
        'effective_tag_pairs': 'effective_tag_pairs',
        'cost_unit_pairs': 'cost_unit_pairs'
    }

    def __init__(self, shared_month=None, bill_cycle=None, bill_type=None, customer_id=None, region_code=None, region_name=None, service_type_code=None, resource_type_code=None, service_type_name=None, resource_type_name=None, effective_time=None, expire_time=None, resource_id=None, resource_name=None, resource_tag=None, product_spec_desc=None, enterprise_project_id=None, enterprise_project_name=None, charging_mode=None, order_id=None, period_type=None, usage_type=None, usage=None, usage_measure_id=None, free_resource_usage=None, free_resource_measure_id=None, ri_usage=None, ri_usage_measure_id=None, consume_amount=None, past_months_amortized_amount=None, current_month_amortized_amount=None, future_months_amortized_amount=None, amortized_cash_amount=None, amortized_credit_amount=None, amortized_coupon_amount=None, amortized_flexipurchase_coupon_amount=None, amortized_stored_value_card_amount=None, amortized_bonus_amount=None, sub_service_type_code=None, sub_service_type_name=None, sub_resource_type_code=None, sub_resource_type_name=None, sub_resource_id=None, sub_resource_name=None, effective_tag_pairs=None, cost_unit_pairs=None):
        """NvlCostAnalysedBillDetail

        The model defined in huaweicloud sdk

        :param shared_month: 查询分摊成本的月份。 格式为YYYY-MM，按照东八区时间截取。
        :type shared_month: str
        :param bill_cycle: 账期。 格式：YYYY-MM。按照东八区时间截取。
        :type bill_cycle: str
        :param bill_type: 账单类型。 1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费16：调账-扣费18：消费-按月付费20：退款-变更23：消费-节省计划抵扣24：退款-包年/包月转按需
        :type bill_type: int
        :param customer_id: 消费的客户账号ID。 如果是普通客户或者企业子查询消费记录，只能查询到自身的消费记录，则这个地方显示的是自身的客户ID。如果是企业主查询消费记录，可以查询到自身以及企业子的消费记录，这个地方是消费的实际客户ID，如果是企业主自身消费，为企业主ID，如果这条消费记录是某个企业子客户的消费，这个地方的ID是企业子账号ID。
        :type customer_id: str
        :param region_code: 云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。
        :type region_code: str
        :param region_name: 云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。
        :type region_name: str
        :param service_type_code: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。
        :type service_type_code: str
        :param resource_type_code: 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。
        :type resource_type_code: str
        :param service_type_name: 云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。
        :type service_type_name: str
        :param resource_type_name: 资源类型名称。例如ECS的资源类型名称为“云主机”。
        :type resource_type_name: str
        :param effective_time: 费用对应的资源使用的开始时间，按需有效，包年/包月该字段保留。
        :type effective_time: str
        :param expire_time: 费用对应的资源使用的结束时间，按需有效，包年/包月该字段保留。
        :type expire_time: str
        :param resource_id: 资源ID。
        :type resource_id: str
        :param resource_name: 资源名称。
        :type resource_name: str
        :param resource_tag: 资源标签。
        :type resource_tag: str
        :param product_spec_desc: 产品的规格描述。
        :type product_spec_desc: str
        :param enterprise_project_id: 企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业项目的名称。
        :type enterprise_project_name: str
        :param charging_mode: 计费模式。 1：包年/包月3：按需10：预留实例11：节省计划
        :type charging_mode: int
        :param order_id: 订单ID。  说明： 包年/包月资源的使用记录才有该字段，按需资源则为空。
        :type order_id: str
        :param period_type: 周期类型。 19：年20：月24：天25：小时5：一次性
        :type period_type: int
        :param usage_type: 资源使用量的类型，您可以调用查询使用量类型列表接口获取。
        :type usage_type: str
        :param usage: 资源的使用量。
        :type usage: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param usage_measure_id: 资源使用量的度量单位，您可以调用查询度量单位列表接口获取。
        :type usage_measure_id: int
        :param free_resource_usage: 套餐内使用量。
        :type free_resource_usage: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param free_resource_measure_id: 套餐内使用量的度量单位，您可以调用查询度量单位列表接口获取。
        :type free_resource_measure_id: int
        :param ri_usage: 预留实例使用量。
        :type ri_usage: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param ri_usage_measure_id: 预留实例使用量单位。
        :type ri_usage_measure_id: int
        :param consume_amount: 消费金额（应付金额）。 消费金额&#x3D;期初已分摊金额+当月分摊金额+期末未分摊金额
        :type consume_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param past_months_amortized_amount: 期初已分摊金额。  说明： 包周期和预留实例预付时有效；计费类型为按需，预留实例为按时计费时该值为0。
        :type past_months_amortized_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param current_month_amortized_amount: 当月分摊金额。 当月分摊金额&#x3D;现金分摊金额+信用额度分摊金额+代金券分摊金额+现金券分摊金额+储值卡分摊金额+奖励金分摊金额
        :type current_month_amortized_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param future_months_amortized_amount: 期末未分摊金额。月度成本分摊时，当月以后还未分摊的金额。  说明： 包周期和预留实例预付时有效；计费类型为按需，预留实例为按时计费时该值为0。
        :type future_months_amortized_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param amortized_cash_amount: 月度成本分摊时，当月已分摊金额中包含的现金金额。
        :type amortized_cash_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param amortized_credit_amount: 月度成本分摊时，当月已分摊金额中包含的信用额度分摊金额。
        :type amortized_credit_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param amortized_coupon_amount: 月度成本分摊时，当月已分摊金额中包含的代金券分摊金额。
        :type amortized_coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param amortized_flexipurchase_coupon_amount: 月度成本分摊时，当月已分摊金额中包含的现金券分摊金额。
        :type amortized_flexipurchase_coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param amortized_stored_value_card_amount: 月度成本分摊时，当月已分摊金额中包含的储值卡分摊金额。
        :type amortized_stored_value_card_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param amortized_bonus_amount: 月度成本分摊时，当月已分摊金额中包含的奖励金分摊金额（用于现网未清干净的奖励金）。
        :type amortized_bonus_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param sub_service_type_code: 整机的子云服务的自身的云服务类型编码。
        :type sub_service_type_code: str
        :param sub_service_type_name: 整机的子云服务的自身的云服务类型名称。
        :type sub_service_type_name: str
        :param sub_resource_type_code: 整机的子云服务的自身的资源类型编码。
        :type sub_resource_type_code: str
        :param sub_resource_type_name: 整机的子云服务的自身的资源类型名称。
        :type sub_resource_type_name: str
        :param sub_resource_id: 整机的子云服务的自身的资源ID，资源标识。（如果为预留实例，则为预留实例标识）
        :type sub_resource_id: str
        :param sub_resource_name: 整机的子云服务的自身的资源名称，资源标识。（如果为预留实例，则为预留实例标识）
        :type sub_resource_name: str
        :param effective_tag_pairs: 成本标签。
        :type effective_tag_pairs: list[:class:`huaweicloudsdkbss.v2.TagPair`]
        :param cost_unit_pairs: 成本单元。
        :type cost_unit_pairs: list[:class:`huaweicloudsdkbss.v2.CostUnitPair`]
        """
        
        

        self._shared_month = None
        self._bill_cycle = None
        self._bill_type = None
        self._customer_id = None
        self._region_code = None
        self._region_name = None
        self._service_type_code = None
        self._resource_type_code = None
        self._service_type_name = None
        self._resource_type_name = None
        self._effective_time = None
        self._expire_time = None
        self._resource_id = None
        self._resource_name = None
        self._resource_tag = None
        self._product_spec_desc = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._charging_mode = None
        self._order_id = None
        self._period_type = None
        self._usage_type = None
        self._usage = None
        self._usage_measure_id = None
        self._free_resource_usage = None
        self._free_resource_measure_id = None
        self._ri_usage = None
        self._ri_usage_measure_id = None
        self._consume_amount = None
        self._past_months_amortized_amount = None
        self._current_month_amortized_amount = None
        self._future_months_amortized_amount = None
        self._amortized_cash_amount = None
        self._amortized_credit_amount = None
        self._amortized_coupon_amount = None
        self._amortized_flexipurchase_coupon_amount = None
        self._amortized_stored_value_card_amount = None
        self._amortized_bonus_amount = None
        self._sub_service_type_code = None
        self._sub_service_type_name = None
        self._sub_resource_type_code = None
        self._sub_resource_type_name = None
        self._sub_resource_id = None
        self._sub_resource_name = None
        self._effective_tag_pairs = None
        self._cost_unit_pairs = None
        self.discriminator = None

        if shared_month is not None:
            self.shared_month = shared_month
        if bill_cycle is not None:
            self.bill_cycle = bill_cycle
        if bill_type is not None:
            self.bill_type = bill_type
        if customer_id is not None:
            self.customer_id = customer_id
        if region_code is not None:
            self.region_code = region_code
        if region_name is not None:
            self.region_name = region_name
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if service_type_name is not None:
            self.service_type_name = service_type_name
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_tag is not None:
            self.resource_tag = resource_tag
        if product_spec_desc is not None:
            self.product_spec_desc = product_spec_desc
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if order_id is not None:
            self.order_id = order_id
        if period_type is not None:
            self.period_type = period_type
        if usage_type is not None:
            self.usage_type = usage_type
        if usage is not None:
            self.usage = usage
        if usage_measure_id is not None:
            self.usage_measure_id = usage_measure_id
        if free_resource_usage is not None:
            self.free_resource_usage = free_resource_usage
        if free_resource_measure_id is not None:
            self.free_resource_measure_id = free_resource_measure_id
        if ri_usage is not None:
            self.ri_usage = ri_usage
        if ri_usage_measure_id is not None:
            self.ri_usage_measure_id = ri_usage_measure_id
        if consume_amount is not None:
            self.consume_amount = consume_amount
        if past_months_amortized_amount is not None:
            self.past_months_amortized_amount = past_months_amortized_amount
        if current_month_amortized_amount is not None:
            self.current_month_amortized_amount = current_month_amortized_amount
        if future_months_amortized_amount is not None:
            self.future_months_amortized_amount = future_months_amortized_amount
        if amortized_cash_amount is not None:
            self.amortized_cash_amount = amortized_cash_amount
        if amortized_credit_amount is not None:
            self.amortized_credit_amount = amortized_credit_amount
        if amortized_coupon_amount is not None:
            self.amortized_coupon_amount = amortized_coupon_amount
        if amortized_flexipurchase_coupon_amount is not None:
            self.amortized_flexipurchase_coupon_amount = amortized_flexipurchase_coupon_amount
        if amortized_stored_value_card_amount is not None:
            self.amortized_stored_value_card_amount = amortized_stored_value_card_amount
        if amortized_bonus_amount is not None:
            self.amortized_bonus_amount = amortized_bonus_amount
        if sub_service_type_code is not None:
            self.sub_service_type_code = sub_service_type_code
        if sub_service_type_name is not None:
            self.sub_service_type_name = sub_service_type_name
        if sub_resource_type_code is not None:
            self.sub_resource_type_code = sub_resource_type_code
        if sub_resource_type_name is not None:
            self.sub_resource_type_name = sub_resource_type_name
        if sub_resource_id is not None:
            self.sub_resource_id = sub_resource_id
        if sub_resource_name is not None:
            self.sub_resource_name = sub_resource_name
        if effective_tag_pairs is not None:
            self.effective_tag_pairs = effective_tag_pairs
        if cost_unit_pairs is not None:
            self.cost_unit_pairs = cost_unit_pairs

    @property
    def shared_month(self):
        """Gets the shared_month of this NvlCostAnalysedBillDetail.

        查询分摊成本的月份。 格式为YYYY-MM，按照东八区时间截取。

        :return: The shared_month of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._shared_month

    @shared_month.setter
    def shared_month(self, shared_month):
        """Sets the shared_month of this NvlCostAnalysedBillDetail.

        查询分摊成本的月份。 格式为YYYY-MM，按照东八区时间截取。

        :param shared_month: The shared_month of this NvlCostAnalysedBillDetail.
        :type shared_month: str
        """
        self._shared_month = shared_month

    @property
    def bill_cycle(self):
        """Gets the bill_cycle of this NvlCostAnalysedBillDetail.

        账期。 格式：YYYY-MM。按照东八区时间截取。

        :return: The bill_cycle of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, bill_cycle):
        """Sets the bill_cycle of this NvlCostAnalysedBillDetail.

        账期。 格式：YYYY-MM。按照东八区时间截取。

        :param bill_cycle: The bill_cycle of this NvlCostAnalysedBillDetail.
        :type bill_cycle: str
        """
        self._bill_cycle = bill_cycle

    @property
    def bill_type(self):
        """Gets the bill_type of this NvlCostAnalysedBillDetail.

        账单类型。 1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费16：调账-扣费18：消费-按月付费20：退款-变更23：消费-节省计划抵扣24：退款-包年/包月转按需

        :return: The bill_type of this NvlCostAnalysedBillDetail.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this NvlCostAnalysedBillDetail.

        账单类型。 1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费16：调账-扣费18：消费-按月付费20：退款-变更23：消费-节省计划抵扣24：退款-包年/包月转按需

        :param bill_type: The bill_type of this NvlCostAnalysedBillDetail.
        :type bill_type: int
        """
        self._bill_type = bill_type

    @property
    def customer_id(self):
        """Gets the customer_id of this NvlCostAnalysedBillDetail.

        消费的客户账号ID。 如果是普通客户或者企业子查询消费记录，只能查询到自身的消费记录，则这个地方显示的是自身的客户ID。如果是企业主查询消费记录，可以查询到自身以及企业子的消费记录，这个地方是消费的实际客户ID，如果是企业主自身消费，为企业主ID，如果这条消费记录是某个企业子客户的消费，这个地方的ID是企业子账号ID。

        :return: The customer_id of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this NvlCostAnalysedBillDetail.

        消费的客户账号ID。 如果是普通客户或者企业子查询消费记录，只能查询到自身的消费记录，则这个地方显示的是自身的客户ID。如果是企业主查询消费记录，可以查询到自身以及企业子的消费记录，这个地方是消费的实际客户ID，如果是企业主自身消费，为企业主ID，如果这条消费记录是某个企业子客户的消费，这个地方的ID是企业子账号ID。

        :param customer_id: The customer_id of this NvlCostAnalysedBillDetail.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def region_code(self):
        """Gets the region_code of this NvlCostAnalysedBillDetail.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :return: The region_code of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this NvlCostAnalysedBillDetail.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :param region_code: The region_code of this NvlCostAnalysedBillDetail.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def region_name(self):
        """Gets the region_name of this NvlCostAnalysedBillDetail.

        云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。

        :return: The region_name of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this NvlCostAnalysedBillDetail.

        云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。

        :param region_name: The region_name of this NvlCostAnalysedBillDetail.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def service_type_code(self):
        """Gets the service_type_code of this NvlCostAnalysedBillDetail.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :return: The service_type_code of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this NvlCostAnalysedBillDetail.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :param service_type_code: The service_type_code of this NvlCostAnalysedBillDetail.
        :type service_type_code: str
        """
        self._service_type_code = service_type_code

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this NvlCostAnalysedBillDetail.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :return: The resource_type_code of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this NvlCostAnalysedBillDetail.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :param resource_type_code: The resource_type_code of this NvlCostAnalysedBillDetail.
        :type resource_type_code: str
        """
        self._resource_type_code = resource_type_code

    @property
    def service_type_name(self):
        """Gets the service_type_name of this NvlCostAnalysedBillDetail.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :return: The service_type_name of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._service_type_name

    @service_type_name.setter
    def service_type_name(self, service_type_name):
        """Sets the service_type_name of this NvlCostAnalysedBillDetail.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :param service_type_name: The service_type_name of this NvlCostAnalysedBillDetail.
        :type service_type_name: str
        """
        self._service_type_name = service_type_name

    @property
    def resource_type_name(self):
        """Gets the resource_type_name of this NvlCostAnalysedBillDetail.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :return: The resource_type_name of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        """Sets the resource_type_name of this NvlCostAnalysedBillDetail.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :param resource_type_name: The resource_type_name of this NvlCostAnalysedBillDetail.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def effective_time(self):
        """Gets the effective_time of this NvlCostAnalysedBillDetail.

        费用对应的资源使用的开始时间，按需有效，包年/包月该字段保留。

        :return: The effective_time of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        """Sets the effective_time of this NvlCostAnalysedBillDetail.

        费用对应的资源使用的开始时间，按需有效，包年/包月该字段保留。

        :param effective_time: The effective_time of this NvlCostAnalysedBillDetail.
        :type effective_time: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        """Gets the expire_time of this NvlCostAnalysedBillDetail.

        费用对应的资源使用的结束时间，按需有效，包年/包月该字段保留。

        :return: The expire_time of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this NvlCostAnalysedBillDetail.

        费用对应的资源使用的结束时间，按需有效，包年/包月该字段保留。

        :param expire_time: The expire_time of this NvlCostAnalysedBillDetail.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def resource_id(self):
        """Gets the resource_id of this NvlCostAnalysedBillDetail.

        资源ID。

        :return: The resource_id of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this NvlCostAnalysedBillDetail.

        资源ID。

        :param resource_id: The resource_id of this NvlCostAnalysedBillDetail.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this NvlCostAnalysedBillDetail.

        资源名称。

        :return: The resource_name of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this NvlCostAnalysedBillDetail.

        资源名称。

        :param resource_name: The resource_name of this NvlCostAnalysedBillDetail.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_tag(self):
        """Gets the resource_tag of this NvlCostAnalysedBillDetail.

        资源标签。

        :return: The resource_tag of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._resource_tag

    @resource_tag.setter
    def resource_tag(self, resource_tag):
        """Sets the resource_tag of this NvlCostAnalysedBillDetail.

        资源标签。

        :param resource_tag: The resource_tag of this NvlCostAnalysedBillDetail.
        :type resource_tag: str
        """
        self._resource_tag = resource_tag

    @property
    def product_spec_desc(self):
        """Gets the product_spec_desc of this NvlCostAnalysedBillDetail.

        产品的规格描述。

        :return: The product_spec_desc of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._product_spec_desc

    @product_spec_desc.setter
    def product_spec_desc(self, product_spec_desc):
        """Sets the product_spec_desc of this NvlCostAnalysedBillDetail.

        产品的规格描述。

        :param product_spec_desc: The product_spec_desc of this NvlCostAnalysedBillDetail.
        :type product_spec_desc: str
        """
        self._product_spec_desc = product_spec_desc

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this NvlCostAnalysedBillDetail.

        企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :return: The enterprise_project_id of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this NvlCostAnalysedBillDetail.

        企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :param enterprise_project_id: The enterprise_project_id of this NvlCostAnalysedBillDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        """Gets the enterprise_project_name of this NvlCostAnalysedBillDetail.

        企业项目的名称。

        :return: The enterprise_project_name of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        """Sets the enterprise_project_name of this NvlCostAnalysedBillDetail.

        企业项目的名称。

        :param enterprise_project_name: The enterprise_project_name of this NvlCostAnalysedBillDetail.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def charging_mode(self):
        """Gets the charging_mode of this NvlCostAnalysedBillDetail.

        计费模式。 1：包年/包月3：按需10：预留实例11：节省计划

        :return: The charging_mode of this NvlCostAnalysedBillDetail.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this NvlCostAnalysedBillDetail.

        计费模式。 1：包年/包月3：按需10：预留实例11：节省计划

        :param charging_mode: The charging_mode of this NvlCostAnalysedBillDetail.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def order_id(self):
        """Gets the order_id of this NvlCostAnalysedBillDetail.

        订单ID。  说明： 包年/包月资源的使用记录才有该字段，按需资源则为空。

        :return: The order_id of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this NvlCostAnalysedBillDetail.

        订单ID。  说明： 包年/包月资源的使用记录才有该字段，按需资源则为空。

        :param order_id: The order_id of this NvlCostAnalysedBillDetail.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def period_type(self):
        """Gets the period_type of this NvlCostAnalysedBillDetail.

        周期类型。 19：年20：月24：天25：小时5：一次性

        :return: The period_type of this NvlCostAnalysedBillDetail.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this NvlCostAnalysedBillDetail.

        周期类型。 19：年20：月24：天25：小时5：一次性

        :param period_type: The period_type of this NvlCostAnalysedBillDetail.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def usage_type(self):
        """Gets the usage_type of this NvlCostAnalysedBillDetail.

        资源使用量的类型，您可以调用查询使用量类型列表接口获取。

        :return: The usage_type of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type):
        """Sets the usage_type of this NvlCostAnalysedBillDetail.

        资源使用量的类型，您可以调用查询使用量类型列表接口获取。

        :param usage_type: The usage_type of this NvlCostAnalysedBillDetail.
        :type usage_type: str
        """
        self._usage_type = usage_type

    @property
    def usage(self):
        """Gets the usage of this NvlCostAnalysedBillDetail.

        资源的使用量。

        :return: The usage of this NvlCostAnalysedBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this NvlCostAnalysedBillDetail.

        资源的使用量。

        :param usage: The usage of this NvlCostAnalysedBillDetail.
        :type usage: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._usage = usage

    @property
    def usage_measure_id(self):
        """Gets the usage_measure_id of this NvlCostAnalysedBillDetail.

        资源使用量的度量单位，您可以调用查询度量单位列表接口获取。

        :return: The usage_measure_id of this NvlCostAnalysedBillDetail.
        :rtype: int
        """
        return self._usage_measure_id

    @usage_measure_id.setter
    def usage_measure_id(self, usage_measure_id):
        """Sets the usage_measure_id of this NvlCostAnalysedBillDetail.

        资源使用量的度量单位，您可以调用查询度量单位列表接口获取。

        :param usage_measure_id: The usage_measure_id of this NvlCostAnalysedBillDetail.
        :type usage_measure_id: int
        """
        self._usage_measure_id = usage_measure_id

    @property
    def free_resource_usage(self):
        """Gets the free_resource_usage of this NvlCostAnalysedBillDetail.

        套餐内使用量。

        :return: The free_resource_usage of this NvlCostAnalysedBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._free_resource_usage

    @free_resource_usage.setter
    def free_resource_usage(self, free_resource_usage):
        """Sets the free_resource_usage of this NvlCostAnalysedBillDetail.

        套餐内使用量。

        :param free_resource_usage: The free_resource_usage of this NvlCostAnalysedBillDetail.
        :type free_resource_usage: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._free_resource_usage = free_resource_usage

    @property
    def free_resource_measure_id(self):
        """Gets the free_resource_measure_id of this NvlCostAnalysedBillDetail.

        套餐内使用量的度量单位，您可以调用查询度量单位列表接口获取。

        :return: The free_resource_measure_id of this NvlCostAnalysedBillDetail.
        :rtype: int
        """
        return self._free_resource_measure_id

    @free_resource_measure_id.setter
    def free_resource_measure_id(self, free_resource_measure_id):
        """Sets the free_resource_measure_id of this NvlCostAnalysedBillDetail.

        套餐内使用量的度量单位，您可以调用查询度量单位列表接口获取。

        :param free_resource_measure_id: The free_resource_measure_id of this NvlCostAnalysedBillDetail.
        :type free_resource_measure_id: int
        """
        self._free_resource_measure_id = free_resource_measure_id

    @property
    def ri_usage(self):
        """Gets the ri_usage of this NvlCostAnalysedBillDetail.

        预留实例使用量。

        :return: The ri_usage of this NvlCostAnalysedBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._ri_usage

    @ri_usage.setter
    def ri_usage(self, ri_usage):
        """Sets the ri_usage of this NvlCostAnalysedBillDetail.

        预留实例使用量。

        :param ri_usage: The ri_usage of this NvlCostAnalysedBillDetail.
        :type ri_usage: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._ri_usage = ri_usage

    @property
    def ri_usage_measure_id(self):
        """Gets the ri_usage_measure_id of this NvlCostAnalysedBillDetail.

        预留实例使用量单位。

        :return: The ri_usage_measure_id of this NvlCostAnalysedBillDetail.
        :rtype: int
        """
        return self._ri_usage_measure_id

    @ri_usage_measure_id.setter
    def ri_usage_measure_id(self, ri_usage_measure_id):
        """Sets the ri_usage_measure_id of this NvlCostAnalysedBillDetail.

        预留实例使用量单位。

        :param ri_usage_measure_id: The ri_usage_measure_id of this NvlCostAnalysedBillDetail.
        :type ri_usage_measure_id: int
        """
        self._ri_usage_measure_id = ri_usage_measure_id

    @property
    def consume_amount(self):
        """Gets the consume_amount of this NvlCostAnalysedBillDetail.

        消费金额（应付金额）。 消费金额=期初已分摊金额+当月分摊金额+期末未分摊金额

        :return: The consume_amount of this NvlCostAnalysedBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._consume_amount

    @consume_amount.setter
    def consume_amount(self, consume_amount):
        """Sets the consume_amount of this NvlCostAnalysedBillDetail.

        消费金额（应付金额）。 消费金额=期初已分摊金额+当月分摊金额+期末未分摊金额

        :param consume_amount: The consume_amount of this NvlCostAnalysedBillDetail.
        :type consume_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._consume_amount = consume_amount

    @property
    def past_months_amortized_amount(self):
        """Gets the past_months_amortized_amount of this NvlCostAnalysedBillDetail.

        期初已分摊金额。  说明： 包周期和预留实例预付时有效；计费类型为按需，预留实例为按时计费时该值为0。

        :return: The past_months_amortized_amount of this NvlCostAnalysedBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._past_months_amortized_amount

    @past_months_amortized_amount.setter
    def past_months_amortized_amount(self, past_months_amortized_amount):
        """Sets the past_months_amortized_amount of this NvlCostAnalysedBillDetail.

        期初已分摊金额。  说明： 包周期和预留实例预付时有效；计费类型为按需，预留实例为按时计费时该值为0。

        :param past_months_amortized_amount: The past_months_amortized_amount of this NvlCostAnalysedBillDetail.
        :type past_months_amortized_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._past_months_amortized_amount = past_months_amortized_amount

    @property
    def current_month_amortized_amount(self):
        """Gets the current_month_amortized_amount of this NvlCostAnalysedBillDetail.

        当月分摊金额。 当月分摊金额=现金分摊金额+信用额度分摊金额+代金券分摊金额+现金券分摊金额+储值卡分摊金额+奖励金分摊金额

        :return: The current_month_amortized_amount of this NvlCostAnalysedBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._current_month_amortized_amount

    @current_month_amortized_amount.setter
    def current_month_amortized_amount(self, current_month_amortized_amount):
        """Sets the current_month_amortized_amount of this NvlCostAnalysedBillDetail.

        当月分摊金额。 当月分摊金额=现金分摊金额+信用额度分摊金额+代金券分摊金额+现金券分摊金额+储值卡分摊金额+奖励金分摊金额

        :param current_month_amortized_amount: The current_month_amortized_amount of this NvlCostAnalysedBillDetail.
        :type current_month_amortized_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._current_month_amortized_amount = current_month_amortized_amount

    @property
    def future_months_amortized_amount(self):
        """Gets the future_months_amortized_amount of this NvlCostAnalysedBillDetail.

        期末未分摊金额。月度成本分摊时，当月以后还未分摊的金额。  说明： 包周期和预留实例预付时有效；计费类型为按需，预留实例为按时计费时该值为0。

        :return: The future_months_amortized_amount of this NvlCostAnalysedBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._future_months_amortized_amount

    @future_months_amortized_amount.setter
    def future_months_amortized_amount(self, future_months_amortized_amount):
        """Sets the future_months_amortized_amount of this NvlCostAnalysedBillDetail.

        期末未分摊金额。月度成本分摊时，当月以后还未分摊的金额。  说明： 包周期和预留实例预付时有效；计费类型为按需，预留实例为按时计费时该值为0。

        :param future_months_amortized_amount: The future_months_amortized_amount of this NvlCostAnalysedBillDetail.
        :type future_months_amortized_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._future_months_amortized_amount = future_months_amortized_amount

    @property
    def amortized_cash_amount(self):
        """Gets the amortized_cash_amount of this NvlCostAnalysedBillDetail.

        月度成本分摊时，当月已分摊金额中包含的现金金额。

        :return: The amortized_cash_amount of this NvlCostAnalysedBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._amortized_cash_amount

    @amortized_cash_amount.setter
    def amortized_cash_amount(self, amortized_cash_amount):
        """Sets the amortized_cash_amount of this NvlCostAnalysedBillDetail.

        月度成本分摊时，当月已分摊金额中包含的现金金额。

        :param amortized_cash_amount: The amortized_cash_amount of this NvlCostAnalysedBillDetail.
        :type amortized_cash_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._amortized_cash_amount = amortized_cash_amount

    @property
    def amortized_credit_amount(self):
        """Gets the amortized_credit_amount of this NvlCostAnalysedBillDetail.

        月度成本分摊时，当月已分摊金额中包含的信用额度分摊金额。

        :return: The amortized_credit_amount of this NvlCostAnalysedBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._amortized_credit_amount

    @amortized_credit_amount.setter
    def amortized_credit_amount(self, amortized_credit_amount):
        """Sets the amortized_credit_amount of this NvlCostAnalysedBillDetail.

        月度成本分摊时，当月已分摊金额中包含的信用额度分摊金额。

        :param amortized_credit_amount: The amortized_credit_amount of this NvlCostAnalysedBillDetail.
        :type amortized_credit_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._amortized_credit_amount = amortized_credit_amount

    @property
    def amortized_coupon_amount(self):
        """Gets the amortized_coupon_amount of this NvlCostAnalysedBillDetail.

        月度成本分摊时，当月已分摊金额中包含的代金券分摊金额。

        :return: The amortized_coupon_amount of this NvlCostAnalysedBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._amortized_coupon_amount

    @amortized_coupon_amount.setter
    def amortized_coupon_amount(self, amortized_coupon_amount):
        """Sets the amortized_coupon_amount of this NvlCostAnalysedBillDetail.

        月度成本分摊时，当月已分摊金额中包含的代金券分摊金额。

        :param amortized_coupon_amount: The amortized_coupon_amount of this NvlCostAnalysedBillDetail.
        :type amortized_coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._amortized_coupon_amount = amortized_coupon_amount

    @property
    def amortized_flexipurchase_coupon_amount(self):
        """Gets the amortized_flexipurchase_coupon_amount of this NvlCostAnalysedBillDetail.

        月度成本分摊时，当月已分摊金额中包含的现金券分摊金额。

        :return: The amortized_flexipurchase_coupon_amount of this NvlCostAnalysedBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._amortized_flexipurchase_coupon_amount

    @amortized_flexipurchase_coupon_amount.setter
    def amortized_flexipurchase_coupon_amount(self, amortized_flexipurchase_coupon_amount):
        """Sets the amortized_flexipurchase_coupon_amount of this NvlCostAnalysedBillDetail.

        月度成本分摊时，当月已分摊金额中包含的现金券分摊金额。

        :param amortized_flexipurchase_coupon_amount: The amortized_flexipurchase_coupon_amount of this NvlCostAnalysedBillDetail.
        :type amortized_flexipurchase_coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._amortized_flexipurchase_coupon_amount = amortized_flexipurchase_coupon_amount

    @property
    def amortized_stored_value_card_amount(self):
        """Gets the amortized_stored_value_card_amount of this NvlCostAnalysedBillDetail.

        月度成本分摊时，当月已分摊金额中包含的储值卡分摊金额。

        :return: The amortized_stored_value_card_amount of this NvlCostAnalysedBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._amortized_stored_value_card_amount

    @amortized_stored_value_card_amount.setter
    def amortized_stored_value_card_amount(self, amortized_stored_value_card_amount):
        """Sets the amortized_stored_value_card_amount of this NvlCostAnalysedBillDetail.

        月度成本分摊时，当月已分摊金额中包含的储值卡分摊金额。

        :param amortized_stored_value_card_amount: The amortized_stored_value_card_amount of this NvlCostAnalysedBillDetail.
        :type amortized_stored_value_card_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._amortized_stored_value_card_amount = amortized_stored_value_card_amount

    @property
    def amortized_bonus_amount(self):
        """Gets the amortized_bonus_amount of this NvlCostAnalysedBillDetail.

        月度成本分摊时，当月已分摊金额中包含的奖励金分摊金额（用于现网未清干净的奖励金）。

        :return: The amortized_bonus_amount of this NvlCostAnalysedBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._amortized_bonus_amount

    @amortized_bonus_amount.setter
    def amortized_bonus_amount(self, amortized_bonus_amount):
        """Sets the amortized_bonus_amount of this NvlCostAnalysedBillDetail.

        月度成本分摊时，当月已分摊金额中包含的奖励金分摊金额（用于现网未清干净的奖励金）。

        :param amortized_bonus_amount: The amortized_bonus_amount of this NvlCostAnalysedBillDetail.
        :type amortized_bonus_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._amortized_bonus_amount = amortized_bonus_amount

    @property
    def sub_service_type_code(self):
        """Gets the sub_service_type_code of this NvlCostAnalysedBillDetail.

        整机的子云服务的自身的云服务类型编码。

        :return: The sub_service_type_code of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._sub_service_type_code

    @sub_service_type_code.setter
    def sub_service_type_code(self, sub_service_type_code):
        """Sets the sub_service_type_code of this NvlCostAnalysedBillDetail.

        整机的子云服务的自身的云服务类型编码。

        :param sub_service_type_code: The sub_service_type_code of this NvlCostAnalysedBillDetail.
        :type sub_service_type_code: str
        """
        self._sub_service_type_code = sub_service_type_code

    @property
    def sub_service_type_name(self):
        """Gets the sub_service_type_name of this NvlCostAnalysedBillDetail.

        整机的子云服务的自身的云服务类型名称。

        :return: The sub_service_type_name of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._sub_service_type_name

    @sub_service_type_name.setter
    def sub_service_type_name(self, sub_service_type_name):
        """Sets the sub_service_type_name of this NvlCostAnalysedBillDetail.

        整机的子云服务的自身的云服务类型名称。

        :param sub_service_type_name: The sub_service_type_name of this NvlCostAnalysedBillDetail.
        :type sub_service_type_name: str
        """
        self._sub_service_type_name = sub_service_type_name

    @property
    def sub_resource_type_code(self):
        """Gets the sub_resource_type_code of this NvlCostAnalysedBillDetail.

        整机的子云服务的自身的资源类型编码。

        :return: The sub_resource_type_code of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._sub_resource_type_code

    @sub_resource_type_code.setter
    def sub_resource_type_code(self, sub_resource_type_code):
        """Sets the sub_resource_type_code of this NvlCostAnalysedBillDetail.

        整机的子云服务的自身的资源类型编码。

        :param sub_resource_type_code: The sub_resource_type_code of this NvlCostAnalysedBillDetail.
        :type sub_resource_type_code: str
        """
        self._sub_resource_type_code = sub_resource_type_code

    @property
    def sub_resource_type_name(self):
        """Gets the sub_resource_type_name of this NvlCostAnalysedBillDetail.

        整机的子云服务的自身的资源类型名称。

        :return: The sub_resource_type_name of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._sub_resource_type_name

    @sub_resource_type_name.setter
    def sub_resource_type_name(self, sub_resource_type_name):
        """Sets the sub_resource_type_name of this NvlCostAnalysedBillDetail.

        整机的子云服务的自身的资源类型名称。

        :param sub_resource_type_name: The sub_resource_type_name of this NvlCostAnalysedBillDetail.
        :type sub_resource_type_name: str
        """
        self._sub_resource_type_name = sub_resource_type_name

    @property
    def sub_resource_id(self):
        """Gets the sub_resource_id of this NvlCostAnalysedBillDetail.

        整机的子云服务的自身的资源ID，资源标识。（如果为预留实例，则为预留实例标识）

        :return: The sub_resource_id of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._sub_resource_id

    @sub_resource_id.setter
    def sub_resource_id(self, sub_resource_id):
        """Sets the sub_resource_id of this NvlCostAnalysedBillDetail.

        整机的子云服务的自身的资源ID，资源标识。（如果为预留实例，则为预留实例标识）

        :param sub_resource_id: The sub_resource_id of this NvlCostAnalysedBillDetail.
        :type sub_resource_id: str
        """
        self._sub_resource_id = sub_resource_id

    @property
    def sub_resource_name(self):
        """Gets the sub_resource_name of this NvlCostAnalysedBillDetail.

        整机的子云服务的自身的资源名称，资源标识。（如果为预留实例，则为预留实例标识）

        :return: The sub_resource_name of this NvlCostAnalysedBillDetail.
        :rtype: str
        """
        return self._sub_resource_name

    @sub_resource_name.setter
    def sub_resource_name(self, sub_resource_name):
        """Sets the sub_resource_name of this NvlCostAnalysedBillDetail.

        整机的子云服务的自身的资源名称，资源标识。（如果为预留实例，则为预留实例标识）

        :param sub_resource_name: The sub_resource_name of this NvlCostAnalysedBillDetail.
        :type sub_resource_name: str
        """
        self._sub_resource_name = sub_resource_name

    @property
    def effective_tag_pairs(self):
        """Gets the effective_tag_pairs of this NvlCostAnalysedBillDetail.

        成本标签。

        :return: The effective_tag_pairs of this NvlCostAnalysedBillDetail.
        :rtype: list[:class:`huaweicloudsdkbss.v2.TagPair`]
        """
        return self._effective_tag_pairs

    @effective_tag_pairs.setter
    def effective_tag_pairs(self, effective_tag_pairs):
        """Sets the effective_tag_pairs of this NvlCostAnalysedBillDetail.

        成本标签。

        :param effective_tag_pairs: The effective_tag_pairs of this NvlCostAnalysedBillDetail.
        :type effective_tag_pairs: list[:class:`huaweicloudsdkbss.v2.TagPair`]
        """
        self._effective_tag_pairs = effective_tag_pairs

    @property
    def cost_unit_pairs(self):
        """Gets the cost_unit_pairs of this NvlCostAnalysedBillDetail.

        成本单元。

        :return: The cost_unit_pairs of this NvlCostAnalysedBillDetail.
        :rtype: list[:class:`huaweicloudsdkbss.v2.CostUnitPair`]
        """
        return self._cost_unit_pairs

    @cost_unit_pairs.setter
    def cost_unit_pairs(self, cost_unit_pairs):
        """Sets the cost_unit_pairs of this NvlCostAnalysedBillDetail.

        成本单元。

        :param cost_unit_pairs: The cost_unit_pairs of this NvlCostAnalysedBillDetail.
        :type cost_unit_pairs: list[:class:`huaweicloudsdkbss.v2.CostUnitPair`]
        """
        self._cost_unit_pairs = cost_unit_pairs

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
        if not isinstance(other, NvlCostAnalysedBillDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
