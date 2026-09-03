# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetInstancesOpsMetricNamesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'metric_group': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'metric_group': 'metric_group',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, metric_group=None, x_language=None):
        r"""GetInstancesOpsMetricNamesRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。
        :type instance_id: str
        :param metric_group: **参数解释**：  监控指标分组名称。  **约束限制**：  不涉及。  **取值范围**：  - realtimeMetric（实时指标） - highRequest（高请求指标） - slowSql（慢SQL指标） - lockWait（锁等待指标） - diskLimit（磁盘限制指标） - memoryLimit（内存限制指标） - importantMetric（重要指标）  **默认取值**：  不涉及。
        :type metric_group: str
        :param x_language: **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认取值**：  en-us。
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._metric_group = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        self.metric_group = metric_group
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this GetInstancesOpsMetricNamesRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :return: The instance_id of this GetInstancesOpsMetricNamesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this GetInstancesOpsMetricNamesRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this GetInstancesOpsMetricNamesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def metric_group(self):
        r"""Gets the metric_group of this GetInstancesOpsMetricNamesRequest.

        **参数解释**：  监控指标分组名称。  **约束限制**：  不涉及。  **取值范围**：  - realtimeMetric（实时指标） - highRequest（高请求指标） - slowSql（慢SQL指标） - lockWait（锁等待指标） - diskLimit（磁盘限制指标） - memoryLimit（内存限制指标） - importantMetric（重要指标）  **默认取值**：  不涉及。

        :return: The metric_group of this GetInstancesOpsMetricNamesRequest.
        :rtype: str
        """
        return self._metric_group

    @metric_group.setter
    def metric_group(self, metric_group):
        r"""Sets the metric_group of this GetInstancesOpsMetricNamesRequest.

        **参数解释**：  监控指标分组名称。  **约束限制**：  不涉及。  **取值范围**：  - realtimeMetric（实时指标） - highRequest（高请求指标） - slowSql（慢SQL指标） - lockWait（锁等待指标） - diskLimit（磁盘限制指标） - memoryLimit（内存限制指标） - importantMetric（重要指标）  **默认取值**：  不涉及。

        :param metric_group: The metric_group of this GetInstancesOpsMetricNamesRequest.
        :type metric_group: str
        """
        self._metric_group = metric_group

    @property
    def x_language(self):
        r"""Gets the x_language of this GetInstancesOpsMetricNamesRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认取值**：  en-us。

        :return: The x_language of this GetInstancesOpsMetricNamesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this GetInstancesOpsMetricNamesRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认取值**：  en-us。

        :param x_language: The x_language of this GetInstancesOpsMetricNamesRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, GetInstancesOpsMetricNamesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
