# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InvokeOpsFineGrainedEvaluationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'object'
    }

    attribute_map = {
        'data': 'data'
    }

    def __init__(self, data=None):
        r"""InvokeOpsFineGrainedEvaluationResponse

        The model defined in huaweicloud sdk

        :param data: **参数解释：** 细粒度评估结果。data字段根据stream参数的不同，返回不同的结构： - stream&#x3D;true时，data为OpsFineGrainedEvaluationSSEEvent，为SSE流式事件中的单条评估结果数据（item_completed事件的data部分）。 - stream&#x3D;false时，data为OpsFineGrainedEvaluationResult，为完整的评估结果，包含所有条目的评估详情。 **约束限制：** data字段两种结构二选一，不会同时出现。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type data: object
        """
        
        super().__init__()

        self._data = None
        self.discriminator = None

        if data is not None:
            self.data = data

    @property
    def data(self):
        r"""Gets the data of this InvokeOpsFineGrainedEvaluationResponse.

        **参数解释：** 细粒度评估结果。data字段根据stream参数的不同，返回不同的结构： - stream=true时，data为OpsFineGrainedEvaluationSSEEvent，为SSE流式事件中的单条评估结果数据（item_completed事件的data部分）。 - stream=false时，data为OpsFineGrainedEvaluationResult，为完整的评估结果，包含所有条目的评估详情。 **约束限制：** data字段两种结构二选一，不会同时出现。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The data of this InvokeOpsFineGrainedEvaluationResponse.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this InvokeOpsFineGrainedEvaluationResponse.

        **参数解释：** 细粒度评估结果。data字段根据stream参数的不同，返回不同的结构： - stream=true时，data为OpsFineGrainedEvaluationSSEEvent，为SSE流式事件中的单条评估结果数据（item_completed事件的data部分）。 - stream=false时，data为OpsFineGrainedEvaluationResult，为完整的评估结果，包含所有条目的评估详情。 **约束限制：** data字段两种结构二选一，不会同时出现。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param data: The data of this InvokeOpsFineGrainedEvaluationResponse.
        :type data: object
        """
        self._data = data

    def to_dict(self):
        import warnings
        warnings.warn("InvokeOpsFineGrainedEvaluationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, InvokeOpsFineGrainedEvaluationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
