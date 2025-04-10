# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesAudio:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audio_redirection_enable': 'bool',
        'play_volume': 'str',
        'play_volume_ratio': 'str',
        'record_volume': 'str',
        'record_volume_ratio': 'str',
        'audio_transmission_mode': 'str',
        'play_redirection_enable': 'bool',
        'play_classification': 'str',
        'play_quality': 'str',
        'play_denoising': 'str',
        'play_agc': 'str',
        'play_crc': 'str',
        'play_device_mode': 'str',
        'play_delay_threshold': 'str',
        'play_amplitude_threshold': 'str',
        'play_prefill_data': 'str',
        'record_redirection_enable': 'bool',
        'record_classification': 'str',
        'record_quality': 'str',
        'record_denoising': 'str',
        'record_agc': 'str',
        'record_crc': 'str',
        'record_device_mode': 'str',
        'record_delay_threshold': 'str',
        'record_amplitude_threshold': 'str'
    }

    attribute_map = {
        'audio_redirection_enable': 'audio_redirection_enable',
        'play_volume': 'play_volume',
        'play_volume_ratio': 'play_volume_ratio',
        'record_volume': 'record_volume',
        'record_volume_ratio': 'record_volume_ratio',
        'audio_transmission_mode': 'audio_transmission_mode',
        'play_redirection_enable': 'play_redirection_enable',
        'play_classification': 'play_classification',
        'play_quality': 'play_quality',
        'play_denoising': 'play_denoising',
        'play_agc': 'play_agc',
        'play_crc': 'play_crc',
        'play_device_mode': 'play_device_mode',
        'play_delay_threshold': 'play_delay_threshold',
        'play_amplitude_threshold': 'play_amplitude_threshold',
        'play_prefill_data': 'play_prefill_data',
        'record_redirection_enable': 'record_redirection_enable',
        'record_classification': 'record_classification',
        'record_quality': 'record_quality',
        'record_denoising': 'record_denoising',
        'record_agc': 'record_agc',
        'record_crc': 'record_crc',
        'record_device_mode': 'record_device_mode',
        'record_delay_threshold': 'record_delay_threshold',
        'record_amplitude_threshold': 'record_amplitude_threshold'
    }

    def __init__(self, audio_redirection_enable=None, play_volume=None, play_volume_ratio=None, record_volume=None, record_volume_ratio=None, audio_transmission_mode=None, play_redirection_enable=None, play_classification=None, play_quality=None, play_denoising=None, play_agc=None, play_crc=None, play_device_mode=None, play_delay_threshold=None, play_amplitude_threshold=None, play_prefill_data=None, record_redirection_enable=None, record_classification=None, record_quality=None, record_denoising=None, record_agc=None, record_crc=None, record_device_mode=None, record_delay_threshold=None, record_amplitude_threshold=None):
        r"""PoliciesAudio

        The model defined in huaweicloud sdk

        :param audio_redirection_enable: 是否开启音频重定向。取值为： false：表示关闭。 true：表示开启。
        :type audio_redirection_enable: bool
        :param play_volume: 播音设置音量。 不设置音量取值为：Do Not Set Volume。 音量设置，最小值为10，最大值为100，中间取值，间隔为5的递增序列。如：10、15、20、25等。
        :type play_volume: str
        :param play_volume_ratio: 播音设置音量线性系数。取值为： 不设置：Do Not Set Volume Ratio。 低：Low。 中：Middle。 高：High。
        :type play_volume_ratio: str
        :param record_volume: 录音设置音量。 不设置取值为：Do Not Set Volume。 音量设置，最小值为10，最大值为100，中间取值，间隔为5的递增序列。如：10、15、20、25等。
        :type record_volume: str
        :param record_volume_ratio: 录音设置音量线性系数。取值为： 不设置：Do Not Set Volume Ratio。 低：Low。 中：Middle。 高：High。
        :type record_volume_ratio: str
        :param audio_transmission_mode: 音频传输方式。取值为： 可靠传输：Reliable Transmission。 实时传输：Real Time Transmission。
        :type audio_transmission_mode: str
        :param play_redirection_enable: 是否开启播音重定向。取值为： false：表示关闭。 true：表示开启。
        :type play_redirection_enable: bool
        :param play_classification: 播音场景。取值为： 无损播音：LossLess。 语音通话：Speech Call。 音乐播音：Music Play。 自动识别：Automatic Identification。
        :type play_classification: str
        :param play_quality: 播音质量。取值为： 低：Low。 中：Middle。 高：High
        :type play_quality: str
        :param play_denoising: 播音降噪。取值为： 不开启降噪：Disable Denoising。 开启降噪，最小值为-100，最大值为-5，中间取值，间隔为5的递增序列。如：-100、-95、-90、-85等。
        :type play_denoising: str
        :param play_agc: 播音增益。取值为：不开启增益：Disable AGC。开启增益，最小值为4000，最大值为32000，中间取值，从10000开始间隔为1000的递增序列。如：4000、6000、8000、10000、11000、12000、13000等。
        :type play_agc: str
        :param play_crc: 播音设置冗余。取值为： 不开启冗余：Disable CRC。 开启冗余：Enable CRC。
        :type play_crc: str
        :param play_device_mode: 播音设置模式。取值为： 播音设备共享模式：Play Device In Shared Mode。 播音设备独占模式：Play Device In Exclusive Mode。
        :type play_device_mode: str
        :param play_delay_threshold: 播音控制时延阈值。取值为：最小值为160，最大值为2500。中间取值，400以下为40的递增序列，1000以下为50的递增序列。从高到低为：2500、2000、1800、1500、1200、1000、950、900、850等。
        :type play_delay_threshold: str
        :param play_amplitude_threshold: 播音检测振幅阈值。取值为：2048、4096、5120、6144、7168、8192。
        :type play_amplitude_threshold: str
        :param play_prefill_data: 播音音乐预充数据。取值为：不预充：Do Not Prefill Data。预充取值：最小值为50，最大值为2000，250以前为50的递增序列，500以前为100的递增序列。从高到低取值如：2000、1500、1000、500、400、300、250。
        :type play_prefill_data: str
        :param record_redirection_enable: 是否开启录音重定向。取值为： false：表示关闭。 true：表示开启。
        :type record_redirection_enable: bool
        :param record_classification: 录音场景。取值为： 无损录音：LossLess。 语音通话：Speech Call。 音乐录音：Music Record。 自动识别：Automatic Identification。
        :type record_classification: str
        :param record_quality: 录音质量。取值为： 低：Low。 中：Middle。 高：High。
        :type record_quality: str
        :param record_denoising: 录音降噪。取值为： 不开启降噪：Disable Denoising。 开启降噪，最小值为-100，最大值为-5，中间取值，间隔为5的递增序列。如：-100、-95、-90、-85等。
        :type record_denoising: str
        :param record_agc: 录音增益。取值为：不开启增益：Disable AGC。开启增益，最小值为4000，最大值为32000，中间取值，从10000开始间隔为1000的递增序列。如：4000、6000、8000、10000、11000、12000、13000等。
        :type record_agc: str
        :param record_crc: 录音设置冗余。取值为： 不开启冗余：Disable CRC。 开启冗余：Enable CRC。
        :type record_crc: str
        :param record_device_mode: 录音设置模式。取值为： 播音设备共享模式：Record Device In Shared Mode。 播音设备独占模式：Record Device In Exclusive Mode。
        :type record_device_mode: str
        :param record_delay_threshold: 录音控制时延阈值。取值为：最小值为160，最大值为2500。中间取值，400以下为40的递增序列，1000以下为50的递增序列。从高到低为：2500、2000、1800、1500、1200、1000、950、900、850等。
        :type record_delay_threshold: str
        :param record_amplitude_threshold: 录音检测振幅阈值。取值为：2048、4096、5120、6144、7168、8192。
        :type record_amplitude_threshold: str
        """
        
        

        self._audio_redirection_enable = None
        self._play_volume = None
        self._play_volume_ratio = None
        self._record_volume = None
        self._record_volume_ratio = None
        self._audio_transmission_mode = None
        self._play_redirection_enable = None
        self._play_classification = None
        self._play_quality = None
        self._play_denoising = None
        self._play_agc = None
        self._play_crc = None
        self._play_device_mode = None
        self._play_delay_threshold = None
        self._play_amplitude_threshold = None
        self._play_prefill_data = None
        self._record_redirection_enable = None
        self._record_classification = None
        self._record_quality = None
        self._record_denoising = None
        self._record_agc = None
        self._record_crc = None
        self._record_device_mode = None
        self._record_delay_threshold = None
        self._record_amplitude_threshold = None
        self.discriminator = None

        if audio_redirection_enable is not None:
            self.audio_redirection_enable = audio_redirection_enable
        if play_volume is not None:
            self.play_volume = play_volume
        if play_volume_ratio is not None:
            self.play_volume_ratio = play_volume_ratio
        if record_volume is not None:
            self.record_volume = record_volume
        if record_volume_ratio is not None:
            self.record_volume_ratio = record_volume_ratio
        if audio_transmission_mode is not None:
            self.audio_transmission_mode = audio_transmission_mode
        if play_redirection_enable is not None:
            self.play_redirection_enable = play_redirection_enable
        if play_classification is not None:
            self.play_classification = play_classification
        if play_quality is not None:
            self.play_quality = play_quality
        if play_denoising is not None:
            self.play_denoising = play_denoising
        if play_agc is not None:
            self.play_agc = play_agc
        if play_crc is not None:
            self.play_crc = play_crc
        if play_device_mode is not None:
            self.play_device_mode = play_device_mode
        if play_delay_threshold is not None:
            self.play_delay_threshold = play_delay_threshold
        if play_amplitude_threshold is not None:
            self.play_amplitude_threshold = play_amplitude_threshold
        if play_prefill_data is not None:
            self.play_prefill_data = play_prefill_data
        if record_redirection_enable is not None:
            self.record_redirection_enable = record_redirection_enable
        if record_classification is not None:
            self.record_classification = record_classification
        if record_quality is not None:
            self.record_quality = record_quality
        if record_denoising is not None:
            self.record_denoising = record_denoising
        if record_agc is not None:
            self.record_agc = record_agc
        if record_crc is not None:
            self.record_crc = record_crc
        if record_device_mode is not None:
            self.record_device_mode = record_device_mode
        if record_delay_threshold is not None:
            self.record_delay_threshold = record_delay_threshold
        if record_amplitude_threshold is not None:
            self.record_amplitude_threshold = record_amplitude_threshold

    @property
    def audio_redirection_enable(self):
        r"""Gets the audio_redirection_enable of this PoliciesAudio.

        是否开启音频重定向。取值为： false：表示关闭。 true：表示开启。

        :return: The audio_redirection_enable of this PoliciesAudio.
        :rtype: bool
        """
        return self._audio_redirection_enable

    @audio_redirection_enable.setter
    def audio_redirection_enable(self, audio_redirection_enable):
        r"""Sets the audio_redirection_enable of this PoliciesAudio.

        是否开启音频重定向。取值为： false：表示关闭。 true：表示开启。

        :param audio_redirection_enable: The audio_redirection_enable of this PoliciesAudio.
        :type audio_redirection_enable: bool
        """
        self._audio_redirection_enable = audio_redirection_enable

    @property
    def play_volume(self):
        r"""Gets the play_volume of this PoliciesAudio.

        播音设置音量。 不设置音量取值为：Do Not Set Volume。 音量设置，最小值为10，最大值为100，中间取值，间隔为5的递增序列。如：10、15、20、25等。

        :return: The play_volume of this PoliciesAudio.
        :rtype: str
        """
        return self._play_volume

    @play_volume.setter
    def play_volume(self, play_volume):
        r"""Sets the play_volume of this PoliciesAudio.

        播音设置音量。 不设置音量取值为：Do Not Set Volume。 音量设置，最小值为10，最大值为100，中间取值，间隔为5的递增序列。如：10、15、20、25等。

        :param play_volume: The play_volume of this PoliciesAudio.
        :type play_volume: str
        """
        self._play_volume = play_volume

    @property
    def play_volume_ratio(self):
        r"""Gets the play_volume_ratio of this PoliciesAudio.

        播音设置音量线性系数。取值为： 不设置：Do Not Set Volume Ratio。 低：Low。 中：Middle。 高：High。

        :return: The play_volume_ratio of this PoliciesAudio.
        :rtype: str
        """
        return self._play_volume_ratio

    @play_volume_ratio.setter
    def play_volume_ratio(self, play_volume_ratio):
        r"""Sets the play_volume_ratio of this PoliciesAudio.

        播音设置音量线性系数。取值为： 不设置：Do Not Set Volume Ratio。 低：Low。 中：Middle。 高：High。

        :param play_volume_ratio: The play_volume_ratio of this PoliciesAudio.
        :type play_volume_ratio: str
        """
        self._play_volume_ratio = play_volume_ratio

    @property
    def record_volume(self):
        r"""Gets the record_volume of this PoliciesAudio.

        录音设置音量。 不设置取值为：Do Not Set Volume。 音量设置，最小值为10，最大值为100，中间取值，间隔为5的递增序列。如：10、15、20、25等。

        :return: The record_volume of this PoliciesAudio.
        :rtype: str
        """
        return self._record_volume

    @record_volume.setter
    def record_volume(self, record_volume):
        r"""Sets the record_volume of this PoliciesAudio.

        录音设置音量。 不设置取值为：Do Not Set Volume。 音量设置，最小值为10，最大值为100，中间取值，间隔为5的递增序列。如：10、15、20、25等。

        :param record_volume: The record_volume of this PoliciesAudio.
        :type record_volume: str
        """
        self._record_volume = record_volume

    @property
    def record_volume_ratio(self):
        r"""Gets the record_volume_ratio of this PoliciesAudio.

        录音设置音量线性系数。取值为： 不设置：Do Not Set Volume Ratio。 低：Low。 中：Middle。 高：High。

        :return: The record_volume_ratio of this PoliciesAudio.
        :rtype: str
        """
        return self._record_volume_ratio

    @record_volume_ratio.setter
    def record_volume_ratio(self, record_volume_ratio):
        r"""Sets the record_volume_ratio of this PoliciesAudio.

        录音设置音量线性系数。取值为： 不设置：Do Not Set Volume Ratio。 低：Low。 中：Middle。 高：High。

        :param record_volume_ratio: The record_volume_ratio of this PoliciesAudio.
        :type record_volume_ratio: str
        """
        self._record_volume_ratio = record_volume_ratio

    @property
    def audio_transmission_mode(self):
        r"""Gets the audio_transmission_mode of this PoliciesAudio.

        音频传输方式。取值为： 可靠传输：Reliable Transmission。 实时传输：Real Time Transmission。

        :return: The audio_transmission_mode of this PoliciesAudio.
        :rtype: str
        """
        return self._audio_transmission_mode

    @audio_transmission_mode.setter
    def audio_transmission_mode(self, audio_transmission_mode):
        r"""Sets the audio_transmission_mode of this PoliciesAudio.

        音频传输方式。取值为： 可靠传输：Reliable Transmission。 实时传输：Real Time Transmission。

        :param audio_transmission_mode: The audio_transmission_mode of this PoliciesAudio.
        :type audio_transmission_mode: str
        """
        self._audio_transmission_mode = audio_transmission_mode

    @property
    def play_redirection_enable(self):
        r"""Gets the play_redirection_enable of this PoliciesAudio.

        是否开启播音重定向。取值为： false：表示关闭。 true：表示开启。

        :return: The play_redirection_enable of this PoliciesAudio.
        :rtype: bool
        """
        return self._play_redirection_enable

    @play_redirection_enable.setter
    def play_redirection_enable(self, play_redirection_enable):
        r"""Sets the play_redirection_enable of this PoliciesAudio.

        是否开启播音重定向。取值为： false：表示关闭。 true：表示开启。

        :param play_redirection_enable: The play_redirection_enable of this PoliciesAudio.
        :type play_redirection_enable: bool
        """
        self._play_redirection_enable = play_redirection_enable

    @property
    def play_classification(self):
        r"""Gets the play_classification of this PoliciesAudio.

        播音场景。取值为： 无损播音：LossLess。 语音通话：Speech Call。 音乐播音：Music Play。 自动识别：Automatic Identification。

        :return: The play_classification of this PoliciesAudio.
        :rtype: str
        """
        return self._play_classification

    @play_classification.setter
    def play_classification(self, play_classification):
        r"""Sets the play_classification of this PoliciesAudio.

        播音场景。取值为： 无损播音：LossLess。 语音通话：Speech Call。 音乐播音：Music Play。 自动识别：Automatic Identification。

        :param play_classification: The play_classification of this PoliciesAudio.
        :type play_classification: str
        """
        self._play_classification = play_classification

    @property
    def play_quality(self):
        r"""Gets the play_quality of this PoliciesAudio.

        播音质量。取值为： 低：Low。 中：Middle。 高：High

        :return: The play_quality of this PoliciesAudio.
        :rtype: str
        """
        return self._play_quality

    @play_quality.setter
    def play_quality(self, play_quality):
        r"""Sets the play_quality of this PoliciesAudio.

        播音质量。取值为： 低：Low。 中：Middle。 高：High

        :param play_quality: The play_quality of this PoliciesAudio.
        :type play_quality: str
        """
        self._play_quality = play_quality

    @property
    def play_denoising(self):
        r"""Gets the play_denoising of this PoliciesAudio.

        播音降噪。取值为： 不开启降噪：Disable Denoising。 开启降噪，最小值为-100，最大值为-5，中间取值，间隔为5的递增序列。如：-100、-95、-90、-85等。

        :return: The play_denoising of this PoliciesAudio.
        :rtype: str
        """
        return self._play_denoising

    @play_denoising.setter
    def play_denoising(self, play_denoising):
        r"""Sets the play_denoising of this PoliciesAudio.

        播音降噪。取值为： 不开启降噪：Disable Denoising。 开启降噪，最小值为-100，最大值为-5，中间取值，间隔为5的递增序列。如：-100、-95、-90、-85等。

        :param play_denoising: The play_denoising of this PoliciesAudio.
        :type play_denoising: str
        """
        self._play_denoising = play_denoising

    @property
    def play_agc(self):
        r"""Gets the play_agc of this PoliciesAudio.

        播音增益。取值为：不开启增益：Disable AGC。开启增益，最小值为4000，最大值为32000，中间取值，从10000开始间隔为1000的递增序列。如：4000、6000、8000、10000、11000、12000、13000等。

        :return: The play_agc of this PoliciesAudio.
        :rtype: str
        """
        return self._play_agc

    @play_agc.setter
    def play_agc(self, play_agc):
        r"""Sets the play_agc of this PoliciesAudio.

        播音增益。取值为：不开启增益：Disable AGC。开启增益，最小值为4000，最大值为32000，中间取值，从10000开始间隔为1000的递增序列。如：4000、6000、8000、10000、11000、12000、13000等。

        :param play_agc: The play_agc of this PoliciesAudio.
        :type play_agc: str
        """
        self._play_agc = play_agc

    @property
    def play_crc(self):
        r"""Gets the play_crc of this PoliciesAudio.

        播音设置冗余。取值为： 不开启冗余：Disable CRC。 开启冗余：Enable CRC。

        :return: The play_crc of this PoliciesAudio.
        :rtype: str
        """
        return self._play_crc

    @play_crc.setter
    def play_crc(self, play_crc):
        r"""Sets the play_crc of this PoliciesAudio.

        播音设置冗余。取值为： 不开启冗余：Disable CRC。 开启冗余：Enable CRC。

        :param play_crc: The play_crc of this PoliciesAudio.
        :type play_crc: str
        """
        self._play_crc = play_crc

    @property
    def play_device_mode(self):
        r"""Gets the play_device_mode of this PoliciesAudio.

        播音设置模式。取值为： 播音设备共享模式：Play Device In Shared Mode。 播音设备独占模式：Play Device In Exclusive Mode。

        :return: The play_device_mode of this PoliciesAudio.
        :rtype: str
        """
        return self._play_device_mode

    @play_device_mode.setter
    def play_device_mode(self, play_device_mode):
        r"""Sets the play_device_mode of this PoliciesAudio.

        播音设置模式。取值为： 播音设备共享模式：Play Device In Shared Mode。 播音设备独占模式：Play Device In Exclusive Mode。

        :param play_device_mode: The play_device_mode of this PoliciesAudio.
        :type play_device_mode: str
        """
        self._play_device_mode = play_device_mode

    @property
    def play_delay_threshold(self):
        r"""Gets the play_delay_threshold of this PoliciesAudio.

        播音控制时延阈值。取值为：最小值为160，最大值为2500。中间取值，400以下为40的递增序列，1000以下为50的递增序列。从高到低为：2500、2000、1800、1500、1200、1000、950、900、850等。

        :return: The play_delay_threshold of this PoliciesAudio.
        :rtype: str
        """
        return self._play_delay_threshold

    @play_delay_threshold.setter
    def play_delay_threshold(self, play_delay_threshold):
        r"""Sets the play_delay_threshold of this PoliciesAudio.

        播音控制时延阈值。取值为：最小值为160，最大值为2500。中间取值，400以下为40的递增序列，1000以下为50的递增序列。从高到低为：2500、2000、1800、1500、1200、1000、950、900、850等。

        :param play_delay_threshold: The play_delay_threshold of this PoliciesAudio.
        :type play_delay_threshold: str
        """
        self._play_delay_threshold = play_delay_threshold

    @property
    def play_amplitude_threshold(self):
        r"""Gets the play_amplitude_threshold of this PoliciesAudio.

        播音检测振幅阈值。取值为：2048、4096、5120、6144、7168、8192。

        :return: The play_amplitude_threshold of this PoliciesAudio.
        :rtype: str
        """
        return self._play_amplitude_threshold

    @play_amplitude_threshold.setter
    def play_amplitude_threshold(self, play_amplitude_threshold):
        r"""Sets the play_amplitude_threshold of this PoliciesAudio.

        播音检测振幅阈值。取值为：2048、4096、5120、6144、7168、8192。

        :param play_amplitude_threshold: The play_amplitude_threshold of this PoliciesAudio.
        :type play_amplitude_threshold: str
        """
        self._play_amplitude_threshold = play_amplitude_threshold

    @property
    def play_prefill_data(self):
        r"""Gets the play_prefill_data of this PoliciesAudio.

        播音音乐预充数据。取值为：不预充：Do Not Prefill Data。预充取值：最小值为50，最大值为2000，250以前为50的递增序列，500以前为100的递增序列。从高到低取值如：2000、1500、1000、500、400、300、250。

        :return: The play_prefill_data of this PoliciesAudio.
        :rtype: str
        """
        return self._play_prefill_data

    @play_prefill_data.setter
    def play_prefill_data(self, play_prefill_data):
        r"""Sets the play_prefill_data of this PoliciesAudio.

        播音音乐预充数据。取值为：不预充：Do Not Prefill Data。预充取值：最小值为50，最大值为2000，250以前为50的递增序列，500以前为100的递增序列。从高到低取值如：2000、1500、1000、500、400、300、250。

        :param play_prefill_data: The play_prefill_data of this PoliciesAudio.
        :type play_prefill_data: str
        """
        self._play_prefill_data = play_prefill_data

    @property
    def record_redirection_enable(self):
        r"""Gets the record_redirection_enable of this PoliciesAudio.

        是否开启录音重定向。取值为： false：表示关闭。 true：表示开启。

        :return: The record_redirection_enable of this PoliciesAudio.
        :rtype: bool
        """
        return self._record_redirection_enable

    @record_redirection_enable.setter
    def record_redirection_enable(self, record_redirection_enable):
        r"""Sets the record_redirection_enable of this PoliciesAudio.

        是否开启录音重定向。取值为： false：表示关闭。 true：表示开启。

        :param record_redirection_enable: The record_redirection_enable of this PoliciesAudio.
        :type record_redirection_enable: bool
        """
        self._record_redirection_enable = record_redirection_enable

    @property
    def record_classification(self):
        r"""Gets the record_classification of this PoliciesAudio.

        录音场景。取值为： 无损录音：LossLess。 语音通话：Speech Call。 音乐录音：Music Record。 自动识别：Automatic Identification。

        :return: The record_classification of this PoliciesAudio.
        :rtype: str
        """
        return self._record_classification

    @record_classification.setter
    def record_classification(self, record_classification):
        r"""Sets the record_classification of this PoliciesAudio.

        录音场景。取值为： 无损录音：LossLess。 语音通话：Speech Call。 音乐录音：Music Record。 自动识别：Automatic Identification。

        :param record_classification: The record_classification of this PoliciesAudio.
        :type record_classification: str
        """
        self._record_classification = record_classification

    @property
    def record_quality(self):
        r"""Gets the record_quality of this PoliciesAudio.

        录音质量。取值为： 低：Low。 中：Middle。 高：High。

        :return: The record_quality of this PoliciesAudio.
        :rtype: str
        """
        return self._record_quality

    @record_quality.setter
    def record_quality(self, record_quality):
        r"""Sets the record_quality of this PoliciesAudio.

        录音质量。取值为： 低：Low。 中：Middle。 高：High。

        :param record_quality: The record_quality of this PoliciesAudio.
        :type record_quality: str
        """
        self._record_quality = record_quality

    @property
    def record_denoising(self):
        r"""Gets the record_denoising of this PoliciesAudio.

        录音降噪。取值为： 不开启降噪：Disable Denoising。 开启降噪，最小值为-100，最大值为-5，中间取值，间隔为5的递增序列。如：-100、-95、-90、-85等。

        :return: The record_denoising of this PoliciesAudio.
        :rtype: str
        """
        return self._record_denoising

    @record_denoising.setter
    def record_denoising(self, record_denoising):
        r"""Sets the record_denoising of this PoliciesAudio.

        录音降噪。取值为： 不开启降噪：Disable Denoising。 开启降噪，最小值为-100，最大值为-5，中间取值，间隔为5的递增序列。如：-100、-95、-90、-85等。

        :param record_denoising: The record_denoising of this PoliciesAudio.
        :type record_denoising: str
        """
        self._record_denoising = record_denoising

    @property
    def record_agc(self):
        r"""Gets the record_agc of this PoliciesAudio.

        录音增益。取值为：不开启增益：Disable AGC。开启增益，最小值为4000，最大值为32000，中间取值，从10000开始间隔为1000的递增序列。如：4000、6000、8000、10000、11000、12000、13000等。

        :return: The record_agc of this PoliciesAudio.
        :rtype: str
        """
        return self._record_agc

    @record_agc.setter
    def record_agc(self, record_agc):
        r"""Sets the record_agc of this PoliciesAudio.

        录音增益。取值为：不开启增益：Disable AGC。开启增益，最小值为4000，最大值为32000，中间取值，从10000开始间隔为1000的递增序列。如：4000、6000、8000、10000、11000、12000、13000等。

        :param record_agc: The record_agc of this PoliciesAudio.
        :type record_agc: str
        """
        self._record_agc = record_agc

    @property
    def record_crc(self):
        r"""Gets the record_crc of this PoliciesAudio.

        录音设置冗余。取值为： 不开启冗余：Disable CRC。 开启冗余：Enable CRC。

        :return: The record_crc of this PoliciesAudio.
        :rtype: str
        """
        return self._record_crc

    @record_crc.setter
    def record_crc(self, record_crc):
        r"""Sets the record_crc of this PoliciesAudio.

        录音设置冗余。取值为： 不开启冗余：Disable CRC。 开启冗余：Enable CRC。

        :param record_crc: The record_crc of this PoliciesAudio.
        :type record_crc: str
        """
        self._record_crc = record_crc

    @property
    def record_device_mode(self):
        r"""Gets the record_device_mode of this PoliciesAudio.

        录音设置模式。取值为： 播音设备共享模式：Record Device In Shared Mode。 播音设备独占模式：Record Device In Exclusive Mode。

        :return: The record_device_mode of this PoliciesAudio.
        :rtype: str
        """
        return self._record_device_mode

    @record_device_mode.setter
    def record_device_mode(self, record_device_mode):
        r"""Sets the record_device_mode of this PoliciesAudio.

        录音设置模式。取值为： 播音设备共享模式：Record Device In Shared Mode。 播音设备独占模式：Record Device In Exclusive Mode。

        :param record_device_mode: The record_device_mode of this PoliciesAudio.
        :type record_device_mode: str
        """
        self._record_device_mode = record_device_mode

    @property
    def record_delay_threshold(self):
        r"""Gets the record_delay_threshold of this PoliciesAudio.

        录音控制时延阈值。取值为：最小值为160，最大值为2500。中间取值，400以下为40的递增序列，1000以下为50的递增序列。从高到低为：2500、2000、1800、1500、1200、1000、950、900、850等。

        :return: The record_delay_threshold of this PoliciesAudio.
        :rtype: str
        """
        return self._record_delay_threshold

    @record_delay_threshold.setter
    def record_delay_threshold(self, record_delay_threshold):
        r"""Sets the record_delay_threshold of this PoliciesAudio.

        录音控制时延阈值。取值为：最小值为160，最大值为2500。中间取值，400以下为40的递增序列，1000以下为50的递增序列。从高到低为：2500、2000、1800、1500、1200、1000、950、900、850等。

        :param record_delay_threshold: The record_delay_threshold of this PoliciesAudio.
        :type record_delay_threshold: str
        """
        self._record_delay_threshold = record_delay_threshold

    @property
    def record_amplitude_threshold(self):
        r"""Gets the record_amplitude_threshold of this PoliciesAudio.

        录音检测振幅阈值。取值为：2048、4096、5120、6144、7168、8192。

        :return: The record_amplitude_threshold of this PoliciesAudio.
        :rtype: str
        """
        return self._record_amplitude_threshold

    @record_amplitude_threshold.setter
    def record_amplitude_threshold(self, record_amplitude_threshold):
        r"""Sets the record_amplitude_threshold of this PoliciesAudio.

        录音检测振幅阈值。取值为：2048、4096、5120、6144、7168、8192。

        :param record_amplitude_threshold: The record_amplitude_threshold of this PoliciesAudio.
        :type record_amplitude_threshold: str
        """
        self._record_amplitude_threshold = record_amplitude_threshold

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
        if not isinstance(other, PoliciesAudio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
