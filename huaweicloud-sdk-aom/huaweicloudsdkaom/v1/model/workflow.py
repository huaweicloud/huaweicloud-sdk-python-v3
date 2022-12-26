# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Workflow:

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
        'type': 'str',
        'description': 'str',
        'tags': 'dict(str, str)',
        'create_time': 'int',
        'create_by': 'str',
        'update_time': 'int',
        'update_by': 'str',
        'template_name': 'str',
        'template_id': 'str',
        'input': 'dict(str, object)',
        'last_execution_id': 'str',
        'status': 'str',
        'citation_urns': 'list[str]',
        'last_execution_end_time': 'int',
        'last_execution_start_time': 'int',
        'quote': 'list[str]',
        'job_name': 'str',
        'job_id': 'str',
        'service_scenario': 'str',
        'service_name': 'str',
        'task_type': 'str',
        'project_id': 'str',
        'workflow_id': 'str',
        'task_status': 'str',
        'nodes': 'list[Node]',
        'edit_time': 'int',
        'execution_action_rules': 'list[str]',
        'execution_permission': 'list[str]',
        'global_parameters': 'list[Parameter]',
        'is_delete': 'bool',
        'steps': 'list[Step]',
        'output': 'str',
        'trigger_id': 'str',
        'trigger_status': 'str',
        'approve_id': 'str',
        'template_i18n': 'dict(str, dict(str, object))',
        'enterprise_project_id': 'str',
        'last_execute_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'tags': 'tags',
        'create_time': 'create_time',
        'create_by': 'create_by',
        'update_time': 'update_time',
        'update_by': 'update_by',
        'template_name': 'template_name',
        'template_id': 'template_id',
        'input': 'input',
        'last_execution_id': 'last_execution_id',
        'status': 'status',
        'citation_urns': 'citation_urns',
        'last_execution_end_time': 'last_execution_end_time',
        'last_execution_start_time': 'last_execution_start_time',
        'quote': 'quote',
        'job_name': 'job_name',
        'job_id': 'job_id',
        'service_scenario': 'service_scenario',
        'service_name': 'service_name',
        'task_type': 'task_type',
        'project_id': 'project_id',
        'workflow_id': 'workflow_id',
        'task_status': 'task_status',
        'nodes': 'nodes',
        'edit_time': 'edit_time',
        'execution_action_rules': 'execution_action_rules',
        'execution_permission': 'execution_permission',
        'global_parameters': 'global_parameters',
        'is_delete': 'is_delete',
        'steps': 'steps',
        'output': 'output',
        'trigger_id': 'trigger_id',
        'trigger_status': 'trigger_status',
        'approve_id': 'approve_id',
        'template_i18n': 'template_i18n',
        'enterprise_project_id': 'enterprise_project_id',
        'last_execute_by': 'last_execute_by'
    }

    def __init__(self, id=None, name=None, type=None, description=None, tags=None, create_time=None, create_by=None, update_time=None, update_by=None, template_name=None, template_id=None, input=None, last_execution_id=None, status=None, citation_urns=None, last_execution_end_time=None, last_execution_start_time=None, quote=None, job_name=None, job_id=None, service_scenario=None, service_name=None, task_type=None, project_id=None, workflow_id=None, task_status=None, nodes=None, edit_time=None, execution_action_rules=None, execution_permission=None, global_parameters=None, is_delete=None, steps=None, output=None, trigger_id=None, trigger_status=None, approve_id=None, template_i18n=None, enterprise_project_id=None, last_execute_by=None):
        """Workflow

        The model defined in huaweicloud sdk

        :param id: 工作流id，唯一标识，根据project_id和workflow_name生成。
        :type id: str
        :param name: 工作流名称，满足：[^\\\\&gt;+&lt;^;#\&quot;\\s&amp;?%&#x3D;&#39;$￥@*/\\]\\[【】{}|:,.，。：‘’“、—！!~&#x60;·？《》…]{1,64}。
        :type name: str
        :param type: 工作流类型，可以为cron、manual
        :type type: str
        :param description: 工作流描述信息。
        :type description: str
        :param tags: 标签键和值列表，标签键值对数量范围是0至20。
        :type tags: dict(str, str)
        :param create_time: 工作流创建时间，为utc时间毫秒数。
        :type create_time: int
        :param create_by: 工作流创人，从接口调用传入的token中获取。
        :type create_by: str
        :param update_time: 工作流更新时间，为utc时间毫秒数。
        :type update_time: int
        :param update_by: 工作流更新人，从接口调用传入的token中获取。
        :type update_by: str
        :param template_name: 模板名称，需要满足：[^\\\\&gt;+&lt;^;#\&quot;\\s&amp;?%&#x3D;&#39;$￥@*/\\]\\[【】{}|:,.，。：‘’“、—！!~&#x60;·？《》…]{1,64}。
        :type template_name: str
        :param template_id: 模板id
        :type template_id: str
        :param input: 任务执行时需要的参数列表。
        :type input: dict(str, object)
        :param last_execution_id: 最近一次执行id，也是工作流id
        :type last_execution_id: str
        :param status: 任务状态，包含success，fail,executing
        :type status: str
        :param citation_urns: 引用链接,workflow引用的工作链接
        :type citation_urns: list[str]
        :param last_execution_end_time: 最近一次执行结束时间，为utc时间毫秒数
        :type last_execution_end_time: int
        :param last_execution_start_time: 最近一次执行开始时间，为utc时间毫秒数
        :type last_execution_start_time: int
        :param quote: 引用，参数引用
        :type quote: list[str]
        :param job_name: 作业名称
        :type job_name: str
        :param job_id: 作业id
        :type job_id: str
        :param service_scenario: 服务场景分类
        :type service_scenario: str
        :param service_name: 服务名称
        :type service_name: str
        :param task_type: 任务类型
        :type task_type: str
        :param project_id: functiongraph返回的PROJECT_ID
        :type project_id: str
        :param workflow_id: functiongraph返回的WORKFLOW_ID
        :type workflow_id: str
        :param task_status: 任务状态
        :type task_status: str
        :param nodes: 任务节点
        :type nodes: list[:class:`huaweicloudsdkaom.v1.Node`]
        :param edit_time: 编辑时间
        :type edit_time: int
        :param execution_action_rules: 执行动作细粒度权限
        :type execution_action_rules: list[str]
        :param execution_permission: 云服务权限
        :type execution_permission: list[str]
        :param global_parameters: 全局参数
        :type global_parameters: list[:class:`huaweicloudsdkaom.v1.Parameter`]
        :param is_delete: 逻辑删除
        :type is_delete: bool
        :param steps: 任务步骤
        :type steps: list[:class:`huaweicloudsdkaom.v1.Step`]
        :param output: 任务输出
        :type output: str
        :param trigger_id: 触发器id
        :type trigger_id: str
        :param trigger_status: 触发器状态
        :type trigger_status: str
        :param approve_id: 审批id
        :type approve_id: str
        :param template_i18n: 任务国际化字段，包含中英文描述
        :type template_i18n: dict(str, dict(str, object))
        :param enterprise_project_id: 任务所属的企业项目
        :type enterprise_project_id: str
        :param last_execute_by: 任务最后一次执行人
        :type last_execute_by: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._description = None
        self._tags = None
        self._create_time = None
        self._create_by = None
        self._update_time = None
        self._update_by = None
        self._template_name = None
        self._template_id = None
        self._input = None
        self._last_execution_id = None
        self._status = None
        self._citation_urns = None
        self._last_execution_end_time = None
        self._last_execution_start_time = None
        self._quote = None
        self._job_name = None
        self._job_id = None
        self._service_scenario = None
        self._service_name = None
        self._task_type = None
        self._project_id = None
        self._workflow_id = None
        self._task_status = None
        self._nodes = None
        self._edit_time = None
        self._execution_action_rules = None
        self._execution_permission = None
        self._global_parameters = None
        self._is_delete = None
        self._steps = None
        self._output = None
        self._trigger_id = None
        self._trigger_status = None
        self._approve_id = None
        self._template_i18n = None
        self._enterprise_project_id = None
        self._last_execute_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if create_time is not None:
            self.create_time = create_time
        if create_by is not None:
            self.create_by = create_by
        if update_time is not None:
            self.update_time = update_time
        if update_by is not None:
            self.update_by = update_by
        if template_name is not None:
            self.template_name = template_name
        if template_id is not None:
            self.template_id = template_id
        if input is not None:
            self.input = input
        if last_execution_id is not None:
            self.last_execution_id = last_execution_id
        if status is not None:
            self.status = status
        if citation_urns is not None:
            self.citation_urns = citation_urns
        if last_execution_end_time is not None:
            self.last_execution_end_time = last_execution_end_time
        if last_execution_start_time is not None:
            self.last_execution_start_time = last_execution_start_time
        if quote is not None:
            self.quote = quote
        if job_name is not None:
            self.job_name = job_name
        if job_id is not None:
            self.job_id = job_id
        if service_scenario is not None:
            self.service_scenario = service_scenario
        if service_name is not None:
            self.service_name = service_name
        if task_type is not None:
            self.task_type = task_type
        if project_id is not None:
            self.project_id = project_id
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if task_status is not None:
            self.task_status = task_status
        if nodes is not None:
            self.nodes = nodes
        if edit_time is not None:
            self.edit_time = edit_time
        if execution_action_rules is not None:
            self.execution_action_rules = execution_action_rules
        if execution_permission is not None:
            self.execution_permission = execution_permission
        if global_parameters is not None:
            self.global_parameters = global_parameters
        if is_delete is not None:
            self.is_delete = is_delete
        if steps is not None:
            self.steps = steps
        if output is not None:
            self.output = output
        if trigger_id is not None:
            self.trigger_id = trigger_id
        if trigger_status is not None:
            self.trigger_status = trigger_status
        if approve_id is not None:
            self.approve_id = approve_id
        if template_i18n is not None:
            self.template_i18n = template_i18n
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if last_execute_by is not None:
            self.last_execute_by = last_execute_by

    @property
    def id(self):
        """Gets the id of this Workflow.

        工作流id，唯一标识，根据project_id和workflow_name生成。

        :return: The id of this Workflow.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Workflow.

        工作流id，唯一标识，根据project_id和workflow_name生成。

        :param id: The id of this Workflow.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Workflow.

        工作流名称，满足：[^\\\\>+<^;#\"\\s&?%='$￥@*/\\]\\[【】{}|:,.，。：‘’“、—！!~`·？《》…]{1,64}。

        :return: The name of this Workflow.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Workflow.

        工作流名称，满足：[^\\\\>+<^;#\"\\s&?%='$￥@*/\\]\\[【】{}|:,.，。：‘’“、—！!~`·？《》…]{1,64}。

        :param name: The name of this Workflow.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this Workflow.

        工作流类型，可以为cron、manual

        :return: The type of this Workflow.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Workflow.

        工作流类型，可以为cron、manual

        :param type: The type of this Workflow.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this Workflow.

        工作流描述信息。

        :return: The description of this Workflow.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Workflow.

        工作流描述信息。

        :param description: The description of this Workflow.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        """Gets the tags of this Workflow.

        标签键和值列表，标签键值对数量范围是0至20。

        :return: The tags of this Workflow.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Workflow.

        标签键和值列表，标签键值对数量范围是0至20。

        :param tags: The tags of this Workflow.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def create_time(self):
        """Gets the create_time of this Workflow.

        工作流创建时间，为utc时间毫秒数。

        :return: The create_time of this Workflow.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Workflow.

        工作流创建时间，为utc时间毫秒数。

        :param create_time: The create_time of this Workflow.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_by(self):
        """Gets the create_by of this Workflow.

        工作流创人，从接口调用传入的token中获取。

        :return: The create_by of this Workflow.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this Workflow.

        工作流创人，从接口调用传入的token中获取。

        :param create_by: The create_by of this Workflow.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_time(self):
        """Gets the update_time of this Workflow.

        工作流更新时间，为utc时间毫秒数。

        :return: The update_time of this Workflow.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Workflow.

        工作流更新时间，为utc时间毫秒数。

        :param update_time: The update_time of this Workflow.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def update_by(self):
        """Gets the update_by of this Workflow.

        工作流更新人，从接口调用传入的token中获取。

        :return: The update_by of this Workflow.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this Workflow.

        工作流更新人，从接口调用传入的token中获取。

        :param update_by: The update_by of this Workflow.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def template_name(self):
        """Gets the template_name of this Workflow.

        模板名称，需要满足：[^\\\\>+<^;#\"\\s&?%='$￥@*/\\]\\[【】{}|:,.，。：‘’“、—！!~`·？《》…]{1,64}。

        :return: The template_name of this Workflow.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this Workflow.

        模板名称，需要满足：[^\\\\>+<^;#\"\\s&?%='$￥@*/\\]\\[【】{}|:,.，。：‘’“、—！!~`·？《》…]{1,64}。

        :param template_name: The template_name of this Workflow.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_id(self):
        """Gets the template_id of this Workflow.

        模板id

        :return: The template_id of this Workflow.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this Workflow.

        模板id

        :param template_id: The template_id of this Workflow.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def input(self):
        """Gets the input of this Workflow.

        任务执行时需要的参数列表。

        :return: The input of this Workflow.
        :rtype: dict(str, object)
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this Workflow.

        任务执行时需要的参数列表。

        :param input: The input of this Workflow.
        :type input: dict(str, object)
        """
        self._input = input

    @property
    def last_execution_id(self):
        """Gets the last_execution_id of this Workflow.

        最近一次执行id，也是工作流id

        :return: The last_execution_id of this Workflow.
        :rtype: str
        """
        return self._last_execution_id

    @last_execution_id.setter
    def last_execution_id(self, last_execution_id):
        """Sets the last_execution_id of this Workflow.

        最近一次执行id，也是工作流id

        :param last_execution_id: The last_execution_id of this Workflow.
        :type last_execution_id: str
        """
        self._last_execution_id = last_execution_id

    @property
    def status(self):
        """Gets the status of this Workflow.

        任务状态，包含success，fail,executing

        :return: The status of this Workflow.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Workflow.

        任务状态，包含success，fail,executing

        :param status: The status of this Workflow.
        :type status: str
        """
        self._status = status

    @property
    def citation_urns(self):
        """Gets the citation_urns of this Workflow.

        引用链接,workflow引用的工作链接

        :return: The citation_urns of this Workflow.
        :rtype: list[str]
        """
        return self._citation_urns

    @citation_urns.setter
    def citation_urns(self, citation_urns):
        """Sets the citation_urns of this Workflow.

        引用链接,workflow引用的工作链接

        :param citation_urns: The citation_urns of this Workflow.
        :type citation_urns: list[str]
        """
        self._citation_urns = citation_urns

    @property
    def last_execution_end_time(self):
        """Gets the last_execution_end_time of this Workflow.

        最近一次执行结束时间，为utc时间毫秒数

        :return: The last_execution_end_time of this Workflow.
        :rtype: int
        """
        return self._last_execution_end_time

    @last_execution_end_time.setter
    def last_execution_end_time(self, last_execution_end_time):
        """Sets the last_execution_end_time of this Workflow.

        最近一次执行结束时间，为utc时间毫秒数

        :param last_execution_end_time: The last_execution_end_time of this Workflow.
        :type last_execution_end_time: int
        """
        self._last_execution_end_time = last_execution_end_time

    @property
    def last_execution_start_time(self):
        """Gets the last_execution_start_time of this Workflow.

        最近一次执行开始时间，为utc时间毫秒数

        :return: The last_execution_start_time of this Workflow.
        :rtype: int
        """
        return self._last_execution_start_time

    @last_execution_start_time.setter
    def last_execution_start_time(self, last_execution_start_time):
        """Sets the last_execution_start_time of this Workflow.

        最近一次执行开始时间，为utc时间毫秒数

        :param last_execution_start_time: The last_execution_start_time of this Workflow.
        :type last_execution_start_time: int
        """
        self._last_execution_start_time = last_execution_start_time

    @property
    def quote(self):
        """Gets the quote of this Workflow.

        引用，参数引用

        :return: The quote of this Workflow.
        :rtype: list[str]
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this Workflow.

        引用，参数引用

        :param quote: The quote of this Workflow.
        :type quote: list[str]
        """
        self._quote = quote

    @property
    def job_name(self):
        """Gets the job_name of this Workflow.

        作业名称

        :return: The job_name of this Workflow.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this Workflow.

        作业名称

        :param job_name: The job_name of this Workflow.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_id(self):
        """Gets the job_id of this Workflow.

        作业id

        :return: The job_id of this Workflow.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Workflow.

        作业id

        :param job_id: The job_id of this Workflow.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def service_scenario(self):
        """Gets the service_scenario of this Workflow.

        服务场景分类

        :return: The service_scenario of this Workflow.
        :rtype: str
        """
        return self._service_scenario

    @service_scenario.setter
    def service_scenario(self, service_scenario):
        """Sets the service_scenario of this Workflow.

        服务场景分类

        :param service_scenario: The service_scenario of this Workflow.
        :type service_scenario: str
        """
        self._service_scenario = service_scenario

    @property
    def service_name(self):
        """Gets the service_name of this Workflow.

        服务名称

        :return: The service_name of this Workflow.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this Workflow.

        服务名称

        :param service_name: The service_name of this Workflow.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def task_type(self):
        """Gets the task_type of this Workflow.

        任务类型

        :return: The task_type of this Workflow.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this Workflow.

        任务类型

        :param task_type: The task_type of this Workflow.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def project_id(self):
        """Gets the project_id of this Workflow.

        functiongraph返回的PROJECT_ID

        :return: The project_id of this Workflow.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Workflow.

        functiongraph返回的PROJECT_ID

        :param project_id: The project_id of this Workflow.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workflow_id(self):
        """Gets the workflow_id of this Workflow.

        functiongraph返回的WORKFLOW_ID

        :return: The workflow_id of this Workflow.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this Workflow.

        functiongraph返回的WORKFLOW_ID

        :param workflow_id: The workflow_id of this Workflow.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def task_status(self):
        """Gets the task_status of this Workflow.

        任务状态

        :return: The task_status of this Workflow.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this Workflow.

        任务状态

        :param task_status: The task_status of this Workflow.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def nodes(self):
        """Gets the nodes of this Workflow.

        任务节点

        :return: The nodes of this Workflow.
        :rtype: list[:class:`huaweicloudsdkaom.v1.Node`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this Workflow.

        任务节点

        :param nodes: The nodes of this Workflow.
        :type nodes: list[:class:`huaweicloudsdkaom.v1.Node`]
        """
        self._nodes = nodes

    @property
    def edit_time(self):
        """Gets the edit_time of this Workflow.

        编辑时间

        :return: The edit_time of this Workflow.
        :rtype: int
        """
        return self._edit_time

    @edit_time.setter
    def edit_time(self, edit_time):
        """Sets the edit_time of this Workflow.

        编辑时间

        :param edit_time: The edit_time of this Workflow.
        :type edit_time: int
        """
        self._edit_time = edit_time

    @property
    def execution_action_rules(self):
        """Gets the execution_action_rules of this Workflow.

        执行动作细粒度权限

        :return: The execution_action_rules of this Workflow.
        :rtype: list[str]
        """
        return self._execution_action_rules

    @execution_action_rules.setter
    def execution_action_rules(self, execution_action_rules):
        """Sets the execution_action_rules of this Workflow.

        执行动作细粒度权限

        :param execution_action_rules: The execution_action_rules of this Workflow.
        :type execution_action_rules: list[str]
        """
        self._execution_action_rules = execution_action_rules

    @property
    def execution_permission(self):
        """Gets the execution_permission of this Workflow.

        云服务权限

        :return: The execution_permission of this Workflow.
        :rtype: list[str]
        """
        return self._execution_permission

    @execution_permission.setter
    def execution_permission(self, execution_permission):
        """Sets the execution_permission of this Workflow.

        云服务权限

        :param execution_permission: The execution_permission of this Workflow.
        :type execution_permission: list[str]
        """
        self._execution_permission = execution_permission

    @property
    def global_parameters(self):
        """Gets the global_parameters of this Workflow.

        全局参数

        :return: The global_parameters of this Workflow.
        :rtype: list[:class:`huaweicloudsdkaom.v1.Parameter`]
        """
        return self._global_parameters

    @global_parameters.setter
    def global_parameters(self, global_parameters):
        """Sets the global_parameters of this Workflow.

        全局参数

        :param global_parameters: The global_parameters of this Workflow.
        :type global_parameters: list[:class:`huaweicloudsdkaom.v1.Parameter`]
        """
        self._global_parameters = global_parameters

    @property
    def is_delete(self):
        """Gets the is_delete of this Workflow.

        逻辑删除

        :return: The is_delete of this Workflow.
        :rtype: bool
        """
        return self._is_delete

    @is_delete.setter
    def is_delete(self, is_delete):
        """Sets the is_delete of this Workflow.

        逻辑删除

        :param is_delete: The is_delete of this Workflow.
        :type is_delete: bool
        """
        self._is_delete = is_delete

    @property
    def steps(self):
        """Gets the steps of this Workflow.

        任务步骤

        :return: The steps of this Workflow.
        :rtype: list[:class:`huaweicloudsdkaom.v1.Step`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this Workflow.

        任务步骤

        :param steps: The steps of this Workflow.
        :type steps: list[:class:`huaweicloudsdkaom.v1.Step`]
        """
        self._steps = steps

    @property
    def output(self):
        """Gets the output of this Workflow.

        任务输出

        :return: The output of this Workflow.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this Workflow.

        任务输出

        :param output: The output of this Workflow.
        :type output: str
        """
        self._output = output

    @property
    def trigger_id(self):
        """Gets the trigger_id of this Workflow.

        触发器id

        :return: The trigger_id of this Workflow.
        :rtype: str
        """
        return self._trigger_id

    @trigger_id.setter
    def trigger_id(self, trigger_id):
        """Sets the trigger_id of this Workflow.

        触发器id

        :param trigger_id: The trigger_id of this Workflow.
        :type trigger_id: str
        """
        self._trigger_id = trigger_id

    @property
    def trigger_status(self):
        """Gets the trigger_status of this Workflow.

        触发器状态

        :return: The trigger_status of this Workflow.
        :rtype: str
        """
        return self._trigger_status

    @trigger_status.setter
    def trigger_status(self, trigger_status):
        """Sets the trigger_status of this Workflow.

        触发器状态

        :param trigger_status: The trigger_status of this Workflow.
        :type trigger_status: str
        """
        self._trigger_status = trigger_status

    @property
    def approve_id(self):
        """Gets the approve_id of this Workflow.

        审批id

        :return: The approve_id of this Workflow.
        :rtype: str
        """
        return self._approve_id

    @approve_id.setter
    def approve_id(self, approve_id):
        """Sets the approve_id of this Workflow.

        审批id

        :param approve_id: The approve_id of this Workflow.
        :type approve_id: str
        """
        self._approve_id = approve_id

    @property
    def template_i18n(self):
        """Gets the template_i18n of this Workflow.

        任务国际化字段，包含中英文描述

        :return: The template_i18n of this Workflow.
        :rtype: dict(str, dict(str, object))
        """
        return self._template_i18n

    @template_i18n.setter
    def template_i18n(self, template_i18n):
        """Sets the template_i18n of this Workflow.

        任务国际化字段，包含中英文描述

        :param template_i18n: The template_i18n of this Workflow.
        :type template_i18n: dict(str, dict(str, object))
        """
        self._template_i18n = template_i18n

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this Workflow.

        任务所属的企业项目

        :return: The enterprise_project_id of this Workflow.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this Workflow.

        任务所属的企业项目

        :param enterprise_project_id: The enterprise_project_id of this Workflow.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def last_execute_by(self):
        """Gets the last_execute_by of this Workflow.

        任务最后一次执行人

        :return: The last_execute_by of this Workflow.
        :rtype: str
        """
        return self._last_execute_by

    @last_execute_by.setter
    def last_execute_by(self, last_execute_by):
        """Sets the last_execute_by of this Workflow.

        任务最后一次执行人

        :param last_execute_by: The last_execute_by of this Workflow.
        :type last_execute_by: str
        """
        self._last_execute_by = last_execute_by

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
        if not isinstance(other, Workflow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
