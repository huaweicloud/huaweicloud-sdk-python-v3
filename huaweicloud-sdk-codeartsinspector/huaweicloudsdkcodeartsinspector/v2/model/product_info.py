# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_service_type': 'str',
        'product_id': 'str',
        'resource_speccode': 'str',
        'resource_type': 'str',
        'resouce_size_measure_id': 'int',
        'resource_size': 'int'
    }

    attribute_map = {
        'cloud_service_type': 'cloud_service_type',
        'product_id': 'product_id',
        'resource_speccode': 'resource_speccode',
        'resource_type': 'resource_type',
        'resouce_size_measure_id': 'resouce_size_measure_id',
        'resource_size': 'resource_size'
    }

    def __init__(self, cloud_service_type=None, product_id=None, resource_speccode=None, resource_type=None, resouce_size_measure_id=None, resource_size=None):
        r"""ProductInfo

        The model defined in huaweicloud sdk

        :param cloud_service_type: 用户购买的云服务的主云服务类型
        :type cloud_service_type: str
        :param product_id: 产品标识，通过订购询价接口获得
        :type product_id: str
        :param resource_speccode: 用户购买云服务产品的资源规格
        :type resource_speccode: str
        :param resource_type: 用户购买云服务产品的资源类型
        :type resource_type: str
        :param resouce_size_measure_id: 资源容量度量标识，购买vss服务时使用14： 15：Mbps（购买带宽时使用） 17：GB（购买云硬盘时使用） 14：个/次
        :type resouce_size_measure_id: int
        :param resource_size: 资源容量大小
        :type resource_size: int
        """
        
        

        self._cloud_service_type = None
        self._product_id = None
        self._resource_speccode = None
        self._resource_type = None
        self._resouce_size_measure_id = None
        self._resource_size = None
        self.discriminator = None

        self.cloud_service_type = cloud_service_type
        self.product_id = product_id
        self.resource_speccode = resource_speccode
        self.resource_type = resource_type
        if resouce_size_measure_id is not None:
            self.resouce_size_measure_id = resouce_size_measure_id
        if resource_size is not None:
            self.resource_size = resource_size

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this ProductInfo.

        用户购买的云服务的主云服务类型

        :return: The cloud_service_type of this ProductInfo.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this ProductInfo.

        用户购买的云服务的主云服务类型

        :param cloud_service_type: The cloud_service_type of this ProductInfo.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def product_id(self):
        r"""Gets the product_id of this ProductInfo.

        产品标识，通过订购询价接口获得

        :return: The product_id of this ProductInfo.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ProductInfo.

        产品标识，通过订购询价接口获得

        :param product_id: The product_id of this ProductInfo.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def resource_speccode(self):
        r"""Gets the resource_speccode of this ProductInfo.

        用户购买云服务产品的资源规格

        :return: The resource_speccode of this ProductInfo.
        :rtype: str
        """
        return self._resource_speccode

    @resource_speccode.setter
    def resource_speccode(self, resource_speccode):
        r"""Sets the resource_speccode of this ProductInfo.

        用户购买云服务产品的资源规格

        :param resource_speccode: The resource_speccode of this ProductInfo.
        :type resource_speccode: str
        """
        self._resource_speccode = resource_speccode

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ProductInfo.

        用户购买云服务产品的资源类型

        :return: The resource_type of this ProductInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ProductInfo.

        用户购买云服务产品的资源类型

        :param resource_type: The resource_type of this ProductInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resouce_size_measure_id(self):
        r"""Gets the resouce_size_measure_id of this ProductInfo.

        资源容量度量标识，购买vss服务时使用14： 15：Mbps（购买带宽时使用） 17：GB（购买云硬盘时使用） 14：个/次

        :return: The resouce_size_measure_id of this ProductInfo.
        :rtype: int
        """
        return self._resouce_size_measure_id

    @resouce_size_measure_id.setter
    def resouce_size_measure_id(self, resouce_size_measure_id):
        r"""Sets the resouce_size_measure_id of this ProductInfo.

        资源容量度量标识，购买vss服务时使用14： 15：Mbps（购买带宽时使用） 17：GB（购买云硬盘时使用） 14：个/次

        :param resouce_size_measure_id: The resouce_size_measure_id of this ProductInfo.
        :type resouce_size_measure_id: int
        """
        self._resouce_size_measure_id = resouce_size_measure_id

    @property
    def resource_size(self):
        r"""Gets the resource_size of this ProductInfo.

        资源容量大小

        :return: The resource_size of this ProductInfo.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        r"""Sets the resource_size of this ProductInfo.

        资源容量大小

        :param resource_size: The resource_size of this ProductInfo.
        :type resource_size: int
        """
        self._resource_size = resource_size

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
        if not isinstance(other, ProductInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
