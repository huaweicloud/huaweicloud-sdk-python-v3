# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotificationObjConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notification_endpoint_type': 'str',
        'schedule_scene': 'str',
        'schedule_role': 'str',
        'schedule_role_name': 'str',
        'recipients': 'str',
        'group_type': 'str',
        'group_id': 'str',
        'group_name': 'str'
    }

    attribute_map = {
        'notification_endpoint_type': 'notification_endpoint_type',
        'schedule_scene': 'schedule_scene',
        'schedule_role': 'schedule_role',
        'schedule_role_name': 'schedule_role_name',
        'recipients': 'recipients',
        'group_type': 'group_type',
        'group_id': 'group_id',
        'group_name': 'group_name'
    }

    def __init__(self, notification_endpoint_type=None, schedule_scene=None, schedule_role=None, schedule_role_name=None, recipients=None, group_type=None, group_id=None, group_name=None):
        r"""NotificationObjConfiguration

        The model defined in huaweicloud sdk

        :param notification_endpoint_type: 通知对象类型（排班/个人/工单责任人/群组）
        :type notification_endpoint_type: str
        :param schedule_scene: 排班场景ID
        :type schedule_scene: str
        :param schedule_role: 排班角色ID
        :type schedule_role: str
        :param schedule_role_name: 排班角色名称
        :type schedule_role_name: str
        :param recipients: 消息通知接收人，对于群组通知而言其对应的是被@的群成员
        :type recipients: str
        :param group_type: 群组类型（企业微信/钉钉/飞书）
        :type group_type: str
        :param group_id: 群组ID
        :type group_id: str
        :param group_name: 群组名称
        :type group_name: str
        """
        
        

        self._notification_endpoint_type = None
        self._schedule_scene = None
        self._schedule_role = None
        self._schedule_role_name = None
        self._recipients = None
        self._group_type = None
        self._group_id = None
        self._group_name = None
        self.discriminator = None

        if notification_endpoint_type is not None:
            self.notification_endpoint_type = notification_endpoint_type
        if schedule_scene is not None:
            self.schedule_scene = schedule_scene
        if schedule_role is not None:
            self.schedule_role = schedule_role
        if schedule_role_name is not None:
            self.schedule_role_name = schedule_role_name
        if recipients is not None:
            self.recipients = recipients
        if group_type is not None:
            self.group_type = group_type
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name

    @property
    def notification_endpoint_type(self):
        r"""Gets the notification_endpoint_type of this NotificationObjConfiguration.

        通知对象类型（排班/个人/工单责任人/群组）

        :return: The notification_endpoint_type of this NotificationObjConfiguration.
        :rtype: str
        """
        return self._notification_endpoint_type

    @notification_endpoint_type.setter
    def notification_endpoint_type(self, notification_endpoint_type):
        r"""Sets the notification_endpoint_type of this NotificationObjConfiguration.

        通知对象类型（排班/个人/工单责任人/群组）

        :param notification_endpoint_type: The notification_endpoint_type of this NotificationObjConfiguration.
        :type notification_endpoint_type: str
        """
        self._notification_endpoint_type = notification_endpoint_type

    @property
    def schedule_scene(self):
        r"""Gets the schedule_scene of this NotificationObjConfiguration.

        排班场景ID

        :return: The schedule_scene of this NotificationObjConfiguration.
        :rtype: str
        """
        return self._schedule_scene

    @schedule_scene.setter
    def schedule_scene(self, schedule_scene):
        r"""Sets the schedule_scene of this NotificationObjConfiguration.

        排班场景ID

        :param schedule_scene: The schedule_scene of this NotificationObjConfiguration.
        :type schedule_scene: str
        """
        self._schedule_scene = schedule_scene

    @property
    def schedule_role(self):
        r"""Gets the schedule_role of this NotificationObjConfiguration.

        排班角色ID

        :return: The schedule_role of this NotificationObjConfiguration.
        :rtype: str
        """
        return self._schedule_role

    @schedule_role.setter
    def schedule_role(self, schedule_role):
        r"""Sets the schedule_role of this NotificationObjConfiguration.

        排班角色ID

        :param schedule_role: The schedule_role of this NotificationObjConfiguration.
        :type schedule_role: str
        """
        self._schedule_role = schedule_role

    @property
    def schedule_role_name(self):
        r"""Gets the schedule_role_name of this NotificationObjConfiguration.

        排班角色名称

        :return: The schedule_role_name of this NotificationObjConfiguration.
        :rtype: str
        """
        return self._schedule_role_name

    @schedule_role_name.setter
    def schedule_role_name(self, schedule_role_name):
        r"""Sets the schedule_role_name of this NotificationObjConfiguration.

        排班角色名称

        :param schedule_role_name: The schedule_role_name of this NotificationObjConfiguration.
        :type schedule_role_name: str
        """
        self._schedule_role_name = schedule_role_name

    @property
    def recipients(self):
        r"""Gets the recipients of this NotificationObjConfiguration.

        消息通知接收人，对于群组通知而言其对应的是被@的群成员

        :return: The recipients of this NotificationObjConfiguration.
        :rtype: str
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        r"""Sets the recipients of this NotificationObjConfiguration.

        消息通知接收人，对于群组通知而言其对应的是被@的群成员

        :param recipients: The recipients of this NotificationObjConfiguration.
        :type recipients: str
        """
        self._recipients = recipients

    @property
    def group_type(self):
        r"""Gets the group_type of this NotificationObjConfiguration.

        群组类型（企业微信/钉钉/飞书）

        :return: The group_type of this NotificationObjConfiguration.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        r"""Sets the group_type of this NotificationObjConfiguration.

        群组类型（企业微信/钉钉/飞书）

        :param group_type: The group_type of this NotificationObjConfiguration.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def group_id(self):
        r"""Gets the group_id of this NotificationObjConfiguration.

        群组ID

        :return: The group_id of this NotificationObjConfiguration.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this NotificationObjConfiguration.

        群组ID

        :param group_id: The group_id of this NotificationObjConfiguration.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this NotificationObjConfiguration.

        群组名称

        :return: The group_name of this NotificationObjConfiguration.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this NotificationObjConfiguration.

        群组名称

        :param group_name: The group_name of this NotificationObjConfiguration.
        :type group_name: str
        """
        self._group_name = group_name

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
        if not isinstance(other, NotificationObjConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
