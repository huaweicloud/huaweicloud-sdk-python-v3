# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsSynthesisTaskResponse(SdkResponse):

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
        'status': 'str',
        'stats': 'EvaluationOpsSynthesisStats',
        'usage': 'EvaluationOpsTokenUsage',
        'model_config': 'EvaluationOpsModelConfig',
        'seed_data': 'EvaluationOpsSeedDataConfig',
        'schemas': 'list[EvaluationOpsSynthesisSchema]',
        'base_info': 'EvaluationOpsTaskBaseInfo'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'scenario_type': 'scenario_type',
        'scenario_name': 'scenario_name',
        'scenario_description': 'scenario_description',
        'status': 'status',
        'stats': 'stats',
        'usage': 'usage',
        'model_config': 'model_config',
        'seed_data': 'seed_data',
        'schemas': 'schemas',
        'base_info': 'base_info'
    }

    def __init__(self, id=None, name=None, scenario_type=None, scenario_name=None, scenario_description=None, status=None, stats=None, usage=None, model_config=None, seed_data=None, schemas=None, base_info=None):
        r"""ShowOpsSynthesisTaskResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 合成任务的唯一标识符。 
        :type id: str
        :param name: **参数解释：** 用户为合成任务定义的描述性名称。 
        :type name: str
        :param scenario_type: **参数解释：** 合成任务所属的技术场景分类标识。 
        :type scenario_type: str
        :param scenario_name: **参数解释：** 合成场景的友好展示名称。 
        :type scenario_name: str
        :param scenario_description: **参数解释：** 该合成任务具体业务逻辑或目标的详细说明。 
        :type scenario_description: str
        :param status: **参数解释：** 合成任务当前的生命周期运行状态。 **取值范围：** 字符长度1-100，pending(等待执行)，running(正在运行)，completed(已完成)，failed(执行失败)，stopped(已人工停止)。 
        :type status: str
        :param stats: 
        :type stats: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsSynthesisStats`
        :param usage: 
        :type usage: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsTokenUsage`
        :param model_config: 
        :type model_config: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsModelConfig`
        :param seed_data: 
        :type seed_data: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsSeedDataConfig`
        :param schemas: **参数解释：** 合成数据所遵循的字段结构定义（Schema）列表。 **取值范围：** 包含字段名称、类型、描述等元数据的对象数组。 
        :type schemas: list[:class:`huaweicloudsdkagentarts.v1.EvaluationOpsSynthesisSchema`]
        :param base_info: 
        :type base_info: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsTaskBaseInfo`
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._scenario_type = None
        self._scenario_name = None
        self._scenario_description = None
        self._status = None
        self._stats = None
        self._usage = None
        self._model_config = None
        self._seed_data = None
        self._schemas = None
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
        if status is not None:
            self.status = status
        if stats is not None:
            self.stats = stats
        if usage is not None:
            self.usage = usage
        if model_config is not None:
            self.model_config = model_config
        if seed_data is not None:
            self.seed_data = seed_data
        if schemas is not None:
            self.schemas = schemas
        if base_info is not None:
            self.base_info = base_info

    @property
    def id(self):
        r"""Gets the id of this ShowOpsSynthesisTaskResponse.

        **参数解释：** 合成任务的唯一标识符。 

        :return: The id of this ShowOpsSynthesisTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowOpsSynthesisTaskResponse.

        **参数解释：** 合成任务的唯一标识符。 

        :param id: The id of this ShowOpsSynthesisTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowOpsSynthesisTaskResponse.

        **参数解释：** 用户为合成任务定义的描述性名称。 

        :return: The name of this ShowOpsSynthesisTaskResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowOpsSynthesisTaskResponse.

        **参数解释：** 用户为合成任务定义的描述性名称。 

        :param name: The name of this ShowOpsSynthesisTaskResponse.
        :type name: str
        """
        self._name = name

    @property
    def scenario_type(self):
        r"""Gets the scenario_type of this ShowOpsSynthesisTaskResponse.

        **参数解释：** 合成任务所属的技术场景分类标识。 

        :return: The scenario_type of this ShowOpsSynthesisTaskResponse.
        :rtype: str
        """
        return self._scenario_type

    @scenario_type.setter
    def scenario_type(self, scenario_type):
        r"""Sets the scenario_type of this ShowOpsSynthesisTaskResponse.

        **参数解释：** 合成任务所属的技术场景分类标识。 

        :param scenario_type: The scenario_type of this ShowOpsSynthesisTaskResponse.
        :type scenario_type: str
        """
        self._scenario_type = scenario_type

    @property
    def scenario_name(self):
        r"""Gets the scenario_name of this ShowOpsSynthesisTaskResponse.

        **参数解释：** 合成场景的友好展示名称。 

        :return: The scenario_name of this ShowOpsSynthesisTaskResponse.
        :rtype: str
        """
        return self._scenario_name

    @scenario_name.setter
    def scenario_name(self, scenario_name):
        r"""Sets the scenario_name of this ShowOpsSynthesisTaskResponse.

        **参数解释：** 合成场景的友好展示名称。 

        :param scenario_name: The scenario_name of this ShowOpsSynthesisTaskResponse.
        :type scenario_name: str
        """
        self._scenario_name = scenario_name

    @property
    def scenario_description(self):
        r"""Gets the scenario_description of this ShowOpsSynthesisTaskResponse.

        **参数解释：** 该合成任务具体业务逻辑或目标的详细说明。 

        :return: The scenario_description of this ShowOpsSynthesisTaskResponse.
        :rtype: str
        """
        return self._scenario_description

    @scenario_description.setter
    def scenario_description(self, scenario_description):
        r"""Sets the scenario_description of this ShowOpsSynthesisTaskResponse.

        **参数解释：** 该合成任务具体业务逻辑或目标的详细说明。 

        :param scenario_description: The scenario_description of this ShowOpsSynthesisTaskResponse.
        :type scenario_description: str
        """
        self._scenario_description = scenario_description

    @property
    def status(self):
        r"""Gets the status of this ShowOpsSynthesisTaskResponse.

        **参数解释：** 合成任务当前的生命周期运行状态。 **取值范围：** 字符长度1-100，pending(等待执行)，running(正在运行)，completed(已完成)，failed(执行失败)，stopped(已人工停止)。 

        :return: The status of this ShowOpsSynthesisTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowOpsSynthesisTaskResponse.

        **参数解释：** 合成任务当前的生命周期运行状态。 **取值范围：** 字符长度1-100，pending(等待执行)，running(正在运行)，completed(已完成)，failed(执行失败)，stopped(已人工停止)。 

        :param status: The status of this ShowOpsSynthesisTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def stats(self):
        r"""Gets the stats of this ShowOpsSynthesisTaskResponse.

        :return: The stats of this ShowOpsSynthesisTaskResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsSynthesisStats`
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        r"""Sets the stats of this ShowOpsSynthesisTaskResponse.

        :param stats: The stats of this ShowOpsSynthesisTaskResponse.
        :type stats: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsSynthesisStats`
        """
        self._stats = stats

    @property
    def usage(self):
        r"""Gets the usage of this ShowOpsSynthesisTaskResponse.

        :return: The usage of this ShowOpsSynthesisTaskResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsTokenUsage`
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        r"""Sets the usage of this ShowOpsSynthesisTaskResponse.

        :param usage: The usage of this ShowOpsSynthesisTaskResponse.
        :type usage: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsTokenUsage`
        """
        self._usage = usage

    @property
    def model_config(self):
        r"""Gets the model_config of this ShowOpsSynthesisTaskResponse.

        :return: The model_config of this ShowOpsSynthesisTaskResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsModelConfig`
        """
        return self._model_config

    @model_config.setter
    def model_config(self, model_config):
        r"""Sets the model_config of this ShowOpsSynthesisTaskResponse.

        :param model_config: The model_config of this ShowOpsSynthesisTaskResponse.
        :type model_config: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsModelConfig`
        """
        self._model_config = model_config

    @property
    def seed_data(self):
        r"""Gets the seed_data of this ShowOpsSynthesisTaskResponse.

        :return: The seed_data of this ShowOpsSynthesisTaskResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsSeedDataConfig`
        """
        return self._seed_data

    @seed_data.setter
    def seed_data(self, seed_data):
        r"""Sets the seed_data of this ShowOpsSynthesisTaskResponse.

        :param seed_data: The seed_data of this ShowOpsSynthesisTaskResponse.
        :type seed_data: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsSeedDataConfig`
        """
        self._seed_data = seed_data

    @property
    def schemas(self):
        r"""Gets the schemas of this ShowOpsSynthesisTaskResponse.

        **参数解释：** 合成数据所遵循的字段结构定义（Schema）列表。 **取值范围：** 包含字段名称、类型、描述等元数据的对象数组。 

        :return: The schemas of this ShowOpsSynthesisTaskResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.EvaluationOpsSynthesisSchema`]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        r"""Sets the schemas of this ShowOpsSynthesisTaskResponse.

        **参数解释：** 合成数据所遵循的字段结构定义（Schema）列表。 **取值范围：** 包含字段名称、类型、描述等元数据的对象数组。 

        :param schemas: The schemas of this ShowOpsSynthesisTaskResponse.
        :type schemas: list[:class:`huaweicloudsdkagentarts.v1.EvaluationOpsSynthesisSchema`]
        """
        self._schemas = schemas

    @property
    def base_info(self):
        r"""Gets the base_info of this ShowOpsSynthesisTaskResponse.

        :return: The base_info of this ShowOpsSynthesisTaskResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsTaskBaseInfo`
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        r"""Sets the base_info of this ShowOpsSynthesisTaskResponse.

        :param base_info: The base_info of this ShowOpsSynthesisTaskResponse.
        :type base_info: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsTaskBaseInfo`
        """
        self._base_info = base_info

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpsSynthesisTaskResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowOpsSynthesisTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
