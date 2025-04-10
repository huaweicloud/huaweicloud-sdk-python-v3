# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetConsumeOffsetReq:

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
        'timestamp': 'str'
    }

    attribute_map = {
        'topic': 'topic',
        'timestamp': 'timestamp'
    }

    def __init__(self, topic=None, timestamp=None):
        r"""ResetConsumeOffsetReq

        The model defined in huaweicloud sdk

        :param topic: 重置的主题。
        :type topic: str
        :param timestamp: 重置的时间。
        :type timestamp: str
        """
        
        

        self._topic = None
        self._timestamp = None
        self.discriminator = None

        self.topic = topic
        self.timestamp = timestamp

    @property
    def topic(self):
        r"""Gets the topic of this ResetConsumeOffsetReq.

        重置的主题。

        :return: The topic of this ResetConsumeOffsetReq.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this ResetConsumeOffsetReq.

        重置的主题。

        :param topic: The topic of this ResetConsumeOffsetReq.
        :type topic: str
        """
        self._topic = topic

    @property
    def timestamp(self):
        r"""Gets the timestamp of this ResetConsumeOffsetReq.

        重置的时间。

        :return: The timestamp of this ResetConsumeOffsetReq.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this ResetConsumeOffsetReq.

        重置的时间。

        :param timestamp: The timestamp of this ResetConsumeOffsetReq.
        :type timestamp: str
        """
        self._timestamp = timestamp

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
        if not isinstance(other, ResetConsumeOffsetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
