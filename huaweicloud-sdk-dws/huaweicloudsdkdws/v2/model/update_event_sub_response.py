# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEventSubResponse(SdkResponse):

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
        'source_type': 'str',
        'source_id': 'str',
        'category': 'str',
        'severity': 'str',
        'tag': 'str',
        'enable': 'int',
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
        'source_type': 'source_type',
        'source_id': 'source_id',
        'category': 'category',
        'severity': 'severity',
        'tag': 'tag',
        'enable': 'enable',
        'project_id': 'project_id',
        'name_space': 'name_space',
        'notification_target': 'notification_target',
        'notification_target_name': 'notification_target_name',
        'notification_target_type': 'notification_target_type',
        'language': 'language',
        'time_zone': 'time_zone'
    }

    def __init__(self, id=None, name=None, source_type=None, source_id=None, category=None, severity=None, tag=None, enable=None, project_id=None, name_space=None, notification_target=None, notification_target_name=None, notification_target_type=None, language=None, time_zone=None):
        """UpdateEventSubResponse

        The model defined in huaweicloud sdk

        :param id: 订阅ID
        :type id: str
        :param name: 订阅名称
        :type name: str
        :param source_type: 事件源类型
        :type source_type: str
        :param source_id: 事件源ID
        :type source_id: str
        :param category: 事件类别
        :type category: str
        :param severity: 事件级别
        :type severity: str
        :param tag: 事件标签
        :type tag: str
        :param enable: 是否开启订阅 1为开启，0为关闭
        :type enable: int
        :param project_id: 租户凭证ID
        :type project_id: str
        :param name_space: 所属服务
        :type name_space: str
        :param notification_target: 消息通知主题地址
        :type notification_target: str
        :param notification_target_name: 消息通知主题名称
        :type notification_target_name: str
        :param notification_target_type: 消息通知类型
        :type notification_target_type: str
        :param language: 语言
        :type language: str
        :param time_zone: 时区
        :type time_zone: str
        """
        
        super(UpdateEventSubResponse, self).__init__()

        self._id = None
        self._name = None
        self._source_type = None
        self._source_id = None
        self._category = None
        self._severity = None
        self._tag = None
        self._enable = None
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
        if source_type is not None:
            self.source_type = source_type
        if source_id is not None:
            self.source_id = source_id
        if category is not None:
            self.category = category
        if severity is not None:
            self.severity = severity
        if tag is not None:
            self.tag = tag
        if enable is not None:
            self.enable = enable
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
        """Gets the id of this UpdateEventSubResponse.

        订阅ID

        :return: The id of this UpdateEventSubResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateEventSubResponse.

        订阅ID

        :param id: The id of this UpdateEventSubResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateEventSubResponse.

        订阅名称

        :return: The name of this UpdateEventSubResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateEventSubResponse.

        订阅名称

        :param name: The name of this UpdateEventSubResponse.
        :type name: str
        """
        self._name = name

    @property
    def source_type(self):
        """Gets the source_type of this UpdateEventSubResponse.

        事件源类型

        :return: The source_type of this UpdateEventSubResponse.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this UpdateEventSubResponse.

        事件源类型

        :param source_type: The source_type of this UpdateEventSubResponse.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def source_id(self):
        """Gets the source_id of this UpdateEventSubResponse.

        事件源ID

        :return: The source_id of this UpdateEventSubResponse.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this UpdateEventSubResponse.

        事件源ID

        :param source_id: The source_id of this UpdateEventSubResponse.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def category(self):
        """Gets the category of this UpdateEventSubResponse.

        事件类别

        :return: The category of this UpdateEventSubResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this UpdateEventSubResponse.

        事件类别

        :param category: The category of this UpdateEventSubResponse.
        :type category: str
        """
        self._category = category

    @property
    def severity(self):
        """Gets the severity of this UpdateEventSubResponse.

        事件级别

        :return: The severity of this UpdateEventSubResponse.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this UpdateEventSubResponse.

        事件级别

        :param severity: The severity of this UpdateEventSubResponse.
        :type severity: str
        """
        self._severity = severity

    @property
    def tag(self):
        """Gets the tag of this UpdateEventSubResponse.

        事件标签

        :return: The tag of this UpdateEventSubResponse.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this UpdateEventSubResponse.

        事件标签

        :param tag: The tag of this UpdateEventSubResponse.
        :type tag: str
        """
        self._tag = tag

    @property
    def enable(self):
        """Gets the enable of this UpdateEventSubResponse.

        是否开启订阅 1为开启，0为关闭

        :return: The enable of this UpdateEventSubResponse.
        :rtype: int
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this UpdateEventSubResponse.

        是否开启订阅 1为开启，0为关闭

        :param enable: The enable of this UpdateEventSubResponse.
        :type enable: int
        """
        self._enable = enable

    @property
    def project_id(self):
        """Gets the project_id of this UpdateEventSubResponse.

        租户凭证ID

        :return: The project_id of this UpdateEventSubResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UpdateEventSubResponse.

        租户凭证ID

        :param project_id: The project_id of this UpdateEventSubResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name_space(self):
        """Gets the name_space of this UpdateEventSubResponse.

        所属服务

        :return: The name_space of this UpdateEventSubResponse.
        :rtype: str
        """
        return self._name_space

    @name_space.setter
    def name_space(self, name_space):
        """Sets the name_space of this UpdateEventSubResponse.

        所属服务

        :param name_space: The name_space of this UpdateEventSubResponse.
        :type name_space: str
        """
        self._name_space = name_space

    @property
    def notification_target(self):
        """Gets the notification_target of this UpdateEventSubResponse.

        消息通知主题地址

        :return: The notification_target of this UpdateEventSubResponse.
        :rtype: str
        """
        return self._notification_target

    @notification_target.setter
    def notification_target(self, notification_target):
        """Sets the notification_target of this UpdateEventSubResponse.

        消息通知主题地址

        :param notification_target: The notification_target of this UpdateEventSubResponse.
        :type notification_target: str
        """
        self._notification_target = notification_target

    @property
    def notification_target_name(self):
        """Gets the notification_target_name of this UpdateEventSubResponse.

        消息通知主题名称

        :return: The notification_target_name of this UpdateEventSubResponse.
        :rtype: str
        """
        return self._notification_target_name

    @notification_target_name.setter
    def notification_target_name(self, notification_target_name):
        """Sets the notification_target_name of this UpdateEventSubResponse.

        消息通知主题名称

        :param notification_target_name: The notification_target_name of this UpdateEventSubResponse.
        :type notification_target_name: str
        """
        self._notification_target_name = notification_target_name

    @property
    def notification_target_type(self):
        """Gets the notification_target_type of this UpdateEventSubResponse.

        消息通知类型

        :return: The notification_target_type of this UpdateEventSubResponse.
        :rtype: str
        """
        return self._notification_target_type

    @notification_target_type.setter
    def notification_target_type(self, notification_target_type):
        """Sets the notification_target_type of this UpdateEventSubResponse.

        消息通知类型

        :param notification_target_type: The notification_target_type of this UpdateEventSubResponse.
        :type notification_target_type: str
        """
        self._notification_target_type = notification_target_type

    @property
    def language(self):
        """Gets the language of this UpdateEventSubResponse.

        语言

        :return: The language of this UpdateEventSubResponse.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this UpdateEventSubResponse.

        语言

        :param language: The language of this UpdateEventSubResponse.
        :type language: str
        """
        self._language = language

    @property
    def time_zone(self):
        """Gets the time_zone of this UpdateEventSubResponse.

        时区

        :return: The time_zone of this UpdateEventSubResponse.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this UpdateEventSubResponse.

        时区

        :param time_zone: The time_zone of this UpdateEventSubResponse.
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
        if not isinstance(other, UpdateEventSubResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
