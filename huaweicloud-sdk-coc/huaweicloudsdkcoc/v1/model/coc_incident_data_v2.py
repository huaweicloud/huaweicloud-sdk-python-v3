# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CocIncidentDataV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_cloud_service_id': 'str',
        'level_id': 'str',
        'mtm_region': 'str',
        'source_id': 'str',
        'forward_rule_id': 'str',
        'enterprise_project_id': 'str',
        'mtm_type': 'str',
        'title': 'str',
        'description': 'str',
        'ticket_id': 'str',
        'is_service_interrupt': 'str',
        'work_flow_status': 'str',
        'phase': 'str',
        'assignee': 'str',
        'creator': 'str',
        'operator': 'str',
        'update_time': 'str',
        'create_time': 'str',
        'start_time': 'str',
        'handle_time': 'str',
        'incident_ownership': 'str',
        'enum_data_list': 'list[CocTicketInfoEnumDataV2]'
    }

    attribute_map = {
        'current_cloud_service_id': 'current_cloud_service_id',
        'level_id': 'level_id',
        'mtm_region': 'mtm_region',
        'source_id': 'source_id',
        'forward_rule_id': 'forward_rule_id',
        'enterprise_project_id': 'enterprise_project_id',
        'mtm_type': 'mtm_type',
        'title': 'title',
        'description': 'description',
        'ticket_id': 'ticket_id',
        'is_service_interrupt': 'is_service_interrupt',
        'work_flow_status': 'work_flow_status',
        'phase': 'phase',
        'assignee': 'assignee',
        'creator': 'creator',
        'operator': 'operator',
        'update_time': 'update_time',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'handle_time': 'handle_time',
        'incident_ownership': 'incident_ownership',
        'enum_data_list': 'enum_data_list'
    }

    def __init__(self, current_cloud_service_id=None, level_id=None, mtm_region=None, source_id=None, forward_rule_id=None, enterprise_project_id=None, mtm_type=None, title=None, description=None, ticket_id=None, is_service_interrupt=None, work_flow_status=None, phase=None, assignee=None, creator=None, operator=None, update_time=None, create_time=None, start_time=None, handle_time=None, incident_ownership=None, enum_data_list=None):
        r"""CocIncidentDataV2

        The model defined in huaweicloud sdk

        :param current_cloud_service_id: 云服务
        :type current_cloud_service_id: str
        :param level_id: 事件等级
        :type level_id: str
        :param mtm_region: 区域Region
        :type mtm_region: str
        :param source_id: 事件来源
        :type source_id: str
        :param forward_rule_id: 转发规则
        :type forward_rule_id: str
        :param enterprise_project_id: 企业应用
        :type enterprise_project_id: str
        :param mtm_type: 事件类别
        :type mtm_type: str
        :param title: 事件标题
        :type title: str
        :param description: 事件描述
        :type description: str
        :param ticket_id: 事件单号
        :type ticket_id: str
        :param is_service_interrupt: 服务是否中断
        :type is_service_interrupt: str
        :param work_flow_status: 流程状态
        :type work_flow_status: str
        :param phase: 阶段
        :type phase: str
        :param assignee: 责任人
        :type assignee: str
        :param creator: 创建人
        :type creator: str
        :param operator: 创建人
        :type operator: str
        :param update_time: 更新时间
        :type update_time: str
        :param create_time: 创建时间
        :type create_time: str
        :param start_time: 故障开始时间
        :type start_time: str
        :param handle_time: 最近一次处理时间
        :type handle_time: str
        :param incident_ownership: 事件归属
        :type incident_ownership: str
        :param enum_data_list: 枚举列表
        :type enum_data_list: list[:class:`huaweicloudsdkcoc.v1.CocTicketInfoEnumDataV2`]
        """
        
        

        self._current_cloud_service_id = None
        self._level_id = None
        self._mtm_region = None
        self._source_id = None
        self._forward_rule_id = None
        self._enterprise_project_id = None
        self._mtm_type = None
        self._title = None
        self._description = None
        self._ticket_id = None
        self._is_service_interrupt = None
        self._work_flow_status = None
        self._phase = None
        self._assignee = None
        self._creator = None
        self._operator = None
        self._update_time = None
        self._create_time = None
        self._start_time = None
        self._handle_time = None
        self._incident_ownership = None
        self._enum_data_list = None
        self.discriminator = None

        if current_cloud_service_id is not None:
            self.current_cloud_service_id = current_cloud_service_id
        if level_id is not None:
            self.level_id = level_id
        if mtm_region is not None:
            self.mtm_region = mtm_region
        if source_id is not None:
            self.source_id = source_id
        if forward_rule_id is not None:
            self.forward_rule_id = forward_rule_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if mtm_type is not None:
            self.mtm_type = mtm_type
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if ticket_id is not None:
            self.ticket_id = ticket_id
        if is_service_interrupt is not None:
            self.is_service_interrupt = is_service_interrupt
        if work_flow_status is not None:
            self.work_flow_status = work_flow_status
        if phase is not None:
            self.phase = phase
        if assignee is not None:
            self.assignee = assignee
        if creator is not None:
            self.creator = creator
        if operator is not None:
            self.operator = operator
        if update_time is not None:
            self.update_time = update_time
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if handle_time is not None:
            self.handle_time = handle_time
        if incident_ownership is not None:
            self.incident_ownership = incident_ownership
        if enum_data_list is not None:
            self.enum_data_list = enum_data_list

    @property
    def current_cloud_service_id(self):
        r"""Gets the current_cloud_service_id of this CocIncidentDataV2.

        云服务

        :return: The current_cloud_service_id of this CocIncidentDataV2.
        :rtype: str
        """
        return self._current_cloud_service_id

    @current_cloud_service_id.setter
    def current_cloud_service_id(self, current_cloud_service_id):
        r"""Sets the current_cloud_service_id of this CocIncidentDataV2.

        云服务

        :param current_cloud_service_id: The current_cloud_service_id of this CocIncidentDataV2.
        :type current_cloud_service_id: str
        """
        self._current_cloud_service_id = current_cloud_service_id

    @property
    def level_id(self):
        r"""Gets the level_id of this CocIncidentDataV2.

        事件等级

        :return: The level_id of this CocIncidentDataV2.
        :rtype: str
        """
        return self._level_id

    @level_id.setter
    def level_id(self, level_id):
        r"""Sets the level_id of this CocIncidentDataV2.

        事件等级

        :param level_id: The level_id of this CocIncidentDataV2.
        :type level_id: str
        """
        self._level_id = level_id

    @property
    def mtm_region(self):
        r"""Gets the mtm_region of this CocIncidentDataV2.

        区域Region

        :return: The mtm_region of this CocIncidentDataV2.
        :rtype: str
        """
        return self._mtm_region

    @mtm_region.setter
    def mtm_region(self, mtm_region):
        r"""Sets the mtm_region of this CocIncidentDataV2.

        区域Region

        :param mtm_region: The mtm_region of this CocIncidentDataV2.
        :type mtm_region: str
        """
        self._mtm_region = mtm_region

    @property
    def source_id(self):
        r"""Gets the source_id of this CocIncidentDataV2.

        事件来源

        :return: The source_id of this CocIncidentDataV2.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this CocIncidentDataV2.

        事件来源

        :param source_id: The source_id of this CocIncidentDataV2.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def forward_rule_id(self):
        r"""Gets the forward_rule_id of this CocIncidentDataV2.

        转发规则

        :return: The forward_rule_id of this CocIncidentDataV2.
        :rtype: str
        """
        return self._forward_rule_id

    @forward_rule_id.setter
    def forward_rule_id(self, forward_rule_id):
        r"""Sets the forward_rule_id of this CocIncidentDataV2.

        转发规则

        :param forward_rule_id: The forward_rule_id of this CocIncidentDataV2.
        :type forward_rule_id: str
        """
        self._forward_rule_id = forward_rule_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CocIncidentDataV2.

        企业应用

        :return: The enterprise_project_id of this CocIncidentDataV2.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CocIncidentDataV2.

        企业应用

        :param enterprise_project_id: The enterprise_project_id of this CocIncidentDataV2.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def mtm_type(self):
        r"""Gets the mtm_type of this CocIncidentDataV2.

        事件类别

        :return: The mtm_type of this CocIncidentDataV2.
        :rtype: str
        """
        return self._mtm_type

    @mtm_type.setter
    def mtm_type(self, mtm_type):
        r"""Sets the mtm_type of this CocIncidentDataV2.

        事件类别

        :param mtm_type: The mtm_type of this CocIncidentDataV2.
        :type mtm_type: str
        """
        self._mtm_type = mtm_type

    @property
    def title(self):
        r"""Gets the title of this CocIncidentDataV2.

        事件标题

        :return: The title of this CocIncidentDataV2.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CocIncidentDataV2.

        事件标题

        :param title: The title of this CocIncidentDataV2.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this CocIncidentDataV2.

        事件描述

        :return: The description of this CocIncidentDataV2.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CocIncidentDataV2.

        事件描述

        :param description: The description of this CocIncidentDataV2.
        :type description: str
        """
        self._description = description

    @property
    def ticket_id(self):
        r"""Gets the ticket_id of this CocIncidentDataV2.

        事件单号

        :return: The ticket_id of this CocIncidentDataV2.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        r"""Sets the ticket_id of this CocIncidentDataV2.

        事件单号

        :param ticket_id: The ticket_id of this CocIncidentDataV2.
        :type ticket_id: str
        """
        self._ticket_id = ticket_id

    @property
    def is_service_interrupt(self):
        r"""Gets the is_service_interrupt of this CocIncidentDataV2.

        服务是否中断

        :return: The is_service_interrupt of this CocIncidentDataV2.
        :rtype: str
        """
        return self._is_service_interrupt

    @is_service_interrupt.setter
    def is_service_interrupt(self, is_service_interrupt):
        r"""Sets the is_service_interrupt of this CocIncidentDataV2.

        服务是否中断

        :param is_service_interrupt: The is_service_interrupt of this CocIncidentDataV2.
        :type is_service_interrupt: str
        """
        self._is_service_interrupt = is_service_interrupt

    @property
    def work_flow_status(self):
        r"""Gets the work_flow_status of this CocIncidentDataV2.

        流程状态

        :return: The work_flow_status of this CocIncidentDataV2.
        :rtype: str
        """
        return self._work_flow_status

    @work_flow_status.setter
    def work_flow_status(self, work_flow_status):
        r"""Sets the work_flow_status of this CocIncidentDataV2.

        流程状态

        :param work_flow_status: The work_flow_status of this CocIncidentDataV2.
        :type work_flow_status: str
        """
        self._work_flow_status = work_flow_status

    @property
    def phase(self):
        r"""Gets the phase of this CocIncidentDataV2.

        阶段

        :return: The phase of this CocIncidentDataV2.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this CocIncidentDataV2.

        阶段

        :param phase: The phase of this CocIncidentDataV2.
        :type phase: str
        """
        self._phase = phase

    @property
    def assignee(self):
        r"""Gets the assignee of this CocIncidentDataV2.

        责任人

        :return: The assignee of this CocIncidentDataV2.
        :rtype: str
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this CocIncidentDataV2.

        责任人

        :param assignee: The assignee of this CocIncidentDataV2.
        :type assignee: str
        """
        self._assignee = assignee

    @property
    def creator(self):
        r"""Gets the creator of this CocIncidentDataV2.

        创建人

        :return: The creator of this CocIncidentDataV2.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this CocIncidentDataV2.

        创建人

        :param creator: The creator of this CocIncidentDataV2.
        :type creator: str
        """
        self._creator = creator

    @property
    def operator(self):
        r"""Gets the operator of this CocIncidentDataV2.

        创建人

        :return: The operator of this CocIncidentDataV2.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this CocIncidentDataV2.

        创建人

        :param operator: The operator of this CocIncidentDataV2.
        :type operator: str
        """
        self._operator = operator

    @property
    def update_time(self):
        r"""Gets the update_time of this CocIncidentDataV2.

        更新时间

        :return: The update_time of this CocIncidentDataV2.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CocIncidentDataV2.

        更新时间

        :param update_time: The update_time of this CocIncidentDataV2.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def create_time(self):
        r"""Gets the create_time of this CocIncidentDataV2.

        创建时间

        :return: The create_time of this CocIncidentDataV2.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CocIncidentDataV2.

        创建时间

        :param create_time: The create_time of this CocIncidentDataV2.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def start_time(self):
        r"""Gets the start_time of this CocIncidentDataV2.

        故障开始时间

        :return: The start_time of this CocIncidentDataV2.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CocIncidentDataV2.

        故障开始时间

        :param start_time: The start_time of this CocIncidentDataV2.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def handle_time(self):
        r"""Gets the handle_time of this CocIncidentDataV2.

        最近一次处理时间

        :return: The handle_time of this CocIncidentDataV2.
        :rtype: str
        """
        return self._handle_time

    @handle_time.setter
    def handle_time(self, handle_time):
        r"""Sets the handle_time of this CocIncidentDataV2.

        最近一次处理时间

        :param handle_time: The handle_time of this CocIncidentDataV2.
        :type handle_time: str
        """
        self._handle_time = handle_time

    @property
    def incident_ownership(self):
        r"""Gets the incident_ownership of this CocIncidentDataV2.

        事件归属

        :return: The incident_ownership of this CocIncidentDataV2.
        :rtype: str
        """
        return self._incident_ownership

    @incident_ownership.setter
    def incident_ownership(self, incident_ownership):
        r"""Sets the incident_ownership of this CocIncidentDataV2.

        事件归属

        :param incident_ownership: The incident_ownership of this CocIncidentDataV2.
        :type incident_ownership: str
        """
        self._incident_ownership = incident_ownership

    @property
    def enum_data_list(self):
        r"""Gets the enum_data_list of this CocIncidentDataV2.

        枚举列表

        :return: The enum_data_list of this CocIncidentDataV2.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.CocTicketInfoEnumDataV2`]
        """
        return self._enum_data_list

    @enum_data_list.setter
    def enum_data_list(self, enum_data_list):
        r"""Sets the enum_data_list of this CocIncidentDataV2.

        枚举列表

        :param enum_data_list: The enum_data_list of this CocIncidentDataV2.
        :type enum_data_list: list[:class:`huaweicloudsdkcoc.v1.CocTicketInfoEnumDataV2`]
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
        if not isinstance(other, CocIncidentDataV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
