# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MonthlyBillRes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cycle': 'str',
        'bill_date': 'str',
        'bill_type': 'int',
        'customer_id': 'str',
        'region': 'str',
        'region_name': 'str',
        'cloud_service_type': 'str',
        'resource_type_code': 'str',
        'cloud_service_type_name': 'str',
        'resource_type_name': 'str',
        'res_instance_id': 'str',
        'resource_name': 'str',
        'resource_tag': 'str',
        'sku_code': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'charge_mode': 'int',
        'consume_amount': 'float',
        'cash_amount': 'float',
        'credit_amount': 'float',
        'coupon_amount': 'float',
        'flexipurchase_coupon_amount': 'float',
        'stored_card_amount': 'float',
        'bonus_amount': 'float',
        'debt_amount': 'float',
        'adjustment_amount': 'float',
        'official_amount': 'float',
        'discount_amount': 'float',
        'measure_id': 'int',
        'period_type': 'int',
        'root_resource_id': 'str',
        'parent_resource_id': 'str',
        'trade_id': 'str',
        'product_spec_desc': 'str'
    }

    attribute_map = {
        'cycle': 'cycle',
        'bill_date': 'bill_date',
        'bill_type': 'bill_type',
        'customer_id': 'customer_id',
        'region': 'region',
        'region_name': 'region_name',
        'cloud_service_type': 'cloud_service_type',
        'resource_type_code': 'resource_Type_code',
        'cloud_service_type_name': 'cloud_service_type_name',
        'resource_type_name': 'resource_type_name',
        'res_instance_id': 'res_instance_id',
        'resource_name': 'resource_name',
        'resource_tag': 'resource_tag',
        'sku_code': 'sku_code',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'charge_mode': 'charge_mode',
        'consume_amount': 'consume_amount',
        'cash_amount': 'cash_amount',
        'credit_amount': 'credit_amount',
        'coupon_amount': 'coupon_amount',
        'flexipurchase_coupon_amount': 'flexipurchase_coupon_amount',
        'stored_card_amount': 'stored_card_amount',
        'bonus_amount': 'bonus_amount',
        'debt_amount': 'debt_amount',
        'adjustment_amount': 'adjustment_amount',
        'official_amount': 'official_amount',
        'discount_amount': 'discount_amount',
        'measure_id': 'measure_id',
        'period_type': 'period_type',
        'root_resource_id': 'root_resource_id',
        'parent_resource_id': 'parent_resource_id',
        'trade_id': 'trade_id',
        'product_spec_desc': 'product_spec_desc'
    }

    def __init__(self, cycle=None, bill_date=None, bill_type=None, customer_id=None, region=None, region_name=None, cloud_service_type=None, resource_type_code=None, cloud_service_type_name=None, resource_type_name=None, res_instance_id=None, resource_name=None, resource_tag=None, sku_code=None, enterprise_project_id=None, enterprise_project_name=None, charge_mode=None, consume_amount=None, cash_amount=None, credit_amount=None, coupon_amount=None, flexipurchase_coupon_amount=None, stored_card_amount=None, bonus_amount=None, debt_amount=None, adjustment_amount=None, official_amount=None, discount_amount=None, measure_id=None, period_type=None, root_resource_id=None, parent_resource_id=None, trade_id=None, product_spec_desc=None):
        """MonthlyBillRes

        The model defined in huaweicloud sdk

        :param cycle: 资源详单数据所在账期，东八区时间，格式为YYYY-MM。 例如2020-01。
        :type cycle: str
        :param bill_date: 消费日期，东八区时间，格式为YYYY-MM-DD。  说明： 当statistic_type&#x3D;2时该字段才有值，否则返回null。
        :type bill_date: str
        :param bill_type: 账单类型。 1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费16：调账-扣费18：消费-按月付费20：退款-变更
        :type bill_type: int
        :param customer_id: 消费的客户账号ID。 如果是普通客户或者企业子客户查询消费记录，只能查询到客户自己的消费记录，且此处显示的是客户自己的客户ID。如果是企业主查询消费记录，可以查询到企业主以及企业子客户的消费记录，此处为消费的实际客户ID。如果是企业主自己的消费记录，则为企业主ID；如果是某个企业子客户的消费记录，则此处为企业子账号ID。
        :type customer_id: str
        :param region: 云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。
        :type region: str
        :param region_name: 云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。
        :type region_name: str
        :param cloud_service_type: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。
        :type cloud_service_type: str
        :param resource_type_code: 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。
        :type resource_type_code: str
        :param cloud_service_type_name: 云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。
        :type cloud_service_type_name: str
        :param resource_type_name: 资源类型名称。例如ECS的资源类型名称为“云主机”。
        :type resource_type_name: str
        :param res_instance_id: 资源实例ID。
        :type res_instance_id: str
        :param resource_name: 资源名称。客户在创建资源的时候，可以输入资源名称，有些资源也可以在管理资源时，修改资源名称。
        :type resource_name: str
        :param resource_tag: 资源标签。客户在管理资源的时候，可以设置资源标签。
        :type resource_tag: str
        :param sku_code: SKU编码，在账单中唯一标识一个资源的规格。
        :type sku_code: str
        :param enterprise_project_id: 企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：-1其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业项目名称。
        :type enterprise_project_name: str
        :param charge_mode: 计费模式。 1 : 包年/包月3：按需10：预留实例
        :type charge_mode: int
        :param consume_amount: 客户购买云服务类型的消费金额，包含代金券、现金券，精确到小数点后2位。  说明： consume_amount的值等于cash_amount，credit_amount，coupon_amount，flexipurchase_coupon_amount，stored_card_amount，bonus_amount，debt_amount，adjustment_amount的总和。
        :type consume_amount: float
        :param cash_amount: 现金支付金额。
        :type cash_amount: float
        :param credit_amount: 信用额度支付金额。
        :type credit_amount: float
        :param coupon_amount: 代金券支付金额。
        :type coupon_amount: float
        :param flexipurchase_coupon_amount: 现金券支付金额。
        :type flexipurchase_coupon_amount: float
        :param stored_card_amount: 储值卡支付金额。
        :type stored_card_amount: float
        :param bonus_amount: 奖励金支付金额（用于现网客户未使用完的奖励金）。
        :type bonus_amount: float
        :param debt_amount: 欠费金额。
        :type debt_amount: float
        :param adjustment_amount: 欠费核销金额。
        :type adjustment_amount: float
        :param official_amount: 官网价。
        :type official_amount: float
        :param discount_amount: 对应官网价折扣金额。
        :type discount_amount: float
        :param measure_id: 金额单位。 1：元
        :type measure_id: int
        :param period_type: 周期类型： 19：年20：月24：天25：小时5：一次性
        :type period_type: int
        :param root_resource_id: 根资源标识。
        :type root_resource_id: str
        :param parent_resource_id: 父资源标识。
        :type parent_resource_id: str
        :param trade_id: 订单ID 或 交易ID。 账单类型为1，2，3，4，8时为订单ID；其它场景下为： 交易ID(非月末扣费：应收ID；月末扣费：账单ID)。
        :type trade_id: str
        :param product_spec_desc: 产品的规格描述。
        :type product_spec_desc: str
        """
        
        

        self._cycle = None
        self._bill_date = None
        self._bill_type = None
        self._customer_id = None
        self._region = None
        self._region_name = None
        self._cloud_service_type = None
        self._resource_type_code = None
        self._cloud_service_type_name = None
        self._resource_type_name = None
        self._res_instance_id = None
        self._resource_name = None
        self._resource_tag = None
        self._sku_code = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._charge_mode = None
        self._consume_amount = None
        self._cash_amount = None
        self._credit_amount = None
        self._coupon_amount = None
        self._flexipurchase_coupon_amount = None
        self._stored_card_amount = None
        self._bonus_amount = None
        self._debt_amount = None
        self._adjustment_amount = None
        self._official_amount = None
        self._discount_amount = None
        self._measure_id = None
        self._period_type = None
        self._root_resource_id = None
        self._parent_resource_id = None
        self._trade_id = None
        self._product_spec_desc = None
        self.discriminator = None

        if cycle is not None:
            self.cycle = cycle
        if bill_date is not None:
            self.bill_date = bill_date
        if bill_type is not None:
            self.bill_type = bill_type
        if customer_id is not None:
            self.customer_id = customer_id
        if region is not None:
            self.region = region
        if region_name is not None:
            self.region_name = region_name
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if cloud_service_type_name is not None:
            self.cloud_service_type_name = cloud_service_type_name
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if res_instance_id is not None:
            self.res_instance_id = res_instance_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_tag is not None:
            self.resource_tag = resource_tag
        if sku_code is not None:
            self.sku_code = sku_code
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if charge_mode is not None:
            self.charge_mode = charge_mode
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
        if stored_card_amount is not None:
            self.stored_card_amount = stored_card_amount
        if bonus_amount is not None:
            self.bonus_amount = bonus_amount
        if debt_amount is not None:
            self.debt_amount = debt_amount
        if adjustment_amount is not None:
            self.adjustment_amount = adjustment_amount
        if official_amount is not None:
            self.official_amount = official_amount
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if period_type is not None:
            self.period_type = period_type
        if root_resource_id is not None:
            self.root_resource_id = root_resource_id
        if parent_resource_id is not None:
            self.parent_resource_id = parent_resource_id
        if trade_id is not None:
            self.trade_id = trade_id
        if product_spec_desc is not None:
            self.product_spec_desc = product_spec_desc

    @property
    def cycle(self):
        """Gets the cycle of this MonthlyBillRes.

        资源详单数据所在账期，东八区时间，格式为YYYY-MM。 例如2020-01。

        :return: The cycle of this MonthlyBillRes.
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this MonthlyBillRes.

        资源详单数据所在账期，东八区时间，格式为YYYY-MM。 例如2020-01。

        :param cycle: The cycle of this MonthlyBillRes.
        :type cycle: str
        """
        self._cycle = cycle

    @property
    def bill_date(self):
        """Gets the bill_date of this MonthlyBillRes.

        消费日期，东八区时间，格式为YYYY-MM-DD。  说明： 当statistic_type=2时该字段才有值，否则返回null。

        :return: The bill_date of this MonthlyBillRes.
        :rtype: str
        """
        return self._bill_date

    @bill_date.setter
    def bill_date(self, bill_date):
        """Sets the bill_date of this MonthlyBillRes.

        消费日期，东八区时间，格式为YYYY-MM-DD。  说明： 当statistic_type=2时该字段才有值，否则返回null。

        :param bill_date: The bill_date of this MonthlyBillRes.
        :type bill_date: str
        """
        self._bill_date = bill_date

    @property
    def bill_type(self):
        """Gets the bill_type of this MonthlyBillRes.

        账单类型。 1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费16：调账-扣费18：消费-按月付费20：退款-变更

        :return: The bill_type of this MonthlyBillRes.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this MonthlyBillRes.

        账单类型。 1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费16：调账-扣费18：消费-按月付费20：退款-变更

        :param bill_type: The bill_type of this MonthlyBillRes.
        :type bill_type: int
        """
        self._bill_type = bill_type

    @property
    def customer_id(self):
        """Gets the customer_id of this MonthlyBillRes.

        消费的客户账号ID。 如果是普通客户或者企业子客户查询消费记录，只能查询到客户自己的消费记录，且此处显示的是客户自己的客户ID。如果是企业主查询消费记录，可以查询到企业主以及企业子客户的消费记录，此处为消费的实际客户ID。如果是企业主自己的消费记录，则为企业主ID；如果是某个企业子客户的消费记录，则此处为企业子账号ID。

        :return: The customer_id of this MonthlyBillRes.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this MonthlyBillRes.

        消费的客户账号ID。 如果是普通客户或者企业子客户查询消费记录，只能查询到客户自己的消费记录，且此处显示的是客户自己的客户ID。如果是企业主查询消费记录，可以查询到企业主以及企业子客户的消费记录，此处为消费的实际客户ID。如果是企业主自己的消费记录，则为企业主ID；如果是某个企业子客户的消费记录，则此处为企业子账号ID。

        :param customer_id: The customer_id of this MonthlyBillRes.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def region(self):
        """Gets the region of this MonthlyBillRes.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :return: The region of this MonthlyBillRes.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this MonthlyBillRes.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :param region: The region of this MonthlyBillRes.
        :type region: str
        """
        self._region = region

    @property
    def region_name(self):
        """Gets the region_name of this MonthlyBillRes.

        云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。

        :return: The region_name of this MonthlyBillRes.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this MonthlyBillRes.

        云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。

        :param region_name: The region_name of this MonthlyBillRes.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this MonthlyBillRes.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :return: The cloud_service_type of this MonthlyBillRes.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this MonthlyBillRes.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :param cloud_service_type: The cloud_service_type of this MonthlyBillRes.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this MonthlyBillRes.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :return: The resource_type_code of this MonthlyBillRes.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this MonthlyBillRes.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :param resource_type_code: The resource_type_code of this MonthlyBillRes.
        :type resource_type_code: str
        """
        self._resource_type_code = resource_type_code

    @property
    def cloud_service_type_name(self):
        """Gets the cloud_service_type_name of this MonthlyBillRes.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :return: The cloud_service_type_name of this MonthlyBillRes.
        :rtype: str
        """
        return self._cloud_service_type_name

    @cloud_service_type_name.setter
    def cloud_service_type_name(self, cloud_service_type_name):
        """Sets the cloud_service_type_name of this MonthlyBillRes.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :param cloud_service_type_name: The cloud_service_type_name of this MonthlyBillRes.
        :type cloud_service_type_name: str
        """
        self._cloud_service_type_name = cloud_service_type_name

    @property
    def resource_type_name(self):
        """Gets the resource_type_name of this MonthlyBillRes.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :return: The resource_type_name of this MonthlyBillRes.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        """Sets the resource_type_name of this MonthlyBillRes.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :param resource_type_name: The resource_type_name of this MonthlyBillRes.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def res_instance_id(self):
        """Gets the res_instance_id of this MonthlyBillRes.

        资源实例ID。

        :return: The res_instance_id of this MonthlyBillRes.
        :rtype: str
        """
        return self._res_instance_id

    @res_instance_id.setter
    def res_instance_id(self, res_instance_id):
        """Sets the res_instance_id of this MonthlyBillRes.

        资源实例ID。

        :param res_instance_id: The res_instance_id of this MonthlyBillRes.
        :type res_instance_id: str
        """
        self._res_instance_id = res_instance_id

    @property
    def resource_name(self):
        """Gets the resource_name of this MonthlyBillRes.

        资源名称。客户在创建资源的时候，可以输入资源名称，有些资源也可以在管理资源时，修改资源名称。

        :return: The resource_name of this MonthlyBillRes.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this MonthlyBillRes.

        资源名称。客户在创建资源的时候，可以输入资源名称，有些资源也可以在管理资源时，修改资源名称。

        :param resource_name: The resource_name of this MonthlyBillRes.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_tag(self):
        """Gets the resource_tag of this MonthlyBillRes.

        资源标签。客户在管理资源的时候，可以设置资源标签。

        :return: The resource_tag of this MonthlyBillRes.
        :rtype: str
        """
        return self._resource_tag

    @resource_tag.setter
    def resource_tag(self, resource_tag):
        """Sets the resource_tag of this MonthlyBillRes.

        资源标签。客户在管理资源的时候，可以设置资源标签。

        :param resource_tag: The resource_tag of this MonthlyBillRes.
        :type resource_tag: str
        """
        self._resource_tag = resource_tag

    @property
    def sku_code(self):
        """Gets the sku_code of this MonthlyBillRes.

        SKU编码，在账单中唯一标识一个资源的规格。

        :return: The sku_code of this MonthlyBillRes.
        :rtype: str
        """
        return self._sku_code

    @sku_code.setter
    def sku_code(self, sku_code):
        """Sets the sku_code of this MonthlyBillRes.

        SKU编码，在账单中唯一标识一个资源的规格。

        :param sku_code: The sku_code of this MonthlyBillRes.
        :type sku_code: str
        """
        self._sku_code = sku_code

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this MonthlyBillRes.

        企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：-1其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :return: The enterprise_project_id of this MonthlyBillRes.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this MonthlyBillRes.

        企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：-1其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :param enterprise_project_id: The enterprise_project_id of this MonthlyBillRes.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        """Gets the enterprise_project_name of this MonthlyBillRes.

        企业项目名称。

        :return: The enterprise_project_name of this MonthlyBillRes.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        """Sets the enterprise_project_name of this MonthlyBillRes.

        企业项目名称。

        :param enterprise_project_name: The enterprise_project_name of this MonthlyBillRes.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def charge_mode(self):
        """Gets the charge_mode of this MonthlyBillRes.

        计费模式。 1 : 包年/包月3：按需10：预留实例

        :return: The charge_mode of this MonthlyBillRes.
        :rtype: int
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this MonthlyBillRes.

        计费模式。 1 : 包年/包月3：按需10：预留实例

        :param charge_mode: The charge_mode of this MonthlyBillRes.
        :type charge_mode: int
        """
        self._charge_mode = charge_mode

    @property
    def consume_amount(self):
        """Gets the consume_amount of this MonthlyBillRes.

        客户购买云服务类型的消费金额，包含代金券、现金券，精确到小数点后2位。  说明： consume_amount的值等于cash_amount，credit_amount，coupon_amount，flexipurchase_coupon_amount，stored_card_amount，bonus_amount，debt_amount，adjustment_amount的总和。

        :return: The consume_amount of this MonthlyBillRes.
        :rtype: float
        """
        return self._consume_amount

    @consume_amount.setter
    def consume_amount(self, consume_amount):
        """Sets the consume_amount of this MonthlyBillRes.

        客户购买云服务类型的消费金额，包含代金券、现金券，精确到小数点后2位。  说明： consume_amount的值等于cash_amount，credit_amount，coupon_amount，flexipurchase_coupon_amount，stored_card_amount，bonus_amount，debt_amount，adjustment_amount的总和。

        :param consume_amount: The consume_amount of this MonthlyBillRes.
        :type consume_amount: float
        """
        self._consume_amount = consume_amount

    @property
    def cash_amount(self):
        """Gets the cash_amount of this MonthlyBillRes.

        现金支付金额。

        :return: The cash_amount of this MonthlyBillRes.
        :rtype: float
        """
        return self._cash_amount

    @cash_amount.setter
    def cash_amount(self, cash_amount):
        """Sets the cash_amount of this MonthlyBillRes.

        现金支付金额。

        :param cash_amount: The cash_amount of this MonthlyBillRes.
        :type cash_amount: float
        """
        self._cash_amount = cash_amount

    @property
    def credit_amount(self):
        """Gets the credit_amount of this MonthlyBillRes.

        信用额度支付金额。

        :return: The credit_amount of this MonthlyBillRes.
        :rtype: float
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        """Sets the credit_amount of this MonthlyBillRes.

        信用额度支付金额。

        :param credit_amount: The credit_amount of this MonthlyBillRes.
        :type credit_amount: float
        """
        self._credit_amount = credit_amount

    @property
    def coupon_amount(self):
        """Gets the coupon_amount of this MonthlyBillRes.

        代金券支付金额。

        :return: The coupon_amount of this MonthlyBillRes.
        :rtype: float
        """
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, coupon_amount):
        """Sets the coupon_amount of this MonthlyBillRes.

        代金券支付金额。

        :param coupon_amount: The coupon_amount of this MonthlyBillRes.
        :type coupon_amount: float
        """
        self._coupon_amount = coupon_amount

    @property
    def flexipurchase_coupon_amount(self):
        """Gets the flexipurchase_coupon_amount of this MonthlyBillRes.

        现金券支付金额。

        :return: The flexipurchase_coupon_amount of this MonthlyBillRes.
        :rtype: float
        """
        return self._flexipurchase_coupon_amount

    @flexipurchase_coupon_amount.setter
    def flexipurchase_coupon_amount(self, flexipurchase_coupon_amount):
        """Sets the flexipurchase_coupon_amount of this MonthlyBillRes.

        现金券支付金额。

        :param flexipurchase_coupon_amount: The flexipurchase_coupon_amount of this MonthlyBillRes.
        :type flexipurchase_coupon_amount: float
        """
        self._flexipurchase_coupon_amount = flexipurchase_coupon_amount

    @property
    def stored_card_amount(self):
        """Gets the stored_card_amount of this MonthlyBillRes.

        储值卡支付金额。

        :return: The stored_card_amount of this MonthlyBillRes.
        :rtype: float
        """
        return self._stored_card_amount

    @stored_card_amount.setter
    def stored_card_amount(self, stored_card_amount):
        """Sets the stored_card_amount of this MonthlyBillRes.

        储值卡支付金额。

        :param stored_card_amount: The stored_card_amount of this MonthlyBillRes.
        :type stored_card_amount: float
        """
        self._stored_card_amount = stored_card_amount

    @property
    def bonus_amount(self):
        """Gets the bonus_amount of this MonthlyBillRes.

        奖励金支付金额（用于现网客户未使用完的奖励金）。

        :return: The bonus_amount of this MonthlyBillRes.
        :rtype: float
        """
        return self._bonus_amount

    @bonus_amount.setter
    def bonus_amount(self, bonus_amount):
        """Sets the bonus_amount of this MonthlyBillRes.

        奖励金支付金额（用于现网客户未使用完的奖励金）。

        :param bonus_amount: The bonus_amount of this MonthlyBillRes.
        :type bonus_amount: float
        """
        self._bonus_amount = bonus_amount

    @property
    def debt_amount(self):
        """Gets the debt_amount of this MonthlyBillRes.

        欠费金额。

        :return: The debt_amount of this MonthlyBillRes.
        :rtype: float
        """
        return self._debt_amount

    @debt_amount.setter
    def debt_amount(self, debt_amount):
        """Sets the debt_amount of this MonthlyBillRes.

        欠费金额。

        :param debt_amount: The debt_amount of this MonthlyBillRes.
        :type debt_amount: float
        """
        self._debt_amount = debt_amount

    @property
    def adjustment_amount(self):
        """Gets the adjustment_amount of this MonthlyBillRes.

        欠费核销金额。

        :return: The adjustment_amount of this MonthlyBillRes.
        :rtype: float
        """
        return self._adjustment_amount

    @adjustment_amount.setter
    def adjustment_amount(self, adjustment_amount):
        """Sets the adjustment_amount of this MonthlyBillRes.

        欠费核销金额。

        :param adjustment_amount: The adjustment_amount of this MonthlyBillRes.
        :type adjustment_amount: float
        """
        self._adjustment_amount = adjustment_amount

    @property
    def official_amount(self):
        """Gets the official_amount of this MonthlyBillRes.

        官网价。

        :return: The official_amount of this MonthlyBillRes.
        :rtype: float
        """
        return self._official_amount

    @official_amount.setter
    def official_amount(self, official_amount):
        """Sets the official_amount of this MonthlyBillRes.

        官网价。

        :param official_amount: The official_amount of this MonthlyBillRes.
        :type official_amount: float
        """
        self._official_amount = official_amount

    @property
    def discount_amount(self):
        """Gets the discount_amount of this MonthlyBillRes.

        对应官网价折扣金额。

        :return: The discount_amount of this MonthlyBillRes.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this MonthlyBillRes.

        对应官网价折扣金额。

        :param discount_amount: The discount_amount of this MonthlyBillRes.
        :type discount_amount: float
        """
        self._discount_amount = discount_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this MonthlyBillRes.

        金额单位。 1：元

        :return: The measure_id of this MonthlyBillRes.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this MonthlyBillRes.

        金额单位。 1：元

        :param measure_id: The measure_id of this MonthlyBillRes.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def period_type(self):
        """Gets the period_type of this MonthlyBillRes.

        周期类型： 19：年20：月24：天25：小时5：一次性

        :return: The period_type of this MonthlyBillRes.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this MonthlyBillRes.

        周期类型： 19：年20：月24：天25：小时5：一次性

        :param period_type: The period_type of this MonthlyBillRes.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def root_resource_id(self):
        """Gets the root_resource_id of this MonthlyBillRes.

        根资源标识。

        :return: The root_resource_id of this MonthlyBillRes.
        :rtype: str
        """
        return self._root_resource_id

    @root_resource_id.setter
    def root_resource_id(self, root_resource_id):
        """Sets the root_resource_id of this MonthlyBillRes.

        根资源标识。

        :param root_resource_id: The root_resource_id of this MonthlyBillRes.
        :type root_resource_id: str
        """
        self._root_resource_id = root_resource_id

    @property
    def parent_resource_id(self):
        """Gets the parent_resource_id of this MonthlyBillRes.

        父资源标识。

        :return: The parent_resource_id of this MonthlyBillRes.
        :rtype: str
        """
        return self._parent_resource_id

    @parent_resource_id.setter
    def parent_resource_id(self, parent_resource_id):
        """Sets the parent_resource_id of this MonthlyBillRes.

        父资源标识。

        :param parent_resource_id: The parent_resource_id of this MonthlyBillRes.
        :type parent_resource_id: str
        """
        self._parent_resource_id = parent_resource_id

    @property
    def trade_id(self):
        """Gets the trade_id of this MonthlyBillRes.

        订单ID 或 交易ID。 账单类型为1，2，3，4，8时为订单ID；其它场景下为： 交易ID(非月末扣费：应收ID；月末扣费：账单ID)。

        :return: The trade_id of this MonthlyBillRes.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        """Sets the trade_id of this MonthlyBillRes.

        订单ID 或 交易ID。 账单类型为1，2，3，4，8时为订单ID；其它场景下为： 交易ID(非月末扣费：应收ID；月末扣费：账单ID)。

        :param trade_id: The trade_id of this MonthlyBillRes.
        :type trade_id: str
        """
        self._trade_id = trade_id

    @property
    def product_spec_desc(self):
        """Gets the product_spec_desc of this MonthlyBillRes.

        产品的规格描述。

        :return: The product_spec_desc of this MonthlyBillRes.
        :rtype: str
        """
        return self._product_spec_desc

    @product_spec_desc.setter
    def product_spec_desc(self, product_spec_desc):
        """Sets the product_spec_desc of this MonthlyBillRes.

        产品的规格描述。

        :param product_spec_desc: The product_spec_desc of this MonthlyBillRes.
        :type product_spec_desc: str
        """
        self._product_spec_desc = product_spec_desc

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
        if not isinstance(other, MonthlyBillRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
