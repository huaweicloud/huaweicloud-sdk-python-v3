# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsFineGrainedEvaluationObjectConfigInputsMapping:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input': 'str',
        'workflow_input': 'OpsFineGrainedEvaluationObjectConfigInputsMappingWorkflowInput'
    }

    attribute_map = {
        'input': 'input',
        'workflow_input': 'workflow_input'
    }

    def __init__(self, input=None, workflow_input=None):
        r"""OpsFineGrainedEvaluationObjectConfigInputsMapping

        The model defined in huaweicloud sdk

        :param input: **参数解释：** 智能体执行时的输入参数来源字段。 **约束限制：** 字符长度1到100。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type input: str
        :param workflow_input: 
        :type workflow_input: :class:`huaweicloudsdkagentarts.v1.OpsFineGrainedEvaluationObjectConfigInputsMappingWorkflowInput`
        """
        
        

        self._input = None
        self._workflow_input = None
        self.discriminator = None

        if input is not None:
            self.input = input
        if workflow_input is not None:
            self.workflow_input = workflow_input

    @property
    def input(self):
        r"""Gets the input of this OpsFineGrainedEvaluationObjectConfigInputsMapping.

        **参数解释：** 智能体执行时的输入参数来源字段。 **约束限制：** 字符长度1到100。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The input of this OpsFineGrainedEvaluationObjectConfigInputsMapping.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this OpsFineGrainedEvaluationObjectConfigInputsMapping.

        **参数解释：** 智能体执行时的输入参数来源字段。 **约束限制：** 字符长度1到100。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param input: The input of this OpsFineGrainedEvaluationObjectConfigInputsMapping.
        :type input: str
        """
        self._input = input

    @property
    def workflow_input(self):
        r"""Gets the workflow_input of this OpsFineGrainedEvaluationObjectConfigInputsMapping.

        :return: The workflow_input of this OpsFineGrainedEvaluationObjectConfigInputsMapping.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsFineGrainedEvaluationObjectConfigInputsMappingWorkflowInput`
        """
        return self._workflow_input

    @workflow_input.setter
    def workflow_input(self, workflow_input):
        r"""Sets the workflow_input of this OpsFineGrainedEvaluationObjectConfigInputsMapping.

        :param workflow_input: The workflow_input of this OpsFineGrainedEvaluationObjectConfigInputsMapping.
        :type workflow_input: :class:`huaweicloudsdkagentarts.v1.OpsFineGrainedEvaluationObjectConfigInputsMappingWorkflowInput`
        """
        self._workflow_input = workflow_input

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
        if not isinstance(other, OpsFineGrainedEvaluationObjectConfigInputsMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
