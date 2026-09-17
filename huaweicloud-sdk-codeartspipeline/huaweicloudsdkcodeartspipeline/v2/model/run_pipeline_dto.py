# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunPipelineDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sources': 'list[RunPipelineDTOSources]',
        'description': 'str',
        'variables': 'list[RunPipelineDTOVariables]',
        'choose_jobs': 'list[str]',
        'choose_stages': 'list[str]',
        'sub_hook': 'bool',
        'execution_plan_id': 'str'
    }

    attribute_map = {
        'sources': 'sources',
        'description': 'description',
        'variables': 'variables',
        'choose_jobs': 'choose_jobs',
        'choose_stages': 'choose_stages',
        'sub_hook': 'sub_hook',
        'execution_plan_id': 'execution_plan_id'
    }

    def __init__(self, sources=None, description=None, variables=None, choose_jobs=None, choose_stages=None, sub_hook=None, execution_plan_id=None):
        r"""RunPipelineDTO

        The model defined in huaweicloud sdk

        :param sources: **参数解释**： 代码源信息列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineDTOSources`]
        :param description: **参数解释**： 流水线运行描述。 **约束限制**： 不涉及。 **取值范围**： 不超过1024字符。 **默认取值**： 不涉及。 
        :type description: str
        :param variables: **参数解释**： 使用的自定义参数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineDTOVariables`]
        :param choose_jobs: **参数解释**： 流水线运行时选择的流水线任务。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type choose_jobs: list[str]
        :param choose_stages: **参数解释**： 选择的流水线阶段。优先级高于choose_jobs，即stage未选择时，无视choose_jobs中该stage下的job。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type choose_stages: list[str]
        :param sub_hook: **参数解释**： 是否为子流水线触发。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type sub_hook: bool
        :param execution_plan_id: **参数解释**： 使用哪一个执行方案运行流水线。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type execution_plan_id: str
        """
        
        

        self._sources = None
        self._description = None
        self._variables = None
        self._choose_jobs = None
        self._choose_stages = None
        self._sub_hook = None
        self._execution_plan_id = None
        self.discriminator = None

        if sources is not None:
            self.sources = sources
        if description is not None:
            self.description = description
        if variables is not None:
            self.variables = variables
        if choose_jobs is not None:
            self.choose_jobs = choose_jobs
        if choose_stages is not None:
            self.choose_stages = choose_stages
        if sub_hook is not None:
            self.sub_hook = sub_hook
        if execution_plan_id is not None:
            self.execution_plan_id = execution_plan_id

    @property
    def sources(self):
        r"""Gets the sources of this RunPipelineDTO.

        **参数解释**： 代码源信息列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The sources of this RunPipelineDTO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineDTOSources`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this RunPipelineDTO.

        **参数解释**： 代码源信息列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param sources: The sources of this RunPipelineDTO.
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineDTOSources`]
        """
        self._sources = sources

    @property
    def description(self):
        r"""Gets the description of this RunPipelineDTO.

        **参数解释**： 流水线运行描述。 **约束限制**： 不涉及。 **取值范围**： 不超过1024字符。 **默认取值**： 不涉及。 

        :return: The description of this RunPipelineDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RunPipelineDTO.

        **参数解释**： 流水线运行描述。 **约束限制**： 不涉及。 **取值范围**： 不超过1024字符。 **默认取值**： 不涉及。 

        :param description: The description of this RunPipelineDTO.
        :type description: str
        """
        self._description = description

    @property
    def variables(self):
        r"""Gets the variables of this RunPipelineDTO.

        **参数解释**： 使用的自定义参数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The variables of this RunPipelineDTO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineDTOVariables`]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        r"""Sets the variables of this RunPipelineDTO.

        **参数解释**： 使用的自定义参数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param variables: The variables of this RunPipelineDTO.
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineDTOVariables`]
        """
        self._variables = variables

    @property
    def choose_jobs(self):
        r"""Gets the choose_jobs of this RunPipelineDTO.

        **参数解释**： 流水线运行时选择的流水线任务。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The choose_jobs of this RunPipelineDTO.
        :rtype: list[str]
        """
        return self._choose_jobs

    @choose_jobs.setter
    def choose_jobs(self, choose_jobs):
        r"""Sets the choose_jobs of this RunPipelineDTO.

        **参数解释**： 流水线运行时选择的流水线任务。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param choose_jobs: The choose_jobs of this RunPipelineDTO.
        :type choose_jobs: list[str]
        """
        self._choose_jobs = choose_jobs

    @property
    def choose_stages(self):
        r"""Gets the choose_stages of this RunPipelineDTO.

        **参数解释**： 选择的流水线阶段。优先级高于choose_jobs，即stage未选择时，无视choose_jobs中该stage下的job。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The choose_stages of this RunPipelineDTO.
        :rtype: list[str]
        """
        return self._choose_stages

    @choose_stages.setter
    def choose_stages(self, choose_stages):
        r"""Sets the choose_stages of this RunPipelineDTO.

        **参数解释**： 选择的流水线阶段。优先级高于choose_jobs，即stage未选择时，无视choose_jobs中该stage下的job。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param choose_stages: The choose_stages of this RunPipelineDTO.
        :type choose_stages: list[str]
        """
        self._choose_stages = choose_stages

    @property
    def sub_hook(self):
        r"""Gets the sub_hook of this RunPipelineDTO.

        **参数解释**： 是否为子流水线触发。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The sub_hook of this RunPipelineDTO.
        :rtype: bool
        """
        return self._sub_hook

    @sub_hook.setter
    def sub_hook(self, sub_hook):
        r"""Sets the sub_hook of this RunPipelineDTO.

        **参数解释**： 是否为子流水线触发。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param sub_hook: The sub_hook of this RunPipelineDTO.
        :type sub_hook: bool
        """
        self._sub_hook = sub_hook

    @property
    def execution_plan_id(self):
        r"""Gets the execution_plan_id of this RunPipelineDTO.

        **参数解释**： 使用哪一个执行方案运行流水线。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The execution_plan_id of this RunPipelineDTO.
        :rtype: str
        """
        return self._execution_plan_id

    @execution_plan_id.setter
    def execution_plan_id(self, execution_plan_id):
        r"""Sets the execution_plan_id of this RunPipelineDTO.

        **参数解释**： 使用哪一个执行方案运行流水线。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param execution_plan_id: The execution_plan_id of this RunPipelineDTO.
        :type execution_plan_id: str
        """
        self._execution_plan_id = execution_plan_id

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
        if not isinstance(other, RunPipelineDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
