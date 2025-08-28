# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubCustomerBillDetailRequest:

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
        'customer_id': 'str',
        'service_type_code': 'str',
        'region_code': 'str',
        'charging_mode': 'int',
        'bill_detail_type': 'int',
        'resource_id': 'str',
        'resource_name': 'str',
        'trade_id': 'str',
        'account_manager_id': 'str',
        'association_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'indirect_partner_id': 'str',
        'bill_date_begin': 'str',
        'bill_date_end': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'bill_cycle': 'bill_cycle',
        'customer_id': 'customer_id',
        'service_type_code': 'service_type_code',
        'region_code': 'region_code',
        'charging_mode': 'charging_mode',
        'bill_detail_type': 'bill_detail_type',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'trade_id': 'trade_id',
        'account_manager_id': 'account_manager_id',
        'association_type': 'association_type',
        'offset': 'offset',
        'limit': 'limit',
        'indirect_partner_id': 'indirect_partner_id',
        'bill_date_begin': 'bill_date_begin',
        'bill_date_end': 'bill_date_end'
    }

    def __init__(self, x_language=None, bill_cycle=None, customer_id=None, service_type_code=None, region_code=None, charging_mode=None, bill_detail_type=None, resource_id=None, resource_name=None, trade_id=None, account_manager_id=None, association_type=None, offset=None, limit=None, indirect_partner_id=None, bill_date_begin=None, bill_date_end=None):
        r"""ListSubCustomerBillDetailRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。忽略大小写，默认 zh_cn：中文 en_us：英文
        :type x_language: str
        :param bill_cycle: 账期所在月份。格式：YYYY-MM
        :type bill_cycle: str
        :param customer_id: 客户账号ID。您可以调用[查询客户列表](https://support.huaweicloud.com/api-bpconsole/mc_00021.html)接口获取customer_id。
        :type customer_id: str
        :param service_type_code: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用[查询云服务类型列表](https://support.huaweicloud.com/api-bpconsole/zh-cn_topic_0000001256679455.html)接口获取。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串或携带值为null时，作为筛选条件。
        :type service_type_code: str
        :param region_code: 云服务区编码，例如：“cn-north-1”。具体请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)对应云服务的“区域”列的值。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串或携带值为null时，作为筛选条件。
        :type region_code: str
        :param charging_mode: 计费模式。1：包周期3：按需10：预留实例11：节省计划此参数不携带或携带值为空或携带为null时，默认查询所有计费模式下的消费记录；不支持携带值为空串。
        :type charging_mode: int
        :param bill_detail_type: 账单类型。1：消费-新购 2：消费-续订 3：消费-变更 4：退款-退订 5：消费-使用 8：消费-自动续订 9：调账-补偿 14：消费-服务支持计划月末扣费 16：调账-扣费 18：消费-按月付费 20：退款-变更 23：消费-节省计划抵扣 24：退款-包年/包月转按需 25：消费-抹零补扣 103：消费-按年付费 此参数不携带或携带值为空或携带值为null时，不作为筛选条件；不支持携带值为空串。
        :type bill_detail_type: int
        :param resource_id: 资源标识。此参数不携带或携带值为空时，不作为筛选条件；携带值为null时，作为筛选条件；不支持携带值为空串。
        :type resource_id: str
        :param resource_name: 资源名称。此参数不携带或携带值为空时，不作为筛选条件；携带值为null时，作为筛选条件；不支持携带值为空串。
        :type resource_name: str
        :param trade_id: 订单ID或交易ID，扣费维度的唯一标识。账单类型为1，2，3，4，8时为订单ID。其它场景下为交易ID。非月末扣费：应收ID月末扣费：账单ID 此参数不携带或携带值为空时，不作为筛选条件；携带值为null时，作为筛选条件；不支持携带值为空串。
        :type trade_id: str
        :param account_manager_id: 客户经理标识。此参数不携带或携带值为空时，不作为筛选条件；携带值为null时，作为筛选条件；不支持携带值为空串。
        :type account_manager_id: str
        :param association_type: 子客户的关联类型：1：顾问销售2：代售 此参数不携带或携带值为空时，不作为筛选条件；不支持携带为null和空串。
        :type association_type: str
        :param offset: 偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 每次查询的数量限制。默认值为10。
        :type limit: int
        :param indirect_partner_id: 云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。  说明： 华为云总经销商可以查询名下所有子客户消费（包括云经销商子客户）。如果是普通经销商，那么此处可以为空。如果华为云总经销商需要查询客户在云经销商关联期间的消费，需要携带该字段；除此之外，此参数不做处理。否则只能查询该客户在与自己关联期间的消费。
        :type indirect_partner_id: str
        :param bill_date_begin: 查询的资源消费记录的开始日期，格式为YYYY-MM-DD。此参数不携带或携带值为空时，不作为筛选条件；不支持携带值为空串。 说明： 必须和bill_cycle（即资源的消费账期）在同一个月。bill_date_begin需小于等于bill_date_end。
        :type bill_date_begin: str
        :param bill_date_end: 查询的资源消费记录的结束日期，格式为YYYY-MM-DD。此参数不携带或携带值为空时，不作为筛选条件；不支持携带值为空串。 说明： 必须和bill_cycle（即资源的消费账期）在同一个月。bill_date_begin和bill_date_end两个参数必须同时出现，否则仅按照bill_cycle（即资源的消费账期）进行查询。bill_date_begin需小于等于bill_date_end。
        :type bill_date_end: str
        """
        
        

        self._x_language = None
        self._bill_cycle = None
        self._customer_id = None
        self._service_type_code = None
        self._region_code = None
        self._charging_mode = None
        self._bill_detail_type = None
        self._resource_id = None
        self._resource_name = None
        self._trade_id = None
        self._account_manager_id = None
        self._association_type = None
        self._offset = None
        self._limit = None
        self._indirect_partner_id = None
        self._bill_date_begin = None
        self._bill_date_end = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.bill_cycle = bill_cycle
        self.customer_id = customer_id
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if region_code is not None:
            self.region_code = region_code
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if bill_detail_type is not None:
            self.bill_detail_type = bill_detail_type
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if trade_id is not None:
            self.trade_id = trade_id
        if account_manager_id is not None:
            self.account_manager_id = account_manager_id
        if association_type is not None:
            self.association_type = association_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id
        if bill_date_begin is not None:
            self.bill_date_begin = bill_date_begin
        if bill_date_end is not None:
            self.bill_date_end = bill_date_end

    @property
    def x_language(self):
        r"""Gets the x_language of this ListSubCustomerBillDetailRequest.

        语言。忽略大小写，默认 zh_cn：中文 en_us：英文

        :return: The x_language of this ListSubCustomerBillDetailRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListSubCustomerBillDetailRequest.

        语言。忽略大小写，默认 zh_cn：中文 en_us：英文

        :param x_language: The x_language of this ListSubCustomerBillDetailRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def bill_cycle(self):
        r"""Gets the bill_cycle of this ListSubCustomerBillDetailRequest.

        账期所在月份。格式：YYYY-MM

        :return: The bill_cycle of this ListSubCustomerBillDetailRequest.
        :rtype: str
        """
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, bill_cycle):
        r"""Sets the bill_cycle of this ListSubCustomerBillDetailRequest.

        账期所在月份。格式：YYYY-MM

        :param bill_cycle: The bill_cycle of this ListSubCustomerBillDetailRequest.
        :type bill_cycle: str
        """
        self._bill_cycle = bill_cycle

    @property
    def customer_id(self):
        r"""Gets the customer_id of this ListSubCustomerBillDetailRequest.

        客户账号ID。您可以调用[查询客户列表](https://support.huaweicloud.com/api-bpconsole/mc_00021.html)接口获取customer_id。

        :return: The customer_id of this ListSubCustomerBillDetailRequest.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this ListSubCustomerBillDetailRequest.

        客户账号ID。您可以调用[查询客户列表](https://support.huaweicloud.com/api-bpconsole/mc_00021.html)接口获取customer_id。

        :param customer_id: The customer_id of this ListSubCustomerBillDetailRequest.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def service_type_code(self):
        r"""Gets the service_type_code of this ListSubCustomerBillDetailRequest.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用[查询云服务类型列表](https://support.huaweicloud.com/api-bpconsole/zh-cn_topic_0000001256679455.html)接口获取。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串或携带值为null时，作为筛选条件。

        :return: The service_type_code of this ListSubCustomerBillDetailRequest.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        r"""Sets the service_type_code of this ListSubCustomerBillDetailRequest.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用[查询云服务类型列表](https://support.huaweicloud.com/api-bpconsole/zh-cn_topic_0000001256679455.html)接口获取。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串或携带值为null时，作为筛选条件。

        :param service_type_code: The service_type_code of this ListSubCustomerBillDetailRequest.
        :type service_type_code: str
        """
        self._service_type_code = service_type_code

    @property
    def region_code(self):
        r"""Gets the region_code of this ListSubCustomerBillDetailRequest.

        云服务区编码，例如：“cn-north-1”。具体请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)对应云服务的“区域”列的值。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串或携带值为null时，作为筛选条件。

        :return: The region_code of this ListSubCustomerBillDetailRequest.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        r"""Sets the region_code of this ListSubCustomerBillDetailRequest.

        云服务区编码，例如：“cn-north-1”。具体请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)对应云服务的“区域”列的值。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串或携带值为null时，作为筛选条件。

        :param region_code: The region_code of this ListSubCustomerBillDetailRequest.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ListSubCustomerBillDetailRequest.

        计费模式。1：包周期3：按需10：预留实例11：节省计划此参数不携带或携带值为空或携带为null时，默认查询所有计费模式下的消费记录；不支持携带值为空串。

        :return: The charging_mode of this ListSubCustomerBillDetailRequest.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ListSubCustomerBillDetailRequest.

        计费模式。1：包周期3：按需10：预留实例11：节省计划此参数不携带或携带值为空或携带为null时，默认查询所有计费模式下的消费记录；不支持携带值为空串。

        :param charging_mode: The charging_mode of this ListSubCustomerBillDetailRequest.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def bill_detail_type(self):
        r"""Gets the bill_detail_type of this ListSubCustomerBillDetailRequest.

        账单类型。1：消费-新购 2：消费-续订 3：消费-变更 4：退款-退订 5：消费-使用 8：消费-自动续订 9：调账-补偿 14：消费-服务支持计划月末扣费 16：调账-扣费 18：消费-按月付费 20：退款-变更 23：消费-节省计划抵扣 24：退款-包年/包月转按需 25：消费-抹零补扣 103：消费-按年付费 此参数不携带或携带值为空或携带值为null时，不作为筛选条件；不支持携带值为空串。

        :return: The bill_detail_type of this ListSubCustomerBillDetailRequest.
        :rtype: int
        """
        return self._bill_detail_type

    @bill_detail_type.setter
    def bill_detail_type(self, bill_detail_type):
        r"""Sets the bill_detail_type of this ListSubCustomerBillDetailRequest.

        账单类型。1：消费-新购 2：消费-续订 3：消费-变更 4：退款-退订 5：消费-使用 8：消费-自动续订 9：调账-补偿 14：消费-服务支持计划月末扣费 16：调账-扣费 18：消费-按月付费 20：退款-变更 23：消费-节省计划抵扣 24：退款-包年/包月转按需 25：消费-抹零补扣 103：消费-按年付费 此参数不携带或携带值为空或携带值为null时，不作为筛选条件；不支持携带值为空串。

        :param bill_detail_type: The bill_detail_type of this ListSubCustomerBillDetailRequest.
        :type bill_detail_type: int
        """
        self._bill_detail_type = bill_detail_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListSubCustomerBillDetailRequest.

        资源标识。此参数不携带或携带值为空时，不作为筛选条件；携带值为null时，作为筛选条件；不支持携带值为空串。

        :return: The resource_id of this ListSubCustomerBillDetailRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListSubCustomerBillDetailRequest.

        资源标识。此参数不携带或携带值为空时，不作为筛选条件；携带值为null时，作为筛选条件；不支持携带值为空串。

        :param resource_id: The resource_id of this ListSubCustomerBillDetailRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ListSubCustomerBillDetailRequest.

        资源名称。此参数不携带或携带值为空时，不作为筛选条件；携带值为null时，作为筛选条件；不支持携带值为空串。

        :return: The resource_name of this ListSubCustomerBillDetailRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ListSubCustomerBillDetailRequest.

        资源名称。此参数不携带或携带值为空时，不作为筛选条件；携带值为null时，作为筛选条件；不支持携带值为空串。

        :param resource_name: The resource_name of this ListSubCustomerBillDetailRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def trade_id(self):
        r"""Gets the trade_id of this ListSubCustomerBillDetailRequest.

        订单ID或交易ID，扣费维度的唯一标识。账单类型为1，2，3，4，8时为订单ID。其它场景下为交易ID。非月末扣费：应收ID月末扣费：账单ID 此参数不携带或携带值为空时，不作为筛选条件；携带值为null时，作为筛选条件；不支持携带值为空串。

        :return: The trade_id of this ListSubCustomerBillDetailRequest.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        r"""Sets the trade_id of this ListSubCustomerBillDetailRequest.

        订单ID或交易ID，扣费维度的唯一标识。账单类型为1，2，3，4，8时为订单ID。其它场景下为交易ID。非月末扣费：应收ID月末扣费：账单ID 此参数不携带或携带值为空时，不作为筛选条件；携带值为null时，作为筛选条件；不支持携带值为空串。

        :param trade_id: The trade_id of this ListSubCustomerBillDetailRequest.
        :type trade_id: str
        """
        self._trade_id = trade_id

    @property
    def account_manager_id(self):
        r"""Gets the account_manager_id of this ListSubCustomerBillDetailRequest.

        客户经理标识。此参数不携带或携带值为空时，不作为筛选条件；携带值为null时，作为筛选条件；不支持携带值为空串。

        :return: The account_manager_id of this ListSubCustomerBillDetailRequest.
        :rtype: str
        """
        return self._account_manager_id

    @account_manager_id.setter
    def account_manager_id(self, account_manager_id):
        r"""Sets the account_manager_id of this ListSubCustomerBillDetailRequest.

        客户经理标识。此参数不携带或携带值为空时，不作为筛选条件；携带值为null时，作为筛选条件；不支持携带值为空串。

        :param account_manager_id: The account_manager_id of this ListSubCustomerBillDetailRequest.
        :type account_manager_id: str
        """
        self._account_manager_id = account_manager_id

    @property
    def association_type(self):
        r"""Gets the association_type of this ListSubCustomerBillDetailRequest.

        子客户的关联类型：1：顾问销售2：代售 此参数不携带或携带值为空时，不作为筛选条件；不支持携带为null和空串。

        :return: The association_type of this ListSubCustomerBillDetailRequest.
        :rtype: str
        """
        return self._association_type

    @association_type.setter
    def association_type(self, association_type):
        r"""Sets the association_type of this ListSubCustomerBillDetailRequest.

        子客户的关联类型：1：顾问销售2：代售 此参数不携带或携带值为空时，不作为筛选条件；不支持携带为null和空串。

        :param association_type: The association_type of this ListSubCustomerBillDetailRequest.
        :type association_type: str
        """
        self._association_type = association_type

    @property
    def offset(self):
        r"""Gets the offset of this ListSubCustomerBillDetailRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this ListSubCustomerBillDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSubCustomerBillDetailRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this ListSubCustomerBillDetailRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSubCustomerBillDetailRequest.

        每次查询的数量限制。默认值为10。

        :return: The limit of this ListSubCustomerBillDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSubCustomerBillDetailRequest.

        每次查询的数量限制。默认值为10。

        :param limit: The limit of this ListSubCustomerBillDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def indirect_partner_id(self):
        r"""Gets the indirect_partner_id of this ListSubCustomerBillDetailRequest.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。  说明： 华为云总经销商可以查询名下所有子客户消费（包括云经销商子客户）。如果是普通经销商，那么此处可以为空。如果华为云总经销商需要查询客户在云经销商关联期间的消费，需要携带该字段；除此之外，此参数不做处理。否则只能查询该客户在与自己关联期间的消费。

        :return: The indirect_partner_id of this ListSubCustomerBillDetailRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        r"""Sets the indirect_partner_id of this ListSubCustomerBillDetailRequest.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。  说明： 华为云总经销商可以查询名下所有子客户消费（包括云经销商子客户）。如果是普通经销商，那么此处可以为空。如果华为云总经销商需要查询客户在云经销商关联期间的消费，需要携带该字段；除此之外，此参数不做处理。否则只能查询该客户在与自己关联期间的消费。

        :param indirect_partner_id: The indirect_partner_id of this ListSubCustomerBillDetailRequest.
        :type indirect_partner_id: str
        """
        self._indirect_partner_id = indirect_partner_id

    @property
    def bill_date_begin(self):
        r"""Gets the bill_date_begin of this ListSubCustomerBillDetailRequest.

        查询的资源消费记录的开始日期，格式为YYYY-MM-DD。此参数不携带或携带值为空时，不作为筛选条件；不支持携带值为空串。 说明： 必须和bill_cycle（即资源的消费账期）在同一个月。bill_date_begin需小于等于bill_date_end。

        :return: The bill_date_begin of this ListSubCustomerBillDetailRequest.
        :rtype: str
        """
        return self._bill_date_begin

    @bill_date_begin.setter
    def bill_date_begin(self, bill_date_begin):
        r"""Sets the bill_date_begin of this ListSubCustomerBillDetailRequest.

        查询的资源消费记录的开始日期，格式为YYYY-MM-DD。此参数不携带或携带值为空时，不作为筛选条件；不支持携带值为空串。 说明： 必须和bill_cycle（即资源的消费账期）在同一个月。bill_date_begin需小于等于bill_date_end。

        :param bill_date_begin: The bill_date_begin of this ListSubCustomerBillDetailRequest.
        :type bill_date_begin: str
        """
        self._bill_date_begin = bill_date_begin

    @property
    def bill_date_end(self):
        r"""Gets the bill_date_end of this ListSubCustomerBillDetailRequest.

        查询的资源消费记录的结束日期，格式为YYYY-MM-DD。此参数不携带或携带值为空时，不作为筛选条件；不支持携带值为空串。 说明： 必须和bill_cycle（即资源的消费账期）在同一个月。bill_date_begin和bill_date_end两个参数必须同时出现，否则仅按照bill_cycle（即资源的消费账期）进行查询。bill_date_begin需小于等于bill_date_end。

        :return: The bill_date_end of this ListSubCustomerBillDetailRequest.
        :rtype: str
        """
        return self._bill_date_end

    @bill_date_end.setter
    def bill_date_end(self, bill_date_end):
        r"""Sets the bill_date_end of this ListSubCustomerBillDetailRequest.

        查询的资源消费记录的结束日期，格式为YYYY-MM-DD。此参数不携带或携带值为空时，不作为筛选条件；不支持携带值为空串。 说明： 必须和bill_cycle（即资源的消费账期）在同一个月。bill_date_begin和bill_date_end两个参数必须同时出现，否则仅按照bill_cycle（即资源的消费账期）进行查询。bill_date_begin需小于等于bill_date_end。

        :param bill_date_end: The bill_date_end of this ListSubCustomerBillDetailRequest.
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
        if not isinstance(other, ListSubCustomerBillDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
