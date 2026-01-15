# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SummaryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'high_risk': 'int',
        'medium_risk': 'int',
        'normal': 'int',
        'suggestion': 'int'
    }

    attribute_map = {
        'high_risk': 'highRisk',
        'medium_risk': 'mediumRisk',
        'normal': 'normal',
        'suggestion': 'suggestion'
    }

    def __init__(self, high_risk=None, medium_risk=None, normal=None, suggestion=None):
        r"""SummaryInfo

        The model defined in huaweicloud sdk

        :param high_risk: **参数解释**： 集群风险概要。 **取值范围**： 不涉及
        :type high_risk: int
        :param medium_risk: **参数解释**： 集群风险检测项判定为中风险的数量。 **取值范围**： 0-100
        :type medium_risk: int
        :param normal: **参数解释： 集群风险检测项判定为正常项的数量。 **取值范围**： 0-100
        :type normal: int
        :param suggestion: **参数解释**： 集群风险检测项判定为提示项的数量。 **取值范围**： 0-100
        :type suggestion: int
        """
        
        

        self._high_risk = None
        self._medium_risk = None
        self._normal = None
        self._suggestion = None
        self.discriminator = None

        if high_risk is not None:
            self.high_risk = high_risk
        if medium_risk is not None:
            self.medium_risk = medium_risk
        if normal is not None:
            self.normal = normal
        if suggestion is not None:
            self.suggestion = suggestion

    @property
    def high_risk(self):
        r"""Gets the high_risk of this SummaryInfo.

        **参数解释**： 集群风险概要。 **取值范围**： 不涉及

        :return: The high_risk of this SummaryInfo.
        :rtype: int
        """
        return self._high_risk

    @high_risk.setter
    def high_risk(self, high_risk):
        r"""Sets the high_risk of this SummaryInfo.

        **参数解释**： 集群风险概要。 **取值范围**： 不涉及

        :param high_risk: The high_risk of this SummaryInfo.
        :type high_risk: int
        """
        self._high_risk = high_risk

    @property
    def medium_risk(self):
        r"""Gets the medium_risk of this SummaryInfo.

        **参数解释**： 集群风险检测项判定为中风险的数量。 **取值范围**： 0-100

        :return: The medium_risk of this SummaryInfo.
        :rtype: int
        """
        return self._medium_risk

    @medium_risk.setter
    def medium_risk(self, medium_risk):
        r"""Sets the medium_risk of this SummaryInfo.

        **参数解释**： 集群风险检测项判定为中风险的数量。 **取值范围**： 0-100

        :param medium_risk: The medium_risk of this SummaryInfo.
        :type medium_risk: int
        """
        self._medium_risk = medium_risk

    @property
    def normal(self):
        r"""Gets the normal of this SummaryInfo.

        **参数解释： 集群风险检测项判定为正常项的数量。 **取值范围**： 0-100

        :return: The normal of this SummaryInfo.
        :rtype: int
        """
        return self._normal

    @normal.setter
    def normal(self, normal):
        r"""Sets the normal of this SummaryInfo.

        **参数解释： 集群风险检测项判定为正常项的数量。 **取值范围**： 0-100

        :param normal: The normal of this SummaryInfo.
        :type normal: int
        """
        self._normal = normal

    @property
    def suggestion(self):
        r"""Gets the suggestion of this SummaryInfo.

        **参数解释**： 集群风险检测项判定为提示项的数量。 **取值范围**： 0-100

        :return: The suggestion of this SummaryInfo.
        :rtype: int
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        r"""Sets the suggestion of this SummaryInfo.

        **参数解释**： 集群风险检测项判定为提示项的数量。 **取值范围**： 0-100

        :param suggestion: The suggestion of this SummaryInfo.
        :type suggestion: int
        """
        self._suggestion = suggestion

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
        if not isinstance(other, SummaryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
