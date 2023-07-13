# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RtmpBrokens:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audio_rec_bytes': 'list[float]',
        'audio_sent_bytes': 'list[float]',
        'rtmp_received_packets': 'list[float]',
        'rtmp_sent_packets': 'list[float]',
        'video_rec_bytes': 'list[float]',
        'video_sent_bytes': 'list[float]'
    }

    attribute_map = {
        'audio_rec_bytes': 'audioRecBytes',
        'audio_sent_bytes': 'audioSentBytes',
        'rtmp_received_packets': 'rtmpReceivedPackets',
        'rtmp_sent_packets': 'rtmpSentPackets',
        'video_rec_bytes': 'videoRecBytes',
        'video_sent_bytes': 'videoSentBytes'
    }

    def __init__(self, audio_rec_bytes=None, audio_sent_bytes=None, rtmp_received_packets=None, rtmp_sent_packets=None, video_rec_bytes=None, video_sent_bytes=None):
        """RtmpBrokens

        The model defined in huaweicloud sdk

        :param audio_rec_bytes: 音频接收字节数
        :type audio_rec_bytes: list[float]
        :param audio_sent_bytes: 音频发送字节数
        :type audio_sent_bytes: list[float]
        :param rtmp_received_packets: RTMP接收数据包数
        :type rtmp_received_packets: list[float]
        :param rtmp_sent_packets: RTMP发送数据包数
        :type rtmp_sent_packets: list[float]
        :param video_rec_bytes: 视频接收字节数
        :type video_rec_bytes: list[float]
        :param video_sent_bytes: 视频发送字节数
        :type video_sent_bytes: list[float]
        """
        
        

        self._audio_rec_bytes = None
        self._audio_sent_bytes = None
        self._rtmp_received_packets = None
        self._rtmp_sent_packets = None
        self._video_rec_bytes = None
        self._video_sent_bytes = None
        self.discriminator = None

        if audio_rec_bytes is not None:
            self.audio_rec_bytes = audio_rec_bytes
        if audio_sent_bytes is not None:
            self.audio_sent_bytes = audio_sent_bytes
        if rtmp_received_packets is not None:
            self.rtmp_received_packets = rtmp_received_packets
        if rtmp_sent_packets is not None:
            self.rtmp_sent_packets = rtmp_sent_packets
        if video_rec_bytes is not None:
            self.video_rec_bytes = video_rec_bytes
        if video_sent_bytes is not None:
            self.video_sent_bytes = video_sent_bytes

    @property
    def audio_rec_bytes(self):
        """Gets the audio_rec_bytes of this RtmpBrokens.

        音频接收字节数

        :return: The audio_rec_bytes of this RtmpBrokens.
        :rtype: list[float]
        """
        return self._audio_rec_bytes

    @audio_rec_bytes.setter
    def audio_rec_bytes(self, audio_rec_bytes):
        """Sets the audio_rec_bytes of this RtmpBrokens.

        音频接收字节数

        :param audio_rec_bytes: The audio_rec_bytes of this RtmpBrokens.
        :type audio_rec_bytes: list[float]
        """
        self._audio_rec_bytes = audio_rec_bytes

    @property
    def audio_sent_bytes(self):
        """Gets the audio_sent_bytes of this RtmpBrokens.

        音频发送字节数

        :return: The audio_sent_bytes of this RtmpBrokens.
        :rtype: list[float]
        """
        return self._audio_sent_bytes

    @audio_sent_bytes.setter
    def audio_sent_bytes(self, audio_sent_bytes):
        """Sets the audio_sent_bytes of this RtmpBrokens.

        音频发送字节数

        :param audio_sent_bytes: The audio_sent_bytes of this RtmpBrokens.
        :type audio_sent_bytes: list[float]
        """
        self._audio_sent_bytes = audio_sent_bytes

    @property
    def rtmp_received_packets(self):
        """Gets the rtmp_received_packets of this RtmpBrokens.

        RTMP接收数据包数

        :return: The rtmp_received_packets of this RtmpBrokens.
        :rtype: list[float]
        """
        return self._rtmp_received_packets

    @rtmp_received_packets.setter
    def rtmp_received_packets(self, rtmp_received_packets):
        """Sets the rtmp_received_packets of this RtmpBrokens.

        RTMP接收数据包数

        :param rtmp_received_packets: The rtmp_received_packets of this RtmpBrokens.
        :type rtmp_received_packets: list[float]
        """
        self._rtmp_received_packets = rtmp_received_packets

    @property
    def rtmp_sent_packets(self):
        """Gets the rtmp_sent_packets of this RtmpBrokens.

        RTMP发送数据包数

        :return: The rtmp_sent_packets of this RtmpBrokens.
        :rtype: list[float]
        """
        return self._rtmp_sent_packets

    @rtmp_sent_packets.setter
    def rtmp_sent_packets(self, rtmp_sent_packets):
        """Sets the rtmp_sent_packets of this RtmpBrokens.

        RTMP发送数据包数

        :param rtmp_sent_packets: The rtmp_sent_packets of this RtmpBrokens.
        :type rtmp_sent_packets: list[float]
        """
        self._rtmp_sent_packets = rtmp_sent_packets

    @property
    def video_rec_bytes(self):
        """Gets the video_rec_bytes of this RtmpBrokens.

        视频接收字节数

        :return: The video_rec_bytes of this RtmpBrokens.
        :rtype: list[float]
        """
        return self._video_rec_bytes

    @video_rec_bytes.setter
    def video_rec_bytes(self, video_rec_bytes):
        """Sets the video_rec_bytes of this RtmpBrokens.

        视频接收字节数

        :param video_rec_bytes: The video_rec_bytes of this RtmpBrokens.
        :type video_rec_bytes: list[float]
        """
        self._video_rec_bytes = video_rec_bytes

    @property
    def video_sent_bytes(self):
        """Gets the video_sent_bytes of this RtmpBrokens.

        视频发送字节数

        :return: The video_sent_bytes of this RtmpBrokens.
        :rtype: list[float]
        """
        return self._video_sent_bytes

    @video_sent_bytes.setter
    def video_sent_bytes(self, video_sent_bytes):
        """Sets the video_sent_bytes of this RtmpBrokens.

        视频发送字节数

        :param video_sent_bytes: The video_sent_bytes of this RtmpBrokens.
        :type video_sent_bytes: list[float]
        """
        self._video_sent_bytes = video_sent_bytes

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
        if not isinstance(other, RtmpBrokens):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
