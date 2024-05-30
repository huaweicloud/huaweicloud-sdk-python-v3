# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomerBillsMonthlyBreakDownRequest:

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
        'shared_month': 'str',
        'service_type_code': 'str',
        'resource_type_code': 'str',
        'region_code': 'str',
        'charging_mode': 'int',
        'bill_type': 'int',
        'offset': 'int',
        'limit': 'int',
        'resource_id': 'str',
        'resource_name': 'str',
        'enterprise_project_id': 'str',
        'method': 'str',
        'sub_customer_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'shared_month': 'shared_month',
        'service_type_code': 'service_type_code',
        'resource_type_code': 'resource_type_code',
        'region_code': 'region_code',
        'charging_mode': 'charging_mode',
        'bill_type': 'bill_type',
        'offset': 'offset',
        'limit': 'limit',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'enterprise_project_id': 'enterprise_project_id',
        'method': 'method',
        'sub_customer_id': 'sub_customer_id'
    }

    def __init__(self, x_language=None, shared_month=None, service_type_code=None, resource_type_code=None, region_code=None, charging_mode=None, bill_type=None, offset=None, limit=None, resource_id=None, resource_name=None, enterprise_project_id=None, method=None, sub_customer_id=None):
        """ListCustomerBillsMonthlyBreakDownRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。en_US：英文。zh_CN：中文
        :type x_language: str
        :param shared_month: 查询分摊成本的月份，东八区时间，格式：YYYY-MM。
        :type shared_month: str
        :param service_type_code: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用[查询云服务类型列表](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001256679455.html)接口获取。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串时，作为筛选条件。
        :type service_type_code: str
        :param resource_type_code: 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用[查询资源类型列表](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001256519451.html)接口获取。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串时，作为筛选条件。
        :type resource_type_code: str
        :param region_code: 云服务区编码，例如：“cn-north-1”。具体请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)对应云服务的“区域”列的值。此参数不携带或携带值为空时，不作为筛选条件。
        :type region_code: str
        :param charging_mode: 计费模式。1：包年/包月3：按需10：预留实例11：节省计划此参数不携带或携带值为空时，不作为筛选条件。
        :type charging_mode: int
        :param bill_type: 账单类型。1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费16：调账-扣费18：消费-按月付费20：退款-变更23：消费-节省计划抵扣24：退款-包年/包月转按需此参数不携带或携带值为空时，不作为筛选条件。
        :type bill_type: int
        :param offset: 偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 每次查询的数量限制。默认值为10。
        :type limit: int
        :param resource_id: 资源ID。此参数不携带或携带值为空时，不作为筛选条件。
        :type resource_id: str
        :param resource_name: 资源名称。此参数不携带或携带值为空时，不作为筛选条件。
        :type resource_name: str
        :param enterprise_project_id: 企业项目标识（企业项目ID）。default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。此参数不携带或携带值为空时，不作为筛选条件。
        :type enterprise_project_id: str
        :param method: 查询资源消费记录的方式。oneself：客户自己sub_customer：企业子客户all：客户自己和企业子客户默认为all，如果没有企业子客户，取值为all时查询的是客户自己的资源消费记录。此参数不携带，不作为筛选条件。
        :type method: str
        :param sub_customer_id: 企业子账号ID。此参数不携带或携带值为空或携带值为空串时，不作为筛选条件。 说明： 如果method取值不为sub_customer，则该参数无效。如果method取值为sub_customer，则该参数不能为空。
        :type sub_customer_id: str
        """
        
        

        self._x_language = None
        self._shared_month = None
        self._service_type_code = None
        self._resource_type_code = None
        self._region_code = None
        self._charging_mode = None
        self._bill_type = None
        self._offset = None
        self._limit = None
        self._resource_id = None
        self._resource_name = None
        self._enterprise_project_id = None
        self._method = None
        self._sub_customer_id = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.shared_month = shared_month
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
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if method is not None:
            self.method = method
        if sub_customer_id is not None:
            self.sub_customer_id = sub_customer_id

    @property
    def x_language(self):
        """Gets the x_language of this ListCustomerBillsMonthlyBreakDownRequest.

        语言。en_US：英文。zh_CN：中文

        :return: The x_language of this ListCustomerBillsMonthlyBreakDownRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListCustomerBillsMonthlyBreakDownRequest.

        语言。en_US：英文。zh_CN：中文

        :param x_language: The x_language of this ListCustomerBillsMonthlyBreakDownRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def shared_month(self):
        """Gets the shared_month of this ListCustomerBillsMonthlyBreakDownRequest.

        查询分摊成本的月份，东八区时间，格式：YYYY-MM。

        :return: The shared_month of this ListCustomerBillsMonthlyBreakDownRequest.
        :rtype: str
        """
        return self._shared_month

    @shared_month.setter
    def shared_month(self, shared_month):
        """Sets the shared_month of this ListCustomerBillsMonthlyBreakDownRequest.

        查询分摊成本的月份，东八区时间，格式：YYYY-MM。

        :param shared_month: The shared_month of this ListCustomerBillsMonthlyBreakDownRequest.
        :type shared_month: str
        """
        self._shared_month = shared_month

    @property
    def service_type_code(self):
        """Gets the service_type_code of this ListCustomerBillsMonthlyBreakDownRequest.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用[查询云服务类型列表](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001256679455.html)接口获取。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串时，作为筛选条件。

        :return: The service_type_code of this ListCustomerBillsMonthlyBreakDownRequest.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this ListCustomerBillsMonthlyBreakDownRequest.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用[查询云服务类型列表](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001256679455.html)接口获取。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串时，作为筛选条件。

        :param service_type_code: The service_type_code of this ListCustomerBillsMonthlyBreakDownRequest.
        :type service_type_code: str
        """
        self._service_type_code = service_type_code

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this ListCustomerBillsMonthlyBreakDownRequest.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用[查询资源类型列表](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001256519451.html)接口获取。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串时，作为筛选条件。

        :return: The resource_type_code of this ListCustomerBillsMonthlyBreakDownRequest.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this ListCustomerBillsMonthlyBreakDownRequest.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用[查询资源类型列表](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001256519451.html)接口获取。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串时，作为筛选条件。

        :param resource_type_code: The resource_type_code of this ListCustomerBillsMonthlyBreakDownRequest.
        :type resource_type_code: str
        """
        self._resource_type_code = resource_type_code

    @property
    def region_code(self):
        """Gets the region_code of this ListCustomerBillsMonthlyBreakDownRequest.

        云服务区编码，例如：“cn-north-1”。具体请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)对应云服务的“区域”列的值。此参数不携带或携带值为空时，不作为筛选条件。

        :return: The region_code of this ListCustomerBillsMonthlyBreakDownRequest.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this ListCustomerBillsMonthlyBreakDownRequest.

        云服务区编码，例如：“cn-north-1”。具体请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)对应云服务的“区域”列的值。此参数不携带或携带值为空时，不作为筛选条件。

        :param region_code: The region_code of this ListCustomerBillsMonthlyBreakDownRequest.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def charging_mode(self):
        """Gets the charging_mode of this ListCustomerBillsMonthlyBreakDownRequest.

        计费模式。1：包年/包月3：按需10：预留实例11：节省计划此参数不携带或携带值为空时，不作为筛选条件。

        :return: The charging_mode of this ListCustomerBillsMonthlyBreakDownRequest.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this ListCustomerBillsMonthlyBreakDownRequest.

        计费模式。1：包年/包月3：按需10：预留实例11：节省计划此参数不携带或携带值为空时，不作为筛选条件。

        :param charging_mode: The charging_mode of this ListCustomerBillsMonthlyBreakDownRequest.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def bill_type(self):
        """Gets the bill_type of this ListCustomerBillsMonthlyBreakDownRequest.

        账单类型。1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费16：调账-扣费18：消费-按月付费20：退款-变更23：消费-节省计划抵扣24：退款-包年/包月转按需此参数不携带或携带值为空时，不作为筛选条件。

        :return: The bill_type of this ListCustomerBillsMonthlyBreakDownRequest.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this ListCustomerBillsMonthlyBreakDownRequest.

        账单类型。1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费16：调账-扣费18：消费-按月付费20：退款-变更23：消费-节省计划抵扣24：退款-包年/包月转按需此参数不携带或携带值为空时，不作为筛选条件。

        :param bill_type: The bill_type of this ListCustomerBillsMonthlyBreakDownRequest.
        :type bill_type: int
        """
        self._bill_type = bill_type

    @property
    def offset(self):
        """Gets the offset of this ListCustomerBillsMonthlyBreakDownRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this ListCustomerBillsMonthlyBreakDownRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCustomerBillsMonthlyBreakDownRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this ListCustomerBillsMonthlyBreakDownRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListCustomerBillsMonthlyBreakDownRequest.

        每次查询的数量限制。默认值为10。

        :return: The limit of this ListCustomerBillsMonthlyBreakDownRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCustomerBillsMonthlyBreakDownRequest.

        每次查询的数量限制。默认值为10。

        :param limit: The limit of this ListCustomerBillsMonthlyBreakDownRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def resource_id(self):
        """Gets the resource_id of this ListCustomerBillsMonthlyBreakDownRequest.

        资源ID。此参数不携带或携带值为空时，不作为筛选条件。

        :return: The resource_id of this ListCustomerBillsMonthlyBreakDownRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListCustomerBillsMonthlyBreakDownRequest.

        资源ID。此参数不携带或携带值为空时，不作为筛选条件。

        :param resource_id: The resource_id of this ListCustomerBillsMonthlyBreakDownRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this ListCustomerBillsMonthlyBreakDownRequest.

        资源名称。此参数不携带或携带值为空时，不作为筛选条件。

        :return: The resource_name of this ListCustomerBillsMonthlyBreakDownRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ListCustomerBillsMonthlyBreakDownRequest.

        资源名称。此参数不携带或携带值为空时，不作为筛选条件。

        :param resource_name: The resource_name of this ListCustomerBillsMonthlyBreakDownRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListCustomerBillsMonthlyBreakDownRequest.

        企业项目标识（企业项目ID）。default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。此参数不携带或携带值为空时，不作为筛选条件。

        :return: The enterprise_project_id of this ListCustomerBillsMonthlyBreakDownRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListCustomerBillsMonthlyBreakDownRequest.

        企业项目标识（企业项目ID）。default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。此参数不携带或携带值为空时，不作为筛选条件。

        :param enterprise_project_id: The enterprise_project_id of this ListCustomerBillsMonthlyBreakDownRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def method(self):
        """Gets the method of this ListCustomerBillsMonthlyBreakDownRequest.

        查询资源消费记录的方式。oneself：客户自己sub_customer：企业子客户all：客户自己和企业子客户默认为all，如果没有企业子客户，取值为all时查询的是客户自己的资源消费记录。此参数不携带，不作为筛选条件。

        :return: The method of this ListCustomerBillsMonthlyBreakDownRequest.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ListCustomerBillsMonthlyBreakDownRequest.

        查询资源消费记录的方式。oneself：客户自己sub_customer：企业子客户all：客户自己和企业子客户默认为all，如果没有企业子客户，取值为all时查询的是客户自己的资源消费记录。此参数不携带，不作为筛选条件。

        :param method: The method of this ListCustomerBillsMonthlyBreakDownRequest.
        :type method: str
        """
        self._method = method

    @property
    def sub_customer_id(self):
        """Gets the sub_customer_id of this ListCustomerBillsMonthlyBreakDownRequest.

        企业子账号ID。此参数不携带或携带值为空或携带值为空串时，不作为筛选条件。 说明： 如果method取值不为sub_customer，则该参数无效。如果method取值为sub_customer，则该参数不能为空。

        :return: The sub_customer_id of this ListCustomerBillsMonthlyBreakDownRequest.
        :rtype: str
        """
        return self._sub_customer_id

    @sub_customer_id.setter
    def sub_customer_id(self, sub_customer_id):
        """Sets the sub_customer_id of this ListCustomerBillsMonthlyBreakDownRequest.

        企业子账号ID。此参数不携带或携带值为空或携带值为空串时，不作为筛选条件。 说明： 如果method取值不为sub_customer，则该参数无效。如果method取值为sub_customer，则该参数不能为空。

        :param sub_customer_id: The sub_customer_id of this ListCustomerBillsMonthlyBreakDownRequest.
        :type sub_customer_id: str
        """
        self._sub_customer_id = sub_customer_id

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
        if not isinstance(other, ListCustomerBillsMonthlyBreakDownRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
