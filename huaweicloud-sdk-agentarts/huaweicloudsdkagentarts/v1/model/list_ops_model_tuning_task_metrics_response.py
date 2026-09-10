# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsModelTuningTaskMetricsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'metrics': 'list[OpsTuningStepMetric]'
    }

    attribute_map = {
        'total': 'total',
        'metrics': 'metrics'
    }

    def __init__(self, total=None, metrics=None):
        r"""ListOpsModelTuningTaskMetricsResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释：** 满足条件的指标记录总数，用于计算分页总页数，单位：条。  **取值范围：** 大于等于0的整数。
        :type total: int
        :param metrics: **参数解释：** 当前分页下的训练指标详情列表。  **取值范围：** 符合OpsTuningStepMetric定义的对象数组。
        :type metrics: list[:class:`huaweicloudsdkagentarts.v1.OpsTuningStepMetric`]
        """
        
        super().__init__()

        self._total = None
        self._metrics = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if metrics is not None:
            self.metrics = metrics

    @property
    def total(self):
        r"""Gets the total of this ListOpsModelTuningTaskMetricsResponse.

        **参数解释：** 满足条件的指标记录总数，用于计算分页总页数，单位：条。  **取值范围：** 大于等于0的整数。

        :return: The total of this ListOpsModelTuningTaskMetricsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListOpsModelTuningTaskMetricsResponse.

        **参数解释：** 满足条件的指标记录总数，用于计算分页总页数，单位：条。  **取值范围：** 大于等于0的整数。

        :param total: The total of this ListOpsModelTuningTaskMetricsResponse.
        :type total: int
        """
        self._total = total

    @property
    def metrics(self):
        r"""Gets the metrics of this ListOpsModelTuningTaskMetricsResponse.

        **参数解释：** 当前分页下的训练指标详情列表。  **取值范围：** 符合OpsTuningStepMetric定义的对象数组。

        :return: The metrics of this ListOpsModelTuningTaskMetricsResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTuningStepMetric`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this ListOpsModelTuningTaskMetricsResponse.

        **参数解释：** 当前分页下的训练指标详情列表。  **取值范围：** 符合OpsTuningStepMetric定义的对象数组。

        :param metrics: The metrics of this ListOpsModelTuningTaskMetricsResponse.
        :type metrics: list[:class:`huaweicloudsdkagentarts.v1.OpsTuningStepMetric`]
        """
        self._metrics = metrics

    def to_dict(self):
        import warnings
        warnings.warn("ListOpsModelTuningTaskMetricsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListOpsModelTuningTaskMetricsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
