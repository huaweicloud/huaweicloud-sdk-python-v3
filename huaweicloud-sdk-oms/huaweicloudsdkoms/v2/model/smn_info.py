# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmnInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notify_result': 'bool',
        'notify_error_message': 'str',
        'topic_name': 'str'
    }

    attribute_map = {
        'notify_result': 'notify_result',
        'notify_error_message': 'notify_error_message',
        'topic_name': 'topic_name'
    }

    def __init__(self, notify_result=None, notify_error_message=None, topic_name=None):
        """SmnInfo

        The model defined in huaweicloud sdk

        :param notify_result: 记录迁移任务执行完毕后SMN消息是否发送成功。
        :type notify_result: bool
        :param notify_error_message: 记录SMN消息发送失败原因的错误码（迁移任务成功时为空）。
        :type notify_error_message: str
        :param topic_name: SMN Topic的名称（SMN消息发送成功时为空）。
        :type topic_name: str
        """
        
        

        self._notify_result = None
        self._notify_error_message = None
        self._topic_name = None
        self.discriminator = None

        if notify_result is not None:
            self.notify_result = notify_result
        if notify_error_message is not None:
            self.notify_error_message = notify_error_message
        if topic_name is not None:
            self.topic_name = topic_name

    @property
    def notify_result(self):
        """Gets the notify_result of this SmnInfo.

        记录迁移任务执行完毕后SMN消息是否发送成功。

        :return: The notify_result of this SmnInfo.
        :rtype: bool
        """
        return self._notify_result

    @notify_result.setter
    def notify_result(self, notify_result):
        """Sets the notify_result of this SmnInfo.

        记录迁移任务执行完毕后SMN消息是否发送成功。

        :param notify_result: The notify_result of this SmnInfo.
        :type notify_result: bool
        """
        self._notify_result = notify_result

    @property
    def notify_error_message(self):
        """Gets the notify_error_message of this SmnInfo.

        记录SMN消息发送失败原因的错误码（迁移任务成功时为空）。

        :return: The notify_error_message of this SmnInfo.
        :rtype: str
        """
        return self._notify_error_message

    @notify_error_message.setter
    def notify_error_message(self, notify_error_message):
        """Sets the notify_error_message of this SmnInfo.

        记录SMN消息发送失败原因的错误码（迁移任务成功时为空）。

        :param notify_error_message: The notify_error_message of this SmnInfo.
        :type notify_error_message: str
        """
        self._notify_error_message = notify_error_message

    @property
    def topic_name(self):
        """Gets the topic_name of this SmnInfo.

        SMN Topic的名称（SMN消息发送成功时为空）。

        :return: The topic_name of this SmnInfo.
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """Sets the topic_name of this SmnInfo.

        SMN Topic的名称（SMN消息发送成功时为空）。

        :param topic_name: The topic_name of this SmnInfo.
        :type topic_name: str
        """
        self._topic_name = topic_name

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
        if not isinstance(other, SmnInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
