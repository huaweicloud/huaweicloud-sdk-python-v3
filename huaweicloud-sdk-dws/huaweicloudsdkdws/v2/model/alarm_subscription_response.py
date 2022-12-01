# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmSubscriptionResponse:

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
        'enable': 'str',
        'alarm_level': 'str',
        'project_id': 'str',
        'name_space': 'str',
        'notification_target': 'str',
        'notification_target_name': 'str',
        'notification_target_type': 'str',
        'language': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'enable': 'enable',
        'alarm_level': 'alarm_level',
        'project_id': 'project_id',
        'name_space': 'name_space',
        'notification_target': 'notification_target',
        'notification_target_name': 'notification_target_name',
        'notification_target_type': 'notification_target_type',
        'language': 'language',
        'time_zone': 'time_zone'
    }

    def __init__(self, id=None, name=None, enable=None, alarm_level=None, project_id=None, name_space=None, notification_target=None, notification_target_name=None, notification_target_type=None, language=None, time_zone=None):
        """AlarmSubscriptionResponse

        The model defined in huaweicloud sdk

        :param id: 告警订阅ID
        :type id: str
        :param name: 告警订阅名称
        :type name: str
        :param enable: 是否开启订阅
        :type enable: str
        :param alarm_level: 告警级别
        :type alarm_level: str
        :param project_id: 租户凭证ID
        :type project_id: str
        :param name_space: 所属服务，支持DWS,DLI,DGC,CloudTable,CDM,GES,CSS
        :type name_space: str
        :param notification_target: 消息主题地址
        :type notification_target: str
        :param notification_target_name: 消息主题名称
        :type notification_target_name: str
        :param notification_target_type: 消息主题类型
        :type notification_target_type: str
        :param language: 语言
        :type language: str
        :param time_zone: 时区
        :type time_zone: str
        """
        
        

        self._id = None
        self._name = None
        self._enable = None
        self._alarm_level = None
        self._project_id = None
        self._name_space = None
        self._notification_target = None
        self._notification_target_name = None
        self._notification_target_type = None
        self._language = None
        self._time_zone = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if enable is not None:
            self.enable = enable
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if project_id is not None:
            self.project_id = project_id
        if name_space is not None:
            self.name_space = name_space
        if notification_target is not None:
            self.notification_target = notification_target
        if notification_target_name is not None:
            self.notification_target_name = notification_target_name
        if notification_target_type is not None:
            self.notification_target_type = notification_target_type
        if language is not None:
            self.language = language
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def id(self):
        """Gets the id of this AlarmSubscriptionResponse.

        告警订阅ID

        :return: The id of this AlarmSubscriptionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlarmSubscriptionResponse.

        告警订阅ID

        :param id: The id of this AlarmSubscriptionResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AlarmSubscriptionResponse.

        告警订阅名称

        :return: The name of this AlarmSubscriptionResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AlarmSubscriptionResponse.

        告警订阅名称

        :param name: The name of this AlarmSubscriptionResponse.
        :type name: str
        """
        self._name = name

    @property
    def enable(self):
        """Gets the enable of this AlarmSubscriptionResponse.

        是否开启订阅

        :return: The enable of this AlarmSubscriptionResponse.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this AlarmSubscriptionResponse.

        是否开启订阅

        :param enable: The enable of this AlarmSubscriptionResponse.
        :type enable: str
        """
        self._enable = enable

    @property
    def alarm_level(self):
        """Gets the alarm_level of this AlarmSubscriptionResponse.

        告警级别

        :return: The alarm_level of this AlarmSubscriptionResponse.
        :rtype: str
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this AlarmSubscriptionResponse.

        告警级别

        :param alarm_level: The alarm_level of this AlarmSubscriptionResponse.
        :type alarm_level: str
        """
        self._alarm_level = alarm_level

    @property
    def project_id(self):
        """Gets the project_id of this AlarmSubscriptionResponse.

        租户凭证ID

        :return: The project_id of this AlarmSubscriptionResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AlarmSubscriptionResponse.

        租户凭证ID

        :param project_id: The project_id of this AlarmSubscriptionResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name_space(self):
        """Gets the name_space of this AlarmSubscriptionResponse.

        所属服务，支持DWS,DLI,DGC,CloudTable,CDM,GES,CSS

        :return: The name_space of this AlarmSubscriptionResponse.
        :rtype: str
        """
        return self._name_space

    @name_space.setter
    def name_space(self, name_space):
        """Sets the name_space of this AlarmSubscriptionResponse.

        所属服务，支持DWS,DLI,DGC,CloudTable,CDM,GES,CSS

        :param name_space: The name_space of this AlarmSubscriptionResponse.
        :type name_space: str
        """
        self._name_space = name_space

    @property
    def notification_target(self):
        """Gets the notification_target of this AlarmSubscriptionResponse.

        消息主题地址

        :return: The notification_target of this AlarmSubscriptionResponse.
        :rtype: str
        """
        return self._notification_target

    @notification_target.setter
    def notification_target(self, notification_target):
        """Sets the notification_target of this AlarmSubscriptionResponse.

        消息主题地址

        :param notification_target: The notification_target of this AlarmSubscriptionResponse.
        :type notification_target: str
        """
        self._notification_target = notification_target

    @property
    def notification_target_name(self):
        """Gets the notification_target_name of this AlarmSubscriptionResponse.

        消息主题名称

        :return: The notification_target_name of this AlarmSubscriptionResponse.
        :rtype: str
        """
        return self._notification_target_name

    @notification_target_name.setter
    def notification_target_name(self, notification_target_name):
        """Sets the notification_target_name of this AlarmSubscriptionResponse.

        消息主题名称

        :param notification_target_name: The notification_target_name of this AlarmSubscriptionResponse.
        :type notification_target_name: str
        """
        self._notification_target_name = notification_target_name

    @property
    def notification_target_type(self):
        """Gets the notification_target_type of this AlarmSubscriptionResponse.

        消息主题类型

        :return: The notification_target_type of this AlarmSubscriptionResponse.
        :rtype: str
        """
        return self._notification_target_type

    @notification_target_type.setter
    def notification_target_type(self, notification_target_type):
        """Sets the notification_target_type of this AlarmSubscriptionResponse.

        消息主题类型

        :param notification_target_type: The notification_target_type of this AlarmSubscriptionResponse.
        :type notification_target_type: str
        """
        self._notification_target_type = notification_target_type

    @property
    def language(self):
        """Gets the language of this AlarmSubscriptionResponse.

        语言

        :return: The language of this AlarmSubscriptionResponse.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AlarmSubscriptionResponse.

        语言

        :param language: The language of this AlarmSubscriptionResponse.
        :type language: str
        """
        self._language = language

    @property
    def time_zone(self):
        """Gets the time_zone of this AlarmSubscriptionResponse.

        时区

        :return: The time_zone of this AlarmSubscriptionResponse.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this AlarmSubscriptionResponse.

        时区

        :param time_zone: The time_zone of this AlarmSubscriptionResponse.
        :type time_zone: str
        """
        self._time_zone = time_zone

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
        if not isinstance(other, AlarmSubscriptionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
