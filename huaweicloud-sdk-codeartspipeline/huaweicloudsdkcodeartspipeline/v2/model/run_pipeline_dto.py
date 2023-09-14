# coding: utf-8

import six

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
        'choose_stages': 'list[str]'
    }

    attribute_map = {
        'sources': 'sources',
        'description': 'description',
        'variables': 'variables',
        'choose_jobs': 'choose_jobs',
        'choose_stages': 'choose_stages'
    }

    def __init__(self, sources=None, description=None, variables=None, choose_jobs=None, choose_stages=None):
        """RunPipelineDTO

        The model defined in huaweicloud sdk

        :param sources: 使用的源
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineDTOSources`]
        :param description: 运行描述
        :type description: str
        :param variables: 使用的自定义参数
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineDTOVariables`]
        :param choose_jobs: 选择的任务
        :type choose_jobs: list[str]
        :param choose_stages: 选择的阶段
        :type choose_stages: list[str]
        """
        
        

        self._sources = None
        self._description = None
        self._variables = None
        self._choose_jobs = None
        self._choose_stages = None
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

    @property
    def sources(self):
        """Gets the sources of this RunPipelineDTO.

        使用的源

        :return: The sources of this RunPipelineDTO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineDTOSources`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this RunPipelineDTO.

        使用的源

        :param sources: The sources of this RunPipelineDTO.
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineDTOSources`]
        """
        self._sources = sources

    @property
    def description(self):
        """Gets the description of this RunPipelineDTO.

        运行描述

        :return: The description of this RunPipelineDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RunPipelineDTO.

        运行描述

        :param description: The description of this RunPipelineDTO.
        :type description: str
        """
        self._description = description

    @property
    def variables(self):
        """Gets the variables of this RunPipelineDTO.

        使用的自定义参数

        :return: The variables of this RunPipelineDTO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineDTOVariables`]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this RunPipelineDTO.

        使用的自定义参数

        :param variables: The variables of this RunPipelineDTO.
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineDTOVariables`]
        """
        self._variables = variables

    @property
    def choose_jobs(self):
        """Gets the choose_jobs of this RunPipelineDTO.

        选择的任务

        :return: The choose_jobs of this RunPipelineDTO.
        :rtype: list[str]
        """
        return self._choose_jobs

    @choose_jobs.setter
    def choose_jobs(self, choose_jobs):
        """Sets the choose_jobs of this RunPipelineDTO.

        选择的任务

        :param choose_jobs: The choose_jobs of this RunPipelineDTO.
        :type choose_jobs: list[str]
        """
        self._choose_jobs = choose_jobs

    @property
    def choose_stages(self):
        """Gets the choose_stages of this RunPipelineDTO.

        选择的阶段

        :return: The choose_stages of this RunPipelineDTO.
        :rtype: list[str]
        """
        return self._choose_stages

    @choose_stages.setter
    def choose_stages(self, choose_stages):
        """Sets the choose_stages of this RunPipelineDTO.

        选择的阶段

        :param choose_stages: The choose_stages of this RunPipelineDTO.
        :type choose_stages: list[str]
        """
        self._choose_stages = choose_stages

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
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
