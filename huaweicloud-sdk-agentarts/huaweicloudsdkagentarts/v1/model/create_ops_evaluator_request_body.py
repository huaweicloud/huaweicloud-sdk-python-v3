# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOpsEvaluatorRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluator_type': 'int',
        'turn_type': 'str',
        'current_version': 'EvaluationOpsCurrentVersion',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'evaluator_type': 'evaluator_type',
        'turn_type': 'turn_type',
        'current_version': 'current_version',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, evaluator_type=None, turn_type=None, current_version=None, name=None, description=None):
        r"""CreateOpsEvaluatorRequestBody

        The model defined in huaweicloud sdk

        :param evaluator_type: **参数解释：** 评估器的核心执行模式。 **约束限制：** 整型数值，取值范围为int32。 **取值范围：** - 1: 模型评估器（模型评估器，基于大语言模型进行智能评判） - 2: 代码评估器（代码评估器，基于预设脚本逻辑进行规则判定） - 3: 自适应评估器 **默认取值：** 不涉及。 
        :type evaluator_type: int
        :param turn_type: **参数解释：** 评估器的轮次类型。 **约束限制：** 长度为0到100个字符。 **取值范围：** - single: 单轮评估器 - multi: 多轮评估器 **默认取值：** 不涉及。 
        :type turn_type: str
        :param current_version: 
        :type current_version: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsCurrentVersion`
        :param name: **参数解释：** 评估器的业务名称。 **约束限制：** 长度为1到10000个字符。 **取值范围：** 中英文、数字、下划线（_）、中划线（-）组成的字符串。 **默认取值：** 不涉及。 
        :type name: str
        :param description: **参数解释：** 对该评估器的功能逻辑和判定准则的详细文字补充。 **约束限制：** 长度为0到10000个字符。 **取值范围：** 任意字符串。 **默认取值：** 不涉及。 
        :type description: str
        """
        
        

        self._evaluator_type = None
        self._turn_type = None
        self._current_version = None
        self._name = None
        self._description = None
        self.discriminator = None

        self.evaluator_type = evaluator_type
        if turn_type is not None:
            self.turn_type = turn_type
        self.current_version = current_version
        self.name = name
        self.description = description

    @property
    def evaluator_type(self):
        r"""Gets the evaluator_type of this CreateOpsEvaluatorRequestBody.

        **参数解释：** 评估器的核心执行模式。 **约束限制：** 整型数值，取值范围为int32。 **取值范围：** - 1: 模型评估器（模型评估器，基于大语言模型进行智能评判） - 2: 代码评估器（代码评估器，基于预设脚本逻辑进行规则判定） - 3: 自适应评估器 **默认取值：** 不涉及。 

        :return: The evaluator_type of this CreateOpsEvaluatorRequestBody.
        :rtype: int
        """
        return self._evaluator_type

    @evaluator_type.setter
    def evaluator_type(self, evaluator_type):
        r"""Sets the evaluator_type of this CreateOpsEvaluatorRequestBody.

        **参数解释：** 评估器的核心执行模式。 **约束限制：** 整型数值，取值范围为int32。 **取值范围：** - 1: 模型评估器（模型评估器，基于大语言模型进行智能评判） - 2: 代码评估器（代码评估器，基于预设脚本逻辑进行规则判定） - 3: 自适应评估器 **默认取值：** 不涉及。 

        :param evaluator_type: The evaluator_type of this CreateOpsEvaluatorRequestBody.
        :type evaluator_type: int
        """
        self._evaluator_type = evaluator_type

    @property
    def turn_type(self):
        r"""Gets the turn_type of this CreateOpsEvaluatorRequestBody.

        **参数解释：** 评估器的轮次类型。 **约束限制：** 长度为0到100个字符。 **取值范围：** - single: 单轮评估器 - multi: 多轮评估器 **默认取值：** 不涉及。 

        :return: The turn_type of this CreateOpsEvaluatorRequestBody.
        :rtype: str
        """
        return self._turn_type

    @turn_type.setter
    def turn_type(self, turn_type):
        r"""Sets the turn_type of this CreateOpsEvaluatorRequestBody.

        **参数解释：** 评估器的轮次类型。 **约束限制：** 长度为0到100个字符。 **取值范围：** - single: 单轮评估器 - multi: 多轮评估器 **默认取值：** 不涉及。 

        :param turn_type: The turn_type of this CreateOpsEvaluatorRequestBody.
        :type turn_type: str
        """
        self._turn_type = turn_type

    @property
    def current_version(self):
        r"""Gets the current_version of this CreateOpsEvaluatorRequestBody.

        :return: The current_version of this CreateOpsEvaluatorRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsCurrentVersion`
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        r"""Sets the current_version of this CreateOpsEvaluatorRequestBody.

        :param current_version: The current_version of this CreateOpsEvaluatorRequestBody.
        :type current_version: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsCurrentVersion`
        """
        self._current_version = current_version

    @property
    def name(self):
        r"""Gets the name of this CreateOpsEvaluatorRequestBody.

        **参数解释：** 评估器的业务名称。 **约束限制：** 长度为1到10000个字符。 **取值范围：** 中英文、数字、下划线（_）、中划线（-）组成的字符串。 **默认取值：** 不涉及。 

        :return: The name of this CreateOpsEvaluatorRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateOpsEvaluatorRequestBody.

        **参数解释：** 评估器的业务名称。 **约束限制：** 长度为1到10000个字符。 **取值范围：** 中英文、数字、下划线（_）、中划线（-）组成的字符串。 **默认取值：** 不涉及。 

        :param name: The name of this CreateOpsEvaluatorRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateOpsEvaluatorRequestBody.

        **参数解释：** 对该评估器的功能逻辑和判定准则的详细文字补充。 **约束限制：** 长度为0到10000个字符。 **取值范围：** 任意字符串。 **默认取值：** 不涉及。 

        :return: The description of this CreateOpsEvaluatorRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateOpsEvaluatorRequestBody.

        **参数解释：** 对该评估器的功能逻辑和判定准则的详细文字补充。 **约束限制：** 长度为0到10000个字符。 **取值范围：** 任意字符串。 **默认取值：** 不涉及。 

        :param description: The description of this CreateOpsEvaluatorRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateOpsEvaluatorRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
