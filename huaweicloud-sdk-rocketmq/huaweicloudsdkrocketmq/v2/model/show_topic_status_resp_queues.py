# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTopicStatusRespQueues:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'min_offset': 'int',
        'max_offset': 'int',
        'last_message_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'min_offset': 'min_offset',
        'max_offset': 'max_offset',
        'last_message_time': 'last_message_time'
    }

    def __init__(self, id=None, min_offset=None, max_offset=None, last_message_time=None):
        """ShowTopicStatusRespQueues

        The model defined in huaweicloud sdk

        :param id: 队列ID。
        :type id: int
        :param min_offset: 最小偏移量。
        :type min_offset: int
        :param max_offset: 最大偏移量。
        :type max_offset: int
        :param last_message_time: 最后一条消息的时间。
        :type last_message_time: int
        """
        
        

        self._id = None
        self._min_offset = None
        self._max_offset = None
        self._last_message_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if min_offset is not None:
            self.min_offset = min_offset
        if max_offset is not None:
            self.max_offset = max_offset
        if last_message_time is not None:
            self.last_message_time = last_message_time

    @property
    def id(self):
        """Gets the id of this ShowTopicStatusRespQueues.

        队列ID。

        :return: The id of this ShowTopicStatusRespQueues.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowTopicStatusRespQueues.

        队列ID。

        :param id: The id of this ShowTopicStatusRespQueues.
        :type id: int
        """
        self._id = id

    @property
    def min_offset(self):
        """Gets the min_offset of this ShowTopicStatusRespQueues.

        最小偏移量。

        :return: The min_offset of this ShowTopicStatusRespQueues.
        :rtype: int
        """
        return self._min_offset

    @min_offset.setter
    def min_offset(self, min_offset):
        """Sets the min_offset of this ShowTopicStatusRespQueues.

        最小偏移量。

        :param min_offset: The min_offset of this ShowTopicStatusRespQueues.
        :type min_offset: int
        """
        self._min_offset = min_offset

    @property
    def max_offset(self):
        """Gets the max_offset of this ShowTopicStatusRespQueues.

        最大偏移量。

        :return: The max_offset of this ShowTopicStatusRespQueues.
        :rtype: int
        """
        return self._max_offset

    @max_offset.setter
    def max_offset(self, max_offset):
        """Sets the max_offset of this ShowTopicStatusRespQueues.

        最大偏移量。

        :param max_offset: The max_offset of this ShowTopicStatusRespQueues.
        :type max_offset: int
        """
        self._max_offset = max_offset

    @property
    def last_message_time(self):
        """Gets the last_message_time of this ShowTopicStatusRespQueues.

        最后一条消息的时间。

        :return: The last_message_time of this ShowTopicStatusRespQueues.
        :rtype: int
        """
        return self._last_message_time

    @last_message_time.setter
    def last_message_time(self, last_message_time):
        """Sets the last_message_time of this ShowTopicStatusRespQueues.

        最后一条消息的时间。

        :param last_message_time: The last_message_time of this ShowTopicStatusRespQueues.
        :type last_message_time: int
        """
        self._last_message_time = last_message_time

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
        if not isinstance(other, ShowTopicStatusRespQueues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
