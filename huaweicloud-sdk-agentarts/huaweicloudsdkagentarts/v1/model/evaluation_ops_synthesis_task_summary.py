# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationOpsSynthesisTaskSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'scenario_type': 'str',
        'scenario_name': 'str',
        'scenario_description': 'str',
        'stats': 'object',
        'status': 'str',
        'error_message': 'str',
        'is_free': 'bool',
        'model_config': 'EvaluationOpsModelConfig',
        'seed_data': 'EvaluationOpsSeedDataConfig',
        'base_info': 'EvaluationOpsTaskBaseInfo'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'scenario_type': 'scenario_type',
        'scenario_name': 'scenario_name',
        'scenario_description': 'scenario_description',
        'stats': 'stats',
        'status': 'status',
        'error_message': 'error_message',
        'is_free': 'is_free',
        'model_config': 'model_config',
        'seed_data': 'seed_data',
        'base_info': 'base_info'
    }

    def __init__(self, id=None, name=None, scenario_type=None, scenario_name=None, scenario_description=None, stats=None, status=None, error_message=None, is_free=None, model_config=None, seed_data=None, base_info=None):
        r"""EvaluationOpsSynthesisTaskSummary

        The model defined in huaweicloud sdk

        :param id: **参数解释：**   合成任务的唯一标识符。 **约束限制：**   1-64 字符。 **取值范围：**   UUID或系统生成的ID。 **默认取值：**   不涉及。 
        :type id: str
        :param name: **参数解释：**   用户为合成任务定义的名称。 **约束限制：**   1-100字符。 **取值范围：**   任意字符串。 **默认取值：**   不涉及。 
        :type name: str
        :param scenario_type: **参数解释：**   合成任务的技术场景类型。 **约束限制：**   枚举值。 **取值范围：**   seed_data等。 **默认取值：**   不涉及。 
        :type scenario_type: str
        :param scenario_name: **参数解释：**   场景的友好展示名称。 **约束限制：**   1-4000字符。 **取值范围：**   如 \&quot;基于种子数据泛化\&quot;。 **默认取值：**   不涉及。 
        :type scenario_name: str
        :param scenario_description: **参数解释：**   合成任务背景的详细描述。 **约束限制：**   1-4000字符。 **取值范围：**   场景背景文本。 **默认取值：**   不涉及。 
        :type scenario_description: str
        :param stats: **参数解释：**   合成任务的运行状态统计列表。 **约束限制：**   数组类型。 **取值范围：**   不涉及。 **默认取值：**   不涉及。 
        :type stats: object
        :param status: **参数解释：**   合成任务当前的生命周期状态。 **约束限制：**   枚举类型。 **取值范围：**   pending, running, completed, failed, stopped。 **默认取值：**   pending。 
        :type status: str
        :param error_message: **参数解释：**   任务失败时的错误信息。 **约束限制：**   不涉及。 **取值范围：**   不涉及。 **默认取值：**   不涉及。 
        :type error_message: str
        :param is_free: **参数解释：**   是否使用免费额度创建的任务。 **约束限制：**   不涉及。 **取值范围：**   - true：免费任务 - false：付费任务 **默认取值：**   不涉及。 
        :type is_free: bool
        :param model_config: 
        :type model_config: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsModelConfig`
        :param seed_data: 
        :type seed_data: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsSeedDataConfig`
        :param base_info: 
        :type base_info: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsTaskBaseInfo`
        """
        
        

        self._id = None
        self._name = None
        self._scenario_type = None
        self._scenario_name = None
        self._scenario_description = None
        self._stats = None
        self._status = None
        self._error_message = None
        self._is_free = None
        self._model_config = None
        self._seed_data = None
        self._base_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if scenario_type is not None:
            self.scenario_type = scenario_type
        if scenario_name is not None:
            self.scenario_name = scenario_name
        if scenario_description is not None:
            self.scenario_description = scenario_description
        if stats is not None:
            self.stats = stats
        if status is not None:
            self.status = status
        if error_message is not None:
            self.error_message = error_message
        if is_free is not None:
            self.is_free = is_free
        if model_config is not None:
            self.model_config = model_config
        if seed_data is not None:
            self.seed_data = seed_data
        if base_info is not None:
            self.base_info = base_info

    @property
    def id(self):
        r"""Gets the id of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   合成任务的唯一标识符。 **约束限制：**   1-64 字符。 **取值范围：**   UUID或系统生成的ID。 **默认取值：**   不涉及。 

        :return: The id of this EvaluationOpsSynthesisTaskSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   合成任务的唯一标识符。 **约束限制：**   1-64 字符。 **取值范围：**   UUID或系统生成的ID。 **默认取值：**   不涉及。 

        :param id: The id of this EvaluationOpsSynthesisTaskSummary.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   用户为合成任务定义的名称。 **约束限制：**   1-100字符。 **取值范围：**   任意字符串。 **默认取值：**   不涉及。 

        :return: The name of this EvaluationOpsSynthesisTaskSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   用户为合成任务定义的名称。 **约束限制：**   1-100字符。 **取值范围：**   任意字符串。 **默认取值：**   不涉及。 

        :param name: The name of this EvaluationOpsSynthesisTaskSummary.
        :type name: str
        """
        self._name = name

    @property
    def scenario_type(self):
        r"""Gets the scenario_type of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   合成任务的技术场景类型。 **约束限制：**   枚举值。 **取值范围：**   seed_data等。 **默认取值：**   不涉及。 

        :return: The scenario_type of this EvaluationOpsSynthesisTaskSummary.
        :rtype: str
        """
        return self._scenario_type

    @scenario_type.setter
    def scenario_type(self, scenario_type):
        r"""Sets the scenario_type of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   合成任务的技术场景类型。 **约束限制：**   枚举值。 **取值范围：**   seed_data等。 **默认取值：**   不涉及。 

        :param scenario_type: The scenario_type of this EvaluationOpsSynthesisTaskSummary.
        :type scenario_type: str
        """
        self._scenario_type = scenario_type

    @property
    def scenario_name(self):
        r"""Gets the scenario_name of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   场景的友好展示名称。 **约束限制：**   1-4000字符。 **取值范围：**   如 \"基于种子数据泛化\"。 **默认取值：**   不涉及。 

        :return: The scenario_name of this EvaluationOpsSynthesisTaskSummary.
        :rtype: str
        """
        return self._scenario_name

    @scenario_name.setter
    def scenario_name(self, scenario_name):
        r"""Sets the scenario_name of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   场景的友好展示名称。 **约束限制：**   1-4000字符。 **取值范围：**   如 \"基于种子数据泛化\"。 **默认取值：**   不涉及。 

        :param scenario_name: The scenario_name of this EvaluationOpsSynthesisTaskSummary.
        :type scenario_name: str
        """
        self._scenario_name = scenario_name

    @property
    def scenario_description(self):
        r"""Gets the scenario_description of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   合成任务背景的详细描述。 **约束限制：**   1-4000字符。 **取值范围：**   场景背景文本。 **默认取值：**   不涉及。 

        :return: The scenario_description of this EvaluationOpsSynthesisTaskSummary.
        :rtype: str
        """
        return self._scenario_description

    @scenario_description.setter
    def scenario_description(self, scenario_description):
        r"""Sets the scenario_description of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   合成任务背景的详细描述。 **约束限制：**   1-4000字符。 **取值范围：**   场景背景文本。 **默认取值：**   不涉及。 

        :param scenario_description: The scenario_description of this EvaluationOpsSynthesisTaskSummary.
        :type scenario_description: str
        """
        self._scenario_description = scenario_description

    @property
    def stats(self):
        r"""Gets the stats of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   合成任务的运行状态统计列表。 **约束限制：**   数组类型。 **取值范围：**   不涉及。 **默认取值：**   不涉及。 

        :return: The stats of this EvaluationOpsSynthesisTaskSummary.
        :rtype: object
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        r"""Sets the stats of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   合成任务的运行状态统计列表。 **约束限制：**   数组类型。 **取值范围：**   不涉及。 **默认取值：**   不涉及。 

        :param stats: The stats of this EvaluationOpsSynthesisTaskSummary.
        :type stats: object
        """
        self._stats = stats

    @property
    def status(self):
        r"""Gets the status of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   合成任务当前的生命周期状态。 **约束限制：**   枚举类型。 **取值范围：**   pending, running, completed, failed, stopped。 **默认取值：**   pending。 

        :return: The status of this EvaluationOpsSynthesisTaskSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   合成任务当前的生命周期状态。 **约束限制：**   枚举类型。 **取值范围：**   pending, running, completed, failed, stopped。 **默认取值：**   pending。 

        :param status: The status of this EvaluationOpsSynthesisTaskSummary.
        :type status: str
        """
        self._status = status

    @property
    def error_message(self):
        r"""Gets the error_message of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   任务失败时的错误信息。 **约束限制：**   不涉及。 **取值范围：**   不涉及。 **默认取值：**   不涉及。 

        :return: The error_message of this EvaluationOpsSynthesisTaskSummary.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   任务失败时的错误信息。 **约束限制：**   不涉及。 **取值范围：**   不涉及。 **默认取值：**   不涉及。 

        :param error_message: The error_message of this EvaluationOpsSynthesisTaskSummary.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def is_free(self):
        r"""Gets the is_free of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   是否使用免费额度创建的任务。 **约束限制：**   不涉及。 **取值范围：**   - true：免费任务 - false：付费任务 **默认取值：**   不涉及。 

        :return: The is_free of this EvaluationOpsSynthesisTaskSummary.
        :rtype: bool
        """
        return self._is_free

    @is_free.setter
    def is_free(self, is_free):
        r"""Sets the is_free of this EvaluationOpsSynthesisTaskSummary.

        **参数解释：**   是否使用免费额度创建的任务。 **约束限制：**   不涉及。 **取值范围：**   - true：免费任务 - false：付费任务 **默认取值：**   不涉及。 

        :param is_free: The is_free of this EvaluationOpsSynthesisTaskSummary.
        :type is_free: bool
        """
        self._is_free = is_free

    @property
    def model_config(self):
        r"""Gets the model_config of this EvaluationOpsSynthesisTaskSummary.

        :return: The model_config of this EvaluationOpsSynthesisTaskSummary.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsModelConfig`
        """
        return self._model_config

    @model_config.setter
    def model_config(self, model_config):
        r"""Sets the model_config of this EvaluationOpsSynthesisTaskSummary.

        :param model_config: The model_config of this EvaluationOpsSynthesisTaskSummary.
        :type model_config: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsModelConfig`
        """
        self._model_config = model_config

    @property
    def seed_data(self):
        r"""Gets the seed_data of this EvaluationOpsSynthesisTaskSummary.

        :return: The seed_data of this EvaluationOpsSynthesisTaskSummary.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsSeedDataConfig`
        """
        return self._seed_data

    @seed_data.setter
    def seed_data(self, seed_data):
        r"""Sets the seed_data of this EvaluationOpsSynthesisTaskSummary.

        :param seed_data: The seed_data of this EvaluationOpsSynthesisTaskSummary.
        :type seed_data: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsSeedDataConfig`
        """
        self._seed_data = seed_data

    @property
    def base_info(self):
        r"""Gets the base_info of this EvaluationOpsSynthesisTaskSummary.

        :return: The base_info of this EvaluationOpsSynthesisTaskSummary.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsTaskBaseInfo`
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        r"""Sets the base_info of this EvaluationOpsSynthesisTaskSummary.

        :param base_info: The base_info of this EvaluationOpsSynthesisTaskSummary.
        :type base_info: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsTaskBaseInfo`
        """
        self._base_info = base_info

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
        if not isinstance(other, EvaluationOpsSynthesisTaskSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
