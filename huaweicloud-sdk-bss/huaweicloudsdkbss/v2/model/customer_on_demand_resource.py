# coding: utf-8

import pprint
import re

import six





class CustomerOnDemandResource:


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
        'region_code': 'str',
        'availability_zone_code': 'str',
        'service_type_code': 'str',
        'resource_type_code': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'effective_time': 'str',
        'expire_time': 'str',
        'status': 'int',
        'resource_spec_code': 'str',
        'resource_info': 'str',
        'product_spec_desc': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'region_code': 'region_code',
        'availability_zone_code': 'availability_zone_code',
        'service_type_code': 'service_type_code',
        'resource_type_code': 'resource_type_code',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time',
        'status': 'status',
        'resource_spec_code': 'resource_spec_code',
        'resource_info': 'resource_info',
        'product_spec_desc': 'product_spec_desc'
    }

    def __init__(self, customer_id=None, region_code=None, availability_zone_code=None, service_type_code=None, resource_type_code=None, resource_id=None, resource_name=None, effective_time=None, expire_time=None, status=None, resource_spec_code=None, resource_info=None, product_spec_desc=None):
        """CustomerOnDemandResource - a model defined in huaweicloud sdk"""
        
        

        self._customer_id = None
        self._region_code = None
        self._availability_zone_code = None
        self._service_type_code = None
        self._resource_type_code = None
        self._resource_id = None
        self._resource_name = None
        self._effective_time = None
        self._expire_time = None
        self._status = None
        self._resource_spec_code = None
        self._resource_info = None
        self._product_spec_desc = None
        self.discriminator = None

        if customer_id is not None:
            self.customer_id = customer_id
        if region_code is not None:
            self.region_code = region_code
        if availability_zone_code is not None:
            self.availability_zone_code = availability_zone_code
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time
        if status is not None:
            self.status = status
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if resource_info is not None:
            self.resource_info = resource_info
        if product_spec_desc is not None:
            self.product_spec_desc = product_spec_desc

    @property
    def customer_id(self):
        """Gets the customer_id of this CustomerOnDemandResource.

        |参数名称：所属的客户ID。| |参数约束及描述：所属的客户ID。|

        :return: The customer_id of this CustomerOnDemandResource.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CustomerOnDemandResource.

        |参数名称：所属的客户ID。| |参数约束及描述：所属的客户ID。|

        :param customer_id: The customer_id of this CustomerOnDemandResource.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def region_code(self):
        """Gets the region_code of this CustomerOnDemandResource.

        |参数名称：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。| |参数约束及描述：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。|

        :return: The region_code of this CustomerOnDemandResource.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this CustomerOnDemandResource.

        |参数名称：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。| |参数约束及描述：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。|

        :param region_code: The region_code of this CustomerOnDemandResource.
        :type: str
        """
        self._region_code = region_code

    @property
    def availability_zone_code(self):
        """Gets the availability_zone_code of this CustomerOnDemandResource.

        |参数名称：所属的AZ的编码。| |参数约束及描述：所属的AZ的编码。|

        :return: The availability_zone_code of this CustomerOnDemandResource.
        :rtype: str
        """
        return self._availability_zone_code

    @availability_zone_code.setter
    def availability_zone_code(self, availability_zone_code):
        """Sets the availability_zone_code of this CustomerOnDemandResource.

        |参数名称：所属的AZ的编码。| |参数约束及描述：所属的AZ的编码。|

        :param availability_zone_code: The availability_zone_code of this CustomerOnDemandResource.
        :type: str
        """
        self._availability_zone_code = availability_zone_code

    @property
    def service_type_code(self):
        """Gets the service_type_code of this CustomerOnDemandResource.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。| |参数约束及描述：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。|

        :return: The service_type_code of this CustomerOnDemandResource.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this CustomerOnDemandResource.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。| |参数约束及描述：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。|

        :param service_type_code: The service_type_code of this CustomerOnDemandResource.
        :type: str
        """
        self._service_type_code = service_type_code

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this CustomerOnDemandResource.

        |参数名称：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。| |参数约束及描述：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。|

        :return: The resource_type_code of this CustomerOnDemandResource.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this CustomerOnDemandResource.

        |参数名称：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。| |参数约束及描述：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。|

        :param resource_type_code: The resource_type_code of this CustomerOnDemandResource.
        :type: str
        """
        self._resource_type_code = resource_type_code

    @property
    def resource_id(self):
        """Gets the resource_id of this CustomerOnDemandResource.

        |参数名称：具体资源的ID。| |参数约束及描述：具体资源的ID。|

        :return: The resource_id of this CustomerOnDemandResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this CustomerOnDemandResource.

        |参数名称：具体资源的ID。| |参数约束及描述：具体资源的ID。|

        :param resource_id: The resource_id of this CustomerOnDemandResource.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this CustomerOnDemandResource.

        |参数名称：资源实例的名称。| |参数约束及描述：资源实例的名称。|

        :return: The resource_name of this CustomerOnDemandResource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this CustomerOnDemandResource.

        |参数名称：资源实例的名称。| |参数约束及描述：资源实例的名称。|

        :param resource_name: The resource_name of this CustomerOnDemandResource.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def effective_time(self):
        """Gets the effective_time of this CustomerOnDemandResource.

        |参数名称：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数约束及描述：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。|

        :return: The effective_time of this CustomerOnDemandResource.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        """Sets the effective_time of this CustomerOnDemandResource.

        |参数名称：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数约束及描述：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。|

        :param effective_time: The effective_time of this CustomerOnDemandResource.
        :type: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        """Gets the expire_time of this CustomerOnDemandResource.

        |参数名称：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数约束及描述：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。|

        :return: The expire_time of this CustomerOnDemandResource.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this CustomerOnDemandResource.

        |参数名称：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数约束及描述：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。|

        :param expire_time: The expire_time of this CustomerOnDemandResource.
        :type: str
        """
        self._expire_time = expire_time

    @property
    def status(self):
        """Gets the status of this CustomerOnDemandResource.

        |参数名称：资源状态：1：正常（已开通）；2：宽限期；3：冻结中；4：变更中；5：正在关闭；6：已关闭。| |参数的约束及描述：资源状态：1：正常（已开通）；2：宽限期；3：冻结中；4：变更中；5：正在关闭；6：已关闭。|

        :return: The status of this CustomerOnDemandResource.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CustomerOnDemandResource.

        |参数名称：资源状态：1：正常（已开通）；2：宽限期；3：冻结中；4：变更中；5：正在关闭；6：已关闭。| |参数的约束及描述：资源状态：1：正常（已开通）；2：宽限期；3：冻结中；4：变更中；5：正在关闭；6：已关闭。|

        :param status: The status of this CustomerOnDemandResource.
        :type: int
        """
        self._status = status

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this CustomerOnDemandResource.

        |参数名称：按需资源规格编码。| |参数约束及描述：按需资源规格编码。|

        :return: The resource_spec_code of this CustomerOnDemandResource.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this CustomerOnDemandResource.

        |参数名称：按需资源规格编码。| |参数约束及描述：按需资源规格编码。|

        :param resource_spec_code: The resource_spec_code of this CustomerOnDemandResource.
        :type: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def resource_info(self):
        """Gets the resource_info of this CustomerOnDemandResource.

        |参数名称：资源容量大小。格式如| |参数约束及描述：资源容量大小。格式如：\"resourceInfo\": \"{\\\"specSize\\\":40.0}\"|

        :return: The resource_info of this CustomerOnDemandResource.
        :rtype: str
        """
        return self._resource_info

    @resource_info.setter
    def resource_info(self, resource_info):
        """Sets the resource_info of this CustomerOnDemandResource.

        |参数名称：资源容量大小。格式如| |参数约束及描述：资源容量大小。格式如：\"resourceInfo\": \"{\\\"specSize\\\":40.0}\"|

        :param resource_info: The resource_info of this CustomerOnDemandResource.
        :type: str
        """
        self._resource_info = resource_info

    @property
    def product_spec_desc(self):
        """Gets the product_spec_desc of this CustomerOnDemandResource.

        |参数名称：产品规格描述| |参数约束及描述：譬如虚拟机为：\"通用计算增强型|c6.2xlarge.4|8vCPUs|32GB|linux\"，硬盘为：\"云硬盘_SATA_LXH01|40.0GB\"|

        :return: The product_spec_desc of this CustomerOnDemandResource.
        :rtype: str
        """
        return self._product_spec_desc

    @product_spec_desc.setter
    def product_spec_desc(self, product_spec_desc):
        """Sets the product_spec_desc of this CustomerOnDemandResource.

        |参数名称：产品规格描述| |参数约束及描述：譬如虚拟机为：\"通用计算增强型|c6.2xlarge.4|8vCPUs|32GB|linux\"，硬盘为：\"云硬盘_SATA_LXH01|40.0GB\"|

        :param product_spec_desc: The product_spec_desc of this CustomerOnDemandResource.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomerOnDemandResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
