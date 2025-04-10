# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WarRoomTenantInfo:

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
        'title': 'str',
        'admin': 'str',
        'recover_member': 'list[str]',
        'recover_leader': 'list[str]',
        'incident': 'WarRoomIncident',
        'source': 'str',
        'regions': 'list[WarRoomTenantInfoRegions]',
        'change_num': 'str',
        'occur_time': 'int',
        'recover_time': 'int',
        'fault_cause': 'str',
        'create_time': 'int',
        'first_report_time': 'int',
        'recovery_notification_time': 'int',
        'fault_impact': 'str',
        'description': 'str',
        'circular_level': 'str',
        'war_room_status': 'WarRoomEnumeration',
        'impacted_application': 'list[WarRoomTenantInfoImpactedApplication]',
        'processing_duration': 'int',
        'restoration_duration': 'int',
        'war_room_num': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'admin': 'admin',
        'recover_member': 'recover_member',
        'recover_leader': 'recover_leader',
        'incident': 'incident',
        'source': 'source',
        'regions': 'regions',
        'change_num': 'change_num',
        'occur_time': 'occur_time',
        'recover_time': 'recover_time',
        'fault_cause': 'fault_cause',
        'create_time': 'create_time',
        'first_report_time': 'first_report_time',
        'recovery_notification_time': 'recovery_notification_time',
        'fault_impact': 'fault_impact',
        'description': 'description',
        'circular_level': 'circular_level',
        'war_room_status': 'war_room_status',
        'impacted_application': 'impacted_application',
        'processing_duration': 'processing_duration',
        'restoration_duration': 'restoration_duration',
        'war_room_num': 'war_room_num',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, title=None, admin=None, recover_member=None, recover_leader=None, incident=None, source=None, regions=None, change_num=None, occur_time=None, recover_time=None, fault_cause=None, create_time=None, first_report_time=None, recovery_notification_time=None, fault_impact=None, description=None, circular_level=None, war_room_status=None, impacted_application=None, processing_duration=None, restoration_duration=None, war_room_num=None, enterprise_project_id=None):
        r"""WarRoomTenantInfo

        The model defined in huaweicloud sdk

        :param id: 主键
        :type id: str
        :param title: 标题
        :type title: str
        :param admin: WarRoom管理员
        :type admin: str
        :param recover_member: 恢复成员
        :type recover_member: list[str]
        :param recover_leader: 主恢复责任人
        :type recover_leader: list[str]
        :param incident: 
        :type incident: :class:`huaweicloudsdkcoc.v1.WarRoomIncident`
        :param source: 事件来源
        :type source: str
        :param regions: 影响的Region
        :type regions: list[:class:`huaweicloudsdkcoc.v1.WarRoomTenantInfoRegions`]
        :param change_num: 变更单号
        :type change_num: str
        :param occur_time: 开始时间
        :type occur_time: int
        :param recover_time: 故障恢复时间
        :type recover_time: int
        :param fault_cause: 故障原因
        :type fault_cause: str
        :param create_time: 添加时间
        :type create_time: int
        :param first_report_time: 首次通报时间
        :type first_report_time: int
        :param recovery_notification_time: 恢复通报时间
        :type recovery_notification_time: int
        :param fault_impact: 故障影响
        :type fault_impact: str
        :param description: WarRoom描述
        :type description: str
        :param circular_level: 通报级别 租户区同事件级别
        :type circular_level: str
        :param war_room_status: 
        :type war_room_status: :class:`huaweicloudsdkcoc.v1.WarRoomEnumeration`
        :param impacted_application: 影响应用
        :type impacted_application: list[:class:`huaweicloudsdkcoc.v1.WarRoomTenantInfoImpactedApplication`]
        :param processing_duration: 处理时长(分钟)
        :type processing_duration: int
        :param restoration_duration: 恢复时长(分钟)
        :type restoration_duration: int
        :param war_room_num: WarRoom单号
        :type war_room_num: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._title = None
        self._admin = None
        self._recover_member = None
        self._recover_leader = None
        self._incident = None
        self._source = None
        self._regions = None
        self._change_num = None
        self._occur_time = None
        self._recover_time = None
        self._fault_cause = None
        self._create_time = None
        self._first_report_time = None
        self._recovery_notification_time = None
        self._fault_impact = None
        self._description = None
        self._circular_level = None
        self._war_room_status = None
        self._impacted_application = None
        self._processing_duration = None
        self._restoration_duration = None
        self._war_room_num = None
        self._enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if admin is not None:
            self.admin = admin
        if recover_member is not None:
            self.recover_member = recover_member
        if recover_leader is not None:
            self.recover_leader = recover_leader
        if incident is not None:
            self.incident = incident
        if source is not None:
            self.source = source
        if regions is not None:
            self.regions = regions
        if change_num is not None:
            self.change_num = change_num
        if occur_time is not None:
            self.occur_time = occur_time
        if recover_time is not None:
            self.recover_time = recover_time
        if fault_cause is not None:
            self.fault_cause = fault_cause
        if create_time is not None:
            self.create_time = create_time
        if first_report_time is not None:
            self.first_report_time = first_report_time
        if recovery_notification_time is not None:
            self.recovery_notification_time = recovery_notification_time
        if fault_impact is not None:
            self.fault_impact = fault_impact
        if description is not None:
            self.description = description
        if circular_level is not None:
            self.circular_level = circular_level
        if war_room_status is not None:
            self.war_room_status = war_room_status
        if impacted_application is not None:
            self.impacted_application = impacted_application
        if processing_duration is not None:
            self.processing_duration = processing_duration
        if restoration_duration is not None:
            self.restoration_duration = restoration_duration
        if war_room_num is not None:
            self.war_room_num = war_room_num
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this WarRoomTenantInfo.

        主键

        :return: The id of this WarRoomTenantInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WarRoomTenantInfo.

        主键

        :param id: The id of this WarRoomTenantInfo.
        :type id: str
        """
        self._id = id

    @property
    def title(self):
        r"""Gets the title of this WarRoomTenantInfo.

        标题

        :return: The title of this WarRoomTenantInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this WarRoomTenantInfo.

        标题

        :param title: The title of this WarRoomTenantInfo.
        :type title: str
        """
        self._title = title

    @property
    def admin(self):
        r"""Gets the admin of this WarRoomTenantInfo.

        WarRoom管理员

        :return: The admin of this WarRoomTenantInfo.
        :rtype: str
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        r"""Sets the admin of this WarRoomTenantInfo.

        WarRoom管理员

        :param admin: The admin of this WarRoomTenantInfo.
        :type admin: str
        """
        self._admin = admin

    @property
    def recover_member(self):
        r"""Gets the recover_member of this WarRoomTenantInfo.

        恢复成员

        :return: The recover_member of this WarRoomTenantInfo.
        :rtype: list[str]
        """
        return self._recover_member

    @recover_member.setter
    def recover_member(self, recover_member):
        r"""Sets the recover_member of this WarRoomTenantInfo.

        恢复成员

        :param recover_member: The recover_member of this WarRoomTenantInfo.
        :type recover_member: list[str]
        """
        self._recover_member = recover_member

    @property
    def recover_leader(self):
        r"""Gets the recover_leader of this WarRoomTenantInfo.

        主恢复责任人

        :return: The recover_leader of this WarRoomTenantInfo.
        :rtype: list[str]
        """
        return self._recover_leader

    @recover_leader.setter
    def recover_leader(self, recover_leader):
        r"""Sets the recover_leader of this WarRoomTenantInfo.

        主恢复责任人

        :param recover_leader: The recover_leader of this WarRoomTenantInfo.
        :type recover_leader: list[str]
        """
        self._recover_leader = recover_leader

    @property
    def incident(self):
        r"""Gets the incident of this WarRoomTenantInfo.

        :return: The incident of this WarRoomTenantInfo.
        :rtype: :class:`huaweicloudsdkcoc.v1.WarRoomIncident`
        """
        return self._incident

    @incident.setter
    def incident(self, incident):
        r"""Sets the incident of this WarRoomTenantInfo.

        :param incident: The incident of this WarRoomTenantInfo.
        :type incident: :class:`huaweicloudsdkcoc.v1.WarRoomIncident`
        """
        self._incident = incident

    @property
    def source(self):
        r"""Gets the source of this WarRoomTenantInfo.

        事件来源

        :return: The source of this WarRoomTenantInfo.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this WarRoomTenantInfo.

        事件来源

        :param source: The source of this WarRoomTenantInfo.
        :type source: str
        """
        self._source = source

    @property
    def regions(self):
        r"""Gets the regions of this WarRoomTenantInfo.

        影响的Region

        :return: The regions of this WarRoomTenantInfo.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.WarRoomTenantInfoRegions`]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        r"""Sets the regions of this WarRoomTenantInfo.

        影响的Region

        :param regions: The regions of this WarRoomTenantInfo.
        :type regions: list[:class:`huaweicloudsdkcoc.v1.WarRoomTenantInfoRegions`]
        """
        self._regions = regions

    @property
    def change_num(self):
        r"""Gets the change_num of this WarRoomTenantInfo.

        变更单号

        :return: The change_num of this WarRoomTenantInfo.
        :rtype: str
        """
        return self._change_num

    @change_num.setter
    def change_num(self, change_num):
        r"""Sets the change_num of this WarRoomTenantInfo.

        变更单号

        :param change_num: The change_num of this WarRoomTenantInfo.
        :type change_num: str
        """
        self._change_num = change_num

    @property
    def occur_time(self):
        r"""Gets the occur_time of this WarRoomTenantInfo.

        开始时间

        :return: The occur_time of this WarRoomTenantInfo.
        :rtype: int
        """
        return self._occur_time

    @occur_time.setter
    def occur_time(self, occur_time):
        r"""Sets the occur_time of this WarRoomTenantInfo.

        开始时间

        :param occur_time: The occur_time of this WarRoomTenantInfo.
        :type occur_time: int
        """
        self._occur_time = occur_time

    @property
    def recover_time(self):
        r"""Gets the recover_time of this WarRoomTenantInfo.

        故障恢复时间

        :return: The recover_time of this WarRoomTenantInfo.
        :rtype: int
        """
        return self._recover_time

    @recover_time.setter
    def recover_time(self, recover_time):
        r"""Sets the recover_time of this WarRoomTenantInfo.

        故障恢复时间

        :param recover_time: The recover_time of this WarRoomTenantInfo.
        :type recover_time: int
        """
        self._recover_time = recover_time

    @property
    def fault_cause(self):
        r"""Gets the fault_cause of this WarRoomTenantInfo.

        故障原因

        :return: The fault_cause of this WarRoomTenantInfo.
        :rtype: str
        """
        return self._fault_cause

    @fault_cause.setter
    def fault_cause(self, fault_cause):
        r"""Sets the fault_cause of this WarRoomTenantInfo.

        故障原因

        :param fault_cause: The fault_cause of this WarRoomTenantInfo.
        :type fault_cause: str
        """
        self._fault_cause = fault_cause

    @property
    def create_time(self):
        r"""Gets the create_time of this WarRoomTenantInfo.

        添加时间

        :return: The create_time of this WarRoomTenantInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this WarRoomTenantInfo.

        添加时间

        :param create_time: The create_time of this WarRoomTenantInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def first_report_time(self):
        r"""Gets the first_report_time of this WarRoomTenantInfo.

        首次通报时间

        :return: The first_report_time of this WarRoomTenantInfo.
        :rtype: int
        """
        return self._first_report_time

    @first_report_time.setter
    def first_report_time(self, first_report_time):
        r"""Sets the first_report_time of this WarRoomTenantInfo.

        首次通报时间

        :param first_report_time: The first_report_time of this WarRoomTenantInfo.
        :type first_report_time: int
        """
        self._first_report_time = first_report_time

    @property
    def recovery_notification_time(self):
        r"""Gets the recovery_notification_time of this WarRoomTenantInfo.

        恢复通报时间

        :return: The recovery_notification_time of this WarRoomTenantInfo.
        :rtype: int
        """
        return self._recovery_notification_time

    @recovery_notification_time.setter
    def recovery_notification_time(self, recovery_notification_time):
        r"""Sets the recovery_notification_time of this WarRoomTenantInfo.

        恢复通报时间

        :param recovery_notification_time: The recovery_notification_time of this WarRoomTenantInfo.
        :type recovery_notification_time: int
        """
        self._recovery_notification_time = recovery_notification_time

    @property
    def fault_impact(self):
        r"""Gets the fault_impact of this WarRoomTenantInfo.

        故障影响

        :return: The fault_impact of this WarRoomTenantInfo.
        :rtype: str
        """
        return self._fault_impact

    @fault_impact.setter
    def fault_impact(self, fault_impact):
        r"""Sets the fault_impact of this WarRoomTenantInfo.

        故障影响

        :param fault_impact: The fault_impact of this WarRoomTenantInfo.
        :type fault_impact: str
        """
        self._fault_impact = fault_impact

    @property
    def description(self):
        r"""Gets the description of this WarRoomTenantInfo.

        WarRoom描述

        :return: The description of this WarRoomTenantInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WarRoomTenantInfo.

        WarRoom描述

        :param description: The description of this WarRoomTenantInfo.
        :type description: str
        """
        self._description = description

    @property
    def circular_level(self):
        r"""Gets the circular_level of this WarRoomTenantInfo.

        通报级别 租户区同事件级别

        :return: The circular_level of this WarRoomTenantInfo.
        :rtype: str
        """
        return self._circular_level

    @circular_level.setter
    def circular_level(self, circular_level):
        r"""Sets the circular_level of this WarRoomTenantInfo.

        通报级别 租户区同事件级别

        :param circular_level: The circular_level of this WarRoomTenantInfo.
        :type circular_level: str
        """
        self._circular_level = circular_level

    @property
    def war_room_status(self):
        r"""Gets the war_room_status of this WarRoomTenantInfo.

        :return: The war_room_status of this WarRoomTenantInfo.
        :rtype: :class:`huaweicloudsdkcoc.v1.WarRoomEnumeration`
        """
        return self._war_room_status

    @war_room_status.setter
    def war_room_status(self, war_room_status):
        r"""Sets the war_room_status of this WarRoomTenantInfo.

        :param war_room_status: The war_room_status of this WarRoomTenantInfo.
        :type war_room_status: :class:`huaweicloudsdkcoc.v1.WarRoomEnumeration`
        """
        self._war_room_status = war_room_status

    @property
    def impacted_application(self):
        r"""Gets the impacted_application of this WarRoomTenantInfo.

        影响应用

        :return: The impacted_application of this WarRoomTenantInfo.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.WarRoomTenantInfoImpactedApplication`]
        """
        return self._impacted_application

    @impacted_application.setter
    def impacted_application(self, impacted_application):
        r"""Sets the impacted_application of this WarRoomTenantInfo.

        影响应用

        :param impacted_application: The impacted_application of this WarRoomTenantInfo.
        :type impacted_application: list[:class:`huaweicloudsdkcoc.v1.WarRoomTenantInfoImpactedApplication`]
        """
        self._impacted_application = impacted_application

    @property
    def processing_duration(self):
        r"""Gets the processing_duration of this WarRoomTenantInfo.

        处理时长(分钟)

        :return: The processing_duration of this WarRoomTenantInfo.
        :rtype: int
        """
        return self._processing_duration

    @processing_duration.setter
    def processing_duration(self, processing_duration):
        r"""Sets the processing_duration of this WarRoomTenantInfo.

        处理时长(分钟)

        :param processing_duration: The processing_duration of this WarRoomTenantInfo.
        :type processing_duration: int
        """
        self._processing_duration = processing_duration

    @property
    def restoration_duration(self):
        r"""Gets the restoration_duration of this WarRoomTenantInfo.

        恢复时长(分钟)

        :return: The restoration_duration of this WarRoomTenantInfo.
        :rtype: int
        """
        return self._restoration_duration

    @restoration_duration.setter
    def restoration_duration(self, restoration_duration):
        r"""Sets the restoration_duration of this WarRoomTenantInfo.

        恢复时长(分钟)

        :param restoration_duration: The restoration_duration of this WarRoomTenantInfo.
        :type restoration_duration: int
        """
        self._restoration_duration = restoration_duration

    @property
    def war_room_num(self):
        r"""Gets the war_room_num of this WarRoomTenantInfo.

        WarRoom单号

        :return: The war_room_num of this WarRoomTenantInfo.
        :rtype: str
        """
        return self._war_room_num

    @war_room_num.setter
    def war_room_num(self, war_room_num):
        r"""Sets the war_room_num of this WarRoomTenantInfo.

        WarRoom单号

        :param war_room_num: The war_room_num of this WarRoomTenantInfo.
        :type war_room_num: str
        """
        self._war_room_num = war_room_num

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this WarRoomTenantInfo.

        企业项目id

        :return: The enterprise_project_id of this WarRoomTenantInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this WarRoomTenantInfo.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this WarRoomTenantInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, WarRoomTenantInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
