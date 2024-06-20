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
        'concurrency_control': 'PipelineConcurrencyMgmt'
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
        'concurrency_control': 'concurrency_control'
    }

    def __init__(self, name=None, description=None, is_publish=None, sources=None, variables=None, schedules=None, triggers=None, manifest_version=None, definition=None, project_name=None, group_id=None, id=None, concurrency_control=None):
        """PipelineDTO

        The model defined in huaweicloud sdk

        :param name: 流水线名称
        :type name: str
        :param description: 流水线描述
        :type description: str
        :param is_publish: 是否为发布流水线
        :type is_publish: bool
        :param sources: 流水线源
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.CodeSource`]
        :param variables: 流水线自定义全局变量
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.CustomVariable`]
        :param schedules: 流水线定时执行配置
        :type schedules: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSchedule`]
        :param triggers: 流水线代码事件触发配置
        :type triggers: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTrigger`]
        :param manifest_version: 流水线结构定义版本，新版默认为3.0
        :type manifest_version: str
        :param definition: 流水线结构定义
        :type definition: str
        :param project_name: 项目名称
        :type project_name: str
        :param group_id: 流水线组ID
        :type group_id: str
        :param id: 若为复制场景，则为原流水线ID
        :type id: str
        :param concurrency_control: 
        :type concurrency_control: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineConcurrencyMgmt`
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

    @property
    def name(self):
        """Gets the name of this PipelineDTO.

        流水线名称

        :return: The name of this PipelineDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelineDTO.

        流水线名称

        :param name: The name of this PipelineDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this PipelineDTO.

        流水线描述

        :return: The description of this PipelineDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PipelineDTO.

        流水线描述

        :param description: The description of this PipelineDTO.
        :type description: str
        """
        self._description = description

    @property
    def is_publish(self):
        """Gets the is_publish of this PipelineDTO.

        是否为发布流水线

        :return: The is_publish of this PipelineDTO.
        :rtype: bool
        """
        return self._is_publish

    @is_publish.setter
    def is_publish(self, is_publish):
        """Sets the is_publish of this PipelineDTO.

        是否为发布流水线

        :param is_publish: The is_publish of this PipelineDTO.
        :type is_publish: bool
        """
        self._is_publish = is_publish

    @property
    def sources(self):
        """Gets the sources of this PipelineDTO.

        流水线源

        :return: The sources of this PipelineDTO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.CodeSource`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this PipelineDTO.

        流水线源

        :param sources: The sources of this PipelineDTO.
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.CodeSource`]
        """
        self._sources = sources

    @property
    def variables(self):
        """Gets the variables of this PipelineDTO.

        流水线自定义全局变量

        :return: The variables of this PipelineDTO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.CustomVariable`]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this PipelineDTO.

        流水线自定义全局变量

        :param variables: The variables of this PipelineDTO.
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.CustomVariable`]
        """
        self._variables = variables

    @property
    def schedules(self):
        """Gets the schedules of this PipelineDTO.

        流水线定时执行配置

        :return: The schedules of this PipelineDTO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSchedule`]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """Sets the schedules of this PipelineDTO.

        流水线定时执行配置

        :param schedules: The schedules of this PipelineDTO.
        :type schedules: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSchedule`]
        """
        self._schedules = schedules

    @property
    def triggers(self):
        """Gets the triggers of this PipelineDTO.

        流水线代码事件触发配置

        :return: The triggers of this PipelineDTO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this PipelineDTO.

        流水线代码事件触发配置

        :param triggers: The triggers of this PipelineDTO.
        :type triggers: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTrigger`]
        """
        self._triggers = triggers

    @property
    def manifest_version(self):
        """Gets the manifest_version of this PipelineDTO.

        流水线结构定义版本，新版默认为3.0

        :return: The manifest_version of this PipelineDTO.
        :rtype: str
        """
        return self._manifest_version

    @manifest_version.setter
    def manifest_version(self, manifest_version):
        """Sets the manifest_version of this PipelineDTO.

        流水线结构定义版本，新版默认为3.0

        :param manifest_version: The manifest_version of this PipelineDTO.
        :type manifest_version: str
        """
        self._manifest_version = manifest_version

    @property
    def definition(self):
        """Gets the definition of this PipelineDTO.

        流水线结构定义

        :return: The definition of this PipelineDTO.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this PipelineDTO.

        流水线结构定义

        :param definition: The definition of this PipelineDTO.
        :type definition: str
        """
        self._definition = definition

    @property
    def project_name(self):
        """Gets the project_name of this PipelineDTO.

        项目名称

        :return: The project_name of this PipelineDTO.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this PipelineDTO.

        项目名称

        :param project_name: The project_name of this PipelineDTO.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def group_id(self):
        """Gets the group_id of this PipelineDTO.

        流水线组ID

        :return: The group_id of this PipelineDTO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this PipelineDTO.

        流水线组ID

        :param group_id: The group_id of this PipelineDTO.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def id(self):
        """Gets the id of this PipelineDTO.

        若为复制场景，则为原流水线ID

        :return: The id of this PipelineDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PipelineDTO.

        若为复制场景，则为原流水线ID

        :param id: The id of this PipelineDTO.
        :type id: str
        """
        self._id = id

    @property
    def concurrency_control(self):
        """Gets the concurrency_control of this PipelineDTO.

        :return: The concurrency_control of this PipelineDTO.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineConcurrencyMgmt`
        """
        return self._concurrency_control

    @concurrency_control.setter
    def concurrency_control(self, concurrency_control):
        """Sets the concurrency_control of this PipelineDTO.

        :param concurrency_control: The concurrency_control of this PipelineDTO.
        :type concurrency_control: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineConcurrencyMgmt`
        """
        self._concurrency_control = concurrency_control

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
