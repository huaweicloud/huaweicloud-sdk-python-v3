# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCocTicketRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'change_notes': 'str',
        'description': 'str',
        'enterprise_project': 'str',
        'change_type': 'str',
        'level': 'str',
        'ticket_type': 'str',
        'change_scheme': 'str',
        'change_guides': 'str',
        'commit_upload_attachment': 'str',
        'regions': 'str',
        'change_scene_id': 'str',
        'current_cloud_service_id': 'str',
        'root_cause_cloud_service': 'str',
        'source': 'str',
        'source_id': 'str',
        'fount_time': 'int',
        'virtual_schedule_type': 'str',
        'issue_contact_person': 'str',
        'schedule_scenes': 'str',
        'virtual_schedule_role': 'str',
        'location_id': 'str',
        'plan_task_sub_type': 'str',
        'plan_task_id': 'str',
        'plan_task_name': 'str',
        'plan_task_params': 'str',
        'is_start_process': 'bool',
        'sub_tickets': 'list[TicketCreateSubTicketInfo]'
    }

    attribute_map = {
        'title': 'title',
        'change_notes': 'change_notes',
        'description': 'description',
        'enterprise_project': 'enterprise_project',
        'change_type': 'change_type',
        'level': 'level',
        'ticket_type': 'ticket_type',
        'change_scheme': 'change_scheme',
        'change_guides': 'change_guides',
        'commit_upload_attachment': 'commit_upload_attachment',
        'regions': 'regions',
        'change_scene_id': 'change_scene_id',
        'current_cloud_service_id': 'current_cloud_service_id',
        'root_cause_cloud_service': 'root_cause_cloud_service',
        'source': 'source',
        'source_id': 'source_id',
        'fount_time': 'fount_time',
        'virtual_schedule_type': 'virtual_schedule_type',
        'issue_contact_person': 'issue_contact_person',
        'schedule_scenes': 'schedule_scenes',
        'virtual_schedule_role': 'virtual_schedule_role',
        'location_id': 'location_id',
        'plan_task_sub_type': 'plan_task_sub_type',
        'plan_task_id': 'plan_task_id',
        'plan_task_name': 'plan_task_name',
        'plan_task_params': 'plan_task_params',
        'is_start_process': 'is_start_process',
        'sub_tickets': 'sub_tickets'
    }

    def __init__(self, title=None, change_notes=None, description=None, enterprise_project=None, change_type=None, level=None, ticket_type=None, change_scheme=None, change_guides=None, commit_upload_attachment=None, regions=None, change_scene_id=None, current_cloud_service_id=None, root_cause_cloud_service=None, source=None, source_id=None, fount_time=None, virtual_schedule_type=None, issue_contact_person=None, schedule_scenes=None, virtual_schedule_role=None, location_id=None, plan_task_sub_type=None, plan_task_id=None, plan_task_name=None, plan_task_params=None, is_start_process=None, sub_tickets=None):
        r"""CreateCocTicketRequestBody

        The model defined in huaweicloud sdk

        :param title: **参数解释：** 工单标题。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type title: str
        :param change_notes: **参数解释：** 变更单描述。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type change_notes: str
        :param description: **参数解释：** 问题单描述信息。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type description: str
        :param enterprise_project: **参数解释：** 企业项目ID **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 0
        :type enterprise_project: str
        :param change_type: **参数解释：** 变更类型。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。 **取值范围：** 枚举值 change_type_conventional：常规变更 change_type_urgentu：紧急变更 **默认取值：** 不涉及
        :type change_type: str
        :param level: **参数解释：** 工单级别。 **约束限制：** 不涉及 **取值范围：** 当ticket_type为change创建变更单时，枚举值 change_level_010 -- A级变更 change_level_020 -- B级变更 change_level_030 -- C级变更 change_level_040 -- D级变更 当ticket_type为issues_mgmt创建问题单时，枚举值 issues_level_1000 -- 致命 issues_level_2000 -- 严重 issues_level_3000 -- 一般 issues_level_4000 -- 提示 **默认取值：** 不涉及
        :type level: str
        :param ticket_type: **参数解释：** 问题单类型，通过访问 云运维中心--&gt;基础配置--&gt;流程管理页签下问题流程--&gt;问题类别可查询所有可传递的问题类型，此处传递问题类型ID。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，必填。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type ticket_type: str
        :param change_scheme: **参数解释：** 任务类型，可选作业或者变更指导书两种。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。当取值为change_scheme_guides时，请求参数change_guides必填。当取值为change_scheme_runbook时，参数plan_task_sub_type、plan_task_id、plan_task_name和plan_task_params必填。 **取值范围：** 枚举值 change_scheme_runbook：作业 change_scheme_guides：变更指导书 **默认取值：** 不涉及
        :type change_scheme: str
        :param change_guides: **参数解释：** 变更指导书ID。 **约束限制：** 当ticket_type为change创建变更单，且任务选择变更指导书时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type change_guides: str
        :param commit_upload_attachment: **参数解释：** 问题单附件，上传附件ID。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type commit_upload_attachment: str
        :param regions: **参数解释：** 问题单所属Region，此处传RegionID，多个Region用英文逗号隔开。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type regions: str
        :param change_scene_id: **参数解释：** 变更场景。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。 **取值范围：** 取配置页面【流程管理】下“变更场景”TAB页中列表属性ID列的值，示例：GOCMLL06 **默认取值：** 不涉及
        :type change_scene_id: str
        :param current_cloud_service_id: **参数解释：** 归属应用。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type current_cloud_service_id: str
        :param root_cause_cloud_service: **参数解释：** 归属应用。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type root_cause_cloud_service: str
        :param source: **参数解释：** 问题单来源。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 当ticket_type为issues_mgmt创建问题单时，枚举值 issues_mgmt_associated_type_1000 -- 事件 issues_mgmt_associated_type_4000 -- 运维主动发现 issues_mgmt_associated_type_2000 -- 告警 issues_mgmt_associated_type_3000 -- WarRoom **默认取值：** 不涉及
        :type source: str
        :param source_id: **参数解释：** 问题单来源工单单号。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。当source的值为issues_mgmt_associated_type_1000、issues_mgmt_associated_type_2000或issues_mgmt_associated_type_3000时，必填。需要填写关联的工单单号。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type source_id: str
        :param fount_time: **参数解释：** 发现时间，时间戳。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type fount_time: int
        :param virtual_schedule_type: **参数解释：** 问题单处理人类型。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段必填。 **取值范围：** 当ticket_type为issues_mgmt创建问题单时，枚举值 issues_mgmt_virtual_schedule_type_1000 -- 排班 issues_mgmt_virtual_schedule_type_2000 -- 个人 **默认取值：** 不涉及
        :type virtual_schedule_type: str
        :param issue_contact_person: **参数解释：** 问题单责任人工号ID。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。如需指定问题单责任人，则该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type issue_contact_person: str
        :param schedule_scenes: **参数解释：** 问题单责任人从排班中获取，该值为排班场景ID。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type schedule_scenes: str
        :param virtual_schedule_role: **参数解释：** 问题单责任人从排班中获取，该值为排班角色ID。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type virtual_schedule_role: str
        :param location_id: **参数解释：** 变更区域ID。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type location_id: str
        :param plan_task_sub_type: **参数解释：** 预案子类型。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。当任务类型change_scheme取值为change_scheme_runbook时，该值必填。 **取值范围：** 枚举值 CUSTOMIZATION：自定义作业 COMMUNAL：公共作业 **默认取值：** 不涉及
        :type plan_task_sub_type: str
        :param plan_task_id: **参数解释：** 需要执行的作业ID。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。当任务类型change_scheme取值为change_scheme_runbook时，该值必填。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type plan_task_id: str
        :param plan_task_name: **参数解释：** 需要执行的作业名称。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。当任务类型change_scheme取值为change_scheme_runbook时，该值必填。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type plan_task_name: str
        :param plan_task_params: **参数解释：** 执行作业时所需的参数信息。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。当任务类型change_scheme取值为change_scheme_runbook时，该值必填。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type plan_task_params: str
        :param is_start_process: **参数解释：** 是否启动流程，当此值为false时，创建出来的工单为草稿状态。此值默认为true，创建出来的工单状态为未受理状态。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type is_start_process: bool
        :param sub_tickets: **参数解释：** 变更子单的信息，包含变更单涉及的服务和Region信息。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填且有效，当ticket_type非change时，该字段可置空。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type sub_tickets: list[:class:`huaweicloudsdkcoc.v1.TicketCreateSubTicketInfo`]
        """
        
        

        self._title = None
        self._change_notes = None
        self._description = None
        self._enterprise_project = None
        self._change_type = None
        self._level = None
        self._ticket_type = None
        self._change_scheme = None
        self._change_guides = None
        self._commit_upload_attachment = None
        self._regions = None
        self._change_scene_id = None
        self._current_cloud_service_id = None
        self._root_cause_cloud_service = None
        self._source = None
        self._source_id = None
        self._fount_time = None
        self._virtual_schedule_type = None
        self._issue_contact_person = None
        self._schedule_scenes = None
        self._virtual_schedule_role = None
        self._location_id = None
        self._plan_task_sub_type = None
        self._plan_task_id = None
        self._plan_task_name = None
        self._plan_task_params = None
        self._is_start_process = None
        self._sub_tickets = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if change_notes is not None:
            self.change_notes = change_notes
        if description is not None:
            self.description = description
        if enterprise_project is not None:
            self.enterprise_project = enterprise_project
        if change_type is not None:
            self.change_type = change_type
        if level is not None:
            self.level = level
        if ticket_type is not None:
            self.ticket_type = ticket_type
        if change_scheme is not None:
            self.change_scheme = change_scheme
        if change_guides is not None:
            self.change_guides = change_guides
        if commit_upload_attachment is not None:
            self.commit_upload_attachment = commit_upload_attachment
        if regions is not None:
            self.regions = regions
        if change_scene_id is not None:
            self.change_scene_id = change_scene_id
        if current_cloud_service_id is not None:
            self.current_cloud_service_id = current_cloud_service_id
        if root_cause_cloud_service is not None:
            self.root_cause_cloud_service = root_cause_cloud_service
        if source is not None:
            self.source = source
        if source_id is not None:
            self.source_id = source_id
        if fount_time is not None:
            self.fount_time = fount_time
        if virtual_schedule_type is not None:
            self.virtual_schedule_type = virtual_schedule_type
        if issue_contact_person is not None:
            self.issue_contact_person = issue_contact_person
        if schedule_scenes is not None:
            self.schedule_scenes = schedule_scenes
        if virtual_schedule_role is not None:
            self.virtual_schedule_role = virtual_schedule_role
        if location_id is not None:
            self.location_id = location_id
        if plan_task_sub_type is not None:
            self.plan_task_sub_type = plan_task_sub_type
        if plan_task_id is not None:
            self.plan_task_id = plan_task_id
        if plan_task_name is not None:
            self.plan_task_name = plan_task_name
        if plan_task_params is not None:
            self.plan_task_params = plan_task_params
        if is_start_process is not None:
            self.is_start_process = is_start_process
        if sub_tickets is not None:
            self.sub_tickets = sub_tickets

    @property
    def title(self):
        r"""Gets the title of this CreateCocTicketRequestBody.

        **参数解释：** 工单标题。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The title of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CreateCocTicketRequestBody.

        **参数解释：** 工单标题。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param title: The title of this CreateCocTicketRequestBody.
        :type title: str
        """
        self._title = title

    @property
    def change_notes(self):
        r"""Gets the change_notes of this CreateCocTicketRequestBody.

        **参数解释：** 变更单描述。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The change_notes of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._change_notes

    @change_notes.setter
    def change_notes(self, change_notes):
        r"""Sets the change_notes of this CreateCocTicketRequestBody.

        **参数解释：** 变更单描述。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param change_notes: The change_notes of this CreateCocTicketRequestBody.
        :type change_notes: str
        """
        self._change_notes = change_notes

    @property
    def description(self):
        r"""Gets the description of this CreateCocTicketRequestBody.

        **参数解释：** 问题单描述信息。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The description of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateCocTicketRequestBody.

        **参数解释：** 问题单描述信息。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param description: The description of this CreateCocTicketRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project(self):
        r"""Gets the enterprise_project of this CreateCocTicketRequestBody.

        **参数解释：** 企业项目ID **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 0

        :return: The enterprise_project of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._enterprise_project

    @enterprise_project.setter
    def enterprise_project(self, enterprise_project):
        r"""Sets the enterprise_project of this CreateCocTicketRequestBody.

        **参数解释：** 企业项目ID **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 0

        :param enterprise_project: The enterprise_project of this CreateCocTicketRequestBody.
        :type enterprise_project: str
        """
        self._enterprise_project = enterprise_project

    @property
    def change_type(self):
        r"""Gets the change_type of this CreateCocTicketRequestBody.

        **参数解释：** 变更类型。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。 **取值范围：** 枚举值 change_type_conventional：常规变更 change_type_urgentu：紧急变更 **默认取值：** 不涉及

        :return: The change_type of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        r"""Sets the change_type of this CreateCocTicketRequestBody.

        **参数解释：** 变更类型。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。 **取值范围：** 枚举值 change_type_conventional：常规变更 change_type_urgentu：紧急变更 **默认取值：** 不涉及

        :param change_type: The change_type of this CreateCocTicketRequestBody.
        :type change_type: str
        """
        self._change_type = change_type

    @property
    def level(self):
        r"""Gets the level of this CreateCocTicketRequestBody.

        **参数解释：** 工单级别。 **约束限制：** 不涉及 **取值范围：** 当ticket_type为change创建变更单时，枚举值 change_level_010 -- A级变更 change_level_020 -- B级变更 change_level_030 -- C级变更 change_level_040 -- D级变更 当ticket_type为issues_mgmt创建问题单时，枚举值 issues_level_1000 -- 致命 issues_level_2000 -- 严重 issues_level_3000 -- 一般 issues_level_4000 -- 提示 **默认取值：** 不涉及

        :return: The level of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this CreateCocTicketRequestBody.

        **参数解释：** 工单级别。 **约束限制：** 不涉及 **取值范围：** 当ticket_type为change创建变更单时，枚举值 change_level_010 -- A级变更 change_level_020 -- B级变更 change_level_030 -- C级变更 change_level_040 -- D级变更 当ticket_type为issues_mgmt创建问题单时，枚举值 issues_level_1000 -- 致命 issues_level_2000 -- 严重 issues_level_3000 -- 一般 issues_level_4000 -- 提示 **默认取值：** 不涉及

        :param level: The level of this CreateCocTicketRequestBody.
        :type level: str
        """
        self._level = level

    @property
    def ticket_type(self):
        r"""Gets the ticket_type of this CreateCocTicketRequestBody.

        **参数解释：** 问题单类型，通过访问 云运维中心-->基础配置-->流程管理页签下问题流程-->问题类别可查询所有可传递的问题类型，此处传递问题类型ID。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The ticket_type of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, ticket_type):
        r"""Sets the ticket_type of this CreateCocTicketRequestBody.

        **参数解释：** 问题单类型，通过访问 云运维中心-->基础配置-->流程管理页签下问题流程-->问题类别可查询所有可传递的问题类型，此处传递问题类型ID。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param ticket_type: The ticket_type of this CreateCocTicketRequestBody.
        :type ticket_type: str
        """
        self._ticket_type = ticket_type

    @property
    def change_scheme(self):
        r"""Gets the change_scheme of this CreateCocTicketRequestBody.

        **参数解释：** 任务类型，可选作业或者变更指导书两种。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。当取值为change_scheme_guides时，请求参数change_guides必填。当取值为change_scheme_runbook时，参数plan_task_sub_type、plan_task_id、plan_task_name和plan_task_params必填。 **取值范围：** 枚举值 change_scheme_runbook：作业 change_scheme_guides：变更指导书 **默认取值：** 不涉及

        :return: The change_scheme of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._change_scheme

    @change_scheme.setter
    def change_scheme(self, change_scheme):
        r"""Sets the change_scheme of this CreateCocTicketRequestBody.

        **参数解释：** 任务类型，可选作业或者变更指导书两种。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。当取值为change_scheme_guides时，请求参数change_guides必填。当取值为change_scheme_runbook时，参数plan_task_sub_type、plan_task_id、plan_task_name和plan_task_params必填。 **取值范围：** 枚举值 change_scheme_runbook：作业 change_scheme_guides：变更指导书 **默认取值：** 不涉及

        :param change_scheme: The change_scheme of this CreateCocTicketRequestBody.
        :type change_scheme: str
        """
        self._change_scheme = change_scheme

    @property
    def change_guides(self):
        r"""Gets the change_guides of this CreateCocTicketRequestBody.

        **参数解释：** 变更指导书ID。 **约束限制：** 当ticket_type为change创建变更单，且任务选择变更指导书时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The change_guides of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._change_guides

    @change_guides.setter
    def change_guides(self, change_guides):
        r"""Sets the change_guides of this CreateCocTicketRequestBody.

        **参数解释：** 变更指导书ID。 **约束限制：** 当ticket_type为change创建变更单，且任务选择变更指导书时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param change_guides: The change_guides of this CreateCocTicketRequestBody.
        :type change_guides: str
        """
        self._change_guides = change_guides

    @property
    def commit_upload_attachment(self):
        r"""Gets the commit_upload_attachment of this CreateCocTicketRequestBody.

        **参数解释：** 问题单附件，上传附件ID。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The commit_upload_attachment of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._commit_upload_attachment

    @commit_upload_attachment.setter
    def commit_upload_attachment(self, commit_upload_attachment):
        r"""Sets the commit_upload_attachment of this CreateCocTicketRequestBody.

        **参数解释：** 问题单附件，上传附件ID。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param commit_upload_attachment: The commit_upload_attachment of this CreateCocTicketRequestBody.
        :type commit_upload_attachment: str
        """
        self._commit_upload_attachment = commit_upload_attachment

    @property
    def regions(self):
        r"""Gets the regions of this CreateCocTicketRequestBody.

        **参数解释：** 问题单所属Region，此处传RegionID，多个Region用英文逗号隔开。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The regions of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        r"""Sets the regions of this CreateCocTicketRequestBody.

        **参数解释：** 问题单所属Region，此处传RegionID，多个Region用英文逗号隔开。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param regions: The regions of this CreateCocTicketRequestBody.
        :type regions: str
        """
        self._regions = regions

    @property
    def change_scene_id(self):
        r"""Gets the change_scene_id of this CreateCocTicketRequestBody.

        **参数解释：** 变更场景。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。 **取值范围：** 取配置页面【流程管理】下“变更场景”TAB页中列表属性ID列的值，示例：GOCMLL06 **默认取值：** 不涉及

        :return: The change_scene_id of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._change_scene_id

    @change_scene_id.setter
    def change_scene_id(self, change_scene_id):
        r"""Sets the change_scene_id of this CreateCocTicketRequestBody.

        **参数解释：** 变更场景。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。 **取值范围：** 取配置页面【流程管理】下“变更场景”TAB页中列表属性ID列的值，示例：GOCMLL06 **默认取值：** 不涉及

        :param change_scene_id: The change_scene_id of this CreateCocTicketRequestBody.
        :type change_scene_id: str
        """
        self._change_scene_id = change_scene_id

    @property
    def current_cloud_service_id(self):
        r"""Gets the current_cloud_service_id of this CreateCocTicketRequestBody.

        **参数解释：** 归属应用。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The current_cloud_service_id of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._current_cloud_service_id

    @current_cloud_service_id.setter
    def current_cloud_service_id(self, current_cloud_service_id):
        r"""Sets the current_cloud_service_id of this CreateCocTicketRequestBody.

        **参数解释：** 归属应用。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param current_cloud_service_id: The current_cloud_service_id of this CreateCocTicketRequestBody.
        :type current_cloud_service_id: str
        """
        self._current_cloud_service_id = current_cloud_service_id

    @property
    def root_cause_cloud_service(self):
        r"""Gets the root_cause_cloud_service of this CreateCocTicketRequestBody.

        **参数解释：** 归属应用。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The root_cause_cloud_service of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._root_cause_cloud_service

    @root_cause_cloud_service.setter
    def root_cause_cloud_service(self, root_cause_cloud_service):
        r"""Sets the root_cause_cloud_service of this CreateCocTicketRequestBody.

        **参数解释：** 归属应用。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param root_cause_cloud_service: The root_cause_cloud_service of this CreateCocTicketRequestBody.
        :type root_cause_cloud_service: str
        """
        self._root_cause_cloud_service = root_cause_cloud_service

    @property
    def source(self):
        r"""Gets the source of this CreateCocTicketRequestBody.

        **参数解释：** 问题单来源。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 当ticket_type为issues_mgmt创建问题单时，枚举值 issues_mgmt_associated_type_1000 -- 事件 issues_mgmt_associated_type_4000 -- 运维主动发现 issues_mgmt_associated_type_2000 -- 告警 issues_mgmt_associated_type_3000 -- WarRoom **默认取值：** 不涉及

        :return: The source of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CreateCocTicketRequestBody.

        **参数解释：** 问题单来源。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 当ticket_type为issues_mgmt创建问题单时，枚举值 issues_mgmt_associated_type_1000 -- 事件 issues_mgmt_associated_type_4000 -- 运维主动发现 issues_mgmt_associated_type_2000 -- 告警 issues_mgmt_associated_type_3000 -- WarRoom **默认取值：** 不涉及

        :param source: The source of this CreateCocTicketRequestBody.
        :type source: str
        """
        self._source = source

    @property
    def source_id(self):
        r"""Gets the source_id of this CreateCocTicketRequestBody.

        **参数解释：** 问题单来源工单单号。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。当source的值为issues_mgmt_associated_type_1000、issues_mgmt_associated_type_2000或issues_mgmt_associated_type_3000时，必填。需要填写关联的工单单号。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The source_id of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this CreateCocTicketRequestBody.

        **参数解释：** 问题单来源工单单号。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。当source的值为issues_mgmt_associated_type_1000、issues_mgmt_associated_type_2000或issues_mgmt_associated_type_3000时，必填。需要填写关联的工单单号。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param source_id: The source_id of this CreateCocTicketRequestBody.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def fount_time(self):
        r"""Gets the fount_time of this CreateCocTicketRequestBody.

        **参数解释：** 发现时间，时间戳。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The fount_time of this CreateCocTicketRequestBody.
        :rtype: int
        """
        return self._fount_time

    @fount_time.setter
    def fount_time(self, fount_time):
        r"""Sets the fount_time of this CreateCocTicketRequestBody.

        **参数解释：** 发现时间，时间戳。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param fount_time: The fount_time of this CreateCocTicketRequestBody.
        :type fount_time: int
        """
        self._fount_time = fount_time

    @property
    def virtual_schedule_type(self):
        r"""Gets the virtual_schedule_type of this CreateCocTicketRequestBody.

        **参数解释：** 问题单处理人类型。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段必填。 **取值范围：** 当ticket_type为issues_mgmt创建问题单时，枚举值 issues_mgmt_virtual_schedule_type_1000 -- 排班 issues_mgmt_virtual_schedule_type_2000 -- 个人 **默认取值：** 不涉及

        :return: The virtual_schedule_type of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._virtual_schedule_type

    @virtual_schedule_type.setter
    def virtual_schedule_type(self, virtual_schedule_type):
        r"""Sets the virtual_schedule_type of this CreateCocTicketRequestBody.

        **参数解释：** 问题单处理人类型。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段必填。 **取值范围：** 当ticket_type为issues_mgmt创建问题单时，枚举值 issues_mgmt_virtual_schedule_type_1000 -- 排班 issues_mgmt_virtual_schedule_type_2000 -- 个人 **默认取值：** 不涉及

        :param virtual_schedule_type: The virtual_schedule_type of this CreateCocTicketRequestBody.
        :type virtual_schedule_type: str
        """
        self._virtual_schedule_type = virtual_schedule_type

    @property
    def issue_contact_person(self):
        r"""Gets the issue_contact_person of this CreateCocTicketRequestBody.

        **参数解释：** 问题单责任人工号ID。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。如需指定问题单责任人，则该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The issue_contact_person of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._issue_contact_person

    @issue_contact_person.setter
    def issue_contact_person(self, issue_contact_person):
        r"""Sets the issue_contact_person of this CreateCocTicketRequestBody.

        **参数解释：** 问题单责任人工号ID。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。如需指定问题单责任人，则该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param issue_contact_person: The issue_contact_person of this CreateCocTicketRequestBody.
        :type issue_contact_person: str
        """
        self._issue_contact_person = issue_contact_person

    @property
    def schedule_scenes(self):
        r"""Gets the schedule_scenes of this CreateCocTicketRequestBody.

        **参数解释：** 问题单责任人从排班中获取，该值为排班场景ID。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The schedule_scenes of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._schedule_scenes

    @schedule_scenes.setter
    def schedule_scenes(self, schedule_scenes):
        r"""Sets the schedule_scenes of this CreateCocTicketRequestBody.

        **参数解释：** 问题单责任人从排班中获取，该值为排班场景ID。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param schedule_scenes: The schedule_scenes of this CreateCocTicketRequestBody.
        :type schedule_scenes: str
        """
        self._schedule_scenes = schedule_scenes

    @property
    def virtual_schedule_role(self):
        r"""Gets the virtual_schedule_role of this CreateCocTicketRequestBody.

        **参数解释：** 问题单责任人从排班中获取，该值为排班角色ID。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The virtual_schedule_role of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._virtual_schedule_role

    @virtual_schedule_role.setter
    def virtual_schedule_role(self, virtual_schedule_role):
        r"""Sets the virtual_schedule_role of this CreateCocTicketRequestBody.

        **参数解释：** 问题单责任人从排班中获取，该值为排班角色ID。 **约束限制：** 当ticket_type为issues_mgmt创建问题单时，该字段选填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param virtual_schedule_role: The virtual_schedule_role of this CreateCocTicketRequestBody.
        :type virtual_schedule_role: str
        """
        self._virtual_schedule_role = virtual_schedule_role

    @property
    def location_id(self):
        r"""Gets the location_id of this CreateCocTicketRequestBody.

        **参数解释：** 变更区域ID。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The location_id of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        r"""Sets the location_id of this CreateCocTicketRequestBody.

        **参数解释：** 变更区域ID。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param location_id: The location_id of this CreateCocTicketRequestBody.
        :type location_id: str
        """
        self._location_id = location_id

    @property
    def plan_task_sub_type(self):
        r"""Gets the plan_task_sub_type of this CreateCocTicketRequestBody.

        **参数解释：** 预案子类型。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。当任务类型change_scheme取值为change_scheme_runbook时，该值必填。 **取值范围：** 枚举值 CUSTOMIZATION：自定义作业 COMMUNAL：公共作业 **默认取值：** 不涉及

        :return: The plan_task_sub_type of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._plan_task_sub_type

    @plan_task_sub_type.setter
    def plan_task_sub_type(self, plan_task_sub_type):
        r"""Sets the plan_task_sub_type of this CreateCocTicketRequestBody.

        **参数解释：** 预案子类型。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。当任务类型change_scheme取值为change_scheme_runbook时，该值必填。 **取值范围：** 枚举值 CUSTOMIZATION：自定义作业 COMMUNAL：公共作业 **默认取值：** 不涉及

        :param plan_task_sub_type: The plan_task_sub_type of this CreateCocTicketRequestBody.
        :type plan_task_sub_type: str
        """
        self._plan_task_sub_type = plan_task_sub_type

    @property
    def plan_task_id(self):
        r"""Gets the plan_task_id of this CreateCocTicketRequestBody.

        **参数解释：** 需要执行的作业ID。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。当任务类型change_scheme取值为change_scheme_runbook时，该值必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The plan_task_id of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._plan_task_id

    @plan_task_id.setter
    def plan_task_id(self, plan_task_id):
        r"""Sets the plan_task_id of this CreateCocTicketRequestBody.

        **参数解释：** 需要执行的作业ID。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。当任务类型change_scheme取值为change_scheme_runbook时，该值必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param plan_task_id: The plan_task_id of this CreateCocTicketRequestBody.
        :type plan_task_id: str
        """
        self._plan_task_id = plan_task_id

    @property
    def plan_task_name(self):
        r"""Gets the plan_task_name of this CreateCocTicketRequestBody.

        **参数解释：** 需要执行的作业名称。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。当任务类型change_scheme取值为change_scheme_runbook时，该值必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The plan_task_name of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._plan_task_name

    @plan_task_name.setter
    def plan_task_name(self, plan_task_name):
        r"""Sets the plan_task_name of this CreateCocTicketRequestBody.

        **参数解释：** 需要执行的作业名称。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。当任务类型change_scheme取值为change_scheme_runbook时，该值必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param plan_task_name: The plan_task_name of this CreateCocTicketRequestBody.
        :type plan_task_name: str
        """
        self._plan_task_name = plan_task_name

    @property
    def plan_task_params(self):
        r"""Gets the plan_task_params of this CreateCocTicketRequestBody.

        **参数解释：** 执行作业时所需的参数信息。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。当任务类型change_scheme取值为change_scheme_runbook时，该值必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The plan_task_params of this CreateCocTicketRequestBody.
        :rtype: str
        """
        return self._plan_task_params

    @plan_task_params.setter
    def plan_task_params(self, plan_task_params):
        r"""Sets the plan_task_params of this CreateCocTicketRequestBody.

        **参数解释：** 执行作业时所需的参数信息。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填。当任务类型change_scheme取值为change_scheme_runbook时，该值必填。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param plan_task_params: The plan_task_params of this CreateCocTicketRequestBody.
        :type plan_task_params: str
        """
        self._plan_task_params = plan_task_params

    @property
    def is_start_process(self):
        r"""Gets the is_start_process of this CreateCocTicketRequestBody.

        **参数解释：** 是否启动流程，当此值为false时，创建出来的工单为草稿状态。此值默认为true，创建出来的工单状态为未受理状态。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The is_start_process of this CreateCocTicketRequestBody.
        :rtype: bool
        """
        return self._is_start_process

    @is_start_process.setter
    def is_start_process(self, is_start_process):
        r"""Sets the is_start_process of this CreateCocTicketRequestBody.

        **参数解释：** 是否启动流程，当此值为false时，创建出来的工单为草稿状态。此值默认为true，创建出来的工单状态为未受理状态。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param is_start_process: The is_start_process of this CreateCocTicketRequestBody.
        :type is_start_process: bool
        """
        self._is_start_process = is_start_process

    @property
    def sub_tickets(self):
        r"""Gets the sub_tickets of this CreateCocTicketRequestBody.

        **参数解释：** 变更子单的信息，包含变更单涉及的服务和Region信息。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填且有效，当ticket_type非change时，该字段可置空。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The sub_tickets of this CreateCocTicketRequestBody.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.TicketCreateSubTicketInfo`]
        """
        return self._sub_tickets

    @sub_tickets.setter
    def sub_tickets(self, sub_tickets):
        r"""Sets the sub_tickets of this CreateCocTicketRequestBody.

        **参数解释：** 变更子单的信息，包含变更单涉及的服务和Region信息。 **约束限制：** 当ticket_type为change创建变更单时，该字段必填且有效，当ticket_type非change时，该字段可置空。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param sub_tickets: The sub_tickets of this CreateCocTicketRequestBody.
        :type sub_tickets: list[:class:`huaweicloudsdkcoc.v1.TicketCreateSubTicketInfo`]
        """
        self._sub_tickets = sub_tickets

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
        if not isinstance(other, CreateCocTicketRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
