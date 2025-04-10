# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductInfoBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'all_resource_names': 'list[str]',
        'cloud_service_type': 'str',
        'display_id': 'str',
        'product_id': 'str',
        'product_spec_desc': 'str',
        'resource_name': 'str',
        'resource_size': 'int',
        'resource_size_measure_id': 'int',
        'resource_spec_code': 'str',
        'resource_type': 'str',
        'usage_factor': 'str',
        'usage_measure_id': 'int',
        'usage_value': 'float'
    }

    attribute_map = {
        'all_resource_names': 'all_resource_names',
        'cloud_service_type': 'cloud_service_type',
        'display_id': 'display_id',
        'product_id': 'product_id',
        'product_spec_desc': 'product_spec_desc',
        'resource_name': 'resource_name',
        'resource_size': 'resource_size',
        'resource_size_measure_id': 'resource_size_measure_id',
        'resource_spec_code': 'resource_spec_code',
        'resource_type': 'resource_type',
        'usage_factor': 'usage_factor',
        'usage_measure_id': 'usage_measure_id',
        'usage_value': 'usage_value'
    }

    def __init__(self, all_resource_names=None, cloud_service_type=None, display_id=None, product_id=None, product_spec_desc=None, resource_name=None, resource_size=None, resource_size_measure_id=None, resource_spec_code=None, resource_type=None, usage_factor=None, usage_measure_id=None, usage_value=None):
        r"""ProductInfoBean

        The model defined in huaweicloud sdk

        :param all_resource_names: 资源名称列表
        :type all_resource_names: list[str]
        :param cloud_service_type: 云服务类型
        :type cloud_service_type: str
        :param display_id: 展示ID
        :type display_id: str
        :param product_id: 产品ID
        :type product_id: str
        :param product_spec_desc: 产品规格描述
        :type product_spec_desc: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_size: 产品支持的数据库数量，或者支持obs的扫描量
        :type resource_size: int
        :param resource_size_measure_id: 资源容量度量标识，枚举值举例如下：15：mbps（购买带宽时使用），17：gb（购买云硬盘时使用），14：个/次
        :type resource_size_measure_id: int
        :param resource_spec_code: 产品编码
        :type resource_spec_code: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param usage_factor: 已使用系数
        :type usage_factor: str
        :param usage_measure_id: 已使用容量度量标识
        :type usage_measure_id: int
        :param usage_value: 已使用值
        :type usage_value: float
        """
        
        

        self._all_resource_names = None
        self._cloud_service_type = None
        self._display_id = None
        self._product_id = None
        self._product_spec_desc = None
        self._resource_name = None
        self._resource_size = None
        self._resource_size_measure_id = None
        self._resource_spec_code = None
        self._resource_type = None
        self._usage_factor = None
        self._usage_measure_id = None
        self._usage_value = None
        self.discriminator = None

        if all_resource_names is not None:
            self.all_resource_names = all_resource_names
        self.cloud_service_type = cloud_service_type
        if display_id is not None:
            self.display_id = display_id
        self.product_id = product_id
        if product_spec_desc is not None:
            self.product_spec_desc = product_spec_desc
        if resource_name is not None:
            self.resource_name = resource_name
        self.resource_size = resource_size
        self.resource_size_measure_id = resource_size_measure_id
        self.resource_spec_code = resource_spec_code
        self.resource_type = resource_type
        if usage_factor is not None:
            self.usage_factor = usage_factor
        if usage_measure_id is not None:
            self.usage_measure_id = usage_measure_id
        if usage_value is not None:
            self.usage_value = usage_value

    @property
    def all_resource_names(self):
        r"""Gets the all_resource_names of this ProductInfoBean.

        资源名称列表

        :return: The all_resource_names of this ProductInfoBean.
        :rtype: list[str]
        """
        return self._all_resource_names

    @all_resource_names.setter
    def all_resource_names(self, all_resource_names):
        r"""Sets the all_resource_names of this ProductInfoBean.

        资源名称列表

        :param all_resource_names: The all_resource_names of this ProductInfoBean.
        :type all_resource_names: list[str]
        """
        self._all_resource_names = all_resource_names

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this ProductInfoBean.

        云服务类型

        :return: The cloud_service_type of this ProductInfoBean.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this ProductInfoBean.

        云服务类型

        :param cloud_service_type: The cloud_service_type of this ProductInfoBean.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def display_id(self):
        r"""Gets the display_id of this ProductInfoBean.

        展示ID

        :return: The display_id of this ProductInfoBean.
        :rtype: str
        """
        return self._display_id

    @display_id.setter
    def display_id(self, display_id):
        r"""Sets the display_id of this ProductInfoBean.

        展示ID

        :param display_id: The display_id of this ProductInfoBean.
        :type display_id: str
        """
        self._display_id = display_id

    @property
    def product_id(self):
        r"""Gets the product_id of this ProductInfoBean.

        产品ID

        :return: The product_id of this ProductInfoBean.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ProductInfoBean.

        产品ID

        :param product_id: The product_id of this ProductInfoBean.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def product_spec_desc(self):
        r"""Gets the product_spec_desc of this ProductInfoBean.

        产品规格描述

        :return: The product_spec_desc of this ProductInfoBean.
        :rtype: str
        """
        return self._product_spec_desc

    @product_spec_desc.setter
    def product_spec_desc(self, product_spec_desc):
        r"""Sets the product_spec_desc of this ProductInfoBean.

        产品规格描述

        :param product_spec_desc: The product_spec_desc of this ProductInfoBean.
        :type product_spec_desc: str
        """
        self._product_spec_desc = product_spec_desc

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ProductInfoBean.

        资源名称

        :return: The resource_name of this ProductInfoBean.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ProductInfoBean.

        资源名称

        :param resource_name: The resource_name of this ProductInfoBean.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_size(self):
        r"""Gets the resource_size of this ProductInfoBean.

        产品支持的数据库数量，或者支持obs的扫描量

        :return: The resource_size of this ProductInfoBean.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        r"""Sets the resource_size of this ProductInfoBean.

        产品支持的数据库数量，或者支持obs的扫描量

        :param resource_size: The resource_size of this ProductInfoBean.
        :type resource_size: int
        """
        self._resource_size = resource_size

    @property
    def resource_size_measure_id(self):
        r"""Gets the resource_size_measure_id of this ProductInfoBean.

        资源容量度量标识，枚举值举例如下：15：mbps（购买带宽时使用），17：gb（购买云硬盘时使用），14：个/次

        :return: The resource_size_measure_id of this ProductInfoBean.
        :rtype: int
        """
        return self._resource_size_measure_id

    @resource_size_measure_id.setter
    def resource_size_measure_id(self, resource_size_measure_id):
        r"""Sets the resource_size_measure_id of this ProductInfoBean.

        资源容量度量标识，枚举值举例如下：15：mbps（购买带宽时使用），17：gb（购买云硬盘时使用），14：个/次

        :param resource_size_measure_id: The resource_size_measure_id of this ProductInfoBean.
        :type resource_size_measure_id: int
        """
        self._resource_size_measure_id = resource_size_measure_id

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this ProductInfoBean.

        产品编码

        :return: The resource_spec_code of this ProductInfoBean.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this ProductInfoBean.

        产品编码

        :param resource_spec_code: The resource_spec_code of this ProductInfoBean.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ProductInfoBean.

        资源类型

        :return: The resource_type of this ProductInfoBean.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ProductInfoBean.

        资源类型

        :param resource_type: The resource_type of this ProductInfoBean.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def usage_factor(self):
        r"""Gets the usage_factor of this ProductInfoBean.

        已使用系数

        :return: The usage_factor of this ProductInfoBean.
        :rtype: str
        """
        return self._usage_factor

    @usage_factor.setter
    def usage_factor(self, usage_factor):
        r"""Sets the usage_factor of this ProductInfoBean.

        已使用系数

        :param usage_factor: The usage_factor of this ProductInfoBean.
        :type usage_factor: str
        """
        self._usage_factor = usage_factor

    @property
    def usage_measure_id(self):
        r"""Gets the usage_measure_id of this ProductInfoBean.

        已使用容量度量标识

        :return: The usage_measure_id of this ProductInfoBean.
        :rtype: int
        """
        return self._usage_measure_id

    @usage_measure_id.setter
    def usage_measure_id(self, usage_measure_id):
        r"""Sets the usage_measure_id of this ProductInfoBean.

        已使用容量度量标识

        :param usage_measure_id: The usage_measure_id of this ProductInfoBean.
        :type usage_measure_id: int
        """
        self._usage_measure_id = usage_measure_id

    @property
    def usage_value(self):
        r"""Gets the usage_value of this ProductInfoBean.

        已使用值

        :return: The usage_value of this ProductInfoBean.
        :rtype: float
        """
        return self._usage_value

    @usage_value.setter
    def usage_value(self, usage_value):
        r"""Sets the usage_value of this ProductInfoBean.

        已使用值

        :param usage_value: The usage_value of this ProductInfoBean.
        :type usage_value: float
        """
        self._usage_value = usage_value

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
        if not isinstance(other, ProductInfoBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
