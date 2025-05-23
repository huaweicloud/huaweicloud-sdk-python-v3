# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMessageNotificationPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message_type': 'str',
        'name_pattern': 'str',
        'notification_types': 'list[str]',
        'topic_urn': 'str'
    }

    attribute_map = {
        'message_type': 'message_type',
        'name_pattern': 'name_pattern',
        'notification_types': 'notification_types',
        'topic_urn': 'topic_urn'
    }

    def __init__(self, message_type=None, name_pattern=None, notification_types=None, topic_urn=None):
        r"""CreateMessageNotificationPolicy

        The model defined in huaweicloud sdk

        :param message_type: 消息类型。job:任务执行结果。
        :type message_type: str
        :param name_pattern: 名称样式，用来匹配消息类型中所有符合该样式的消息。比如，message_type设置为job，name_pattern设置为ray_job*，表示匹配到所有以\&quot;ray_job\&quot;开头的job发出的消息。
        :type name_pattern: str
        :param notification_types: 通知类型。SUCCESS:成功通知；FAILED：失败通知
        :type notification_types: list[str]
        :param topic_urn: 消息通知主题。
        :type topic_urn: str
        """
        
        

        self._message_type = None
        self._name_pattern = None
        self._notification_types = None
        self._topic_urn = None
        self.discriminator = None

        self.message_type = message_type
        self.name_pattern = name_pattern
        self.notification_types = notification_types
        self.topic_urn = topic_urn

    @property
    def message_type(self):
        r"""Gets the message_type of this CreateMessageNotificationPolicy.

        消息类型。job:任务执行结果。

        :return: The message_type of this CreateMessageNotificationPolicy.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        r"""Sets the message_type of this CreateMessageNotificationPolicy.

        消息类型。job:任务执行结果。

        :param message_type: The message_type of this CreateMessageNotificationPolicy.
        :type message_type: str
        """
        self._message_type = message_type

    @property
    def name_pattern(self):
        r"""Gets the name_pattern of this CreateMessageNotificationPolicy.

        名称样式，用来匹配消息类型中所有符合该样式的消息。比如，message_type设置为job，name_pattern设置为ray_job*，表示匹配到所有以\"ray_job\"开头的job发出的消息。

        :return: The name_pattern of this CreateMessageNotificationPolicy.
        :rtype: str
        """
        return self._name_pattern

    @name_pattern.setter
    def name_pattern(self, name_pattern):
        r"""Sets the name_pattern of this CreateMessageNotificationPolicy.

        名称样式，用来匹配消息类型中所有符合该样式的消息。比如，message_type设置为job，name_pattern设置为ray_job*，表示匹配到所有以\"ray_job\"开头的job发出的消息。

        :param name_pattern: The name_pattern of this CreateMessageNotificationPolicy.
        :type name_pattern: str
        """
        self._name_pattern = name_pattern

    @property
    def notification_types(self):
        r"""Gets the notification_types of this CreateMessageNotificationPolicy.

        通知类型。SUCCESS:成功通知；FAILED：失败通知

        :return: The notification_types of this CreateMessageNotificationPolicy.
        :rtype: list[str]
        """
        return self._notification_types

    @notification_types.setter
    def notification_types(self, notification_types):
        r"""Sets the notification_types of this CreateMessageNotificationPolicy.

        通知类型。SUCCESS:成功通知；FAILED：失败通知

        :param notification_types: The notification_types of this CreateMessageNotificationPolicy.
        :type notification_types: list[str]
        """
        self._notification_types = notification_types

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this CreateMessageNotificationPolicy.

        消息通知主题。

        :return: The topic_urn of this CreateMessageNotificationPolicy.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this CreateMessageNotificationPolicy.

        消息通知主题。

        :param topic_urn: The topic_urn of this CreateMessageNotificationPolicy.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

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
        if not isinstance(other, CreateMessageNotificationPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
