# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'resource_type_name': 'str',
        'service_type_name': 'str',
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
        'resource_type_name': 'resource_type_name',
        'service_type_name': 'service_type_name',
        'region_code': 'region_code',
        'base_order_id': 'base_order_id'
    }

    def __init__(self, id=None, amount=None, measure_id=None, customer_id=None, resource_type_code=None, service_type_code=None, resource_type_name=None, service_type_name=None, region_code=None, base_order_id=None):
        """OrderRefundInfoV2

        The model defined in huaweicloud sdk

        :param id: 该记录的ID。
        :type id: str
        :param amount: 金额。 金额为负数，表示退订金额。金额为正数，表示已消费金额或收取的退订手续费。
        :type amount: float
        :param measure_id: 金额的度量单位。 1：元
        :type measure_id: str
        :param customer_id: 客户账号ID。
        :type customer_id: str
        :param resource_type_code: 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。
        :type resource_type_code: str
        :param service_type_code: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。
        :type service_type_code: str
        :param resource_type_name: 资源类型名称。例如ECS的资源类型名称为“云主机”。
        :type resource_type_name: str
        :param service_type_name: 云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。
        :type service_type_name: str
        :param region_code: 云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。
        :type region_code: str
        :param base_order_id: 退订金额、已消费金额或收取退订手续费对应的原订单ID。
        :type base_order_id: str
        """
        
        

        self._id = None
        self._amount = None
        self._measure_id = None
        self._customer_id = None
        self._resource_type_code = None
        self._service_type_code = None
        self._resource_type_name = None
        self._service_type_name = None
        self._region_code = None
        self._base_order_id = None
        self.discriminator = None

        self.id = id
        self.amount = amount
        self.measure_id = measure_id
        self.customer_id = customer_id
        self.resource_type_code = resource_type_code
        self.service_type_code = service_type_code
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if service_type_name is not None:
            self.service_type_name = service_type_name
        self.region_code = region_code
        if base_order_id is not None:
            self.base_order_id = base_order_id

    @property
    def id(self):
        """Gets the id of this OrderRefundInfoV2.

        该记录的ID。

        :return: The id of this OrderRefundInfoV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderRefundInfoV2.

        该记录的ID。

        :param id: The id of this OrderRefundInfoV2.
        :type id: str
        """
        self._id = id

    @property
    def amount(self):
        """Gets the amount of this OrderRefundInfoV2.

        金额。 金额为负数，表示退订金额。金额为正数，表示已消费金额或收取的退订手续费。

        :return: The amount of this OrderRefundInfoV2.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this OrderRefundInfoV2.

        金额。 金额为负数，表示退订金额。金额为正数，表示已消费金额或收取的退订手续费。

        :param amount: The amount of this OrderRefundInfoV2.
        :type amount: float
        """
        self._amount = amount

    @property
    def measure_id(self):
        """Gets the measure_id of this OrderRefundInfoV2.

        金额的度量单位。 1：元

        :return: The measure_id of this OrderRefundInfoV2.
        :rtype: str
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this OrderRefundInfoV2.

        金额的度量单位。 1：元

        :param measure_id: The measure_id of this OrderRefundInfoV2.
        :type measure_id: str
        """
        self._measure_id = measure_id

    @property
    def customer_id(self):
        """Gets the customer_id of this OrderRefundInfoV2.

        客户账号ID。

        :return: The customer_id of this OrderRefundInfoV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this OrderRefundInfoV2.

        客户账号ID。

        :param customer_id: The customer_id of this OrderRefundInfoV2.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this OrderRefundInfoV2.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :return: The resource_type_code of this OrderRefundInfoV2.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this OrderRefundInfoV2.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :param resource_type_code: The resource_type_code of this OrderRefundInfoV2.
        :type resource_type_code: str
        """
        self._resource_type_code = resource_type_code

    @property
    def service_type_code(self):
        """Gets the service_type_code of this OrderRefundInfoV2.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :return: The service_type_code of this OrderRefundInfoV2.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this OrderRefundInfoV2.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :param service_type_code: The service_type_code of this OrderRefundInfoV2.
        :type service_type_code: str
        """
        self._service_type_code = service_type_code

    @property
    def resource_type_name(self):
        """Gets the resource_type_name of this OrderRefundInfoV2.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :return: The resource_type_name of this OrderRefundInfoV2.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        """Sets the resource_type_name of this OrderRefundInfoV2.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :param resource_type_name: The resource_type_name of this OrderRefundInfoV2.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def service_type_name(self):
        """Gets the service_type_name of this OrderRefundInfoV2.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :return: The service_type_name of this OrderRefundInfoV2.
        :rtype: str
        """
        return self._service_type_name

    @service_type_name.setter
    def service_type_name(self, service_type_name):
        """Sets the service_type_name of this OrderRefundInfoV2.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :param service_type_name: The service_type_name of this OrderRefundInfoV2.
        :type service_type_name: str
        """
        self._service_type_name = service_type_name

    @property
    def region_code(self):
        """Gets the region_code of this OrderRefundInfoV2.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :return: The region_code of this OrderRefundInfoV2.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this OrderRefundInfoV2.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :param region_code: The region_code of this OrderRefundInfoV2.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def base_order_id(self):
        """Gets the base_order_id of this OrderRefundInfoV2.

        退订金额、已消费金额或收取退订手续费对应的原订单ID。

        :return: The base_order_id of this OrderRefundInfoV2.
        :rtype: str
        """
        return self._base_order_id

    @base_order_id.setter
    def base_order_id(self, base_order_id):
        """Sets the base_order_id of this OrderRefundInfoV2.

        退订金额、已消费金额或收取退订手续费对应的原订单ID。

        :param base_order_id: The base_order_id of this OrderRefundInfoV2.
        :type base_order_id: str
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
        if not isinstance(other, OrderRefundInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
