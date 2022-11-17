# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricDataDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'value': 'int',
        'read_at': 'datetime',
        'dimension': 'MetricDataDetailDimension'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'read_at': 'read_at',
        'dimension': 'dimension'
    }

    def __init__(self, name=None, value=None, read_at=None, dimension=None):
        """MetricDataDetail

        The model defined in huaweicloud sdk

        :param name: 监控指标名称，当前包含指标： - cpu_used：该维度vCPU已使用核数，单位：个，支持维度：site_id，flavor - cpu_available_total：用户可使用该维度vCPU总核数，单位：个，支持维度：site_id，flavor - cpu_total：该维度vCPU总核数（包含HA等预留核数），单位：个，支持维度：site_id，flavor - memory_used：该维度内存已使用量，单位：Gb，支持维度：site_id，flavor - memory_available_total：用户可使用该维度内存总量，单位：Gb，支持维度：site_id，flavor - memory_total：该维度内存总量（包含HA等预留内存量），单位：Gb，支持维度：site_id，flavor - capacity_used：该维度块存储资源已使用量，单位：GiB，支持维度：site_id，storage - capacity_available_total：用户可使用该维度块存储资源总容量（用户订购开通的存储容量），单位：GiB，支持维度：site_id，storage - capacity_total：当前已订购的资源场景下该维度块存储资源最大容量（订购资源包含的存储容量可能大于用户已开通容量），单位：GiB，支持维度：site_id，storage - available：该维度对应规格剩余可发放数量，单位：台，支持维度：flavor_capacity
        :type name: str
        :param value: 监控值
        :type value: int
        :param read_at: 记录更新时间
        :type read_at: datetime
        :param dimension: 
        :type dimension: :class:`huaweicloudsdkies.v1.MetricDataDetailDimension`
        """
        
        

        self._name = None
        self._value = None
        self._read_at = None
        self._dimension = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if read_at is not None:
            self.read_at = read_at
        if dimension is not None:
            self.dimension = dimension

    @property
    def name(self):
        """Gets the name of this MetricDataDetail.

        监控指标名称，当前包含指标： - cpu_used：该维度vCPU已使用核数，单位：个，支持维度：site_id，flavor - cpu_available_total：用户可使用该维度vCPU总核数，单位：个，支持维度：site_id，flavor - cpu_total：该维度vCPU总核数（包含HA等预留核数），单位：个，支持维度：site_id，flavor - memory_used：该维度内存已使用量，单位：Gb，支持维度：site_id，flavor - memory_available_total：用户可使用该维度内存总量，单位：Gb，支持维度：site_id，flavor - memory_total：该维度内存总量（包含HA等预留内存量），单位：Gb，支持维度：site_id，flavor - capacity_used：该维度块存储资源已使用量，单位：GiB，支持维度：site_id，storage - capacity_available_total：用户可使用该维度块存储资源总容量（用户订购开通的存储容量），单位：GiB，支持维度：site_id，storage - capacity_total：当前已订购的资源场景下该维度块存储资源最大容量（订购资源包含的存储容量可能大于用户已开通容量），单位：GiB，支持维度：site_id，storage - available：该维度对应规格剩余可发放数量，单位：台，支持维度：flavor_capacity

        :return: The name of this MetricDataDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetricDataDetail.

        监控指标名称，当前包含指标： - cpu_used：该维度vCPU已使用核数，单位：个，支持维度：site_id，flavor - cpu_available_total：用户可使用该维度vCPU总核数，单位：个，支持维度：site_id，flavor - cpu_total：该维度vCPU总核数（包含HA等预留核数），单位：个，支持维度：site_id，flavor - memory_used：该维度内存已使用量，单位：Gb，支持维度：site_id，flavor - memory_available_total：用户可使用该维度内存总量，单位：Gb，支持维度：site_id，flavor - memory_total：该维度内存总量（包含HA等预留内存量），单位：Gb，支持维度：site_id，flavor - capacity_used：该维度块存储资源已使用量，单位：GiB，支持维度：site_id，storage - capacity_available_total：用户可使用该维度块存储资源总容量（用户订购开通的存储容量），单位：GiB，支持维度：site_id，storage - capacity_total：当前已订购的资源场景下该维度块存储资源最大容量（订购资源包含的存储容量可能大于用户已开通容量），单位：GiB，支持维度：site_id，storage - available：该维度对应规格剩余可发放数量，单位：台，支持维度：flavor_capacity

        :param name: The name of this MetricDataDetail.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this MetricDataDetail.

        监控值

        :return: The value of this MetricDataDetail.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MetricDataDetail.

        监控值

        :param value: The value of this MetricDataDetail.
        :type value: int
        """
        self._value = value

    @property
    def read_at(self):
        """Gets the read_at of this MetricDataDetail.

        记录更新时间

        :return: The read_at of this MetricDataDetail.
        :rtype: datetime
        """
        return self._read_at

    @read_at.setter
    def read_at(self, read_at):
        """Sets the read_at of this MetricDataDetail.

        记录更新时间

        :param read_at: The read_at of this MetricDataDetail.
        :type read_at: datetime
        """
        self._read_at = read_at

    @property
    def dimension(self):
        """Gets the dimension of this MetricDataDetail.

        :return: The dimension of this MetricDataDetail.
        :rtype: :class:`huaweicloudsdkies.v1.MetricDataDetailDimension`
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this MetricDataDetail.

        :param dimension: The dimension of this MetricDataDetail.
        :type dimension: :class:`huaweicloudsdkies.v1.MetricDataDetailDimension`
        """
        self._dimension = dimension

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
        if not isinstance(other, MetricDataDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
