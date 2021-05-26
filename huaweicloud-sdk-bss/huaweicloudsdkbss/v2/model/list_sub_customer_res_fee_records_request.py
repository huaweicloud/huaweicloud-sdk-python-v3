# coding: utf-8

import pprint
import re

import six





class ListSubCustomerResFeeRecordsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'customer_id': 'str',
        'cycle': 'str',
        'cloud_service_type': 'str',
        'region': 'str',
        'charge_mode': 'str',
        'bill_type': 'int',
        'offset': 'int',
        'limit': 'int',
        'resource_id': 'str',
        'include_zero_record': 'bool',
        'indirect_partner_id': 'str',
        'bill_date_begin': 'str',
        'bill_date_end': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'cycle': 'cycle',
        'cloud_service_type': 'cloud_service_type',
        'region': 'region',
        'charge_mode': 'charge_mode',
        'bill_type': 'bill_type',
        'offset': 'offset',
        'limit': 'limit',
        'resource_id': 'resource_id',
        'include_zero_record': 'include_zero_record',
        'indirect_partner_id': 'indirect_partner_id',
        'bill_date_begin': 'bill_date_begin',
        'bill_date_end': 'bill_date_end'
    }

    def __init__(self, customer_id=None, cycle=None, cloud_service_type=None, region=None, charge_mode=None, bill_type=None, offset=None, limit=None, resource_id=None, include_zero_record=None, indirect_partner_id=None, bill_date_begin=None, bill_date_end=None):
        """ListSubCustomerResFeeRecordsRequest - a model defined in huaweicloud sdk"""
        
        

        self._customer_id = None
        self._cycle = None
        self._cloud_service_type = None
        self._region = None
        self._charge_mode = None
        self._bill_type = None
        self._offset = None
        self._limit = None
        self._resource_id = None
        self._include_zero_record = None
        self._indirect_partner_id = None
        self._bill_date_begin = None
        self._bill_date_end = None
        self.discriminator = None

        self.customer_id = customer_id
        self.cycle = cycle
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if region is not None:
            self.region = region
        self.charge_mode = charge_mode
        if bill_type is not None:
            self.bill_type = bill_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if resource_id is not None:
            self.resource_id = resource_id
        if include_zero_record is not None:
            self.include_zero_record = include_zero_record
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id
        if bill_date_begin is not None:
            self.bill_date_begin = bill_date_begin
        if bill_date_end is not None:
            self.bill_date_end = bill_date_end

    @property
    def customer_id(self):
        """Gets the customer_id of this ListSubCustomerResFeeRecordsRequest.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :return: The customer_id of this ListSubCustomerResFeeRecordsRequest.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ListSubCustomerResFeeRecordsRequest.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :param customer_id: The customer_id of this ListSubCustomerResFeeRecordsRequest.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def cycle(self):
        """Gets the cycle of this ListSubCustomerResFeeRecordsRequest.

        查询的客户消费记录所在账期，格式：YYYY-MM。

        :return: The cycle of this ListSubCustomerResFeeRecordsRequest.
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this ListSubCustomerResFeeRecordsRequest.

        查询的客户消费记录所在账期，格式：YYYY-MM。

        :param cycle: The cycle of this ListSubCustomerResFeeRecordsRequest.
        :type: str
        """
        self._cycle = cycle

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this ListSubCustomerResFeeRecordsRequest.

        云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。您可以调用查询云服务类型列表接口获取。

        :return: The cloud_service_type of this ListSubCustomerResFeeRecordsRequest.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this ListSubCustomerResFeeRecordsRequest.

        云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。您可以调用查询云服务类型列表接口获取。

        :param cloud_service_type: The cloud_service_type of this ListSubCustomerResFeeRecordsRequest.
        :type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def region(self):
        """Gets the region of this ListSubCustomerResFeeRecordsRequest.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :return: The region of this ListSubCustomerResFeeRecordsRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListSubCustomerResFeeRecordsRequest.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :param region: The region of this ListSubCustomerResFeeRecordsRequest.
        :type: str
        """
        self._region = region

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ListSubCustomerResFeeRecordsRequest.

        计费模式。 1 : 包年/包月3：按需10: 预留实例

        :return: The charge_mode of this ListSubCustomerResFeeRecordsRequest.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ListSubCustomerResFeeRecordsRequest.

        计费模式。 1 : 包年/包月3：按需10: 预留实例

        :param charge_mode: The charge_mode of this ListSubCustomerResFeeRecordsRequest.
        :type: str
        """
        self._charge_mode = charge_mode

    @property
    def bill_type(self):
        """Gets the bill_type of this ListSubCustomerResFeeRecordsRequest.

        账单类型。 1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费16：调账-扣费

        :return: The bill_type of this ListSubCustomerResFeeRecordsRequest.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this ListSubCustomerResFeeRecordsRequest.

        账单类型。 1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿14：消费-服务支持计划月末扣费16：调账-扣费

        :param bill_type: The bill_type of this ListSubCustomerResFeeRecordsRequest.
        :type: int
        """
        self._bill_type = bill_type

    @property
    def offset(self):
        """Gets the offset of this ListSubCustomerResFeeRecordsRequest.

        偏移量，从0开始。默认值为0。

        :return: The offset of this ListSubCustomerResFeeRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSubCustomerResFeeRecordsRequest.

        偏移量，从0开始。默认值为0。

        :param offset: The offset of this ListSubCustomerResFeeRecordsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSubCustomerResFeeRecordsRequest.

        每次查询的数量限制。默认值为10。

        :return: The limit of this ListSubCustomerResFeeRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSubCustomerResFeeRecordsRequest.

        每次查询的数量限制。默认值为10。

        :param limit: The limit of this ListSubCustomerResFeeRecordsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def resource_id(self):
        """Gets the resource_id of this ListSubCustomerResFeeRecordsRequest.

        资源ID。

        :return: The resource_id of this ListSubCustomerResFeeRecordsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListSubCustomerResFeeRecordsRequest.

        资源ID。

        :param resource_id: The resource_id of this ListSubCustomerResFeeRecordsRequest.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def include_zero_record(self):
        """Gets the include_zero_record of this ListSubCustomerResFeeRecordsRequest.

        返回是否包含应付金额为0的记录。 true：包含false：不包含

        :return: The include_zero_record of this ListSubCustomerResFeeRecordsRequest.
        :rtype: bool
        """
        return self._include_zero_record

    @include_zero_record.setter
    def include_zero_record(self, include_zero_record):
        """Sets the include_zero_record of this ListSubCustomerResFeeRecordsRequest.

        返回是否包含应付金额为0的记录。 true：包含false：不包含

        :param include_zero_record: The include_zero_record of this ListSubCustomerResFeeRecordsRequest.
        :type: bool
        """
        self._include_zero_record = include_zero_record

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ListSubCustomerResFeeRecordsRequest.

        精英服务商ID。 如果华为云伙伴能力中心需要查询客户在精英服务商关联期间的消费，需要携带该字段；否则只能查询该客户在与自己关联期间的消费。

        :return: The indirect_partner_id of this ListSubCustomerResFeeRecordsRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ListSubCustomerResFeeRecordsRequest.

        精英服务商ID。 如果华为云伙伴能力中心需要查询客户在精英服务商关联期间的消费，需要携带该字段；否则只能查询该客户在与自己关联期间的消费。

        :param indirect_partner_id: The indirect_partner_id of this ListSubCustomerResFeeRecordsRequest.
        :type: str
        """
        self._indirect_partner_id = indirect_partner_id

    @property
    def bill_date_begin(self):
        """Gets the bill_date_begin of this ListSubCustomerResFeeRecordsRequest.

        |参数名称：查询的资源消费记录的开始日期，格式为YYYY-MM-DD。| |参数的约束及描述：必须和cycle（即资源的消费账期）在同一个月。|

        :return: The bill_date_begin of this ListSubCustomerResFeeRecordsRequest.
        :rtype: str
        """
        return self._bill_date_begin

    @bill_date_begin.setter
    def bill_date_begin(self, bill_date_begin):
        """Sets the bill_date_begin of this ListSubCustomerResFeeRecordsRequest.

        |参数名称：查询的资源消费记录的开始日期，格式为YYYY-MM-DD。| |参数的约束及描述：必须和cycle（即资源的消费账期）在同一个月。|

        :param bill_date_begin: The bill_date_begin of this ListSubCustomerResFeeRecordsRequest.
        :type: str
        """
        self._bill_date_begin = bill_date_begin

    @property
    def bill_date_end(self):
        """Gets the bill_date_end of this ListSubCustomerResFeeRecordsRequest.

        |参数名称：查询的资源消费记录的结束日期，格式为YYYY-MM-DD。| |参数的约束及描述：必须和cycle（即资源的消费账期）在同一个月。bill_date_begin和bill_date_end两个参数必须同时出现，否则仅按照cycle（即资源的消费账期）进行查询。|

        :return: The bill_date_end of this ListSubCustomerResFeeRecordsRequest.
        :rtype: str
        """
        return self._bill_date_end

    @bill_date_end.setter
    def bill_date_end(self, bill_date_end):
        """Sets the bill_date_end of this ListSubCustomerResFeeRecordsRequest.

        |参数名称：查询的资源消费记录的结束日期，格式为YYYY-MM-DD。| |参数的约束及描述：必须和cycle（即资源的消费账期）在同一个月。bill_date_begin和bill_date_end两个参数必须同时出现，否则仅按照cycle（即资源的消费账期）进行查询。|

        :param bill_date_end: The bill_date_end of this ListSubCustomerResFeeRecordsRequest.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSubCustomerResFeeRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
