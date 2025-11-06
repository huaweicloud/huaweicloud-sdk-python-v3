# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordingRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recording_rule': 'str'
    }

    attribute_map = {
        'recording_rule': 'recording_rule'
    }

    def __init__(self, recording_rule=None):
        r"""RecordingRuleRequest

        The model defined in huaweicloud sdk

        :param recording_rule: 预聚合规则。 待创建的预聚合规则详细信息。支持如下子参数： - groups：规则组。一份RecordingRule.yaml可以配置多组规则组。 - name：规则组名称。规则组名称必须唯一。 - interval：规则组的执行周期。默认60s。（可选） - rules：规则。一个规则组可以包含多条规则。 - record：规则的名称。聚合规则的名称必须符合  [Prometheus指标名称规范](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels)。  - expr：计算表达式。Prometheus监控将通过该表达式计算得出预聚合指标。计算表达式必须符合[PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/)。 - labels：指标的标签。标签必须符合[Prometheus指标标签规范](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels)。（可选）
        :type recording_rule: str
        """
        
        

        self._recording_rule = None
        self.discriminator = None

        self.recording_rule = recording_rule

    @property
    def recording_rule(self):
        r"""Gets the recording_rule of this RecordingRuleRequest.

        预聚合规则。 待创建的预聚合规则详细信息。支持如下子参数： - groups：规则组。一份RecordingRule.yaml可以配置多组规则组。 - name：规则组名称。规则组名称必须唯一。 - interval：规则组的执行周期。默认60s。（可选） - rules：规则。一个规则组可以包含多条规则。 - record：规则的名称。聚合规则的名称必须符合  [Prometheus指标名称规范](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels)。  - expr：计算表达式。Prometheus监控将通过该表达式计算得出预聚合指标。计算表达式必须符合[PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/)。 - labels：指标的标签。标签必须符合[Prometheus指标标签规范](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels)。（可选）

        :return: The recording_rule of this RecordingRuleRequest.
        :rtype: str
        """
        return self._recording_rule

    @recording_rule.setter
    def recording_rule(self, recording_rule):
        r"""Sets the recording_rule of this RecordingRuleRequest.

        预聚合规则。 待创建的预聚合规则详细信息。支持如下子参数： - groups：规则组。一份RecordingRule.yaml可以配置多组规则组。 - name：规则组名称。规则组名称必须唯一。 - interval：规则组的执行周期。默认60s。（可选） - rules：规则。一个规则组可以包含多条规则。 - record：规则的名称。聚合规则的名称必须符合  [Prometheus指标名称规范](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels)。  - expr：计算表达式。Prometheus监控将通过该表达式计算得出预聚合指标。计算表达式必须符合[PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/)。 - labels：指标的标签。标签必须符合[Prometheus指标标签规范](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels)。（可选）

        :param recording_rule: The recording_rule of this RecordingRuleRequest.
        :type recording_rule: str
        """
        self._recording_rule = recording_rule

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
        if not isinstance(other, RecordingRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
