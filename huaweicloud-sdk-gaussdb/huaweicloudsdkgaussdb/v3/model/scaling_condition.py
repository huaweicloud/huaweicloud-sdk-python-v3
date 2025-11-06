# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScalingCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'condition_id': 'str',
        'duration': 'int',
        'interval': 'int',
        'metric_conditions': 'list[MetricCondition]'
    }

    attribute_map = {
        'condition_id': 'condition_id',
        'duration': 'duration',
        'interval': 'interval',
        'metric_conditions': 'metric_conditions'
    }

    def __init__(self, condition_id=None, duration=None, interval=None, metric_conditions=None):
        r"""ScalingCondition

        The model defined in huaweicloud sdk

        :param condition_id: **参数描述**:  变配条件名称。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字和中划线组成，且长度不超过32个字符，不能为空。  **默认取值**：  不涉及。
        :type condition_id: str
        :param duration: **参数描述**：  持续时间，单位是毫秒。  **约束限制**：  不涉及。  **取值范围**：  2000-5000。  **默认取值**：  不涉及。
        :type duration: int
        :param interval: **参数解释**:  间隔时间，单位是毫秒。  **约束限制**：  不涉及。  **取值范围**：  1000-5000。  **默认取值**：  不涉及。
        :type interval: int
        :param metric_conditions: **参数描述**:  指标变配条件。  **约束条件**：  不涉及。
        :type metric_conditions: list[:class:`huaweicloudsdkgaussdb.v3.MetricCondition`]
        """
        
        

        self._condition_id = None
        self._duration = None
        self._interval = None
        self._metric_conditions = None
        self.discriminator = None

        if condition_id is not None:
            self.condition_id = condition_id
        if duration is not None:
            self.duration = duration
        if interval is not None:
            self.interval = interval
        if metric_conditions is not None:
            self.metric_conditions = metric_conditions

    @property
    def condition_id(self):
        r"""Gets the condition_id of this ScalingCondition.

        **参数描述**:  变配条件名称。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字和中划线组成，且长度不超过32个字符，不能为空。  **默认取值**：  不涉及。

        :return: The condition_id of this ScalingCondition.
        :rtype: str
        """
        return self._condition_id

    @condition_id.setter
    def condition_id(self, condition_id):
        r"""Sets the condition_id of this ScalingCondition.

        **参数描述**:  变配条件名称。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字和中划线组成，且长度不超过32个字符，不能为空。  **默认取值**：  不涉及。

        :param condition_id: The condition_id of this ScalingCondition.
        :type condition_id: str
        """
        self._condition_id = condition_id

    @property
    def duration(self):
        r"""Gets the duration of this ScalingCondition.

        **参数描述**：  持续时间，单位是毫秒。  **约束限制**：  不涉及。  **取值范围**：  2000-5000。  **默认取值**：  不涉及。

        :return: The duration of this ScalingCondition.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ScalingCondition.

        **参数描述**：  持续时间，单位是毫秒。  **约束限制**：  不涉及。  **取值范围**：  2000-5000。  **默认取值**：  不涉及。

        :param duration: The duration of this ScalingCondition.
        :type duration: int
        """
        self._duration = duration

    @property
    def interval(self):
        r"""Gets the interval of this ScalingCondition.

        **参数解释**:  间隔时间，单位是毫秒。  **约束限制**：  不涉及。  **取值范围**：  1000-5000。  **默认取值**：  不涉及。

        :return: The interval of this ScalingCondition.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this ScalingCondition.

        **参数解释**:  间隔时间，单位是毫秒。  **约束限制**：  不涉及。  **取值范围**：  1000-5000。  **默认取值**：  不涉及。

        :param interval: The interval of this ScalingCondition.
        :type interval: int
        """
        self._interval = interval

    @property
    def metric_conditions(self):
        r"""Gets the metric_conditions of this ScalingCondition.

        **参数描述**:  指标变配条件。  **约束条件**：  不涉及。

        :return: The metric_conditions of this ScalingCondition.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.MetricCondition`]
        """
        return self._metric_conditions

    @metric_conditions.setter
    def metric_conditions(self, metric_conditions):
        r"""Sets the metric_conditions of this ScalingCondition.

        **参数描述**:  指标变配条件。  **约束条件**：  不涉及。

        :param metric_conditions: The metric_conditions of this ScalingCondition.
        :type metric_conditions: list[:class:`huaweicloudsdkgaussdb.v3.MetricCondition`]
        """
        self._metric_conditions = metric_conditions

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
        if not isinstance(other, ScalingCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
