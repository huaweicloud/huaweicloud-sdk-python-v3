# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Qos:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'network_quality': 'str',
        'codec_type': 'str',
        'band_width': 'int',
        'lost_packet_rate': 'int',
        'delay': 'int',
        'jitter': 'int',
        'resolution_height': 'int',
        'resolution_width': 'int',
        'frame_rate': 'int',
        'codec_user_id': 'str'
    }

    attribute_map = {
        'network_quality': 'networkQuality',
        'codec_type': 'codecType',
        'band_width': 'bandWidth',
        'lost_packet_rate': 'lostPacketRate',
        'delay': 'delay',
        'jitter': 'jitter',
        'resolution_height': 'resolutionHeight',
        'resolution_width': 'resolutionWidth',
        'frame_rate': 'frameRate',
        'codec_user_id': 'codecUserId'
    }

    def __init__(self, network_quality=None, codec_type=None, band_width=None, lost_packet_rate=None, delay=None, jitter=None, resolution_height=None, resolution_width=None, frame_rate=None, codec_user_id=None):
        r"""Qos

        The model defined in huaweicloud sdk

        :param network_quality: 网络质量评级
        :type network_quality: str
        :param codec_type: 编解码类型
        :type codec_type: str
        :param band_width: 带宽(kbit/s)
        :type band_width: int
        :param lost_packet_rate: 丢包率（千分数）
        :type lost_packet_rate: int
        :param delay: 时延(ms)
        :type delay: int
        :param jitter: 抖动(ms)
        :type jitter: int
        :param resolution_height: 分辨率:高
        :type resolution_height: int
        :param resolution_width: 分辨率：宽
        :type resolution_width: int
        :param frame_rate: 帧率
        :type frame_rate: int
        :param codec_user_id: 该媒体流编码会场ID，仅服务器向端侧发送方向涉及(视频)，如路径A--&gt;服务器--&gt;B，即B观看A，该媒体流的codec_user_id为A
        :type codec_user_id: str
        """
        
        

        self._network_quality = None
        self._codec_type = None
        self._band_width = None
        self._lost_packet_rate = None
        self._delay = None
        self._jitter = None
        self._resolution_height = None
        self._resolution_width = None
        self._frame_rate = None
        self._codec_user_id = None
        self.discriminator = None

        if network_quality is not None:
            self.network_quality = network_quality
        if codec_type is not None:
            self.codec_type = codec_type
        if band_width is not None:
            self.band_width = band_width
        if lost_packet_rate is not None:
            self.lost_packet_rate = lost_packet_rate
        if delay is not None:
            self.delay = delay
        if jitter is not None:
            self.jitter = jitter
        if resolution_height is not None:
            self.resolution_height = resolution_height
        if resolution_width is not None:
            self.resolution_width = resolution_width
        if frame_rate is not None:
            self.frame_rate = frame_rate
        if codec_user_id is not None:
            self.codec_user_id = codec_user_id

    @property
    def network_quality(self):
        r"""Gets the network_quality of this Qos.

        网络质量评级

        :return: The network_quality of this Qos.
        :rtype: str
        """
        return self._network_quality

    @network_quality.setter
    def network_quality(self, network_quality):
        r"""Sets the network_quality of this Qos.

        网络质量评级

        :param network_quality: The network_quality of this Qos.
        :type network_quality: str
        """
        self._network_quality = network_quality

    @property
    def codec_type(self):
        r"""Gets the codec_type of this Qos.

        编解码类型

        :return: The codec_type of this Qos.
        :rtype: str
        """
        return self._codec_type

    @codec_type.setter
    def codec_type(self, codec_type):
        r"""Sets the codec_type of this Qos.

        编解码类型

        :param codec_type: The codec_type of this Qos.
        :type codec_type: str
        """
        self._codec_type = codec_type

    @property
    def band_width(self):
        r"""Gets the band_width of this Qos.

        带宽(kbit/s)

        :return: The band_width of this Qos.
        :rtype: int
        """
        return self._band_width

    @band_width.setter
    def band_width(self, band_width):
        r"""Sets the band_width of this Qos.

        带宽(kbit/s)

        :param band_width: The band_width of this Qos.
        :type band_width: int
        """
        self._band_width = band_width

    @property
    def lost_packet_rate(self):
        r"""Gets the lost_packet_rate of this Qos.

        丢包率（千分数）

        :return: The lost_packet_rate of this Qos.
        :rtype: int
        """
        return self._lost_packet_rate

    @lost_packet_rate.setter
    def lost_packet_rate(self, lost_packet_rate):
        r"""Sets the lost_packet_rate of this Qos.

        丢包率（千分数）

        :param lost_packet_rate: The lost_packet_rate of this Qos.
        :type lost_packet_rate: int
        """
        self._lost_packet_rate = lost_packet_rate

    @property
    def delay(self):
        r"""Gets the delay of this Qos.

        时延(ms)

        :return: The delay of this Qos.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this Qos.

        时延(ms)

        :param delay: The delay of this Qos.
        :type delay: int
        """
        self._delay = delay

    @property
    def jitter(self):
        r"""Gets the jitter of this Qos.

        抖动(ms)

        :return: The jitter of this Qos.
        :rtype: int
        """
        return self._jitter

    @jitter.setter
    def jitter(self, jitter):
        r"""Sets the jitter of this Qos.

        抖动(ms)

        :param jitter: The jitter of this Qos.
        :type jitter: int
        """
        self._jitter = jitter

    @property
    def resolution_height(self):
        r"""Gets the resolution_height of this Qos.

        分辨率:高

        :return: The resolution_height of this Qos.
        :rtype: int
        """
        return self._resolution_height

    @resolution_height.setter
    def resolution_height(self, resolution_height):
        r"""Sets the resolution_height of this Qos.

        分辨率:高

        :param resolution_height: The resolution_height of this Qos.
        :type resolution_height: int
        """
        self._resolution_height = resolution_height

    @property
    def resolution_width(self):
        r"""Gets the resolution_width of this Qos.

        分辨率：宽

        :return: The resolution_width of this Qos.
        :rtype: int
        """
        return self._resolution_width

    @resolution_width.setter
    def resolution_width(self, resolution_width):
        r"""Sets the resolution_width of this Qos.

        分辨率：宽

        :param resolution_width: The resolution_width of this Qos.
        :type resolution_width: int
        """
        self._resolution_width = resolution_width

    @property
    def frame_rate(self):
        r"""Gets the frame_rate of this Qos.

        帧率

        :return: The frame_rate of this Qos.
        :rtype: int
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        r"""Sets the frame_rate of this Qos.

        帧率

        :param frame_rate: The frame_rate of this Qos.
        :type frame_rate: int
        """
        self._frame_rate = frame_rate

    @property
    def codec_user_id(self):
        r"""Gets the codec_user_id of this Qos.

        该媒体流编码会场ID，仅服务器向端侧发送方向涉及(视频)，如路径A-->服务器-->B，即B观看A，该媒体流的codec_user_id为A

        :return: The codec_user_id of this Qos.
        :rtype: str
        """
        return self._codec_user_id

    @codec_user_id.setter
    def codec_user_id(self, codec_user_id):
        r"""Sets the codec_user_id of this Qos.

        该媒体流编码会场ID，仅服务器向端侧发送方向涉及(视频)，如路径A-->服务器-->B，即B观看A，该媒体流的codec_user_id为A

        :param codec_user_id: The codec_user_id of this Qos.
        :type codec_user_id: str
        """
        self._codec_user_id = codec_user_id

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
        if not isinstance(other, Qos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
