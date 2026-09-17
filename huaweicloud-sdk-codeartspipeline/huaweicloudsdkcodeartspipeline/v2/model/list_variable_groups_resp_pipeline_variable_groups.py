# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVariableGroupsRespPipelineVariableGroups:

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
        'project_id': 'str',
        'domain_id': 'str',
        'name': 'str',
        'description': 'str',
        'variables': 'list[QueryVariableGroupDetailRespVariables]',
        'related_pipelines': 'list[ListVariableGroupsRespRelatedPipelines]',
        'creator_id': 'str',
        'updater_id': 'str',
        'creator_name': 'str',
        'updater_name': 'str',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'domain_id': 'domain_id',
        'name': 'name',
        'description': 'description',
        'variables': 'variables',
        'related_pipelines': 'related_pipelines',
        'creator_id': 'creator_id',
        'updater_id': 'updater_id',
        'creator_name': 'creator_name',
        'updater_name': 'updater_name',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, project_id=None, domain_id=None, name=None, description=None, variables=None, related_pipelines=None, creator_id=None, updater_id=None, creator_name=None, updater_name=None, create_time=None, update_time=None):
        r"""ListVariableGroupsRespPipelineVariableGroups

        The model defined in huaweicloud sdk

        :param id: 参数组ID
        :type id: str
        :param project_id: 项目ID
        :type project_id: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param name: 参数组名称
        :type name: str
        :param description: 描述
        :type description: str
        :param variables: **参数解释**： 参数列表。 **取值范围**： 不涉及。 
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.QueryVariableGroupDetailRespVariables`]
        :param related_pipelines: 关联的流水线
        :type related_pipelines: list[:class:`huaweicloudsdkcodeartspipeline.v2.ListVariableGroupsRespRelatedPipelines`]
        :param creator_id: 创建人ID
        :type creator_id: str
        :param updater_id: 更新人ID
        :type updater_id: str
        :param creator_name: 创建人名称
        :type creator_name: str
        :param updater_name: 更新人名称
        :type updater_name: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        """
        
        

        self._id = None
        self._project_id = None
        self._domain_id = None
        self._name = None
        self._description = None
        self._variables = None
        self._related_pipelines = None
        self._creator_id = None
        self._updater_id = None
        self._creator_name = None
        self._updater_name = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if domain_id is not None:
            self.domain_id = domain_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if variables is not None:
            self.variables = variables
        if related_pipelines is not None:
            self.related_pipelines = related_pipelines
        if creator_id is not None:
            self.creator_id = creator_id
        if updater_id is not None:
            self.updater_id = updater_id
        if creator_name is not None:
            self.creator_name = creator_name
        if updater_name is not None:
            self.updater_name = updater_name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this ListVariableGroupsRespPipelineVariableGroups.

        参数组ID

        :return: The id of this ListVariableGroupsRespPipelineVariableGroups.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListVariableGroupsRespPipelineVariableGroups.

        参数组ID

        :param id: The id of this ListVariableGroupsRespPipelineVariableGroups.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this ListVariableGroupsRespPipelineVariableGroups.

        项目ID

        :return: The project_id of this ListVariableGroupsRespPipelineVariableGroups.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListVariableGroupsRespPipelineVariableGroups.

        项目ID

        :param project_id: The project_id of this ListVariableGroupsRespPipelineVariableGroups.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListVariableGroupsRespPipelineVariableGroups.

        租户ID

        :return: The domain_id of this ListVariableGroupsRespPipelineVariableGroups.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListVariableGroupsRespPipelineVariableGroups.

        租户ID

        :param domain_id: The domain_id of this ListVariableGroupsRespPipelineVariableGroups.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        r"""Gets the name of this ListVariableGroupsRespPipelineVariableGroups.

        参数组名称

        :return: The name of this ListVariableGroupsRespPipelineVariableGroups.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListVariableGroupsRespPipelineVariableGroups.

        参数组名称

        :param name: The name of this ListVariableGroupsRespPipelineVariableGroups.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListVariableGroupsRespPipelineVariableGroups.

        描述

        :return: The description of this ListVariableGroupsRespPipelineVariableGroups.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListVariableGroupsRespPipelineVariableGroups.

        描述

        :param description: The description of this ListVariableGroupsRespPipelineVariableGroups.
        :type description: str
        """
        self._description = description

    @property
    def variables(self):
        r"""Gets the variables of this ListVariableGroupsRespPipelineVariableGroups.

        **参数解释**： 参数列表。 **取值范围**： 不涉及。 

        :return: The variables of this ListVariableGroupsRespPipelineVariableGroups.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.QueryVariableGroupDetailRespVariables`]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        r"""Sets the variables of this ListVariableGroupsRespPipelineVariableGroups.

        **参数解释**： 参数列表。 **取值范围**： 不涉及。 

        :param variables: The variables of this ListVariableGroupsRespPipelineVariableGroups.
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.QueryVariableGroupDetailRespVariables`]
        """
        self._variables = variables

    @property
    def related_pipelines(self):
        r"""Gets the related_pipelines of this ListVariableGroupsRespPipelineVariableGroups.

        关联的流水线

        :return: The related_pipelines of this ListVariableGroupsRespPipelineVariableGroups.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.ListVariableGroupsRespRelatedPipelines`]
        """
        return self._related_pipelines

    @related_pipelines.setter
    def related_pipelines(self, related_pipelines):
        r"""Sets the related_pipelines of this ListVariableGroupsRespPipelineVariableGroups.

        关联的流水线

        :param related_pipelines: The related_pipelines of this ListVariableGroupsRespPipelineVariableGroups.
        :type related_pipelines: list[:class:`huaweicloudsdkcodeartspipeline.v2.ListVariableGroupsRespRelatedPipelines`]
        """
        self._related_pipelines = related_pipelines

    @property
    def creator_id(self):
        r"""Gets the creator_id of this ListVariableGroupsRespPipelineVariableGroups.

        创建人ID

        :return: The creator_id of this ListVariableGroupsRespPipelineVariableGroups.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this ListVariableGroupsRespPipelineVariableGroups.

        创建人ID

        :param creator_id: The creator_id of this ListVariableGroupsRespPipelineVariableGroups.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def updater_id(self):
        r"""Gets the updater_id of this ListVariableGroupsRespPipelineVariableGroups.

        更新人ID

        :return: The updater_id of this ListVariableGroupsRespPipelineVariableGroups.
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        r"""Sets the updater_id of this ListVariableGroupsRespPipelineVariableGroups.

        更新人ID

        :param updater_id: The updater_id of this ListVariableGroupsRespPipelineVariableGroups.
        :type updater_id: str
        """
        self._updater_id = updater_id

    @property
    def creator_name(self):
        r"""Gets the creator_name of this ListVariableGroupsRespPipelineVariableGroups.

        创建人名称

        :return: The creator_name of this ListVariableGroupsRespPipelineVariableGroups.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this ListVariableGroupsRespPipelineVariableGroups.

        创建人名称

        :param creator_name: The creator_name of this ListVariableGroupsRespPipelineVariableGroups.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def updater_name(self):
        r"""Gets the updater_name of this ListVariableGroupsRespPipelineVariableGroups.

        更新人名称

        :return: The updater_name of this ListVariableGroupsRespPipelineVariableGroups.
        :rtype: str
        """
        return self._updater_name

    @updater_name.setter
    def updater_name(self, updater_name):
        r"""Sets the updater_name of this ListVariableGroupsRespPipelineVariableGroups.

        更新人名称

        :param updater_name: The updater_name of this ListVariableGroupsRespPipelineVariableGroups.
        :type updater_name: str
        """
        self._updater_name = updater_name

    @property
    def create_time(self):
        r"""Gets the create_time of this ListVariableGroupsRespPipelineVariableGroups.

        创建时间

        :return: The create_time of this ListVariableGroupsRespPipelineVariableGroups.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListVariableGroupsRespPipelineVariableGroups.

        创建时间

        :param create_time: The create_time of this ListVariableGroupsRespPipelineVariableGroups.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ListVariableGroupsRespPipelineVariableGroups.

        更新时间

        :return: The update_time of this ListVariableGroupsRespPipelineVariableGroups.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ListVariableGroupsRespPipelineVariableGroups.

        更新时间

        :param update_time: The update_time of this ListVariableGroupsRespPipelineVariableGroups.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, ListVariableGroupsRespPipelineVariableGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
