# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AsyncAssociateRGAndTemplatesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_ids': 'list[str]',
        'notification_enabled': 'bool',
        'alarm_notifications': 'list[Notification]',
        'ok_notifications': 'list[Notification]',
        'notification_begin_time': 'str',
        'notification_end_time': 'str',
        'effective_timezone': 'str',
        'enterprise_project_id': 'str',
        'notification_manner': 'str',
        'notification_policy_ids': 'list[str]'
    }

    attribute_map = {
        'template_ids': 'template_ids',
        'notification_enabled': 'notification_enabled',
        'alarm_notifications': 'alarm_notifications',
        'ok_notifications': 'ok_notifications',
        'notification_begin_time': 'notification_begin_time',
        'notification_end_time': 'notification_end_time',
        'effective_timezone': 'effective_timezone',
        'enterprise_project_id': 'enterprise_project_id',
        'notification_manner': 'notification_manner',
        'notification_policy_ids': 'notification_policy_ids'
    }

    def __init__(self, template_ids=None, notification_enabled=None, alarm_notifications=None, ok_notifications=None, notification_begin_time=None, notification_end_time=None, effective_timezone=None, enterprise_project_id=None, notification_manner=None, notification_policy_ids=None):
        r"""AsyncAssociateRGAndTemplatesReq

        The model defined in huaweicloud sdk

        :param template_ids: 告警模板编号列表，当ID列表为空时，将删除该资源分组已关联的告警模板所创建的告警规则
        :type template_ids: list[str]
        :param notification_enabled: 是否开启告警通知。true:开启，false:关闭。
        :type notification_enabled: bool
        :param alarm_notifications: 告警触发通知列表
        :type alarm_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        :param ok_notifications: 告警恢复通知列表
        :type ok_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        :param notification_begin_time: **参数解释**： 每天告警通知的开始时间。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符。 **默认取值**： 不涉及。 
        :type notification_begin_time: str
        :param notification_end_time: **参数解释**： 每天告警通知的结束时间。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符。 **默认取值**： 不涉及。 
        :type notification_end_time: str
        :param effective_timezone: 时区，形如：\&quot;GMT-08:00\&quot;、\&quot;GMT+08:00\&quot;、\&quot;GMT+0:00\&quot;
        :type effective_timezone: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param notification_manner: NOTIFICATION_GROUP(通知组)/TOPIC_SUBSCRIPTION(主题订阅)/NOTIFICATION_POLICY(通知策略)
        :type notification_manner: str
        :param notification_policy_ids: 关联的通知策略ID列表
        :type notification_policy_ids: list[str]
        """
        
        

        self._template_ids = None
        self._notification_enabled = None
        self._alarm_notifications = None
        self._ok_notifications = None
        self._notification_begin_time = None
        self._notification_end_time = None
        self._effective_timezone = None
        self._enterprise_project_id = None
        self._notification_manner = None
        self._notification_policy_ids = None
        self.discriminator = None

        self.template_ids = template_ids
        self.notification_enabled = notification_enabled
        if alarm_notifications is not None:
            self.alarm_notifications = alarm_notifications
        if ok_notifications is not None:
            self.ok_notifications = ok_notifications
        if notification_begin_time is not None:
            self.notification_begin_time = notification_begin_time
        if notification_end_time is not None:
            self.notification_end_time = notification_end_time
        if effective_timezone is not None:
            self.effective_timezone = effective_timezone
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if notification_manner is not None:
            self.notification_manner = notification_manner
        if notification_policy_ids is not None:
            self.notification_policy_ids = notification_policy_ids

    @property
    def template_ids(self):
        r"""Gets the template_ids of this AsyncAssociateRGAndTemplatesReq.

        告警模板编号列表，当ID列表为空时，将删除该资源分组已关联的告警模板所创建的告警规则

        :return: The template_ids of this AsyncAssociateRGAndTemplatesReq.
        :rtype: list[str]
        """
        return self._template_ids

    @template_ids.setter
    def template_ids(self, template_ids):
        r"""Sets the template_ids of this AsyncAssociateRGAndTemplatesReq.

        告警模板编号列表，当ID列表为空时，将删除该资源分组已关联的告警模板所创建的告警规则

        :param template_ids: The template_ids of this AsyncAssociateRGAndTemplatesReq.
        :type template_ids: list[str]
        """
        self._template_ids = template_ids

    @property
    def notification_enabled(self):
        r"""Gets the notification_enabled of this AsyncAssociateRGAndTemplatesReq.

        是否开启告警通知。true:开启，false:关闭。

        :return: The notification_enabled of this AsyncAssociateRGAndTemplatesReq.
        :rtype: bool
        """
        return self._notification_enabled

    @notification_enabled.setter
    def notification_enabled(self, notification_enabled):
        r"""Sets the notification_enabled of this AsyncAssociateRGAndTemplatesReq.

        是否开启告警通知。true:开启，false:关闭。

        :param notification_enabled: The notification_enabled of this AsyncAssociateRGAndTemplatesReq.
        :type notification_enabled: bool
        """
        self._notification_enabled = notification_enabled

    @property
    def alarm_notifications(self):
        r"""Gets the alarm_notifications of this AsyncAssociateRGAndTemplatesReq.

        告警触发通知列表

        :return: The alarm_notifications of this AsyncAssociateRGAndTemplatesReq.
        :rtype: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        return self._alarm_notifications

    @alarm_notifications.setter
    def alarm_notifications(self, alarm_notifications):
        r"""Sets the alarm_notifications of this AsyncAssociateRGAndTemplatesReq.

        告警触发通知列表

        :param alarm_notifications: The alarm_notifications of this AsyncAssociateRGAndTemplatesReq.
        :type alarm_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        self._alarm_notifications = alarm_notifications

    @property
    def ok_notifications(self):
        r"""Gets the ok_notifications of this AsyncAssociateRGAndTemplatesReq.

        告警恢复通知列表

        :return: The ok_notifications of this AsyncAssociateRGAndTemplatesReq.
        :rtype: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        return self._ok_notifications

    @ok_notifications.setter
    def ok_notifications(self, ok_notifications):
        r"""Sets the ok_notifications of this AsyncAssociateRGAndTemplatesReq.

        告警恢复通知列表

        :param ok_notifications: The ok_notifications of this AsyncAssociateRGAndTemplatesReq.
        :type ok_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        self._ok_notifications = ok_notifications

    @property
    def notification_begin_time(self):
        r"""Gets the notification_begin_time of this AsyncAssociateRGAndTemplatesReq.

        **参数解释**： 每天告警通知的开始时间。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符。 **默认取值**： 不涉及。 

        :return: The notification_begin_time of this AsyncAssociateRGAndTemplatesReq.
        :rtype: str
        """
        return self._notification_begin_time

    @notification_begin_time.setter
    def notification_begin_time(self, notification_begin_time):
        r"""Sets the notification_begin_time of this AsyncAssociateRGAndTemplatesReq.

        **参数解释**： 每天告警通知的开始时间。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符。 **默认取值**： 不涉及。 

        :param notification_begin_time: The notification_begin_time of this AsyncAssociateRGAndTemplatesReq.
        :type notification_begin_time: str
        """
        self._notification_begin_time = notification_begin_time

    @property
    def notification_end_time(self):
        r"""Gets the notification_end_time of this AsyncAssociateRGAndTemplatesReq.

        **参数解释**： 每天告警通知的结束时间。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符。 **默认取值**： 不涉及。 

        :return: The notification_end_time of this AsyncAssociateRGAndTemplatesReq.
        :rtype: str
        """
        return self._notification_end_time

    @notification_end_time.setter
    def notification_end_time(self, notification_end_time):
        r"""Sets the notification_end_time of this AsyncAssociateRGAndTemplatesReq.

        **参数解释**： 每天告警通知的结束时间。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符。 **默认取值**： 不涉及。 

        :param notification_end_time: The notification_end_time of this AsyncAssociateRGAndTemplatesReq.
        :type notification_end_time: str
        """
        self._notification_end_time = notification_end_time

    @property
    def effective_timezone(self):
        r"""Gets the effective_timezone of this AsyncAssociateRGAndTemplatesReq.

        时区，形如：\"GMT-08:00\"、\"GMT+08:00\"、\"GMT+0:00\"

        :return: The effective_timezone of this AsyncAssociateRGAndTemplatesReq.
        :rtype: str
        """
        return self._effective_timezone

    @effective_timezone.setter
    def effective_timezone(self, effective_timezone):
        r"""Sets the effective_timezone of this AsyncAssociateRGAndTemplatesReq.

        时区，形如：\"GMT-08:00\"、\"GMT+08:00\"、\"GMT+0:00\"

        :param effective_timezone: The effective_timezone of this AsyncAssociateRGAndTemplatesReq.
        :type effective_timezone: str
        """
        self._effective_timezone = effective_timezone

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this AsyncAssociateRGAndTemplatesReq.

        企业项目ID

        :return: The enterprise_project_id of this AsyncAssociateRGAndTemplatesReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this AsyncAssociateRGAndTemplatesReq.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this AsyncAssociateRGAndTemplatesReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def notification_manner(self):
        r"""Gets the notification_manner of this AsyncAssociateRGAndTemplatesReq.

        NOTIFICATION_GROUP(通知组)/TOPIC_SUBSCRIPTION(主题订阅)/NOTIFICATION_POLICY(通知策略)

        :return: The notification_manner of this AsyncAssociateRGAndTemplatesReq.
        :rtype: str
        """
        return self._notification_manner

    @notification_manner.setter
    def notification_manner(self, notification_manner):
        r"""Sets the notification_manner of this AsyncAssociateRGAndTemplatesReq.

        NOTIFICATION_GROUP(通知组)/TOPIC_SUBSCRIPTION(主题订阅)/NOTIFICATION_POLICY(通知策略)

        :param notification_manner: The notification_manner of this AsyncAssociateRGAndTemplatesReq.
        :type notification_manner: str
        """
        self._notification_manner = notification_manner

    @property
    def notification_policy_ids(self):
        r"""Gets the notification_policy_ids of this AsyncAssociateRGAndTemplatesReq.

        关联的通知策略ID列表

        :return: The notification_policy_ids of this AsyncAssociateRGAndTemplatesReq.
        :rtype: list[str]
        """
        return self._notification_policy_ids

    @notification_policy_ids.setter
    def notification_policy_ids(self, notification_policy_ids):
        r"""Sets the notification_policy_ids of this AsyncAssociateRGAndTemplatesReq.

        关联的通知策略ID列表

        :param notification_policy_ids: The notification_policy_ids of this AsyncAssociateRGAndTemplatesReq.
        :type notification_policy_ids: list[str]
        """
        self._notification_policy_ids = notification_policy_ids

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
        if not isinstance(other, AsyncAssociateRGAndTemplatesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
