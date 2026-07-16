# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsEvaluatorScoreDistribution:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluator_id': 'str',
        'evaluator_name': 'str',
        'distrution': 'list[OpsScoreCountItem]'
    }

    attribute_map = {
        'evaluator_id': 'evaluator_id',
        'evaluator_name': 'evaluator_name',
        'distrution': 'distrution'
    }

    def __init__(self, evaluator_id=None, evaluator_name=None, distrution=None):
        r"""OpsEvaluatorScoreDistribution

        The model defined in huaweicloud sdk

        :param evaluator_id: **参数解释：** 评估器的唯一标识符ID。 **取值范围：** UUID格式的字符串。 
        :type evaluator_id: str
        :param evaluator_name: **参数解释：** 评估器的显示名称。 **取值范围：** 1-100字符。 
        :type evaluator_name: str
        :param distrution: **参数解释：** 该评估器的得分分布列表，包含各分数及其对应的样本数量。 **取值范围：** 不涉及。 
        :type distrution: list[:class:`huaweicloudsdkagentarts.v1.OpsScoreCountItem`]
        """
        
        

        self._evaluator_id = None
        self._evaluator_name = None
        self._distrution = None
        self.discriminator = None

        if evaluator_id is not None:
            self.evaluator_id = evaluator_id
        if evaluator_name is not None:
            self.evaluator_name = evaluator_name
        if distrution is not None:
            self.distrution = distrution

    @property
    def evaluator_id(self):
        r"""Gets the evaluator_id of this OpsEvaluatorScoreDistribution.

        **参数解释：** 评估器的唯一标识符ID。 **取值范围：** UUID格式的字符串。 

        :return: The evaluator_id of this OpsEvaluatorScoreDistribution.
        :rtype: str
        """
        return self._evaluator_id

    @evaluator_id.setter
    def evaluator_id(self, evaluator_id):
        r"""Sets the evaluator_id of this OpsEvaluatorScoreDistribution.

        **参数解释：** 评估器的唯一标识符ID。 **取值范围：** UUID格式的字符串。 

        :param evaluator_id: The evaluator_id of this OpsEvaluatorScoreDistribution.
        :type evaluator_id: str
        """
        self._evaluator_id = evaluator_id

    @property
    def evaluator_name(self):
        r"""Gets the evaluator_name of this OpsEvaluatorScoreDistribution.

        **参数解释：** 评估器的显示名称。 **取值范围：** 1-100字符。 

        :return: The evaluator_name of this OpsEvaluatorScoreDistribution.
        :rtype: str
        """
        return self._evaluator_name

    @evaluator_name.setter
    def evaluator_name(self, evaluator_name):
        r"""Sets the evaluator_name of this OpsEvaluatorScoreDistribution.

        **参数解释：** 评估器的显示名称。 **取值范围：** 1-100字符。 

        :param evaluator_name: The evaluator_name of this OpsEvaluatorScoreDistribution.
        :type evaluator_name: str
        """
        self._evaluator_name = evaluator_name

    @property
    def distrution(self):
        r"""Gets the distrution of this OpsEvaluatorScoreDistribution.

        **参数解释：** 该评估器的得分分布列表，包含各分数及其对应的样本数量。 **取值范围：** 不涉及。 

        :return: The distrution of this OpsEvaluatorScoreDistribution.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsScoreCountItem`]
        """
        return self._distrution

    @distrution.setter
    def distrution(self, distrution):
        r"""Sets the distrution of this OpsEvaluatorScoreDistribution.

        **参数解释：** 该评估器的得分分布列表，包含各分数及其对应的样本数量。 **取值范围：** 不涉及。 

        :param distrution: The distrution of this OpsEvaluatorScoreDistribution.
        :type distrution: list[:class:`huaweicloudsdkagentarts.v1.OpsScoreCountItem`]
        """
        self._distrution = distrution

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
        if not isinstance(other, OpsEvaluatorScoreDistribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
