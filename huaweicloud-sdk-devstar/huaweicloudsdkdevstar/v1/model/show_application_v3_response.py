# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowApplicationV3Response(SdkResponse):

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
        'region_id': 'str',
        'region_name': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'icon': 'str',
        'pipeline_creation_result': 'list[PipelineCreationResult]',
        'repository_creation_result': 'RepositoryCreationResult',
        'environment_creation_result': 'list[str]',
        'template_types': 'list[TemplateType]',
        'template_deployment': 'str',
        'deploy_type': 'str',
        'creator_name': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'region_id': 'region_id',
        'region_name': 'region_name',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'icon': 'icon',
        'pipeline_creation_result': 'pipeline_creation_result',
        'repository_creation_result': 'repository_creation_result',
        'environment_creation_result': 'environment_creation_result',
        'template_types': 'template_types',
        'template_deployment': 'template_deployment',
        'deploy_type': 'deploy_type',
        'creator_name': 'creator_name',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'version': 'version'
    }

    def __init__(self, id=None, name=None, description=None, region_id=None, region_name=None, project_id=None, project_name=None, icon=None, pipeline_creation_result=None, repository_creation_result=None, environment_creation_result=None, template_types=None, template_deployment=None, deploy_type=None, creator_name=None, created_at=None, updated_at=None, version=None):
        """ShowApplicationV3Response

        The model defined in huaweicloud sdk

        :param id: 应用id
        :type id: str
        :param name: 应用名称
        :type name: str
        :param description: 应用描述
        :type description: str
        :param region_id: 区域id
        :type region_id: str
        :param region_name: 区域名称
        :type region_name: str
        :param project_id: 所属项目id
        :type project_id: str
        :param project_name: 项目名称
        :type project_name: str
        :param icon: 应用图标
        :type icon: str
        :param pipeline_creation_result: 流水线列表
        :type pipeline_creation_result: list[:class:`huaweicloudsdkdevstar.v1.PipelineCreationResult`]
        :param repository_creation_result: 
        :type repository_creation_result: :class:`huaweicloudsdkdevstar.v1.RepositoryCreationResult`
        :param environment_creation_result: 环境信息
        :type environment_creation_result: list[str]
        :param template_types: 模板类型
        :type template_types: list[:class:`huaweicloudsdkdevstar.v1.TemplateType`]
        :param template_deployment: 模板部署信息
        :type template_deployment: str
        :param deploy_type: 部署类型, function:函数部署,cci:cci容器部署,ServiceStage(Jar):ServiceStage jar包部署,ServiceStage(Docker):ServiceStage Docker容器部署,none不支持部署
        :type deploy_type: str
        :param creator_name: 创建者名称
        :type creator_name: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param version: 应用版本号
        :type version: str
        """
        
        super(ShowApplicationV3Response, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._region_id = None
        self._region_name = None
        self._project_id = None
        self._project_name = None
        self._icon = None
        self._pipeline_creation_result = None
        self._repository_creation_result = None
        self._environment_creation_result = None
        self._template_types = None
        self._template_deployment = None
        self._deploy_type = None
        self._creator_name = None
        self._created_at = None
        self._updated_at = None
        self._version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.region_id = region_id
        self.region_name = region_name
        self.project_id = project_id
        self.project_name = project_name
        if icon is not None:
            self.icon = icon
        if pipeline_creation_result is not None:
            self.pipeline_creation_result = pipeline_creation_result
        if repository_creation_result is not None:
            self.repository_creation_result = repository_creation_result
        if environment_creation_result is not None:
            self.environment_creation_result = environment_creation_result
        if template_types is not None:
            self.template_types = template_types
        if template_deployment is not None:
            self.template_deployment = template_deployment
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if creator_name is not None:
            self.creator_name = creator_name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if version is not None:
            self.version = version

    @property
    def id(self):
        """Gets the id of this ShowApplicationV3Response.

        应用id

        :return: The id of this ShowApplicationV3Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowApplicationV3Response.

        应用id

        :param id: The id of this ShowApplicationV3Response.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowApplicationV3Response.

        应用名称

        :return: The name of this ShowApplicationV3Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowApplicationV3Response.

        应用名称

        :param name: The name of this ShowApplicationV3Response.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowApplicationV3Response.

        应用描述

        :return: The description of this ShowApplicationV3Response.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowApplicationV3Response.

        应用描述

        :param description: The description of this ShowApplicationV3Response.
        :type description: str
        """
        self._description = description

    @property
    def region_id(self):
        """Gets the region_id of this ShowApplicationV3Response.

        区域id

        :return: The region_id of this ShowApplicationV3Response.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ShowApplicationV3Response.

        区域id

        :param region_id: The region_id of this ShowApplicationV3Response.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def region_name(self):
        """Gets the region_name of this ShowApplicationV3Response.

        区域名称

        :return: The region_name of this ShowApplicationV3Response.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this ShowApplicationV3Response.

        区域名称

        :param region_name: The region_name of this ShowApplicationV3Response.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def project_id(self):
        """Gets the project_id of this ShowApplicationV3Response.

        所属项目id

        :return: The project_id of this ShowApplicationV3Response.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowApplicationV3Response.

        所属项目id

        :param project_id: The project_id of this ShowApplicationV3Response.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this ShowApplicationV3Response.

        项目名称

        :return: The project_name of this ShowApplicationV3Response.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ShowApplicationV3Response.

        项目名称

        :param project_name: The project_name of this ShowApplicationV3Response.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def icon(self):
        """Gets the icon of this ShowApplicationV3Response.

        应用图标

        :return: The icon of this ShowApplicationV3Response.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this ShowApplicationV3Response.

        应用图标

        :param icon: The icon of this ShowApplicationV3Response.
        :type icon: str
        """
        self._icon = icon

    @property
    def pipeline_creation_result(self):
        """Gets the pipeline_creation_result of this ShowApplicationV3Response.

        流水线列表

        :return: The pipeline_creation_result of this ShowApplicationV3Response.
        :rtype: list[:class:`huaweicloudsdkdevstar.v1.PipelineCreationResult`]
        """
        return self._pipeline_creation_result

    @pipeline_creation_result.setter
    def pipeline_creation_result(self, pipeline_creation_result):
        """Sets the pipeline_creation_result of this ShowApplicationV3Response.

        流水线列表

        :param pipeline_creation_result: The pipeline_creation_result of this ShowApplicationV3Response.
        :type pipeline_creation_result: list[:class:`huaweicloudsdkdevstar.v1.PipelineCreationResult`]
        """
        self._pipeline_creation_result = pipeline_creation_result

    @property
    def repository_creation_result(self):
        """Gets the repository_creation_result of this ShowApplicationV3Response.

        :return: The repository_creation_result of this ShowApplicationV3Response.
        :rtype: :class:`huaweicloudsdkdevstar.v1.RepositoryCreationResult`
        """
        return self._repository_creation_result

    @repository_creation_result.setter
    def repository_creation_result(self, repository_creation_result):
        """Sets the repository_creation_result of this ShowApplicationV3Response.

        :param repository_creation_result: The repository_creation_result of this ShowApplicationV3Response.
        :type repository_creation_result: :class:`huaweicloudsdkdevstar.v1.RepositoryCreationResult`
        """
        self._repository_creation_result = repository_creation_result

    @property
    def environment_creation_result(self):
        """Gets the environment_creation_result of this ShowApplicationV3Response.

        环境信息

        :return: The environment_creation_result of this ShowApplicationV3Response.
        :rtype: list[str]
        """
        return self._environment_creation_result

    @environment_creation_result.setter
    def environment_creation_result(self, environment_creation_result):
        """Sets the environment_creation_result of this ShowApplicationV3Response.

        环境信息

        :param environment_creation_result: The environment_creation_result of this ShowApplicationV3Response.
        :type environment_creation_result: list[str]
        """
        self._environment_creation_result = environment_creation_result

    @property
    def template_types(self):
        """Gets the template_types of this ShowApplicationV3Response.

        模板类型

        :return: The template_types of this ShowApplicationV3Response.
        :rtype: list[:class:`huaweicloudsdkdevstar.v1.TemplateType`]
        """
        return self._template_types

    @template_types.setter
    def template_types(self, template_types):
        """Sets the template_types of this ShowApplicationV3Response.

        模板类型

        :param template_types: The template_types of this ShowApplicationV3Response.
        :type template_types: list[:class:`huaweicloudsdkdevstar.v1.TemplateType`]
        """
        self._template_types = template_types

    @property
    def template_deployment(self):
        """Gets the template_deployment of this ShowApplicationV3Response.

        模板部署信息

        :return: The template_deployment of this ShowApplicationV3Response.
        :rtype: str
        """
        return self._template_deployment

    @template_deployment.setter
    def template_deployment(self, template_deployment):
        """Sets the template_deployment of this ShowApplicationV3Response.

        模板部署信息

        :param template_deployment: The template_deployment of this ShowApplicationV3Response.
        :type template_deployment: str
        """
        self._template_deployment = template_deployment

    @property
    def deploy_type(self):
        """Gets the deploy_type of this ShowApplicationV3Response.

        部署类型, function:函数部署,cci:cci容器部署,ServiceStage(Jar):ServiceStage jar包部署,ServiceStage(Docker):ServiceStage Docker容器部署,none不支持部署

        :return: The deploy_type of this ShowApplicationV3Response.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        """Sets the deploy_type of this ShowApplicationV3Response.

        部署类型, function:函数部署,cci:cci容器部署,ServiceStage(Jar):ServiceStage jar包部署,ServiceStage(Docker):ServiceStage Docker容器部署,none不支持部署

        :param deploy_type: The deploy_type of this ShowApplicationV3Response.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def creator_name(self):
        """Gets the creator_name of this ShowApplicationV3Response.

        创建者名称

        :return: The creator_name of this ShowApplicationV3Response.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this ShowApplicationV3Response.

        创建者名称

        :param creator_name: The creator_name of this ShowApplicationV3Response.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def created_at(self):
        """Gets the created_at of this ShowApplicationV3Response.

        创建时间

        :return: The created_at of this ShowApplicationV3Response.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowApplicationV3Response.

        创建时间

        :param created_at: The created_at of this ShowApplicationV3Response.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ShowApplicationV3Response.

        更新时间

        :return: The updated_at of this ShowApplicationV3Response.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ShowApplicationV3Response.

        更新时间

        :param updated_at: The updated_at of this ShowApplicationV3Response.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def version(self):
        """Gets the version of this ShowApplicationV3Response.

        应用版本号

        :return: The version of this ShowApplicationV3Response.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowApplicationV3Response.

        应用版本号

        :param version: The version of this ShowApplicationV3Response.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ShowApplicationV3Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
