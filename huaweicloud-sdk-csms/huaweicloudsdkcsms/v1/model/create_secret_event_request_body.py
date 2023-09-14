# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecretEventRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'event_types': 'list[str]',
        'state': 'str',
        'notification': 'Notification'
    }

    attribute_map = {
        'name': 'name',
        'event_types': 'event_types',
        'state': 'state',
        'notification': 'notification'
    }

    def __init__(self, name=None, event_types=None, state=None, notification=None):
        """CreateSecretEventRequestBody

        The model defined in huaweicloud sdk

        :param name: 新创建事件通知的名称。  约束：取值范围为1到64个字符，满足正则匹配“^[a-zA-Z0-9_-]{1,64}$”。 
        :type name: str
        :param event_types: 本次事件通知的基础事件列表，基础事件类型如下。  SECRET_VERSION_CREATED：版本创建 SECRET_VERSION_EXPIRED：版本过期 SECRET_ROTATED：凭据轮转 SECRET_DELETED：凭据删除  列表包含的基础事件类型不能重复。 
        :type event_types: list[str]
        :param state: 控制事件是否生效，只有启用状态才能触发包含的基础事件类型  ENABLED：启用 DISABLED：禁用 
        :type state: str
        :param notification: 
        :type notification: :class:`huaweicloudsdkcsms.v1.Notification`
        """
        
        

        self._name = None
        self._event_types = None
        self._state = None
        self._notification = None
        self.discriminator = None

        self.name = name
        self.event_types = event_types
        self.state = state
        self.notification = notification

    @property
    def name(self):
        """Gets the name of this CreateSecretEventRequestBody.

        新创建事件通知的名称。  约束：取值范围为1到64个字符，满足正则匹配“^[a-zA-Z0-9_-]{1,64}$”。 

        :return: The name of this CreateSecretEventRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSecretEventRequestBody.

        新创建事件通知的名称。  约束：取值范围为1到64个字符，满足正则匹配“^[a-zA-Z0-9_-]{1,64}$”。 

        :param name: The name of this CreateSecretEventRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def event_types(self):
        """Gets the event_types of this CreateSecretEventRequestBody.

        本次事件通知的基础事件列表，基础事件类型如下。  SECRET_VERSION_CREATED：版本创建 SECRET_VERSION_EXPIRED：版本过期 SECRET_ROTATED：凭据轮转 SECRET_DELETED：凭据删除  列表包含的基础事件类型不能重复。 

        :return: The event_types of this CreateSecretEventRequestBody.
        :rtype: list[str]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        """Sets the event_types of this CreateSecretEventRequestBody.

        本次事件通知的基础事件列表，基础事件类型如下。  SECRET_VERSION_CREATED：版本创建 SECRET_VERSION_EXPIRED：版本过期 SECRET_ROTATED：凭据轮转 SECRET_DELETED：凭据删除  列表包含的基础事件类型不能重复。 

        :param event_types: The event_types of this CreateSecretEventRequestBody.
        :type event_types: list[str]
        """
        self._event_types = event_types

    @property
    def state(self):
        """Gets the state of this CreateSecretEventRequestBody.

        控制事件是否生效，只有启用状态才能触发包含的基础事件类型  ENABLED：启用 DISABLED：禁用 

        :return: The state of this CreateSecretEventRequestBody.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CreateSecretEventRequestBody.

        控制事件是否生效，只有启用状态才能触发包含的基础事件类型  ENABLED：启用 DISABLED：禁用 

        :param state: The state of this CreateSecretEventRequestBody.
        :type state: str
        """
        self._state = state

    @property
    def notification(self):
        """Gets the notification of this CreateSecretEventRequestBody.

        :return: The notification of this CreateSecretEventRequestBody.
        :rtype: :class:`huaweicloudsdkcsms.v1.Notification`
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this CreateSecretEventRequestBody.

        :param notification: The notification of this CreateSecretEventRequestBody.
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
        if not isinstance(other, CreateSecretEventRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
