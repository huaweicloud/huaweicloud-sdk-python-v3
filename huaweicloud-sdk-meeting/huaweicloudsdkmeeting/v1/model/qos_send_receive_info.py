# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QosSendReceiveInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bitrate': 'list[QosDataNoThrElement]',
        'latency': 'list[QosDataElement]',
        'jitter': 'list[QosDataElement]',
        'packet_loss_max': 'list[QosDataElement]',
        'resolution': 'list[QosDataNoThrElement]',
        'frame': 'list[QosDataNoThrElement]'
    }

    attribute_map = {
        'bitrate': 'bitrate',
        'latency': 'latency',
        'jitter': 'jitter',
        'packet_loss_max': 'packet_loss_max',
        'resolution': 'resolution',
        'frame': 'frame'
    }

    def __init__(self, bitrate=None, latency=None, jitter=None, packet_loss_max=None, resolution=None, frame=None):
        """QosSendReceiveInfo

        The model defined in huaweicloud sdk

        :param bitrate: 码率, 单位kbps，不含阈值告警。当qosType &#x3D; audio/video/screen 时有效。
        :type bitrate: list[:class:`huaweicloudsdkmeeting.v1.QosDataNoThrElement`]
        :param latency: 时延，单位毫秒, 含阈值告警。当qosType &#x3D; audio/video/screen 时有效。
        :type latency: list[:class:`huaweicloudsdkmeeting.v1.QosDataElement`]
        :param jitter: 抖动, 单位毫秒，含阈值告警。当qosType &#x3D; audio/video/screen 时有效。
        :type jitter: list[:class:`huaweicloudsdkmeeting.v1.QosDataElement`]
        :param packet_loss_max: 最大丢包率, 单位百分比 含阈值告警。当qosType &#x3D; audio/video/screen 时有效。
        :type packet_loss_max: list[:class:`huaweicloudsdkmeeting.v1.QosDataElement`]
        :param resolution: 分辨率, 不含阈值告警。当qosType &#x3D; video/screen 时有效。
        :type resolution: list[:class:`huaweicloudsdkmeeting.v1.QosDataNoThrElement`]
        :param frame: 帧率, 单位fps，不含阈值告警。当qosType &#x3D; video/screen 时有效。
        :type frame: list[:class:`huaweicloudsdkmeeting.v1.QosDataNoThrElement`]
        """
        
        

        self._bitrate = None
        self._latency = None
        self._jitter = None
        self._packet_loss_max = None
        self._resolution = None
        self._frame = None
        self.discriminator = None

        if bitrate is not None:
            self.bitrate = bitrate
        if latency is not None:
            self.latency = latency
        if jitter is not None:
            self.jitter = jitter
        if packet_loss_max is not None:
            self.packet_loss_max = packet_loss_max
        if resolution is not None:
            self.resolution = resolution
        if frame is not None:
            self.frame = frame

    @property
    def bitrate(self):
        """Gets the bitrate of this QosSendReceiveInfo.

        码率, 单位kbps，不含阈值告警。当qosType = audio/video/screen 时有效。

        :return: The bitrate of this QosSendReceiveInfo.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.QosDataNoThrElement`]
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this QosSendReceiveInfo.

        码率, 单位kbps，不含阈值告警。当qosType = audio/video/screen 时有效。

        :param bitrate: The bitrate of this QosSendReceiveInfo.
        :type bitrate: list[:class:`huaweicloudsdkmeeting.v1.QosDataNoThrElement`]
        """
        self._bitrate = bitrate

    @property
    def latency(self):
        """Gets the latency of this QosSendReceiveInfo.

        时延，单位毫秒, 含阈值告警。当qosType = audio/video/screen 时有效。

        :return: The latency of this QosSendReceiveInfo.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.QosDataElement`]
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this QosSendReceiveInfo.

        时延，单位毫秒, 含阈值告警。当qosType = audio/video/screen 时有效。

        :param latency: The latency of this QosSendReceiveInfo.
        :type latency: list[:class:`huaweicloudsdkmeeting.v1.QosDataElement`]
        """
        self._latency = latency

    @property
    def jitter(self):
        """Gets the jitter of this QosSendReceiveInfo.

        抖动, 单位毫秒，含阈值告警。当qosType = audio/video/screen 时有效。

        :return: The jitter of this QosSendReceiveInfo.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.QosDataElement`]
        """
        return self._jitter

    @jitter.setter
    def jitter(self, jitter):
        """Sets the jitter of this QosSendReceiveInfo.

        抖动, 单位毫秒，含阈值告警。当qosType = audio/video/screen 时有效。

        :param jitter: The jitter of this QosSendReceiveInfo.
        :type jitter: list[:class:`huaweicloudsdkmeeting.v1.QosDataElement`]
        """
        self._jitter = jitter

    @property
    def packet_loss_max(self):
        """Gets the packet_loss_max of this QosSendReceiveInfo.

        最大丢包率, 单位百分比 含阈值告警。当qosType = audio/video/screen 时有效。

        :return: The packet_loss_max of this QosSendReceiveInfo.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.QosDataElement`]
        """
        return self._packet_loss_max

    @packet_loss_max.setter
    def packet_loss_max(self, packet_loss_max):
        """Sets the packet_loss_max of this QosSendReceiveInfo.

        最大丢包率, 单位百分比 含阈值告警。当qosType = audio/video/screen 时有效。

        :param packet_loss_max: The packet_loss_max of this QosSendReceiveInfo.
        :type packet_loss_max: list[:class:`huaweicloudsdkmeeting.v1.QosDataElement`]
        """
        self._packet_loss_max = packet_loss_max

    @property
    def resolution(self):
        """Gets the resolution of this QosSendReceiveInfo.

        分辨率, 不含阈值告警。当qosType = video/screen 时有效。

        :return: The resolution of this QosSendReceiveInfo.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.QosDataNoThrElement`]
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this QosSendReceiveInfo.

        分辨率, 不含阈值告警。当qosType = video/screen 时有效。

        :param resolution: The resolution of this QosSendReceiveInfo.
        :type resolution: list[:class:`huaweicloudsdkmeeting.v1.QosDataNoThrElement`]
        """
        self._resolution = resolution

    @property
    def frame(self):
        """Gets the frame of this QosSendReceiveInfo.

        帧率, 单位fps，不含阈值告警。当qosType = video/screen 时有效。

        :return: The frame of this QosSendReceiveInfo.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.QosDataNoThrElement`]
        """
        return self._frame

    @frame.setter
    def frame(self, frame):
        """Sets the frame of this QosSendReceiveInfo.

        帧率, 单位fps，不含阈值告警。当qosType = video/screen 时有效。

        :param frame: The frame of this QosSendReceiveInfo.
        :type frame: list[:class:`huaweicloudsdkmeeting.v1.QosDataNoThrElement`]
        """
        self._frame = frame

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
        if not isinstance(other, QosSendReceiveInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
