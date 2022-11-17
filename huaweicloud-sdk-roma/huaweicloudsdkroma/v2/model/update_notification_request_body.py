# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNotificationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic': 'str',
        'status': 'int'
    }

    attribute_map = {
        'topic': 'topic',
        'status': 'status'
    }

    def __init__(self, topic=None, status=None):
        """UpdateNotificationRequestBody

        The model defined in huaweicloud sdk

        :param topic: 通知发送的主题名，该主题需要在MQS存在
        :type topic: str
        :param status: 启停状态 0-启用 1-停用
        :type status: int
        """
        
        

        self._topic = None
        self._status = None
        self.discriminator = None

        self.topic = topic
        self.status = status

    @property
    def topic(self):
        """Gets the topic of this UpdateNotificationRequestBody.

        通知发送的主题名，该主题需要在MQS存在

        :return: The topic of this UpdateNotificationRequestBody.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this UpdateNotificationRequestBody.

        通知发送的主题名，该主题需要在MQS存在

        :param topic: The topic of this UpdateNotificationRequestBody.
        :type topic: str
        """
        self._topic = topic

    @property
    def status(self):
        """Gets the status of this UpdateNotificationRequestBody.

        启停状态 0-启用 1-停用

        :return: The status of this UpdateNotificationRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateNotificationRequestBody.

        启停状态 0-启用 1-停用

        :param status: The status of this UpdateNotificationRequestBody.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, UpdateNotificationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
