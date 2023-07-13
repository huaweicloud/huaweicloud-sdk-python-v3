# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoSeek:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_video_seek': 'bool',
        'enable_flv_by_time_seek': 'bool',
        'start_parameter': 'str',
        'end_parameter': 'str'
    }

    attribute_map = {
        'enable_video_seek': 'enable_video_seek',
        'enable_flv_by_time_seek': 'enable_flv_by_time_seek',
        'start_parameter': 'start_parameter',
        'end_parameter': 'end_parameter'
    }

    def __init__(self, enable_video_seek=None, enable_flv_by_time_seek=None, start_parameter=None, end_parameter=None):
        """VideoSeek

        The model defined in huaweicloud sdk

        :param enable_video_seek: 视频拖拽开关， true：开启，false：关闭  &gt; 当本字段设置为“false”时，查询域名配置接口将不会返回视频拖拽配置信息。
        :type enable_video_seek: bool
        :param enable_flv_by_time_seek: flv时间拖拽开关， true：开启，false：关闭。
        :type enable_flv_by_time_seek: bool
        :param start_parameter: 自定义用户请求URL中视频播放的开始参数，支持使用数字0-9、字符a-z、A-Z，及\&quot;_\&quot;，长度≤64个字符。
        :type start_parameter: str
        :param end_parameter: 自定义用户请求URL中视频播放的结束参数，支持使用数字0-9、字符a-z、A-Z，及\&quot;_\&quot;，长度≤64个字符。
        :type end_parameter: str
        """
        
        

        self._enable_video_seek = None
        self._enable_flv_by_time_seek = None
        self._start_parameter = None
        self._end_parameter = None
        self.discriminator = None

        self.enable_video_seek = enable_video_seek
        if enable_flv_by_time_seek is not None:
            self.enable_flv_by_time_seek = enable_flv_by_time_seek
        if start_parameter is not None:
            self.start_parameter = start_parameter
        if end_parameter is not None:
            self.end_parameter = end_parameter

    @property
    def enable_video_seek(self):
        """Gets the enable_video_seek of this VideoSeek.

        视频拖拽开关， true：开启，false：关闭  > 当本字段设置为“false”时，查询域名配置接口将不会返回视频拖拽配置信息。

        :return: The enable_video_seek of this VideoSeek.
        :rtype: bool
        """
        return self._enable_video_seek

    @enable_video_seek.setter
    def enable_video_seek(self, enable_video_seek):
        """Sets the enable_video_seek of this VideoSeek.

        视频拖拽开关， true：开启，false：关闭  > 当本字段设置为“false”时，查询域名配置接口将不会返回视频拖拽配置信息。

        :param enable_video_seek: The enable_video_seek of this VideoSeek.
        :type enable_video_seek: bool
        """
        self._enable_video_seek = enable_video_seek

    @property
    def enable_flv_by_time_seek(self):
        """Gets the enable_flv_by_time_seek of this VideoSeek.

        flv时间拖拽开关， true：开启，false：关闭。

        :return: The enable_flv_by_time_seek of this VideoSeek.
        :rtype: bool
        """
        return self._enable_flv_by_time_seek

    @enable_flv_by_time_seek.setter
    def enable_flv_by_time_seek(self, enable_flv_by_time_seek):
        """Sets the enable_flv_by_time_seek of this VideoSeek.

        flv时间拖拽开关， true：开启，false：关闭。

        :param enable_flv_by_time_seek: The enable_flv_by_time_seek of this VideoSeek.
        :type enable_flv_by_time_seek: bool
        """
        self._enable_flv_by_time_seek = enable_flv_by_time_seek

    @property
    def start_parameter(self):
        """Gets the start_parameter of this VideoSeek.

        自定义用户请求URL中视频播放的开始参数，支持使用数字0-9、字符a-z、A-Z，及\"_\"，长度≤64个字符。

        :return: The start_parameter of this VideoSeek.
        :rtype: str
        """
        return self._start_parameter

    @start_parameter.setter
    def start_parameter(self, start_parameter):
        """Sets the start_parameter of this VideoSeek.

        自定义用户请求URL中视频播放的开始参数，支持使用数字0-9、字符a-z、A-Z，及\"_\"，长度≤64个字符。

        :param start_parameter: The start_parameter of this VideoSeek.
        :type start_parameter: str
        """
        self._start_parameter = start_parameter

    @property
    def end_parameter(self):
        """Gets the end_parameter of this VideoSeek.

        自定义用户请求URL中视频播放的结束参数，支持使用数字0-9、字符a-z、A-Z，及\"_\"，长度≤64个字符。

        :return: The end_parameter of this VideoSeek.
        :rtype: str
        """
        return self._end_parameter

    @end_parameter.setter
    def end_parameter(self, end_parameter):
        """Sets the end_parameter of this VideoSeek.

        自定义用户请求URL中视频播放的结束参数，支持使用数字0-9、字符a-z、A-Z，及\"_\"，长度≤64个字符。

        :param end_parameter: The end_parameter of this VideoSeek.
        :type end_parameter: str
        """
        self._end_parameter = end_parameter

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
        if not isinstance(other, VideoSeek):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
