# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AopWorkflowVersionInfo:

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
        'version_id': 'str',
        'name': 'str',
        'aopworkflow_id': 'str',
        'description': 'str',
        'project_id': 'str',
        'owner_id': 'str',
        'creator_id': 'str',
        'creator_name': 'str',
        'create_time': 'str',
        'modifier_id': 'str',
        'modifier_name': 'str',
        'update_time': 'str',
        'enabled': 'bool',
        'status': 'str',
        'version': 'str',
        'taskconfig': 'str',
        'taskflow': 'str',
        'taskflow_type': 'str',
        'aop_type': 'str',
        'input': 'str',
        'output': 'str',
        'dataclass_id': 'str',
        'dataclass_name': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version_id': 'version_id',
        'name': 'name',
        'aopworkflow_id': 'aopworkflow_id',
        'description': 'description',
        'project_id': 'project_id',
        'owner_id': 'owner_id',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'create_time': 'create_time',
        'modifier_id': 'modifier_id',
        'modifier_name': 'modifier_name',
        'update_time': 'update_time',
        'enabled': 'enabled',
        'status': 'status',
        'version': 'version',
        'taskconfig': 'taskconfig',
        'taskflow': 'taskflow',
        'taskflow_type': 'taskflow_type',
        'aop_type': 'aop_type',
        'input': 'input',
        'output': 'output',
        'dataclass_id': 'dataclass_id',
        'dataclass_name': 'dataclass_name',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, id=None, version_id=None, name=None, aopworkflow_id=None, description=None, project_id=None, owner_id=None, creator_id=None, creator_name=None, create_time=None, modifier_id=None, modifier_name=None, update_time=None, enabled=None, status=None, version=None, taskconfig=None, taskflow=None, taskflow_type=None, aop_type=None, input=None, output=None, dataclass_id=None, dataclass_name=None, workspace_id=None):
        r"""AopWorkflowVersionInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 流程版本ID **约束限制**: 不涉及
        :type id: str
        :param version_id: **参数解释**: 流程版本ID **约束限制**: 不涉及
        :type version_id: str
        :param name: **参数解释**: 流程版本名字 **约束限制**: 不涉及
        :type name: str
        :param aopworkflow_id: **参数解释**: 流程ID **约束限制**: 不涉及
        :type aopworkflow_id: str
        :param description: **参数解释**: 流程版本的描述 **取值范围**: 不涉及
        :type description: str
        :param project_id: **参数解释**: 租户的项目ID **约束限制**: 不涉及
        :type project_id: str
        :param owner_id: **参数解释**: 所有者ID **约束限制**: 不涉及
        :type owner_id: str
        :param creator_id: **参数解释**: 创建者ID **取值范围**: 不涉及
        :type creator_id: str
        :param creator_name: **参数解释**: 创建者的名称 **取值范围**: 不涉及
        :type creator_name: str
        :param create_time: **参数解释**: 创建时间 **取值范围**: 不涉及
        :type create_time: str
        :param modifier_id: **参数解释**: 更新者的ID **取值范围**: 不涉及
        :type modifier_id: str
        :param modifier_name: **参数解释**: 更新者的名称 **取值范围**: 不涉及
        :type modifier_name: str
        :param update_time: **参数解释**: 更新的时间 **取值范围**: 不涉及
        :type update_time: str
        :param enabled: **参数解释**: 是否已启用 **约束限制**: 不涉及         **取值范围**: - true  已启用 - false 未启用  **默认值**:  false
        :type enabled: bool
        :param status: **参数解释**: 流程的状态 - pending_submit 草稿 - pending_approval 待审核 - publishing 发布中 - publish_failed 发布失败 - not_activated 未激活 - activated 已激活 - rejected 审核拒绝  **取值范围**: - pending_submit - pending_approval - publishing - publish_failed - not_activated - activated - rejected
        :type status: str
        :param version: **参数解释**: 当前流程的版本 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type version: str
        :param taskconfig: **参数解释**: 流程拓扑图的参数配置 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type taskconfig: str
        :param taskflow: **参数解释**: 流程的拓扑图的BASE64编码 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type taskflow: str
        :param taskflow_type: **参数解释**: 流程的类型 **约束限制**: 不涉及         **取值范围**: - JSON  **默认值**:  不涉及
        :type taskflow_type: str
        :param aop_type: **参数解释**: 流程的类型 - NORMAL 通用 - SURVEY 调查 - HEMOSTASIS 止血 - EASE 缓解  **约束限制**: 不涉及         **取值范围**: - NORMAL - SURVEY - HEMOSTASIS - EASE  **默认值**:  不涉及
        :type aop_type: str
        :param input: **参数解释**: 流程的输入 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type input: str
        :param output: **参数解释**: 流程的输出 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type output: str
        :param dataclass_id: **参数解释**: 数据类的ID **取值范围**: 不涉及
        :type dataclass_id: str
        :param dataclass_name: **参数解释**: 数据类的名称 **取值范围**: 不涉及
        :type dataclass_name: str
        :param workspace_id: **参数解释**: 工作空间ID **取值范围**: 不涉及
        :type workspace_id: str
        """
        
        

        self._id = None
        self._version_id = None
        self._name = None
        self._aopworkflow_id = None
        self._description = None
        self._project_id = None
        self._owner_id = None
        self._creator_id = None
        self._creator_name = None
        self._create_time = None
        self._modifier_id = None
        self._modifier_name = None
        self._update_time = None
        self._enabled = None
        self._status = None
        self._version = None
        self._taskconfig = None
        self._taskflow = None
        self._taskflow_type = None
        self._aop_type = None
        self._input = None
        self._output = None
        self._dataclass_id = None
        self._dataclass_name = None
        self._workspace_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version_id is not None:
            self.version_id = version_id
        if name is not None:
            self.name = name
        if aopworkflow_id is not None:
            self.aopworkflow_id = aopworkflow_id
        if description is not None:
            self.description = description
        if project_id is not None:
            self.project_id = project_id
        if owner_id is not None:
            self.owner_id = owner_id
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if create_time is not None:
            self.create_time = create_time
        if modifier_id is not None:
            self.modifier_id = modifier_id
        if modifier_name is not None:
            self.modifier_name = modifier_name
        if update_time is not None:
            self.update_time = update_time
        if enabled is not None:
            self.enabled = enabled
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version
        if taskconfig is not None:
            self.taskconfig = taskconfig
        if taskflow is not None:
            self.taskflow = taskflow
        if taskflow_type is not None:
            self.taskflow_type = taskflow_type
        if aop_type is not None:
            self.aop_type = aop_type
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if dataclass_name is not None:
            self.dataclass_name = dataclass_name
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def id(self):
        r"""Gets the id of this AopWorkflowVersionInfo.

        **参数解释**: 流程版本ID **约束限制**: 不涉及

        :return: The id of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AopWorkflowVersionInfo.

        **参数解释**: 流程版本ID **约束限制**: 不涉及

        :param id: The id of this AopWorkflowVersionInfo.
        :type id: str
        """
        self._id = id

    @property
    def version_id(self):
        r"""Gets the version_id of this AopWorkflowVersionInfo.

        **参数解释**: 流程版本ID **约束限制**: 不涉及

        :return: The version_id of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this AopWorkflowVersionInfo.

        **参数解释**: 流程版本ID **约束限制**: 不涉及

        :param version_id: The version_id of this AopWorkflowVersionInfo.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def name(self):
        r"""Gets the name of this AopWorkflowVersionInfo.

        **参数解释**: 流程版本名字 **约束限制**: 不涉及

        :return: The name of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AopWorkflowVersionInfo.

        **参数解释**: 流程版本名字 **约束限制**: 不涉及

        :param name: The name of this AopWorkflowVersionInfo.
        :type name: str
        """
        self._name = name

    @property
    def aopworkflow_id(self):
        r"""Gets the aopworkflow_id of this AopWorkflowVersionInfo.

        **参数解释**: 流程ID **约束限制**: 不涉及

        :return: The aopworkflow_id of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._aopworkflow_id

    @aopworkflow_id.setter
    def aopworkflow_id(self, aopworkflow_id):
        r"""Sets the aopworkflow_id of this AopWorkflowVersionInfo.

        **参数解释**: 流程ID **约束限制**: 不涉及

        :param aopworkflow_id: The aopworkflow_id of this AopWorkflowVersionInfo.
        :type aopworkflow_id: str
        """
        self._aopworkflow_id = aopworkflow_id

    @property
    def description(self):
        r"""Gets the description of this AopWorkflowVersionInfo.

        **参数解释**: 流程版本的描述 **取值范围**: 不涉及

        :return: The description of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AopWorkflowVersionInfo.

        **参数解释**: 流程版本的描述 **取值范围**: 不涉及

        :param description: The description of this AopWorkflowVersionInfo.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        r"""Gets the project_id of this AopWorkflowVersionInfo.

        **参数解释**: 租户的项目ID **约束限制**: 不涉及

        :return: The project_id of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AopWorkflowVersionInfo.

        **参数解释**: 租户的项目ID **约束限制**: 不涉及

        :param project_id: The project_id of this AopWorkflowVersionInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def owner_id(self):
        r"""Gets the owner_id of this AopWorkflowVersionInfo.

        **参数解释**: 所有者ID **约束限制**: 不涉及

        :return: The owner_id of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this AopWorkflowVersionInfo.

        **参数解释**: 所有者ID **约束限制**: 不涉及

        :param owner_id: The owner_id of this AopWorkflowVersionInfo.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def creator_id(self):
        r"""Gets the creator_id of this AopWorkflowVersionInfo.

        **参数解释**: 创建者ID **取值范围**: 不涉及

        :return: The creator_id of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this AopWorkflowVersionInfo.

        **参数解释**: 创建者ID **取值范围**: 不涉及

        :param creator_id: The creator_id of this AopWorkflowVersionInfo.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        r"""Gets the creator_name of this AopWorkflowVersionInfo.

        **参数解释**: 创建者的名称 **取值范围**: 不涉及

        :return: The creator_name of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this AopWorkflowVersionInfo.

        **参数解释**: 创建者的名称 **取值范围**: 不涉及

        :param creator_name: The creator_name of this AopWorkflowVersionInfo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def create_time(self):
        r"""Gets the create_time of this AopWorkflowVersionInfo.

        **参数解释**: 创建时间 **取值范围**: 不涉及

        :return: The create_time of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AopWorkflowVersionInfo.

        **参数解释**: 创建时间 **取值范围**: 不涉及

        :param create_time: The create_time of this AopWorkflowVersionInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def modifier_id(self):
        r"""Gets the modifier_id of this AopWorkflowVersionInfo.

        **参数解释**: 更新者的ID **取值范围**: 不涉及

        :return: The modifier_id of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, modifier_id):
        r"""Sets the modifier_id of this AopWorkflowVersionInfo.

        **参数解释**: 更新者的ID **取值范围**: 不涉及

        :param modifier_id: The modifier_id of this AopWorkflowVersionInfo.
        :type modifier_id: str
        """
        self._modifier_id = modifier_id

    @property
    def modifier_name(self):
        r"""Gets the modifier_name of this AopWorkflowVersionInfo.

        **参数解释**: 更新者的名称 **取值范围**: 不涉及

        :return: The modifier_name of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, modifier_name):
        r"""Sets the modifier_name of this AopWorkflowVersionInfo.

        **参数解释**: 更新者的名称 **取值范围**: 不涉及

        :param modifier_name: The modifier_name of this AopWorkflowVersionInfo.
        :type modifier_name: str
        """
        self._modifier_name = modifier_name

    @property
    def update_time(self):
        r"""Gets the update_time of this AopWorkflowVersionInfo.

        **参数解释**: 更新的时间 **取值范围**: 不涉及

        :return: The update_time of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AopWorkflowVersionInfo.

        **参数解释**: 更新的时间 **取值范围**: 不涉及

        :param update_time: The update_time of this AopWorkflowVersionInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def enabled(self):
        r"""Gets the enabled of this AopWorkflowVersionInfo.

        **参数解释**: 是否已启用 **约束限制**: 不涉及         **取值范围**: - true  已启用 - false 未启用  **默认值**:  false

        :return: The enabled of this AopWorkflowVersionInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this AopWorkflowVersionInfo.

        **参数解释**: 是否已启用 **约束限制**: 不涉及         **取值范围**: - true  已启用 - false 未启用  **默认值**:  false

        :param enabled: The enabled of this AopWorkflowVersionInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def status(self):
        r"""Gets the status of this AopWorkflowVersionInfo.

        **参数解释**: 流程的状态 - pending_submit 草稿 - pending_approval 待审核 - publishing 发布中 - publish_failed 发布失败 - not_activated 未激活 - activated 已激活 - rejected 审核拒绝  **取值范围**: - pending_submit - pending_approval - publishing - publish_failed - not_activated - activated - rejected

        :return: The status of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AopWorkflowVersionInfo.

        **参数解释**: 流程的状态 - pending_submit 草稿 - pending_approval 待审核 - publishing 发布中 - publish_failed 发布失败 - not_activated 未激活 - activated 已激活 - rejected 审核拒绝  **取值范围**: - pending_submit - pending_approval - publishing - publish_failed - not_activated - activated - rejected

        :param status: The status of this AopWorkflowVersionInfo.
        :type status: str
        """
        self._status = status

    @property
    def version(self):
        r"""Gets the version of this AopWorkflowVersionInfo.

        **参数解释**: 当前流程的版本 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The version of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this AopWorkflowVersionInfo.

        **参数解释**: 当前流程的版本 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param version: The version of this AopWorkflowVersionInfo.
        :type version: str
        """
        self._version = version

    @property
    def taskconfig(self):
        r"""Gets the taskconfig of this AopWorkflowVersionInfo.

        **参数解释**: 流程拓扑图的参数配置 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The taskconfig of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._taskconfig

    @taskconfig.setter
    def taskconfig(self, taskconfig):
        r"""Sets the taskconfig of this AopWorkflowVersionInfo.

        **参数解释**: 流程拓扑图的参数配置 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param taskconfig: The taskconfig of this AopWorkflowVersionInfo.
        :type taskconfig: str
        """
        self._taskconfig = taskconfig

    @property
    def taskflow(self):
        r"""Gets the taskflow of this AopWorkflowVersionInfo.

        **参数解释**: 流程的拓扑图的BASE64编码 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The taskflow of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._taskflow

    @taskflow.setter
    def taskflow(self, taskflow):
        r"""Sets the taskflow of this AopWorkflowVersionInfo.

        **参数解释**: 流程的拓扑图的BASE64编码 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param taskflow: The taskflow of this AopWorkflowVersionInfo.
        :type taskflow: str
        """
        self._taskflow = taskflow

    @property
    def taskflow_type(self):
        r"""Gets the taskflow_type of this AopWorkflowVersionInfo.

        **参数解释**: 流程的类型 **约束限制**: 不涉及         **取值范围**: - JSON  **默认值**:  不涉及

        :return: The taskflow_type of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._taskflow_type

    @taskflow_type.setter
    def taskflow_type(self, taskflow_type):
        r"""Sets the taskflow_type of this AopWorkflowVersionInfo.

        **参数解释**: 流程的类型 **约束限制**: 不涉及         **取值范围**: - JSON  **默认值**:  不涉及

        :param taskflow_type: The taskflow_type of this AopWorkflowVersionInfo.
        :type taskflow_type: str
        """
        self._taskflow_type = taskflow_type

    @property
    def aop_type(self):
        r"""Gets the aop_type of this AopWorkflowVersionInfo.

        **参数解释**: 流程的类型 - NORMAL 通用 - SURVEY 调查 - HEMOSTASIS 止血 - EASE 缓解  **约束限制**: 不涉及         **取值范围**: - NORMAL - SURVEY - HEMOSTASIS - EASE  **默认值**:  不涉及

        :return: The aop_type of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._aop_type

    @aop_type.setter
    def aop_type(self, aop_type):
        r"""Sets the aop_type of this AopWorkflowVersionInfo.

        **参数解释**: 流程的类型 - NORMAL 通用 - SURVEY 调查 - HEMOSTASIS 止血 - EASE 缓解  **约束限制**: 不涉及         **取值范围**: - NORMAL - SURVEY - HEMOSTASIS - EASE  **默认值**:  不涉及

        :param aop_type: The aop_type of this AopWorkflowVersionInfo.
        :type aop_type: str
        """
        self._aop_type = aop_type

    @property
    def input(self):
        r"""Gets the input of this AopWorkflowVersionInfo.

        **参数解释**: 流程的输入 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The input of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this AopWorkflowVersionInfo.

        **参数解释**: 流程的输入 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param input: The input of this AopWorkflowVersionInfo.
        :type input: str
        """
        self._input = input

    @property
    def output(self):
        r"""Gets the output of this AopWorkflowVersionInfo.

        **参数解释**: 流程的输出 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The output of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this AopWorkflowVersionInfo.

        **参数解释**: 流程的输出 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param output: The output of this AopWorkflowVersionInfo.
        :type output: str
        """
        self._output = output

    @property
    def dataclass_id(self):
        r"""Gets the dataclass_id of this AopWorkflowVersionInfo.

        **参数解释**: 数据类的ID **取值范围**: 不涉及

        :return: The dataclass_id of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        r"""Sets the dataclass_id of this AopWorkflowVersionInfo.

        **参数解释**: 数据类的ID **取值范围**: 不涉及

        :param dataclass_id: The dataclass_id of this AopWorkflowVersionInfo.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def dataclass_name(self):
        r"""Gets the dataclass_name of this AopWorkflowVersionInfo.

        **参数解释**: 数据类的名称 **取值范围**: 不涉及

        :return: The dataclass_name of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._dataclass_name

    @dataclass_name.setter
    def dataclass_name(self, dataclass_name):
        r"""Sets the dataclass_name of this AopWorkflowVersionInfo.

        **参数解释**: 数据类的名称 **取值范围**: 不涉及

        :param dataclass_name: The dataclass_name of this AopWorkflowVersionInfo.
        :type dataclass_name: str
        """
        self._dataclass_name = dataclass_name

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this AopWorkflowVersionInfo.

        **参数解释**: 工作空间ID **取值范围**: 不涉及

        :return: The workspace_id of this AopWorkflowVersionInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this AopWorkflowVersionInfo.

        **参数解释**: 工作空间ID **取值范围**: 不涉及

        :param workspace_id: The workspace_id of this AopWorkflowVersionInfo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, AopWorkflowVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
