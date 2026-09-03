# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetInstancesOpsMetricNamesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metrics': 'list[MetricItem]',
        'namespace': 'str',
        'dim': 'str'
    }

    attribute_map = {
        'metrics': 'metrics',
        'namespace': 'namespace',
        'dim': 'dim'
    }

    def __init__(self, metrics=None, namespace=None, dim=None):
        r"""GetInstancesOpsMetricNamesResponse

        The model defined in huaweicloud sdk

        :param metrics: **参数解释**：  监控指标项列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type metrics: list[:class:`huaweicloudsdkrds.v3.MetricItem`]
        :param namespace: **参数解释**：  CES命名空间。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type namespace: str
        :param dim: **参数解释**：  监控维度类型。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type dim: str
        """
        
        super().__init__()

        self._metrics = None
        self._namespace = None
        self._dim = None
        self.discriminator = None

        if metrics is not None:
            self.metrics = metrics
        if namespace is not None:
            self.namespace = namespace
        if dim is not None:
            self.dim = dim

    @property
    def metrics(self):
        r"""Gets the metrics of this GetInstancesOpsMetricNamesResponse.

        **参数解释**：  监控指标项列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The metrics of this GetInstancesOpsMetricNamesResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.MetricItem`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this GetInstancesOpsMetricNamesResponse.

        **参数解释**：  监控指标项列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param metrics: The metrics of this GetInstancesOpsMetricNamesResponse.
        :type metrics: list[:class:`huaweicloudsdkrds.v3.MetricItem`]
        """
        self._metrics = metrics

    @property
    def namespace(self):
        r"""Gets the namespace of this GetInstancesOpsMetricNamesResponse.

        **参数解释**：  CES命名空间。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The namespace of this GetInstancesOpsMetricNamesResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this GetInstancesOpsMetricNamesResponse.

        **参数解释**：  CES命名空间。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param namespace: The namespace of this GetInstancesOpsMetricNamesResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dim(self):
        r"""Gets the dim of this GetInstancesOpsMetricNamesResponse.

        **参数解释**：  监控维度类型。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The dim of this GetInstancesOpsMetricNamesResponse.
        :rtype: str
        """
        return self._dim

    @dim.setter
    def dim(self, dim):
        r"""Sets the dim of this GetInstancesOpsMetricNamesResponse.

        **参数解释**：  监控维度类型。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param dim: The dim of this GetInstancesOpsMetricNamesResponse.
        :type dim: str
        """
        self._dim = dim

    def to_dict(self):
        import warnings
        warnings.warn("GetInstancesOpsMetricNamesResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, GetInstancesOpsMetricNamesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
