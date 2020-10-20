# coding: utf-8

import pprint
import re

import six





class RestSubscriberInPic:


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
        """RestSubscriberInPic - a model defined in huaweicloud sdk"""
        
        

        self._index = None
        self._subscriber = None
        self._is_assist_stream = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if subscriber is not None:
            self.subscriber = subscriber
        if is_assist_stream is not None:
            self.is_assist_stream = is_assist_stream

    @property
    def index(self):
        """Gets the index of this RestSubscriberInPic.

        多画面中每个画面的编号，编号从1开始

        :return: The index of this RestSubscriberInPic.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this RestSubscriberInPic.

        多画面中每个画面的编号，编号从1开始

        :param index: The index of this RestSubscriberInPic.
        :type: int
        """
        self._index = index

    @property
    def subscriber(self):
        """Gets the subscriber of this RestSubscriberInPic.

        每个画面中会话标识，即Call_ID，通过会议状态通知获取

        :return: The subscriber of this RestSubscriberInPic.
        :rtype: list[str]
        """
        return self._subscriber

    @subscriber.setter
    def subscriber(self, subscriber):
        """Sets the subscriber of this RestSubscriberInPic.

        每个画面中会话标识，即Call_ID，通过会议状态通知获取

        :param subscriber: The subscriber of this RestSubscriberInPic.
        :type: list[str]
        """
        self._subscriber = subscriber

    @property
    def is_assist_stream(self):
        """Gets the is_assist_stream of this RestSubscriberInPic.

        是否为辅流 0： 不是辅流 1： 是辅流

        :return: The is_assist_stream of this RestSubscriberInPic.
        :rtype: int
        """
        return self._is_assist_stream

    @is_assist_stream.setter
    def is_assist_stream(self, is_assist_stream):
        """Sets the is_assist_stream of this RestSubscriberInPic.

        是否为辅流 0： 不是辅流 1： 是辅流

        :param is_assist_stream: The is_assist_stream of this RestSubscriberInPic.
        :type: int
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RestSubscriberInPic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
