# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOpsEvaluatorResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluator_id': 'str'
    }

    attribute_map = {
        'evaluator_id': 'evaluator_id'
    }

    def __init__(self, evaluator_id=None):
        r"""CreateOpsEvaluatorResponse

        The model defined in huaweicloud sdk

        :param evaluator_id: **参数解释：** 成功创建后生成的评估器唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 
        :type evaluator_id: str
        """
        
        super().__init__()

        self._evaluator_id = None
        self.discriminator = None

        if evaluator_id is not None:
            self.evaluator_id = evaluator_id

    @property
    def evaluator_id(self):
        r"""Gets the evaluator_id of this CreateOpsEvaluatorResponse.

        **参数解释：** 成功创建后生成的评估器唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 

        :return: The evaluator_id of this CreateOpsEvaluatorResponse.
        :rtype: str
        """
        return self._evaluator_id

    @evaluator_id.setter
    def evaluator_id(self, evaluator_id):
        r"""Sets the evaluator_id of this CreateOpsEvaluatorResponse.

        **参数解释：** 成功创建后生成的评估器唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 

        :param evaluator_id: The evaluator_id of this CreateOpsEvaluatorResponse.
        :type evaluator_id: str
        """
        self._evaluator_id = evaluator_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateOpsEvaluatorResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateOpsEvaluatorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
