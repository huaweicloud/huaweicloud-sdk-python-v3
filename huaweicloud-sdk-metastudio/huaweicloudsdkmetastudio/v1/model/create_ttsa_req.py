# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTTSAReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'voice_asset_id': 'str',
        'script_type': 'str',
        'text': 'str',
        'audio_file_download_url': 'str',
        'speed': 'int',
        'pitch': 'int',
        'volume': 'int',
        'emotion': 'str',
        'style_id': 'str',
        'camera_position': 'str',
        'job_type': 'str'
    }

    attribute_map = {
        'voice_asset_id': 'voice_asset_id',
        'script_type': 'script_type',
        'text': 'text',
        'audio_file_download_url': 'audio_file_download_url',
        'speed': 'speed',
        'pitch': 'pitch',
        'volume': 'volume',
        'emotion': 'emotion',
        'style_id': 'style_id',
        'camera_position': 'camera_position',
        'job_type': 'job_type'
    }

    def __init__(self, voice_asset_id=None, script_type=None, text=None, audio_file_download_url=None, speed=None, pitch=None, volume=None, emotion=None, style_id=None, camera_position=None, job_type=None):
        r"""CreateTTSAReq

        The model defined in huaweicloud sdk

        :param voice_asset_id: 音色模型ID。需要使用MetaStudio的数字资产管理相关接口从资产库查出。
        :type voice_asset_id: str
        :param script_type: 脚本类型，即视频制作的驱动方式。默认TEXT * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动
        :type script_type: str
        :param text: HTML格式的台词，可包含动作。最多2048个字符。 &gt; * HTML格式举例：\\&lt;speak&gt;大家好&lt;insert-action id&#x3D;\\\&quot;14cc7bbcde4982aab82f9d9af9e0f743\\\&quot;/&gt;，非常高兴给大家介绍MetaStudio。\\&lt;/speak&gt; &gt; * insert-action id通过查询资产列表接口获取，查询时asset_type&#x3D;ANIMATION &gt; * 多音字标签：\\&lt;phoneme ph&#x3D;\\\&quot;拼音\\\&quot;&gt;汉字\\&lt;/phoneme&gt;，南京\\&lt;phoneme ph&#x3D;\\\&quot;shi4 zhang3\\\&quot;&gt;市长\\&lt;/phoneme&gt;江大桥。 &gt; * 停顿标签：\\&lt;break/&gt;，中方一贯主张\\&lt;break/&gt;维护国家主权平等，不干涉他国内政\\&lt;break time&#x3D;\\\&quot;300ms\\\&quot;/&gt;是联合国宪章\\&lt;break time&#x3D;\\\&quot;500ms\\\&quot;/&gt;最重要的原则。
        :type text: str
        :param audio_file_download_url: 语音驱动音频文件下载URL。
        :type audio_file_download_url: str
        :param speed: 语速。  取值范围[50,200]   默认值：100
        :type speed: int
        :param pitch: 基频。  取值范围[50,200]  默认值：100
        :type pitch: int
        :param volume: 音量。  取值范围[90,240]   默认值：100
        :type volume: int
        :param emotion: 情感标签。 * ANGER：愤怒 * HAPPY：开心 * SAD：悲伤 * CALM：平静
        :type emotion: str
        :param style_id: 风格化ID。需要调用数字人风格管理相关接口，从系统中查得。
        :type style_id: str
        :param camera_position: 人位置及相机位置。由如下4组浮点数组成的字符：人位置的X/Y/Z值，人角度的Pitch/Yaw/Roll值；相机位置的X/Y/Z值，相机角度的Pitch/Yaw/Roll值。
        :type camera_position: str
        :param job_type: 任务类型。 * REAL_JOB：实时任务。如数字人交互。 * UNREAL_JOB：非实时任务。如数字人视频制作
        :type job_type: str
        """
        
        

        self._voice_asset_id = None
        self._script_type = None
        self._text = None
        self._audio_file_download_url = None
        self._speed = None
        self._pitch = None
        self._volume = None
        self._emotion = None
        self._style_id = None
        self._camera_position = None
        self._job_type = None
        self.discriminator = None

        self.voice_asset_id = voice_asset_id
        if script_type is not None:
            self.script_type = script_type
        if text is not None:
            self.text = text
        if audio_file_download_url is not None:
            self.audio_file_download_url = audio_file_download_url
        if speed is not None:
            self.speed = speed
        if pitch is not None:
            self.pitch = pitch
        if volume is not None:
            self.volume = volume
        if emotion is not None:
            self.emotion = emotion
        self.style_id = style_id
        if camera_position is not None:
            self.camera_position = camera_position
        if job_type is not None:
            self.job_type = job_type

    @property
    def voice_asset_id(self):
        r"""Gets the voice_asset_id of this CreateTTSAReq.

        音色模型ID。需要使用MetaStudio的数字资产管理相关接口从资产库查出。

        :return: The voice_asset_id of this CreateTTSAReq.
        :rtype: str
        """
        return self._voice_asset_id

    @voice_asset_id.setter
    def voice_asset_id(self, voice_asset_id):
        r"""Sets the voice_asset_id of this CreateTTSAReq.

        音色模型ID。需要使用MetaStudio的数字资产管理相关接口从资产库查出。

        :param voice_asset_id: The voice_asset_id of this CreateTTSAReq.
        :type voice_asset_id: str
        """
        self._voice_asset_id = voice_asset_id

    @property
    def script_type(self):
        r"""Gets the script_type of this CreateTTSAReq.

        脚本类型，即视频制作的驱动方式。默认TEXT * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动

        :return: The script_type of this CreateTTSAReq.
        :rtype: str
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        r"""Sets the script_type of this CreateTTSAReq.

        脚本类型，即视频制作的驱动方式。默认TEXT * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动

        :param script_type: The script_type of this CreateTTSAReq.
        :type script_type: str
        """
        self._script_type = script_type

    @property
    def text(self):
        r"""Gets the text of this CreateTTSAReq.

        HTML格式的台词，可包含动作。最多2048个字符。 > * HTML格式举例：\\<speak>大家好<insert-action id=\\\"14cc7bbcde4982aab82f9d9af9e0f743\\\"/>，非常高兴给大家介绍MetaStudio。\\</speak> > * insert-action id通过查询资产列表接口获取，查询时asset_type=ANIMATION > * 多音字标签：\\<phoneme ph=\\\"拼音\\\">汉字\\</phoneme>，南京\\<phoneme ph=\\\"shi4 zhang3\\\">市长\\</phoneme>江大桥。 > * 停顿标签：\\<break/>，中方一贯主张\\<break/>维护国家主权平等，不干涉他国内政\\<break time=\\\"300ms\\\"/>是联合国宪章\\<break time=\\\"500ms\\\"/>最重要的原则。

        :return: The text of this CreateTTSAReq.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this CreateTTSAReq.

        HTML格式的台词，可包含动作。最多2048个字符。 > * HTML格式举例：\\<speak>大家好<insert-action id=\\\"14cc7bbcde4982aab82f9d9af9e0f743\\\"/>，非常高兴给大家介绍MetaStudio。\\</speak> > * insert-action id通过查询资产列表接口获取，查询时asset_type=ANIMATION > * 多音字标签：\\<phoneme ph=\\\"拼音\\\">汉字\\</phoneme>，南京\\<phoneme ph=\\\"shi4 zhang3\\\">市长\\</phoneme>江大桥。 > * 停顿标签：\\<break/>，中方一贯主张\\<break/>维护国家主权平等，不干涉他国内政\\<break time=\\\"300ms\\\"/>是联合国宪章\\<break time=\\\"500ms\\\"/>最重要的原则。

        :param text: The text of this CreateTTSAReq.
        :type text: str
        """
        self._text = text

    @property
    def audio_file_download_url(self):
        r"""Gets the audio_file_download_url of this CreateTTSAReq.

        语音驱动音频文件下载URL。

        :return: The audio_file_download_url of this CreateTTSAReq.
        :rtype: str
        """
        return self._audio_file_download_url

    @audio_file_download_url.setter
    def audio_file_download_url(self, audio_file_download_url):
        r"""Sets the audio_file_download_url of this CreateTTSAReq.

        语音驱动音频文件下载URL。

        :param audio_file_download_url: The audio_file_download_url of this CreateTTSAReq.
        :type audio_file_download_url: str
        """
        self._audio_file_download_url = audio_file_download_url

    @property
    def speed(self):
        r"""Gets the speed of this CreateTTSAReq.

        语速。  取值范围[50,200]   默认值：100

        :return: The speed of this CreateTTSAReq.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        r"""Sets the speed of this CreateTTSAReq.

        语速。  取值范围[50,200]   默认值：100

        :param speed: The speed of this CreateTTSAReq.
        :type speed: int
        """
        self._speed = speed

    @property
    def pitch(self):
        r"""Gets the pitch of this CreateTTSAReq.

        基频。  取值范围[50,200]  默认值：100

        :return: The pitch of this CreateTTSAReq.
        :rtype: int
        """
        return self._pitch

    @pitch.setter
    def pitch(self, pitch):
        r"""Sets the pitch of this CreateTTSAReq.

        基频。  取值范围[50,200]  默认值：100

        :param pitch: The pitch of this CreateTTSAReq.
        :type pitch: int
        """
        self._pitch = pitch

    @property
    def volume(self):
        r"""Gets the volume of this CreateTTSAReq.

        音量。  取值范围[90,240]   默认值：100

        :return: The volume of this CreateTTSAReq.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this CreateTTSAReq.

        音量。  取值范围[90,240]   默认值：100

        :param volume: The volume of this CreateTTSAReq.
        :type volume: int
        """
        self._volume = volume

    @property
    def emotion(self):
        r"""Gets the emotion of this CreateTTSAReq.

        情感标签。 * ANGER：愤怒 * HAPPY：开心 * SAD：悲伤 * CALM：平静

        :return: The emotion of this CreateTTSAReq.
        :rtype: str
        """
        return self._emotion

    @emotion.setter
    def emotion(self, emotion):
        r"""Sets the emotion of this CreateTTSAReq.

        情感标签。 * ANGER：愤怒 * HAPPY：开心 * SAD：悲伤 * CALM：平静

        :param emotion: The emotion of this CreateTTSAReq.
        :type emotion: str
        """
        self._emotion = emotion

    @property
    def style_id(self):
        r"""Gets the style_id of this CreateTTSAReq.

        风格化ID。需要调用数字人风格管理相关接口，从系统中查得。

        :return: The style_id of this CreateTTSAReq.
        :rtype: str
        """
        return self._style_id

    @style_id.setter
    def style_id(self, style_id):
        r"""Sets the style_id of this CreateTTSAReq.

        风格化ID。需要调用数字人风格管理相关接口，从系统中查得。

        :param style_id: The style_id of this CreateTTSAReq.
        :type style_id: str
        """
        self._style_id = style_id

    @property
    def camera_position(self):
        r"""Gets the camera_position of this CreateTTSAReq.

        人位置及相机位置。由如下4组浮点数组成的字符：人位置的X/Y/Z值，人角度的Pitch/Yaw/Roll值；相机位置的X/Y/Z值，相机角度的Pitch/Yaw/Roll值。

        :return: The camera_position of this CreateTTSAReq.
        :rtype: str
        """
        return self._camera_position

    @camera_position.setter
    def camera_position(self, camera_position):
        r"""Sets the camera_position of this CreateTTSAReq.

        人位置及相机位置。由如下4组浮点数组成的字符：人位置的X/Y/Z值，人角度的Pitch/Yaw/Roll值；相机位置的X/Y/Z值，相机角度的Pitch/Yaw/Roll值。

        :param camera_position: The camera_position of this CreateTTSAReq.
        :type camera_position: str
        """
        self._camera_position = camera_position

    @property
    def job_type(self):
        r"""Gets the job_type of this CreateTTSAReq.

        任务类型。 * REAL_JOB：实时任务。如数字人交互。 * UNREAL_JOB：非实时任务。如数字人视频制作

        :return: The job_type of this CreateTTSAReq.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this CreateTTSAReq.

        任务类型。 * REAL_JOB：实时任务。如数字人交互。 * UNREAL_JOB：非实时任务。如数字人视频制作

        :param job_type: The job_type of this CreateTTSAReq.
        :type job_type: str
        """
        self._job_type = job_type

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
        if not isinstance(other, CreateTTSAReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
