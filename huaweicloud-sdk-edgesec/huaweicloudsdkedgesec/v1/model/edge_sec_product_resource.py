# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeSecProductResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_id': 'str',
        'cloud_service_type': 'str',
        'product_id': 'str',
        'resource_id': 'str',
        'enterprise_project_id': 'str',
        'region_id': 'str',
        'resource_type': 'str',
        'resource_spec_code': 'str',
        'resource_size': 'int',
        'bill_type': 'int',
        'charging_mode': 'str'
    }

    attribute_map = {
        'order_id': 'order_id',
        'cloud_service_type': 'cloud_service_type',
        'product_id': 'product_id',
        'resource_id': 'resource_id',
        'enterprise_project_id': 'enterprise_project_id',
        'region_id': 'region_id',
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code',
        'resource_size': 'resource_size',
        'bill_type': 'bill_type',
        'charging_mode': 'charging_mode'
    }

    def __init__(self, order_id=None, cloud_service_type=None, product_id=None, resource_id=None, enterprise_project_id=None, region_id=None, resource_type=None, resource_spec_code=None, resource_size=None, bill_type=None, charging_mode=None):
        """EdgeSecProductResource

        The model defined in huaweicloud sdk

        :param order_id: 购买该资源的订单ID
        :type order_id: str
        :param cloud_service_type: 云服务类型，边缘安全为hws.service.type.edgesec
        :type cloud_service_type: str
        :param product_id: 产品ID
        :type product_id: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param region_id: region ID
        :type region_id: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param resource_spec_code: 资源规格编码
        :type resource_spec_code: str
        :param resource_size: 扩展包资源数量
        :type resource_size: int
        :param bill_type: 计费方式（0:不按照流量计费， 1:带宽峰值， 2:流量）
        :type bill_type: int
        :param charging_mode: 收费模式（1:一次性、包周期（包年包月）， 2:按需计费）
        :type charging_mode: str
        """
        
        

        self._order_id = None
        self._cloud_service_type = None
        self._product_id = None
        self._resource_id = None
        self._enterprise_project_id = None
        self._region_id = None
        self._resource_type = None
        self._resource_spec_code = None
        self._resource_size = None
        self._bill_type = None
        self._charging_mode = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if product_id is not None:
            self.product_id = product_id
        if resource_id is not None:
            self.resource_id = resource_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if region_id is not None:
            self.region_id = region_id
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if resource_size is not None:
            self.resource_size = resource_size
        if bill_type is not None:
            self.bill_type = bill_type
        if charging_mode is not None:
            self.charging_mode = charging_mode

    @property
    def order_id(self):
        """Gets the order_id of this EdgeSecProductResource.

        购买该资源的订单ID

        :return: The order_id of this EdgeSecProductResource.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this EdgeSecProductResource.

        购买该资源的订单ID

        :param order_id: The order_id of this EdgeSecProductResource.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this EdgeSecProductResource.

        云服务类型，边缘安全为hws.service.type.edgesec

        :return: The cloud_service_type of this EdgeSecProductResource.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this EdgeSecProductResource.

        云服务类型，边缘安全为hws.service.type.edgesec

        :param cloud_service_type: The cloud_service_type of this EdgeSecProductResource.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def product_id(self):
        """Gets the product_id of this EdgeSecProductResource.

        产品ID

        :return: The product_id of this EdgeSecProductResource.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this EdgeSecProductResource.

        产品ID

        :param product_id: The product_id of this EdgeSecProductResource.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def resource_id(self):
        """Gets the resource_id of this EdgeSecProductResource.

        资源ID

        :return: The resource_id of this EdgeSecProductResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this EdgeSecProductResource.

        资源ID

        :param resource_id: The resource_id of this EdgeSecProductResource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this EdgeSecProductResource.

        企业项目ID

        :return: The enterprise_project_id of this EdgeSecProductResource.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this EdgeSecProductResource.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this EdgeSecProductResource.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def region_id(self):
        """Gets the region_id of this EdgeSecProductResource.

        region ID

        :return: The region_id of this EdgeSecProductResource.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this EdgeSecProductResource.

        region ID

        :param region_id: The region_id of this EdgeSecProductResource.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def resource_type(self):
        """Gets the resource_type of this EdgeSecProductResource.

        资源类型

        :return: The resource_type of this EdgeSecProductResource.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this EdgeSecProductResource.

        资源类型

        :param resource_type: The resource_type of this EdgeSecProductResource.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this EdgeSecProductResource.

        资源规格编码

        :return: The resource_spec_code of this EdgeSecProductResource.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this EdgeSecProductResource.

        资源规格编码

        :param resource_spec_code: The resource_spec_code of this EdgeSecProductResource.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def resource_size(self):
        """Gets the resource_size of this EdgeSecProductResource.

        扩展包资源数量

        :return: The resource_size of this EdgeSecProductResource.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        """Sets the resource_size of this EdgeSecProductResource.

        扩展包资源数量

        :param resource_size: The resource_size of this EdgeSecProductResource.
        :type resource_size: int
        """
        self._resource_size = resource_size

    @property
    def bill_type(self):
        """Gets the bill_type of this EdgeSecProductResource.

        计费方式（0:不按照流量计费， 1:带宽峰值， 2:流量）

        :return: The bill_type of this EdgeSecProductResource.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this EdgeSecProductResource.

        计费方式（0:不按照流量计费， 1:带宽峰值， 2:流量）

        :param bill_type: The bill_type of this EdgeSecProductResource.
        :type bill_type: int
        """
        self._bill_type = bill_type

    @property
    def charging_mode(self):
        """Gets the charging_mode of this EdgeSecProductResource.

        收费模式（1:一次性、包周期（包年包月）， 2:按需计费）

        :return: The charging_mode of this EdgeSecProductResource.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this EdgeSecProductResource.

        收费模式（1:一次性、包周期（包年包月）， 2:按需计费）

        :param charging_mode: The charging_mode of this EdgeSecProductResource.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

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
        if not isinstance(other, EdgeSecProductResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
