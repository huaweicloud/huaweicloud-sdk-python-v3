# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAlarmSubResponse(SdkResponse):

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
        'enable': 'int',
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
        r"""CreateAlarmSubResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 告警订阅ID。 **取值范围**： 不涉及。
        :type id: str
        :param name: **参数解释**： 告警订阅名称。 **取值范围**： 不涉及。
        :type name: str
        :param enable: **参数解释**： 是否开启订阅。 **取值范围**： 不涉及。
        :type enable: int
        :param alarm_level: **参数解释**： 告警级别。 **取值范围**： 不涉及。
        :type alarm_level: str
        :param project_id: **参数解释**： 项目ID。 **取值范围**： 不涉及。
        :type project_id: str
        :param name_space: **参数解释**： 所属服务。 **取值范围**： 不涉及。
        :type name_space: str
        :param notification_target: **参数解释**： 消息主题地址。 **取值范围**： 不涉及。
        :type notification_target: str
        :param notification_target_name: **参数解释**： 消息主题名称。 **取值范围**： 不涉及。
        :type notification_target_name: str
        :param notification_target_type: **参数解释**： 消息主题类型。 **取值范围**： 不涉及。
        :type notification_target_type: str
        :param language: **参数解释**： 语言。 **取值范围**： 不涉及。
        :type language: str
        :param time_zone: **参数解释**： 时区。 **取值范围**： 不涉及。
        :type time_zone: str
        """
        
        super(CreateAlarmSubResponse, self).__init__()

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
        r"""Gets the id of this CreateAlarmSubResponse.

        **参数解释**： 告警订阅ID。 **取值范围**： 不涉及。

        :return: The id of this CreateAlarmSubResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateAlarmSubResponse.

        **参数解释**： 告警订阅ID。 **取值范围**： 不涉及。

        :param id: The id of this CreateAlarmSubResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateAlarmSubResponse.

        **参数解释**： 告警订阅名称。 **取值范围**： 不涉及。

        :return: The name of this CreateAlarmSubResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateAlarmSubResponse.

        **参数解释**： 告警订阅名称。 **取值范围**： 不涉及。

        :param name: The name of this CreateAlarmSubResponse.
        :type name: str
        """
        self._name = name

    @property
    def enable(self):
        r"""Gets the enable of this CreateAlarmSubResponse.

        **参数解释**： 是否开启订阅。 **取值范围**： 不涉及。

        :return: The enable of this CreateAlarmSubResponse.
        :rtype: int
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this CreateAlarmSubResponse.

        **参数解释**： 是否开启订阅。 **取值范围**： 不涉及。

        :param enable: The enable of this CreateAlarmSubResponse.
        :type enable: int
        """
        self._enable = enable

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this CreateAlarmSubResponse.

        **参数解释**： 告警级别。 **取值范围**： 不涉及。

        :return: The alarm_level of this CreateAlarmSubResponse.
        :rtype: str
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this CreateAlarmSubResponse.

        **参数解释**： 告警级别。 **取值范围**： 不涉及。

        :param alarm_level: The alarm_level of this CreateAlarmSubResponse.
        :type alarm_level: str
        """
        self._alarm_level = alarm_level

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateAlarmSubResponse.

        **参数解释**： 项目ID。 **取值范围**： 不涉及。

        :return: The project_id of this CreateAlarmSubResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateAlarmSubResponse.

        **参数解释**： 项目ID。 **取值范围**： 不涉及。

        :param project_id: The project_id of this CreateAlarmSubResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name_space(self):
        r"""Gets the name_space of this CreateAlarmSubResponse.

        **参数解释**： 所属服务。 **取值范围**： 不涉及。

        :return: The name_space of this CreateAlarmSubResponse.
        :rtype: str
        """
        return self._name_space

    @name_space.setter
    def name_space(self, name_space):
        r"""Sets the name_space of this CreateAlarmSubResponse.

        **参数解释**： 所属服务。 **取值范围**： 不涉及。

        :param name_space: The name_space of this CreateAlarmSubResponse.
        :type name_space: str
        """
        self._name_space = name_space

    @property
    def notification_target(self):
        r"""Gets the notification_target of this CreateAlarmSubResponse.

        **参数解释**： 消息主题地址。 **取值范围**： 不涉及。

        :return: The notification_target of this CreateAlarmSubResponse.
        :rtype: str
        """
        return self._notification_target

    @notification_target.setter
    def notification_target(self, notification_target):
        r"""Sets the notification_target of this CreateAlarmSubResponse.

        **参数解释**： 消息主题地址。 **取值范围**： 不涉及。

        :param notification_target: The notification_target of this CreateAlarmSubResponse.
        :type notification_target: str
        """
        self._notification_target = notification_target

    @property
    def notification_target_name(self):
        r"""Gets the notification_target_name of this CreateAlarmSubResponse.

        **参数解释**： 消息主题名称。 **取值范围**： 不涉及。

        :return: The notification_target_name of this CreateAlarmSubResponse.
        :rtype: str
        """
        return self._notification_target_name

    @notification_target_name.setter
    def notification_target_name(self, notification_target_name):
        r"""Sets the notification_target_name of this CreateAlarmSubResponse.

        **参数解释**： 消息主题名称。 **取值范围**： 不涉及。

        :param notification_target_name: The notification_target_name of this CreateAlarmSubResponse.
        :type notification_target_name: str
        """
        self._notification_target_name = notification_target_name

    @property
    def notification_target_type(self):
        r"""Gets the notification_target_type of this CreateAlarmSubResponse.

        **参数解释**： 消息主题类型。 **取值范围**： 不涉及。

        :return: The notification_target_type of this CreateAlarmSubResponse.
        :rtype: str
        """
        return self._notification_target_type

    @notification_target_type.setter
    def notification_target_type(self, notification_target_type):
        r"""Sets the notification_target_type of this CreateAlarmSubResponse.

        **参数解释**： 消息主题类型。 **取值范围**： 不涉及。

        :param notification_target_type: The notification_target_type of this CreateAlarmSubResponse.
        :type notification_target_type: str
        """
        self._notification_target_type = notification_target_type

    @property
    def language(self):
        r"""Gets the language of this CreateAlarmSubResponse.

        **参数解释**： 语言。 **取值范围**： 不涉及。

        :return: The language of this CreateAlarmSubResponse.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this CreateAlarmSubResponse.

        **参数解释**： 语言。 **取值范围**： 不涉及。

        :param language: The language of this CreateAlarmSubResponse.
        :type language: str
        """
        self._language = language

    @property
    def time_zone(self):
        r"""Gets the time_zone of this CreateAlarmSubResponse.

        **参数解释**： 时区。 **取值范围**： 不涉及。

        :return: The time_zone of this CreateAlarmSubResponse.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this CreateAlarmSubResponse.

        **参数解释**： 时区。 **取值范围**： 不涉及。

        :param time_zone: The time_zone of this CreateAlarmSubResponse.
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
        if not isinstance(other, CreateAlarmSubResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
