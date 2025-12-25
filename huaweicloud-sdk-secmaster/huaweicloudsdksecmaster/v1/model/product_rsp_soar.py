# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductRspSoar:

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
        'resource_type': 'str',
        'resource_spec_code': 'str',
        'resource_size_measure_id': 'int',
        'usage_factor': 'str',
        'usage_measure_id': 'int',
        'region_id': 'str'
    }

    attribute_map = {
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code',
        'resource_size_measure_id': 'resource_size_measure_id',
        'usage_factor': 'usage_factor',
        'usage_measure_id': 'usage_measure_id',
        'region_id': 'region_id'
    }

    def __init__(self, cloud_service_type=None, resource_type=None, resource_spec_code=None, resource_size_measure_id=None, usage_factor=None, usage_measure_id=None, region_id=None):
        r"""ProductRspSoar

        The model defined in huaweicloud sdk

        :param cloud_service_type: 云服务产品的主服务类型，云脑默认为：hws.service.type.sa
        :type cloud_service_type: str
        :param resource_type: 资源类型编码
        :type resource_type: str
        :param resource_spec_code: 资源规格编码
        :type resource_spec_code: str
        :param resource_size_measure_id: 资源容量度量标识
        :type resource_size_measure_id: int
        :param usage_factor: 使用量因子，按需计费必填，取值和话单中的使用量因子一致，云服务和使用量因子对应关系如下: 云脑目前支持有： duration： 时间，主要针对主版本(basic、standard、professional) count：次数，主要针对安全编排 flow：流量，主要针对日志分析和采集 retention：保留，主要针对日志保留
        :type usage_factor: str
        :param usage_measure_id: 使用量单位标识，按需询价必填，例如按小时询价，使用量值为1，使用量单位为小时，枚举值如下： 4：小时 10：GB（带宽按流量询价使用） 11：MB（带宽按流量询价使用） 13：Byte（带宽按流量询价使用）
        :type usage_measure_id: int
        :param region_id: 当前region编码，默认为null，即为当前region
        :type region_id: str
        """
        
        

        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec_code = None
        self._resource_size_measure_id = None
        self._usage_factor = None
        self._usage_measure_id = None
        self._region_id = None
        self.discriminator = None

        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if resource_size_measure_id is not None:
            self.resource_size_measure_id = resource_size_measure_id
        if usage_factor is not None:
            self.usage_factor = usage_factor
        if usage_measure_id is not None:
            self.usage_measure_id = usage_measure_id
        if region_id is not None:
            self.region_id = region_id

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this ProductRspSoar.

        云服务产品的主服务类型，云脑默认为：hws.service.type.sa

        :return: The cloud_service_type of this ProductRspSoar.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this ProductRspSoar.

        云服务产品的主服务类型，云脑默认为：hws.service.type.sa

        :param cloud_service_type: The cloud_service_type of this ProductRspSoar.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ProductRspSoar.

        资源类型编码

        :return: The resource_type of this ProductRspSoar.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ProductRspSoar.

        资源类型编码

        :param resource_type: The resource_type of this ProductRspSoar.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this ProductRspSoar.

        资源规格编码

        :return: The resource_spec_code of this ProductRspSoar.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this ProductRspSoar.

        资源规格编码

        :param resource_spec_code: The resource_spec_code of this ProductRspSoar.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def resource_size_measure_id(self):
        r"""Gets the resource_size_measure_id of this ProductRspSoar.

        资源容量度量标识

        :return: The resource_size_measure_id of this ProductRspSoar.
        :rtype: int
        """
        return self._resource_size_measure_id

    @resource_size_measure_id.setter
    def resource_size_measure_id(self, resource_size_measure_id):
        r"""Sets the resource_size_measure_id of this ProductRspSoar.

        资源容量度量标识

        :param resource_size_measure_id: The resource_size_measure_id of this ProductRspSoar.
        :type resource_size_measure_id: int
        """
        self._resource_size_measure_id = resource_size_measure_id

    @property
    def usage_factor(self):
        r"""Gets the usage_factor of this ProductRspSoar.

        使用量因子，按需计费必填，取值和话单中的使用量因子一致，云服务和使用量因子对应关系如下: 云脑目前支持有： duration： 时间，主要针对主版本(basic、standard、professional) count：次数，主要针对安全编排 flow：流量，主要针对日志分析和采集 retention：保留，主要针对日志保留

        :return: The usage_factor of this ProductRspSoar.
        :rtype: str
        """
        return self._usage_factor

    @usage_factor.setter
    def usage_factor(self, usage_factor):
        r"""Sets the usage_factor of this ProductRspSoar.

        使用量因子，按需计费必填，取值和话单中的使用量因子一致，云服务和使用量因子对应关系如下: 云脑目前支持有： duration： 时间，主要针对主版本(basic、standard、professional) count：次数，主要针对安全编排 flow：流量，主要针对日志分析和采集 retention：保留，主要针对日志保留

        :param usage_factor: The usage_factor of this ProductRspSoar.
        :type usage_factor: str
        """
        self._usage_factor = usage_factor

    @property
    def usage_measure_id(self):
        r"""Gets the usage_measure_id of this ProductRspSoar.

        使用量单位标识，按需询价必填，例如按小时询价，使用量值为1，使用量单位为小时，枚举值如下： 4：小时 10：GB（带宽按流量询价使用） 11：MB（带宽按流量询价使用） 13：Byte（带宽按流量询价使用）

        :return: The usage_measure_id of this ProductRspSoar.
        :rtype: int
        """
        return self._usage_measure_id

    @usage_measure_id.setter
    def usage_measure_id(self, usage_measure_id):
        r"""Sets the usage_measure_id of this ProductRspSoar.

        使用量单位标识，按需询价必填，例如按小时询价，使用量值为1，使用量单位为小时，枚举值如下： 4：小时 10：GB（带宽按流量询价使用） 11：MB（带宽按流量询价使用） 13：Byte（带宽按流量询价使用）

        :param usage_measure_id: The usage_measure_id of this ProductRspSoar.
        :type usage_measure_id: int
        """
        self._usage_measure_id = usage_measure_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ProductRspSoar.

        当前region编码，默认为null，即为当前region

        :return: The region_id of this ProductRspSoar.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ProductRspSoar.

        当前region编码，默认为null，即为当前region

        :param region_id: The region_id of this ProductRspSoar.
        :type region_id: str
        """
        self._region_id = region_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProductRspSoar):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
