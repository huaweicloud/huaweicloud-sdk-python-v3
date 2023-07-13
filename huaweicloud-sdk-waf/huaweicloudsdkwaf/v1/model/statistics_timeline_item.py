# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticsTimelineItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'timeline': 'list[TimeLineItem]'
    }

    attribute_map = {
        'key': 'key',
        'timeline': 'timeline'
    }

    def __init__(self, key=None, timeline=None):
        """StatisticsTimelineItem

        The model defined in huaweicloud sdk

        :param key: 键值，包括请求总量（ACCESS）、Bot攻击防护（CRAWLER）、攻击总量（ATTACK）、Web基础防护（WEB_ATTACK）、精准防护（PRECISE）、CC攻击防护（CC）
        :type key: str
        :param timeline: 对应键值的时间线统计数据
        :type timeline: list[:class:`huaweicloudsdkwaf.v1.TimeLineItem`]
        """
        
        

        self._key = None
        self._timeline = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if timeline is not None:
            self.timeline = timeline

    @property
    def key(self):
        """Gets the key of this StatisticsTimelineItem.

        键值，包括请求总量（ACCESS）、Bot攻击防护（CRAWLER）、攻击总量（ATTACK）、Web基础防护（WEB_ATTACK）、精准防护（PRECISE）、CC攻击防护（CC）

        :return: The key of this StatisticsTimelineItem.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this StatisticsTimelineItem.

        键值，包括请求总量（ACCESS）、Bot攻击防护（CRAWLER）、攻击总量（ATTACK）、Web基础防护（WEB_ATTACK）、精准防护（PRECISE）、CC攻击防护（CC）

        :param key: The key of this StatisticsTimelineItem.
        :type key: str
        """
        self._key = key

    @property
    def timeline(self):
        """Gets the timeline of this StatisticsTimelineItem.

        对应键值的时间线统计数据

        :return: The timeline of this StatisticsTimelineItem.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.TimeLineItem`]
        """
        return self._timeline

    @timeline.setter
    def timeline(self, timeline):
        """Sets the timeline of this StatisticsTimelineItem.

        对应键值的时间线统计数据

        :param timeline: The timeline of this StatisticsTimelineItem.
        :type timeline: list[:class:`huaweicloudsdkwaf.v1.TimeLineItem`]
        """
        self._timeline = timeline

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
        if not isinstance(other, StatisticsTimelineItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
