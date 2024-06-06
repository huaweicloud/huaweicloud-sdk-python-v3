# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNoticeRuleRespItem:

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
        'name': 'str',
        'event_name': 'str',
        'scope': 'NoticeRuleScope',
        'trigger_policy': 'TriggerPolicy',
        'notification': 'NoticeRuleNotification',
        'enable': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'event_name': 'event_name',
        'scope': 'scope',
        'trigger_policy': 'trigger_policy',
        'notification': 'notification',
        'enable': 'enable'
    }

    def __init__(self, id=None, name=None, event_name=None, scope=None, trigger_policy=None, notification=None, enable=None):
        """CreateNoticeRuleRespItem

        The model defined in huaweicloud sdk

        :param id: 通知规则的唯一标识。
        :type id: str
        :param name: 通知名称。
        :type name: str
        :param event_name: 触发事件名称。
        :type event_name: str
        :param scope: 
        :type scope: :class:`huaweicloudsdkcae.v1.NoticeRuleScope`
        :param trigger_policy: 
        :type trigger_policy: :class:`huaweicloudsdkcae.v1.TriggerPolicy`
        :param notification: 
        :type notification: :class:`huaweicloudsdkcae.v1.NoticeRuleNotification`
        :param enable: 是否启用。
        :type enable: bool
        """
        
        

        self._id = None
        self._name = None
        self._event_name = None
        self._scope = None
        self._trigger_policy = None
        self._notification = None
        self._enable = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if event_name is not None:
            self.event_name = event_name
        if scope is not None:
            self.scope = scope
        if trigger_policy is not None:
            self.trigger_policy = trigger_policy
        if notification is not None:
            self.notification = notification
        if enable is not None:
            self.enable = enable

    @property
    def id(self):
        """Gets the id of this CreateNoticeRuleRespItem.

        通知规则的唯一标识。

        :return: The id of this CreateNoticeRuleRespItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateNoticeRuleRespItem.

        通知规则的唯一标识。

        :param id: The id of this CreateNoticeRuleRespItem.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateNoticeRuleRespItem.

        通知名称。

        :return: The name of this CreateNoticeRuleRespItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateNoticeRuleRespItem.

        通知名称。

        :param name: The name of this CreateNoticeRuleRespItem.
        :type name: str
        """
        self._name = name

    @property
    def event_name(self):
        """Gets the event_name of this CreateNoticeRuleRespItem.

        触发事件名称。

        :return: The event_name of this CreateNoticeRuleRespItem.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this CreateNoticeRuleRespItem.

        触发事件名称。

        :param event_name: The event_name of this CreateNoticeRuleRespItem.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def scope(self):
        """Gets the scope of this CreateNoticeRuleRespItem.

        :return: The scope of this CreateNoticeRuleRespItem.
        :rtype: :class:`huaweicloudsdkcae.v1.NoticeRuleScope`
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this CreateNoticeRuleRespItem.

        :param scope: The scope of this CreateNoticeRuleRespItem.
        :type scope: :class:`huaweicloudsdkcae.v1.NoticeRuleScope`
        """
        self._scope = scope

    @property
    def trigger_policy(self):
        """Gets the trigger_policy of this CreateNoticeRuleRespItem.

        :return: The trigger_policy of this CreateNoticeRuleRespItem.
        :rtype: :class:`huaweicloudsdkcae.v1.TriggerPolicy`
        """
        return self._trigger_policy

    @trigger_policy.setter
    def trigger_policy(self, trigger_policy):
        """Sets the trigger_policy of this CreateNoticeRuleRespItem.

        :param trigger_policy: The trigger_policy of this CreateNoticeRuleRespItem.
        :type trigger_policy: :class:`huaweicloudsdkcae.v1.TriggerPolicy`
        """
        self._trigger_policy = trigger_policy

    @property
    def notification(self):
        """Gets the notification of this CreateNoticeRuleRespItem.

        :return: The notification of this CreateNoticeRuleRespItem.
        :rtype: :class:`huaweicloudsdkcae.v1.NoticeRuleNotification`
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this CreateNoticeRuleRespItem.

        :param notification: The notification of this CreateNoticeRuleRespItem.
        :type notification: :class:`huaweicloudsdkcae.v1.NoticeRuleNotification`
        """
        self._notification = notification

    @property
    def enable(self):
        """Gets the enable of this CreateNoticeRuleRespItem.

        是否启用。

        :return: The enable of this CreateNoticeRuleRespItem.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this CreateNoticeRuleRespItem.

        是否启用。

        :param enable: The enable of this CreateNoticeRuleRespItem.
        :type enable: bool
        """
        self._enable = enable

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
        if not isinstance(other, CreateNoticeRuleRespItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
