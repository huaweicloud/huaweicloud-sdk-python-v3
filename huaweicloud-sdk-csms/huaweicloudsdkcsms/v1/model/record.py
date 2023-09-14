# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Record:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_name': 'str',
        'trigger_event_type': 'str',
        'create_time': 'int',
        'secret_name': 'str',
        'secret_type': 'str',
        'notification_target_name': 'str',
        'notification_target_id': 'str',
        'notification_content': 'str',
        'notification_status': 'str'
    }

    attribute_map = {
        'event_name': 'event_name',
        'trigger_event_type': 'trigger_event_type',
        'create_time': 'create_time',
        'secret_name': 'secret_name',
        'secret_type': 'secret_type',
        'notification_target_name': 'notification_target_name',
        'notification_target_id': 'notification_target_id',
        'notification_content': 'notification_content',
        'notification_status': 'notification_status'
    }

    def __init__(self, event_name=None, trigger_event_type=None, create_time=None, secret_name=None, secret_type=None, notification_target_name=None, notification_target_id=None, notification_content=None, notification_status=None):
        """Record

        The model defined in huaweicloud sdk

        :param event_name: 凭据名称。
        :type event_name: str
        :param trigger_event_type: 凭据类型  取值 ： COMMON ：通用凭据 RDS ：RDS凭据 
        :type trigger_event_type: str
        :param create_time: 事件通知记录的创建时间，时间戳，即从1970年1月1日至该时间的总秒数。 
        :type create_time: int
        :param secret_name: 凭据名称。
        :type secret_name: str
        :param secret_type: 凭据类型  取值 ： COMMON ：通用凭据(默认)。用于应用系统中的各种敏感信息储存。         RDS ：RDS凭据 。专门针对RDS的凭据，用于存储RDS的账号信息。 
        :type secret_type: str
        :param notification_target_name: 事件通知的对象名称。
        :type notification_target_name: str
        :param notification_target_id: 事件通知的对象ID。
        :type notification_target_id: str
        :param notification_content: 凭据的描述信息。
        :type notification_content: str
        :param notification_status: 凭据类型  取值 ： SUCCESS ：事件通知成功。         FAIL ：事件通知失败。         INVALID ：事件通知配置主题信息无效或不正确，无法触发通知。 
        :type notification_status: str
        """
        
        

        self._event_name = None
        self._trigger_event_type = None
        self._create_time = None
        self._secret_name = None
        self._secret_type = None
        self._notification_target_name = None
        self._notification_target_id = None
        self._notification_content = None
        self._notification_status = None
        self.discriminator = None

        if event_name is not None:
            self.event_name = event_name
        if trigger_event_type is not None:
            self.trigger_event_type = trigger_event_type
        if create_time is not None:
            self.create_time = create_time
        if secret_name is not None:
            self.secret_name = secret_name
        if secret_type is not None:
            self.secret_type = secret_type
        if notification_target_name is not None:
            self.notification_target_name = notification_target_name
        if notification_target_id is not None:
            self.notification_target_id = notification_target_id
        if notification_content is not None:
            self.notification_content = notification_content
        if notification_status is not None:
            self.notification_status = notification_status

    @property
    def event_name(self):
        """Gets the event_name of this Record.

        凭据名称。

        :return: The event_name of this Record.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this Record.

        凭据名称。

        :param event_name: The event_name of this Record.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def trigger_event_type(self):
        """Gets the trigger_event_type of this Record.

        凭据类型  取值 ： COMMON ：通用凭据 RDS ：RDS凭据 

        :return: The trigger_event_type of this Record.
        :rtype: str
        """
        return self._trigger_event_type

    @trigger_event_type.setter
    def trigger_event_type(self, trigger_event_type):
        """Sets the trigger_event_type of this Record.

        凭据类型  取值 ： COMMON ：通用凭据 RDS ：RDS凭据 

        :param trigger_event_type: The trigger_event_type of this Record.
        :type trigger_event_type: str
        """
        self._trigger_event_type = trigger_event_type

    @property
    def create_time(self):
        """Gets the create_time of this Record.

        事件通知记录的创建时间，时间戳，即从1970年1月1日至该时间的总秒数。 

        :return: The create_time of this Record.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Record.

        事件通知记录的创建时间，时间戳，即从1970年1月1日至该时间的总秒数。 

        :param create_time: The create_time of this Record.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def secret_name(self):
        """Gets the secret_name of this Record.

        凭据名称。

        :return: The secret_name of this Record.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """Sets the secret_name of this Record.

        凭据名称。

        :param secret_name: The secret_name of this Record.
        :type secret_name: str
        """
        self._secret_name = secret_name

    @property
    def secret_type(self):
        """Gets the secret_type of this Record.

        凭据类型  取值 ： COMMON ：通用凭据(默认)。用于应用系统中的各种敏感信息储存。         RDS ：RDS凭据 。专门针对RDS的凭据，用于存储RDS的账号信息。 

        :return: The secret_type of this Record.
        :rtype: str
        """
        return self._secret_type

    @secret_type.setter
    def secret_type(self, secret_type):
        """Sets the secret_type of this Record.

        凭据类型  取值 ： COMMON ：通用凭据(默认)。用于应用系统中的各种敏感信息储存。         RDS ：RDS凭据 。专门针对RDS的凭据，用于存储RDS的账号信息。 

        :param secret_type: The secret_type of this Record.
        :type secret_type: str
        """
        self._secret_type = secret_type

    @property
    def notification_target_name(self):
        """Gets the notification_target_name of this Record.

        事件通知的对象名称。

        :return: The notification_target_name of this Record.
        :rtype: str
        """
        return self._notification_target_name

    @notification_target_name.setter
    def notification_target_name(self, notification_target_name):
        """Sets the notification_target_name of this Record.

        事件通知的对象名称。

        :param notification_target_name: The notification_target_name of this Record.
        :type notification_target_name: str
        """
        self._notification_target_name = notification_target_name

    @property
    def notification_target_id(self):
        """Gets the notification_target_id of this Record.

        事件通知的对象ID。

        :return: The notification_target_id of this Record.
        :rtype: str
        """
        return self._notification_target_id

    @notification_target_id.setter
    def notification_target_id(self, notification_target_id):
        """Sets the notification_target_id of this Record.

        事件通知的对象ID。

        :param notification_target_id: The notification_target_id of this Record.
        :type notification_target_id: str
        """
        self._notification_target_id = notification_target_id

    @property
    def notification_content(self):
        """Gets the notification_content of this Record.

        凭据的描述信息。

        :return: The notification_content of this Record.
        :rtype: str
        """
        return self._notification_content

    @notification_content.setter
    def notification_content(self, notification_content):
        """Sets the notification_content of this Record.

        凭据的描述信息。

        :param notification_content: The notification_content of this Record.
        :type notification_content: str
        """
        self._notification_content = notification_content

    @property
    def notification_status(self):
        """Gets the notification_status of this Record.

        凭据类型  取值 ： SUCCESS ：事件通知成功。         FAIL ：事件通知失败。         INVALID ：事件通知配置主题信息无效或不正确，无法触发通知。 

        :return: The notification_status of this Record.
        :rtype: str
        """
        return self._notification_status

    @notification_status.setter
    def notification_status(self, notification_status):
        """Sets the notification_status of this Record.

        凭据类型  取值 ： SUCCESS ：事件通知成功。         FAIL ：事件通知失败。         INVALID ：事件通知配置主题信息无效或不正确，无法触发通知。 

        :param notification_status: The notification_status of this Record.
        :type notification_status: str
        """
        self._notification_status = notification_status

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
        if not isinstance(other, Record):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
