# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineDTO:

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
        'description': 'str',
        'is_publish': 'bool',
        'sources': 'list[CodeSource]',
        'variables': 'list[CustomVariable]',
        'schedules': 'list[PipelineSchedule]',
        'triggers': 'list[PipelineTrigger]',
        'manifest_version': 'str',
        'definition': 'str',
        'project_name': 'str',
        'group_id': 'str',
        'id': 'str',
        'concurrency_control': 'PipelineConcurrencyMgmt',
        'security_level': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'is_publish': 'is_publish',
        'sources': 'sources',
        'variables': 'variables',
        'schedules': 'schedules',
        'triggers': 'triggers',
        'manifest_version': 'manifest_version',
        'definition': 'definition',
        'project_name': 'project_name',
        'group_id': 'group_id',
        'id': 'id',
        'concurrency_control': 'concurrency_control',
        'security_level': 'security_level'
    }

    def __init__(self, name=None, description=None, is_publish=None, sources=None, variables=None, schedules=None, triggers=None, manifest_version=None, definition=None, project_name=None, group_id=None, id=None, concurrency_control=None, security_level=None):
        r"""PipelineDTO

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 流水线名称。 **约束限制**： 不涉及。 **取值范围**： 仅包含中文、大小写英文字母、数字、&#39;-&#39;和&#39;_&#39;，且长度为[1,128]个字符。 **默认取值**： 不涉及。 
        :type name: str
        :param description: **参数解释**： 流水线描述。 **约束限制**： 不涉及。 **取值范围**： 不超过1024字符。 **默认取值**： 不涉及。 
        :type description: str
        :param is_publish: **参数解释**： 是否为变更流水线。 **约束限制**： 不涉及。 **取值范围**： - true：变更流水线。 - false：非变更流水线。 **默认取值**： 不涉及。 
        :type is_publish: bool
        :param sources: **参数解释**： 流水线源信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.CodeSource`]
        :param variables: **参数解释**： 流水线自定义全局变量列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.CustomVariable`]
        :param schedules: **参数解释**： 流水线定时执行配置列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type schedules: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSchedule`]
        :param triggers: **参数解释**： 流水线代码事件触发配置。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type triggers: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTrigger`]
        :param manifest_version: **参数解释**： 流水线结构定义版本。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 3.0。 
        :type manifest_version: str
        :param definition: **参数解释**： 流水线结构定义JSON。该字段结构复杂，建议使用页面编辑流水线后，从[查询流水线详情](ShowPipelineDetail.xml)接口获取。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type definition: str
        :param project_name: **参数解释**： 项目名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type project_name: str
        :param group_id: **参数解释**： 流水线组ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 
        :type group_id: str
        :param id: **参数解释**： 复制场景使用，为流水线组ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 
        :type id: str
        :param concurrency_control: 
        :type concurrency_control: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineConcurrencyMgmt`
        :param security_level: **参数解释**： 流水线涉密等级。 **约束限制**： 非涉密场景不涉及，涉密场景必填。 **取值范围**： 正整数（1为最低密级）。 **默认取值**： 不涉及。 
        :type security_level: int
        """
        
        

        self._name = None
        self._description = None
        self._is_publish = None
        self._sources = None
        self._variables = None
        self._schedules = None
        self._triggers = None
        self._manifest_version = None
        self._definition = None
        self._project_name = None
        self._group_id = None
        self._id = None
        self._concurrency_control = None
        self._security_level = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.is_publish = is_publish
        if sources is not None:
            self.sources = sources
        if variables is not None:
            self.variables = variables
        if schedules is not None:
            self.schedules = schedules
        if triggers is not None:
            self.triggers = triggers
        if manifest_version is not None:
            self.manifest_version = manifest_version
        self.definition = definition
        if project_name is not None:
            self.project_name = project_name
        if group_id is not None:
            self.group_id = group_id
        if id is not None:
            self.id = id
        if concurrency_control is not None:
            self.concurrency_control = concurrency_control
        if security_level is not None:
            self.security_level = security_level

    @property
    def name(self):
        r"""Gets the name of this PipelineDTO.

        **参数解释**： 流水线名称。 **约束限制**： 不涉及。 **取值范围**： 仅包含中文、大小写英文字母、数字、'-'和'_'，且长度为[1,128]个字符。 **默认取值**： 不涉及。 

        :return: The name of this PipelineDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PipelineDTO.

        **参数解释**： 流水线名称。 **约束限制**： 不涉及。 **取值范围**： 仅包含中文、大小写英文字母、数字、'-'和'_'，且长度为[1,128]个字符。 **默认取值**： 不涉及。 

        :param name: The name of this PipelineDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this PipelineDTO.

        **参数解释**： 流水线描述。 **约束限制**： 不涉及。 **取值范围**： 不超过1024字符。 **默认取值**： 不涉及。 

        :return: The description of this PipelineDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PipelineDTO.

        **参数解释**： 流水线描述。 **约束限制**： 不涉及。 **取值范围**： 不超过1024字符。 **默认取值**： 不涉及。 

        :param description: The description of this PipelineDTO.
        :type description: str
        """
        self._description = description

    @property
    def is_publish(self):
        r"""Gets the is_publish of this PipelineDTO.

        **参数解释**： 是否为变更流水线。 **约束限制**： 不涉及。 **取值范围**： - true：变更流水线。 - false：非变更流水线。 **默认取值**： 不涉及。 

        :return: The is_publish of this PipelineDTO.
        :rtype: bool
        """
        return self._is_publish

    @is_publish.setter
    def is_publish(self, is_publish):
        r"""Sets the is_publish of this PipelineDTO.

        **参数解释**： 是否为变更流水线。 **约束限制**： 不涉及。 **取值范围**： - true：变更流水线。 - false：非变更流水线。 **默认取值**： 不涉及。 

        :param is_publish: The is_publish of this PipelineDTO.
        :type is_publish: bool
        """
        self._is_publish = is_publish

    @property
    def sources(self):
        r"""Gets the sources of this PipelineDTO.

        **参数解释**： 流水线源信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The sources of this PipelineDTO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.CodeSource`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this PipelineDTO.

        **参数解释**： 流水线源信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param sources: The sources of this PipelineDTO.
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.CodeSource`]
        """
        self._sources = sources

    @property
    def variables(self):
        r"""Gets the variables of this PipelineDTO.

        **参数解释**： 流水线自定义全局变量列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The variables of this PipelineDTO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.CustomVariable`]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        r"""Sets the variables of this PipelineDTO.

        **参数解释**： 流水线自定义全局变量列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param variables: The variables of this PipelineDTO.
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.CustomVariable`]
        """
        self._variables = variables

    @property
    def schedules(self):
        r"""Gets the schedules of this PipelineDTO.

        **参数解释**： 流水线定时执行配置列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The schedules of this PipelineDTO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSchedule`]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        r"""Sets the schedules of this PipelineDTO.

        **参数解释**： 流水线定时执行配置列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param schedules: The schedules of this PipelineDTO.
        :type schedules: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSchedule`]
        """
        self._schedules = schedules

    @property
    def triggers(self):
        r"""Gets the triggers of this PipelineDTO.

        **参数解释**： 流水线代码事件触发配置。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The triggers of this PipelineDTO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        r"""Sets the triggers of this PipelineDTO.

        **参数解释**： 流水线代码事件触发配置。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param triggers: The triggers of this PipelineDTO.
        :type triggers: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTrigger`]
        """
        self._triggers = triggers

    @property
    def manifest_version(self):
        r"""Gets the manifest_version of this PipelineDTO.

        **参数解释**： 流水线结构定义版本。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 3.0。 

        :return: The manifest_version of this PipelineDTO.
        :rtype: str
        """
        return self._manifest_version

    @manifest_version.setter
    def manifest_version(self, manifest_version):
        r"""Sets the manifest_version of this PipelineDTO.

        **参数解释**： 流水线结构定义版本。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 3.0。 

        :param manifest_version: The manifest_version of this PipelineDTO.
        :type manifest_version: str
        """
        self._manifest_version = manifest_version

    @property
    def definition(self):
        r"""Gets the definition of this PipelineDTO.

        **参数解释**： 流水线结构定义JSON。该字段结构复杂，建议使用页面编辑流水线后，从[查询流水线详情](ShowPipelineDetail.xml)接口获取。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The definition of this PipelineDTO.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        r"""Sets the definition of this PipelineDTO.

        **参数解释**： 流水线结构定义JSON。该字段结构复杂，建议使用页面编辑流水线后，从[查询流水线详情](ShowPipelineDetail.xml)接口获取。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param definition: The definition of this PipelineDTO.
        :type definition: str
        """
        self._definition = definition

    @property
    def project_name(self):
        r"""Gets the project_name of this PipelineDTO.

        **参数解释**： 项目名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The project_name of this PipelineDTO.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this PipelineDTO.

        **参数解释**： 项目名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param project_name: The project_name of this PipelineDTO.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def group_id(self):
        r"""Gets the group_id of this PipelineDTO.

        **参数解释**： 流水线组ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 

        :return: The group_id of this PipelineDTO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this PipelineDTO.

        **参数解释**： 流水线组ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 

        :param group_id: The group_id of this PipelineDTO.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def id(self):
        r"""Gets the id of this PipelineDTO.

        **参数解释**： 复制场景使用，为流水线组ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 

        :return: The id of this PipelineDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PipelineDTO.

        **参数解释**： 复制场景使用，为流水线组ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 

        :param id: The id of this PipelineDTO.
        :type id: str
        """
        self._id = id

    @property
    def concurrency_control(self):
        r"""Gets the concurrency_control of this PipelineDTO.

        :return: The concurrency_control of this PipelineDTO.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineConcurrencyMgmt`
        """
        return self._concurrency_control

    @concurrency_control.setter
    def concurrency_control(self, concurrency_control):
        r"""Sets the concurrency_control of this PipelineDTO.

        :param concurrency_control: The concurrency_control of this PipelineDTO.
        :type concurrency_control: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineConcurrencyMgmt`
        """
        self._concurrency_control = concurrency_control

    @property
    def security_level(self):
        r"""Gets the security_level of this PipelineDTO.

        **参数解释**： 流水线涉密等级。 **约束限制**： 非涉密场景不涉及，涉密场景必填。 **取值范围**： 正整数（1为最低密级）。 **默认取值**： 不涉及。 

        :return: The security_level of this PipelineDTO.
        :rtype: int
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        r"""Sets the security_level of this PipelineDTO.

        **参数解释**： 流水线涉密等级。 **约束限制**： 非涉密场景不涉及，涉密场景必填。 **取值范围**： 正整数（1为最低密级）。 **默认取值**： 不涉及。 

        :param security_level: The security_level of this PipelineDTO.
        :type security_level: int
        """
        self._security_level = security_level

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
        if not isinstance(other, PipelineDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
