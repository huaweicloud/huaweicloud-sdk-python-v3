# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsOfflineConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluator_config': 'list[OpsEvaluatorConfigInfo]'
    }

    attribute_map = {
        'evaluator_config': 'evaluator_config'
    }

    def __init__(self, evaluator_config=None):
        r"""OpsOfflineConfig

        The model defined in huaweicloud sdk

        :param evaluator_config: **参数解释：** 评估器的配置。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type evaluator_config: list[:class:`huaweicloudsdkagentarts.v1.OpsEvaluatorConfigInfo`]
        """
        
        

        self._evaluator_config = None
        self.discriminator = None

        if evaluator_config is not None:
            self.evaluator_config = evaluator_config

    @property
    def evaluator_config(self):
        r"""Gets the evaluator_config of this OpsOfflineConfig.

        **参数解释：** 评估器的配置。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The evaluator_config of this OpsOfflineConfig.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsEvaluatorConfigInfo`]
        """
        return self._evaluator_config

    @evaluator_config.setter
    def evaluator_config(self, evaluator_config):
        r"""Sets the evaluator_config of this OpsOfflineConfig.

        **参数解释：** 评估器的配置。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param evaluator_config: The evaluator_config of this OpsOfflineConfig.
        :type evaluator_config: list[:class:`huaweicloudsdkagentarts.v1.OpsEvaluatorConfigInfo`]
        """
        self._evaluator_config = evaluator_config

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
        if not isinstance(other, OpsOfflineConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
