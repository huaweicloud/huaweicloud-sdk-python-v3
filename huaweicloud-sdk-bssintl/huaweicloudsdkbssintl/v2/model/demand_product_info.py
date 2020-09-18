# coding: utf-8

import pprint
import re

import six





class DemandProductInfo:


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
        'usage_factor': 'str',
        'usage_value': 'float',
        'usage_measure_id': 'int',
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
        'usage_factor': 'usage_factor',
        'usage_value': 'usage_value',
        'usage_measure_id': 'usage_measure_id',
        'subscription_num': 'subscription_num'
    }

    def __init__(self, id=None, cloud_service_type=None, resource_type=None, resource_spec=None, region=None, available_zone=None, resource_size=None, size_measure_id=None, usage_factor=None, usage_value=None, usage_measure_id=None, subscription_num=None):
        """DemandProductInfo - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec = None
        self._region = None
        self._available_zone = None
        self._resource_size = None
        self._size_measure_id = None
        self._usage_factor = None
        self._usage_value = None
        self._usage_measure_id = None
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
        self.usage_factor = usage_factor
        self.usage_value = usage_value
        self.usage_measure_id = usage_measure_id
        self.subscription_num = subscription_num

    @property
    def id(self):
        """Gets the id of this DemandProductInfo.

        |参数名称：ID标识| |参数约束及描述：同一次询价中不能重复，用于标识返回询价结果和请求的映射关系|

        :return: The id of this DemandProductInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DemandProductInfo.

        |参数名称：ID标识| |参数约束及描述：同一次询价中不能重复，用于标识返回询价结果和请求的映射关系|

        :param id: The id of this DemandProductInfo.
        :type: str
        """
        self._id = id

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this DemandProductInfo.

        |参数名称：用户购买云服务产品的云服务类型| |参数约束及描述：例如EC2，云服务类型为hws.service.type.ec2|

        :return: The cloud_service_type of this DemandProductInfo.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this DemandProductInfo.

        |参数名称：用户购买云服务产品的云服务类型| |参数约束及描述：例如EC2，云服务类型为hws.service.type.ec2|

        :param cloud_service_type: The cloud_service_type of this DemandProductInfo.
        :type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        """Gets the resource_type of this DemandProductInfo.

        |参数名称：用户购买云服务产品的资源类型| |参数约束及描述：例如EC2中的VM，资源类型为hws.resource.type.vm。ResourceType是CloudServiceType中的一种资源，CloudServiceType由多种ResourceType组合提供|

        :return: The resource_type of this DemandProductInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this DemandProductInfo.

        |参数名称：用户购买云服务产品的资源类型| |参数约束及描述：例如EC2中的VM，资源类型为hws.resource.type.vm。ResourceType是CloudServiceType中的一种资源，CloudServiceType由多种ResourceType组合提供|

        :param resource_type: The resource_type of this DemandProductInfo.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec(self):
        """Gets the resource_spec of this DemandProductInfo.

        |参数名称：用户购买云服务产品的资源规格| |参数约束及描述：例如VM的小型规格，资源规格为m1.tiny|

        :return: The resource_spec of this DemandProductInfo.
        :rtype: str
        """
        return self._resource_spec

    @resource_spec.setter
    def resource_spec(self, resource_spec):
        """Sets the resource_spec of this DemandProductInfo.

        |参数名称：用户购买云服务产品的资源规格| |参数约束及描述：例如VM的小型规格，资源规格为m1.tiny|

        :param resource_spec: The resource_spec of this DemandProductInfo.
        :type: str
        """
        self._resource_spec = resource_spec

    @property
    def region(self):
        """Gets the region of this DemandProductInfo.

        |参数名称：云服务区编码| |参数约束及描述：云服务区编码|

        :return: The region of this DemandProductInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DemandProductInfo.

        |参数名称：云服务区编码| |参数约束及描述：云服务区编码|

        :param region: The region of this DemandProductInfo.
        :type: str
        """
        self._region = region

    @property
    def available_zone(self):
        """Gets the available_zone of this DemandProductInfo.

        |参数名称：可用区标识| |参数约束及描述：可用区标识|

        :return: The available_zone of this DemandProductInfo.
        :rtype: str
        """
        return self._available_zone

    @available_zone.setter
    def available_zone(self, available_zone):
        """Sets the available_zone of this DemandProductInfo.

        |参数名称：可用区标识| |参数约束及描述：可用区标识|

        :param available_zone: The available_zone of this DemandProductInfo.
        :type: str
        """
        self._available_zone = available_zone

    @property
    def resource_size(self):
        """Gets the resource_size of this DemandProductInfo.

        |参数名称：资源容量大小| |参数约束及描述：例如购买的卷大小或带宽大小，只有线性产品才有这个字段|

        :return: The resource_size of this DemandProductInfo.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        """Sets the resource_size of this DemandProductInfo.

        |参数名称：资源容量大小| |参数约束及描述：例如购买的卷大小或带宽大小，只有线性产品才有这个字段|

        :param resource_size: The resource_size of this DemandProductInfo.
        :type: int
        """
        self._resource_size = resource_size

    @property
    def size_measure_id(self):
        """Gets the size_measure_id of this DemandProductInfo.

        |参数名称：资源容量度量标识| |参数约束及描述：枚举值如下：15：Mbps（购买带宽时使用）17：GB（购买云硬盘时使用）14：个只有线性产品才有这个字段|

        :return: The size_measure_id of this DemandProductInfo.
        :rtype: int
        """
        return self._size_measure_id

    @size_measure_id.setter
    def size_measure_id(self, size_measure_id):
        """Sets the size_measure_id of this DemandProductInfo.

        |参数名称：资源容量度量标识| |参数约束及描述：枚举值如下：15：Mbps（购买带宽时使用）17：GB（购买云硬盘时使用）14：个只有线性产品才有这个字段|

        :param size_measure_id: The size_measure_id of this DemandProductInfo.
        :type: int
        """
        self._size_measure_id = size_measure_id

    @property
    def usage_factor(self):
        """Gets the usage_factor of this DemandProductInfo.

        |参数名称：使用量因子编码| |参数约束及描述：云服务器：Duration云硬盘：Duration弹性IP：Duration带宽：Duration或upflow市场镜像：Duration具体每种云服务使用什么样的计费因子，需要找具体云服务确认，全集请参考|

        :return: The usage_factor of this DemandProductInfo.
        :rtype: str
        """
        return self._usage_factor

    @usage_factor.setter
    def usage_factor(self, usage_factor):
        """Sets the usage_factor of this DemandProductInfo.

        |参数名称：使用量因子编码| |参数约束及描述：云服务器：Duration云硬盘：Duration弹性IP：Duration带宽：Duration或upflow市场镜像：Duration具体每种云服务使用什么样的计费因子，需要找具体云服务确认，全集请参考|

        :param usage_factor: The usage_factor of this DemandProductInfo.
        :type: str
        """
        self._usage_factor = usage_factor

    @property
    def usage_value(self):
        """Gets the usage_value of this DemandProductInfo.

        |参数名称：使用量值| |参数约束及描述：例如按小时询价，使用量值为1，使用量单位为小时|

        :return: The usage_value of this DemandProductInfo.
        :rtype: float
        """
        return self._usage_value

    @usage_value.setter
    def usage_value(self, usage_value):
        """Sets the usage_value of this DemandProductInfo.

        |参数名称：使用量值| |参数约束及描述：例如按小时询价，使用量值为1，使用量单位为小时|

        :param usage_value: The usage_value of this DemandProductInfo.
        :type: float
        """
        self._usage_value = usage_value

    @property
    def usage_measure_id(self):
        """Gets the usage_measure_id of this DemandProductInfo.

        |参数名称：使用量单位标识| |参数约束及描述：例如按小时询价，使用量值为1，使用量单位为小时，枚举值如下：4：小时全量枚举如下：0：天（时长）；1：元（货币）；2：角（货币）；3：分（货币）；4：小时（时长）；5：分钟（时长）；6：秒（时长）；7：EB（流量）；8：PB（流量）；9：TB（流量）；10：GB（流量）；11：MB（流量）；12：KB（流量）；13：Byte（流量）；14：个(次)（数量）；15：Mbps（流量）；16：Byte（容量）；17：GB（容量）；18：KLOC（行数）；19：年（周期）；20：月（周期）；21：MB（容量）；22：赫兹（频率）；23：核（数量）；24：天（周期）；25：小时（周期）；30：个数（个数）；31：千次（数量）；32：百万次（数量）；33：十亿次（数量）；34：bps（带宽速率）；35：kbps（带宽速率）；36：Mbps（带宽速率）；37：Gbps（带宽速率）；38：Tbps（带宽速率）；39：GB-秒（容量时长）；40：次（数量）；41：个（数量）；42：千个（数量）；43：张（数量）；44：千张（数量）；45：每秒查询率（查询速率）；46：人/天（数量）；47：TB（容量）；48：PB（容量）。具体某个云服务应该使用什么单位，需要和云服务确认。|

        :return: The usage_measure_id of this DemandProductInfo.
        :rtype: int
        """
        return self._usage_measure_id

    @usage_measure_id.setter
    def usage_measure_id(self, usage_measure_id):
        """Sets the usage_measure_id of this DemandProductInfo.

        |参数名称：使用量单位标识| |参数约束及描述：例如按小时询价，使用量值为1，使用量单位为小时，枚举值如下：4：小时全量枚举如下：0：天（时长）；1：元（货币）；2：角（货币）；3：分（货币）；4：小时（时长）；5：分钟（时长）；6：秒（时长）；7：EB（流量）；8：PB（流量）；9：TB（流量）；10：GB（流量）；11：MB（流量）；12：KB（流量）；13：Byte（流量）；14：个(次)（数量）；15：Mbps（流量）；16：Byte（容量）；17：GB（容量）；18：KLOC（行数）；19：年（周期）；20：月（周期）；21：MB（容量）；22：赫兹（频率）；23：核（数量）；24：天（周期）；25：小时（周期）；30：个数（个数）；31：千次（数量）；32：百万次（数量）；33：十亿次（数量）；34：bps（带宽速率）；35：kbps（带宽速率）；36：Mbps（带宽速率）；37：Gbps（带宽速率）；38：Tbps（带宽速率）；39：GB-秒（容量时长）；40：次（数量）；41：个（数量）；42：千个（数量）；43：张（数量）；44：千张（数量）；45：每秒查询率（查询速率）；46：人/天（数量）；47：TB（容量）；48：PB（容量）。具体某个云服务应该使用什么单位，需要和云服务确认。|

        :param usage_measure_id: The usage_measure_id of this DemandProductInfo.
        :type: int
        """
        self._usage_measure_id = usage_measure_id

    @property
    def subscription_num(self):
        """Gets the subscription_num of this DemandProductInfo.

        |参数名称：订购数量| |参数约束及描述：订购数量,有值时不能小于0，默认为1|

        :return: The subscription_num of this DemandProductInfo.
        :rtype: int
        """
        return self._subscription_num

    @subscription_num.setter
    def subscription_num(self, subscription_num):
        """Sets the subscription_num of this DemandProductInfo.

        |参数名称：订购数量| |参数约束及描述：订购数量,有值时不能小于0，默认为1|

        :param subscription_num: The subscription_num of this DemandProductInfo.
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
        if not isinstance(other, DemandProductInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
