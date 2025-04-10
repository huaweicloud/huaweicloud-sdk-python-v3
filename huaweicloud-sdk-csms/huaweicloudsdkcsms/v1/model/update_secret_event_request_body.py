# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecretEventRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'state': 'str',
        'event_types': 'list[str]',
        'notification': 'Notification'
    }

    attribute_map = {
        'state': 'state',
        'event_types': 'event_types',
        'notification': 'notification'
    }

    def __init__(self, state=None, event_types=None, notification=None):
        r"""UpdateSecretEventRequestBody

        The model defined in huaweicloud sdk

        :param state: 事件通知状态，取值如下。  ENABLED：表示启用状态 DISABLED：表示禁用状态
        :type state: str
        :param event_types: 本次事件通知的基础事件列表，基础事件类型如下。  - SECRET_VERSION_CREATED:版本创建 - SECRET_VERSION_EXPIRED:版本过期 - SECRET_ROTATED:凭据轮转成功 - SECRET_DELETED:凭据删除 - SECRET_ROTATED_FAILED:凭据轮转失败  列表包含的基础事件类型不能重复。
        :type event_types: list[str]
        :param notification: 
        :type notification: :class:`huaweicloudsdkcsms.v1.Notification`
        """
        
        

        self._state = None
        self._event_types = None
        self._notification = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if event_types is not None:
            self.event_types = event_types
        if notification is not None:
            self.notification = notification

    @property
    def state(self):
        r"""Gets the state of this UpdateSecretEventRequestBody.

        事件通知状态，取值如下。  ENABLED：表示启用状态 DISABLED：表示禁用状态

        :return: The state of this UpdateSecretEventRequestBody.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this UpdateSecretEventRequestBody.

        事件通知状态，取值如下。  ENABLED：表示启用状态 DISABLED：表示禁用状态

        :param state: The state of this UpdateSecretEventRequestBody.
        :type state: str
        """
        self._state = state

    @property
    def event_types(self):
        r"""Gets the event_types of this UpdateSecretEventRequestBody.

        本次事件通知的基础事件列表，基础事件类型如下。  - SECRET_VERSION_CREATED:版本创建 - SECRET_VERSION_EXPIRED:版本过期 - SECRET_ROTATED:凭据轮转成功 - SECRET_DELETED:凭据删除 - SECRET_ROTATED_FAILED:凭据轮转失败  列表包含的基础事件类型不能重复。

        :return: The event_types of this UpdateSecretEventRequestBody.
        :rtype: list[str]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        r"""Sets the event_types of this UpdateSecretEventRequestBody.

        本次事件通知的基础事件列表，基础事件类型如下。  - SECRET_VERSION_CREATED:版本创建 - SECRET_VERSION_EXPIRED:版本过期 - SECRET_ROTATED:凭据轮转成功 - SECRET_DELETED:凭据删除 - SECRET_ROTATED_FAILED:凭据轮转失败  列表包含的基础事件类型不能重复。

        :param event_types: The event_types of this UpdateSecretEventRequestBody.
        :type event_types: list[str]
        """
        self._event_types = event_types

    @property
    def notification(self):
        r"""Gets the notification of this UpdateSecretEventRequestBody.

        :return: The notification of this UpdateSecretEventRequestBody.
        :rtype: :class:`huaweicloudsdkcsms.v1.Notification`
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        r"""Sets the notification of this UpdateSecretEventRequestBody.

        :param notification: The notification of this UpdateSecretEventRequestBody.
        :type notification: :class:`huaweicloudsdkcsms.v1.Notification`
        """
        self._notification = notification

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
        if not isinstance(other, UpdateSecretEventRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
