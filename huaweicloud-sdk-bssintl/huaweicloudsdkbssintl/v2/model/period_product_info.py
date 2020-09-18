# coding: utf-8

import pprint
import re

import six





class PeriodProductInfo:


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
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'resource_spec': 'str',
        'region': 'str',
        'available_zone': 'str',
        'resource_size': 'int',
        'size_measure_id': 'int',
        'period_type': 'int',
        'period_num': 'int',
        'subscription_num': 'int'
    }

    attribute_map = {
        'id': 'id',
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'resource_spec': 'resource_spec',
        'region': 'region',
        'available_zone': 'available_zone',
        'resource_size': 'resource_size',
        'size_measure_id': 'size_measure_id',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'subscription_num': 'subscription_num'
    }

    def __init__(self, id=None, cloud_service_type=None, resource_type=None, resource_spec=None, region=None, available_zone=None, resource_size=None, size_measure_id=None, period_type=None, period_num=None, subscription_num=None):
        """PeriodProductInfo - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec = None
        self._region = None
        self._available_zone = None
        self._resource_size = None
        self._size_measure_id = None
        self._period_type = None
        self._period_num = None
        self._subscription_num = None
        self.discriminator = None

        self.id = id
        self.cloud_service_type = cloud_service_type
        self.resource_type = resource_type
        self.resource_spec = resource_spec
        self.region = region
        if available_zone is not None:
            self.available_zone = available_zone
        if resource_size is not None:
            self.resource_size = resource_size
        if size_measure_id is not None:
            self.size_measure_id = size_measure_id
        self.period_type = period_type
        self.period_num = period_num
        self.subscription_num = subscription_num

    @property
    def id(self):
        """Gets the id of this PeriodProductInfo.

        |参数名称：ID标识| |参数约束及描述：同一次询价中不能重复，用于标识返回询价结果和请求的映射关系|

        :return: The id of this PeriodProductInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PeriodProductInfo.

        |参数名称：ID标识| |参数约束及描述：同一次询价中不能重复，用于标识返回询价结果和请求的映射关系|

        :param id: The id of this PeriodProductInfo.
        :type: str
        """
        self._id = id

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this PeriodProductInfo.

        |参数名称：用户购买云服务产品的云服务类型| |参数约束及描述：例如EC2，云服务类型为hws.service.type.ec2|

        :return: The cloud_service_type of this PeriodProductInfo.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this PeriodProductInfo.

        |参数名称：用户购买云服务产品的云服务类型| |参数约束及描述：例如EC2，云服务类型为hws.service.type.ec2|

        :param cloud_service_type: The cloud_service_type of this PeriodProductInfo.
        :type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        """Gets the resource_type of this PeriodProductInfo.

        |参数名称：用户购买云服务产品的资源类型| |参数约束及描述：例如EC2中的VM，资源类型为hws.resource.type.vm。ResourceType是CloudServiceType中的一种资源，CloudServiceType由多种ResourceType组合提供|

        :return: The resource_type of this PeriodProductInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this PeriodProductInfo.

        |参数名称：用户购买云服务产品的资源类型| |参数约束及描述：例如EC2中的VM，资源类型为hws.resource.type.vm。ResourceType是CloudServiceType中的一种资源，CloudServiceType由多种ResourceType组合提供|

        :param resource_type: The resource_type of this PeriodProductInfo.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec(self):
        """Gets the resource_spec of this PeriodProductInfo.

        |参数名称：用户购买云服务产品的资源规格| |参数约束及描述：例如VM的小型规格，资源规格为m1.tiny|

        :return: The resource_spec of this PeriodProductInfo.
        :rtype: str
        """
        return self._resource_spec

    @resource_spec.setter
    def resource_spec(self, resource_spec):
        """Sets the resource_spec of this PeriodProductInfo.

        |参数名称：用户购买云服务产品的资源规格| |参数约束及描述：例如VM的小型规格，资源规格为m1.tiny|

        :param resource_spec: The resource_spec of this PeriodProductInfo.
        :type: str
        """
        self._resource_spec = resource_spec

    @property
    def region(self):
        """Gets the region of this PeriodProductInfo.

        |参数名称：云服务区编码| |参数约束及描述：云服务区编码|

        :return: The region of this PeriodProductInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this PeriodProductInfo.

        |参数名称：云服务区编码| |参数约束及描述：云服务区编码|

        :param region: The region of this PeriodProductInfo.
        :type: str
        """
        self._region = region

    @property
    def available_zone(self):
        """Gets the available_zone of this PeriodProductInfo.

        |参数名称：可用区标识| |参数约束及描述：可用区标识|

        :return: The available_zone of this PeriodProductInfo.
        :rtype: str
        """
        return self._available_zone

    @available_zone.setter
    def available_zone(self, available_zone):
        """Sets the available_zone of this PeriodProductInfo.

        |参数名称：可用区标识| |参数约束及描述：可用区标识|

        :param available_zone: The available_zone of this PeriodProductInfo.
        :type: str
        """
        self._available_zone = available_zone

    @property
    def resource_size(self):
        """Gets the resource_size of this PeriodProductInfo.

        |参数名称：资源容量大小| |参数约束及描述：例如购买的卷大小或带宽大小，只有线性产品才有这个字段|

        :return: The resource_size of this PeriodProductInfo.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        """Sets the resource_size of this PeriodProductInfo.

        |参数名称：资源容量大小| |参数约束及描述：例如购买的卷大小或带宽大小，只有线性产品才有这个字段|

        :param resource_size: The resource_size of this PeriodProductInfo.
        :type: int
        """
        self._resource_size = resource_size

    @property
    def size_measure_id(self):
        """Gets the size_measure_id of this PeriodProductInfo.

        |参数名称：资源容量度量标识| |参数约束及描述：枚举值如下：15：Mbps（购买带宽时使用）17：GB（购买云硬盘时使用）14：个只有线性产品才有这个字段|

        :return: The size_measure_id of this PeriodProductInfo.
        :rtype: int
        """
        return self._size_measure_id

    @size_measure_id.setter
    def size_measure_id(self, size_measure_id):
        """Sets the size_measure_id of this PeriodProductInfo.

        |参数名称：资源容量度量标识| |参数约束及描述：枚举值如下：15：Mbps（购买带宽时使用）17：GB（购买云硬盘时使用）14：个只有线性产品才有这个字段|

        :param size_measure_id: The size_measure_id of this PeriodProductInfo.
        :type: int
        """
        self._size_measure_id = size_measure_id

    @property
    def period_type(self):
        """Gets the period_type of this PeriodProductInfo.

        |参数名称：订购周期类型| |参数约束及描述：0：天；1：周；2：月；3：年；4：小时；|

        :return: The period_type of this PeriodProductInfo.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this PeriodProductInfo.

        |参数名称：订购周期类型| |参数约束及描述：0：天；1：周；2：月；3：年；4：小时；|

        :param period_type: The period_type of this PeriodProductInfo.
        :type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this PeriodProductInfo.

        |参数名称：订购周期数| |参数约束及描述：订购周期数|

        :return: The period_num of this PeriodProductInfo.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this PeriodProductInfo.

        |参数名称：订购周期数| |参数约束及描述：订购周期数|

        :param period_num: The period_num of this PeriodProductInfo.
        :type: int
        """
        self._period_num = period_num

    @property
    def subscription_num(self):
        """Gets the subscription_num of this PeriodProductInfo.

        |参数名称：订购数量| |参数约束及描述：订购数量,有值时不能小于0|

        :return: The subscription_num of this PeriodProductInfo.
        :rtype: int
        """
        return self._subscription_num

    @subscription_num.setter
    def subscription_num(self, subscription_num):
        """Sets the subscription_num of this PeriodProductInfo.

        |参数名称：订购数量| |参数约束及描述：订购数量,有值时不能小于0|

        :param subscription_num: The subscription_num of this PeriodProductInfo.
        :type: int
        """
        self._subscription_num = subscription_num

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
        if not isinstance(other, PeriodProductInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
