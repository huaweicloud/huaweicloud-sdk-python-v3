# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriberInPic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'index': 'int',
        'subscriber': 'list[str]',
        'is_assist_stream': 'int'
    }

    attribute_map = {
        'index': 'index',
        'subscriber': 'subscriber',
        'is_assist_stream': 'isAssistStream'
    }

    def __init__(self, index=None, subscriber=None, is_assist_stream=None):
        """SubscriberInPic

        The model defined in huaweicloud sdk

        :param index: 多画面中每个画面的编号。编号从1开始。 默认值为1。
        :type index: int
        :param subscriber: 每个画面中与会者标识列表，从[[查询会议实时信息](https://support.huaweicloud.com/api-meeting/meeting_21_0029.html)](tag:hws)[[查询会议实时信息](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0029.html)](tag:hk)接口返回的pid中获取。
        :type subscriber: list[str]
        :param is_assist_stream: 是否为辅流。默认值为0。 - 0: 不是辅流 - 1: 是辅流
        :type is_assist_stream: int
        """
        
        

        self._index = None
        self._subscriber = None
        self._is_assist_stream = None
        self.discriminator = None

        self.index = index
        if subscriber is not None:
            self.subscriber = subscriber
        if is_assist_stream is not None:
            self.is_assist_stream = is_assist_stream

    @property
    def index(self):
        """Gets the index of this SubscriberInPic.

        多画面中每个画面的编号。编号从1开始。 默认值为1。

        :return: The index of this SubscriberInPic.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this SubscriberInPic.

        多画面中每个画面的编号。编号从1开始。 默认值为1。

        :param index: The index of this SubscriberInPic.
        :type index: int
        """
        self._index = index

    @property
    def subscriber(self):
        """Gets the subscriber of this SubscriberInPic.

        每个画面中与会者标识列表，从[[查询会议实时信息](https://support.huaweicloud.com/api-meeting/meeting_21_0029.html)](tag:hws)[[查询会议实时信息](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0029.html)](tag:hk)接口返回的pid中获取。

        :return: The subscriber of this SubscriberInPic.
        :rtype: list[str]
        """
        return self._subscriber

    @subscriber.setter
    def subscriber(self, subscriber):
        """Sets the subscriber of this SubscriberInPic.

        每个画面中与会者标识列表，从[[查询会议实时信息](https://support.huaweicloud.com/api-meeting/meeting_21_0029.html)](tag:hws)[[查询会议实时信息](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0029.html)](tag:hk)接口返回的pid中获取。

        :param subscriber: The subscriber of this SubscriberInPic.
        :type subscriber: list[str]
        """
        self._subscriber = subscriber

    @property
    def is_assist_stream(self):
        """Gets the is_assist_stream of this SubscriberInPic.

        是否为辅流。默认值为0。 - 0: 不是辅流 - 1: 是辅流

        :return: The is_assist_stream of this SubscriberInPic.
        :rtype: int
        """
        return self._is_assist_stream

    @is_assist_stream.setter
    def is_assist_stream(self, is_assist_stream):
        """Sets the is_assist_stream of this SubscriberInPic.

        是否为辅流。默认值为0。 - 0: 不是辅流 - 1: 是辅流

        :param is_assist_stream: The is_assist_stream of this SubscriberInPic.
        :type is_assist_stream: int
        """
        self._is_assist_stream = is_assist_stream

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
        if not isinstance(other, SubscriberInPic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
