# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWarRoomRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'war_room_name': 'str',
        'description': 'str',
        'region_code_list': 'list[str]',
        'application_id_list': 'list[str]',
        'incident_number': 'str',
        'schedule_group': 'list[ScheduleGroupInfo]',
        'participant': 'list[str]',
        'war_room_admin': 'str',
        'application_names': 'list[str]',
        'region_names': 'list[str]',
        'enterprise_project_id': 'str',
        'notification_type': 'str'
    }

    attribute_map = {
        'war_room_name': 'war_room_name',
        'description': 'description',
        'region_code_list': 'region_code_list',
        'application_id_list': 'application_id_list',
        'incident_number': 'incident_number',
        'schedule_group': 'schedule_group',
        'participant': 'participant',
        'war_room_admin': 'war_room_admin',
        'application_names': 'application_names',
        'region_names': 'region_names',
        'enterprise_project_id': 'enterprise_project_id',
        'notification_type': 'notification_type'
    }

    def __init__(self, war_room_name=None, description=None, region_code_list=None, application_id_list=None, incident_number=None, schedule_group=None, participant=None, war_room_admin=None, application_names=None, region_names=None, enterprise_project_id=None, notification_type=None):
        r"""CreateWarRoomRequestBody

        The model defined in huaweicloud sdk

        :param war_room_name: WarRoom名称
        :type war_room_name: str
        :param description: WarRoom描述
        :type description: str
        :param region_code_list: 区域id
        :type region_code_list: list[str]
        :param application_id_list: 影响应用id
        :type application_id_list: list[str]
        :param incident_number: 事件单号
        :type incident_number: str
        :param schedule_group: 排班分组
        :type schedule_group: list[:class:`huaweicloudsdkcoc.v1.ScheduleGroupInfo`]
        :param participant: 参与者
        :type participant: list[str]
        :param war_room_admin: WarRoom管理员
        :type war_room_admin: str
        :param application_names: 应用名称列表
        :type application_names: list[str]
        :param region_names: region名称列表
        :type region_names: list[str]
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param notification_type: 创建群组方式
        :type notification_type: str
        """
        
        

        self._war_room_name = None
        self._description = None
        self._region_code_list = None
        self._application_id_list = None
        self._incident_number = None
        self._schedule_group = None
        self._participant = None
        self._war_room_admin = None
        self._application_names = None
        self._region_names = None
        self._enterprise_project_id = None
        self._notification_type = None
        self.discriminator = None

        self.war_room_name = war_room_name
        if description is not None:
            self.description = description
        if region_code_list is not None:
            self.region_code_list = region_code_list
        self.application_id_list = application_id_list
        self.incident_number = incident_number
        self.schedule_group = schedule_group
        if participant is not None:
            self.participant = participant
        self.war_room_admin = war_room_admin
        if application_names is not None:
            self.application_names = application_names
        if region_names is not None:
            self.region_names = region_names
        self.enterprise_project_id = enterprise_project_id
        if notification_type is not None:
            self.notification_type = notification_type

    @property
    def war_room_name(self):
        r"""Gets the war_room_name of this CreateWarRoomRequestBody.

        WarRoom名称

        :return: The war_room_name of this CreateWarRoomRequestBody.
        :rtype: str
        """
        return self._war_room_name

    @war_room_name.setter
    def war_room_name(self, war_room_name):
        r"""Sets the war_room_name of this CreateWarRoomRequestBody.

        WarRoom名称

        :param war_room_name: The war_room_name of this CreateWarRoomRequestBody.
        :type war_room_name: str
        """
        self._war_room_name = war_room_name

    @property
    def description(self):
        r"""Gets the description of this CreateWarRoomRequestBody.

        WarRoom描述

        :return: The description of this CreateWarRoomRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateWarRoomRequestBody.

        WarRoom描述

        :param description: The description of this CreateWarRoomRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def region_code_list(self):
        r"""Gets the region_code_list of this CreateWarRoomRequestBody.

        区域id

        :return: The region_code_list of this CreateWarRoomRequestBody.
        :rtype: list[str]
        """
        return self._region_code_list

    @region_code_list.setter
    def region_code_list(self, region_code_list):
        r"""Sets the region_code_list of this CreateWarRoomRequestBody.

        区域id

        :param region_code_list: The region_code_list of this CreateWarRoomRequestBody.
        :type region_code_list: list[str]
        """
        self._region_code_list = region_code_list

    @property
    def application_id_list(self):
        r"""Gets the application_id_list of this CreateWarRoomRequestBody.

        影响应用id

        :return: The application_id_list of this CreateWarRoomRequestBody.
        :rtype: list[str]
        """
        return self._application_id_list

    @application_id_list.setter
    def application_id_list(self, application_id_list):
        r"""Sets the application_id_list of this CreateWarRoomRequestBody.

        影响应用id

        :param application_id_list: The application_id_list of this CreateWarRoomRequestBody.
        :type application_id_list: list[str]
        """
        self._application_id_list = application_id_list

    @property
    def incident_number(self):
        r"""Gets the incident_number of this CreateWarRoomRequestBody.

        事件单号

        :return: The incident_number of this CreateWarRoomRequestBody.
        :rtype: str
        """
        return self._incident_number

    @incident_number.setter
    def incident_number(self, incident_number):
        r"""Sets the incident_number of this CreateWarRoomRequestBody.

        事件单号

        :param incident_number: The incident_number of this CreateWarRoomRequestBody.
        :type incident_number: str
        """
        self._incident_number = incident_number

    @property
    def schedule_group(self):
        r"""Gets the schedule_group of this CreateWarRoomRequestBody.

        排班分组

        :return: The schedule_group of this CreateWarRoomRequestBody.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ScheduleGroupInfo`]
        """
        return self._schedule_group

    @schedule_group.setter
    def schedule_group(self, schedule_group):
        r"""Sets the schedule_group of this CreateWarRoomRequestBody.

        排班分组

        :param schedule_group: The schedule_group of this CreateWarRoomRequestBody.
        :type schedule_group: list[:class:`huaweicloudsdkcoc.v1.ScheduleGroupInfo`]
        """
        self._schedule_group = schedule_group

    @property
    def participant(self):
        r"""Gets the participant of this CreateWarRoomRequestBody.

        参与者

        :return: The participant of this CreateWarRoomRequestBody.
        :rtype: list[str]
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        r"""Sets the participant of this CreateWarRoomRequestBody.

        参与者

        :param participant: The participant of this CreateWarRoomRequestBody.
        :type participant: list[str]
        """
        self._participant = participant

    @property
    def war_room_admin(self):
        r"""Gets the war_room_admin of this CreateWarRoomRequestBody.

        WarRoom管理员

        :return: The war_room_admin of this CreateWarRoomRequestBody.
        :rtype: str
        """
        return self._war_room_admin

    @war_room_admin.setter
    def war_room_admin(self, war_room_admin):
        r"""Sets the war_room_admin of this CreateWarRoomRequestBody.

        WarRoom管理员

        :param war_room_admin: The war_room_admin of this CreateWarRoomRequestBody.
        :type war_room_admin: str
        """
        self._war_room_admin = war_room_admin

    @property
    def application_names(self):
        r"""Gets the application_names of this CreateWarRoomRequestBody.

        应用名称列表

        :return: The application_names of this CreateWarRoomRequestBody.
        :rtype: list[str]
        """
        return self._application_names

    @application_names.setter
    def application_names(self, application_names):
        r"""Sets the application_names of this CreateWarRoomRequestBody.

        应用名称列表

        :param application_names: The application_names of this CreateWarRoomRequestBody.
        :type application_names: list[str]
        """
        self._application_names = application_names

    @property
    def region_names(self):
        r"""Gets the region_names of this CreateWarRoomRequestBody.

        region名称列表

        :return: The region_names of this CreateWarRoomRequestBody.
        :rtype: list[str]
        """
        return self._region_names

    @region_names.setter
    def region_names(self, region_names):
        r"""Sets the region_names of this CreateWarRoomRequestBody.

        region名称列表

        :param region_names: The region_names of this CreateWarRoomRequestBody.
        :type region_names: list[str]
        """
        self._region_names = region_names

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateWarRoomRequestBody.

        企业项目id

        :return: The enterprise_project_id of this CreateWarRoomRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateWarRoomRequestBody.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this CreateWarRoomRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def notification_type(self):
        r"""Gets the notification_type of this CreateWarRoomRequestBody.

        创建群组方式

        :return: The notification_type of this CreateWarRoomRequestBody.
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        r"""Sets the notification_type of this CreateWarRoomRequestBody.

        创建群组方式

        :param notification_type: The notification_type of this CreateWarRoomRequestBody.
        :type notification_type: str
        """
        self._notification_type = notification_type

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
        if not isinstance(other, CreateWarRoomRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
