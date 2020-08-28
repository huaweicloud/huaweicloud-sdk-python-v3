# coding: utf-8

import pprint
import re

import six





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
        'bill_type': 'int',
        'charge_mode': 'int',
        'cloud_service_type': 'str',
        'cycle': 'str',
        'enterprise_project_id': 'str',
        'include_zero_record': 'bool',
        'limit': 'int',
        'offset': 'int',
        'region': 'str',
        'res_instance_id': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'bill_type': 'bill_type',
        'charge_mode': 'charge_mode',
        'cloud_service_type': 'cloud_service_type',
        'cycle': 'cycle',
        'enterprise_project_id': 'enterprise_project_id',
        'include_zero_record': 'include_zero_record',
        'limit': 'limit',
        'offset': 'offset',
        'region': 'region',
        'res_instance_id': 'res_instance_id',
        'resource_type': 'resource_type'
    }

    def __init__(self, bill_type=None, charge_mode=None, cloud_service_type=None, cycle=None, enterprise_project_id=None, include_zero_record=None, limit=10, offset=0, region=None, res_instance_id=None, resource_type=None):
        """QueryResRecordsDetailReq - a model defined in huaweicloud sdk"""
        
        

        self._bill_type = None
        self._charge_mode = None
        self._cloud_service_type = None
        self._cycle = None
        self._enterprise_project_id = None
        self._include_zero_record = None
        self._limit = None
        self._offset = None
        self._region = None
        self._res_instance_id = None
        self._resource_type = None
        self.discriminator = None

        if bill_type is not None:
            self.bill_type = bill_type
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        self.cycle = cycle
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if include_zero_record is not None:
            self.include_zero_record = include_zero_record
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if region is not None:
            self.region = region
        if res_instance_id is not None:
            self.res_instance_id = res_instance_id
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def bill_type(self):
        """Gets the bill_type of this QueryResRecordsDetailReq.

        |参数名称：账单类型| |参数的约束及描述：该参数非必填，且只允许整数,1：消费-新购；2：消费-续订；3：消费-变更；4：退款-退订；5：消费-使用；8：消费-自动续订；9：调账-补偿；12：消费-按时计费；13：消费-退订手续费；14：消费-服务支持计划月末扣费；16：调账-扣费|

        :return: The bill_type of this QueryResRecordsDetailReq.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this QueryResRecordsDetailReq.

        |参数名称：账单类型| |参数的约束及描述：该参数非必填，且只允许整数,1：消费-新购；2：消费-续订；3：消费-变更；4：退款-退订；5：消费-使用；8：消费-自动续订；9：调账-补偿；12：消费-按时计费；13：消费-退订手续费；14：消费-服务支持计划月末扣费；16：调账-扣费|

        :param bill_type: The bill_type of this QueryResRecordsDetailReq.
        :type: int
        """
        self._bill_type = bill_type

    @property
    def charge_mode(self):
        """Gets the charge_mode of this QueryResRecordsDetailReq.

        |参数名称：支付方式| |参数的约束及描述：该参数非必填，且只允许整数,1 : 包周期；3: 按需。10: 预留实例|

        :return: The charge_mode of this QueryResRecordsDetailReq.
        :rtype: int
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this QueryResRecordsDetailReq.

        |参数名称：支付方式| |参数的约束及描述：该参数非必填，且只允许整数,1 : 包周期；3: 按需。10: 预留实例|

        :param charge_mode: The charge_mode of this QueryResRecordsDetailReq.
        :type: int
        """
        self._charge_mode = charge_mode

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this QueryResRecordsDetailReq.

        |参数名称：云服务类型编码| |参数的约束及描述：该参数非必填，最大长度：64，且只允许字符串，例如ECS的云服务类型编码为“hws.service.type.ec2”|

        :return: The cloud_service_type of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this QueryResRecordsDetailReq.

        |参数名称：云服务类型编码| |参数的约束及描述：该参数非必填，最大长度：64，且只允许字符串，例如ECS的云服务类型编码为“hws.service.type.ec2”|

        :param cloud_service_type: The cloud_service_type of this QueryResRecordsDetailReq.
        :type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def cycle(self):
        """Gets the cycle of this QueryResRecordsDetailReq.

        |参数名称：消费月份| |参数的约束及描述：该参数必填，最大长度：8，比如2018-12|

        :return: The cycle of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this QueryResRecordsDetailReq.

        |参数名称：消费月份| |参数的约束及描述：该参数必填，最大长度：8，比如2018-12|

        :param cycle: The cycle of this QueryResRecordsDetailReq.
        :type: str
        """
        self._cycle = cycle

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this QueryResRecordsDetailReq.

        |参数名称：企业项目ID| |参数的约束及描述：该参数非必，最大长度：64，且只允许字符串|

        :return: The enterprise_project_id of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this QueryResRecordsDetailReq.

        |参数名称：企业项目ID| |参数的约束及描述：该参数非必，最大长度：64，且只允许字符串|

        :param enterprise_project_id: The enterprise_project_id of this QueryResRecordsDetailReq.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def include_zero_record(self):
        """Gets the include_zero_record of this QueryResRecordsDetailReq.

        |参数名称：返回是否包含应付金额为0的记录| |参数的约束及描述：该参数非必填，且只允许布尔型，true: 包含；false: 不包含|

        :return: The include_zero_record of this QueryResRecordsDetailReq.
        :rtype: bool
        """
        return self._include_zero_record

    @include_zero_record.setter
    def include_zero_record(self, include_zero_record):
        """Sets the include_zero_record of this QueryResRecordsDetailReq.

        |参数名称：返回是否包含应付金额为0的记录| |参数的约束及描述：该参数非必填，且只允许布尔型，true: 包含；false: 不包含|

        :param include_zero_record: The include_zero_record of this QueryResRecordsDetailReq.
        :type: bool
        """
        self._include_zero_record = include_zero_record

    @property
    def limit(self):
        """Gets the limit of this QueryResRecordsDetailReq.

        |参数名称：页面大小| |参数的约束及描述：该参数非必填，且只允许1-100的数字，默认10|

        :return: The limit of this QueryResRecordsDetailReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QueryResRecordsDetailReq.

        |参数名称：页面大小| |参数的约束及描述：该参数非必填，且只允许1-100的数字，默认10|

        :param limit: The limit of this QueryResRecordsDetailReq.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this QueryResRecordsDetailReq.

        |参数名称：偏移量| |参数的约束及描述：该参数非必填，且只允许数字，默认为1|

        :return: The offset of this QueryResRecordsDetailReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this QueryResRecordsDetailReq.

        |参数名称：偏移量| |参数的约束及描述：该参数非必填，且只允许数字，默认为1|

        :param offset: The offset of this QueryResRecordsDetailReq.
        :type: int
        """
        self._offset = offset

    @property
    def region(self):
        """Gets the region of this QueryResRecordsDetailReq.

        |参数名称：云服务区编码| |参数的约束及描述：该参数非必填，最大长度：64，且只允许字符串，例如：“cn-north-1”|

        :return: The region of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this QueryResRecordsDetailReq.

        |参数名称：云服务区编码| |参数的约束及描述：该参数非必填，最大长度：64，且只允许字符串，例如：“cn-north-1”|

        :param region: The region of this QueryResRecordsDetailReq.
        :type: str
        """
        self._region = region

    @property
    def res_instance_id(self):
        """Gets the res_instance_id of this QueryResRecordsDetailReq.

        |参数名称：资源实例ID| |参数的约束及描述：该参数非必填，最大长度：64，且只允字符串|

        :return: The res_instance_id of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._res_instance_id

    @res_instance_id.setter
    def res_instance_id(self, res_instance_id):
        """Sets the res_instance_id of this QueryResRecordsDetailReq.

        |参数名称：资源实例ID| |参数的约束及描述：该参数非必填，最大长度：64，且只允字符串|

        :param res_instance_id: The res_instance_id of this QueryResRecordsDetailReq.
        :type: str
        """
        self._res_instance_id = res_instance_id

    @property
    def resource_type(self):
        """Gets the resource_type of this QueryResRecordsDetailReq.

        |参数名称：资源类型编码| |参数的约束及描述：该参数非必填，最大长度：64，且只允许字符串，例如ECS的VM为“hws.resource.type.vm”|

        :return: The resource_type of this QueryResRecordsDetailReq.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this QueryResRecordsDetailReq.

        |参数名称：资源类型编码| |参数的约束及描述：该参数非必填，最大长度：64，且只允许字符串，例如ECS的VM为“hws.resource.type.vm”|

        :param resource_type: The resource_type of this QueryResRecordsDetailReq.
        :type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, QueryResRecordsDetailReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
