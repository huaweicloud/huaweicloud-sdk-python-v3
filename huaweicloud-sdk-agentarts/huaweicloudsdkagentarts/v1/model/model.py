# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Model:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_tokens_top': 'int',
        'max_tokens_bottom': 'int',
        'model_id': 'str',
        'model_name': 'str',
        'temperature_top': 'str',
        'temperature_bottom': 'str',
        'top_p_top': 'str',
        'top_p_bottom': 'str',
        'supported_scenes': 'list[str]'
    }

    attribute_map = {
        'max_tokens_top': 'max_tokens_top',
        'max_tokens_bottom': 'max_tokens_bottom',
        'model_id': 'model_id',
        'model_name': 'model_name',
        'temperature_top': 'temperature_top',
        'temperature_bottom': 'temperature_bottom',
        'top_p_top': 'top_p_top',
        'top_p_bottom': 'top_p_bottom',
        'supported_scenes': 'supported_scenes'
    }

    def __init__(self, max_tokens_top=None, max_tokens_bottom=None, model_id=None, model_name=None, temperature_top=None, temperature_bottom=None, top_p_top=None, top_p_bottom=None, supported_scenes=None):
        r"""Model

        The model defined in huaweicloud sdk

        :param max_tokens_top: **参数解释：** 模型生成文本的最大长度上限。 **取值范围：** 0 - 10000。
        :type max_tokens_top: int
        :param max_tokens_bottom: **参数解释：** 模型生成文本的最小长度下限。 **取值范围：** 0 - 10000。
        :type max_tokens_bottom: int
        :param model_id: **参数解释：** 模型的唯一标识符。 **取值范围：** 不涉及。
        :type model_id: str
        :param model_name: **参数解释：** 模型的显示名称。 **取值范围：** 不涉及。
        :type model_name: str
        :param temperature_top: **参数解释：** 模型生成随机性（Temperature）的上限值。 **取值范围：** 不涉及。
        :type temperature_top: str
        :param temperature_bottom: **参数解释：** 模型生成随机性的下限值。 **约束限制：** 0到10000字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type temperature_bottom: str
        :param top_p_top: **参数解释：** TopP采样策略的上限值。 **取值范围：** 不涉及。
        :type top_p_top: str
        :param top_p_bottom: **参数解释：** TopP采样策略的下限值。 **取值范围：** 不涉及。
        :type top_p_bottom: str
        :param supported_scenes: **参数解释：** 模型支持的应用场景列表。 **取值范围：** 数组长度为0到100。可选枚举值包括： - evaluators：评估器场景，用于质量评估。 - datasets-synthesis：数据合成场景，用于生成评测集。
        :type supported_scenes: list[str]
        """
        
        

        self._max_tokens_top = None
        self._max_tokens_bottom = None
        self._model_id = None
        self._model_name = None
        self._temperature_top = None
        self._temperature_bottom = None
        self._top_p_top = None
        self._top_p_bottom = None
        self._supported_scenes = None
        self.discriminator = None

        if max_tokens_top is not None:
            self.max_tokens_top = max_tokens_top
        if max_tokens_bottom is not None:
            self.max_tokens_bottom = max_tokens_bottom
        if model_id is not None:
            self.model_id = model_id
        if model_name is not None:
            self.model_name = model_name
        if temperature_top is not None:
            self.temperature_top = temperature_top
        if temperature_bottom is not None:
            self.temperature_bottom = temperature_bottom
        if top_p_top is not None:
            self.top_p_top = top_p_top
        if top_p_bottom is not None:
            self.top_p_bottom = top_p_bottom
        if supported_scenes is not None:
            self.supported_scenes = supported_scenes

    @property
    def max_tokens_top(self):
        r"""Gets the max_tokens_top of this Model.

        **参数解释：** 模型生成文本的最大长度上限。 **取值范围：** 0 - 10000。

        :return: The max_tokens_top of this Model.
        :rtype: int
        """
        return self._max_tokens_top

    @max_tokens_top.setter
    def max_tokens_top(self, max_tokens_top):
        r"""Sets the max_tokens_top of this Model.

        **参数解释：** 模型生成文本的最大长度上限。 **取值范围：** 0 - 10000。

        :param max_tokens_top: The max_tokens_top of this Model.
        :type max_tokens_top: int
        """
        self._max_tokens_top = max_tokens_top

    @property
    def max_tokens_bottom(self):
        r"""Gets the max_tokens_bottom of this Model.

        **参数解释：** 模型生成文本的最小长度下限。 **取值范围：** 0 - 10000。

        :return: The max_tokens_bottom of this Model.
        :rtype: int
        """
        return self._max_tokens_bottom

    @max_tokens_bottom.setter
    def max_tokens_bottom(self, max_tokens_bottom):
        r"""Sets the max_tokens_bottom of this Model.

        **参数解释：** 模型生成文本的最小长度下限。 **取值范围：** 0 - 10000。

        :param max_tokens_bottom: The max_tokens_bottom of this Model.
        :type max_tokens_bottom: int
        """
        self._max_tokens_bottom = max_tokens_bottom

    @property
    def model_id(self):
        r"""Gets the model_id of this Model.

        **参数解释：** 模型的唯一标识符。 **取值范围：** 不涉及。

        :return: The model_id of this Model.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this Model.

        **参数解释：** 模型的唯一标识符。 **取值范围：** 不涉及。

        :param model_id: The model_id of this Model.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def model_name(self):
        r"""Gets the model_name of this Model.

        **参数解释：** 模型的显示名称。 **取值范围：** 不涉及。

        :return: The model_name of this Model.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this Model.

        **参数解释：** 模型的显示名称。 **取值范围：** 不涉及。

        :param model_name: The model_name of this Model.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def temperature_top(self):
        r"""Gets the temperature_top of this Model.

        **参数解释：** 模型生成随机性（Temperature）的上限值。 **取值范围：** 不涉及。

        :return: The temperature_top of this Model.
        :rtype: str
        """
        return self._temperature_top

    @temperature_top.setter
    def temperature_top(self, temperature_top):
        r"""Sets the temperature_top of this Model.

        **参数解释：** 模型生成随机性（Temperature）的上限值。 **取值范围：** 不涉及。

        :param temperature_top: The temperature_top of this Model.
        :type temperature_top: str
        """
        self._temperature_top = temperature_top

    @property
    def temperature_bottom(self):
        r"""Gets the temperature_bottom of this Model.

        **参数解释：** 模型生成随机性的下限值。 **约束限制：** 0到10000字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The temperature_bottom of this Model.
        :rtype: str
        """
        return self._temperature_bottom

    @temperature_bottom.setter
    def temperature_bottom(self, temperature_bottom):
        r"""Sets the temperature_bottom of this Model.

        **参数解释：** 模型生成随机性的下限值。 **约束限制：** 0到10000字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param temperature_bottom: The temperature_bottom of this Model.
        :type temperature_bottom: str
        """
        self._temperature_bottom = temperature_bottom

    @property
    def top_p_top(self):
        r"""Gets the top_p_top of this Model.

        **参数解释：** TopP采样策略的上限值。 **取值范围：** 不涉及。

        :return: The top_p_top of this Model.
        :rtype: str
        """
        return self._top_p_top

    @top_p_top.setter
    def top_p_top(self, top_p_top):
        r"""Sets the top_p_top of this Model.

        **参数解释：** TopP采样策略的上限值。 **取值范围：** 不涉及。

        :param top_p_top: The top_p_top of this Model.
        :type top_p_top: str
        """
        self._top_p_top = top_p_top

    @property
    def top_p_bottom(self):
        r"""Gets the top_p_bottom of this Model.

        **参数解释：** TopP采样策略的下限值。 **取值范围：** 不涉及。

        :return: The top_p_bottom of this Model.
        :rtype: str
        """
        return self._top_p_bottom

    @top_p_bottom.setter
    def top_p_bottom(self, top_p_bottom):
        r"""Sets the top_p_bottom of this Model.

        **参数解释：** TopP采样策略的下限值。 **取值范围：** 不涉及。

        :param top_p_bottom: The top_p_bottom of this Model.
        :type top_p_bottom: str
        """
        self._top_p_bottom = top_p_bottom

    @property
    def supported_scenes(self):
        r"""Gets the supported_scenes of this Model.

        **参数解释：** 模型支持的应用场景列表。 **取值范围：** 数组长度为0到100。可选枚举值包括： - evaluators：评估器场景，用于质量评估。 - datasets-synthesis：数据合成场景，用于生成评测集。

        :return: The supported_scenes of this Model.
        :rtype: list[str]
        """
        return self._supported_scenes

    @supported_scenes.setter
    def supported_scenes(self, supported_scenes):
        r"""Sets the supported_scenes of this Model.

        **参数解释：** 模型支持的应用场景列表。 **取值范围：** 数组长度为0到100。可选枚举值包括： - evaluators：评估器场景，用于质量评估。 - datasets-synthesis：数据合成场景，用于生成评测集。

        :param supported_scenes: The supported_scenes of this Model.
        :type supported_scenes: list[str]
        """
        self._supported_scenes = supported_scenes

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
        if not isinstance(other, Model):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
