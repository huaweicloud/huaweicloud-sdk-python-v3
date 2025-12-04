# coding: utf-8

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
        r"""StatisticsTimelineItem

        The model defined in huaweicloud sdk

        :param key: **参数解释：** 键值标识，用于区分不同的防护统计类型 **约束限制：** 不涉及 **取值范围：**  - ACCESS:请求总量  - CRAWLER:Bot攻击防护  - ATTACK:攻击总量  - WEB_ATTACK:Web基础防护  - PRECISE:精准防护  - CC:CC攻击防护 **默认取值：** 不涉及
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
        r"""Gets the key of this StatisticsTimelineItem.

        **参数解释：** 键值标识，用于区分不同的防护统计类型 **约束限制：** 不涉及 **取值范围：**  - ACCESS:请求总量  - CRAWLER:Bot攻击防护  - ATTACK:攻击总量  - WEB_ATTACK:Web基础防护  - PRECISE:精准防护  - CC:CC攻击防护 **默认取值：** 不涉及

        :return: The key of this StatisticsTimelineItem.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this StatisticsTimelineItem.

        **参数解释：** 键值标识，用于区分不同的防护统计类型 **约束限制：** 不涉及 **取值范围：**  - ACCESS:请求总量  - CRAWLER:Bot攻击防护  - ATTACK:攻击总量  - WEB_ATTACK:Web基础防护  - PRECISE:精准防护  - CC:CC攻击防护 **默认取值：** 不涉及

        :param key: The key of this StatisticsTimelineItem.
        :type key: str
        """
        self._key = key

    @property
    def timeline(self):
        r"""Gets the timeline of this StatisticsTimelineItem.

        对应键值的时间线统计数据

        :return: The timeline of this StatisticsTimelineItem.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.TimeLineItem`]
        """
        return self._timeline

    @timeline.setter
    def timeline(self, timeline):
        r"""Sets the timeline of this StatisticsTimelineItem.

        对应键值的时间线统计数据

        :param timeline: The timeline of this StatisticsTimelineItem.
        :type timeline: list[:class:`huaweicloudsdkwaf.v1.TimeLineItem`]
        """
        self._timeline = timeline

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
