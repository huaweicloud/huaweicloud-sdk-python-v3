# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CocTicketDetailInfoResponseData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'issue_correlation_sla': 'str',
        'level': 'str',
        'root_cause_cloud_service': 'str',
        'root_cause_type': 'str',
        'current_cloud_service_id': 'str',
        'issue_contact_person': 'str',
        'issue_version': 'str',
        'source': 'str',
        'commit_upload_attachment': 'str',
        'source_id': 'str',
        'enterprise_project': 'str',
        'virtual_schedule_type': 'str',
        'title': 'str',
        'regions': 'str',
        'description': 'str',
        'root_cause_comment': 'str',
        'solution': 'str',
        'regions_serch': 'str',
        'level_approve_config': 'str',
        'suspension_approve_config': 'str',
        'handle_time': 'int',
        'fount_time': 'int',
        'is_common_issue': 'bool',
        'is_need_change': 'bool',
        'is_enable_suspension': 'bool',
        'is_start_process_async': 'bool',
        'is_update_null': 'bool',
        'creator': 'str',
        'operator': 'str',
        'is_return_full_info': 'bool',
        'is_start_process': 'bool',
        'ticket_id': 'str',
        'real_ticket_id': 'str',
        'assignee': 'str',
        'participator': 'str',
        'work_flow_status': 'str',
        'engine_error_msg': 'str',
        'baseline_status': 'str',
        'ticket_type': 'str',
        'phase': 'str',
        'sub_tickets': 'list[CocTicketDetailInfoResponseDataSubTickets]',
        'enum_data_list': 'list[IssuesTicketInfoEnumData]',
        'id': 'str',
        'meta_data_version': 'int',
        'update_time': 'int',
        'create_time': 'int',
        'is_deleted': 'bool',
        'ticket_type_id': 'str',
        'form_info': 'object'
    }

    attribute_map = {
        'issue_correlation_sla': 'issue_correlation_sla',
        'level': 'level',
        'root_cause_cloud_service': 'root_cause_cloud_service',
        'root_cause_type': 'root_cause_type',
        'current_cloud_service_id': 'current_cloud_service_id',
        'issue_contact_person': 'issue_contact_person',
        'issue_version': 'issue_version',
        'source': 'source',
        'commit_upload_attachment': 'commit_upload_attachment',
        'source_id': 'source_id',
        'enterprise_project': 'enterprise_project',
        'virtual_schedule_type': 'virtual_schedule_type',
        'title': 'title',
        'regions': 'regions',
        'description': 'description',
        'root_cause_comment': 'root_cause_comment',
        'solution': 'solution',
        'regions_serch': 'regions_serch',
        'level_approve_config': 'level_approve_config',
        'suspension_approve_config': 'suspension_approve_config',
        'handle_time': 'handle_time',
        'fount_time': 'fount_time',
        'is_common_issue': 'is_common_issue',
        'is_need_change': 'is_need_change',
        'is_enable_suspension': 'is_enable_suspension',
        'is_start_process_async': 'is_start_process_async',
        'is_update_null': 'is_update_null',
        'creator': 'creator',
        'operator': 'operator',
        'is_return_full_info': 'is_return_full_info',
        'is_start_process': 'is_start_process',
        'ticket_id': 'ticket_id',
        'real_ticket_id': 'real_ticket_id',
        'assignee': 'assignee',
        'participator': 'participator',
        'work_flow_status': 'work_flow_status',
        'engine_error_msg': 'engine_error_msg',
        'baseline_status': 'baseline_status',
        'ticket_type': 'ticket_type',
        'phase': 'phase',
        'sub_tickets': 'sub_tickets',
        'enum_data_list': 'enum_data_list',
        'id': 'id',
        'meta_data_version': 'meta_data_version',
        'update_time': 'update_time',
        'create_time': 'create_time',
        'is_deleted': 'is_deleted',
        'ticket_type_id': 'ticket_type_id',
        'form_info': '_form_info'
    }

    def __init__(self, issue_correlation_sla=None, level=None, root_cause_cloud_service=None, root_cause_type=None, current_cloud_service_id=None, issue_contact_person=None, issue_version=None, source=None, commit_upload_attachment=None, source_id=None, enterprise_project=None, virtual_schedule_type=None, title=None, regions=None, description=None, root_cause_comment=None, solution=None, regions_serch=None, level_approve_config=None, suspension_approve_config=None, handle_time=None, fount_time=None, is_common_issue=None, is_need_change=None, is_enable_suspension=None, is_start_process_async=None, is_update_null=None, creator=None, operator=None, is_return_full_info=None, is_start_process=None, ticket_id=None, real_ticket_id=None, assignee=None, participator=None, work_flow_status=None, engine_error_msg=None, baseline_status=None, ticket_type=None, phase=None, sub_tickets=None, enum_data_list=None, id=None, meta_data_version=None, update_time=None, create_time=None, is_deleted=None, ticket_type_id=None, form_info=None):
        r"""CocTicketDetailInfoResponseData

        The model defined in huaweicloud sdk

        :param issue_correlation_sla: 问题关联SLA。
        :type issue_correlation_sla: str
        :param level: 问题单级别。
        :type level: str
        :param root_cause_cloud_service: 问题单责任服务。
        :type root_cause_cloud_service: str
        :param root_cause_type: 问题单根因分类。
        :type root_cause_type: str
        :param current_cloud_service_id: 问题单服务。
        :type current_cloud_service_id: str
        :param issue_contact_person: 问题单接口人。
        :type issue_contact_person: str
        :param issue_version: 发现问题版本号。
        :type issue_version: str
        :param source: 问题单来源。
        :type source: str
        :param commit_upload_attachment: 上传附件。
        :type commit_upload_attachment: str
        :param source_id: 问题单来源id。
        :type source_id: str
        :param enterprise_project: 问题单企业项目。
        :type enterprise_project: str
        :param virtual_schedule_type: 问题单排班类型。
        :type virtual_schedule_type: str
        :param title: 问题单标题。
        :type title: str
        :param regions: 问题单region信息。
        :type regions: str
        :param description: 问题单描述。
        :type description: str
        :param root_cause_comment: 问题单根因分析。
        :type root_cause_comment: str
        :param solution: 问题单解决方案。
        :type solution: str
        :param regions_serch: 问题单区域搜索。
        :type regions_serch: str
        :param level_approve_config: 问题单级别审批配置。
        :type level_approve_config: str
        :param suspension_approve_config: 问题单挂起审批配置。
        :type suspension_approve_config: str
        :param handle_time: 处理时长。
        :type handle_time: int
        :param fount_time: 发现时间。
        :type fount_time: int
        :param is_common_issue: 是否共性问题。
        :type is_common_issue: bool
        :param is_need_change: 问题单是否需要变更。
        :type is_need_change: bool
        :param is_enable_suspension: 问题单是否开启挂起。
        :type is_enable_suspension: bool
        :param is_start_process_async: 是否启动异步流程。
        :type is_start_process_async: bool
        :param is_update_null: 是否重新提交空字段。
        :type is_update_null: bool
        :param creator: 问题单创建人。
        :type creator: str
        :param operator: 问题单操作人。
        :type operator: str
        :param is_return_full_info: 是否返回所有字段信息。
        :type is_return_full_info: bool
        :param is_start_process: 是否启动流程。
        :type is_start_process: bool
        :param ticket_id: 问题单工单ID。
        :type ticket_id: str
        :param real_ticket_id: 问题单工单单号。
        :type real_ticket_id: str
        :param assignee: 问题单当前责任人。
        :type assignee: str
        :param participator: 问题单参与人。
        :type participator: str
        :param work_flow_status: 问题单状态。
        :type work_flow_status: str
        :param engine_error_msg: 流程状态。
        :type engine_error_msg: str
        :param baseline_status: 基线状态。
        :type baseline_status: str
        :param ticket_type: 工单类型。
        :type ticket_type: str
        :param phase: 问题单当前阶段信息。
        :type phase: str
        :param sub_tickets: 变更子单信息。
        :type sub_tickets: list[:class:`huaweicloudsdkcoc.v1.CocTicketDetailInfoResponseDataSubTickets`]
        :param enum_data_list: 枚举列表。
        :type enum_data_list: list[:class:`huaweicloudsdkcoc.v1.IssuesTicketInfoEnumData`]
        :param id: 主键uuid
        :type id: str
        :param meta_data_version: 应用版本
        :type meta_data_version: int
        :param update_time: 更新时间。
        :type update_time: int
        :param create_time: 创单时间戳。
        :type create_time: int
        :param is_deleted: 工单是否被删除。
        :type is_deleted: bool
        :param ticket_type_id: 工单类型。
        :type ticket_type_id: str
        :param form_info: 动作信息。
        :type form_info: object
        """
        
        

        self._issue_correlation_sla = None
        self._level = None
        self._root_cause_cloud_service = None
        self._root_cause_type = None
        self._current_cloud_service_id = None
        self._issue_contact_person = None
        self._issue_version = None
        self._source = None
        self._commit_upload_attachment = None
        self._source_id = None
        self._enterprise_project = None
        self._virtual_schedule_type = None
        self._title = None
        self._regions = None
        self._description = None
        self._root_cause_comment = None
        self._solution = None
        self._regions_serch = None
        self._level_approve_config = None
        self._suspension_approve_config = None
        self._handle_time = None
        self._fount_time = None
        self._is_common_issue = None
        self._is_need_change = None
        self._is_enable_suspension = None
        self._is_start_process_async = None
        self._is_update_null = None
        self._creator = None
        self._operator = None
        self._is_return_full_info = None
        self._is_start_process = None
        self._ticket_id = None
        self._real_ticket_id = None
        self._assignee = None
        self._participator = None
        self._work_flow_status = None
        self._engine_error_msg = None
        self._baseline_status = None
        self._ticket_type = None
        self._phase = None
        self._sub_tickets = None
        self._enum_data_list = None
        self._id = None
        self._meta_data_version = None
        self._update_time = None
        self._create_time = None
        self._is_deleted = None
        self._ticket_type_id = None
        self._form_info = None
        self.discriminator = None

        if issue_correlation_sla is not None:
            self.issue_correlation_sla = issue_correlation_sla
        if level is not None:
            self.level = level
        if root_cause_cloud_service is not None:
            self.root_cause_cloud_service = root_cause_cloud_service
        if root_cause_type is not None:
            self.root_cause_type = root_cause_type
        if current_cloud_service_id is not None:
            self.current_cloud_service_id = current_cloud_service_id
        if issue_contact_person is not None:
            self.issue_contact_person = issue_contact_person
        if issue_version is not None:
            self.issue_version = issue_version
        if source is not None:
            self.source = source
        if commit_upload_attachment is not None:
            self.commit_upload_attachment = commit_upload_attachment
        if source_id is not None:
            self.source_id = source_id
        if enterprise_project is not None:
            self.enterprise_project = enterprise_project
        if virtual_schedule_type is not None:
            self.virtual_schedule_type = virtual_schedule_type
        if title is not None:
            self.title = title
        if regions is not None:
            self.regions = regions
        if description is not None:
            self.description = description
        if root_cause_comment is not None:
            self.root_cause_comment = root_cause_comment
        if solution is not None:
            self.solution = solution
        if regions_serch is not None:
            self.regions_serch = regions_serch
        if level_approve_config is not None:
            self.level_approve_config = level_approve_config
        if suspension_approve_config is not None:
            self.suspension_approve_config = suspension_approve_config
        if handle_time is not None:
            self.handle_time = handle_time
        if fount_time is not None:
            self.fount_time = fount_time
        if is_common_issue is not None:
            self.is_common_issue = is_common_issue
        if is_need_change is not None:
            self.is_need_change = is_need_change
        if is_enable_suspension is not None:
            self.is_enable_suspension = is_enable_suspension
        if is_start_process_async is not None:
            self.is_start_process_async = is_start_process_async
        if is_update_null is not None:
            self.is_update_null = is_update_null
        if creator is not None:
            self.creator = creator
        if operator is not None:
            self.operator = operator
        if is_return_full_info is not None:
            self.is_return_full_info = is_return_full_info
        if is_start_process is not None:
            self.is_start_process = is_start_process
        if ticket_id is not None:
            self.ticket_id = ticket_id
        if real_ticket_id is not None:
            self.real_ticket_id = real_ticket_id
        if assignee is not None:
            self.assignee = assignee
        if participator is not None:
            self.participator = participator
        if work_flow_status is not None:
            self.work_flow_status = work_flow_status
        if engine_error_msg is not None:
            self.engine_error_msg = engine_error_msg
        if baseline_status is not None:
            self.baseline_status = baseline_status
        if ticket_type is not None:
            self.ticket_type = ticket_type
        if phase is not None:
            self.phase = phase
        if sub_tickets is not None:
            self.sub_tickets = sub_tickets
        if enum_data_list is not None:
            self.enum_data_list = enum_data_list
        if id is not None:
            self.id = id
        if meta_data_version is not None:
            self.meta_data_version = meta_data_version
        if update_time is not None:
            self.update_time = update_time
        if create_time is not None:
            self.create_time = create_time
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if ticket_type_id is not None:
            self.ticket_type_id = ticket_type_id
        if form_info is not None:
            self.form_info = form_info

    @property
    def issue_correlation_sla(self):
        r"""Gets the issue_correlation_sla of this CocTicketDetailInfoResponseData.

        问题关联SLA。

        :return: The issue_correlation_sla of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._issue_correlation_sla

    @issue_correlation_sla.setter
    def issue_correlation_sla(self, issue_correlation_sla):
        r"""Sets the issue_correlation_sla of this CocTicketDetailInfoResponseData.

        问题关联SLA。

        :param issue_correlation_sla: The issue_correlation_sla of this CocTicketDetailInfoResponseData.
        :type issue_correlation_sla: str
        """
        self._issue_correlation_sla = issue_correlation_sla

    @property
    def level(self):
        r"""Gets the level of this CocTicketDetailInfoResponseData.

        问题单级别。

        :return: The level of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this CocTicketDetailInfoResponseData.

        问题单级别。

        :param level: The level of this CocTicketDetailInfoResponseData.
        :type level: str
        """
        self._level = level

    @property
    def root_cause_cloud_service(self):
        r"""Gets the root_cause_cloud_service of this CocTicketDetailInfoResponseData.

        问题单责任服务。

        :return: The root_cause_cloud_service of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._root_cause_cloud_service

    @root_cause_cloud_service.setter
    def root_cause_cloud_service(self, root_cause_cloud_service):
        r"""Sets the root_cause_cloud_service of this CocTicketDetailInfoResponseData.

        问题单责任服务。

        :param root_cause_cloud_service: The root_cause_cloud_service of this CocTicketDetailInfoResponseData.
        :type root_cause_cloud_service: str
        """
        self._root_cause_cloud_service = root_cause_cloud_service

    @property
    def root_cause_type(self):
        r"""Gets the root_cause_type of this CocTicketDetailInfoResponseData.

        问题单根因分类。

        :return: The root_cause_type of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._root_cause_type

    @root_cause_type.setter
    def root_cause_type(self, root_cause_type):
        r"""Sets the root_cause_type of this CocTicketDetailInfoResponseData.

        问题单根因分类。

        :param root_cause_type: The root_cause_type of this CocTicketDetailInfoResponseData.
        :type root_cause_type: str
        """
        self._root_cause_type = root_cause_type

    @property
    def current_cloud_service_id(self):
        r"""Gets the current_cloud_service_id of this CocTicketDetailInfoResponseData.

        问题单服务。

        :return: The current_cloud_service_id of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._current_cloud_service_id

    @current_cloud_service_id.setter
    def current_cloud_service_id(self, current_cloud_service_id):
        r"""Sets the current_cloud_service_id of this CocTicketDetailInfoResponseData.

        问题单服务。

        :param current_cloud_service_id: The current_cloud_service_id of this CocTicketDetailInfoResponseData.
        :type current_cloud_service_id: str
        """
        self._current_cloud_service_id = current_cloud_service_id

    @property
    def issue_contact_person(self):
        r"""Gets the issue_contact_person of this CocTicketDetailInfoResponseData.

        问题单接口人。

        :return: The issue_contact_person of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._issue_contact_person

    @issue_contact_person.setter
    def issue_contact_person(self, issue_contact_person):
        r"""Sets the issue_contact_person of this CocTicketDetailInfoResponseData.

        问题单接口人。

        :param issue_contact_person: The issue_contact_person of this CocTicketDetailInfoResponseData.
        :type issue_contact_person: str
        """
        self._issue_contact_person = issue_contact_person

    @property
    def issue_version(self):
        r"""Gets the issue_version of this CocTicketDetailInfoResponseData.

        发现问题版本号。

        :return: The issue_version of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._issue_version

    @issue_version.setter
    def issue_version(self, issue_version):
        r"""Sets the issue_version of this CocTicketDetailInfoResponseData.

        发现问题版本号。

        :param issue_version: The issue_version of this CocTicketDetailInfoResponseData.
        :type issue_version: str
        """
        self._issue_version = issue_version

    @property
    def source(self):
        r"""Gets the source of this CocTicketDetailInfoResponseData.

        问题单来源。

        :return: The source of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CocTicketDetailInfoResponseData.

        问题单来源。

        :param source: The source of this CocTicketDetailInfoResponseData.
        :type source: str
        """
        self._source = source

    @property
    def commit_upload_attachment(self):
        r"""Gets the commit_upload_attachment of this CocTicketDetailInfoResponseData.

        上传附件。

        :return: The commit_upload_attachment of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._commit_upload_attachment

    @commit_upload_attachment.setter
    def commit_upload_attachment(self, commit_upload_attachment):
        r"""Sets the commit_upload_attachment of this CocTicketDetailInfoResponseData.

        上传附件。

        :param commit_upload_attachment: The commit_upload_attachment of this CocTicketDetailInfoResponseData.
        :type commit_upload_attachment: str
        """
        self._commit_upload_attachment = commit_upload_attachment

    @property
    def source_id(self):
        r"""Gets the source_id of this CocTicketDetailInfoResponseData.

        问题单来源id。

        :return: The source_id of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this CocTicketDetailInfoResponseData.

        问题单来源id。

        :param source_id: The source_id of this CocTicketDetailInfoResponseData.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def enterprise_project(self):
        r"""Gets the enterprise_project of this CocTicketDetailInfoResponseData.

        问题单企业项目。

        :return: The enterprise_project of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._enterprise_project

    @enterprise_project.setter
    def enterprise_project(self, enterprise_project):
        r"""Sets the enterprise_project of this CocTicketDetailInfoResponseData.

        问题单企业项目。

        :param enterprise_project: The enterprise_project of this CocTicketDetailInfoResponseData.
        :type enterprise_project: str
        """
        self._enterprise_project = enterprise_project

    @property
    def virtual_schedule_type(self):
        r"""Gets the virtual_schedule_type of this CocTicketDetailInfoResponseData.

        问题单排班类型。

        :return: The virtual_schedule_type of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._virtual_schedule_type

    @virtual_schedule_type.setter
    def virtual_schedule_type(self, virtual_schedule_type):
        r"""Sets the virtual_schedule_type of this CocTicketDetailInfoResponseData.

        问题单排班类型。

        :param virtual_schedule_type: The virtual_schedule_type of this CocTicketDetailInfoResponseData.
        :type virtual_schedule_type: str
        """
        self._virtual_schedule_type = virtual_schedule_type

    @property
    def title(self):
        r"""Gets the title of this CocTicketDetailInfoResponseData.

        问题单标题。

        :return: The title of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CocTicketDetailInfoResponseData.

        问题单标题。

        :param title: The title of this CocTicketDetailInfoResponseData.
        :type title: str
        """
        self._title = title

    @property
    def regions(self):
        r"""Gets the regions of this CocTicketDetailInfoResponseData.

        问题单region信息。

        :return: The regions of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        r"""Sets the regions of this CocTicketDetailInfoResponseData.

        问题单region信息。

        :param regions: The regions of this CocTicketDetailInfoResponseData.
        :type regions: str
        """
        self._regions = regions

    @property
    def description(self):
        r"""Gets the description of this CocTicketDetailInfoResponseData.

        问题单描述。

        :return: The description of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CocTicketDetailInfoResponseData.

        问题单描述。

        :param description: The description of this CocTicketDetailInfoResponseData.
        :type description: str
        """
        self._description = description

    @property
    def root_cause_comment(self):
        r"""Gets the root_cause_comment of this CocTicketDetailInfoResponseData.

        问题单根因分析。

        :return: The root_cause_comment of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._root_cause_comment

    @root_cause_comment.setter
    def root_cause_comment(self, root_cause_comment):
        r"""Sets the root_cause_comment of this CocTicketDetailInfoResponseData.

        问题单根因分析。

        :param root_cause_comment: The root_cause_comment of this CocTicketDetailInfoResponseData.
        :type root_cause_comment: str
        """
        self._root_cause_comment = root_cause_comment

    @property
    def solution(self):
        r"""Gets the solution of this CocTicketDetailInfoResponseData.

        问题单解决方案。

        :return: The solution of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        r"""Sets the solution of this CocTicketDetailInfoResponseData.

        问题单解决方案。

        :param solution: The solution of this CocTicketDetailInfoResponseData.
        :type solution: str
        """
        self._solution = solution

    @property
    def regions_serch(self):
        r"""Gets the regions_serch of this CocTicketDetailInfoResponseData.

        问题单区域搜索。

        :return: The regions_serch of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._regions_serch

    @regions_serch.setter
    def regions_serch(self, regions_serch):
        r"""Sets the regions_serch of this CocTicketDetailInfoResponseData.

        问题单区域搜索。

        :param regions_serch: The regions_serch of this CocTicketDetailInfoResponseData.
        :type regions_serch: str
        """
        self._regions_serch = regions_serch

    @property
    def level_approve_config(self):
        r"""Gets the level_approve_config of this CocTicketDetailInfoResponseData.

        问题单级别审批配置。

        :return: The level_approve_config of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._level_approve_config

    @level_approve_config.setter
    def level_approve_config(self, level_approve_config):
        r"""Sets the level_approve_config of this CocTicketDetailInfoResponseData.

        问题单级别审批配置。

        :param level_approve_config: The level_approve_config of this CocTicketDetailInfoResponseData.
        :type level_approve_config: str
        """
        self._level_approve_config = level_approve_config

    @property
    def suspension_approve_config(self):
        r"""Gets the suspension_approve_config of this CocTicketDetailInfoResponseData.

        问题单挂起审批配置。

        :return: The suspension_approve_config of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._suspension_approve_config

    @suspension_approve_config.setter
    def suspension_approve_config(self, suspension_approve_config):
        r"""Sets the suspension_approve_config of this CocTicketDetailInfoResponseData.

        问题单挂起审批配置。

        :param suspension_approve_config: The suspension_approve_config of this CocTicketDetailInfoResponseData.
        :type suspension_approve_config: str
        """
        self._suspension_approve_config = suspension_approve_config

    @property
    def handle_time(self):
        r"""Gets the handle_time of this CocTicketDetailInfoResponseData.

        处理时长。

        :return: The handle_time of this CocTicketDetailInfoResponseData.
        :rtype: int
        """
        return self._handle_time

    @handle_time.setter
    def handle_time(self, handle_time):
        r"""Sets the handle_time of this CocTicketDetailInfoResponseData.

        处理时长。

        :param handle_time: The handle_time of this CocTicketDetailInfoResponseData.
        :type handle_time: int
        """
        self._handle_time = handle_time

    @property
    def fount_time(self):
        r"""Gets the fount_time of this CocTicketDetailInfoResponseData.

        发现时间。

        :return: The fount_time of this CocTicketDetailInfoResponseData.
        :rtype: int
        """
        return self._fount_time

    @fount_time.setter
    def fount_time(self, fount_time):
        r"""Sets the fount_time of this CocTicketDetailInfoResponseData.

        发现时间。

        :param fount_time: The fount_time of this CocTicketDetailInfoResponseData.
        :type fount_time: int
        """
        self._fount_time = fount_time

    @property
    def is_common_issue(self):
        r"""Gets the is_common_issue of this CocTicketDetailInfoResponseData.

        是否共性问题。

        :return: The is_common_issue of this CocTicketDetailInfoResponseData.
        :rtype: bool
        """
        return self._is_common_issue

    @is_common_issue.setter
    def is_common_issue(self, is_common_issue):
        r"""Sets the is_common_issue of this CocTicketDetailInfoResponseData.

        是否共性问题。

        :param is_common_issue: The is_common_issue of this CocTicketDetailInfoResponseData.
        :type is_common_issue: bool
        """
        self._is_common_issue = is_common_issue

    @property
    def is_need_change(self):
        r"""Gets the is_need_change of this CocTicketDetailInfoResponseData.

        问题单是否需要变更。

        :return: The is_need_change of this CocTicketDetailInfoResponseData.
        :rtype: bool
        """
        return self._is_need_change

    @is_need_change.setter
    def is_need_change(self, is_need_change):
        r"""Sets the is_need_change of this CocTicketDetailInfoResponseData.

        问题单是否需要变更。

        :param is_need_change: The is_need_change of this CocTicketDetailInfoResponseData.
        :type is_need_change: bool
        """
        self._is_need_change = is_need_change

    @property
    def is_enable_suspension(self):
        r"""Gets the is_enable_suspension of this CocTicketDetailInfoResponseData.

        问题单是否开启挂起。

        :return: The is_enable_suspension of this CocTicketDetailInfoResponseData.
        :rtype: bool
        """
        return self._is_enable_suspension

    @is_enable_suspension.setter
    def is_enable_suspension(self, is_enable_suspension):
        r"""Sets the is_enable_suspension of this CocTicketDetailInfoResponseData.

        问题单是否开启挂起。

        :param is_enable_suspension: The is_enable_suspension of this CocTicketDetailInfoResponseData.
        :type is_enable_suspension: bool
        """
        self._is_enable_suspension = is_enable_suspension

    @property
    def is_start_process_async(self):
        r"""Gets the is_start_process_async of this CocTicketDetailInfoResponseData.

        是否启动异步流程。

        :return: The is_start_process_async of this CocTicketDetailInfoResponseData.
        :rtype: bool
        """
        return self._is_start_process_async

    @is_start_process_async.setter
    def is_start_process_async(self, is_start_process_async):
        r"""Sets the is_start_process_async of this CocTicketDetailInfoResponseData.

        是否启动异步流程。

        :param is_start_process_async: The is_start_process_async of this CocTicketDetailInfoResponseData.
        :type is_start_process_async: bool
        """
        self._is_start_process_async = is_start_process_async

    @property
    def is_update_null(self):
        r"""Gets the is_update_null of this CocTicketDetailInfoResponseData.

        是否重新提交空字段。

        :return: The is_update_null of this CocTicketDetailInfoResponseData.
        :rtype: bool
        """
        return self._is_update_null

    @is_update_null.setter
    def is_update_null(self, is_update_null):
        r"""Sets the is_update_null of this CocTicketDetailInfoResponseData.

        是否重新提交空字段。

        :param is_update_null: The is_update_null of this CocTicketDetailInfoResponseData.
        :type is_update_null: bool
        """
        self._is_update_null = is_update_null

    @property
    def creator(self):
        r"""Gets the creator of this CocTicketDetailInfoResponseData.

        问题单创建人。

        :return: The creator of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this CocTicketDetailInfoResponseData.

        问题单创建人。

        :param creator: The creator of this CocTicketDetailInfoResponseData.
        :type creator: str
        """
        self._creator = creator

    @property
    def operator(self):
        r"""Gets the operator of this CocTicketDetailInfoResponseData.

        问题单操作人。

        :return: The operator of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this CocTicketDetailInfoResponseData.

        问题单操作人。

        :param operator: The operator of this CocTicketDetailInfoResponseData.
        :type operator: str
        """
        self._operator = operator

    @property
    def is_return_full_info(self):
        r"""Gets the is_return_full_info of this CocTicketDetailInfoResponseData.

        是否返回所有字段信息。

        :return: The is_return_full_info of this CocTicketDetailInfoResponseData.
        :rtype: bool
        """
        return self._is_return_full_info

    @is_return_full_info.setter
    def is_return_full_info(self, is_return_full_info):
        r"""Sets the is_return_full_info of this CocTicketDetailInfoResponseData.

        是否返回所有字段信息。

        :param is_return_full_info: The is_return_full_info of this CocTicketDetailInfoResponseData.
        :type is_return_full_info: bool
        """
        self._is_return_full_info = is_return_full_info

    @property
    def is_start_process(self):
        r"""Gets the is_start_process of this CocTicketDetailInfoResponseData.

        是否启动流程。

        :return: The is_start_process of this CocTicketDetailInfoResponseData.
        :rtype: bool
        """
        return self._is_start_process

    @is_start_process.setter
    def is_start_process(self, is_start_process):
        r"""Sets the is_start_process of this CocTicketDetailInfoResponseData.

        是否启动流程。

        :param is_start_process: The is_start_process of this CocTicketDetailInfoResponseData.
        :type is_start_process: bool
        """
        self._is_start_process = is_start_process

    @property
    def ticket_id(self):
        r"""Gets the ticket_id of this CocTicketDetailInfoResponseData.

        问题单工单ID。

        :return: The ticket_id of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        r"""Sets the ticket_id of this CocTicketDetailInfoResponseData.

        问题单工单ID。

        :param ticket_id: The ticket_id of this CocTicketDetailInfoResponseData.
        :type ticket_id: str
        """
        self._ticket_id = ticket_id

    @property
    def real_ticket_id(self):
        r"""Gets the real_ticket_id of this CocTicketDetailInfoResponseData.

        问题单工单单号。

        :return: The real_ticket_id of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._real_ticket_id

    @real_ticket_id.setter
    def real_ticket_id(self, real_ticket_id):
        r"""Sets the real_ticket_id of this CocTicketDetailInfoResponseData.

        问题单工单单号。

        :param real_ticket_id: The real_ticket_id of this CocTicketDetailInfoResponseData.
        :type real_ticket_id: str
        """
        self._real_ticket_id = real_ticket_id

    @property
    def assignee(self):
        r"""Gets the assignee of this CocTicketDetailInfoResponseData.

        问题单当前责任人。

        :return: The assignee of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this CocTicketDetailInfoResponseData.

        问题单当前责任人。

        :param assignee: The assignee of this CocTicketDetailInfoResponseData.
        :type assignee: str
        """
        self._assignee = assignee

    @property
    def participator(self):
        r"""Gets the participator of this CocTicketDetailInfoResponseData.

        问题单参与人。

        :return: The participator of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._participator

    @participator.setter
    def participator(self, participator):
        r"""Sets the participator of this CocTicketDetailInfoResponseData.

        问题单参与人。

        :param participator: The participator of this CocTicketDetailInfoResponseData.
        :type participator: str
        """
        self._participator = participator

    @property
    def work_flow_status(self):
        r"""Gets the work_flow_status of this CocTicketDetailInfoResponseData.

        问题单状态。

        :return: The work_flow_status of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._work_flow_status

    @work_flow_status.setter
    def work_flow_status(self, work_flow_status):
        r"""Sets the work_flow_status of this CocTicketDetailInfoResponseData.

        问题单状态。

        :param work_flow_status: The work_flow_status of this CocTicketDetailInfoResponseData.
        :type work_flow_status: str
        """
        self._work_flow_status = work_flow_status

    @property
    def engine_error_msg(self):
        r"""Gets the engine_error_msg of this CocTicketDetailInfoResponseData.

        流程状态。

        :return: The engine_error_msg of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._engine_error_msg

    @engine_error_msg.setter
    def engine_error_msg(self, engine_error_msg):
        r"""Sets the engine_error_msg of this CocTicketDetailInfoResponseData.

        流程状态。

        :param engine_error_msg: The engine_error_msg of this CocTicketDetailInfoResponseData.
        :type engine_error_msg: str
        """
        self._engine_error_msg = engine_error_msg

    @property
    def baseline_status(self):
        r"""Gets the baseline_status of this CocTicketDetailInfoResponseData.

        基线状态。

        :return: The baseline_status of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._baseline_status

    @baseline_status.setter
    def baseline_status(self, baseline_status):
        r"""Sets the baseline_status of this CocTicketDetailInfoResponseData.

        基线状态。

        :param baseline_status: The baseline_status of this CocTicketDetailInfoResponseData.
        :type baseline_status: str
        """
        self._baseline_status = baseline_status

    @property
    def ticket_type(self):
        r"""Gets the ticket_type of this CocTicketDetailInfoResponseData.

        工单类型。

        :return: The ticket_type of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, ticket_type):
        r"""Sets the ticket_type of this CocTicketDetailInfoResponseData.

        工单类型。

        :param ticket_type: The ticket_type of this CocTicketDetailInfoResponseData.
        :type ticket_type: str
        """
        self._ticket_type = ticket_type

    @property
    def phase(self):
        r"""Gets the phase of this CocTicketDetailInfoResponseData.

        问题单当前阶段信息。

        :return: The phase of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this CocTicketDetailInfoResponseData.

        问题单当前阶段信息。

        :param phase: The phase of this CocTicketDetailInfoResponseData.
        :type phase: str
        """
        self._phase = phase

    @property
    def sub_tickets(self):
        r"""Gets the sub_tickets of this CocTicketDetailInfoResponseData.

        变更子单信息。

        :return: The sub_tickets of this CocTicketDetailInfoResponseData.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.CocTicketDetailInfoResponseDataSubTickets`]
        """
        return self._sub_tickets

    @sub_tickets.setter
    def sub_tickets(self, sub_tickets):
        r"""Sets the sub_tickets of this CocTicketDetailInfoResponseData.

        变更子单信息。

        :param sub_tickets: The sub_tickets of this CocTicketDetailInfoResponseData.
        :type sub_tickets: list[:class:`huaweicloudsdkcoc.v1.CocTicketDetailInfoResponseDataSubTickets`]
        """
        self._sub_tickets = sub_tickets

    @property
    def enum_data_list(self):
        r"""Gets the enum_data_list of this CocTicketDetailInfoResponseData.

        枚举列表。

        :return: The enum_data_list of this CocTicketDetailInfoResponseData.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.IssuesTicketInfoEnumData`]
        """
        return self._enum_data_list

    @enum_data_list.setter
    def enum_data_list(self, enum_data_list):
        r"""Sets the enum_data_list of this CocTicketDetailInfoResponseData.

        枚举列表。

        :param enum_data_list: The enum_data_list of this CocTicketDetailInfoResponseData.
        :type enum_data_list: list[:class:`huaweicloudsdkcoc.v1.IssuesTicketInfoEnumData`]
        """
        self._enum_data_list = enum_data_list

    @property
    def id(self):
        r"""Gets the id of this CocTicketDetailInfoResponseData.

        主键uuid

        :return: The id of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CocTicketDetailInfoResponseData.

        主键uuid

        :param id: The id of this CocTicketDetailInfoResponseData.
        :type id: str
        """
        self._id = id

    @property
    def meta_data_version(self):
        r"""Gets the meta_data_version of this CocTicketDetailInfoResponseData.

        应用版本

        :return: The meta_data_version of this CocTicketDetailInfoResponseData.
        :rtype: int
        """
        return self._meta_data_version

    @meta_data_version.setter
    def meta_data_version(self, meta_data_version):
        r"""Sets the meta_data_version of this CocTicketDetailInfoResponseData.

        应用版本

        :param meta_data_version: The meta_data_version of this CocTicketDetailInfoResponseData.
        :type meta_data_version: int
        """
        self._meta_data_version = meta_data_version

    @property
    def update_time(self):
        r"""Gets the update_time of this CocTicketDetailInfoResponseData.

        更新时间。

        :return: The update_time of this CocTicketDetailInfoResponseData.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CocTicketDetailInfoResponseData.

        更新时间。

        :param update_time: The update_time of this CocTicketDetailInfoResponseData.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def create_time(self):
        r"""Gets the create_time of this CocTicketDetailInfoResponseData.

        创单时间戳。

        :return: The create_time of this CocTicketDetailInfoResponseData.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CocTicketDetailInfoResponseData.

        创单时间戳。

        :param create_time: The create_time of this CocTicketDetailInfoResponseData.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def is_deleted(self):
        r"""Gets the is_deleted of this CocTicketDetailInfoResponseData.

        工单是否被删除。

        :return: The is_deleted of this CocTicketDetailInfoResponseData.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        r"""Sets the is_deleted of this CocTicketDetailInfoResponseData.

        工单是否被删除。

        :param is_deleted: The is_deleted of this CocTicketDetailInfoResponseData.
        :type is_deleted: bool
        """
        self._is_deleted = is_deleted

    @property
    def ticket_type_id(self):
        r"""Gets the ticket_type_id of this CocTicketDetailInfoResponseData.

        工单类型。

        :return: The ticket_type_id of this CocTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._ticket_type_id

    @ticket_type_id.setter
    def ticket_type_id(self, ticket_type_id):
        r"""Sets the ticket_type_id of this CocTicketDetailInfoResponseData.

        工单类型。

        :param ticket_type_id: The ticket_type_id of this CocTicketDetailInfoResponseData.
        :type ticket_type_id: str
        """
        self._ticket_type_id = ticket_type_id

    @property
    def form_info(self):
        r"""Gets the form_info of this CocTicketDetailInfoResponseData.

        动作信息。

        :return: The form_info of this CocTicketDetailInfoResponseData.
        :rtype: object
        """
        return self._form_info

    @form_info.setter
    def form_info(self, form_info):
        r"""Sets the form_info of this CocTicketDetailInfoResponseData.

        动作信息。

        :param form_info: The form_info of this CocTicketDetailInfoResponseData.
        :type form_info: object
        """
        self._form_info = form_info

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
        if not isinstance(other, CocTicketDetailInfoResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
