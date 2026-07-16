# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatingStep:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'step': 'int',
        'type': 'str'
    }

    attribute_map = {
        'step': 'step',
        'type': 'type'
    }

    def __init__(self, step=None, type=None):
        r"""CreatingStep

        The model defined in huaweicloud sdk

        :param step: **参数解释**：超节点的步长。仅支持资源规格详情中包含的步长。 **取值范围**：不涉及。
        :type step: int
        :param type: **参数解释**：批量创建类型。 **取值范围**：可选值如下： - hyperinstance：超节点。
        :type type: str
        """
        
        

        self._step = None
        self._type = None
        self.discriminator = None

        if step is not None:
            self.step = step
        if type is not None:
            self.type = type

    @property
    def step(self):
        r"""Gets the step of this CreatingStep.

        **参数解释**：超节点的步长。仅支持资源规格详情中包含的步长。 **取值范围**：不涉及。

        :return: The step of this CreatingStep.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        r"""Sets the step of this CreatingStep.

        **参数解释**：超节点的步长。仅支持资源规格详情中包含的步长。 **取值范围**：不涉及。

        :param step: The step of this CreatingStep.
        :type step: int
        """
        self._step = step

    @property
    def type(self):
        r"""Gets the type of this CreatingStep.

        **参数解释**：批量创建类型。 **取值范围**：可选值如下： - hyperinstance：超节点。

        :return: The type of this CreatingStep.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreatingStep.

        **参数解释**：批量创建类型。 **取值范围**：可选值如下： - hyperinstance：超节点。

        :param type: The type of this CreatingStep.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, CreatingStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
