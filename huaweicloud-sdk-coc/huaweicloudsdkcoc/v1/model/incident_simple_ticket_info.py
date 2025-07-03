# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncidentSimpleTicketInfo:

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
        'ticket_id': 'str',
        'description': 'str',
        'status': 'str',
        'level': 'str',
        'enterprise_project': 'str',
        'source': 'str',
        'creator': 'str',
        'assignee': 'list[str]'
    }

    attribute_map = {
        'title': 'title',
        'ticket_id': 'ticket_id',
        'description': 'description',
        'status': 'status',
        'level': 'level',
        'enterprise_project': 'enterprise_project',
        'source': 'source',
        'creator': 'creator',
        'assignee': 'assignee'
    }

    def __init__(self, title=None, ticket_id=None, description=None, status=None, level=None, enterprise_project=None, source=None, creator=None, assignee=None):
        r"""IncidentSimpleTicketInfo

        The model defined in huaweicloud sdk

        :param title: 事件单标题
        :type title: str
        :param ticket_id: 事件单单号
        :type ticket_id: str
        :param description: 事件单描述
        :type description: str
        :param status: 事件状态 参考：枚举 [事件状态](coc_api_04_03_001_006.xml) incident_status
        :type status: str
        :param level: 事件级别 参考：枚举 [事件级别](coc_api_04_03_001_006.xml) incident_level
        :type level: str
        :param enterprise_project: 企业项目ID
        :type enterprise_project: str
        :param source: 单据来源 参考：枚举 [事件来源](coc_api_04_03_001_006.xml) incident_source
        :type source: str
        :param creator: 创建人工号
        :type creator: str
        :param assignee: 当前责任人，可能存在多个责任人使用列表展示，内容为责任人用户ID信息
        :type assignee: list[str]
        """
        
        

        self._title = None
        self._ticket_id = None
        self._description = None
        self._status = None
        self._level = None
        self._enterprise_project = None
        self._source = None
        self._creator = None
        self._assignee = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if ticket_id is not None:
            self.ticket_id = ticket_id
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if level is not None:
            self.level = level
        if enterprise_project is not None:
            self.enterprise_project = enterprise_project
        if source is not None:
            self.source = source
        if creator is not None:
            self.creator = creator
        if assignee is not None:
            self.assignee = assignee

    @property
    def title(self):
        r"""Gets the title of this IncidentSimpleTicketInfo.

        事件单标题

        :return: The title of this IncidentSimpleTicketInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this IncidentSimpleTicketInfo.

        事件单标题

        :param title: The title of this IncidentSimpleTicketInfo.
        :type title: str
        """
        self._title = title

    @property
    def ticket_id(self):
        r"""Gets the ticket_id of this IncidentSimpleTicketInfo.

        事件单单号

        :return: The ticket_id of this IncidentSimpleTicketInfo.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        r"""Sets the ticket_id of this IncidentSimpleTicketInfo.

        事件单单号

        :param ticket_id: The ticket_id of this IncidentSimpleTicketInfo.
        :type ticket_id: str
        """
        self._ticket_id = ticket_id

    @property
    def description(self):
        r"""Gets the description of this IncidentSimpleTicketInfo.

        事件单描述

        :return: The description of this IncidentSimpleTicketInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IncidentSimpleTicketInfo.

        事件单描述

        :param description: The description of this IncidentSimpleTicketInfo.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this IncidentSimpleTicketInfo.

        事件状态 参考：枚举 [事件状态](coc_api_04_03_001_006.xml) incident_status

        :return: The status of this IncidentSimpleTicketInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IncidentSimpleTicketInfo.

        事件状态 参考：枚举 [事件状态](coc_api_04_03_001_006.xml) incident_status

        :param status: The status of this IncidentSimpleTicketInfo.
        :type status: str
        """
        self._status = status

    @property
    def level(self):
        r"""Gets the level of this IncidentSimpleTicketInfo.

        事件级别 参考：枚举 [事件级别](coc_api_04_03_001_006.xml) incident_level

        :return: The level of this IncidentSimpleTicketInfo.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this IncidentSimpleTicketInfo.

        事件级别 参考：枚举 [事件级别](coc_api_04_03_001_006.xml) incident_level

        :param level: The level of this IncidentSimpleTicketInfo.
        :type level: str
        """
        self._level = level

    @property
    def enterprise_project(self):
        r"""Gets the enterprise_project of this IncidentSimpleTicketInfo.

        企业项目ID

        :return: The enterprise_project of this IncidentSimpleTicketInfo.
        :rtype: str
        """
        return self._enterprise_project

    @enterprise_project.setter
    def enterprise_project(self, enterprise_project):
        r"""Sets the enterprise_project of this IncidentSimpleTicketInfo.

        企业项目ID

        :param enterprise_project: The enterprise_project of this IncidentSimpleTicketInfo.
        :type enterprise_project: str
        """
        self._enterprise_project = enterprise_project

    @property
    def source(self):
        r"""Gets the source of this IncidentSimpleTicketInfo.

        单据来源 参考：枚举 [事件来源](coc_api_04_03_001_006.xml) incident_source

        :return: The source of this IncidentSimpleTicketInfo.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this IncidentSimpleTicketInfo.

        单据来源 参考：枚举 [事件来源](coc_api_04_03_001_006.xml) incident_source

        :param source: The source of this IncidentSimpleTicketInfo.
        :type source: str
        """
        self._source = source

    @property
    def creator(self):
        r"""Gets the creator of this IncidentSimpleTicketInfo.

        创建人工号

        :return: The creator of this IncidentSimpleTicketInfo.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this IncidentSimpleTicketInfo.

        创建人工号

        :param creator: The creator of this IncidentSimpleTicketInfo.
        :type creator: str
        """
        self._creator = creator

    @property
    def assignee(self):
        r"""Gets the assignee of this IncidentSimpleTicketInfo.

        当前责任人，可能存在多个责任人使用列表展示，内容为责任人用户ID信息

        :return: The assignee of this IncidentSimpleTicketInfo.
        :rtype: list[str]
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this IncidentSimpleTicketInfo.

        当前责任人，可能存在多个责任人使用列表展示，内容为责任人用户ID信息

        :param assignee: The assignee of this IncidentSimpleTicketInfo.
        :type assignee: list[str]
        """
        self._assignee = assignee

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
        if not isinstance(other, IncidentSimpleTicketInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
