# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserQos:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'participant_id': 'str',
        'net_rate': 'str',
        'band_width_up': 'int',
        'band_width_down': 'int',
        'lost_packet_rate_up': 'int',
        'lost_packet_rate_down': 'int',
        'delay': 'int',
        'video_qos': 'MediaQos',
        'audio_qos': 'MediaQos',
        'aux_qos': 'MediaQos'
    }

    attribute_map = {
        'participant_id': 'participantID',
        'net_rate': 'netRate',
        'band_width_up': 'bandWidthUp',
        'band_width_down': 'bandWidthDown',
        'lost_packet_rate_up': 'lostPacketRateUp',
        'lost_packet_rate_down': 'lostPacketRateDown',
        'delay': 'delay',
        'video_qos': 'videoQos',
        'audio_qos': 'audioQos',
        'aux_qos': 'auxQos'
    }

    def __init__(self, participant_id=None, net_rate=None, band_width_up=None, band_width_down=None, lost_packet_rate_up=None, lost_packet_rate_down=None, delay=None, video_qos=None, audio_qos=None, aux_qos=None):
        r"""UserQos

        The model defined in huaweicloud sdk

        :param participant_id: 会场ID
        :type participant_id: str
        :param net_rate: 网络质量评级
        :type net_rate: str
        :param band_width_up: 上行总带宽(kbit/s)
        :type band_width_up: int
        :param band_width_down: 下行总带宽(kbit/s)
        :type band_width_down: int
        :param lost_packet_rate_up: 上行丢包率（千分数）
        :type lost_packet_rate_up: int
        :param lost_packet_rate_down: 下行丢包率（千分数）
        :type lost_packet_rate_down: int
        :param delay: 时延(ms)
        :type delay: int
        :param video_qos: 
        :type video_qos: :class:`huaweicloudsdkmeeting.v1.MediaQos`
        :param audio_qos: 
        :type audio_qos: :class:`huaweicloudsdkmeeting.v1.MediaQos`
        :param aux_qos: 
        :type aux_qos: :class:`huaweicloudsdkmeeting.v1.MediaQos`
        """
        
        

        self._participant_id = None
        self._net_rate = None
        self._band_width_up = None
        self._band_width_down = None
        self._lost_packet_rate_up = None
        self._lost_packet_rate_down = None
        self._delay = None
        self._video_qos = None
        self._audio_qos = None
        self._aux_qos = None
        self.discriminator = None

        if participant_id is not None:
            self.participant_id = participant_id
        if net_rate is not None:
            self.net_rate = net_rate
        if band_width_up is not None:
            self.band_width_up = band_width_up
        if band_width_down is not None:
            self.band_width_down = band_width_down
        if lost_packet_rate_up is not None:
            self.lost_packet_rate_up = lost_packet_rate_up
        if lost_packet_rate_down is not None:
            self.lost_packet_rate_down = lost_packet_rate_down
        if delay is not None:
            self.delay = delay
        if video_qos is not None:
            self.video_qos = video_qos
        if audio_qos is not None:
            self.audio_qos = audio_qos
        if aux_qos is not None:
            self.aux_qos = aux_qos

    @property
    def participant_id(self):
        r"""Gets the participant_id of this UserQos.

        会场ID

        :return: The participant_id of this UserQos.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        r"""Sets the participant_id of this UserQos.

        会场ID

        :param participant_id: The participant_id of this UserQos.
        :type participant_id: str
        """
        self._participant_id = participant_id

    @property
    def net_rate(self):
        r"""Gets the net_rate of this UserQos.

        网络质量评级

        :return: The net_rate of this UserQos.
        :rtype: str
        """
        return self._net_rate

    @net_rate.setter
    def net_rate(self, net_rate):
        r"""Sets the net_rate of this UserQos.

        网络质量评级

        :param net_rate: The net_rate of this UserQos.
        :type net_rate: str
        """
        self._net_rate = net_rate

    @property
    def band_width_up(self):
        r"""Gets the band_width_up of this UserQos.

        上行总带宽(kbit/s)

        :return: The band_width_up of this UserQos.
        :rtype: int
        """
        return self._band_width_up

    @band_width_up.setter
    def band_width_up(self, band_width_up):
        r"""Sets the band_width_up of this UserQos.

        上行总带宽(kbit/s)

        :param band_width_up: The band_width_up of this UserQos.
        :type band_width_up: int
        """
        self._band_width_up = band_width_up

    @property
    def band_width_down(self):
        r"""Gets the band_width_down of this UserQos.

        下行总带宽(kbit/s)

        :return: The band_width_down of this UserQos.
        :rtype: int
        """
        return self._band_width_down

    @band_width_down.setter
    def band_width_down(self, band_width_down):
        r"""Sets the band_width_down of this UserQos.

        下行总带宽(kbit/s)

        :param band_width_down: The band_width_down of this UserQos.
        :type band_width_down: int
        """
        self._band_width_down = band_width_down

    @property
    def lost_packet_rate_up(self):
        r"""Gets the lost_packet_rate_up of this UserQos.

        上行丢包率（千分数）

        :return: The lost_packet_rate_up of this UserQos.
        :rtype: int
        """
        return self._lost_packet_rate_up

    @lost_packet_rate_up.setter
    def lost_packet_rate_up(self, lost_packet_rate_up):
        r"""Sets the lost_packet_rate_up of this UserQos.

        上行丢包率（千分数）

        :param lost_packet_rate_up: The lost_packet_rate_up of this UserQos.
        :type lost_packet_rate_up: int
        """
        self._lost_packet_rate_up = lost_packet_rate_up

    @property
    def lost_packet_rate_down(self):
        r"""Gets the lost_packet_rate_down of this UserQos.

        下行丢包率（千分数）

        :return: The lost_packet_rate_down of this UserQos.
        :rtype: int
        """
        return self._lost_packet_rate_down

    @lost_packet_rate_down.setter
    def lost_packet_rate_down(self, lost_packet_rate_down):
        r"""Sets the lost_packet_rate_down of this UserQos.

        下行丢包率（千分数）

        :param lost_packet_rate_down: The lost_packet_rate_down of this UserQos.
        :type lost_packet_rate_down: int
        """
        self._lost_packet_rate_down = lost_packet_rate_down

    @property
    def delay(self):
        r"""Gets the delay of this UserQos.

        时延(ms)

        :return: The delay of this UserQos.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this UserQos.

        时延(ms)

        :param delay: The delay of this UserQos.
        :type delay: int
        """
        self._delay = delay

    @property
    def video_qos(self):
        r"""Gets the video_qos of this UserQos.

        :return: The video_qos of this UserQos.
        :rtype: :class:`huaweicloudsdkmeeting.v1.MediaQos`
        """
        return self._video_qos

    @video_qos.setter
    def video_qos(self, video_qos):
        r"""Sets the video_qos of this UserQos.

        :param video_qos: The video_qos of this UserQos.
        :type video_qos: :class:`huaweicloudsdkmeeting.v1.MediaQos`
        """
        self._video_qos = video_qos

    @property
    def audio_qos(self):
        r"""Gets the audio_qos of this UserQos.

        :return: The audio_qos of this UserQos.
        :rtype: :class:`huaweicloudsdkmeeting.v1.MediaQos`
        """
        return self._audio_qos

    @audio_qos.setter
    def audio_qos(self, audio_qos):
        r"""Sets the audio_qos of this UserQos.

        :param audio_qos: The audio_qos of this UserQos.
        :type audio_qos: :class:`huaweicloudsdkmeeting.v1.MediaQos`
        """
        self._audio_qos = audio_qos

    @property
    def aux_qos(self):
        r"""Gets the aux_qos of this UserQos.

        :return: The aux_qos of this UserQos.
        :rtype: :class:`huaweicloudsdkmeeting.v1.MediaQos`
        """
        return self._aux_qos

    @aux_qos.setter
    def aux_qos(self, aux_qos):
        r"""Sets the aux_qos of this UserQos.

        :param aux_qos: The aux_qos of this UserQos.
        :type aux_qos: :class:`huaweicloudsdkmeeting.v1.MediaQos`
        """
        self._aux_qos = aux_qos

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
        if not isinstance(other, UserQos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
