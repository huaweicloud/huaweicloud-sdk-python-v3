# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomerselfResourceRecordsRequest:

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
        'cycle': 'str',
        'cloud_service_type': 'str',
        'region': 'str',
        'charge_mode': 'str',
        'bill_type': 'int',
        'offset': 'int',
        'limit': 'int',
        'resource_id': 'str',
        'enterprise_project_id': 'str',
        'include_zero_record': 'bool',
        'method': 'str',
        'sub_customer_id': 'str',
        'trade_id': 'str',
        'bill_date_begin': 'str',
        'bill_date_end': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'cycle': 'cycle',
        'cloud_service_type': 'cloud_service_type',
        'region': 'region',
        'charge_mode': 'charge_mode',
        'bill_type': 'bill_type',
        'offset': 'offset',
        'limit': 'limit',
        'resource_id': 'resource_id',
        'enterprise_project_id': 'enterprise_project_id',
        'include_zero_record': 'include_zero_record',
        'method': 'method',
        'sub_customer_id': 'sub_customer_id',
        'trade_id': 'trade_id',
        'bill_date_begin': 'bill_date_begin',
        'bill_date_end': 'bill_date_end'
    }

    def __init__(self, x_language=None, cycle=None, cloud_service_type=None, region=None, charge_mode=None, bill_type=None, offset=None, limit=None, resource_id=None, enterprise_project_id=None, include_zero_record=None, method=None, sub_customer_id=None, trade_id=None, bill_date_begin=None, bill_date_end=None):
        """ListCustomerselfResourceRecordsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言：中文：zh_CN 英文：en_US。缺省为zh_CN
        :type x_language: str
        :param cycle: 查询的资源消费记录所在账期，东八区时间，格式：YYYY-MM。
        :type cycle: str
        :param cloud_service_type: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用[查询云服务类型列表](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001256679455.html)接口获取。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。
        :type cloud_service_type: str
        :param region: 云服务区编码，例如：“cn-north-1”。具体请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)对应云服务的“区域”列的值。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。
        :type region: str
        :param charge_mode: 计费模式。1：包年/包月3：按需10：预留实例 此参数不携带时，不作为筛选条件。
        :type charge_mode: str
        :param bill_type: 账单类型。1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费16：调账-扣费18：消费-按月付费20：退款-变更此参数不携带或携带值为空时，不作为筛选条件。
        :type bill_type: int
        :param offset: 偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 每次查询的数量限制。默认值为10。
        :type limit: int
        :param resource_id: 资源ID。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。
        :type resource_id: str
        :param enterprise_project_id: 企业项目标识（企业项目ID）。default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。
        :type enterprise_project_id: str
        :param include_zero_record: 返回是否包含应付金额为0的记录。true：包含false：不包含 此参数不携带或携带值为空时，不作为筛选条件。
        :type include_zero_record: bool
        :param method: 查询资源消费记录的方式。oneself：客户自己sub_customer：企业子客户all：客户自己和企业子客户 此参数不携带或携带值为空时，默认值为“all”，如果没有企业子客户，取值为all时查询的是客户自己的资源消费记录。
        :type method: str
        :param sub_customer_id: 企业子账号ID。此参数携带值为空串时，不作为筛选条件。 说明： 如果method取值不为sub_customer，则该参数无效。如果method取值为sub_customer，则该参数不能为空。
        :type sub_customer_id: str
        :param trade_id: 订单ID或交易ID。账单类型为1、2、3、4和8时此处为订单ID。账单类型为其它场景时此处为交易ID，为扣费维度的唯一标识。例如非月末扣费时为应收ID；月末扣费时为账单ID。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。
        :type trade_id: str
        :param bill_date_begin: 查询的资源消费记录的开始日期，东八区时间，格式为YYYY-MM-DD。此参数不携带或携带值为空或携带值为空串时，默认值取cycle月份的第一天。 说明： 必须和cycle（即资源的消费账期）在同一个月。bill_date_begin和bill_date_end两个参数必须同时出现，否则仅按照cycle（即资源的消费账期）进行查询。
        :type bill_date_begin: str
        :param bill_date_end: 查询的资源消费记录的结束日期，东八区时间，格式为YYYY-MM-DD。此参数不携带或携带值为空或携带值为空串时，默认值取cycle月份的最后一天。 说明： 必须和cycle（即资源的消费账期）在同一个月。bill_date_begin和bill_date_end两个参数必须同时出现，否则仅按照cycle（即资源的消费账期）进行查询。
        :type bill_date_end: str
        """
        
        

        self._x_language = None
        self._cycle = None
        self._cloud_service_type = None
        self._region = None
        self._charge_mode = None
        self._bill_type = None
        self._offset = None
        self._limit = None
        self._resource_id = None
        self._enterprise_project_id = None
        self._include_zero_record = None
        self._method = None
        self._sub_customer_id = None
        self._trade_id = None
        self._bill_date_begin = None
        self._bill_date_end = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.cycle = cycle
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if region is not None:
            self.region = region
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if bill_type is not None:
            self.bill_type = bill_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if resource_id is not None:
            self.resource_id = resource_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if include_zero_record is not None:
            self.include_zero_record = include_zero_record
        if method is not None:
            self.method = method
        if sub_customer_id is not None:
            self.sub_customer_id = sub_customer_id
        if trade_id is not None:
            self.trade_id = trade_id
        if bill_date_begin is not None:
            self.bill_date_begin = bill_date_begin
        if bill_date_end is not None:
            self.bill_date_end = bill_date_end

    @property
    def x_language(self):
        """Gets the x_language of this ListCustomerselfResourceRecordsRequest.

        语言：中文：zh_CN 英文：en_US。缺省为zh_CN

        :return: The x_language of this ListCustomerselfResourceRecordsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListCustomerselfResourceRecordsRequest.

        语言：中文：zh_CN 英文：en_US。缺省为zh_CN

        :param x_language: The x_language of this ListCustomerselfResourceRecordsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def cycle(self):
        """Gets the cycle of this ListCustomerselfResourceRecordsRequest.

        查询的资源消费记录所在账期，东八区时间，格式：YYYY-MM。

        :return: The cycle of this ListCustomerselfResourceRecordsRequest.
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this ListCustomerselfResourceRecordsRequest.

        查询的资源消费记录所在账期，东八区时间，格式：YYYY-MM。

        :param cycle: The cycle of this ListCustomerselfResourceRecordsRequest.
        :type cycle: str
        """
        self._cycle = cycle

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this ListCustomerselfResourceRecordsRequest.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用[查询云服务类型列表](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001256679455.html)接口获取。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。

        :return: The cloud_service_type of this ListCustomerselfResourceRecordsRequest.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this ListCustomerselfResourceRecordsRequest.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用[查询云服务类型列表](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001256679455.html)接口获取。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。

        :param cloud_service_type: The cloud_service_type of this ListCustomerselfResourceRecordsRequest.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def region(self):
        """Gets the region of this ListCustomerselfResourceRecordsRequest.

        云服务区编码，例如：“cn-north-1”。具体请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)对应云服务的“区域”列的值。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。

        :return: The region of this ListCustomerselfResourceRecordsRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListCustomerselfResourceRecordsRequest.

        云服务区编码，例如：“cn-north-1”。具体请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)对应云服务的“区域”列的值。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。

        :param region: The region of this ListCustomerselfResourceRecordsRequest.
        :type region: str
        """
        self._region = region

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ListCustomerselfResourceRecordsRequest.

        计费模式。1：包年/包月3：按需10：预留实例 此参数不携带时，不作为筛选条件。

        :return: The charge_mode of this ListCustomerselfResourceRecordsRequest.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ListCustomerselfResourceRecordsRequest.

        计费模式。1：包年/包月3：按需10：预留实例 此参数不携带时，不作为筛选条件。

        :param charge_mode: The charge_mode of this ListCustomerselfResourceRecordsRequest.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def bill_type(self):
        """Gets the bill_type of this ListCustomerselfResourceRecordsRequest.

        账单类型。1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费16：调账-扣费18：消费-按月付费20：退款-变更此参数不携带或携带值为空时，不作为筛选条件。

        :return: The bill_type of this ListCustomerselfResourceRecordsRequest.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this ListCustomerselfResourceRecordsRequest.

        账单类型。1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费16：调账-扣费18：消费-按月付费20：退款-变更此参数不携带或携带值为空时，不作为筛选条件。

        :param bill_type: The bill_type of this ListCustomerselfResourceRecordsRequest.
        :type bill_type: int
        """
        self._bill_type = bill_type

    @property
    def offset(self):
        """Gets the offset of this ListCustomerselfResourceRecordsRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this ListCustomerselfResourceRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCustomerselfResourceRecordsRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this ListCustomerselfResourceRecordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListCustomerselfResourceRecordsRequest.

        每次查询的数量限制。默认值为10。

        :return: The limit of this ListCustomerselfResourceRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCustomerselfResourceRecordsRequest.

        每次查询的数量限制。默认值为10。

        :param limit: The limit of this ListCustomerselfResourceRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def resource_id(self):
        """Gets the resource_id of this ListCustomerselfResourceRecordsRequest.

        资源ID。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。

        :return: The resource_id of this ListCustomerselfResourceRecordsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListCustomerselfResourceRecordsRequest.

        资源ID。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。

        :param resource_id: The resource_id of this ListCustomerselfResourceRecordsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListCustomerselfResourceRecordsRequest.

        企业项目标识（企业项目ID）。default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。

        :return: The enterprise_project_id of this ListCustomerselfResourceRecordsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListCustomerselfResourceRecordsRequest.

        企业项目标识（企业项目ID）。default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。

        :param enterprise_project_id: The enterprise_project_id of this ListCustomerselfResourceRecordsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def include_zero_record(self):
        """Gets the include_zero_record of this ListCustomerselfResourceRecordsRequest.

        返回是否包含应付金额为0的记录。true：包含false：不包含 此参数不携带或携带值为空时，不作为筛选条件。

        :return: The include_zero_record of this ListCustomerselfResourceRecordsRequest.
        :rtype: bool
        """
        return self._include_zero_record

    @include_zero_record.setter
    def include_zero_record(self, include_zero_record):
        """Sets the include_zero_record of this ListCustomerselfResourceRecordsRequest.

        返回是否包含应付金额为0的记录。true：包含false：不包含 此参数不携带或携带值为空时，不作为筛选条件。

        :param include_zero_record: The include_zero_record of this ListCustomerselfResourceRecordsRequest.
        :type include_zero_record: bool
        """
        self._include_zero_record = include_zero_record

    @property
    def method(self):
        """Gets the method of this ListCustomerselfResourceRecordsRequest.

        查询资源消费记录的方式。oneself：客户自己sub_customer：企业子客户all：客户自己和企业子客户 此参数不携带或携带值为空时，默认值为“all”，如果没有企业子客户，取值为all时查询的是客户自己的资源消费记录。

        :return: The method of this ListCustomerselfResourceRecordsRequest.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ListCustomerselfResourceRecordsRequest.

        查询资源消费记录的方式。oneself：客户自己sub_customer：企业子客户all：客户自己和企业子客户 此参数不携带或携带值为空时，默认值为“all”，如果没有企业子客户，取值为all时查询的是客户自己的资源消费记录。

        :param method: The method of this ListCustomerselfResourceRecordsRequest.
        :type method: str
        """
        self._method = method

    @property
    def sub_customer_id(self):
        """Gets the sub_customer_id of this ListCustomerselfResourceRecordsRequest.

        企业子账号ID。此参数携带值为空串时，不作为筛选条件。 说明： 如果method取值不为sub_customer，则该参数无效。如果method取值为sub_customer，则该参数不能为空。

        :return: The sub_customer_id of this ListCustomerselfResourceRecordsRequest.
        :rtype: str
        """
        return self._sub_customer_id

    @sub_customer_id.setter
    def sub_customer_id(self, sub_customer_id):
        """Sets the sub_customer_id of this ListCustomerselfResourceRecordsRequest.

        企业子账号ID。此参数携带值为空串时，不作为筛选条件。 说明： 如果method取值不为sub_customer，则该参数无效。如果method取值为sub_customer，则该参数不能为空。

        :param sub_customer_id: The sub_customer_id of this ListCustomerselfResourceRecordsRequest.
        :type sub_customer_id: str
        """
        self._sub_customer_id = sub_customer_id

    @property
    def trade_id(self):
        """Gets the trade_id of this ListCustomerselfResourceRecordsRequest.

        订单ID或交易ID。账单类型为1、2、3、4和8时此处为订单ID。账单类型为其它场景时此处为交易ID，为扣费维度的唯一标识。例如非月末扣费时为应收ID；月末扣费时为账单ID。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。

        :return: The trade_id of this ListCustomerselfResourceRecordsRequest.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        """Sets the trade_id of this ListCustomerselfResourceRecordsRequest.

        订单ID或交易ID。账单类型为1、2、3、4和8时此处为订单ID。账单类型为其它场景时此处为交易ID，为扣费维度的唯一标识。例如非月末扣费时为应收ID；月末扣费时为账单ID。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。

        :param trade_id: The trade_id of this ListCustomerselfResourceRecordsRequest.
        :type trade_id: str
        """
        self._trade_id = trade_id

    @property
    def bill_date_begin(self):
        """Gets the bill_date_begin of this ListCustomerselfResourceRecordsRequest.

        查询的资源消费记录的开始日期，东八区时间，格式为YYYY-MM-DD。此参数不携带或携带值为空或携带值为空串时，默认值取cycle月份的第一天。 说明： 必须和cycle（即资源的消费账期）在同一个月。bill_date_begin和bill_date_end两个参数必须同时出现，否则仅按照cycle（即资源的消费账期）进行查询。

        :return: The bill_date_begin of this ListCustomerselfResourceRecordsRequest.
        :rtype: str
        """
        return self._bill_date_begin

    @bill_date_begin.setter
    def bill_date_begin(self, bill_date_begin):
        """Sets the bill_date_begin of this ListCustomerselfResourceRecordsRequest.

        查询的资源消费记录的开始日期，东八区时间，格式为YYYY-MM-DD。此参数不携带或携带值为空或携带值为空串时，默认值取cycle月份的第一天。 说明： 必须和cycle（即资源的消费账期）在同一个月。bill_date_begin和bill_date_end两个参数必须同时出现，否则仅按照cycle（即资源的消费账期）进行查询。

        :param bill_date_begin: The bill_date_begin of this ListCustomerselfResourceRecordsRequest.
        :type bill_date_begin: str
        """
        self._bill_date_begin = bill_date_begin

    @property
    def bill_date_end(self):
        """Gets the bill_date_end of this ListCustomerselfResourceRecordsRequest.

        查询的资源消费记录的结束日期，东八区时间，格式为YYYY-MM-DD。此参数不携带或携带值为空或携带值为空串时，默认值取cycle月份的最后一天。 说明： 必须和cycle（即资源的消费账期）在同一个月。bill_date_begin和bill_date_end两个参数必须同时出现，否则仅按照cycle（即资源的消费账期）进行查询。

        :return: The bill_date_end of this ListCustomerselfResourceRecordsRequest.
        :rtype: str
        """
        return self._bill_date_end

    @bill_date_end.setter
    def bill_date_end(self, bill_date_end):
        """Sets the bill_date_end of this ListCustomerselfResourceRecordsRequest.

        查询的资源消费记录的结束日期，东八区时间，格式为YYYY-MM-DD。此参数不携带或携带值为空或携带值为空串时，默认值取cycle月份的最后一天。 说明： 必须和cycle（即资源的消费账期）在同一个月。bill_date_begin和bill_date_end两个参数必须同时出现，否则仅按照cycle（即资源的消费账期）进行查询。

        :param bill_date_end: The bill_date_end of this ListCustomerselfResourceRecordsRequest.
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
        if not isinstance(other, ListCustomerselfResourceRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
