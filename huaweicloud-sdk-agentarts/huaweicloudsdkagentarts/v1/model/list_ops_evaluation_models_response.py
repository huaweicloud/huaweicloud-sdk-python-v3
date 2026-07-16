# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsEvaluationModelsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'models': 'list[ListOpsEvaluatorModelsResponseBodyModels]'
    }

    attribute_map = {
        'models': 'models'
    }

    def __init__(self, models=None):
        r"""ListOpsEvaluationModelsResponse

        The model defined in huaweicloud sdk

        :param models: **参数解释：** 模型信息的列表，包含多个模型的配置参数、阈值范围以及支持的业务场景。 **取值范围：** 符合模型定义的对象数组。 
        :type models: list[:class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorModelsResponseBodyModels`]
        """
        
        super().__init__()

        self._models = None
        self.discriminator = None

        if models is not None:
            self.models = models

    @property
    def models(self):
        r"""Gets the models of this ListOpsEvaluationModelsResponse.

        **参数解释：** 模型信息的列表，包含多个模型的配置参数、阈值范围以及支持的业务场景。 **取值范围：** 符合模型定义的对象数组。 

        :return: The models of this ListOpsEvaluationModelsResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorModelsResponseBodyModels`]
        """
        return self._models

    @models.setter
    def models(self, models):
        r"""Sets the models of this ListOpsEvaluationModelsResponse.

        **参数解释：** 模型信息的列表，包含多个模型的配置参数、阈值范围以及支持的业务场景。 **取值范围：** 符合模型定义的对象数组。 

        :param models: The models of this ListOpsEvaluationModelsResponse.
        :type models: list[:class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorModelsResponseBodyModels`]
        """
        self._models = models

    def to_dict(self):
        import warnings
        warnings.warn("ListOpsEvaluationModelsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListOpsEvaluationModelsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
