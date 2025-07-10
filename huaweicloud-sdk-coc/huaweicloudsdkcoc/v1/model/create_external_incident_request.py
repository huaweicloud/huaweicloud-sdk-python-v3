# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateExternalIncidentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'list[str]',
        'enterprise_project': 'list[str]',
        'current_cloud_service': 'list[str]',
        'incident_level': 'str',
        'is_service_interrupt': 'bool',
        'incident_type': 'str',
        'incident_title': 'str',
        'incident_description': 'str',
        'incident_source': 'str',
        'incident_assignee': 'list[str]',
        'assignee_scene': 'str',
        'assignee_role': 'str',
        'creator': 'str',
        'incident_ownership': 'str',
        'start_time': 'int'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project': 'enterprise_project',
        'current_cloud_service': 'current_cloud_service',
        'incident_level': 'incident_level',
        'is_service_interrupt': 'is_service_interrupt',
        'incident_type': 'incident_type',
        'incident_title': 'incident_title',
        'incident_description': 'incident_description',
        'incident_source': 'incident_source',
        'incident_assignee': 'incident_assignee',
        'assignee_scene': 'assignee_scene',
        'assignee_role': 'assignee_role',
        'creator': 'creator',
        'incident_ownership': 'incident_ownership',
        'start_time': 'start_time'
    }

    def __init__(self, region=None, enterprise_project=None, current_cloud_service=None, incident_level=None, is_service_interrupt=None, incident_type=None, incident_title=None, incident_description=None, incident_source=None, incident_assignee=None, assignee_scene=None, assignee_role=None, creator=None, incident_ownership=None, start_time=None):
        r"""CreateExternalIncidentRequest

        The model defined in huaweicloud sdk

        :param region: 区域Code，如果自动拉起WarRoom则为必填，现在只支持1个
        :type region: list[str]
        :param enterprise_project: 企业项目ID，现在只支持1个
        :type enterprise_project: list[str]
        :param current_cloud_service: 归属应用ID，现在只支持1个
        :type current_cloud_service: list[str]
        :param incident_level: 事件级别 参考：枚举 事件级别incident_level
        :type incident_level: str
        :param is_service_interrupt: 业务是否中断，取值：true/false
        :type is_service_interrupt: bool
        :param incident_type: 事件类别 参考：枚举 事件类别incident_type
        :type incident_type: str
        :param incident_title: 事件标题，最大长度：200
        :type incident_title: str
        :param incident_description: 事件描述，最大长度：600
        :type incident_description: str
        :param incident_source: 单据来源 参考：枚举 事件来源incident_source
        :type incident_source: str
        :param incident_assignee: 责任人，排班场景和排班角色不能同时为空，现在只支持1个
        :type incident_assignee: list[str]
        :param assignee_scene: 排班场景，责任人和排班角色不能同时为空
        :type assignee_scene: str
        :param assignee_role: 排班角色，排班场景和责任人不能同时为空
        :type assignee_role: str
        :param creator: 创单人
        :type creator: str
        :param incident_ownership: 事件归属
        :type incident_ownership: str
        :param start_time: 故障发生时间戳
        :type start_time: int
        """
        
        

        self._region = None
        self._enterprise_project = None
        self._current_cloud_service = None
        self._incident_level = None
        self._is_service_interrupt = None
        self._incident_type = None
        self._incident_title = None
        self._incident_description = None
        self._incident_source = None
        self._incident_assignee = None
        self._assignee_scene = None
        self._assignee_role = None
        self._creator = None
        self._incident_ownership = None
        self._start_time = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project is not None:
            self.enterprise_project = enterprise_project
        if current_cloud_service is not None:
            self.current_cloud_service = current_cloud_service
        self.incident_level = incident_level
        self.is_service_interrupt = is_service_interrupt
        self.incident_type = incident_type
        self.incident_title = incident_title
        if incident_description is not None:
            self.incident_description = incident_description
        self.incident_source = incident_source
        if incident_assignee is not None:
            self.incident_assignee = incident_assignee
        if assignee_scene is not None:
            self.assignee_scene = assignee_scene
        if assignee_role is not None:
            self.assignee_role = assignee_role
        self.creator = creator
        if incident_ownership is not None:
            self.incident_ownership = incident_ownership
        if start_time is not None:
            self.start_time = start_time

    @property
    def region(self):
        r"""Gets the region of this CreateExternalIncidentRequest.

        区域Code，如果自动拉起WarRoom则为必填，现在只支持1个

        :return: The region of this CreateExternalIncidentRequest.
        :rtype: list[str]
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CreateExternalIncidentRequest.

        区域Code，如果自动拉起WarRoom则为必填，现在只支持1个

        :param region: The region of this CreateExternalIncidentRequest.
        :type region: list[str]
        """
        self._region = region

    @property
    def enterprise_project(self):
        r"""Gets the enterprise_project of this CreateExternalIncidentRequest.

        企业项目ID，现在只支持1个

        :return: The enterprise_project of this CreateExternalIncidentRequest.
        :rtype: list[str]
        """
        return self._enterprise_project

    @enterprise_project.setter
    def enterprise_project(self, enterprise_project):
        r"""Sets the enterprise_project of this CreateExternalIncidentRequest.

        企业项目ID，现在只支持1个

        :param enterprise_project: The enterprise_project of this CreateExternalIncidentRequest.
        :type enterprise_project: list[str]
        """
        self._enterprise_project = enterprise_project

    @property
    def current_cloud_service(self):
        r"""Gets the current_cloud_service of this CreateExternalIncidentRequest.

        归属应用ID，现在只支持1个

        :return: The current_cloud_service of this CreateExternalIncidentRequest.
        :rtype: list[str]
        """
        return self._current_cloud_service

    @current_cloud_service.setter
    def current_cloud_service(self, current_cloud_service):
        r"""Sets the current_cloud_service of this CreateExternalIncidentRequest.

        归属应用ID，现在只支持1个

        :param current_cloud_service: The current_cloud_service of this CreateExternalIncidentRequest.
        :type current_cloud_service: list[str]
        """
        self._current_cloud_service = current_cloud_service

    @property
    def incident_level(self):
        r"""Gets the incident_level of this CreateExternalIncidentRequest.

        事件级别 参考：枚举 事件级别incident_level

        :return: The incident_level of this CreateExternalIncidentRequest.
        :rtype: str
        """
        return self._incident_level

    @incident_level.setter
    def incident_level(self, incident_level):
        r"""Sets the incident_level of this CreateExternalIncidentRequest.

        事件级别 参考：枚举 事件级别incident_level

        :param incident_level: The incident_level of this CreateExternalIncidentRequest.
        :type incident_level: str
        """
        self._incident_level = incident_level

    @property
    def is_service_interrupt(self):
        r"""Gets the is_service_interrupt of this CreateExternalIncidentRequest.

        业务是否中断，取值：true/false

        :return: The is_service_interrupt of this CreateExternalIncidentRequest.
        :rtype: bool
        """
        return self._is_service_interrupt

    @is_service_interrupt.setter
    def is_service_interrupt(self, is_service_interrupt):
        r"""Sets the is_service_interrupt of this CreateExternalIncidentRequest.

        业务是否中断，取值：true/false

        :param is_service_interrupt: The is_service_interrupt of this CreateExternalIncidentRequest.
        :type is_service_interrupt: bool
        """
        self._is_service_interrupt = is_service_interrupt

    @property
    def incident_type(self):
        r"""Gets the incident_type of this CreateExternalIncidentRequest.

        事件类别 参考：枚举 事件类别incident_type

        :return: The incident_type of this CreateExternalIncidentRequest.
        :rtype: str
        """
        return self._incident_type

    @incident_type.setter
    def incident_type(self, incident_type):
        r"""Sets the incident_type of this CreateExternalIncidentRequest.

        事件类别 参考：枚举 事件类别incident_type

        :param incident_type: The incident_type of this CreateExternalIncidentRequest.
        :type incident_type: str
        """
        self._incident_type = incident_type

    @property
    def incident_title(self):
        r"""Gets the incident_title of this CreateExternalIncidentRequest.

        事件标题，最大长度：200

        :return: The incident_title of this CreateExternalIncidentRequest.
        :rtype: str
        """
        return self._incident_title

    @incident_title.setter
    def incident_title(self, incident_title):
        r"""Sets the incident_title of this CreateExternalIncidentRequest.

        事件标题，最大长度：200

        :param incident_title: The incident_title of this CreateExternalIncidentRequest.
        :type incident_title: str
        """
        self._incident_title = incident_title

    @property
    def incident_description(self):
        r"""Gets the incident_description of this CreateExternalIncidentRequest.

        事件描述，最大长度：600

        :return: The incident_description of this CreateExternalIncidentRequest.
        :rtype: str
        """
        return self._incident_description

    @incident_description.setter
    def incident_description(self, incident_description):
        r"""Sets the incident_description of this CreateExternalIncidentRequest.

        事件描述，最大长度：600

        :param incident_description: The incident_description of this CreateExternalIncidentRequest.
        :type incident_description: str
        """
        self._incident_description = incident_description

    @property
    def incident_source(self):
        r"""Gets the incident_source of this CreateExternalIncidentRequest.

        单据来源 参考：枚举 事件来源incident_source

        :return: The incident_source of this CreateExternalIncidentRequest.
        :rtype: str
        """
        return self._incident_source

    @incident_source.setter
    def incident_source(self, incident_source):
        r"""Sets the incident_source of this CreateExternalIncidentRequest.

        单据来源 参考：枚举 事件来源incident_source

        :param incident_source: The incident_source of this CreateExternalIncidentRequest.
        :type incident_source: str
        """
        self._incident_source = incident_source

    @property
    def incident_assignee(self):
        r"""Gets the incident_assignee of this CreateExternalIncidentRequest.

        责任人，排班场景和排班角色不能同时为空，现在只支持1个

        :return: The incident_assignee of this CreateExternalIncidentRequest.
        :rtype: list[str]
        """
        return self._incident_assignee

    @incident_assignee.setter
    def incident_assignee(self, incident_assignee):
        r"""Sets the incident_assignee of this CreateExternalIncidentRequest.

        责任人，排班场景和排班角色不能同时为空，现在只支持1个

        :param incident_assignee: The incident_assignee of this CreateExternalIncidentRequest.
        :type incident_assignee: list[str]
        """
        self._incident_assignee = incident_assignee

    @property
    def assignee_scene(self):
        r"""Gets the assignee_scene of this CreateExternalIncidentRequest.

        排班场景，责任人和排班角色不能同时为空

        :return: The assignee_scene of this CreateExternalIncidentRequest.
        :rtype: str
        """
        return self._assignee_scene

    @assignee_scene.setter
    def assignee_scene(self, assignee_scene):
        r"""Sets the assignee_scene of this CreateExternalIncidentRequest.

        排班场景，责任人和排班角色不能同时为空

        :param assignee_scene: The assignee_scene of this CreateExternalIncidentRequest.
        :type assignee_scene: str
        """
        self._assignee_scene = assignee_scene

    @property
    def assignee_role(self):
        r"""Gets the assignee_role of this CreateExternalIncidentRequest.

        排班角色，排班场景和责任人不能同时为空

        :return: The assignee_role of this CreateExternalIncidentRequest.
        :rtype: str
        """
        return self._assignee_role

    @assignee_role.setter
    def assignee_role(self, assignee_role):
        r"""Sets the assignee_role of this CreateExternalIncidentRequest.

        排班角色，排班场景和责任人不能同时为空

        :param assignee_role: The assignee_role of this CreateExternalIncidentRequest.
        :type assignee_role: str
        """
        self._assignee_role = assignee_role

    @property
    def creator(self):
        r"""Gets the creator of this CreateExternalIncidentRequest.

        创单人

        :return: The creator of this CreateExternalIncidentRequest.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this CreateExternalIncidentRequest.

        创单人

        :param creator: The creator of this CreateExternalIncidentRequest.
        :type creator: str
        """
        self._creator = creator

    @property
    def incident_ownership(self):
        r"""Gets the incident_ownership of this CreateExternalIncidentRequest.

        事件归属

        :return: The incident_ownership of this CreateExternalIncidentRequest.
        :rtype: str
        """
        return self._incident_ownership

    @incident_ownership.setter
    def incident_ownership(self, incident_ownership):
        r"""Sets the incident_ownership of this CreateExternalIncidentRequest.

        事件归属

        :param incident_ownership: The incident_ownership of this CreateExternalIncidentRequest.
        :type incident_ownership: str
        """
        self._incident_ownership = incident_ownership

    @property
    def start_time(self):
        r"""Gets the start_time of this CreateExternalIncidentRequest.

        故障发生时间戳

        :return: The start_time of this CreateExternalIncidentRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CreateExternalIncidentRequest.

        故障发生时间戳

        :param start_time: The start_time of this CreateExternalIncidentRequest.
        :type start_time: int
        """
        self._start_time = start_time

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
        if not isinstance(other, CreateExternalIncidentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
