# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SloInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'slo_objectives': 'list[SloObjectives]',
        'predict_window_seconds': 'int'
    }

    attribute_map = {
        'slo_objectives': 'slo_objectives',
        'predict_window_seconds': 'predict_window_seconds'
    }

    def __init__(self, slo_objectives=None, predict_window_seconds=None):
        r"""SloInfo

        The model defined in huaweicloud sdk

        :param slo_objectives: **参数解释：** 仿真期望指标。 **取值范围：** 不涉及。
        :type slo_objectives: list[:class:`huaweicloudsdkmodelarts.v1.SloObjectives`]
        :param predict_window_seconds: **参数解释：** 预测时间窗口。 **约束限制：** 60~600。 **取值范围：** 不涉及。 **默认取值：** 60。
        :type predict_window_seconds: int
        """
        
        

        self._slo_objectives = None
        self._predict_window_seconds = None
        self.discriminator = None

        self.slo_objectives = slo_objectives
        if predict_window_seconds is not None:
            self.predict_window_seconds = predict_window_seconds

    @property
    def slo_objectives(self):
        r"""Gets the slo_objectives of this SloInfo.

        **参数解释：** 仿真期望指标。 **取值范围：** 不涉及。

        :return: The slo_objectives of this SloInfo.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.SloObjectives`]
        """
        return self._slo_objectives

    @slo_objectives.setter
    def slo_objectives(self, slo_objectives):
        r"""Sets the slo_objectives of this SloInfo.

        **参数解释：** 仿真期望指标。 **取值范围：** 不涉及。

        :param slo_objectives: The slo_objectives of this SloInfo.
        :type slo_objectives: list[:class:`huaweicloudsdkmodelarts.v1.SloObjectives`]
        """
        self._slo_objectives = slo_objectives

    @property
    def predict_window_seconds(self):
        r"""Gets the predict_window_seconds of this SloInfo.

        **参数解释：** 预测时间窗口。 **约束限制：** 60~600。 **取值范围：** 不涉及。 **默认取值：** 60。

        :return: The predict_window_seconds of this SloInfo.
        :rtype: int
        """
        return self._predict_window_seconds

    @predict_window_seconds.setter
    def predict_window_seconds(self, predict_window_seconds):
        r"""Sets the predict_window_seconds of this SloInfo.

        **参数解释：** 预测时间窗口。 **约束限制：** 60~600。 **取值范围：** 不涉及。 **默认取值：** 60。

        :param predict_window_seconds: The predict_window_seconds of this SloInfo.
        :type predict_window_seconds: int
        """
        self._predict_window_seconds = predict_window_seconds

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
        if not isinstance(other, SloInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
