# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsTuningRewardSetting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reward_type': 'str',
        'model_name': 'str',
        'apikey_credential_provider': 'str',
        'rubric': 'str',
        'rules': 'list[OpsTuningRewardRule]',
        'code_interpreter_id': 'str',
        'code': 'str'
    }

    attribute_map = {
        'reward_type': 'reward_type',
        'model_name': 'model_name',
        'apikey_credential_provider': 'apikey_credential_provider',
        'rubric': 'rubric',
        'rules': 'rules',
        'code_interpreter_id': 'code_interpreter_id',
        'code': 'code'
    }

    def __init__(self, reward_type=None, model_name=None, apikey_credential_provider=None, rubric=None, rules=None, code_interpreter_id=None, code=None):
        r"""OpsTuningRewardSetting

        The model defined in huaweicloud sdk

        :param reward_type: **参数解释：** 奖励类型，决定采用何种方式评估模型输出质量。  **约束限制：** 不涉及  **取值范围：** rule：规则奖励，基于预定义规则进行评分；generative：生成式奖励，使用判别模型进行评分；code：基于代码进行评分。  **默认取值：** 无
        :type reward_type: str
        :param model_name: **参数解释：** 模型名称，用于生成式奖励打分的裁判模型。  **约束限制：** generative类型必填。  **取值范围：** 支持的判别模型名称字符串。  **默认取值：** 无
        :type model_name: str
        :param apikey_credential_provider: **参数解释：** API密钥凭证提供者，用于访问判别模型的认证信息。  **约束限制：** generative类型必填。  **取值范围：** 平台中配置的凭证名称。  **默认取值：** 无
        :type apikey_credential_provider: str
        :param rubric: **参数解释：** 评分标准，指导判别模型进行评分的提示词内容。  **约束限制：** generative类型必填。  **取值范围：** 长度0-4096个字符的提示词。  **默认取值：** 无
        :type rubric: str
        :param rules: **参数解释：** 规则列表，定义具体的规则奖励函数。  **约束限制：** rule类型必填。  **取值范围：** 数组长度1-10。  **默认取值：** 无
        :type rules: list[:class:`huaweicloudsdkagentarts.v1.OpsTuningRewardRule`]
        :param code_interpreter_id: **参数解释：** 代码解释器ID，可通过[查询代码解释器列表](https://support.huaweicloud.com/api-agentarts/ListCoreCodeInterpreters.html)接口获取。  **约束限制：** code类型必填。  **取值范围：** 符合UUID正则^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$的36位字符串。  **默认取值：** 不涉及。
        :type code_interpreter_id: str
        :param code: **参数解释：** 计算奖励的代码片段。  **约束限制：** code类型必填。  **取值范围：** 最大长度4000。  **默认取值：** 不涉及。
        :type code: str
        """
        
        

        self._reward_type = None
        self._model_name = None
        self._apikey_credential_provider = None
        self._rubric = None
        self._rules = None
        self._code_interpreter_id = None
        self._code = None
        self.discriminator = None

        self.reward_type = reward_type
        if model_name is not None:
            self.model_name = model_name
        if apikey_credential_provider is not None:
            self.apikey_credential_provider = apikey_credential_provider
        if rubric is not None:
            self.rubric = rubric
        if rules is not None:
            self.rules = rules
        if code_interpreter_id is not None:
            self.code_interpreter_id = code_interpreter_id
        if code is not None:
            self.code = code

    @property
    def reward_type(self):
        r"""Gets the reward_type of this OpsTuningRewardSetting.

        **参数解释：** 奖励类型，决定采用何种方式评估模型输出质量。  **约束限制：** 不涉及  **取值范围：** rule：规则奖励，基于预定义规则进行评分；generative：生成式奖励，使用判别模型进行评分；code：基于代码进行评分。  **默认取值：** 无

        :return: The reward_type of this OpsTuningRewardSetting.
        :rtype: str
        """
        return self._reward_type

    @reward_type.setter
    def reward_type(self, reward_type):
        r"""Sets the reward_type of this OpsTuningRewardSetting.

        **参数解释：** 奖励类型，决定采用何种方式评估模型输出质量。  **约束限制：** 不涉及  **取值范围：** rule：规则奖励，基于预定义规则进行评分；generative：生成式奖励，使用判别模型进行评分；code：基于代码进行评分。  **默认取值：** 无

        :param reward_type: The reward_type of this OpsTuningRewardSetting.
        :type reward_type: str
        """
        self._reward_type = reward_type

    @property
    def model_name(self):
        r"""Gets the model_name of this OpsTuningRewardSetting.

        **参数解释：** 模型名称，用于生成式奖励打分的裁判模型。  **约束限制：** generative类型必填。  **取值范围：** 支持的判别模型名称字符串。  **默认取值：** 无

        :return: The model_name of this OpsTuningRewardSetting.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this OpsTuningRewardSetting.

        **参数解释：** 模型名称，用于生成式奖励打分的裁判模型。  **约束限制：** generative类型必填。  **取值范围：** 支持的判别模型名称字符串。  **默认取值：** 无

        :param model_name: The model_name of this OpsTuningRewardSetting.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def apikey_credential_provider(self):
        r"""Gets the apikey_credential_provider of this OpsTuningRewardSetting.

        **参数解释：** API密钥凭证提供者，用于访问判别模型的认证信息。  **约束限制：** generative类型必填。  **取值范围：** 平台中配置的凭证名称。  **默认取值：** 无

        :return: The apikey_credential_provider of this OpsTuningRewardSetting.
        :rtype: str
        """
        return self._apikey_credential_provider

    @apikey_credential_provider.setter
    def apikey_credential_provider(self, apikey_credential_provider):
        r"""Sets the apikey_credential_provider of this OpsTuningRewardSetting.

        **参数解释：** API密钥凭证提供者，用于访问判别模型的认证信息。  **约束限制：** generative类型必填。  **取值范围：** 平台中配置的凭证名称。  **默认取值：** 无

        :param apikey_credential_provider: The apikey_credential_provider of this OpsTuningRewardSetting.
        :type apikey_credential_provider: str
        """
        self._apikey_credential_provider = apikey_credential_provider

    @property
    def rubric(self):
        r"""Gets the rubric of this OpsTuningRewardSetting.

        **参数解释：** 评分标准，指导判别模型进行评分的提示词内容。  **约束限制：** generative类型必填。  **取值范围：** 长度0-4096个字符的提示词。  **默认取值：** 无

        :return: The rubric of this OpsTuningRewardSetting.
        :rtype: str
        """
        return self._rubric

    @rubric.setter
    def rubric(self, rubric):
        r"""Sets the rubric of this OpsTuningRewardSetting.

        **参数解释：** 评分标准，指导判别模型进行评分的提示词内容。  **约束限制：** generative类型必填。  **取值范围：** 长度0-4096个字符的提示词。  **默认取值：** 无

        :param rubric: The rubric of this OpsTuningRewardSetting.
        :type rubric: str
        """
        self._rubric = rubric

    @property
    def rules(self):
        r"""Gets the rules of this OpsTuningRewardSetting.

        **参数解释：** 规则列表，定义具体的规则奖励函数。  **约束限制：** rule类型必填。  **取值范围：** 数组长度1-10。  **默认取值：** 无

        :return: The rules of this OpsTuningRewardSetting.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTuningRewardRule`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this OpsTuningRewardSetting.

        **参数解释：** 规则列表，定义具体的规则奖励函数。  **约束限制：** rule类型必填。  **取值范围：** 数组长度1-10。  **默认取值：** 无

        :param rules: The rules of this OpsTuningRewardSetting.
        :type rules: list[:class:`huaweicloudsdkagentarts.v1.OpsTuningRewardRule`]
        """
        self._rules = rules

    @property
    def code_interpreter_id(self):
        r"""Gets the code_interpreter_id of this OpsTuningRewardSetting.

        **参数解释：** 代码解释器ID，可通过[查询代码解释器列表](https://support.huaweicloud.com/api-agentarts/ListCoreCodeInterpreters.html)接口获取。  **约束限制：** code类型必填。  **取值范围：** 符合UUID正则^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$的36位字符串。  **默认取值：** 不涉及。

        :return: The code_interpreter_id of this OpsTuningRewardSetting.
        :rtype: str
        """
        return self._code_interpreter_id

    @code_interpreter_id.setter
    def code_interpreter_id(self, code_interpreter_id):
        r"""Sets the code_interpreter_id of this OpsTuningRewardSetting.

        **参数解释：** 代码解释器ID，可通过[查询代码解释器列表](https://support.huaweicloud.com/api-agentarts/ListCoreCodeInterpreters.html)接口获取。  **约束限制：** code类型必填。  **取值范围：** 符合UUID正则^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$的36位字符串。  **默认取值：** 不涉及。

        :param code_interpreter_id: The code_interpreter_id of this OpsTuningRewardSetting.
        :type code_interpreter_id: str
        """
        self._code_interpreter_id = code_interpreter_id

    @property
    def code(self):
        r"""Gets the code of this OpsTuningRewardSetting.

        **参数解释：** 计算奖励的代码片段。  **约束限制：** code类型必填。  **取值范围：** 最大长度4000。  **默认取值：** 不涉及。

        :return: The code of this OpsTuningRewardSetting.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this OpsTuningRewardSetting.

        **参数解释：** 计算奖励的代码片段。  **约束限制：** code类型必填。  **取值范围：** 最大长度4000。  **默认取值：** 不涉及。

        :param code: The code of this OpsTuningRewardSetting.
        :type code: str
        """
        self._code = code

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
        if not isinstance(other, OpsTuningRewardSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
