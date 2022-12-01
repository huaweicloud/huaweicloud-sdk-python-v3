# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventSubRequest:

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
        'source_type': 'str',
        'source_id': 'str',
        'category': 'str',
        'severity': 'str',
        'tag': 'str',
        'enable': 'int',
        'notification_target': 'str',
        'notification_target_name': 'str',
        'notification_target_type': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'name': 'name',
        'source_type': 'source_type',
        'source_id': 'source_id',
        'category': 'category',
        'severity': 'severity',
        'tag': 'tag',
        'enable': 'enable',
        'notification_target': 'notification_target',
        'notification_target_name': 'notification_target_name',
        'notification_target_type': 'notification_target_type',
        'time_zone': 'time_zone'
    }

    def __init__(self, name=None, source_type=None, source_id=None, category=None, severity=None, tag=None, enable=None, notification_target=None, notification_target_name=None, notification_target_type=None, time_zone=None):
        """EventSubRequest

        The model defined in huaweicloud sdk

        :param name: 事件订阅名称
        :type name: str
        :param source_type: 事件源类型支持cluster，backup，disaster-recovery
        :type source_type: str
        :param source_id: 事件源ID
        :type source_id: str
        :param category: 事件类别支持management，monitor，security，system alarm
        :type category: str
        :param severity: 事件级别支持normal，warning
        :type severity: str
        :param tag: 事件标签
        :type tag: str
        :param enable: 是否开启订阅 1为开启，0为关闭
        :type enable: int
        :param notification_target: 消息通知地址
        :type notification_target: str
        :param notification_target_name: 消息主题名称
        :type notification_target_name: str
        :param notification_target_type: 消息通知类型只支持SMN
        :type notification_target_type: str
        :param time_zone: 时区
        :type time_zone: str
        """
        
        

        self._name = None
        self._source_type = None
        self._source_id = None
        self._category = None
        self._severity = None
        self._tag = None
        self._enable = None
        self._notification_target = None
        self._notification_target_name = None
        self._notification_target_type = None
        self._time_zone = None
        self.discriminator = None

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
        self.enable = enable
        self.notification_target = notification_target
        self.notification_target_name = notification_target_name
        self.notification_target_type = notification_target_type
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def name(self):
        """Gets the name of this EventSubRequest.

        事件订阅名称

        :return: The name of this EventSubRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventSubRequest.

        事件订阅名称

        :param name: The name of this EventSubRequest.
        :type name: str
        """
        self._name = name

    @property
    def source_type(self):
        """Gets the source_type of this EventSubRequest.

        事件源类型支持cluster，backup，disaster-recovery

        :return: The source_type of this EventSubRequest.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this EventSubRequest.

        事件源类型支持cluster，backup，disaster-recovery

        :param source_type: The source_type of this EventSubRequest.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def source_id(self):
        """Gets the source_id of this EventSubRequest.

        事件源ID

        :return: The source_id of this EventSubRequest.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this EventSubRequest.

        事件源ID

        :param source_id: The source_id of this EventSubRequest.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def category(self):
        """Gets the category of this EventSubRequest.

        事件类别支持management，monitor，security，system alarm

        :return: The category of this EventSubRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this EventSubRequest.

        事件类别支持management，monitor，security，system alarm

        :param category: The category of this EventSubRequest.
        :type category: str
        """
        self._category = category

    @property
    def severity(self):
        """Gets the severity of this EventSubRequest.

        事件级别支持normal，warning

        :return: The severity of this EventSubRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this EventSubRequest.

        事件级别支持normal，warning

        :param severity: The severity of this EventSubRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def tag(self):
        """Gets the tag of this EventSubRequest.

        事件标签

        :return: The tag of this EventSubRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this EventSubRequest.

        事件标签

        :param tag: The tag of this EventSubRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def enable(self):
        """Gets the enable of this EventSubRequest.

        是否开启订阅 1为开启，0为关闭

        :return: The enable of this EventSubRequest.
        :rtype: int
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this EventSubRequest.

        是否开启订阅 1为开启，0为关闭

        :param enable: The enable of this EventSubRequest.
        :type enable: int
        """
        self._enable = enable

    @property
    def notification_target(self):
        """Gets the notification_target of this EventSubRequest.

        消息通知地址

        :return: The notification_target of this EventSubRequest.
        :rtype: str
        """
        return self._notification_target

    @notification_target.setter
    def notification_target(self, notification_target):
        """Sets the notification_target of this EventSubRequest.

        消息通知地址

        :param notification_target: The notification_target of this EventSubRequest.
        :type notification_target: str
        """
        self._notification_target = notification_target

    @property
    def notification_target_name(self):
        """Gets the notification_target_name of this EventSubRequest.

        消息主题名称

        :return: The notification_target_name of this EventSubRequest.
        :rtype: str
        """
        return self._notification_target_name

    @notification_target_name.setter
    def notification_target_name(self, notification_target_name):
        """Sets the notification_target_name of this EventSubRequest.

        消息主题名称

        :param notification_target_name: The notification_target_name of this EventSubRequest.
        :type notification_target_name: str
        """
        self._notification_target_name = notification_target_name

    @property
    def notification_target_type(self):
        """Gets the notification_target_type of this EventSubRequest.

        消息通知类型只支持SMN

        :return: The notification_target_type of this EventSubRequest.
        :rtype: str
        """
        return self._notification_target_type

    @notification_target_type.setter
    def notification_target_type(self, notification_target_type):
        """Sets the notification_target_type of this EventSubRequest.

        消息通知类型只支持SMN

        :param notification_target_type: The notification_target_type of this EventSubRequest.
        :type notification_target_type: str
        """
        self._notification_target_type = notification_target_type

    @property
    def time_zone(self):
        """Gets the time_zone of this EventSubRequest.

        时区

        :return: The time_zone of this EventSubRequest.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this EventSubRequest.

        时区

        :param time_zone: The time_zone of this EventSubRequest.
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
        if not isinstance(other, EventSubRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
