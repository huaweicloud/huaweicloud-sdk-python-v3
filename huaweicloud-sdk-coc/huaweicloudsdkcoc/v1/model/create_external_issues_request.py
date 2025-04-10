# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateExternalIssuesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creator': 'str',
        'title': 'str',
        'description': 'str',
        'regions': 'list[str]',
        'enterprise_project': 'str',
        'source': 'str',
        'source_id': 'str',
        'fount_time': 'int',
        'impacted_cloud_services': 'list[str]',
        'level': 'str',
        'ticket_type': 'str',
        'reproduce_probability': 'str',
        'root_cause_cloud_service': 'list[str]',
        'virtual_schedule_type': 'str',
        'schedule_scenes': 'str',
        'virtual_schedule_role': 'str',
        'issue_contact_person': 'str'
    }

    attribute_map = {
        'creator': 'creator',
        'title': 'title',
        'description': 'description',
        'regions': 'regions',
        'enterprise_project': 'enterprise_project',
        'source': 'source',
        'source_id': 'source_id',
        'fount_time': 'fount_time',
        'impacted_cloud_services': 'impacted_cloud_services',
        'level': 'level',
        'ticket_type': 'ticket_type',
        'reproduce_probability': 'reproduce_probability',
        'root_cause_cloud_service': 'root_cause_cloud_service',
        'virtual_schedule_type': 'virtual_schedule_type',
        'schedule_scenes': 'schedule_scenes',
        'virtual_schedule_role': 'virtual_schedule_role',
        'issue_contact_person': 'issue_contact_person'
    }

    def __init__(self, creator=None, title=None, description=None, regions=None, enterprise_project=None, source=None, source_id=None, fount_time=None, impacted_cloud_services=None, level=None, ticket_type=None, reproduce_probability=None, root_cause_cloud_service=None, virtual_schedule_type=None, schedule_scenes=None, virtual_schedule_role=None, issue_contact_person=None):
        r"""CreateExternalIssuesRequest

        The model defined in huaweicloud sdk

        :param creator: 创建人id
        :type creator: str
        :param title: 标题
        :type title: str
        :param description: 描述
        :type description: str
        :param regions: 区域Code,最大100个
        :type regions: list[str]
        :param enterprise_project: 企业项目id
        :type enterprise_project: str
        :param source: 问题来源 issues_source_1000 事件 issues_source_2000 Warroom issues_source_3000 告警
        :type source: str
        :param source_id: 问题来源id
        :type source_id: str
        :param fount_time: 发现时间
        :type fount_time: int
        :param impacted_cloud_services: 影响应用ID，最多10条
        :type impacted_cloud_services: list[str]
        :param level: 问题级别 issues_level_1000 致命 issues_level_2000 严重 issues_level_3000 一般
        :type level: str
        :param ticket_type: 问题类型 issues_type_1000  功能性问题 issues_type_2000  性能问题 issues_type_3000  可靠性问题 issues_type_4000  兼容性问题 issues_type_5000  用户体验问题 issues_type_6000  可维护性问题 issues_type_7000  变更类问题 issues_type_8000  安全问题 issues_type_9000  工程实施类 issues_type_10000 交付部署问题 issues_type_11000 LLD规划问题 issues_type_12000 供用商问题 issues_type_13000 咨询类问题 issues_type_14000 需求类问题 issues_type_15000 其他问题
        :type ticket_type: str
        :param reproduce_probability: 重现概率 issues_reproduce_probability_1000 有条件必现 issues_reproduce_probability_2000 有条件概率重现 issues_reproduce_probability_3000 无规律重现 issues_reproduce_probability_4000 很难重现
        :type reproduce_probability: str
        :param root_cause_cloud_service: 责任应用ID，必填,限1条
        :type root_cause_cloud_service: list[str]
        :param virtual_schedule_type: 排班类型 参考：枚举 issues_mgmt_virtual_schedule_type_1000 排班,schedule_scenes排班场景,virtual_schedule_role排班角色必填,指定排班 issues_mgmt_virtual_schedule_type_2000 个人,issue_contact_person字段必填,指定责任人
        :type virtual_schedule_type: str
        :param schedule_scenes: 排班场景id
        :type schedule_scenes: str
        :param virtual_schedule_role: 排班角色id
        :type virtual_schedule_role: str
        :param issue_contact_person: 问题责任人id
        :type issue_contact_person: str
        """
        
        

        self._creator = None
        self._title = None
        self._description = None
        self._regions = None
        self._enterprise_project = None
        self._source = None
        self._source_id = None
        self._fount_time = None
        self._impacted_cloud_services = None
        self._level = None
        self._ticket_type = None
        self._reproduce_probability = None
        self._root_cause_cloud_service = None
        self._virtual_schedule_type = None
        self._schedule_scenes = None
        self._virtual_schedule_role = None
        self._issue_contact_person = None
        self.discriminator = None

        if creator is not None:
            self.creator = creator
        self.title = title
        self.description = description
        if regions is not None:
            self.regions = regions
        if enterprise_project is not None:
            self.enterprise_project = enterprise_project
        if source is not None:
            self.source = source
        if source_id is not None:
            self.source_id = source_id
        if fount_time is not None:
            self.fount_time = fount_time
        self.impacted_cloud_services = impacted_cloud_services
        self.level = level
        self.ticket_type = ticket_type
        self.reproduce_probability = reproduce_probability
        self.root_cause_cloud_service = root_cause_cloud_service
        self.virtual_schedule_type = virtual_schedule_type
        if schedule_scenes is not None:
            self.schedule_scenes = schedule_scenes
        if virtual_schedule_role is not None:
            self.virtual_schedule_role = virtual_schedule_role
        if issue_contact_person is not None:
            self.issue_contact_person = issue_contact_person

    @property
    def creator(self):
        r"""Gets the creator of this CreateExternalIssuesRequest.

        创建人id

        :return: The creator of this CreateExternalIssuesRequest.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this CreateExternalIssuesRequest.

        创建人id

        :param creator: The creator of this CreateExternalIssuesRequest.
        :type creator: str
        """
        self._creator = creator

    @property
    def title(self):
        r"""Gets the title of this CreateExternalIssuesRequest.

        标题

        :return: The title of this CreateExternalIssuesRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CreateExternalIssuesRequest.

        标题

        :param title: The title of this CreateExternalIssuesRequest.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this CreateExternalIssuesRequest.

        描述

        :return: The description of this CreateExternalIssuesRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateExternalIssuesRequest.

        描述

        :param description: The description of this CreateExternalIssuesRequest.
        :type description: str
        """
        self._description = description

    @property
    def regions(self):
        r"""Gets the regions of this CreateExternalIssuesRequest.

        区域Code,最大100个

        :return: The regions of this CreateExternalIssuesRequest.
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        r"""Sets the regions of this CreateExternalIssuesRequest.

        区域Code,最大100个

        :param regions: The regions of this CreateExternalIssuesRequest.
        :type regions: list[str]
        """
        self._regions = regions

    @property
    def enterprise_project(self):
        r"""Gets the enterprise_project of this CreateExternalIssuesRequest.

        企业项目id

        :return: The enterprise_project of this CreateExternalIssuesRequest.
        :rtype: str
        """
        return self._enterprise_project

    @enterprise_project.setter
    def enterprise_project(self, enterprise_project):
        r"""Sets the enterprise_project of this CreateExternalIssuesRequest.

        企业项目id

        :param enterprise_project: The enterprise_project of this CreateExternalIssuesRequest.
        :type enterprise_project: str
        """
        self._enterprise_project = enterprise_project

    @property
    def source(self):
        r"""Gets the source of this CreateExternalIssuesRequest.

        问题来源 issues_source_1000 事件 issues_source_2000 Warroom issues_source_3000 告警

        :return: The source of this CreateExternalIssuesRequest.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CreateExternalIssuesRequest.

        问题来源 issues_source_1000 事件 issues_source_2000 Warroom issues_source_3000 告警

        :param source: The source of this CreateExternalIssuesRequest.
        :type source: str
        """
        self._source = source

    @property
    def source_id(self):
        r"""Gets the source_id of this CreateExternalIssuesRequest.

        问题来源id

        :return: The source_id of this CreateExternalIssuesRequest.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this CreateExternalIssuesRequest.

        问题来源id

        :param source_id: The source_id of this CreateExternalIssuesRequest.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def fount_time(self):
        r"""Gets the fount_time of this CreateExternalIssuesRequest.

        发现时间

        :return: The fount_time of this CreateExternalIssuesRequest.
        :rtype: int
        """
        return self._fount_time

    @fount_time.setter
    def fount_time(self, fount_time):
        r"""Sets the fount_time of this CreateExternalIssuesRequest.

        发现时间

        :param fount_time: The fount_time of this CreateExternalIssuesRequest.
        :type fount_time: int
        """
        self._fount_time = fount_time

    @property
    def impacted_cloud_services(self):
        r"""Gets the impacted_cloud_services of this CreateExternalIssuesRequest.

        影响应用ID，最多10条

        :return: The impacted_cloud_services of this CreateExternalIssuesRequest.
        :rtype: list[str]
        """
        return self._impacted_cloud_services

    @impacted_cloud_services.setter
    def impacted_cloud_services(self, impacted_cloud_services):
        r"""Sets the impacted_cloud_services of this CreateExternalIssuesRequest.

        影响应用ID，最多10条

        :param impacted_cloud_services: The impacted_cloud_services of this CreateExternalIssuesRequest.
        :type impacted_cloud_services: list[str]
        """
        self._impacted_cloud_services = impacted_cloud_services

    @property
    def level(self):
        r"""Gets the level of this CreateExternalIssuesRequest.

        问题级别 issues_level_1000 致命 issues_level_2000 严重 issues_level_3000 一般

        :return: The level of this CreateExternalIssuesRequest.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this CreateExternalIssuesRequest.

        问题级别 issues_level_1000 致命 issues_level_2000 严重 issues_level_3000 一般

        :param level: The level of this CreateExternalIssuesRequest.
        :type level: str
        """
        self._level = level

    @property
    def ticket_type(self):
        r"""Gets the ticket_type of this CreateExternalIssuesRequest.

        问题类型 issues_type_1000  功能性问题 issues_type_2000  性能问题 issues_type_3000  可靠性问题 issues_type_4000  兼容性问题 issues_type_5000  用户体验问题 issues_type_6000  可维护性问题 issues_type_7000  变更类问题 issues_type_8000  安全问题 issues_type_9000  工程实施类 issues_type_10000 交付部署问题 issues_type_11000 LLD规划问题 issues_type_12000 供用商问题 issues_type_13000 咨询类问题 issues_type_14000 需求类问题 issues_type_15000 其他问题

        :return: The ticket_type of this CreateExternalIssuesRequest.
        :rtype: str
        """
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, ticket_type):
        r"""Sets the ticket_type of this CreateExternalIssuesRequest.

        问题类型 issues_type_1000  功能性问题 issues_type_2000  性能问题 issues_type_3000  可靠性问题 issues_type_4000  兼容性问题 issues_type_5000  用户体验问题 issues_type_6000  可维护性问题 issues_type_7000  变更类问题 issues_type_8000  安全问题 issues_type_9000  工程实施类 issues_type_10000 交付部署问题 issues_type_11000 LLD规划问题 issues_type_12000 供用商问题 issues_type_13000 咨询类问题 issues_type_14000 需求类问题 issues_type_15000 其他问题

        :param ticket_type: The ticket_type of this CreateExternalIssuesRequest.
        :type ticket_type: str
        """
        self._ticket_type = ticket_type

    @property
    def reproduce_probability(self):
        r"""Gets the reproduce_probability of this CreateExternalIssuesRequest.

        重现概率 issues_reproduce_probability_1000 有条件必现 issues_reproduce_probability_2000 有条件概率重现 issues_reproduce_probability_3000 无规律重现 issues_reproduce_probability_4000 很难重现

        :return: The reproduce_probability of this CreateExternalIssuesRequest.
        :rtype: str
        """
        return self._reproduce_probability

    @reproduce_probability.setter
    def reproduce_probability(self, reproduce_probability):
        r"""Sets the reproduce_probability of this CreateExternalIssuesRequest.

        重现概率 issues_reproduce_probability_1000 有条件必现 issues_reproduce_probability_2000 有条件概率重现 issues_reproduce_probability_3000 无规律重现 issues_reproduce_probability_4000 很难重现

        :param reproduce_probability: The reproduce_probability of this CreateExternalIssuesRequest.
        :type reproduce_probability: str
        """
        self._reproduce_probability = reproduce_probability

    @property
    def root_cause_cloud_service(self):
        r"""Gets the root_cause_cloud_service of this CreateExternalIssuesRequest.

        责任应用ID，必填,限1条

        :return: The root_cause_cloud_service of this CreateExternalIssuesRequest.
        :rtype: list[str]
        """
        return self._root_cause_cloud_service

    @root_cause_cloud_service.setter
    def root_cause_cloud_service(self, root_cause_cloud_service):
        r"""Sets the root_cause_cloud_service of this CreateExternalIssuesRequest.

        责任应用ID，必填,限1条

        :param root_cause_cloud_service: The root_cause_cloud_service of this CreateExternalIssuesRequest.
        :type root_cause_cloud_service: list[str]
        """
        self._root_cause_cloud_service = root_cause_cloud_service

    @property
    def virtual_schedule_type(self):
        r"""Gets the virtual_schedule_type of this CreateExternalIssuesRequest.

        排班类型 参考：枚举 issues_mgmt_virtual_schedule_type_1000 排班,schedule_scenes排班场景,virtual_schedule_role排班角色必填,指定排班 issues_mgmt_virtual_schedule_type_2000 个人,issue_contact_person字段必填,指定责任人

        :return: The virtual_schedule_type of this CreateExternalIssuesRequest.
        :rtype: str
        """
        return self._virtual_schedule_type

    @virtual_schedule_type.setter
    def virtual_schedule_type(self, virtual_schedule_type):
        r"""Sets the virtual_schedule_type of this CreateExternalIssuesRequest.

        排班类型 参考：枚举 issues_mgmt_virtual_schedule_type_1000 排班,schedule_scenes排班场景,virtual_schedule_role排班角色必填,指定排班 issues_mgmt_virtual_schedule_type_2000 个人,issue_contact_person字段必填,指定责任人

        :param virtual_schedule_type: The virtual_schedule_type of this CreateExternalIssuesRequest.
        :type virtual_schedule_type: str
        """
        self._virtual_schedule_type = virtual_schedule_type

    @property
    def schedule_scenes(self):
        r"""Gets the schedule_scenes of this CreateExternalIssuesRequest.

        排班场景id

        :return: The schedule_scenes of this CreateExternalIssuesRequest.
        :rtype: str
        """
        return self._schedule_scenes

    @schedule_scenes.setter
    def schedule_scenes(self, schedule_scenes):
        r"""Sets the schedule_scenes of this CreateExternalIssuesRequest.

        排班场景id

        :param schedule_scenes: The schedule_scenes of this CreateExternalIssuesRequest.
        :type schedule_scenes: str
        """
        self._schedule_scenes = schedule_scenes

    @property
    def virtual_schedule_role(self):
        r"""Gets the virtual_schedule_role of this CreateExternalIssuesRequest.

        排班角色id

        :return: The virtual_schedule_role of this CreateExternalIssuesRequest.
        :rtype: str
        """
        return self._virtual_schedule_role

    @virtual_schedule_role.setter
    def virtual_schedule_role(self, virtual_schedule_role):
        r"""Sets the virtual_schedule_role of this CreateExternalIssuesRequest.

        排班角色id

        :param virtual_schedule_role: The virtual_schedule_role of this CreateExternalIssuesRequest.
        :type virtual_schedule_role: str
        """
        self._virtual_schedule_role = virtual_schedule_role

    @property
    def issue_contact_person(self):
        r"""Gets the issue_contact_person of this CreateExternalIssuesRequest.

        问题责任人id

        :return: The issue_contact_person of this CreateExternalIssuesRequest.
        :rtype: str
        """
        return self._issue_contact_person

    @issue_contact_person.setter
    def issue_contact_person(self, issue_contact_person):
        r"""Sets the issue_contact_person of this CreateExternalIssuesRequest.

        问题责任人id

        :param issue_contact_person: The issue_contact_person of this CreateExternalIssuesRequest.
        :type issue_contact_person: str
        """
        self._issue_contact_person = issue_contact_person

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
        if not isinstance(other, CreateExternalIssuesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
