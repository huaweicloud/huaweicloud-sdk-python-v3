# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductPostPaid:

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
        'product_id': 'str',
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'resource_spec_code': 'str',
        'usage_measure_id': 'int',
        'usage_value': 'float',
        'resource_size': 'int',
        'usage_factor': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'product_id': 'product_id',
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code',
        'usage_measure_id': 'usage_measure_id',
        'usage_value': 'usage_value',
        'resource_size': 'resource_size',
        'usage_factor': 'usage_factor',
        'resource_id': 'resource_id'
    }

    def __init__(self, id=None, product_id=None, cloud_service_type=None, resource_type=None, resource_spec_code=None, usage_measure_id=None, usage_value=None, resource_size=None, usage_factor=None, resource_id=None):
        r"""ProductPostPaid

        The model defined in huaweicloud sdk

        :param id: ID标识，同一次询价中不能重复，用于标识返回询价结果和请求的映射关系
        :type id: str
        :param product_id: 产品Id，通过向CBC询价获取该商品的标识
        :type product_id: str
        :param cloud_service_type: 云服务类型，固定值为hws.service.type.sa
        :type cloud_service_type: str
        :param resource_type: 用户购买云服务产品的资源类型，例如SecMaster中的典型场景配置，资源类型为hws.resource.type.secmaster.typical
        :type resource_type: str
        :param resource_spec_code: 用户购买云服务产品的资源规格，例如安全云脑中的基础版，资源规格为secmaster.basic
        :type resource_spec_code: str
        :param usage_measure_id: 使用量单位标识，按需询价必填，例如按小时询价，使用量值为1，使用量单位为小时，枚举值如下： 4：小时 10：GB（带宽按流量询价使用） 11：MB（带宽按流量询价使用）
        :type usage_measure_id: int
        :param usage_value: 使用量值，按需询价必填，例如按小时询价，使用量值为1，使用量单位为小时
        :type usage_value: float
        :param resource_size: 配额个数
        :type resource_size: int
        :param usage_factor: 使用量因子，按需计费必填，取值和话单中的使用量因子一致，云服务和使用量因子对应关系如下： 典型场景配置：Duration 态势管理：duration 安全编排：count 智能分析：flow
        :type usage_factor: str
        :param resource_id: 资源id，仅在增加配额的时候传入
        :type resource_id: str
        """
        
        

        self._id = None
        self._product_id = None
        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec_code = None
        self._usage_measure_id = None
        self._usage_value = None
        self._resource_size = None
        self._usage_factor = None
        self._resource_id = None
        self.discriminator = None

        self.id = id
        self.product_id = product_id
        self.cloud_service_type = cloud_service_type
        self.resource_type = resource_type
        self.resource_spec_code = resource_spec_code
        self.usage_measure_id = usage_measure_id
        self.usage_value = usage_value
        self.resource_size = resource_size
        self.usage_factor = usage_factor
        if resource_id is not None:
            self.resource_id = resource_id

    @property
    def id(self):
        r"""Gets the id of this ProductPostPaid.

        ID标识，同一次询价中不能重复，用于标识返回询价结果和请求的映射关系

        :return: The id of this ProductPostPaid.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProductPostPaid.

        ID标识，同一次询价中不能重复，用于标识返回询价结果和请求的映射关系

        :param id: The id of this ProductPostPaid.
        :type id: str
        """
        self._id = id

    @property
    def product_id(self):
        r"""Gets the product_id of this ProductPostPaid.

        产品Id，通过向CBC询价获取该商品的标识

        :return: The product_id of this ProductPostPaid.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ProductPostPaid.

        产品Id，通过向CBC询价获取该商品的标识

        :param product_id: The product_id of this ProductPostPaid.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this ProductPostPaid.

        云服务类型，固定值为hws.service.type.sa

        :return: The cloud_service_type of this ProductPostPaid.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this ProductPostPaid.

        云服务类型，固定值为hws.service.type.sa

        :param cloud_service_type: The cloud_service_type of this ProductPostPaid.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ProductPostPaid.

        用户购买云服务产品的资源类型，例如SecMaster中的典型场景配置，资源类型为hws.resource.type.secmaster.typical

        :return: The resource_type of this ProductPostPaid.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ProductPostPaid.

        用户购买云服务产品的资源类型，例如SecMaster中的典型场景配置，资源类型为hws.resource.type.secmaster.typical

        :param resource_type: The resource_type of this ProductPostPaid.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this ProductPostPaid.

        用户购买云服务产品的资源规格，例如安全云脑中的基础版，资源规格为secmaster.basic

        :return: The resource_spec_code of this ProductPostPaid.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this ProductPostPaid.

        用户购买云服务产品的资源规格，例如安全云脑中的基础版，资源规格为secmaster.basic

        :param resource_spec_code: The resource_spec_code of this ProductPostPaid.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def usage_measure_id(self):
        r"""Gets the usage_measure_id of this ProductPostPaid.

        使用量单位标识，按需询价必填，例如按小时询价，使用量值为1，使用量单位为小时，枚举值如下： 4：小时 10：GB（带宽按流量询价使用） 11：MB（带宽按流量询价使用）

        :return: The usage_measure_id of this ProductPostPaid.
        :rtype: int
        """
        return self._usage_measure_id

    @usage_measure_id.setter
    def usage_measure_id(self, usage_measure_id):
        r"""Sets the usage_measure_id of this ProductPostPaid.

        使用量单位标识，按需询价必填，例如按小时询价，使用量值为1，使用量单位为小时，枚举值如下： 4：小时 10：GB（带宽按流量询价使用） 11：MB（带宽按流量询价使用）

        :param usage_measure_id: The usage_measure_id of this ProductPostPaid.
        :type usage_measure_id: int
        """
        self._usage_measure_id = usage_measure_id

    @property
    def usage_value(self):
        r"""Gets the usage_value of this ProductPostPaid.

        使用量值，按需询价必填，例如按小时询价，使用量值为1，使用量单位为小时

        :return: The usage_value of this ProductPostPaid.
        :rtype: float
        """
        return self._usage_value

    @usage_value.setter
    def usage_value(self, usage_value):
        r"""Sets the usage_value of this ProductPostPaid.

        使用量值，按需询价必填，例如按小时询价，使用量值为1，使用量单位为小时

        :param usage_value: The usage_value of this ProductPostPaid.
        :type usage_value: float
        """
        self._usage_value = usage_value

    @property
    def resource_size(self):
        r"""Gets the resource_size of this ProductPostPaid.

        配额个数

        :return: The resource_size of this ProductPostPaid.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        r"""Sets the resource_size of this ProductPostPaid.

        配额个数

        :param resource_size: The resource_size of this ProductPostPaid.
        :type resource_size: int
        """
        self._resource_size = resource_size

    @property
    def usage_factor(self):
        r"""Gets the usage_factor of this ProductPostPaid.

        使用量因子，按需计费必填，取值和话单中的使用量因子一致，云服务和使用量因子对应关系如下： 典型场景配置：Duration 态势管理：duration 安全编排：count 智能分析：flow

        :return: The usage_factor of this ProductPostPaid.
        :rtype: str
        """
        return self._usage_factor

    @usage_factor.setter
    def usage_factor(self, usage_factor):
        r"""Sets the usage_factor of this ProductPostPaid.

        使用量因子，按需计费必填，取值和话单中的使用量因子一致，云服务和使用量因子对应关系如下： 典型场景配置：Duration 态势管理：duration 安全编排：count 智能分析：flow

        :param usage_factor: The usage_factor of this ProductPostPaid.
        :type usage_factor: str
        """
        self._usage_factor = usage_factor

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ProductPostPaid.

        资源id，仅在增加配额的时候传入

        :return: The resource_id of this ProductPostPaid.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ProductPostPaid.

        资源id，仅在增加配额的时候传入

        :param resource_id: The resource_id of this ProductPostPaid.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, ProductPostPaid):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
