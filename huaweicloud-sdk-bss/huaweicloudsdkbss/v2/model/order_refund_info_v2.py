# coding: utf-8

import pprint
import re

import six





class OrderRefundInfoV2:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'amount': 'float',
        'measure_id': 'str',
        'customer_id': 'str',
        'resource_type_code': 'str',
        'service_type_code': 'str',
        'region_code': 'str',
        'base_order_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'amount': 'amount',
        'measure_id': 'measure_id',
        'customer_id': 'customer_id',
        'resource_type_code': 'resource_type_code',
        'service_type_code': 'service_type_code',
        'region_code': 'region_code',
        'base_order_id': 'base_order_id'
    }

    def __init__(self, id=None, amount=None, measure_id=None, customer_id=None, resource_type_code=None, service_type_code=None, region_code=None, base_order_id=None):
        """OrderRefundInfoV2 - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._amount = None
        self._measure_id = None
        self._customer_id = None
        self._resource_type_code = None
        self._service_type_code = None
        self._region_code = None
        self._base_order_id = None
        self.discriminator = None

        self.id = id
        self.amount = amount
        self.measure_id = measure_id
        self.customer_id = customer_id
        self.resource_type_code = resource_type_code
        self.service_type_code = service_type_code
        self.region_code = region_code
        if base_order_id is not None:
            self.base_order_id = base_order_id

    @property
    def id(self):
        """Gets the id of this OrderRefundInfoV2.

        |参数名称：该记录的ID。| |参数约束及描述：该记录的ID。|

        :return: The id of this OrderRefundInfoV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderRefundInfoV2.

        |参数名称：该记录的ID。| |参数约束及描述：该记录的ID。|

        :param id: The id of this OrderRefundInfoV2.
        :type: str
        """
        self._id = id

    @property
    def amount(self):
        """Gets the amount of this OrderRefundInfoV2.

        |参数名称：金额。金额为负数，表示退订金额。金额为正数，表示已消费金额或收取的退订手续费。| |参数的约束及描述：金额。金额为负数，表示退订金额。金额为正数，表示已消费金额或收取的退订手续费。|

        :return: The amount of this OrderRefundInfoV2.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this OrderRefundInfoV2.

        |参数名称：金额。金额为负数，表示退订金额。金额为正数，表示已消费金额或收取的退订手续费。| |参数的约束及描述：金额。金额为负数，表示退订金额。金额为正数，表示已消费金额或收取的退订手续费。|

        :param amount: The amount of this OrderRefundInfoV2.
        :type: float
        """
        self._amount = amount

    @property
    def measure_id(self):
        """Gets the measure_id of this OrderRefundInfoV2.

        |参数名称：度量单位。1：元2：角3：分| |参数约束及描述：度量单位。1：元2：角3：分|

        :return: The measure_id of this OrderRefundInfoV2.
        :rtype: str
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this OrderRefundInfoV2.

        |参数名称：度量单位。1：元2：角3：分| |参数约束及描述：度量单位。1：元2：角3：分|

        :param measure_id: The measure_id of this OrderRefundInfoV2.
        :type: str
        """
        self._measure_id = measure_id

    @property
    def customer_id(self):
        """Gets the customer_id of this OrderRefundInfoV2.

        |参数名称：客户ID。| |参数约束及描述：客户ID。|

        :return: The customer_id of this OrderRefundInfoV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this OrderRefundInfoV2.

        |参数名称：客户ID。| |参数约束及描述：客户ID。|

        :param customer_id: The customer_id of this OrderRefundInfoV2.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this OrderRefundInfoV2.

        |参数名称：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。| |参数约束及描述：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。|

        :return: The resource_type_code of this OrderRefundInfoV2.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this OrderRefundInfoV2.

        |参数名称：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。| |参数约束及描述：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。|

        :param resource_type_code: The resource_type_code of this OrderRefundInfoV2.
        :type: str
        """
        self._resource_type_code = resource_type_code

    @property
    def service_type_code(self):
        """Gets the service_type_code of this OrderRefundInfoV2.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。| |参数约束及描述：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。|

        :return: The service_type_code of this OrderRefundInfoV2.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this OrderRefundInfoV2.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。| |参数约束及描述：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。|

        :param service_type_code: The service_type_code of this OrderRefundInfoV2.
        :type: str
        """
        self._service_type_code = service_type_code

    @property
    def region_code(self):
        """Gets the region_code of this OrderRefundInfoV2.

        |参数名称：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。| |参数约束及描述：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。|

        :return: The region_code of this OrderRefundInfoV2.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this OrderRefundInfoV2.

        |参数名称：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。| |参数约束及描述：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。|

        :param region_code: The region_code of this OrderRefundInfoV2.
        :type: str
        """
        self._region_code = region_code

    @property
    def base_order_id(self):
        """Gets the base_order_id of this OrderRefundInfoV2.

        |参数名称：退订金额、已消费金额或收取退订手续费对应的原订单ID。| |参数约束及描述：退订金额、已消费金额或收取退订手续费对应的原订单ID。|

        :return: The base_order_id of this OrderRefundInfoV2.
        :rtype: str
        """
        return self._base_order_id

    @base_order_id.setter
    def base_order_id(self, base_order_id):
        """Sets the base_order_id of this OrderRefundInfoV2.

        |参数名称：退订金额、已消费金额或收取退订手续费对应的原订单ID。| |参数约束及描述：退订金额、已消费金额或收取退订手续费对应的原订单ID。|

        :param base_order_id: The base_order_id of this OrderRefundInfoV2.
        :type: str
        """
        self._base_order_id = base_order_id

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
        if not isinstance(other, OrderRefundInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
