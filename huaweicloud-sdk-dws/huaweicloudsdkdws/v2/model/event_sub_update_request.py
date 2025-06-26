# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventSubUpdateRequest:

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
        'notification_target_type': 'str'
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
        'notification_target_type': 'notification_target_type'
    }

    def __init__(self, name=None, source_type=None, source_id=None, category=None, severity=None, tag=None, enable=None, notification_target=None, notification_target_name=None, notification_target_type=None):
        r"""EventSubUpdateRequest

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 事件订阅名称。 **取值范围**： 不涉及。
        :type name: str
        :param source_type: **参数解释**： 事件源类型。 **取值范围**： 支持cluster，backup，disaster-recovery。
        :type source_type: str
        :param source_id: **参数解释**： 事件源ID。 **取值范围**： 不涉及。
        :type source_id: str
        :param category: **参数解释**： 事件类别。 **取值范围**： 支持management、monitor、security、system alarm。
        :type category: str
        :param severity: **参数解释**： 事件级别。 **取值范围**： 支持normal、warning。
        :type severity: str
        :param tag: **参数解释**： 事件标签。 **取值范围**： 不涉及。
        :type tag: str
        :param enable: **参数解释**： 是否开启订阅。 **取值范围**： 1为开启，0为关闭。
        :type enable: int
        :param notification_target: **参数解释**： 消息通知地址。 **取值范围**： 不涉及。
        :type notification_target: str
        :param notification_target_name: **参数解释**： 消息主题名称。 **取值范围**： 不涉及。
        :type notification_target_name: str
        :param notification_target_type: **参数解释**： 消息通知类型。只支持SMN。 **取值范围**： SMN。
        :type notification_target_type: str
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
        if enable is not None:
            self.enable = enable
        self.notification_target = notification_target
        self.notification_target_name = notification_target_name
        self.notification_target_type = notification_target_type

    @property
    def name(self):
        r"""Gets the name of this EventSubUpdateRequest.

        **参数解释**： 事件订阅名称。 **取值范围**： 不涉及。

        :return: The name of this EventSubUpdateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EventSubUpdateRequest.

        **参数解释**： 事件订阅名称。 **取值范围**： 不涉及。

        :param name: The name of this EventSubUpdateRequest.
        :type name: str
        """
        self._name = name

    @property
    def source_type(self):
        r"""Gets the source_type of this EventSubUpdateRequest.

        **参数解释**： 事件源类型。 **取值范围**： 支持cluster，backup，disaster-recovery。

        :return: The source_type of this EventSubUpdateRequest.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this EventSubUpdateRequest.

        **参数解释**： 事件源类型。 **取值范围**： 支持cluster，backup，disaster-recovery。

        :param source_type: The source_type of this EventSubUpdateRequest.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def source_id(self):
        r"""Gets the source_id of this EventSubUpdateRequest.

        **参数解释**： 事件源ID。 **取值范围**： 不涉及。

        :return: The source_id of this EventSubUpdateRequest.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this EventSubUpdateRequest.

        **参数解释**： 事件源ID。 **取值范围**： 不涉及。

        :param source_id: The source_id of this EventSubUpdateRequest.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def category(self):
        r"""Gets the category of this EventSubUpdateRequest.

        **参数解释**： 事件类别。 **取值范围**： 支持management、monitor、security、system alarm。

        :return: The category of this EventSubUpdateRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this EventSubUpdateRequest.

        **参数解释**： 事件类别。 **取值范围**： 支持management、monitor、security、system alarm。

        :param category: The category of this EventSubUpdateRequest.
        :type category: str
        """
        self._category = category

    @property
    def severity(self):
        r"""Gets the severity of this EventSubUpdateRequest.

        **参数解释**： 事件级别。 **取值范围**： 支持normal、warning。

        :return: The severity of this EventSubUpdateRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this EventSubUpdateRequest.

        **参数解释**： 事件级别。 **取值范围**： 支持normal、warning。

        :param severity: The severity of this EventSubUpdateRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def tag(self):
        r"""Gets the tag of this EventSubUpdateRequest.

        **参数解释**： 事件标签。 **取值范围**： 不涉及。

        :return: The tag of this EventSubUpdateRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this EventSubUpdateRequest.

        **参数解释**： 事件标签。 **取值范围**： 不涉及。

        :param tag: The tag of this EventSubUpdateRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def enable(self):
        r"""Gets the enable of this EventSubUpdateRequest.

        **参数解释**： 是否开启订阅。 **取值范围**： 1为开启，0为关闭。

        :return: The enable of this EventSubUpdateRequest.
        :rtype: int
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this EventSubUpdateRequest.

        **参数解释**： 是否开启订阅。 **取值范围**： 1为开启，0为关闭。

        :param enable: The enable of this EventSubUpdateRequest.
        :type enable: int
        """
        self._enable = enable

    @property
    def notification_target(self):
        r"""Gets the notification_target of this EventSubUpdateRequest.

        **参数解释**： 消息通知地址。 **取值范围**： 不涉及。

        :return: The notification_target of this EventSubUpdateRequest.
        :rtype: str
        """
        return self._notification_target

    @notification_target.setter
    def notification_target(self, notification_target):
        r"""Sets the notification_target of this EventSubUpdateRequest.

        **参数解释**： 消息通知地址。 **取值范围**： 不涉及。

        :param notification_target: The notification_target of this EventSubUpdateRequest.
        :type notification_target: str
        """
        self._notification_target = notification_target

    @property
    def notification_target_name(self):
        r"""Gets the notification_target_name of this EventSubUpdateRequest.

        **参数解释**： 消息主题名称。 **取值范围**： 不涉及。

        :return: The notification_target_name of this EventSubUpdateRequest.
        :rtype: str
        """
        return self._notification_target_name

    @notification_target_name.setter
    def notification_target_name(self, notification_target_name):
        r"""Sets the notification_target_name of this EventSubUpdateRequest.

        **参数解释**： 消息主题名称。 **取值范围**： 不涉及。

        :param notification_target_name: The notification_target_name of this EventSubUpdateRequest.
        :type notification_target_name: str
        """
        self._notification_target_name = notification_target_name

    @property
    def notification_target_type(self):
        r"""Gets the notification_target_type of this EventSubUpdateRequest.

        **参数解释**： 消息通知类型。只支持SMN。 **取值范围**： SMN。

        :return: The notification_target_type of this EventSubUpdateRequest.
        :rtype: str
        """
        return self._notification_target_type

    @notification_target_type.setter
    def notification_target_type(self, notification_target_type):
        r"""Sets the notification_target_type of this EventSubUpdateRequest.

        **参数解释**： 消息通知类型。只支持SMN。 **取值范围**： SMN。

        :param notification_target_type: The notification_target_type of this EventSubUpdateRequest.
        :type notification_target_type: str
        """
        self._notification_target_type = notification_target_type

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
        if not isinstance(other, EventSubUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
