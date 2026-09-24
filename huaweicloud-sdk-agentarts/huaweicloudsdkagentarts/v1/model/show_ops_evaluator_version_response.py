# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluatorVersionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluator': 'OpsListEvaluatorsInfo'
    }

    attribute_map = {
        'evaluator': 'evaluator'
    }

    def __init__(self, evaluator=None):
        r"""ShowOpsEvaluatorVersionResponse

        The model defined in huaweicloud sdk

        :param evaluator: 
        :type evaluator: :class:`huaweicloudsdkagentarts.v1.OpsListEvaluatorsInfo`
        """
        
        super().__init__()

        self._evaluator = None
        self.discriminator = None

        if evaluator is not None:
            self.evaluator = evaluator

    @property
    def evaluator(self):
        r"""Gets the evaluator of this ShowOpsEvaluatorVersionResponse.

        :return: The evaluator of this ShowOpsEvaluatorVersionResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsListEvaluatorsInfo`
        """
        return self._evaluator

    @evaluator.setter
    def evaluator(self, evaluator):
        r"""Sets the evaluator of this ShowOpsEvaluatorVersionResponse.

        :param evaluator: The evaluator of this ShowOpsEvaluatorVersionResponse.
        :type evaluator: :class:`huaweicloudsdkagentarts.v1.OpsListEvaluatorsInfo`
        """
        self._evaluator = evaluator

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpsEvaluatorVersionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowOpsEvaluatorVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
