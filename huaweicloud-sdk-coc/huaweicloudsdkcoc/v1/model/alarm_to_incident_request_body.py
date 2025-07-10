# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmToIncidentRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_ids': 'str',
        'enterprise_project_id': 'str',
        'assignee': 'str',
        'assignee_role': 'str',
        'assignee_scene': 'str',
        'attachment': 'str',
        'current_cloud_service_id': 'str',
        'description': 'str',
        'is_change_event': 'bool',
        'is_service_interrupt': 'bool',
        'level_id': 'str',
        'mtm_region': 'str',
        'mtm_type': 'str',
        'source_id': 'str',
        'title': 'str'
    }

    attribute_map = {
        'alarm_ids': 'alarm_ids',
        'enterprise_project_id': 'enterprise_project_id',
        'assignee': 'assignee',
        'assignee_role': 'assignee_role',
        'assignee_scene': 'assignee_scene',
        'attachment': 'attachment',
        'current_cloud_service_id': 'current_cloud_service_id',
        'description': 'description',
        'is_change_event': 'is_change_event',
        'is_service_interrupt': 'is_service_interrupt',
        'level_id': 'level_id',
        'mtm_region': 'mtm_region',
        'mtm_type': 'mtm_type',
        'source_id': 'source_id',
        'title': 'title'
    }

    def __init__(self, alarm_ids=None, enterprise_project_id=None, assignee=None, assignee_role=None, assignee_scene=None, attachment=None, current_cloud_service_id=None, description=None, is_change_event=None, is_service_interrupt=None, level_id=None, mtm_region=None, mtm_type=None, source_id=None, title=None):
        r"""AlarmToIncidentRequestBody

        The model defined in huaweicloud sdk

        :param alarm_ids: 告警id，多个以”，分隔“
        :type alarm_ids: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param assignee: 责任人（个人）
        :type assignee: str
        :param assignee_role: 责任人（排班角色）
        :type assignee_role: str
        :param assignee_scene: 责任人（排版场景）
        :type assignee_scene: str
        :param attachment: 附件
        :type attachment: str
        :param current_cloud_service_id: 归属应用
        :type current_cloud_service_id: str
        :param description: 事件描述
        :type description: str
        :param is_change_event: 是否变更事件
        :type is_change_event: bool
        :param is_service_interrupt: 业务是否中断
        :type is_service_interrupt: bool
        :param level_id: 事件等级
        :type level_id: str
        :param mtm_region: region
        :type mtm_region: str
        :param mtm_type: 事件类别
        :type mtm_type: str
        :param source_id: 资源id
        :type source_id: str
        :param title: 事件名称
        :type title: str
        """
        
        

        self._alarm_ids = None
        self._enterprise_project_id = None
        self._assignee = None
        self._assignee_role = None
        self._assignee_scene = None
        self._attachment = None
        self._current_cloud_service_id = None
        self._description = None
        self._is_change_event = None
        self._is_service_interrupt = None
        self._level_id = None
        self._mtm_region = None
        self._mtm_type = None
        self._source_id = None
        self._title = None
        self.discriminator = None

        self.alarm_ids = alarm_ids
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if assignee is not None:
            self.assignee = assignee
        if assignee_role is not None:
            self.assignee_role = assignee_role
        if assignee_scene is not None:
            self.assignee_scene = assignee_scene
        if attachment is not None:
            self.attachment = attachment
        self.current_cloud_service_id = current_cloud_service_id
        self.description = description
        if is_change_event is not None:
            self.is_change_event = is_change_event
        self.is_service_interrupt = is_service_interrupt
        self.level_id = level_id
        if mtm_region is not None:
            self.mtm_region = mtm_region
        self.mtm_type = mtm_type
        if source_id is not None:
            self.source_id = source_id
        self.title = title

    @property
    def alarm_ids(self):
        r"""Gets the alarm_ids of this AlarmToIncidentRequestBody.

        告警id，多个以”，分隔“

        :return: The alarm_ids of this AlarmToIncidentRequestBody.
        :rtype: str
        """
        return self._alarm_ids

    @alarm_ids.setter
    def alarm_ids(self, alarm_ids):
        r"""Sets the alarm_ids of this AlarmToIncidentRequestBody.

        告警id，多个以”，分隔“

        :param alarm_ids: The alarm_ids of this AlarmToIncidentRequestBody.
        :type alarm_ids: str
        """
        self._alarm_ids = alarm_ids

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this AlarmToIncidentRequestBody.

        企业项目id

        :return: The enterprise_project_id of this AlarmToIncidentRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this AlarmToIncidentRequestBody.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this AlarmToIncidentRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def assignee(self):
        r"""Gets the assignee of this AlarmToIncidentRequestBody.

        责任人（个人）

        :return: The assignee of this AlarmToIncidentRequestBody.
        :rtype: str
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this AlarmToIncidentRequestBody.

        责任人（个人）

        :param assignee: The assignee of this AlarmToIncidentRequestBody.
        :type assignee: str
        """
        self._assignee = assignee

    @property
    def assignee_role(self):
        r"""Gets the assignee_role of this AlarmToIncidentRequestBody.

        责任人（排班角色）

        :return: The assignee_role of this AlarmToIncidentRequestBody.
        :rtype: str
        """
        return self._assignee_role

    @assignee_role.setter
    def assignee_role(self, assignee_role):
        r"""Sets the assignee_role of this AlarmToIncidentRequestBody.

        责任人（排班角色）

        :param assignee_role: The assignee_role of this AlarmToIncidentRequestBody.
        :type assignee_role: str
        """
        self._assignee_role = assignee_role

    @property
    def assignee_scene(self):
        r"""Gets the assignee_scene of this AlarmToIncidentRequestBody.

        责任人（排版场景）

        :return: The assignee_scene of this AlarmToIncidentRequestBody.
        :rtype: str
        """
        return self._assignee_scene

    @assignee_scene.setter
    def assignee_scene(self, assignee_scene):
        r"""Sets the assignee_scene of this AlarmToIncidentRequestBody.

        责任人（排版场景）

        :param assignee_scene: The assignee_scene of this AlarmToIncidentRequestBody.
        :type assignee_scene: str
        """
        self._assignee_scene = assignee_scene

    @property
    def attachment(self):
        r"""Gets the attachment of this AlarmToIncidentRequestBody.

        附件

        :return: The attachment of this AlarmToIncidentRequestBody.
        :rtype: str
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        r"""Sets the attachment of this AlarmToIncidentRequestBody.

        附件

        :param attachment: The attachment of this AlarmToIncidentRequestBody.
        :type attachment: str
        """
        self._attachment = attachment

    @property
    def current_cloud_service_id(self):
        r"""Gets the current_cloud_service_id of this AlarmToIncidentRequestBody.

        归属应用

        :return: The current_cloud_service_id of this AlarmToIncidentRequestBody.
        :rtype: str
        """
        return self._current_cloud_service_id

    @current_cloud_service_id.setter
    def current_cloud_service_id(self, current_cloud_service_id):
        r"""Sets the current_cloud_service_id of this AlarmToIncidentRequestBody.

        归属应用

        :param current_cloud_service_id: The current_cloud_service_id of this AlarmToIncidentRequestBody.
        :type current_cloud_service_id: str
        """
        self._current_cloud_service_id = current_cloud_service_id

    @property
    def description(self):
        r"""Gets the description of this AlarmToIncidentRequestBody.

        事件描述

        :return: The description of this AlarmToIncidentRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AlarmToIncidentRequestBody.

        事件描述

        :param description: The description of this AlarmToIncidentRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def is_change_event(self):
        r"""Gets the is_change_event of this AlarmToIncidentRequestBody.

        是否变更事件

        :return: The is_change_event of this AlarmToIncidentRequestBody.
        :rtype: bool
        """
        return self._is_change_event

    @is_change_event.setter
    def is_change_event(self, is_change_event):
        r"""Sets the is_change_event of this AlarmToIncidentRequestBody.

        是否变更事件

        :param is_change_event: The is_change_event of this AlarmToIncidentRequestBody.
        :type is_change_event: bool
        """
        self._is_change_event = is_change_event

    @property
    def is_service_interrupt(self):
        r"""Gets the is_service_interrupt of this AlarmToIncidentRequestBody.

        业务是否中断

        :return: The is_service_interrupt of this AlarmToIncidentRequestBody.
        :rtype: bool
        """
        return self._is_service_interrupt

    @is_service_interrupt.setter
    def is_service_interrupt(self, is_service_interrupt):
        r"""Sets the is_service_interrupt of this AlarmToIncidentRequestBody.

        业务是否中断

        :param is_service_interrupt: The is_service_interrupt of this AlarmToIncidentRequestBody.
        :type is_service_interrupt: bool
        """
        self._is_service_interrupt = is_service_interrupt

    @property
    def level_id(self):
        r"""Gets the level_id of this AlarmToIncidentRequestBody.

        事件等级

        :return: The level_id of this AlarmToIncidentRequestBody.
        :rtype: str
        """
        return self._level_id

    @level_id.setter
    def level_id(self, level_id):
        r"""Sets the level_id of this AlarmToIncidentRequestBody.

        事件等级

        :param level_id: The level_id of this AlarmToIncidentRequestBody.
        :type level_id: str
        """
        self._level_id = level_id

    @property
    def mtm_region(self):
        r"""Gets the mtm_region of this AlarmToIncidentRequestBody.

        region

        :return: The mtm_region of this AlarmToIncidentRequestBody.
        :rtype: str
        """
        return self._mtm_region

    @mtm_region.setter
    def mtm_region(self, mtm_region):
        r"""Sets the mtm_region of this AlarmToIncidentRequestBody.

        region

        :param mtm_region: The mtm_region of this AlarmToIncidentRequestBody.
        :type mtm_region: str
        """
        self._mtm_region = mtm_region

    @property
    def mtm_type(self):
        r"""Gets the mtm_type of this AlarmToIncidentRequestBody.

        事件类别

        :return: The mtm_type of this AlarmToIncidentRequestBody.
        :rtype: str
        """
        return self._mtm_type

    @mtm_type.setter
    def mtm_type(self, mtm_type):
        r"""Sets the mtm_type of this AlarmToIncidentRequestBody.

        事件类别

        :param mtm_type: The mtm_type of this AlarmToIncidentRequestBody.
        :type mtm_type: str
        """
        self._mtm_type = mtm_type

    @property
    def source_id(self):
        r"""Gets the source_id of this AlarmToIncidentRequestBody.

        资源id

        :return: The source_id of this AlarmToIncidentRequestBody.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this AlarmToIncidentRequestBody.

        资源id

        :param source_id: The source_id of this AlarmToIncidentRequestBody.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def title(self):
        r"""Gets the title of this AlarmToIncidentRequestBody.

        事件名称

        :return: The title of this AlarmToIncidentRequestBody.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this AlarmToIncidentRequestBody.

        事件名称

        :param title: The title of this AlarmToIncidentRequestBody.
        :type title: str
        """
        self._title = title

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
        if not isinstance(other, AlarmToIncidentRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
