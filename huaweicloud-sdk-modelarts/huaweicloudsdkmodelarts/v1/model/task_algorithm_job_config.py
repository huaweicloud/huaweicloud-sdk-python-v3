# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskAlgorithmJobConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parameters': 'list[Parameter]',
        'inputs': 'list[Input]',
        'outputs': 'list[Output]',
        'engine': 'TaskAlgorithmJobConfigEngine'
    }

    attribute_map = {
        'parameters': 'parameters',
        'inputs': 'inputs',
        'outputs': 'outputs',
        'engine': 'engine'
    }

    def __init__(self, parameters=None, inputs=None, outputs=None, engine=None):
        r"""TaskAlgorithmJobConfig

        The model defined in huaweicloud sdk

        :param parameters: **参数解释**：算法的运行参数。 **约束限制**：不涉及。
        :type parameters: list[:class:`huaweicloudsdkmodelarts.v1.Parameter`]
        :param inputs: **参数解释**：算法的数据输入。 **约束限制**：不涉及。
        :type inputs: list[:class:`huaweicloudsdkmodelarts.v1.Input`]
        :param outputs: **参数解释**：算法的数据输出。 **约束限制**：不涉及。
        :type outputs: list[:class:`huaweicloudsdkmodelarts.v1.Output`]
        :param engine: 
        :type engine: :class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmJobConfigEngine`
        """
        
        

        self._parameters = None
        self._inputs = None
        self._outputs = None
        self._engine = None
        self.discriminator = None

        if parameters is not None:
            self.parameters = parameters
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs
        if engine is not None:
            self.engine = engine

    @property
    def parameters(self):
        r"""Gets the parameters of this TaskAlgorithmJobConfig.

        **参数解释**：算法的运行参数。 **约束限制**：不涉及。

        :return: The parameters of this TaskAlgorithmJobConfig.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Parameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this TaskAlgorithmJobConfig.

        **参数解释**：算法的运行参数。 **约束限制**：不涉及。

        :param parameters: The parameters of this TaskAlgorithmJobConfig.
        :type parameters: list[:class:`huaweicloudsdkmodelarts.v1.Parameter`]
        """
        self._parameters = parameters

    @property
    def inputs(self):
        r"""Gets the inputs of this TaskAlgorithmJobConfig.

        **参数解释**：算法的数据输入。 **约束限制**：不涉及。

        :return: The inputs of this TaskAlgorithmJobConfig.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Input`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this TaskAlgorithmJobConfig.

        **参数解释**：算法的数据输入。 **约束限制**：不涉及。

        :param inputs: The inputs of this TaskAlgorithmJobConfig.
        :type inputs: list[:class:`huaweicloudsdkmodelarts.v1.Input`]
        """
        self._inputs = inputs

    @property
    def outputs(self):
        r"""Gets the outputs of this TaskAlgorithmJobConfig.

        **参数解释**：算法的数据输出。 **约束限制**：不涉及。

        :return: The outputs of this TaskAlgorithmJobConfig.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Output`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        r"""Sets the outputs of this TaskAlgorithmJobConfig.

        **参数解释**：算法的数据输出。 **约束限制**：不涉及。

        :param outputs: The outputs of this TaskAlgorithmJobConfig.
        :type outputs: list[:class:`huaweicloudsdkmodelarts.v1.Output`]
        """
        self._outputs = outputs

    @property
    def engine(self):
        r"""Gets the engine of this TaskAlgorithmJobConfig.

        :return: The engine of this TaskAlgorithmJobConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmJobConfigEngine`
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this TaskAlgorithmJobConfig.

        :param engine: The engine of this TaskAlgorithmJobConfig.
        :type engine: :class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmJobConfigEngine`
        """
        self._engine = engine

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
        if not isinstance(other, TaskAlgorithmJobConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
