# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SloObjectives:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_ttft': 'int',
        'metric_tpot': 'int',
        'percental': 'int'
    }

    attribute_map = {
        'metric_ttft': 'metric_ttft',
        'metric_tpot': 'metric_tpot',
        'percental': 'percental'
    }

    def __init__(self, metric_ttft=None, metric_tpot=None, percental=None):
        r"""SloObjectives

        The model defined in huaweicloud sdk

        :param metric_ttft: **参数解释：** TTFT指标，单位毫秒。 **取值范围：** 0~10000。 **约束限制：** 不涉及。 **默认取值：** 100。
        :type metric_ttft: int
        :param metric_tpot: **参数解释：** TPOT指标，单位毫秒。 **取值范围：** 0~1000。 **约束限制：** 不涉及。 **默认取值：** 50。
        :type metric_tpot: int
        :param percental: **参数解释：** SLO满足百分比。 **取值范围：** 0~100。
        :type percental: int
        """
        
        

        self._metric_ttft = None
        self._metric_tpot = None
        self._percental = None
        self.discriminator = None

        if metric_ttft is not None:
            self.metric_ttft = metric_ttft
        if metric_tpot is not None:
            self.metric_tpot = metric_tpot
        if percental is not None:
            self.percental = percental

    @property
    def metric_ttft(self):
        r"""Gets the metric_ttft of this SloObjectives.

        **参数解释：** TTFT指标，单位毫秒。 **取值范围：** 0~10000。 **约束限制：** 不涉及。 **默认取值：** 100。

        :return: The metric_ttft of this SloObjectives.
        :rtype: int
        """
        return self._metric_ttft

    @metric_ttft.setter
    def metric_ttft(self, metric_ttft):
        r"""Sets the metric_ttft of this SloObjectives.

        **参数解释：** TTFT指标，单位毫秒。 **取值范围：** 0~10000。 **约束限制：** 不涉及。 **默认取值：** 100。

        :param metric_ttft: The metric_ttft of this SloObjectives.
        :type metric_ttft: int
        """
        self._metric_ttft = metric_ttft

    @property
    def metric_tpot(self):
        r"""Gets the metric_tpot of this SloObjectives.

        **参数解释：** TPOT指标，单位毫秒。 **取值范围：** 0~1000。 **约束限制：** 不涉及。 **默认取值：** 50。

        :return: The metric_tpot of this SloObjectives.
        :rtype: int
        """
        return self._metric_tpot

    @metric_tpot.setter
    def metric_tpot(self, metric_tpot):
        r"""Sets the metric_tpot of this SloObjectives.

        **参数解释：** TPOT指标，单位毫秒。 **取值范围：** 0~1000。 **约束限制：** 不涉及。 **默认取值：** 50。

        :param metric_tpot: The metric_tpot of this SloObjectives.
        :type metric_tpot: int
        """
        self._metric_tpot = metric_tpot

    @property
    def percental(self):
        r"""Gets the percental of this SloObjectives.

        **参数解释：** SLO满足百分比。 **取值范围：** 0~100。

        :return: The percental of this SloObjectives.
        :rtype: int
        """
        return self._percental

    @percental.setter
    def percental(self, percental):
        r"""Sets the percental of this SloObjectives.

        **参数解释：** SLO满足百分比。 **取值范围：** 0~100。

        :param percental: The percental of this SloObjectives.
        :type percental: int
        """
        self._percental = percental

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
        if not isinstance(other, SloObjectives):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
