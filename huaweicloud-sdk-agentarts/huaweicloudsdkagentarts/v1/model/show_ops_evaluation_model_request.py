# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluationModelRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'model_id': 'str'
    }

    attribute_map = {
        'model_id': 'model_id'
    }

    def __init__(self, model_id=None):
        r"""ShowOpsEvaluationModelRequest

        The model defined in huaweicloud sdk

        :param model_id: **参数解释：** 大模型的唯一标识符（ID）。该参数用于在路径中指定当前操作所针对的具体模型资源。获取方法请参考9.1-获取模型信息 - ListOpsEvaluationModels。 **约束限制：** 长度为 1到100个字符。 **取值范围：** 存在的模型ID。 **默认取值：** 不涉及。
        :type model_id: str
        """
        
        

        self._model_id = None
        self.discriminator = None

        self.model_id = model_id

    @property
    def model_id(self):
        r"""Gets the model_id of this ShowOpsEvaluationModelRequest.

        **参数解释：** 大模型的唯一标识符（ID）。该参数用于在路径中指定当前操作所针对的具体模型资源。获取方法请参考9.1-获取模型信息 - ListOpsEvaluationModels。 **约束限制：** 长度为 1到100个字符。 **取值范围：** 存在的模型ID。 **默认取值：** 不涉及。

        :return: The model_id of this ShowOpsEvaluationModelRequest.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this ShowOpsEvaluationModelRequest.

        **参数解释：** 大模型的唯一标识符（ID）。该参数用于在路径中指定当前操作所针对的具体模型资源。获取方法请参考9.1-获取模型信息 - ListOpsEvaluationModels。 **约束限制：** 长度为 1到100个字符。 **取值范围：** 存在的模型ID。 **默认取值：** 不涉及。

        :param model_id: The model_id of this ShowOpsEvaluationModelRequest.
        :type model_id: str
        """
        self._model_id = model_id

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
        if not isinstance(other, ShowOpsEvaluationModelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
