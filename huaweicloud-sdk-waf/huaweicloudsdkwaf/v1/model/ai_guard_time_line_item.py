# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiGuardTimeLineItem:

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
        'timeline': 'list[TimeLinePoint]'
    }

    attribute_map = {
        'key': 'key',
        'timeline': 'timeline'
    }

    def __init__(self, key=None, timeline=None):
        r"""AiGuardTimeLineItem

        The model defined in huaweicloud sdk

        :param key: 统计指标类型： - api_detection_requests：检测请求数量 - total_matched：命中规则的请求数量 
        :type key: str
        :param timeline: 时间线统计数据列表
        :type timeline: list[:class:`huaweicloudsdkwaf.v1.TimeLinePoint`]
        """
        
        

        self._key = None
        self._timeline = None
        self.discriminator = None

        self.key = key
        self.timeline = timeline

    @property
    def key(self):
        r"""Gets the key of this AiGuardTimeLineItem.

        统计指标类型： - api_detection_requests：检测请求数量 - total_matched：命中规则的请求数量 

        :return: The key of this AiGuardTimeLineItem.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this AiGuardTimeLineItem.

        统计指标类型： - api_detection_requests：检测请求数量 - total_matched：命中规则的请求数量 

        :param key: The key of this AiGuardTimeLineItem.
        :type key: str
        """
        self._key = key

    @property
    def timeline(self):
        r"""Gets the timeline of this AiGuardTimeLineItem.

        时间线统计数据列表

        :return: The timeline of this AiGuardTimeLineItem.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.TimeLinePoint`]
        """
        return self._timeline

    @timeline.setter
    def timeline(self, timeline):
        r"""Sets the timeline of this AiGuardTimeLineItem.

        时间线统计数据列表

        :param timeline: The timeline of this AiGuardTimeLineItem.
        :type timeline: list[:class:`huaweicloudsdkwaf.v1.TimeLinePoint`]
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
        if not isinstance(other, AiGuardTimeLineItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
