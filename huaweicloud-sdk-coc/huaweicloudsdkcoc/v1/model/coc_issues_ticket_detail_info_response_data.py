# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CocIssuesTicketDetailInfoResponseData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ticket_type': 'str',
        'level': 'str',
        'impacted_cloud_services': 'str',
        'root_cause_cloud_service': 'str',
        'root_cause_type': 'str',
        'root_cause_comment': 'str',
        'solution': 'str',
        'issue_contact_person': 'str',
        'reproduce_probability': 'str',
        'issue_version': 'str',
        'title': 'str',
        'virtual_schedule_type': 'str',
        'regions': 'str',
        'description': 'str',
        'fount_time': 'int',
        'is_common_issue': 'bool',
        'is_need_change': 'bool',
        'creator': 'str',
        'operator': 'str',
        'ticket_id': 'str',
        'assignee': 'str',
        'work_flow_status': 'str',
        'phase': 'str',
        'update_time': 'int',
        'create_time': 'int',
        'is_deleted': 'bool',
        'enum_data_list': 'list[TicketInfoEnumData]'
    }

    attribute_map = {
        'ticket_type': 'ticket_type',
        'level': 'level',
        'impacted_cloud_services': 'impacted_cloud_services',
        'root_cause_cloud_service': 'root_cause_cloud_service',
        'root_cause_type': 'root_cause_type',
        'root_cause_comment': 'root_cause_comment',
        'solution': 'solution',
        'issue_contact_person': 'issue_contact_person',
        'reproduce_probability': 'reproduce_probability',
        'issue_version': 'issue_version',
        'title': 'title',
        'virtual_schedule_type': 'virtual_schedule_type',
        'regions': 'regions',
        'description': 'description',
        'fount_time': 'fount_time',
        'is_common_issue': 'is_common_issue',
        'is_need_change': 'is_need_change',
        'creator': 'creator',
        'operator': 'operator',
        'ticket_id': 'ticket_id',
        'assignee': 'assignee',
        'work_flow_status': 'work_flow_status',
        'phase': 'phase',
        'update_time': 'update_time',
        'create_time': 'create_time',
        'is_deleted': 'is_deleted',
        'enum_data_list': 'enum_data_list'
    }

    def __init__(self, ticket_type=None, level=None, impacted_cloud_services=None, root_cause_cloud_service=None, root_cause_type=None, root_cause_comment=None, solution=None, issue_contact_person=None, reproduce_probability=None, issue_version=None, title=None, virtual_schedule_type=None, regions=None, description=None, fount_time=None, is_common_issue=None, is_need_change=None, creator=None, operator=None, ticket_id=None, assignee=None, work_flow_status=None, phase=None, update_time=None, create_time=None, is_deleted=None, enum_data_list=None):
        r"""CocIssuesTicketDetailInfoResponseData

        The model defined in huaweicloud sdk

        :param ticket_type: 问题类型
        :type ticket_type: str
        :param level: 问题等级
        :type level: str
        :param impacted_cloud_services: 影响服务
        :type impacted_cloud_services: str
        :param root_cause_cloud_service: 责任服务
        :type root_cause_cloud_service: str
        :param root_cause_type: 根因类型
        :type root_cause_type: str
        :param root_cause_comment: 根因分析
        :type root_cause_comment: str
        :param solution: 解决方案
        :type solution: str
        :param issue_contact_person: 问题接口人id
        :type issue_contact_person: str
        :param reproduce_probability: 重现概率
        :type reproduce_probability: str
        :param issue_version: 发现问题的版本号
        :type issue_version: str
        :param title: 问题标题
        :type title: str
        :param virtual_schedule_type: 排班类型
        :type virtual_schedule_type: str
        :param regions: 区域
        :type regions: str
        :param description: 描述
        :type description: str
        :param fount_time: 发现时间
        :type fount_time: int
        :param is_common_issue: 是否共性问题
        :type is_common_issue: bool
        :param is_need_change: 是否需要变更
        :type is_need_change: bool
        :param creator: 创建人
        :type creator: str
        :param operator: 操作人
        :type operator: str
        :param ticket_id: 问题单id
        :type ticket_id: str
        :param assignee: 责任人
        :type assignee: str
        :param work_flow_status: 问题单状态
        :type work_flow_status: str
        :param phase: 阶段
        :type phase: str
        :param update_time: 更新时间
        :type update_time: int
        :param create_time: 创建时间
        :type create_time: int
        :param is_deleted: 是否删除
        :type is_deleted: bool
        :param enum_data_list: 枚举列表
        :type enum_data_list: list[:class:`huaweicloudsdkcoc.v1.TicketInfoEnumData`]
        """
        
        

        self._ticket_type = None
        self._level = None
        self._impacted_cloud_services = None
        self._root_cause_cloud_service = None
        self._root_cause_type = None
        self._root_cause_comment = None
        self._solution = None
        self._issue_contact_person = None
        self._reproduce_probability = None
        self._issue_version = None
        self._title = None
        self._virtual_schedule_type = None
        self._regions = None
        self._description = None
        self._fount_time = None
        self._is_common_issue = None
        self._is_need_change = None
        self._creator = None
        self._operator = None
        self._ticket_id = None
        self._assignee = None
        self._work_flow_status = None
        self._phase = None
        self._update_time = None
        self._create_time = None
        self._is_deleted = None
        self._enum_data_list = None
        self.discriminator = None

        if ticket_type is not None:
            self.ticket_type = ticket_type
        if level is not None:
            self.level = level
        if impacted_cloud_services is not None:
            self.impacted_cloud_services = impacted_cloud_services
        if root_cause_cloud_service is not None:
            self.root_cause_cloud_service = root_cause_cloud_service
        if root_cause_type is not None:
            self.root_cause_type = root_cause_type
        if root_cause_comment is not None:
            self.root_cause_comment = root_cause_comment
        if solution is not None:
            self.solution = solution
        if issue_contact_person is not None:
            self.issue_contact_person = issue_contact_person
        if reproduce_probability is not None:
            self.reproduce_probability = reproduce_probability
        if issue_version is not None:
            self.issue_version = issue_version
        if title is not None:
            self.title = title
        if virtual_schedule_type is not None:
            self.virtual_schedule_type = virtual_schedule_type
        if regions is not None:
            self.regions = regions
        if description is not None:
            self.description = description
        if fount_time is not None:
            self.fount_time = fount_time
        if is_common_issue is not None:
            self.is_common_issue = is_common_issue
        if is_need_change is not None:
            self.is_need_change = is_need_change
        if creator is not None:
            self.creator = creator
        if operator is not None:
            self.operator = operator
        if ticket_id is not None:
            self.ticket_id = ticket_id
        if assignee is not None:
            self.assignee = assignee
        if work_flow_status is not None:
            self.work_flow_status = work_flow_status
        if phase is not None:
            self.phase = phase
        if update_time is not None:
            self.update_time = update_time
        if create_time is not None:
            self.create_time = create_time
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if enum_data_list is not None:
            self.enum_data_list = enum_data_list

    @property
    def ticket_type(self):
        r"""Gets the ticket_type of this CocIssuesTicketDetailInfoResponseData.

        问题类型

        :return: The ticket_type of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, ticket_type):
        r"""Sets the ticket_type of this CocIssuesTicketDetailInfoResponseData.

        问题类型

        :param ticket_type: The ticket_type of this CocIssuesTicketDetailInfoResponseData.
        :type ticket_type: str
        """
        self._ticket_type = ticket_type

    @property
    def level(self):
        r"""Gets the level of this CocIssuesTicketDetailInfoResponseData.

        问题等级

        :return: The level of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this CocIssuesTicketDetailInfoResponseData.

        问题等级

        :param level: The level of this CocIssuesTicketDetailInfoResponseData.
        :type level: str
        """
        self._level = level

    @property
    def impacted_cloud_services(self):
        r"""Gets the impacted_cloud_services of this CocIssuesTicketDetailInfoResponseData.

        影响服务

        :return: The impacted_cloud_services of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._impacted_cloud_services

    @impacted_cloud_services.setter
    def impacted_cloud_services(self, impacted_cloud_services):
        r"""Sets the impacted_cloud_services of this CocIssuesTicketDetailInfoResponseData.

        影响服务

        :param impacted_cloud_services: The impacted_cloud_services of this CocIssuesTicketDetailInfoResponseData.
        :type impacted_cloud_services: str
        """
        self._impacted_cloud_services = impacted_cloud_services

    @property
    def root_cause_cloud_service(self):
        r"""Gets the root_cause_cloud_service of this CocIssuesTicketDetailInfoResponseData.

        责任服务

        :return: The root_cause_cloud_service of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._root_cause_cloud_service

    @root_cause_cloud_service.setter
    def root_cause_cloud_service(self, root_cause_cloud_service):
        r"""Sets the root_cause_cloud_service of this CocIssuesTicketDetailInfoResponseData.

        责任服务

        :param root_cause_cloud_service: The root_cause_cloud_service of this CocIssuesTicketDetailInfoResponseData.
        :type root_cause_cloud_service: str
        """
        self._root_cause_cloud_service = root_cause_cloud_service

    @property
    def root_cause_type(self):
        r"""Gets the root_cause_type of this CocIssuesTicketDetailInfoResponseData.

        根因类型

        :return: The root_cause_type of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._root_cause_type

    @root_cause_type.setter
    def root_cause_type(self, root_cause_type):
        r"""Sets the root_cause_type of this CocIssuesTicketDetailInfoResponseData.

        根因类型

        :param root_cause_type: The root_cause_type of this CocIssuesTicketDetailInfoResponseData.
        :type root_cause_type: str
        """
        self._root_cause_type = root_cause_type

    @property
    def root_cause_comment(self):
        r"""Gets the root_cause_comment of this CocIssuesTicketDetailInfoResponseData.

        根因分析

        :return: The root_cause_comment of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._root_cause_comment

    @root_cause_comment.setter
    def root_cause_comment(self, root_cause_comment):
        r"""Sets the root_cause_comment of this CocIssuesTicketDetailInfoResponseData.

        根因分析

        :param root_cause_comment: The root_cause_comment of this CocIssuesTicketDetailInfoResponseData.
        :type root_cause_comment: str
        """
        self._root_cause_comment = root_cause_comment

    @property
    def solution(self):
        r"""Gets the solution of this CocIssuesTicketDetailInfoResponseData.

        解决方案

        :return: The solution of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        r"""Sets the solution of this CocIssuesTicketDetailInfoResponseData.

        解决方案

        :param solution: The solution of this CocIssuesTicketDetailInfoResponseData.
        :type solution: str
        """
        self._solution = solution

    @property
    def issue_contact_person(self):
        r"""Gets the issue_contact_person of this CocIssuesTicketDetailInfoResponseData.

        问题接口人id

        :return: The issue_contact_person of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._issue_contact_person

    @issue_contact_person.setter
    def issue_contact_person(self, issue_contact_person):
        r"""Sets the issue_contact_person of this CocIssuesTicketDetailInfoResponseData.

        问题接口人id

        :param issue_contact_person: The issue_contact_person of this CocIssuesTicketDetailInfoResponseData.
        :type issue_contact_person: str
        """
        self._issue_contact_person = issue_contact_person

    @property
    def reproduce_probability(self):
        r"""Gets the reproduce_probability of this CocIssuesTicketDetailInfoResponseData.

        重现概率

        :return: The reproduce_probability of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._reproduce_probability

    @reproduce_probability.setter
    def reproduce_probability(self, reproduce_probability):
        r"""Sets the reproduce_probability of this CocIssuesTicketDetailInfoResponseData.

        重现概率

        :param reproduce_probability: The reproduce_probability of this CocIssuesTicketDetailInfoResponseData.
        :type reproduce_probability: str
        """
        self._reproduce_probability = reproduce_probability

    @property
    def issue_version(self):
        r"""Gets the issue_version of this CocIssuesTicketDetailInfoResponseData.

        发现问题的版本号

        :return: The issue_version of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._issue_version

    @issue_version.setter
    def issue_version(self, issue_version):
        r"""Sets the issue_version of this CocIssuesTicketDetailInfoResponseData.

        发现问题的版本号

        :param issue_version: The issue_version of this CocIssuesTicketDetailInfoResponseData.
        :type issue_version: str
        """
        self._issue_version = issue_version

    @property
    def title(self):
        r"""Gets the title of this CocIssuesTicketDetailInfoResponseData.

        问题标题

        :return: The title of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CocIssuesTicketDetailInfoResponseData.

        问题标题

        :param title: The title of this CocIssuesTicketDetailInfoResponseData.
        :type title: str
        """
        self._title = title

    @property
    def virtual_schedule_type(self):
        r"""Gets the virtual_schedule_type of this CocIssuesTicketDetailInfoResponseData.

        排班类型

        :return: The virtual_schedule_type of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._virtual_schedule_type

    @virtual_schedule_type.setter
    def virtual_schedule_type(self, virtual_schedule_type):
        r"""Sets the virtual_schedule_type of this CocIssuesTicketDetailInfoResponseData.

        排班类型

        :param virtual_schedule_type: The virtual_schedule_type of this CocIssuesTicketDetailInfoResponseData.
        :type virtual_schedule_type: str
        """
        self._virtual_schedule_type = virtual_schedule_type

    @property
    def regions(self):
        r"""Gets the regions of this CocIssuesTicketDetailInfoResponseData.

        区域

        :return: The regions of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        r"""Sets the regions of this CocIssuesTicketDetailInfoResponseData.

        区域

        :param regions: The regions of this CocIssuesTicketDetailInfoResponseData.
        :type regions: str
        """
        self._regions = regions

    @property
    def description(self):
        r"""Gets the description of this CocIssuesTicketDetailInfoResponseData.

        描述

        :return: The description of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CocIssuesTicketDetailInfoResponseData.

        描述

        :param description: The description of this CocIssuesTicketDetailInfoResponseData.
        :type description: str
        """
        self._description = description

    @property
    def fount_time(self):
        r"""Gets the fount_time of this CocIssuesTicketDetailInfoResponseData.

        发现时间

        :return: The fount_time of this CocIssuesTicketDetailInfoResponseData.
        :rtype: int
        """
        return self._fount_time

    @fount_time.setter
    def fount_time(self, fount_time):
        r"""Sets the fount_time of this CocIssuesTicketDetailInfoResponseData.

        发现时间

        :param fount_time: The fount_time of this CocIssuesTicketDetailInfoResponseData.
        :type fount_time: int
        """
        self._fount_time = fount_time

    @property
    def is_common_issue(self):
        r"""Gets the is_common_issue of this CocIssuesTicketDetailInfoResponseData.

        是否共性问题

        :return: The is_common_issue of this CocIssuesTicketDetailInfoResponseData.
        :rtype: bool
        """
        return self._is_common_issue

    @is_common_issue.setter
    def is_common_issue(self, is_common_issue):
        r"""Sets the is_common_issue of this CocIssuesTicketDetailInfoResponseData.

        是否共性问题

        :param is_common_issue: The is_common_issue of this CocIssuesTicketDetailInfoResponseData.
        :type is_common_issue: bool
        """
        self._is_common_issue = is_common_issue

    @property
    def is_need_change(self):
        r"""Gets the is_need_change of this CocIssuesTicketDetailInfoResponseData.

        是否需要变更

        :return: The is_need_change of this CocIssuesTicketDetailInfoResponseData.
        :rtype: bool
        """
        return self._is_need_change

    @is_need_change.setter
    def is_need_change(self, is_need_change):
        r"""Sets the is_need_change of this CocIssuesTicketDetailInfoResponseData.

        是否需要变更

        :param is_need_change: The is_need_change of this CocIssuesTicketDetailInfoResponseData.
        :type is_need_change: bool
        """
        self._is_need_change = is_need_change

    @property
    def creator(self):
        r"""Gets the creator of this CocIssuesTicketDetailInfoResponseData.

        创建人

        :return: The creator of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this CocIssuesTicketDetailInfoResponseData.

        创建人

        :param creator: The creator of this CocIssuesTicketDetailInfoResponseData.
        :type creator: str
        """
        self._creator = creator

    @property
    def operator(self):
        r"""Gets the operator of this CocIssuesTicketDetailInfoResponseData.

        操作人

        :return: The operator of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this CocIssuesTicketDetailInfoResponseData.

        操作人

        :param operator: The operator of this CocIssuesTicketDetailInfoResponseData.
        :type operator: str
        """
        self._operator = operator

    @property
    def ticket_id(self):
        r"""Gets the ticket_id of this CocIssuesTicketDetailInfoResponseData.

        问题单id

        :return: The ticket_id of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        r"""Sets the ticket_id of this CocIssuesTicketDetailInfoResponseData.

        问题单id

        :param ticket_id: The ticket_id of this CocIssuesTicketDetailInfoResponseData.
        :type ticket_id: str
        """
        self._ticket_id = ticket_id

    @property
    def assignee(self):
        r"""Gets the assignee of this CocIssuesTicketDetailInfoResponseData.

        责任人

        :return: The assignee of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this CocIssuesTicketDetailInfoResponseData.

        责任人

        :param assignee: The assignee of this CocIssuesTicketDetailInfoResponseData.
        :type assignee: str
        """
        self._assignee = assignee

    @property
    def work_flow_status(self):
        r"""Gets the work_flow_status of this CocIssuesTicketDetailInfoResponseData.

        问题单状态

        :return: The work_flow_status of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._work_flow_status

    @work_flow_status.setter
    def work_flow_status(self, work_flow_status):
        r"""Sets the work_flow_status of this CocIssuesTicketDetailInfoResponseData.

        问题单状态

        :param work_flow_status: The work_flow_status of this CocIssuesTicketDetailInfoResponseData.
        :type work_flow_status: str
        """
        self._work_flow_status = work_flow_status

    @property
    def phase(self):
        r"""Gets the phase of this CocIssuesTicketDetailInfoResponseData.

        阶段

        :return: The phase of this CocIssuesTicketDetailInfoResponseData.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this CocIssuesTicketDetailInfoResponseData.

        阶段

        :param phase: The phase of this CocIssuesTicketDetailInfoResponseData.
        :type phase: str
        """
        self._phase = phase

    @property
    def update_time(self):
        r"""Gets the update_time of this CocIssuesTicketDetailInfoResponseData.

        更新时间

        :return: The update_time of this CocIssuesTicketDetailInfoResponseData.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CocIssuesTicketDetailInfoResponseData.

        更新时间

        :param update_time: The update_time of this CocIssuesTicketDetailInfoResponseData.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def create_time(self):
        r"""Gets the create_time of this CocIssuesTicketDetailInfoResponseData.

        创建时间

        :return: The create_time of this CocIssuesTicketDetailInfoResponseData.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CocIssuesTicketDetailInfoResponseData.

        创建时间

        :param create_time: The create_time of this CocIssuesTicketDetailInfoResponseData.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def is_deleted(self):
        r"""Gets the is_deleted of this CocIssuesTicketDetailInfoResponseData.

        是否删除

        :return: The is_deleted of this CocIssuesTicketDetailInfoResponseData.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        r"""Sets the is_deleted of this CocIssuesTicketDetailInfoResponseData.

        是否删除

        :param is_deleted: The is_deleted of this CocIssuesTicketDetailInfoResponseData.
        :type is_deleted: bool
        """
        self._is_deleted = is_deleted

    @property
    def enum_data_list(self):
        r"""Gets the enum_data_list of this CocIssuesTicketDetailInfoResponseData.

        枚举列表

        :return: The enum_data_list of this CocIssuesTicketDetailInfoResponseData.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.TicketInfoEnumData`]
        """
        return self._enum_data_list

    @enum_data_list.setter
    def enum_data_list(self, enum_data_list):
        r"""Sets the enum_data_list of this CocIssuesTicketDetailInfoResponseData.

        枚举列表

        :param enum_data_list: The enum_data_list of this CocIssuesTicketDetailInfoResponseData.
        :type enum_data_list: list[:class:`huaweicloudsdkcoc.v1.TicketInfoEnumData`]
        """
        self._enum_data_list = enum_data_list

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
        if not isinstance(other, CocIssuesTicketDetailInfoResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
