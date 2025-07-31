# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryResRecordsDetailReq:

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
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'region': 'str',
        'res_instance_id': 'str',
        'charge_mode': 'int',
        'bill_type': 'int',
        'enterprise_project_id': 'str',
        'include_zero_record': 'bool',
        'offset': 'int',
        'limit': 'int',
        'method': 'str',
        'sub_customer_id': 'str',
        'statistic_type': 'int',
        'query_type': 'str',
        'bill_cycle_begin': 'str',
        'bill_cycle_end': 'str',
        'payer_account_id': 'str'
    }

    attribute_map = {
        'cycle': 'cycle',
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'region': 'region',
        'res_instance_id': 'res_instance_id',
        'charge_mode': 'charge_mode',
        'bill_type': 'bill_type',
        'enterprise_project_id': 'enterprise_project_id',
        'include_zero_record': 'include_zero_record',
        'offset': 'offset',
        'limit': 'limit',
        'method': 'method',
        'sub_customer_id': 'sub_customer_id',
        'statistic_type': 'statistic_type',
        'query_type': 'query_type',
        'bill_cycle_begin': 'bill_cycle_begin',
        'bill_cycle_end': 'bill_cycle_end',
        'payer_account_id': 'payer_account_id'
    }

    def __init__(self, cycle=None, cloud_service_type=None, resource_type=None, region=None, res_instance_id=None, charge_mode=None, bill_type=None, enterprise_project_id=None, include_zero_record=None, offset=None, limit=None, method=None, sub_customer_id=None, statistic_type=None, query_type=None, bill_cycle_begin=None, bill_cycle_end=None, payer_account_id=None):
        r"""QueryResRecordsDetailReq

        The model defined in huaweicloud sdk

        :param cycle: 查询的资源详单所在账期，东八区时间，格式为YYYY-MM。 示例：2019-01。  说明： 不支持2019年1月份之前的资源详单。
        :type cycle: str
        :param cloud_service_type: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type cloud_service_type: str
        :param resource_type: 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type resource_type: str
        :param region: 云服务区编码，例如：“ap-southeast-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type region: str
        :param res_instance_id: 资源实例ID。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type res_instance_id: str
        :param charge_mode: 计费模式。 1 : 包年/包月3：按需10：预留实例11：节省计划。 此参数不携带或者携带值为null时，返回所有计费模式的资源详单数据记录。
        :type charge_mode: int
        :param bill_type: 账单类型： 1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费15：消费-税金16：调账-扣费17：消费-保底差额 说明： 保底差额&#x3D;客户签约保底合同后，如果没有达到保底消费，客户需要补交的费用，仅限于直销或者伙伴顾问销售类子客户，且为后付费用户。 18：消费-按月付费20：退款-变更100：退款-退订税金23：消费-节省计划抵扣 24：退款-包年/包月转按需101：调账-补偿税金102：调账-扣费税金 此参数不携带或者携带值为null时，返回所有账单类型的资源详单数据记录。
        :type bill_type: int
        :param enterprise_project_id: 企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type enterprise_project_id: str
        :param include_zero_record: 返回是否包含应付金额为0的记录。 true: 包含false: 不包含 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type include_zero_record: bool
        :param offset: 偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 页面大小。默认值为10。
        :type limit: int
        :param method: 查询方式。 oneself：客户自己sub_customer：企业子客户all：客户自己和企业子客户 此参数不携带或携带值为空串或携带值为null时，默认值为“all”，如果没有企业子客户，all的时候也是查询客户自己的数据。
        :type method: str
        :param sub_customer_id: 企业子账号ID。  说明： 如果method取值不为sub_customer，则此参数无效。如果method取值为sub_customer，则此参数不能为空。
        :type sub_customer_id: str
        :param statistic_type: 统计类型。默认值为1。 1：按账期2：按天3：按明细
        :type statistic_type: int
        :param query_type: |参数名称：查询类型。默认值为BILLCYCLE。| |参数的约束及描述：默认值为BILLCYCLE。BILLCYCLE：按月 DAILY：按天 仅当statistic_type&#x3D;2或3时，支持传递query_type&#x3D;DAILY。该参数不携带或携带值为null或携带为空串时，取默认值BILLCYCLE。|
        :type query_type: str
        :param bill_cycle_begin: |账期开始时间。格式为YYYY-MM-DD。| |参数的约束及描述：仅当query_type&#x3D;DAILY时，必须传递账期开始时间。该参数不携带或携带值为null或携带为空串时，不作为筛选条件。|
        :type bill_cycle_begin: str
        :param bill_cycle_end: |参数名称：账期结束时间。格式为YYYY-MM-DD。| |参数的约束及描述：仅当query_type&#x3D;DAILY时，必须传递账期结束时间。该参数不携带或携带值为null或携带为空串时，不作为筛选条件。|
        :type bill_cycle_end: str
        :param payer_account_id: |参数名称：支付账号ID。| |参数的约束及描述：普通客户、财务独立企业子客户查询消费记录，只能查询到客户自己的消费记录，该参数不携带或携带为自身ID时，查询的都只是自身的消费记录； 企业主客户查询消费记录，不携带时，查询的是自身的、财务托管企业子、财务独立企业子的消费记录；入参自身ID时，查询的是自身的、财务托管企业子的消费记录；也可入参其名下财务独立企业子的客户ID，只查询该财务独立企业子的消费记录； 财务托管企业子查询消费记录，入参自身ID时，查询的是未与企业主关联时的消费记录；入参企业主客户ID时，查询的是与企业主关联后的消费记录；不携带时查询以上全部消费记录|
        :type payer_account_id: str
        """
        
        

        self._cycle = None
        self._cloud_service_type = None
        self._resource_type = None
        self._region = None
        self._res_instance_id = None
        self._charge_mode = None
        self._bill_type = None
        self._enterprise_project_id = None
        self._include_zero_record = None
        self._offset = None
        self._limit = None
        self._method = None
        self._sub_customer_id = None
        self._statistic_type = None
        self._query_type = None
        self._bill_cycle_begin = None
        self._bill_cycle_end = None
        self._payer_account_id = None
        self.discriminator = None

        self.cycle = cycle
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if resource_type is not None:
            self.resource_type = resource_type
        if region is not None:
            self.region = region
        if res_instance_id is not None:
            self.res_instance_id = res_instance_id
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if bill_type is not None:
            self.bill_type = bill_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if include_zero_record is not None:
            self.include_zero_record = include_zero_record
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if method is not None:
            self.method = method
        if sub_customer_id is not None:
            self.sub_customer_id = sub_customer_id
        if statistic_type is not None:
            self.statistic_type = statistic_type
        if query_type is not None:
            self.query_type = query_type
        if bill_cycle_begin is not None:
            self.bill_cycle_begin = bill_cycle_begin
        if bill_cycle_end is not None:
            self.bill_cycle_end = bill_cycle_end
        if payer_account_id is not None:
            self.payer_account_id = payer_account_id

    @property
    def cycle(self):
        r"""Gets the cycle of this QueryResRecordsDetailReq.

        查询的资源详单所在账期，东八区时间，格式为YYYY-MM。 示例：2019-01。  说明： 不支持2019年1月份之前的资源详单。

        :return: The cycle of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        r"""Sets the cycle of this QueryResRecordsDetailReq.

        查询的资源详单所在账期，东八区时间，格式为YYYY-MM。 示例：2019-01。  说明： 不支持2019年1月份之前的资源详单。

        :param cycle: The cycle of this QueryResRecordsDetailReq.
        :type cycle: str
        """
        self._cycle = cycle

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this QueryResRecordsDetailReq.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The cloud_service_type of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this QueryResRecordsDetailReq.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param cloud_service_type: The cloud_service_type of this QueryResRecordsDetailReq.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this QueryResRecordsDetailReq.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The resource_type of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this QueryResRecordsDetailReq.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param resource_type: The resource_type of this QueryResRecordsDetailReq.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def region(self):
        r"""Gets the region of this QueryResRecordsDetailReq.

        云服务区编码，例如：“ap-southeast-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The region of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this QueryResRecordsDetailReq.

        云服务区编码，例如：“ap-southeast-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param region: The region of this QueryResRecordsDetailReq.
        :type region: str
        """
        self._region = region

    @property
    def res_instance_id(self):
        r"""Gets the res_instance_id of this QueryResRecordsDetailReq.

        资源实例ID。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The res_instance_id of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._res_instance_id

    @res_instance_id.setter
    def res_instance_id(self, res_instance_id):
        r"""Sets the res_instance_id of this QueryResRecordsDetailReq.

        资源实例ID。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param res_instance_id: The res_instance_id of this QueryResRecordsDetailReq.
        :type res_instance_id: str
        """
        self._res_instance_id = res_instance_id

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this QueryResRecordsDetailReq.

        计费模式。 1 : 包年/包月3：按需10：预留实例11：节省计划。 此参数不携带或者携带值为null时，返回所有计费模式的资源详单数据记录。

        :return: The charge_mode of this QueryResRecordsDetailReq.
        :rtype: int
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this QueryResRecordsDetailReq.

        计费模式。 1 : 包年/包月3：按需10：预留实例11：节省计划。 此参数不携带或者携带值为null时，返回所有计费模式的资源详单数据记录。

        :param charge_mode: The charge_mode of this QueryResRecordsDetailReq.
        :type charge_mode: int
        """
        self._charge_mode = charge_mode

    @property
    def bill_type(self):
        r"""Gets the bill_type of this QueryResRecordsDetailReq.

        账单类型： 1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费15：消费-税金16：调账-扣费17：消费-保底差额 说明： 保底差额=客户签约保底合同后，如果没有达到保底消费，客户需要补交的费用，仅限于直销或者伙伴顾问销售类子客户，且为后付费用户。 18：消费-按月付费20：退款-变更100：退款-退订税金23：消费-节省计划抵扣 24：退款-包年/包月转按需101：调账-补偿税金102：调账-扣费税金 此参数不携带或者携带值为null时，返回所有账单类型的资源详单数据记录。

        :return: The bill_type of this QueryResRecordsDetailReq.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        r"""Sets the bill_type of this QueryResRecordsDetailReq.

        账单类型： 1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费15：消费-税金16：调账-扣费17：消费-保底差额 说明： 保底差额=客户签约保底合同后，如果没有达到保底消费，客户需要补交的费用，仅限于直销或者伙伴顾问销售类子客户，且为后付费用户。 18：消费-按月付费20：退款-变更100：退款-退订税金23：消费-节省计划抵扣 24：退款-包年/包月转按需101：调账-补偿税金102：调账-扣费税金 此参数不携带或者携带值为null时，返回所有账单类型的资源详单数据记录。

        :param bill_type: The bill_type of this QueryResRecordsDetailReq.
        :type bill_type: int
        """
        self._bill_type = bill_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this QueryResRecordsDetailReq.

        企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The enterprise_project_id of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this QueryResRecordsDetailReq.

        企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param enterprise_project_id: The enterprise_project_id of this QueryResRecordsDetailReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def include_zero_record(self):
        r"""Gets the include_zero_record of this QueryResRecordsDetailReq.

        返回是否包含应付金额为0的记录。 true: 包含false: 不包含 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The include_zero_record of this QueryResRecordsDetailReq.
        :rtype: bool
        """
        return self._include_zero_record

    @include_zero_record.setter
    def include_zero_record(self, include_zero_record):
        r"""Sets the include_zero_record of this QueryResRecordsDetailReq.

        返回是否包含应付金额为0的记录。 true: 包含false: 不包含 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param include_zero_record: The include_zero_record of this QueryResRecordsDetailReq.
        :type include_zero_record: bool
        """
        self._include_zero_record = include_zero_record

    @property
    def offset(self):
        r"""Gets the offset of this QueryResRecordsDetailReq.

        偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this QueryResRecordsDetailReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this QueryResRecordsDetailReq.

        偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this QueryResRecordsDetailReq.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this QueryResRecordsDetailReq.

        页面大小。默认值为10。

        :return: The limit of this QueryResRecordsDetailReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this QueryResRecordsDetailReq.

        页面大小。默认值为10。

        :param limit: The limit of this QueryResRecordsDetailReq.
        :type limit: int
        """
        self._limit = limit

    @property
    def method(self):
        r"""Gets the method of this QueryResRecordsDetailReq.

        查询方式。 oneself：客户自己sub_customer：企业子客户all：客户自己和企业子客户 此参数不携带或携带值为空串或携带值为null时，默认值为“all”，如果没有企业子客户，all的时候也是查询客户自己的数据。

        :return: The method of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        r"""Sets the method of this QueryResRecordsDetailReq.

        查询方式。 oneself：客户自己sub_customer：企业子客户all：客户自己和企业子客户 此参数不携带或携带值为空串或携带值为null时，默认值为“all”，如果没有企业子客户，all的时候也是查询客户自己的数据。

        :param method: The method of this QueryResRecordsDetailReq.
        :type method: str
        """
        self._method = method

    @property
    def sub_customer_id(self):
        r"""Gets the sub_customer_id of this QueryResRecordsDetailReq.

        企业子账号ID。  说明： 如果method取值不为sub_customer，则此参数无效。如果method取值为sub_customer，则此参数不能为空。

        :return: The sub_customer_id of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._sub_customer_id

    @sub_customer_id.setter
    def sub_customer_id(self, sub_customer_id):
        r"""Sets the sub_customer_id of this QueryResRecordsDetailReq.

        企业子账号ID。  说明： 如果method取值不为sub_customer，则此参数无效。如果method取值为sub_customer，则此参数不能为空。

        :param sub_customer_id: The sub_customer_id of this QueryResRecordsDetailReq.
        :type sub_customer_id: str
        """
        self._sub_customer_id = sub_customer_id

    @property
    def statistic_type(self):
        r"""Gets the statistic_type of this QueryResRecordsDetailReq.

        统计类型。默认值为1。 1：按账期2：按天3：按明细

        :return: The statistic_type of this QueryResRecordsDetailReq.
        :rtype: int
        """
        return self._statistic_type

    @statistic_type.setter
    def statistic_type(self, statistic_type):
        r"""Sets the statistic_type of this QueryResRecordsDetailReq.

        统计类型。默认值为1。 1：按账期2：按天3：按明细

        :param statistic_type: The statistic_type of this QueryResRecordsDetailReq.
        :type statistic_type: int
        """
        self._statistic_type = statistic_type

    @property
    def query_type(self):
        r"""Gets the query_type of this QueryResRecordsDetailReq.

        |参数名称：查询类型。默认值为BILLCYCLE。| |参数的约束及描述：默认值为BILLCYCLE。BILLCYCLE：按月 DAILY：按天 仅当statistic_type=2或3时，支持传递query_type=DAILY。该参数不携带或携带值为null或携带为空串时，取默认值BILLCYCLE。|

        :return: The query_type of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this QueryResRecordsDetailReq.

        |参数名称：查询类型。默认值为BILLCYCLE。| |参数的约束及描述：默认值为BILLCYCLE。BILLCYCLE：按月 DAILY：按天 仅当statistic_type=2或3时，支持传递query_type=DAILY。该参数不携带或携带值为null或携带为空串时，取默认值BILLCYCLE。|

        :param query_type: The query_type of this QueryResRecordsDetailReq.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def bill_cycle_begin(self):
        r"""Gets the bill_cycle_begin of this QueryResRecordsDetailReq.

        |账期开始时间。格式为YYYY-MM-DD。| |参数的约束及描述：仅当query_type=DAILY时，必须传递账期开始时间。该参数不携带或携带值为null或携带为空串时，不作为筛选条件。|

        :return: The bill_cycle_begin of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._bill_cycle_begin

    @bill_cycle_begin.setter
    def bill_cycle_begin(self, bill_cycle_begin):
        r"""Sets the bill_cycle_begin of this QueryResRecordsDetailReq.

        |账期开始时间。格式为YYYY-MM-DD。| |参数的约束及描述：仅当query_type=DAILY时，必须传递账期开始时间。该参数不携带或携带值为null或携带为空串时，不作为筛选条件。|

        :param bill_cycle_begin: The bill_cycle_begin of this QueryResRecordsDetailReq.
        :type bill_cycle_begin: str
        """
        self._bill_cycle_begin = bill_cycle_begin

    @property
    def bill_cycle_end(self):
        r"""Gets the bill_cycle_end of this QueryResRecordsDetailReq.

        |参数名称：账期结束时间。格式为YYYY-MM-DD。| |参数的约束及描述：仅当query_type=DAILY时，必须传递账期结束时间。该参数不携带或携带值为null或携带为空串时，不作为筛选条件。|

        :return: The bill_cycle_end of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._bill_cycle_end

    @bill_cycle_end.setter
    def bill_cycle_end(self, bill_cycle_end):
        r"""Sets the bill_cycle_end of this QueryResRecordsDetailReq.

        |参数名称：账期结束时间。格式为YYYY-MM-DD。| |参数的约束及描述：仅当query_type=DAILY时，必须传递账期结束时间。该参数不携带或携带值为null或携带为空串时，不作为筛选条件。|

        :param bill_cycle_end: The bill_cycle_end of this QueryResRecordsDetailReq.
        :type bill_cycle_end: str
        """
        self._bill_cycle_end = bill_cycle_end

    @property
    def payer_account_id(self):
        r"""Gets the payer_account_id of this QueryResRecordsDetailReq.

        |参数名称：支付账号ID。| |参数的约束及描述：普通客户、财务独立企业子客户查询消费记录，只能查询到客户自己的消费记录，该参数不携带或携带为自身ID时，查询的都只是自身的消费记录； 企业主客户查询消费记录，不携带时，查询的是自身的、财务托管企业子、财务独立企业子的消费记录；入参自身ID时，查询的是自身的、财务托管企业子的消费记录；也可入参其名下财务独立企业子的客户ID，只查询该财务独立企业子的消费记录； 财务托管企业子查询消费记录，入参自身ID时，查询的是未与企业主关联时的消费记录；入参企业主客户ID时，查询的是与企业主关联后的消费记录；不携带时查询以上全部消费记录|

        :return: The payer_account_id of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._payer_account_id

    @payer_account_id.setter
    def payer_account_id(self, payer_account_id):
        r"""Sets the payer_account_id of this QueryResRecordsDetailReq.

        |参数名称：支付账号ID。| |参数的约束及描述：普通客户、财务独立企业子客户查询消费记录，只能查询到客户自己的消费记录，该参数不携带或携带为自身ID时，查询的都只是自身的消费记录； 企业主客户查询消费记录，不携带时，查询的是自身的、财务托管企业子、财务独立企业子的消费记录；入参自身ID时，查询的是自身的、财务托管企业子的消费记录；也可入参其名下财务独立企业子的客户ID，只查询该财务独立企业子的消费记录； 财务托管企业子查询消费记录，入参自身ID时，查询的是未与企业主关联时的消费记录；入参企业主客户ID时，查询的是与企业主关联后的消费记录；不携带时查询以上全部消费记录|

        :param payer_account_id: The payer_account_id of this QueryResRecordsDetailReq.
        :type payer_account_id: str
        """
        self._payer_account_id = payer_account_id

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
        if not isinstance(other, QueryResRecordsDetailReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
