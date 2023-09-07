# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchFlowByIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'apic_id': 'str',
        'apic_release_status': 'str',
        'apig_url': 'str',
        'connectors': 'list[object]',
        'connectors_latest': 'list[object]',
        'creatd_time': 'datetime',
        'description': 'str',
        'dev_status': 'str',
        'domain_id': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'extend_configs': 'object',
        'flow_source_type': 'str',
        'functions': 'object',
        'graph': 'object',
        'his_transfer_status': 'str',
        'icon': 'str',
        'id': 'str',
        'installed_connector': 'str',
        'is_valid': 'bool',
        'label': 'str',
        'name': 'str',
        'notice_status': 'str',
        'project_id': 'str',
        'schema_version': 'str',
        'status': 'str',
        'steps': 'list[dict(str, object)]',
        'tags': 'list[Tag]',
        'template_id': 'str',
        'template_name': 'str',
        'test_result': 'str',
        'type': 'str',
        'updated_time': 'datetime',
        'user_id': 'str',
        'version': 'str',
        'webhook': 'str'
    }

    attribute_map = {
        'apic_id': 'apic_id',
        'apic_release_status': 'apic_release_status',
        'apig_url': 'apig_url',
        'connectors': 'connectors',
        'connectors_latest': 'connectors_latest',
        'creatd_time': 'creatd_time',
        'description': 'description',
        'dev_status': 'dev_status',
        'domain_id': 'domain_id',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'extend_configs': 'extend_configs',
        'flow_source_type': 'flow_source_type',
        'functions': 'functions',
        'graph': 'graph',
        'his_transfer_status': 'his_transfer_status',
        'icon': 'icon',
        'id': 'id',
        'installed_connector': 'installed_connector',
        'is_valid': 'is_valid',
        'label': 'label',
        'name': 'name',
        'notice_status': 'notice_status',
        'project_id': 'project_id',
        'schema_version': 'schemaVersion',
        'status': 'status',
        'steps': 'steps',
        'tags': 'tags',
        'template_id': 'template_id',
        'template_name': 'template_name',
        'test_result': 'test_result',
        'type': 'type',
        'updated_time': 'updated_time',
        'user_id': 'user_id',
        'version': 'version',
        'webhook': 'webhook'
    }

    def __init__(self, apic_id=None, apic_release_status=None, apig_url=None, connectors=None, connectors_latest=None, creatd_time=None, description=None, dev_status=None, domain_id=None, enterprise_project_id=None, enterprise_project_name=None, extend_configs=None, flow_source_type=None, functions=None, graph=None, his_transfer_status=None, icon=None, id=None, installed_connector=None, is_valid=None, label=None, name=None, notice_status=None, project_id=None, schema_version=None, status=None, steps=None, tags=None, template_id=None, template_name=None, test_result=None, type=None, updated_time=None, user_id=None, version=None, webhook=None):
        """SearchFlowByIdResponse

        The model defined in huaweicloud sdk

        :param apic_id: 发布到apic的api id
        :type apic_id: str
        :param apic_release_status: 发布到apic的状态
        :type apic_release_status: str
        :param apig_url: api流注册到apig的url
        :type apig_url: str
        :param connectors: 连接器
        :type connectors: list[object]
        :param connectors_latest: 连接器最新版本
        :type connectors_latest: list[object]
        :param creatd_time: 创建时间
        :type creatd_time: datetime
        :param description: 流的描述信息
        :type description: str
        :param dev_status: 开发状态
        :type dev_status: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业项目名称
        :type enterprise_project_name: str
        :param extend_configs: 流/流模板扩展配置列表
        :type extend_configs: object
        :param flow_source_type: 流来源： inner: 公共流模板； custom： 我的流模板
        :type flow_source_type: str
        :param functions: 流/流模板函数列表
        :type functions: object
        :param graph: 流的编排数据(大josn)
        :type graph: object
        :param his_transfer_status: 
        :type his_transfer_status: str
        :param icon: logo base64编码
        :type icon: str
        :param id: ID
        :type id: str
        :param installed_connector: 已部署的connector id
        :type installed_connector: str
        :param is_valid: 
        :type is_valid: bool
        :param label: 
        :type label: str
        :param name: 流的名称
        :type name: str
        :param notice_status: 
        :type notice_status: str
        :param project_id: 用户项目ID
        :type project_id: str
        :param schema_version: schema版本
        :type schema_version: str
        :param status: 流的状态
        :type status: str
        :param steps: 流的编排数据（大josn）
        :type steps: list[dict(str, object)]
        :param tags: 标签列表
        :type tags: list[:class:`huaweicloudsdkmssi.v1.Tag`]
        :param template_id: 模板ID
        :type template_id: str
        :param template_name: 模板名称
        :type template_name: str
        :param test_result: 测试结果
        :type test_result: str
        :param type: 类型
        :type type: str
        :param updated_time: 修改时间
        :type updated_time: datetime
        :param user_id: 账号（所有者）
        :type user_id: str
        :param version: 流的版本号
        :type version: str
        :param webhook: webhook触发url的ID
        :type webhook: str
        """
        
        super(SearchFlowByIdResponse, self).__init__()

        self._apic_id = None
        self._apic_release_status = None
        self._apig_url = None
        self._connectors = None
        self._connectors_latest = None
        self._creatd_time = None
        self._description = None
        self._dev_status = None
        self._domain_id = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._extend_configs = None
        self._flow_source_type = None
        self._functions = None
        self._graph = None
        self._his_transfer_status = None
        self._icon = None
        self._id = None
        self._installed_connector = None
        self._is_valid = None
        self._label = None
        self._name = None
        self._notice_status = None
        self._project_id = None
        self._schema_version = None
        self._status = None
        self._steps = None
        self._tags = None
        self._template_id = None
        self._template_name = None
        self._test_result = None
        self._type = None
        self._updated_time = None
        self._user_id = None
        self._version = None
        self._webhook = None
        self.discriminator = None

        if apic_id is not None:
            self.apic_id = apic_id
        if apic_release_status is not None:
            self.apic_release_status = apic_release_status
        if apig_url is not None:
            self.apig_url = apig_url
        if connectors is not None:
            self.connectors = connectors
        if connectors_latest is not None:
            self.connectors_latest = connectors_latest
        if creatd_time is not None:
            self.creatd_time = creatd_time
        if description is not None:
            self.description = description
        if dev_status is not None:
            self.dev_status = dev_status
        if domain_id is not None:
            self.domain_id = domain_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if extend_configs is not None:
            self.extend_configs = extend_configs
        if flow_source_type is not None:
            self.flow_source_type = flow_source_type
        if functions is not None:
            self.functions = functions
        if graph is not None:
            self.graph = graph
        if his_transfer_status is not None:
            self.his_transfer_status = his_transfer_status
        if icon is not None:
            self.icon = icon
        if id is not None:
            self.id = id
        if installed_connector is not None:
            self.installed_connector = installed_connector
        if is_valid is not None:
            self.is_valid = is_valid
        if label is not None:
            self.label = label
        if name is not None:
            self.name = name
        if notice_status is not None:
            self.notice_status = notice_status
        if project_id is not None:
            self.project_id = project_id
        if schema_version is not None:
            self.schema_version = schema_version
        if status is not None:
            self.status = status
        if steps is not None:
            self.steps = steps
        if tags is not None:
            self.tags = tags
        if template_id is not None:
            self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if test_result is not None:
            self.test_result = test_result
        if type is not None:
            self.type = type
        if updated_time is not None:
            self.updated_time = updated_time
        if user_id is not None:
            self.user_id = user_id
        if version is not None:
            self.version = version
        if webhook is not None:
            self.webhook = webhook

    @property
    def apic_id(self):
        """Gets the apic_id of this SearchFlowByIdResponse.

        发布到apic的api id

        :return: The apic_id of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._apic_id

    @apic_id.setter
    def apic_id(self, apic_id):
        """Sets the apic_id of this SearchFlowByIdResponse.

        发布到apic的api id

        :param apic_id: The apic_id of this SearchFlowByIdResponse.
        :type apic_id: str
        """
        self._apic_id = apic_id

    @property
    def apic_release_status(self):
        """Gets the apic_release_status of this SearchFlowByIdResponse.

        发布到apic的状态

        :return: The apic_release_status of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._apic_release_status

    @apic_release_status.setter
    def apic_release_status(self, apic_release_status):
        """Sets the apic_release_status of this SearchFlowByIdResponse.

        发布到apic的状态

        :param apic_release_status: The apic_release_status of this SearchFlowByIdResponse.
        :type apic_release_status: str
        """
        self._apic_release_status = apic_release_status

    @property
    def apig_url(self):
        """Gets the apig_url of this SearchFlowByIdResponse.

        api流注册到apig的url

        :return: The apig_url of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._apig_url

    @apig_url.setter
    def apig_url(self, apig_url):
        """Sets the apig_url of this SearchFlowByIdResponse.

        api流注册到apig的url

        :param apig_url: The apig_url of this SearchFlowByIdResponse.
        :type apig_url: str
        """
        self._apig_url = apig_url

    @property
    def connectors(self):
        """Gets the connectors of this SearchFlowByIdResponse.

        连接器

        :return: The connectors of this SearchFlowByIdResponse.
        :rtype: list[object]
        """
        return self._connectors

    @connectors.setter
    def connectors(self, connectors):
        """Sets the connectors of this SearchFlowByIdResponse.

        连接器

        :param connectors: The connectors of this SearchFlowByIdResponse.
        :type connectors: list[object]
        """
        self._connectors = connectors

    @property
    def connectors_latest(self):
        """Gets the connectors_latest of this SearchFlowByIdResponse.

        连接器最新版本

        :return: The connectors_latest of this SearchFlowByIdResponse.
        :rtype: list[object]
        """
        return self._connectors_latest

    @connectors_latest.setter
    def connectors_latest(self, connectors_latest):
        """Sets the connectors_latest of this SearchFlowByIdResponse.

        连接器最新版本

        :param connectors_latest: The connectors_latest of this SearchFlowByIdResponse.
        :type connectors_latest: list[object]
        """
        self._connectors_latest = connectors_latest

    @property
    def creatd_time(self):
        """Gets the creatd_time of this SearchFlowByIdResponse.

        创建时间

        :return: The creatd_time of this SearchFlowByIdResponse.
        :rtype: datetime
        """
        return self._creatd_time

    @creatd_time.setter
    def creatd_time(self, creatd_time):
        """Sets the creatd_time of this SearchFlowByIdResponse.

        创建时间

        :param creatd_time: The creatd_time of this SearchFlowByIdResponse.
        :type creatd_time: datetime
        """
        self._creatd_time = creatd_time

    @property
    def description(self):
        """Gets the description of this SearchFlowByIdResponse.

        流的描述信息

        :return: The description of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SearchFlowByIdResponse.

        流的描述信息

        :param description: The description of this SearchFlowByIdResponse.
        :type description: str
        """
        self._description = description

    @property
    def dev_status(self):
        """Gets the dev_status of this SearchFlowByIdResponse.

        开发状态

        :return: The dev_status of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._dev_status

    @dev_status.setter
    def dev_status(self, dev_status):
        """Sets the dev_status of this SearchFlowByIdResponse.

        开发状态

        :param dev_status: The dev_status of this SearchFlowByIdResponse.
        :type dev_status: str
        """
        self._dev_status = dev_status

    @property
    def domain_id(self):
        """Gets the domain_id of this SearchFlowByIdResponse.

        租户ID

        :return: The domain_id of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this SearchFlowByIdResponse.

        租户ID

        :param domain_id: The domain_id of this SearchFlowByIdResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this SearchFlowByIdResponse.

        企业项目id

        :return: The enterprise_project_id of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this SearchFlowByIdResponse.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this SearchFlowByIdResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        """Gets the enterprise_project_name of this SearchFlowByIdResponse.

        企业项目名称

        :return: The enterprise_project_name of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        """Sets the enterprise_project_name of this SearchFlowByIdResponse.

        企业项目名称

        :param enterprise_project_name: The enterprise_project_name of this SearchFlowByIdResponse.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def extend_configs(self):
        """Gets the extend_configs of this SearchFlowByIdResponse.

        流/流模板扩展配置列表

        :return: The extend_configs of this SearchFlowByIdResponse.
        :rtype: object
        """
        return self._extend_configs

    @extend_configs.setter
    def extend_configs(self, extend_configs):
        """Sets the extend_configs of this SearchFlowByIdResponse.

        流/流模板扩展配置列表

        :param extend_configs: The extend_configs of this SearchFlowByIdResponse.
        :type extend_configs: object
        """
        self._extend_configs = extend_configs

    @property
    def flow_source_type(self):
        """Gets the flow_source_type of this SearchFlowByIdResponse.

        流来源： inner: 公共流模板； custom： 我的流模板

        :return: The flow_source_type of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._flow_source_type

    @flow_source_type.setter
    def flow_source_type(self, flow_source_type):
        """Sets the flow_source_type of this SearchFlowByIdResponse.

        流来源： inner: 公共流模板； custom： 我的流模板

        :param flow_source_type: The flow_source_type of this SearchFlowByIdResponse.
        :type flow_source_type: str
        """
        self._flow_source_type = flow_source_type

    @property
    def functions(self):
        """Gets the functions of this SearchFlowByIdResponse.

        流/流模板函数列表

        :return: The functions of this SearchFlowByIdResponse.
        :rtype: object
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """Sets the functions of this SearchFlowByIdResponse.

        流/流模板函数列表

        :param functions: The functions of this SearchFlowByIdResponse.
        :type functions: object
        """
        self._functions = functions

    @property
    def graph(self):
        """Gets the graph of this SearchFlowByIdResponse.

        流的编排数据(大josn)

        :return: The graph of this SearchFlowByIdResponse.
        :rtype: object
        """
        return self._graph

    @graph.setter
    def graph(self, graph):
        """Sets the graph of this SearchFlowByIdResponse.

        流的编排数据(大josn)

        :param graph: The graph of this SearchFlowByIdResponse.
        :type graph: object
        """
        self._graph = graph

    @property
    def his_transfer_status(self):
        """Gets the his_transfer_status of this SearchFlowByIdResponse.

        :return: The his_transfer_status of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._his_transfer_status

    @his_transfer_status.setter
    def his_transfer_status(self, his_transfer_status):
        """Sets the his_transfer_status of this SearchFlowByIdResponse.

        :param his_transfer_status: The his_transfer_status of this SearchFlowByIdResponse.
        :type his_transfer_status: str
        """
        self._his_transfer_status = his_transfer_status

    @property
    def icon(self):
        """Gets the icon of this SearchFlowByIdResponse.

        logo base64编码

        :return: The icon of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this SearchFlowByIdResponse.

        logo base64编码

        :param icon: The icon of this SearchFlowByIdResponse.
        :type icon: str
        """
        self._icon = icon

    @property
    def id(self):
        """Gets the id of this SearchFlowByIdResponse.

        ID

        :return: The id of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SearchFlowByIdResponse.

        ID

        :param id: The id of this SearchFlowByIdResponse.
        :type id: str
        """
        self._id = id

    @property
    def installed_connector(self):
        """Gets the installed_connector of this SearchFlowByIdResponse.

        已部署的connector id

        :return: The installed_connector of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._installed_connector

    @installed_connector.setter
    def installed_connector(self, installed_connector):
        """Sets the installed_connector of this SearchFlowByIdResponse.

        已部署的connector id

        :param installed_connector: The installed_connector of this SearchFlowByIdResponse.
        :type installed_connector: str
        """
        self._installed_connector = installed_connector

    @property
    def is_valid(self):
        """Gets the is_valid of this SearchFlowByIdResponse.

        :return: The is_valid of this SearchFlowByIdResponse.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this SearchFlowByIdResponse.

        :param is_valid: The is_valid of this SearchFlowByIdResponse.
        :type is_valid: bool
        """
        self._is_valid = is_valid

    @property
    def label(self):
        """Gets the label of this SearchFlowByIdResponse.

        :return: The label of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SearchFlowByIdResponse.

        :param label: The label of this SearchFlowByIdResponse.
        :type label: str
        """
        self._label = label

    @property
    def name(self):
        """Gets the name of this SearchFlowByIdResponse.

        流的名称

        :return: The name of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SearchFlowByIdResponse.

        流的名称

        :param name: The name of this SearchFlowByIdResponse.
        :type name: str
        """
        self._name = name

    @property
    def notice_status(self):
        """Gets the notice_status of this SearchFlowByIdResponse.

        :return: The notice_status of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._notice_status

    @notice_status.setter
    def notice_status(self, notice_status):
        """Sets the notice_status of this SearchFlowByIdResponse.

        :param notice_status: The notice_status of this SearchFlowByIdResponse.
        :type notice_status: str
        """
        self._notice_status = notice_status

    @property
    def project_id(self):
        """Gets the project_id of this SearchFlowByIdResponse.

        用户项目ID

        :return: The project_id of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SearchFlowByIdResponse.

        用户项目ID

        :param project_id: The project_id of this SearchFlowByIdResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def schema_version(self):
        """Gets the schema_version of this SearchFlowByIdResponse.

        schema版本

        :return: The schema_version of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """Sets the schema_version of this SearchFlowByIdResponse.

        schema版本

        :param schema_version: The schema_version of this SearchFlowByIdResponse.
        :type schema_version: str
        """
        self._schema_version = schema_version

    @property
    def status(self):
        """Gets the status of this SearchFlowByIdResponse.

        流的状态

        :return: The status of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SearchFlowByIdResponse.

        流的状态

        :param status: The status of this SearchFlowByIdResponse.
        :type status: str
        """
        self._status = status

    @property
    def steps(self):
        """Gets the steps of this SearchFlowByIdResponse.

        流的编排数据（大josn）

        :return: The steps of this SearchFlowByIdResponse.
        :rtype: list[dict(str, object)]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this SearchFlowByIdResponse.

        流的编排数据（大josn）

        :param steps: The steps of this SearchFlowByIdResponse.
        :type steps: list[dict(str, object)]
        """
        self._steps = steps

    @property
    def tags(self):
        """Gets the tags of this SearchFlowByIdResponse.

        标签列表

        :return: The tags of this SearchFlowByIdResponse.
        :rtype: list[:class:`huaweicloudsdkmssi.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SearchFlowByIdResponse.

        标签列表

        :param tags: The tags of this SearchFlowByIdResponse.
        :type tags: list[:class:`huaweicloudsdkmssi.v1.Tag`]
        """
        self._tags = tags

    @property
    def template_id(self):
        """Gets the template_id of this SearchFlowByIdResponse.

        模板ID

        :return: The template_id of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this SearchFlowByIdResponse.

        模板ID

        :param template_id: The template_id of this SearchFlowByIdResponse.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        """Gets the template_name of this SearchFlowByIdResponse.

        模板名称

        :return: The template_name of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this SearchFlowByIdResponse.

        模板名称

        :param template_name: The template_name of this SearchFlowByIdResponse.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def test_result(self):
        """Gets the test_result of this SearchFlowByIdResponse.

        测试结果

        :return: The test_result of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._test_result

    @test_result.setter
    def test_result(self, test_result):
        """Sets the test_result of this SearchFlowByIdResponse.

        测试结果

        :param test_result: The test_result of this SearchFlowByIdResponse.
        :type test_result: str
        """
        self._test_result = test_result

    @property
    def type(self):
        """Gets the type of this SearchFlowByIdResponse.

        类型

        :return: The type of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SearchFlowByIdResponse.

        类型

        :param type: The type of this SearchFlowByIdResponse.
        :type type: str
        """
        self._type = type

    @property
    def updated_time(self):
        """Gets the updated_time of this SearchFlowByIdResponse.

        修改时间

        :return: The updated_time of this SearchFlowByIdResponse.
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this SearchFlowByIdResponse.

        修改时间

        :param updated_time: The updated_time of this SearchFlowByIdResponse.
        :type updated_time: datetime
        """
        self._updated_time = updated_time

    @property
    def user_id(self):
        """Gets the user_id of this SearchFlowByIdResponse.

        账号（所有者）

        :return: The user_id of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SearchFlowByIdResponse.

        账号（所有者）

        :param user_id: The user_id of this SearchFlowByIdResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def version(self):
        """Gets the version of this SearchFlowByIdResponse.

        流的版本号

        :return: The version of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SearchFlowByIdResponse.

        流的版本号

        :param version: The version of this SearchFlowByIdResponse.
        :type version: str
        """
        self._version = version

    @property
    def webhook(self):
        """Gets the webhook of this SearchFlowByIdResponse.

        webhook触发url的ID

        :return: The webhook of this SearchFlowByIdResponse.
        :rtype: str
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this SearchFlowByIdResponse.

        webhook触发url的ID

        :param webhook: The webhook of this SearchFlowByIdResponse.
        :type webhook: str
        """
        self._webhook = webhook

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
        if not isinstance(other, SearchFlowByIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
