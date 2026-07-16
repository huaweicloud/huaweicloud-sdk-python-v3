# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOpsSynthesisTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'scenario_type': 'str',
        'scenario_description': 'str',
        'status': 'str',
        'model_config': 'EvaluationOpsModelConfig',
        'seed_data': 'EvaluationOpsSeedDataCreateConfig',
        'schemas': 'list[EvaluationOpsSynthesisSchema]',
        'sample_count': 'int'
    }

    attribute_map = {
        'name': 'name',
        'scenario_type': 'scenario_type',
        'scenario_description': 'scenario_description',
        'status': 'status',
        'model_config': 'model_config',
        'seed_data': 'seed_data',
        'schemas': 'schemas',
        'sample_count': 'sample_count'
    }

    def __init__(self, name=None, scenario_type=None, scenario_description=None, status=None, model_config=None, seed_data=None, schemas=None, sample_count=None):
        r"""CreateOpsSynthesisTaskRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：**   数据合成任务的显示名称，用于在任务列表中进行识别与检索。 **约束限制：**   长度为2-100个字符。 **取值范围：**   任意字符串。 **默认取值：**   不涉及。 
        :type name: str
        :param scenario_type: **参数解释：**   指定数据合成的具体逻辑场景。 **约束限制：**   必填，仅支持枚举值。字符长度1-100。 **取值范围：**   字符长度1-100，seed_data (基于种子数据生成)。 **默认取值：**   不涉及。 
        :type scenario_type: str
        :param scenario_description: **参数解释：**   对合成任务背景的详细描述，辅助模型更好地理解合成目标。 **约束限制：**   1-4000个字符。 **取值范围：**   字符长度1-4000，由用户定义的业务背景描述。 **默认取值：**   不涉及。 
        :type scenario_description: str
        :param status: **参数解释：**   任务创建后的初始执行状态。 **约束限制：**   字符长度1-100，枚举类型。 **取值范围：**   字符长度1-100，pending(仅保存草稿)，running(立即启动运行)。 **默认取值：**   pending。 
        :type status: str
        :param model_config: 
        :type model_config: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsModelConfig`
        :param seed_data: 
        :type seed_data: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsSeedDataCreateConfig`
        :param schemas: **参数解释：**   定义合成数据输出的字段结构与约束。 **约束限制：**   数组长度为 1-50。 **取值范围：**   参考EvaluationOpsSynthesisSchema定义。 **默认取值：**   不涉及。 
        :type schemas: list[:class:`huaweicloudsdkagentarts.v1.EvaluationOpsSynthesisSchema`]
        :param sample_count: **参数解释：**   期望通过本次合成任务产出的目标样本总数。 **约束限制：**   1-500之间的整数。 **取值范围：**   1-500。 **默认取值：**   不涉及。 
        :type sample_count: int
        """
        
        

        self._name = None
        self._scenario_type = None
        self._scenario_description = None
        self._status = None
        self._model_config = None
        self._seed_data = None
        self._schemas = None
        self._sample_count = None
        self.discriminator = None

        self.name = name
        self.scenario_type = scenario_type
        if scenario_description is not None:
            self.scenario_description = scenario_description
        if status is not None:
            self.status = status
        self.model_config = model_config
        if seed_data is not None:
            self.seed_data = seed_data
        self.schemas = schemas
        self.sample_count = sample_count

    @property
    def name(self):
        r"""Gets the name of this CreateOpsSynthesisTaskRequestBody.

        **参数解释：**   数据合成任务的显示名称，用于在任务列表中进行识别与检索。 **约束限制：**   长度为2-100个字符。 **取值范围：**   任意字符串。 **默认取值：**   不涉及。 

        :return: The name of this CreateOpsSynthesisTaskRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateOpsSynthesisTaskRequestBody.

        **参数解释：**   数据合成任务的显示名称，用于在任务列表中进行识别与检索。 **约束限制：**   长度为2-100个字符。 **取值范围：**   任意字符串。 **默认取值：**   不涉及。 

        :param name: The name of this CreateOpsSynthesisTaskRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def scenario_type(self):
        r"""Gets the scenario_type of this CreateOpsSynthesisTaskRequestBody.

        **参数解释：**   指定数据合成的具体逻辑场景。 **约束限制：**   必填，仅支持枚举值。字符长度1-100。 **取值范围：**   字符长度1-100，seed_data (基于种子数据生成)。 **默认取值：**   不涉及。 

        :return: The scenario_type of this CreateOpsSynthesisTaskRequestBody.
        :rtype: str
        """
        return self._scenario_type

    @scenario_type.setter
    def scenario_type(self, scenario_type):
        r"""Sets the scenario_type of this CreateOpsSynthesisTaskRequestBody.

        **参数解释：**   指定数据合成的具体逻辑场景。 **约束限制：**   必填，仅支持枚举值。字符长度1-100。 **取值范围：**   字符长度1-100，seed_data (基于种子数据生成)。 **默认取值：**   不涉及。 

        :param scenario_type: The scenario_type of this CreateOpsSynthesisTaskRequestBody.
        :type scenario_type: str
        """
        self._scenario_type = scenario_type

    @property
    def scenario_description(self):
        r"""Gets the scenario_description of this CreateOpsSynthesisTaskRequestBody.

        **参数解释：**   对合成任务背景的详细描述，辅助模型更好地理解合成目标。 **约束限制：**   1-4000个字符。 **取值范围：**   字符长度1-4000，由用户定义的业务背景描述。 **默认取值：**   不涉及。 

        :return: The scenario_description of this CreateOpsSynthesisTaskRequestBody.
        :rtype: str
        """
        return self._scenario_description

    @scenario_description.setter
    def scenario_description(self, scenario_description):
        r"""Sets the scenario_description of this CreateOpsSynthesisTaskRequestBody.

        **参数解释：**   对合成任务背景的详细描述，辅助模型更好地理解合成目标。 **约束限制：**   1-4000个字符。 **取值范围：**   字符长度1-4000，由用户定义的业务背景描述。 **默认取值：**   不涉及。 

        :param scenario_description: The scenario_description of this CreateOpsSynthesisTaskRequestBody.
        :type scenario_description: str
        """
        self._scenario_description = scenario_description

    @property
    def status(self):
        r"""Gets the status of this CreateOpsSynthesisTaskRequestBody.

        **参数解释：**   任务创建后的初始执行状态。 **约束限制：**   字符长度1-100，枚举类型。 **取值范围：**   字符长度1-100，pending(仅保存草稿)，running(立即启动运行)。 **默认取值：**   pending。 

        :return: The status of this CreateOpsSynthesisTaskRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateOpsSynthesisTaskRequestBody.

        **参数解释：**   任务创建后的初始执行状态。 **约束限制：**   字符长度1-100，枚举类型。 **取值范围：**   字符长度1-100，pending(仅保存草稿)，running(立即启动运行)。 **默认取值：**   pending。 

        :param status: The status of this CreateOpsSynthesisTaskRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def model_config(self):
        r"""Gets the model_config of this CreateOpsSynthesisTaskRequestBody.

        :return: The model_config of this CreateOpsSynthesisTaskRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsModelConfig`
        """
        return self._model_config

    @model_config.setter
    def model_config(self, model_config):
        r"""Sets the model_config of this CreateOpsSynthesisTaskRequestBody.

        :param model_config: The model_config of this CreateOpsSynthesisTaskRequestBody.
        :type model_config: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsModelConfig`
        """
        self._model_config = model_config

    @property
    def seed_data(self):
        r"""Gets the seed_data of this CreateOpsSynthesisTaskRequestBody.

        :return: The seed_data of this CreateOpsSynthesisTaskRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsSeedDataCreateConfig`
        """
        return self._seed_data

    @seed_data.setter
    def seed_data(self, seed_data):
        r"""Sets the seed_data of this CreateOpsSynthesisTaskRequestBody.

        :param seed_data: The seed_data of this CreateOpsSynthesisTaskRequestBody.
        :type seed_data: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsSeedDataCreateConfig`
        """
        self._seed_data = seed_data

    @property
    def schemas(self):
        r"""Gets the schemas of this CreateOpsSynthesisTaskRequestBody.

        **参数解释：**   定义合成数据输出的字段结构与约束。 **约束限制：**   数组长度为 1-50。 **取值范围：**   参考EvaluationOpsSynthesisSchema定义。 **默认取值：**   不涉及。 

        :return: The schemas of this CreateOpsSynthesisTaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.EvaluationOpsSynthesisSchema`]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        r"""Sets the schemas of this CreateOpsSynthesisTaskRequestBody.

        **参数解释：**   定义合成数据输出的字段结构与约束。 **约束限制：**   数组长度为 1-50。 **取值范围：**   参考EvaluationOpsSynthesisSchema定义。 **默认取值：**   不涉及。 

        :param schemas: The schemas of this CreateOpsSynthesisTaskRequestBody.
        :type schemas: list[:class:`huaweicloudsdkagentarts.v1.EvaluationOpsSynthesisSchema`]
        """
        self._schemas = schemas

    @property
    def sample_count(self):
        r"""Gets the sample_count of this CreateOpsSynthesisTaskRequestBody.

        **参数解释：**   期望通过本次合成任务产出的目标样本总数。 **约束限制：**   1-500之间的整数。 **取值范围：**   1-500。 **默认取值：**   不涉及。 

        :return: The sample_count of this CreateOpsSynthesisTaskRequestBody.
        :rtype: int
        """
        return self._sample_count

    @sample_count.setter
    def sample_count(self, sample_count):
        r"""Sets the sample_count of this CreateOpsSynthesisTaskRequestBody.

        **参数解释：**   期望通过本次合成任务产出的目标样本总数。 **约束限制：**   1-500之间的整数。 **取值范围：**   1-500。 **默认取值：**   不涉及。 

        :param sample_count: The sample_count of this CreateOpsSynthesisTaskRequestBody.
        :type sample_count: int
        """
        self._sample_count = sample_count

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
        if not isinstance(other, CreateOpsSynthesisTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
