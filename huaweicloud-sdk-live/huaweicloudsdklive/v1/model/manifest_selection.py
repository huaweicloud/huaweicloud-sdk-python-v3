# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ManifestSelection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stream_order': 'str',
        'min_video_bandwidth': 'int',
        'max_video_bandwidth': 'int'
    }

    attribute_map = {
        'stream_order': 'stream_order',
        'min_video_bandwidth': 'min_video_bandwidth',
        'max_video_bandwidth': 'max_video_bandwidth'
    }

    def __init__(self, stream_order=None, min_video_bandwidth=None, max_video_bandwidth=None):
        r"""ManifestSelection

        The model defined in huaweicloud sdk

        :param stream_order: **参数解释**： 流排序模式 **约束限制**： 不涉及 **取值范围**： - ORIGINAL：保持原始顺序，即按照频道配置中转码模板的顺序 - VIDEO_BITRATE_ASCENDING：按照视频码率升序 - VIDEO_BITRATE_DESCENDING：按照视频码率降序 
        :type stream_order: str
        :param min_video_bandwidth: **参数解释**： 视频码率过滤的最小码率 **约束限制**： 单位：bit/s；取值必须比max_video_bandwidth小 
        :type min_video_bandwidth: int
        :param max_video_bandwidth: **参数解释**： 视频码率过滤的最大码率 **约束限制**： 单位：bit/s；取值必须比min_video_bandwidth大 
        :type max_video_bandwidth: int
        """
        
        

        self._stream_order = None
        self._min_video_bandwidth = None
        self._max_video_bandwidth = None
        self.discriminator = None

        if stream_order is not None:
            self.stream_order = stream_order
        if min_video_bandwidth is not None:
            self.min_video_bandwidth = min_video_bandwidth
        if max_video_bandwidth is not None:
            self.max_video_bandwidth = max_video_bandwidth

    @property
    def stream_order(self):
        r"""Gets the stream_order of this ManifestSelection.

        **参数解释**： 流排序模式 **约束限制**： 不涉及 **取值范围**： - ORIGINAL：保持原始顺序，即按照频道配置中转码模板的顺序 - VIDEO_BITRATE_ASCENDING：按照视频码率升序 - VIDEO_BITRATE_DESCENDING：按照视频码率降序 

        :return: The stream_order of this ManifestSelection.
        :rtype: str
        """
        return self._stream_order

    @stream_order.setter
    def stream_order(self, stream_order):
        r"""Sets the stream_order of this ManifestSelection.

        **参数解释**： 流排序模式 **约束限制**： 不涉及 **取值范围**： - ORIGINAL：保持原始顺序，即按照频道配置中转码模板的顺序 - VIDEO_BITRATE_ASCENDING：按照视频码率升序 - VIDEO_BITRATE_DESCENDING：按照视频码率降序 

        :param stream_order: The stream_order of this ManifestSelection.
        :type stream_order: str
        """
        self._stream_order = stream_order

    @property
    def min_video_bandwidth(self):
        r"""Gets the min_video_bandwidth of this ManifestSelection.

        **参数解释**： 视频码率过滤的最小码率 **约束限制**： 单位：bit/s；取值必须比max_video_bandwidth小 

        :return: The min_video_bandwidth of this ManifestSelection.
        :rtype: int
        """
        return self._min_video_bandwidth

    @min_video_bandwidth.setter
    def min_video_bandwidth(self, min_video_bandwidth):
        r"""Sets the min_video_bandwidth of this ManifestSelection.

        **参数解释**： 视频码率过滤的最小码率 **约束限制**： 单位：bit/s；取值必须比max_video_bandwidth小 

        :param min_video_bandwidth: The min_video_bandwidth of this ManifestSelection.
        :type min_video_bandwidth: int
        """
        self._min_video_bandwidth = min_video_bandwidth

    @property
    def max_video_bandwidth(self):
        r"""Gets the max_video_bandwidth of this ManifestSelection.

        **参数解释**： 视频码率过滤的最大码率 **约束限制**： 单位：bit/s；取值必须比min_video_bandwidth大 

        :return: The max_video_bandwidth of this ManifestSelection.
        :rtype: int
        """
        return self._max_video_bandwidth

    @max_video_bandwidth.setter
    def max_video_bandwidth(self, max_video_bandwidth):
        r"""Sets the max_video_bandwidth of this ManifestSelection.

        **参数解释**： 视频码率过滤的最大码率 **约束限制**： 单位：bit/s；取值必须比min_video_bandwidth大 

        :param max_video_bandwidth: The max_video_bandwidth of this ManifestSelection.
        :type max_video_bandwidth: int
        """
        self._max_video_bandwidth = max_video_bandwidth

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
        if not isinstance(other, ManifestSelection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
