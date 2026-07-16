# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetScaleEvaluationsDevServerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluations': 'list[ServerScaleEvaluation]'
    }

    attribute_map = {
        'evaluations': 'evaluations'
    }

    def __init__(self, evaluations=None):
        r"""GetScaleEvaluationsDevServerResponse

        The model defined in huaweicloud sdk

        :param evaluations: **参数解释**：规格容量保有情况 **约束限制**：不涉及 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type evaluations: list[:class:`huaweicloudsdkmodelarts.v1.ServerScaleEvaluation`]
        """
        
        super().__init__()

        self._evaluations = None
        self.discriminator = None

        if evaluations is not None:
            self.evaluations = evaluations

    @property
    def evaluations(self):
        r"""Gets the evaluations of this GetScaleEvaluationsDevServerResponse.

        **参数解释**：规格容量保有情况 **约束限制**：不涉及 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The evaluations of this GetScaleEvaluationsDevServerResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ServerScaleEvaluation`]
        """
        return self._evaluations

    @evaluations.setter
    def evaluations(self, evaluations):
        r"""Sets the evaluations of this GetScaleEvaluationsDevServerResponse.

        **参数解释**：规格容量保有情况 **约束限制**：不涉及 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param evaluations: The evaluations of this GetScaleEvaluationsDevServerResponse.
        :type evaluations: list[:class:`huaweicloudsdkmodelarts.v1.ServerScaleEvaluation`]
        """
        self._evaluations = evaluations

    def to_dict(self):
        import warnings
        warnings.warn("GetScaleEvaluationsDevServerResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, GetScaleEvaluationsDevServerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
