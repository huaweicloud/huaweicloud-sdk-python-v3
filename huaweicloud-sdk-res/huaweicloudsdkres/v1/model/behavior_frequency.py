# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BehaviorFrequency:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'behavior_type': 'str',
        'lower_limit': 'int',
        'upper_limit': 'int',
        'time_interval': 'int'
    }

    attribute_map = {
        'behavior_type': 'behavior_type',
        'lower_limit': 'lower_limit',
        'upper_limit': 'upper_limit',
        'time_interval': 'time_interval'
    }

    def __init__(self, behavior_type=None, lower_limit=None, upper_limit=None, time_interval=None):
        """BehaviorFrequency

        The model defined in huaweicloud sdk

        :param behavior_type: 行为类型： - view，曝光 - click，点击 - collect，收藏 - uncollect，取消收藏 - search_click，搜索后点击 - comment，评论 - share，分享 - like，点赞 - dislike，点衰 - grade，评分 - consume，消费 - use，观看视频/听音乐/阅读 - download，下载 - tip，打赏 - subscribe，关注
        :type behavior_type: str
        :param lower_limit: 最小次数。
        :type lower_limit: int
        :param upper_limit: 最大次数。
        :type upper_limit: int
        :param time_interval: 时间区间。
        :type time_interval: int
        """
        
        

        self._behavior_type = None
        self._lower_limit = None
        self._upper_limit = None
        self._time_interval = None
        self.discriminator = None

        self.behavior_type = behavior_type
        if lower_limit is not None:
            self.lower_limit = lower_limit
        if upper_limit is not None:
            self.upper_limit = upper_limit
        self.time_interval = time_interval

    @property
    def behavior_type(self):
        """Gets the behavior_type of this BehaviorFrequency.

        行为类型： - view，曝光 - click，点击 - collect，收藏 - uncollect，取消收藏 - search_click，搜索后点击 - comment，评论 - share，分享 - like，点赞 - dislike，点衰 - grade，评分 - consume，消费 - use，观看视频/听音乐/阅读 - download，下载 - tip，打赏 - subscribe，关注

        :return: The behavior_type of this BehaviorFrequency.
        :rtype: str
        """
        return self._behavior_type

    @behavior_type.setter
    def behavior_type(self, behavior_type):
        """Sets the behavior_type of this BehaviorFrequency.

        行为类型： - view，曝光 - click，点击 - collect，收藏 - uncollect，取消收藏 - search_click，搜索后点击 - comment，评论 - share，分享 - like，点赞 - dislike，点衰 - grade，评分 - consume，消费 - use，观看视频/听音乐/阅读 - download，下载 - tip，打赏 - subscribe，关注

        :param behavior_type: The behavior_type of this BehaviorFrequency.
        :type behavior_type: str
        """
        self._behavior_type = behavior_type

    @property
    def lower_limit(self):
        """Gets the lower_limit of this BehaviorFrequency.

        最小次数。

        :return: The lower_limit of this BehaviorFrequency.
        :rtype: int
        """
        return self._lower_limit

    @lower_limit.setter
    def lower_limit(self, lower_limit):
        """Sets the lower_limit of this BehaviorFrequency.

        最小次数。

        :param lower_limit: The lower_limit of this BehaviorFrequency.
        :type lower_limit: int
        """
        self._lower_limit = lower_limit

    @property
    def upper_limit(self):
        """Gets the upper_limit of this BehaviorFrequency.

        最大次数。

        :return: The upper_limit of this BehaviorFrequency.
        :rtype: int
        """
        return self._upper_limit

    @upper_limit.setter
    def upper_limit(self, upper_limit):
        """Sets the upper_limit of this BehaviorFrequency.

        最大次数。

        :param upper_limit: The upper_limit of this BehaviorFrequency.
        :type upper_limit: int
        """
        self._upper_limit = upper_limit

    @property
    def time_interval(self):
        """Gets the time_interval of this BehaviorFrequency.

        时间区间。

        :return: The time_interval of this BehaviorFrequency.
        :rtype: int
        """
        return self._time_interval

    @time_interval.setter
    def time_interval(self, time_interval):
        """Sets the time_interval of this BehaviorFrequency.

        时间区间。

        :param time_interval: The time_interval of this BehaviorFrequency.
        :type time_interval: int
        """
        self._time_interval = time_interval

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
        if not isinstance(other, BehaviorFrequency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
