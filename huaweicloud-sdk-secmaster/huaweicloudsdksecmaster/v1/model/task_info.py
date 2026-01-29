# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskInfo:

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
        'aopengine_task_id': 'str',
        'name': 'str',
        'project_id': 'str',
        'description': 'str',
        'create_time': 'str',
        'creator_id': 'str',
        'creator_name': 'str',
        'update_time': 'str',
        'modifier_id': 'str',
        'modifier_name': 'str',
        'approveuser_id': 'str',
        'approveuser_name': 'str',
        'approver': 'str',
        'notes': 'str',
        'definition_key': 'str',
        'note': 'str',
        'due_date': 'str',
        'action_id': 'str',
        'action_version_id': 'str',
        'action_instance_id': 'str',
        'workspace_id': 'str',
        'review_comments': 'str',
        'view_parameters': 'str',
        'handle_parameters': 'str',
        'business_type': 'str',
        'related_object': 'str',
        'attachment_id_list': 'list[str]',
        'comments': 'list[TaskCommentInfo]',
        'status': 'str',
        'due_handle': 'str'
    }

    attribute_map = {
        'id': 'id',
        'aopengine_task_id': 'aopengine_task_id',
        'name': 'name',
        'project_id': 'project_id',
        'description': 'description',
        'create_time': 'create_time',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'update_time': 'update_time',
        'modifier_id': 'modifier_id',
        'modifier_name': 'modifier_name',
        'approveuser_id': 'approveuser_id',
        'approveuser_name': 'approveuser_name',
        'approver': 'approver',
        'notes': 'notes',
        'definition_key': 'definition_key',
        'note': 'note',
        'due_date': 'due_date',
        'action_id': 'action_id',
        'action_version_id': 'action_version_id',
        'action_instance_id': 'action_instance_id',
        'workspace_id': 'workspace_id',
        'review_comments': 'review_comments',
        'view_parameters': 'view_parameters',
        'handle_parameters': 'handle_parameters',
        'business_type': 'business_type',
        'related_object': 'related_object',
        'attachment_id_list': 'attachment_id_list',
        'comments': 'comments',
        'status': 'status',
        'due_handle': 'due_handle'
    }

    def __init__(self, id=None, aopengine_task_id=None, name=None, project_id=None, description=None, create_time=None, creator_id=None, creator_name=None, update_time=None, modifier_id=None, modifier_name=None, approveuser_id=None, approveuser_name=None, approver=None, notes=None, definition_key=None, note=None, due_date=None, action_id=None, action_version_id=None, action_instance_id=None, workspace_id=None, review_comments=None, view_parameters=None, handle_parameters=None, business_type=None, related_object=None, attachment_id_list=None, comments=None, status=None, due_handle=None):
        r"""TaskInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 待办任务的ID **取值范围**: 不涉及
        :type id: str
        :param aopengine_task_id: **参数解释**: 待办任务的引擎任务Id **取值范围**: 不涉及.
        :type aopengine_task_id: str
        :param name: **参数解释**: 待办任务的名称 **取值范围**: 不涉及
        :type name: str
        :param project_id: **参数解释**: 待办任务的项目Id **取值范围**: 不涉及
        :type project_id: str
        :param description: **参数解释**: 待办任务的描述 **取值范围**: 不涉及
        :type description: str
        :param create_time: **参数解释**: 待办的创建时间 **取值范围**: 不涉及
        :type create_time: str
        :param creator_id: **参数解释**: 待办的创建者ID **取值范围**: system
        :type creator_id: str
        :param creator_name: **参数解释**: 待办的创建者名字 **取值范围**: 不涉及
        :type creator_name: str
        :param update_time: **参数解释**: 待办的更新时间 **取值范围**: 不涉及
        :type update_time: str
        :param modifier_id: **参数解释**: 待办的修改者ID **取值范围**: system
        :type modifier_id: str
        :param modifier_name: **参数解释**: 待办的修改者名字 **取值范围**: 不涉及
        :type modifier_name: str
        :param approveuser_id: **参数解释**: 待办支持的审核人用户ID **取值范围**: 不涉及
        :type approveuser_id: str
        :param approveuser_name: **参数解释**: 待办支持的审核人用户名字 **取值范围**: 不涉及
        :type approveuser_name: str
        :param approver: **参数解释**: 待办审核人用户名称 **取值范围**: 不涉及
        :type approver: str
        :param notes: **参数解释**: 待办的备注 **取值范围**: 不涉及
        :type notes: str
        :param definition_key: **参数解释**: 待办的节点流程拓扑图的KEY **取值范围**: 不涉及
        :type definition_key: str
        :param note: **参数解释**: 待办的备注 **取值范围**: 不涉及
        :type note: str
        :param due_date: **参数解释**: 待办的超期时间 **取值范围**: 默认为创建时间+15天
        :type due_date: str
        :param action_id: **参数解释**: 待办的节点的流程或剧本ID 当 business_type是WORKFLOWPUBLISH或者WORKFLOWNODEAPPROVE，此时为流程ID 当 business_type是PLAYBOOKPUBLISH或者PLAYBOOKNODEAPPROVE，此时为剧本ID **取值范围**: 不涉及
        :type action_id: str
        :param action_version_id: **参数解释**: 待办的节点的流程或剧本版本ID 当 business_type是WORKFLOWPUBLISH或者WORKFLOWNODEAPPROVE，此时为流程版本ID 当 business_type是PLAYBOOKPUBLISH或者PLAYBOOKNODEAPPROVE，此时为剧本版本ID  **取值范围**: 不涉及
        :type action_version_id: str
        :param action_instance_id: **参数解释**: 待办的节点的流程或剧本的实例ID 当 business_type是WORKFLOWNODEAPPROVE，此时为流程实例ID 当 business_type是PLAYBOOKNODEAPPROVE，此时为剧本实例ID  **取值范围**: 不涉及
        :type action_instance_id: str
        :param workspace_id: **参数解释**: 待办任务的空间ID **取值范围**: 不涉及
        :type workspace_id: str
        :param review_comments: **参数解释**: 待办任务审核意见 **取值范围**: 不涉及
        :type review_comments: str
        :param view_parameters: **参数解释**: 待办任务查看参数 **取值范围**: 不涉及
        :type view_parameters: str
        :param handle_parameters: **参数解释**: 待办任务的人工处理参数 **取值范围**: 不涉及
        :type handle_parameters: str
        :param business_type: **参数解释**: 待办的业务类型 - WORKFLOWPUBLISH 流程发布 - WORKFLOWNODEAPPROVE 流程节点审核 - PLAYBOOKPUBLISH 剧本发布 - PLAYBOOKNODEAPPROVE 剧本节点审核  **取值范围**: - WORKFLOWPUBLISH - WORKFLOWNODEAPPROVE - PLAYBOOKPUBLISH - PLAYBOOKNODEAPPROVE
        :type business_type: str
        :param related_object: **参数解释**: 待办任务的关联的流程 or 剧本名称 **取值范围**: 不涉及
        :type related_object: str
        :param attachment_id_list: **参数解释**: 待办节点的附件ID列表 **取值范围**: 不涉及
        :type attachment_id_list: list[str]
        :param comments: **参数解释**: 待办节点的待办评论 **取值范围**: 不涉及
        :type comments: list[:class:`huaweicloudsdksecmaster.v1.TaskCommentInfo`]
        :param status: **参数解释**: 待办的业务类型 - waiting  待处理 - canceled 已取消 - finished 已完成  **取值范围**: - waiting - canceled - finished
        :type status: str
        :param due_handle: **参数解释**: 待办的到期处理方式 - CONTINUE 继续执行 - INTERRUPT 终止  **取值范围**: - CONTINUE - INTERRUPT
        :type due_handle: str
        """
        
        

        self._id = None
        self._aopengine_task_id = None
        self._name = None
        self._project_id = None
        self._description = None
        self._create_time = None
        self._creator_id = None
        self._creator_name = None
        self._update_time = None
        self._modifier_id = None
        self._modifier_name = None
        self._approveuser_id = None
        self._approveuser_name = None
        self._approver = None
        self._notes = None
        self._definition_key = None
        self._note = None
        self._due_date = None
        self._action_id = None
        self._action_version_id = None
        self._action_instance_id = None
        self._workspace_id = None
        self._review_comments = None
        self._view_parameters = None
        self._handle_parameters = None
        self._business_type = None
        self._related_object = None
        self._attachment_id_list = None
        self._comments = None
        self._status = None
        self._due_handle = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if aopengine_task_id is not None:
            self.aopengine_task_id = aopengine_task_id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if update_time is not None:
            self.update_time = update_time
        if modifier_id is not None:
            self.modifier_id = modifier_id
        if modifier_name is not None:
            self.modifier_name = modifier_name
        if approveuser_id is not None:
            self.approveuser_id = approveuser_id
        if approveuser_name is not None:
            self.approveuser_name = approveuser_name
        if approver is not None:
            self.approver = approver
        if notes is not None:
            self.notes = notes
        if definition_key is not None:
            self.definition_key = definition_key
        if note is not None:
            self.note = note
        if due_date is not None:
            self.due_date = due_date
        if action_id is not None:
            self.action_id = action_id
        if action_version_id is not None:
            self.action_version_id = action_version_id
        if action_instance_id is not None:
            self.action_instance_id = action_instance_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if review_comments is not None:
            self.review_comments = review_comments
        if view_parameters is not None:
            self.view_parameters = view_parameters
        if handle_parameters is not None:
            self.handle_parameters = handle_parameters
        if business_type is not None:
            self.business_type = business_type
        if related_object is not None:
            self.related_object = related_object
        if attachment_id_list is not None:
            self.attachment_id_list = attachment_id_list
        if comments is not None:
            self.comments = comments
        if status is not None:
            self.status = status
        if due_handle is not None:
            self.due_handle = due_handle

    @property
    def id(self):
        r"""Gets the id of this TaskInfo.

        **参数解释**: 待办任务的ID **取值范围**: 不涉及

        :return: The id of this TaskInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TaskInfo.

        **参数解释**: 待办任务的ID **取值范围**: 不涉及

        :param id: The id of this TaskInfo.
        :type id: str
        """
        self._id = id

    @property
    def aopengine_task_id(self):
        r"""Gets the aopengine_task_id of this TaskInfo.

        **参数解释**: 待办任务的引擎任务Id **取值范围**: 不涉及.

        :return: The aopengine_task_id of this TaskInfo.
        :rtype: str
        """
        return self._aopengine_task_id

    @aopengine_task_id.setter
    def aopengine_task_id(self, aopengine_task_id):
        r"""Sets the aopengine_task_id of this TaskInfo.

        **参数解释**: 待办任务的引擎任务Id **取值范围**: 不涉及.

        :param aopengine_task_id: The aopengine_task_id of this TaskInfo.
        :type aopengine_task_id: str
        """
        self._aopengine_task_id = aopengine_task_id

    @property
    def name(self):
        r"""Gets the name of this TaskInfo.

        **参数解释**: 待办任务的名称 **取值范围**: 不涉及

        :return: The name of this TaskInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TaskInfo.

        **参数解释**: 待办任务的名称 **取值范围**: 不涉及

        :param name: The name of this TaskInfo.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this TaskInfo.

        **参数解释**: 待办任务的项目Id **取值范围**: 不涉及

        :return: The project_id of this TaskInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TaskInfo.

        **参数解释**: 待办任务的项目Id **取值范围**: 不涉及

        :param project_id: The project_id of this TaskInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def description(self):
        r"""Gets the description of this TaskInfo.

        **参数解释**: 待办任务的描述 **取值范围**: 不涉及

        :return: The description of this TaskInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TaskInfo.

        **参数解释**: 待办任务的描述 **取值范围**: 不涉及

        :param description: The description of this TaskInfo.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this TaskInfo.

        **参数解释**: 待办的创建时间 **取值范围**: 不涉及

        :return: The create_time of this TaskInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TaskInfo.

        **参数解释**: 待办的创建时间 **取值范围**: 不涉及

        :param create_time: The create_time of this TaskInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator_id(self):
        r"""Gets the creator_id of this TaskInfo.

        **参数解释**: 待办的创建者ID **取值范围**: system

        :return: The creator_id of this TaskInfo.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this TaskInfo.

        **参数解释**: 待办的创建者ID **取值范围**: system

        :param creator_id: The creator_id of this TaskInfo.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        r"""Gets the creator_name of this TaskInfo.

        **参数解释**: 待办的创建者名字 **取值范围**: 不涉及

        :return: The creator_name of this TaskInfo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this TaskInfo.

        **参数解释**: 待办的创建者名字 **取值范围**: 不涉及

        :param creator_name: The creator_name of this TaskInfo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def update_time(self):
        r"""Gets the update_time of this TaskInfo.

        **参数解释**: 待办的更新时间 **取值范围**: 不涉及

        :return: The update_time of this TaskInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TaskInfo.

        **参数解释**: 待办的更新时间 **取值范围**: 不涉及

        :param update_time: The update_time of this TaskInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def modifier_id(self):
        r"""Gets the modifier_id of this TaskInfo.

        **参数解释**: 待办的修改者ID **取值范围**: system

        :return: The modifier_id of this TaskInfo.
        :rtype: str
        """
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, modifier_id):
        r"""Sets the modifier_id of this TaskInfo.

        **参数解释**: 待办的修改者ID **取值范围**: system

        :param modifier_id: The modifier_id of this TaskInfo.
        :type modifier_id: str
        """
        self._modifier_id = modifier_id

    @property
    def modifier_name(self):
        r"""Gets the modifier_name of this TaskInfo.

        **参数解释**: 待办的修改者名字 **取值范围**: 不涉及

        :return: The modifier_name of this TaskInfo.
        :rtype: str
        """
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, modifier_name):
        r"""Sets the modifier_name of this TaskInfo.

        **参数解释**: 待办的修改者名字 **取值范围**: 不涉及

        :param modifier_name: The modifier_name of this TaskInfo.
        :type modifier_name: str
        """
        self._modifier_name = modifier_name

    @property
    def approveuser_id(self):
        r"""Gets the approveuser_id of this TaskInfo.

        **参数解释**: 待办支持的审核人用户ID **取值范围**: 不涉及

        :return: The approveuser_id of this TaskInfo.
        :rtype: str
        """
        return self._approveuser_id

    @approveuser_id.setter
    def approveuser_id(self, approveuser_id):
        r"""Sets the approveuser_id of this TaskInfo.

        **参数解释**: 待办支持的审核人用户ID **取值范围**: 不涉及

        :param approveuser_id: The approveuser_id of this TaskInfo.
        :type approveuser_id: str
        """
        self._approveuser_id = approveuser_id

    @property
    def approveuser_name(self):
        r"""Gets the approveuser_name of this TaskInfo.

        **参数解释**: 待办支持的审核人用户名字 **取值范围**: 不涉及

        :return: The approveuser_name of this TaskInfo.
        :rtype: str
        """
        return self._approveuser_name

    @approveuser_name.setter
    def approveuser_name(self, approveuser_name):
        r"""Sets the approveuser_name of this TaskInfo.

        **参数解释**: 待办支持的审核人用户名字 **取值范围**: 不涉及

        :param approveuser_name: The approveuser_name of this TaskInfo.
        :type approveuser_name: str
        """
        self._approveuser_name = approveuser_name

    @property
    def approver(self):
        r"""Gets the approver of this TaskInfo.

        **参数解释**: 待办审核人用户名称 **取值范围**: 不涉及

        :return: The approver of this TaskInfo.
        :rtype: str
        """
        return self._approver

    @approver.setter
    def approver(self, approver):
        r"""Sets the approver of this TaskInfo.

        **参数解释**: 待办审核人用户名称 **取值范围**: 不涉及

        :param approver: The approver of this TaskInfo.
        :type approver: str
        """
        self._approver = approver

    @property
    def notes(self):
        r"""Gets the notes of this TaskInfo.

        **参数解释**: 待办的备注 **取值范围**: 不涉及

        :return: The notes of this TaskInfo.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        r"""Sets the notes of this TaskInfo.

        **参数解释**: 待办的备注 **取值范围**: 不涉及

        :param notes: The notes of this TaskInfo.
        :type notes: str
        """
        self._notes = notes

    @property
    def definition_key(self):
        r"""Gets the definition_key of this TaskInfo.

        **参数解释**: 待办的节点流程拓扑图的KEY **取值范围**: 不涉及

        :return: The definition_key of this TaskInfo.
        :rtype: str
        """
        return self._definition_key

    @definition_key.setter
    def definition_key(self, definition_key):
        r"""Sets the definition_key of this TaskInfo.

        **参数解释**: 待办的节点流程拓扑图的KEY **取值范围**: 不涉及

        :param definition_key: The definition_key of this TaskInfo.
        :type definition_key: str
        """
        self._definition_key = definition_key

    @property
    def note(self):
        r"""Gets the note of this TaskInfo.

        **参数解释**: 待办的备注 **取值范围**: 不涉及

        :return: The note of this TaskInfo.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        r"""Sets the note of this TaskInfo.

        **参数解释**: 待办的备注 **取值范围**: 不涉及

        :param note: The note of this TaskInfo.
        :type note: str
        """
        self._note = note

    @property
    def due_date(self):
        r"""Gets the due_date of this TaskInfo.

        **参数解释**: 待办的超期时间 **取值范围**: 默认为创建时间+15天

        :return: The due_date of this TaskInfo.
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        r"""Sets the due_date of this TaskInfo.

        **参数解释**: 待办的超期时间 **取值范围**: 默认为创建时间+15天

        :param due_date: The due_date of this TaskInfo.
        :type due_date: str
        """
        self._due_date = due_date

    @property
    def action_id(self):
        r"""Gets the action_id of this TaskInfo.

        **参数解释**: 待办的节点的流程或剧本ID 当 business_type是WORKFLOWPUBLISH或者WORKFLOWNODEAPPROVE，此时为流程ID 当 business_type是PLAYBOOKPUBLISH或者PLAYBOOKNODEAPPROVE，此时为剧本ID **取值范围**: 不涉及

        :return: The action_id of this TaskInfo.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        r"""Sets the action_id of this TaskInfo.

        **参数解释**: 待办的节点的流程或剧本ID 当 business_type是WORKFLOWPUBLISH或者WORKFLOWNODEAPPROVE，此时为流程ID 当 business_type是PLAYBOOKPUBLISH或者PLAYBOOKNODEAPPROVE，此时为剧本ID **取值范围**: 不涉及

        :param action_id: The action_id of this TaskInfo.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def action_version_id(self):
        r"""Gets the action_version_id of this TaskInfo.

        **参数解释**: 待办的节点的流程或剧本版本ID 当 business_type是WORKFLOWPUBLISH或者WORKFLOWNODEAPPROVE，此时为流程版本ID 当 business_type是PLAYBOOKPUBLISH或者PLAYBOOKNODEAPPROVE，此时为剧本版本ID  **取值范围**: 不涉及

        :return: The action_version_id of this TaskInfo.
        :rtype: str
        """
        return self._action_version_id

    @action_version_id.setter
    def action_version_id(self, action_version_id):
        r"""Sets the action_version_id of this TaskInfo.

        **参数解释**: 待办的节点的流程或剧本版本ID 当 business_type是WORKFLOWPUBLISH或者WORKFLOWNODEAPPROVE，此时为流程版本ID 当 business_type是PLAYBOOKPUBLISH或者PLAYBOOKNODEAPPROVE，此时为剧本版本ID  **取值范围**: 不涉及

        :param action_version_id: The action_version_id of this TaskInfo.
        :type action_version_id: str
        """
        self._action_version_id = action_version_id

    @property
    def action_instance_id(self):
        r"""Gets the action_instance_id of this TaskInfo.

        **参数解释**: 待办的节点的流程或剧本的实例ID 当 business_type是WORKFLOWNODEAPPROVE，此时为流程实例ID 当 business_type是PLAYBOOKNODEAPPROVE，此时为剧本实例ID  **取值范围**: 不涉及

        :return: The action_instance_id of this TaskInfo.
        :rtype: str
        """
        return self._action_instance_id

    @action_instance_id.setter
    def action_instance_id(self, action_instance_id):
        r"""Sets the action_instance_id of this TaskInfo.

        **参数解释**: 待办的节点的流程或剧本的实例ID 当 business_type是WORKFLOWNODEAPPROVE，此时为流程实例ID 当 business_type是PLAYBOOKNODEAPPROVE，此时为剧本实例ID  **取值范围**: 不涉及

        :param action_instance_id: The action_instance_id of this TaskInfo.
        :type action_instance_id: str
        """
        self._action_instance_id = action_instance_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this TaskInfo.

        **参数解释**: 待办任务的空间ID **取值范围**: 不涉及

        :return: The workspace_id of this TaskInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this TaskInfo.

        **参数解释**: 待办任务的空间ID **取值范围**: 不涉及

        :param workspace_id: The workspace_id of this TaskInfo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def review_comments(self):
        r"""Gets the review_comments of this TaskInfo.

        **参数解释**: 待办任务审核意见 **取值范围**: 不涉及

        :return: The review_comments of this TaskInfo.
        :rtype: str
        """
        return self._review_comments

    @review_comments.setter
    def review_comments(self, review_comments):
        r"""Sets the review_comments of this TaskInfo.

        **参数解释**: 待办任务审核意见 **取值范围**: 不涉及

        :param review_comments: The review_comments of this TaskInfo.
        :type review_comments: str
        """
        self._review_comments = review_comments

    @property
    def view_parameters(self):
        r"""Gets the view_parameters of this TaskInfo.

        **参数解释**: 待办任务查看参数 **取值范围**: 不涉及

        :return: The view_parameters of this TaskInfo.
        :rtype: str
        """
        return self._view_parameters

    @view_parameters.setter
    def view_parameters(self, view_parameters):
        r"""Sets the view_parameters of this TaskInfo.

        **参数解释**: 待办任务查看参数 **取值范围**: 不涉及

        :param view_parameters: The view_parameters of this TaskInfo.
        :type view_parameters: str
        """
        self._view_parameters = view_parameters

    @property
    def handle_parameters(self):
        r"""Gets the handle_parameters of this TaskInfo.

        **参数解释**: 待办任务的人工处理参数 **取值范围**: 不涉及

        :return: The handle_parameters of this TaskInfo.
        :rtype: str
        """
        return self._handle_parameters

    @handle_parameters.setter
    def handle_parameters(self, handle_parameters):
        r"""Sets the handle_parameters of this TaskInfo.

        **参数解释**: 待办任务的人工处理参数 **取值范围**: 不涉及

        :param handle_parameters: The handle_parameters of this TaskInfo.
        :type handle_parameters: str
        """
        self._handle_parameters = handle_parameters

    @property
    def business_type(self):
        r"""Gets the business_type of this TaskInfo.

        **参数解释**: 待办的业务类型 - WORKFLOWPUBLISH 流程发布 - WORKFLOWNODEAPPROVE 流程节点审核 - PLAYBOOKPUBLISH 剧本发布 - PLAYBOOKNODEAPPROVE 剧本节点审核  **取值范围**: - WORKFLOWPUBLISH - WORKFLOWNODEAPPROVE - PLAYBOOKPUBLISH - PLAYBOOKNODEAPPROVE

        :return: The business_type of this TaskInfo.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        r"""Sets the business_type of this TaskInfo.

        **参数解释**: 待办的业务类型 - WORKFLOWPUBLISH 流程发布 - WORKFLOWNODEAPPROVE 流程节点审核 - PLAYBOOKPUBLISH 剧本发布 - PLAYBOOKNODEAPPROVE 剧本节点审核  **取值范围**: - WORKFLOWPUBLISH - WORKFLOWNODEAPPROVE - PLAYBOOKPUBLISH - PLAYBOOKNODEAPPROVE

        :param business_type: The business_type of this TaskInfo.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def related_object(self):
        r"""Gets the related_object of this TaskInfo.

        **参数解释**: 待办任务的关联的流程 or 剧本名称 **取值范围**: 不涉及

        :return: The related_object of this TaskInfo.
        :rtype: str
        """
        return self._related_object

    @related_object.setter
    def related_object(self, related_object):
        r"""Sets the related_object of this TaskInfo.

        **参数解释**: 待办任务的关联的流程 or 剧本名称 **取值范围**: 不涉及

        :param related_object: The related_object of this TaskInfo.
        :type related_object: str
        """
        self._related_object = related_object

    @property
    def attachment_id_list(self):
        r"""Gets the attachment_id_list of this TaskInfo.

        **参数解释**: 待办节点的附件ID列表 **取值范围**: 不涉及

        :return: The attachment_id_list of this TaskInfo.
        :rtype: list[str]
        """
        return self._attachment_id_list

    @attachment_id_list.setter
    def attachment_id_list(self, attachment_id_list):
        r"""Sets the attachment_id_list of this TaskInfo.

        **参数解释**: 待办节点的附件ID列表 **取值范围**: 不涉及

        :param attachment_id_list: The attachment_id_list of this TaskInfo.
        :type attachment_id_list: list[str]
        """
        self._attachment_id_list = attachment_id_list

    @property
    def comments(self):
        r"""Gets the comments of this TaskInfo.

        **参数解释**: 待办节点的待办评论 **取值范围**: 不涉及

        :return: The comments of this TaskInfo.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.TaskCommentInfo`]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        r"""Sets the comments of this TaskInfo.

        **参数解释**: 待办节点的待办评论 **取值范围**: 不涉及

        :param comments: The comments of this TaskInfo.
        :type comments: list[:class:`huaweicloudsdksecmaster.v1.TaskCommentInfo`]
        """
        self._comments = comments

    @property
    def status(self):
        r"""Gets the status of this TaskInfo.

        **参数解释**: 待办的业务类型 - waiting  待处理 - canceled 已取消 - finished 已完成  **取值范围**: - waiting - canceled - finished

        :return: The status of this TaskInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TaskInfo.

        **参数解释**: 待办的业务类型 - waiting  待处理 - canceled 已取消 - finished 已完成  **取值范围**: - waiting - canceled - finished

        :param status: The status of this TaskInfo.
        :type status: str
        """
        self._status = status

    @property
    def due_handle(self):
        r"""Gets the due_handle of this TaskInfo.

        **参数解释**: 待办的到期处理方式 - CONTINUE 继续执行 - INTERRUPT 终止  **取值范围**: - CONTINUE - INTERRUPT

        :return: The due_handle of this TaskInfo.
        :rtype: str
        """
        return self._due_handle

    @due_handle.setter
    def due_handle(self, due_handle):
        r"""Sets the due_handle of this TaskInfo.

        **参数解释**: 待办的到期处理方式 - CONTINUE 继续执行 - INTERRUPT 终止  **取值范围**: - CONTINUE - INTERRUPT

        :param due_handle: The due_handle of this TaskInfo.
        :type due_handle: str
        """
        self._due_handle = due_handle

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
        if not isinstance(other, TaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
