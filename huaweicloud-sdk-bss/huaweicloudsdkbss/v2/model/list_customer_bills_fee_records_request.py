# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomerBillsFeeRecordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'bill_cycle': 'str',
        'provider_type': 'int',
        'service_type_code': 'str',
        'resource_type_code': 'str',
        'region_code': 'str',
        'charging_mode': 'int',
        'bill_type': 'int',
        'trade_id': 'str',
        'enterprise_project_id': 'str',
        'include_zero_record': 'bool',
        'status': 'int',
        'method': 'str',
        'sub_customer_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'bill_date_begin': 'str',
        'bill_date_end': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'bill_cycle': 'bill_cycle',
        'provider_type': 'provider_type',
        'service_type_code': 'service_type_code',
        'resource_type_code': 'resource_type_code',
        'region_code': 'region_code',
        'charging_mode': 'charging_mode',
        'bill_type': 'bill_type',
        'trade_id': 'trade_id',
        'enterprise_project_id': 'enterprise_project_id',
        'include_zero_record': 'include_zero_record',
        'status': 'status',
        'method': 'method',
        'sub_customer_id': 'sub_customer_id',
        'offset': 'offset',
        'limit': 'limit',
        'bill_date_begin': 'bill_date_begin',
        'bill_date_end': 'bill_date_end'
    }

    def __init__(self, x_language=None, bill_cycle=None, provider_type=None, service_type_code=None, resource_type_code=None, region_code=None, charging_mode=None, bill_type=None, trade_id=None, enterprise_project_id=None, include_zero_record=None, status=None, method=None, sub_customer_id=None, offset=None, limit=None, bill_date_begin=None, bill_date_end=None):
        """ListCustomerBillsFeeRecordsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。zh_CN：中文 en_US：英文。默认为zh_CN：中文。
        :type x_language: str
        :param bill_cycle: 查询的流水账单所在账期，东八区时间，格式为YYYY-MM。
        :type bill_cycle: str
        :param provider_type: 服务商。1：华为云2：云商店为空时查询包含华为云和云商店在内的全部服务商。此参数不携带或携带值为空时，不作为筛选条件。
        :type provider_type: int
        :param service_type_code: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用[查询云服务类型列表](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001256679455.html)接口获取。此参数不携带或携带值为空时，不作为筛选条件。
        :type service_type_code: str
        :param resource_type_code: 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用[查询资源类型列表](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001256519451.html)接口获取。此参数不携带或携带值为空时，不作为筛选条件。
        :type resource_type_code: str
        :param region_code: 云服务区编码，例如：“cn-north-1”。具体请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)对应云服务的“区域”列的值。此参数不携带或携带值为空时，不作为筛选条件。
        :type region_code: str
        :param charging_mode: 计费模式：1 : 包年/包月3：按需10：预留实例 此参数不携带或携带值为空时，不作为筛选条件。
        :type charging_mode: int
        :param bill_type: 账单类型：1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费16：调账-扣费18：消费-按月付费20 退款-变更(整机)21 退款-变更(降配) 此参数不携带或携带值为空时，不作为筛选条件。
        :type bill_type: int
        :param trade_id: 订单ID或交易ID。账单类型为1、2、3、4和8时此处为订单ID。账单类型为其它场景时此处为交易ID，为扣费维度的唯一标识。例如非月末扣费时为应收ID；月末扣费时为账单ID。此参数不携带或携带值为空时，不作为筛选条件。
        :type trade_id: str
        :param enterprise_project_id: 企业项目标识（企业项目ID）。default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。此参数不携带或携带值为空时，不作为筛选条件。
        :type enterprise_project_id: str
        :param include_zero_record: 返回是否包含应付金额为0的记录。true：包含false：不包含此参数不携带或携带值为空时，不作为筛选条件。
        :type include_zero_record: bool
        :param status: 支付状态。1：已支付2：未结清3：未出账此参数不携带或携带值为空时，不作为筛选条件。
        :type status: int
        :param method: 查询流水账单的方式。oneself：客户自己sub_customer：企业子客户all：客户自己和企业子客户 此参数不携带或携带值为空时，默认值为“all”，如果没有企业子客户，取值为all时查询的是客户自己的流水账单。
        :type method: str
        :param sub_customer_id: 企业子账号ID。 说明： 如果method取值不为sub_customer，则该参数无效。如果method取值为sub_customer，则该参数不能为空。
        :type sub_customer_id: str
        :param offset: 偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 页面大小。默认值为10。
        :type limit: int
        :param bill_date_begin: 查询的流水账单的开始日期，东八区时间，格式为YYYY-MM-DD。此参数不携带或携带值为空时，不作为筛选条件。 说明： 必须和bill_cycle（即流水账单的所在账期）在同一个月。bill_date_begin和bill_date_end两个参数必须同时出现，否则仅按照bill_cycle（即流水账单的所在账期）进行查询。
        :type bill_date_begin: str
        :param bill_date_end: 查询的流水账单的结束日期，东八区时间，格式为YYYY-MM-DD。此参数不携带或携带值为空时，不作为筛选条件。 说明： 必须和bill_cycle（即流水账单的所在账期）在同一个月。bill_date_begin和bill_date_end两个参数必须同时出现，否则仅按照bill_cycle（即流水账单的所在账期）进行查询。
        :type bill_date_end: str
        """
        
        

        self._x_language = None
        self._bill_cycle = None
        self._provider_type = None
        self._service_type_code = None
        self._resource_type_code = None
        self._region_code = None
        self._charging_mode = None
        self._bill_type = None
        self._trade_id = None
        self._enterprise_project_id = None
        self._include_zero_record = None
        self._status = None
        self._method = None
        self._sub_customer_id = None
        self._offset = None
        self._limit = None
        self._bill_date_begin = None
        self._bill_date_end = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.bill_cycle = bill_cycle
        if provider_type is not None:
            self.provider_type = provider_type
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if region_code is not None:
            self.region_code = region_code
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if bill_type is not None:
            self.bill_type = bill_type
        if trade_id is not None:
            self.trade_id = trade_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if include_zero_record is not None:
            self.include_zero_record = include_zero_record
        if status is not None:
            self.status = status
        if method is not None:
            self.method = method
        if sub_customer_id is not None:
            self.sub_customer_id = sub_customer_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if bill_date_begin is not None:
            self.bill_date_begin = bill_date_begin
        if bill_date_end is not None:
            self.bill_date_end = bill_date_end

    @property
    def x_language(self):
        """Gets the x_language of this ListCustomerBillsFeeRecordsRequest.

        语言。zh_CN：中文 en_US：英文。默认为zh_CN：中文。

        :return: The x_language of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListCustomerBillsFeeRecordsRequest.

        语言。zh_CN：中文 en_US：英文。默认为zh_CN：中文。

        :param x_language: The x_language of this ListCustomerBillsFeeRecordsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def bill_cycle(self):
        """Gets the bill_cycle of this ListCustomerBillsFeeRecordsRequest.

        查询的流水账单所在账期，东八区时间，格式为YYYY-MM。

        :return: The bill_cycle of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, bill_cycle):
        """Sets the bill_cycle of this ListCustomerBillsFeeRecordsRequest.

        查询的流水账单所在账期，东八区时间，格式为YYYY-MM。

        :param bill_cycle: The bill_cycle of this ListCustomerBillsFeeRecordsRequest.
        :type bill_cycle: str
        """
        self._bill_cycle = bill_cycle

    @property
    def provider_type(self):
        """Gets the provider_type of this ListCustomerBillsFeeRecordsRequest.

        服务商。1：华为云2：云商店为空时查询包含华为云和云商店在内的全部服务商。此参数不携带或携带值为空时，不作为筛选条件。

        :return: The provider_type of this ListCustomerBillsFeeRecordsRequest.
        :rtype: int
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this ListCustomerBillsFeeRecordsRequest.

        服务商。1：华为云2：云商店为空时查询包含华为云和云商店在内的全部服务商。此参数不携带或携带值为空时，不作为筛选条件。

        :param provider_type: The provider_type of this ListCustomerBillsFeeRecordsRequest.
        :type provider_type: int
        """
        self._provider_type = provider_type

    @property
    def service_type_code(self):
        """Gets the service_type_code of this ListCustomerBillsFeeRecordsRequest.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用[查询云服务类型列表](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001256679455.html)接口获取。此参数不携带或携带值为空时，不作为筛选条件。

        :return: The service_type_code of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this ListCustomerBillsFeeRecordsRequest.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用[查询云服务类型列表](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001256679455.html)接口获取。此参数不携带或携带值为空时，不作为筛选条件。

        :param service_type_code: The service_type_code of this ListCustomerBillsFeeRecordsRequest.
        :type service_type_code: str
        """
        self._service_type_code = service_type_code

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this ListCustomerBillsFeeRecordsRequest.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用[查询资源类型列表](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001256519451.html)接口获取。此参数不携带或携带值为空时，不作为筛选条件。

        :return: The resource_type_code of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this ListCustomerBillsFeeRecordsRequest.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用[查询资源类型列表](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001256519451.html)接口获取。此参数不携带或携带值为空时，不作为筛选条件。

        :param resource_type_code: The resource_type_code of this ListCustomerBillsFeeRecordsRequest.
        :type resource_type_code: str
        """
        self._resource_type_code = resource_type_code

    @property
    def region_code(self):
        """Gets the region_code of this ListCustomerBillsFeeRecordsRequest.

        云服务区编码，例如：“cn-north-1”。具体请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)对应云服务的“区域”列的值。此参数不携带或携带值为空时，不作为筛选条件。

        :return: The region_code of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this ListCustomerBillsFeeRecordsRequest.

        云服务区编码，例如：“cn-north-1”。具体请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)对应云服务的“区域”列的值。此参数不携带或携带值为空时，不作为筛选条件。

        :param region_code: The region_code of this ListCustomerBillsFeeRecordsRequest.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def charging_mode(self):
        """Gets the charging_mode of this ListCustomerBillsFeeRecordsRequest.

        计费模式：1 : 包年/包月3：按需10：预留实例 此参数不携带或携带值为空时，不作为筛选条件。

        :return: The charging_mode of this ListCustomerBillsFeeRecordsRequest.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this ListCustomerBillsFeeRecordsRequest.

        计费模式：1 : 包年/包月3：按需10：预留实例 此参数不携带或携带值为空时，不作为筛选条件。

        :param charging_mode: The charging_mode of this ListCustomerBillsFeeRecordsRequest.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def bill_type(self):
        """Gets the bill_type of this ListCustomerBillsFeeRecordsRequest.

        账单类型：1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费16：调账-扣费18：消费-按月付费20 退款-变更(整机)21 退款-变更(降配) 此参数不携带或携带值为空时，不作为筛选条件。

        :return: The bill_type of this ListCustomerBillsFeeRecordsRequest.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this ListCustomerBillsFeeRecordsRequest.

        账单类型：1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费16：调账-扣费18：消费-按月付费20 退款-变更(整机)21 退款-变更(降配) 此参数不携带或携带值为空时，不作为筛选条件。

        :param bill_type: The bill_type of this ListCustomerBillsFeeRecordsRequest.
        :type bill_type: int
        """
        self._bill_type = bill_type

    @property
    def trade_id(self):
        """Gets the trade_id of this ListCustomerBillsFeeRecordsRequest.

        订单ID或交易ID。账单类型为1、2、3、4和8时此处为订单ID。账单类型为其它场景时此处为交易ID，为扣费维度的唯一标识。例如非月末扣费时为应收ID；月末扣费时为账单ID。此参数不携带或携带值为空时，不作为筛选条件。

        :return: The trade_id of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        """Sets the trade_id of this ListCustomerBillsFeeRecordsRequest.

        订单ID或交易ID。账单类型为1、2、3、4和8时此处为订单ID。账单类型为其它场景时此处为交易ID，为扣费维度的唯一标识。例如非月末扣费时为应收ID；月末扣费时为账单ID。此参数不携带或携带值为空时，不作为筛选条件。

        :param trade_id: The trade_id of this ListCustomerBillsFeeRecordsRequest.
        :type trade_id: str
        """
        self._trade_id = trade_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListCustomerBillsFeeRecordsRequest.

        企业项目标识（企业项目ID）。default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。此参数不携带或携带值为空时，不作为筛选条件。

        :return: The enterprise_project_id of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListCustomerBillsFeeRecordsRequest.

        企业项目标识（企业项目ID）。default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。此参数不携带或携带值为空时，不作为筛选条件。

        :param enterprise_project_id: The enterprise_project_id of this ListCustomerBillsFeeRecordsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def include_zero_record(self):
        """Gets the include_zero_record of this ListCustomerBillsFeeRecordsRequest.

        返回是否包含应付金额为0的记录。true：包含false：不包含此参数不携带或携带值为空时，不作为筛选条件。

        :return: The include_zero_record of this ListCustomerBillsFeeRecordsRequest.
        :rtype: bool
        """
        return self._include_zero_record

    @include_zero_record.setter
    def include_zero_record(self, include_zero_record):
        """Sets the include_zero_record of this ListCustomerBillsFeeRecordsRequest.

        返回是否包含应付金额为0的记录。true：包含false：不包含此参数不携带或携带值为空时，不作为筛选条件。

        :param include_zero_record: The include_zero_record of this ListCustomerBillsFeeRecordsRequest.
        :type include_zero_record: bool
        """
        self._include_zero_record = include_zero_record

    @property
    def status(self):
        """Gets the status of this ListCustomerBillsFeeRecordsRequest.

        支付状态。1：已支付2：未结清3：未出账此参数不携带或携带值为空时，不作为筛选条件。

        :return: The status of this ListCustomerBillsFeeRecordsRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListCustomerBillsFeeRecordsRequest.

        支付状态。1：已支付2：未结清3：未出账此参数不携带或携带值为空时，不作为筛选条件。

        :param status: The status of this ListCustomerBillsFeeRecordsRequest.
        :type status: int
        """
        self._status = status

    @property
    def method(self):
        """Gets the method of this ListCustomerBillsFeeRecordsRequest.

        查询流水账单的方式。oneself：客户自己sub_customer：企业子客户all：客户自己和企业子客户 此参数不携带或携带值为空时，默认值为“all”，如果没有企业子客户，取值为all时查询的是客户自己的流水账单。

        :return: The method of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ListCustomerBillsFeeRecordsRequest.

        查询流水账单的方式。oneself：客户自己sub_customer：企业子客户all：客户自己和企业子客户 此参数不携带或携带值为空时，默认值为“all”，如果没有企业子客户，取值为all时查询的是客户自己的流水账单。

        :param method: The method of this ListCustomerBillsFeeRecordsRequest.
        :type method: str
        """
        self._method = method

    @property
    def sub_customer_id(self):
        """Gets the sub_customer_id of this ListCustomerBillsFeeRecordsRequest.

        企业子账号ID。 说明： 如果method取值不为sub_customer，则该参数无效。如果method取值为sub_customer，则该参数不能为空。

        :return: The sub_customer_id of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._sub_customer_id

    @sub_customer_id.setter
    def sub_customer_id(self, sub_customer_id):
        """Sets the sub_customer_id of this ListCustomerBillsFeeRecordsRequest.

        企业子账号ID。 说明： 如果method取值不为sub_customer，则该参数无效。如果method取值为sub_customer，则该参数不能为空。

        :param sub_customer_id: The sub_customer_id of this ListCustomerBillsFeeRecordsRequest.
        :type sub_customer_id: str
        """
        self._sub_customer_id = sub_customer_id

    @property
    def offset(self):
        """Gets the offset of this ListCustomerBillsFeeRecordsRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this ListCustomerBillsFeeRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCustomerBillsFeeRecordsRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this ListCustomerBillsFeeRecordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListCustomerBillsFeeRecordsRequest.

        页面大小。默认值为10。

        :return: The limit of this ListCustomerBillsFeeRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCustomerBillsFeeRecordsRequest.

        页面大小。默认值为10。

        :param limit: The limit of this ListCustomerBillsFeeRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def bill_date_begin(self):
        """Gets the bill_date_begin of this ListCustomerBillsFeeRecordsRequest.

        查询的流水账单的开始日期，东八区时间，格式为YYYY-MM-DD。此参数不携带或携带值为空时，不作为筛选条件。 说明： 必须和bill_cycle（即流水账单的所在账期）在同一个月。bill_date_begin和bill_date_end两个参数必须同时出现，否则仅按照bill_cycle（即流水账单的所在账期）进行查询。

        :return: The bill_date_begin of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._bill_date_begin

    @bill_date_begin.setter
    def bill_date_begin(self, bill_date_begin):
        """Sets the bill_date_begin of this ListCustomerBillsFeeRecordsRequest.

        查询的流水账单的开始日期，东八区时间，格式为YYYY-MM-DD。此参数不携带或携带值为空时，不作为筛选条件。 说明： 必须和bill_cycle（即流水账单的所在账期）在同一个月。bill_date_begin和bill_date_end两个参数必须同时出现，否则仅按照bill_cycle（即流水账单的所在账期）进行查询。

        :param bill_date_begin: The bill_date_begin of this ListCustomerBillsFeeRecordsRequest.
        :type bill_date_begin: str
        """
        self._bill_date_begin = bill_date_begin

    @property
    def bill_date_end(self):
        """Gets the bill_date_end of this ListCustomerBillsFeeRecordsRequest.

        查询的流水账单的结束日期，东八区时间，格式为YYYY-MM-DD。此参数不携带或携带值为空时，不作为筛选条件。 说明： 必须和bill_cycle（即流水账单的所在账期）在同一个月。bill_date_begin和bill_date_end两个参数必须同时出现，否则仅按照bill_cycle（即流水账单的所在账期）进行查询。

        :return: The bill_date_end of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._bill_date_end

    @bill_date_end.setter
    def bill_date_end(self, bill_date_end):
        """Sets the bill_date_end of this ListCustomerBillsFeeRecordsRequest.

        查询的流水账单的结束日期，东八区时间，格式为YYYY-MM-DD。此参数不携带或携带值为空时，不作为筛选条件。 说明： 必须和bill_cycle（即流水账单的所在账期）在同一个月。bill_date_begin和bill_date_end两个参数必须同时出现，否则仅按照bill_cycle（即流水账单的所在账期）进行查询。

        :param bill_date_end: The bill_date_end of this ListCustomerBillsFeeRecordsRequest.
        :type bill_date_end: str
        """
        self._bill_date_end = bill_date_end

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
        if not isinstance(other, ListCustomerBillsFeeRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
