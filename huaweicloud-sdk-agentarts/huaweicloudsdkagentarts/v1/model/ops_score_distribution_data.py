# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsScoreDistributionData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluator_distrution_info': 'list[OpsEvaluatorScoreDistribution]'
    }

    attribute_map = {
        'evaluator_distrution_info': 'evaluator_distrution_info'
    }

    def __init__(self, evaluator_distrution_info=None):
        r"""OpsScoreDistributionData

        The model defined in huaweicloud sdk

        :param evaluator_distrution_info: **参数解释：** 各评估器的得分分布信息列表。 **取值范围：** 不涉及。 
        :type evaluator_distrution_info: list[:class:`huaweicloudsdkagentarts.v1.OpsEvaluatorScoreDistribution`]
        """
        
        

        self._evaluator_distrution_info = None
        self.discriminator = None

        if evaluator_distrution_info is not None:
            self.evaluator_distrution_info = evaluator_distrution_info

    @property
    def evaluator_distrution_info(self):
        r"""Gets the evaluator_distrution_info of this OpsScoreDistributionData.

        **参数解释：** 各评估器的得分分布信息列表。 **取值范围：** 不涉及。 

        :return: The evaluator_distrution_info of this OpsScoreDistributionData.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsEvaluatorScoreDistribution`]
        """
        return self._evaluator_distrution_info

    @evaluator_distrution_info.setter
    def evaluator_distrution_info(self, evaluator_distrution_info):
        r"""Sets the evaluator_distrution_info of this OpsScoreDistributionData.

        **参数解释：** 各评估器的得分分布信息列表。 **取值范围：** 不涉及。 

        :param evaluator_distrution_info: The evaluator_distrution_info of this OpsScoreDistributionData.
        :type evaluator_distrution_info: list[:class:`huaweicloudsdkagentarts.v1.OpsEvaluatorScoreDistribution`]
        """
        self._evaluator_distrution_info = evaluator_distrution_info

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
        if not isinstance(other, OpsScoreDistributionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
