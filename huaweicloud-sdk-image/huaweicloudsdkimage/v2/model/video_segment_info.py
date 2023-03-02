# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoSegmentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'float',
        'duration': 'float',
        'to_gif': 'int',
        'speed': 'float',
        'gif_compress': 'float'
    }

    attribute_map = {
        'start_time': 'start_time',
        'duration': 'duration',
        'to_gif': 'to_gif',
        'speed': 'speed',
        'gif_compress': 'gif_compress'
    }

    def __init__(self, start_time=None, duration=None, to_gif=None, speed=None, gif_compress=None):
        """VideoSegmentInfo

        The model defined in huaweicloud sdk

        :param start_time: 视频分段起始时间
        :type start_time: float
        :param duration: 视频分段持续时间
        :type duration: float
        :param to_gif: 视频剪切服务生成视频或gif开关，1生成gif，0生成视频，默认为视频
        :type to_gif: int
        :param speed: 视频或gif倍速，默认1
        :type speed: float
        :param gif_compress: gif分辨率压缩率，gif最终分辨率为最终合成视频分辨率*gif_compress
        :type gif_compress: float
        """
        
        

        self._start_time = None
        self._duration = None
        self._to_gif = None
        self._speed = None
        self._gif_compress = None
        self.discriminator = None

        self.start_time = start_time
        self.duration = duration
        if to_gif is not None:
            self.to_gif = to_gif
        if speed is not None:
            self.speed = speed
        if gif_compress is not None:
            self.gif_compress = gif_compress

    @property
    def start_time(self):
        """Gets the start_time of this VideoSegmentInfo.

        视频分段起始时间

        :return: The start_time of this VideoSegmentInfo.
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this VideoSegmentInfo.

        视频分段起始时间

        :param start_time: The start_time of this VideoSegmentInfo.
        :type start_time: float
        """
        self._start_time = start_time

    @property
    def duration(self):
        """Gets the duration of this VideoSegmentInfo.

        视频分段持续时间

        :return: The duration of this VideoSegmentInfo.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this VideoSegmentInfo.

        视频分段持续时间

        :param duration: The duration of this VideoSegmentInfo.
        :type duration: float
        """
        self._duration = duration

    @property
    def to_gif(self):
        """Gets the to_gif of this VideoSegmentInfo.

        视频剪切服务生成视频或gif开关，1生成gif，0生成视频，默认为视频

        :return: The to_gif of this VideoSegmentInfo.
        :rtype: int
        """
        return self._to_gif

    @to_gif.setter
    def to_gif(self, to_gif):
        """Sets the to_gif of this VideoSegmentInfo.

        视频剪切服务生成视频或gif开关，1生成gif，0生成视频，默认为视频

        :param to_gif: The to_gif of this VideoSegmentInfo.
        :type to_gif: int
        """
        self._to_gif = to_gif

    @property
    def speed(self):
        """Gets the speed of this VideoSegmentInfo.

        视频或gif倍速，默认1

        :return: The speed of this VideoSegmentInfo.
        :rtype: float
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this VideoSegmentInfo.

        视频或gif倍速，默认1

        :param speed: The speed of this VideoSegmentInfo.
        :type speed: float
        """
        self._speed = speed

    @property
    def gif_compress(self):
        """Gets the gif_compress of this VideoSegmentInfo.

        gif分辨率压缩率，gif最终分辨率为最终合成视频分辨率*gif_compress

        :return: The gif_compress of this VideoSegmentInfo.
        :rtype: float
        """
        return self._gif_compress

    @gif_compress.setter
    def gif_compress(self, gif_compress):
        """Sets the gif_compress of this VideoSegmentInfo.

        gif分辨率压缩率，gif最终分辨率为最终合成视频分辨率*gif_compress

        :param gif_compress: The gif_compress of this VideoSegmentInfo.
        :type gif_compress: float
        """
        self._gif_compress = gif_compress

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
        if not isinstance(other, VideoSegmentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
