# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPipelineDetailResponse(SdkResponse):

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
        'description': 'str',
        'manifest_version': 'str',
        'region': 'str',
        'domain_id': 'str',
        'project_id': 'str',
        'component_id': 'str',
        'is_publish': 'bool',
        'creator_id': 'str',
        'creator_name': 'str',
        'updater_id': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'is_collect': 'bool',
        'sources': 'list[PipelineSource]',
        'variables': 'list[PipelineVariable]',
        'schedules': 'list[PipelineSchedule]',
        'triggers': 'list[PipelineTrigger]',
        'group_id': 'str',
        'definition': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'manifest_version': 'manifest_version',
        'region': 'region',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'component_id': 'component_id',
        'is_publish': 'is_publish',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'updater_id': 'updater_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'is_collect': 'is_collect',
        'sources': 'sources',
        'variables': 'variables',
        'schedules': 'schedules',
        'triggers': 'triggers',
        'group_id': 'group_id',
        'definition': 'definition'
    }

    def __init__(self, id=None, name=None, description=None, manifest_version=None, region=None, domain_id=None, project_id=None, component_id=None, is_publish=None, creator_id=None, creator_name=None, updater_id=None, create_time=None, update_time=None, is_collect=None, sources=None, variables=None, schedules=None, triggers=None, group_id=None, definition=None):
        """ShowPipelineDetailResponse

        The model defined in huaweicloud sdk

        :param id: 流水线ID
        :type id: str
        :param name: 流水线名称
        :type name: str
        :param description: 描述
        :type description: str
        :param manifest_version: 流水线版本
        :type manifest_version: str
        :param region: 局点
        :type region: str
        :param domain_id: 所属租户ID
        :type domain_id: str
        :param project_id: 所属项目ID
        :type project_id: str
        :param component_id: 所属微服务ID
        :type component_id: str
        :param is_publish: 是否为变更流水线
        :type is_publish: bool
        :param creator_id: 创建人ID
        :type creator_id: str
        :param creator_name: 创建人名称
        :type creator_name: str
        :param updater_id: 更新人ID
        :type updater_id: str
        :param create_time: 更新人名称
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        :param is_collect: 是否被当前用户收藏
        :type is_collect: bool
        :param sources: 流水线源
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSource`]
        :param variables: 流水线自定义参数
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineVariable`]
        :param schedules: 流水线定时任务设置
        :type schedules: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSchedule`]
        :param triggers: 流水线事件触发设置
        :type triggers: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTrigger`]
        :param group_id: 流水线所属分组ID
        :type group_id: str
        :param definition: 流水线定义
        :type definition: str
        """
        
        super(ShowPipelineDetailResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._manifest_version = None
        self._region = None
        self._domain_id = None
        self._project_id = None
        self._component_id = None
        self._is_publish = None
        self._creator_id = None
        self._creator_name = None
        self._updater_id = None
        self._create_time = None
        self._update_time = None
        self._is_collect = None
        self._sources = None
        self._variables = None
        self._schedules = None
        self._triggers = None
        self._group_id = None
        self._definition = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if manifest_version is not None:
            self.manifest_version = manifest_version
        if region is not None:
            self.region = region
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if component_id is not None:
            self.component_id = component_id
        if is_publish is not None:
            self.is_publish = is_publish
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if updater_id is not None:
            self.updater_id = updater_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if is_collect is not None:
            self.is_collect = is_collect
        if sources is not None:
            self.sources = sources
        if variables is not None:
            self.variables = variables
        if schedules is not None:
            self.schedules = schedules
        if triggers is not None:
            self.triggers = triggers
        if group_id is not None:
            self.group_id = group_id
        if definition is not None:
            self.definition = definition

    @property
    def id(self):
        """Gets the id of this ShowPipelineDetailResponse.

        流水线ID

        :return: The id of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowPipelineDetailResponse.

        流水线ID

        :param id: The id of this ShowPipelineDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowPipelineDetailResponse.

        流水线名称

        :return: The name of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowPipelineDetailResponse.

        流水线名称

        :param name: The name of this ShowPipelineDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowPipelineDetailResponse.

        描述

        :return: The description of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowPipelineDetailResponse.

        描述

        :param description: The description of this ShowPipelineDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def manifest_version(self):
        """Gets the manifest_version of this ShowPipelineDetailResponse.

        流水线版本

        :return: The manifest_version of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._manifest_version

    @manifest_version.setter
    def manifest_version(self, manifest_version):
        """Sets the manifest_version of this ShowPipelineDetailResponse.

        流水线版本

        :param manifest_version: The manifest_version of this ShowPipelineDetailResponse.
        :type manifest_version: str
        """
        self._manifest_version = manifest_version

    @property
    def region(self):
        """Gets the region of this ShowPipelineDetailResponse.

        局点

        :return: The region of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ShowPipelineDetailResponse.

        局点

        :param region: The region of this ShowPipelineDetailResponse.
        :type region: str
        """
        self._region = region

    @property
    def domain_id(self):
        """Gets the domain_id of this ShowPipelineDetailResponse.

        所属租户ID

        :return: The domain_id of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ShowPipelineDetailResponse.

        所属租户ID

        :param domain_id: The domain_id of this ShowPipelineDetailResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        """Gets the project_id of this ShowPipelineDetailResponse.

        所属项目ID

        :return: The project_id of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowPipelineDetailResponse.

        所属项目ID

        :param project_id: The project_id of this ShowPipelineDetailResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def component_id(self):
        """Gets the component_id of this ShowPipelineDetailResponse.

        所属微服务ID

        :return: The component_id of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this ShowPipelineDetailResponse.

        所属微服务ID

        :param component_id: The component_id of this ShowPipelineDetailResponse.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def is_publish(self):
        """Gets the is_publish of this ShowPipelineDetailResponse.

        是否为变更流水线

        :return: The is_publish of this ShowPipelineDetailResponse.
        :rtype: bool
        """
        return self._is_publish

    @is_publish.setter
    def is_publish(self, is_publish):
        """Sets the is_publish of this ShowPipelineDetailResponse.

        是否为变更流水线

        :param is_publish: The is_publish of this ShowPipelineDetailResponse.
        :type is_publish: bool
        """
        self._is_publish = is_publish

    @property
    def creator_id(self):
        """Gets the creator_id of this ShowPipelineDetailResponse.

        创建人ID

        :return: The creator_id of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this ShowPipelineDetailResponse.

        创建人ID

        :param creator_id: The creator_id of this ShowPipelineDetailResponse.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        """Gets the creator_name of this ShowPipelineDetailResponse.

        创建人名称

        :return: The creator_name of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this ShowPipelineDetailResponse.

        创建人名称

        :param creator_name: The creator_name of this ShowPipelineDetailResponse.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def updater_id(self):
        """Gets the updater_id of this ShowPipelineDetailResponse.

        更新人ID

        :return: The updater_id of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """Sets the updater_id of this ShowPipelineDetailResponse.

        更新人ID

        :param updater_id: The updater_id of this ShowPipelineDetailResponse.
        :type updater_id: str
        """
        self._updater_id = updater_id

    @property
    def create_time(self):
        """Gets the create_time of this ShowPipelineDetailResponse.

        更新人名称

        :return: The create_time of this ShowPipelineDetailResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowPipelineDetailResponse.

        更新人名称

        :param create_time: The create_time of this ShowPipelineDetailResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowPipelineDetailResponse.

        更新时间

        :return: The update_time of this ShowPipelineDetailResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowPipelineDetailResponse.

        更新时间

        :param update_time: The update_time of this ShowPipelineDetailResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def is_collect(self):
        """Gets the is_collect of this ShowPipelineDetailResponse.

        是否被当前用户收藏

        :return: The is_collect of this ShowPipelineDetailResponse.
        :rtype: bool
        """
        return self._is_collect

    @is_collect.setter
    def is_collect(self, is_collect):
        """Sets the is_collect of this ShowPipelineDetailResponse.

        是否被当前用户收藏

        :param is_collect: The is_collect of this ShowPipelineDetailResponse.
        :type is_collect: bool
        """
        self._is_collect = is_collect

    @property
    def sources(self):
        """Gets the sources of this ShowPipelineDetailResponse.

        流水线源

        :return: The sources of this ShowPipelineDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSource`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this ShowPipelineDetailResponse.

        流水线源

        :param sources: The sources of this ShowPipelineDetailResponse.
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSource`]
        """
        self._sources = sources

    @property
    def variables(self):
        """Gets the variables of this ShowPipelineDetailResponse.

        流水线自定义参数

        :return: The variables of this ShowPipelineDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineVariable`]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this ShowPipelineDetailResponse.

        流水线自定义参数

        :param variables: The variables of this ShowPipelineDetailResponse.
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineVariable`]
        """
        self._variables = variables

    @property
    def schedules(self):
        """Gets the schedules of this ShowPipelineDetailResponse.

        流水线定时任务设置

        :return: The schedules of this ShowPipelineDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSchedule`]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """Sets the schedules of this ShowPipelineDetailResponse.

        流水线定时任务设置

        :param schedules: The schedules of this ShowPipelineDetailResponse.
        :type schedules: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSchedule`]
        """
        self._schedules = schedules

    @property
    def triggers(self):
        """Gets the triggers of this ShowPipelineDetailResponse.

        流水线事件触发设置

        :return: The triggers of this ShowPipelineDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this ShowPipelineDetailResponse.

        流水线事件触发设置

        :param triggers: The triggers of this ShowPipelineDetailResponse.
        :type triggers: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTrigger`]
        """
        self._triggers = triggers

    @property
    def group_id(self):
        """Gets the group_id of this ShowPipelineDetailResponse.

        流水线所属分组ID

        :return: The group_id of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ShowPipelineDetailResponse.

        流水线所属分组ID

        :param group_id: The group_id of this ShowPipelineDetailResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def definition(self):
        """Gets the definition of this ShowPipelineDetailResponse.

        流水线定义

        :return: The definition of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this ShowPipelineDetailResponse.

        流水线定义

        :param definition: The definition of this ShowPipelineDetailResponse.
        :type definition: str
        """
        self._definition = definition

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
        if not isinstance(other, ShowPipelineDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
