# coding: utf-8

import pprint
import re

import six





class CreateTranscodingReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'input': 'ObsObjInfo',
        'output': 'ObsObjInfo',
        'trans_template_id': 'list[int]',
        'av_parameters': 'list[AvParameters]',
        'output_filenames': 'list[str]',
        'user_data': 'str',
        'watermarks': 'list[WatermarkRequest]',
        'thumbnail': 'Thumbnail',
        'digital_watermark': 'DigitalWatermark',
        'priority': 'int',
        'audit': 'Audit',
        'subtitle': 'Subtitle',
        'special_effect': 'SpecialEffect',
        'encryption': 'Encryption',
        'crop': 'Crop',
        'audio_track': 'AudioTrack',
        'multi_audio': 'MultiAudio',
        'video_process': 'VideoProcess',
        'audio_process': 'AudioProcess',
        'quality_enhance': 'QualityEnhance',
        'system_process': 'SystemProcess',
        'template_extend': 'TemplateExtend'
    }

    attribute_map = {
        'input': 'input',
        'output': 'output',
        'trans_template_id': 'trans_template_id',
        'av_parameters': 'av_parameters',
        'output_filenames': 'output_filenames',
        'user_data': 'user_data',
        'watermarks': 'watermarks',
        'thumbnail': 'thumbnail',
        'digital_watermark': 'digital_watermark',
        'priority': 'priority',
        'audit': 'audit',
        'subtitle': 'subtitle',
        'special_effect': 'special_effect',
        'encryption': 'encryption',
        'crop': 'crop',
        'audio_track': 'audio_track',
        'multi_audio': 'multi_audio',
        'video_process': 'video_process',
        'audio_process': 'audio_process',
        'quality_enhance': 'quality_enhance',
        'system_process': 'system_process',
        'template_extend': 'template_extend'
    }

    def __init__(self, input=None, output=None, trans_template_id=None, av_parameters=None, output_filenames=None, user_data=None, watermarks=None, thumbnail=None, digital_watermark=None, priority=6, audit=None, subtitle=None, special_effect=None, encryption=None, crop=None, audio_track=None, multi_audio=None, video_process=None, audio_process=None, quality_enhance=None, system_process=None, template_extend=None):
        """CreateTranscodingReq - a model defined in huaweicloud sdk"""
        
        

        self._input = None
        self._output = None
        self._trans_template_id = None
        self._av_parameters = None
        self._output_filenames = None
        self._user_data = None
        self._watermarks = None
        self._thumbnail = None
        self._digital_watermark = None
        self._priority = None
        self._audit = None
        self._subtitle = None
        self._special_effect = None
        self._encryption = None
        self._crop = None
        self._audio_track = None
        self._multi_audio = None
        self._video_process = None
        self._audio_process = None
        self._quality_enhance = None
        self._system_process = None
        self._template_extend = None
        self.discriminator = None

        if input is not None:
            self.input = input
        self.output = output
        if trans_template_id is not None:
            self.trans_template_id = trans_template_id
        if av_parameters is not None:
            self.av_parameters = av_parameters
        if output_filenames is not None:
            self.output_filenames = output_filenames
        if user_data is not None:
            self.user_data = user_data
        if watermarks is not None:
            self.watermarks = watermarks
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if digital_watermark is not None:
            self.digital_watermark = digital_watermark
        if priority is not None:
            self.priority = priority
        if audit is not None:
            self.audit = audit
        if subtitle is not None:
            self.subtitle = subtitle
        if special_effect is not None:
            self.special_effect = special_effect
        if encryption is not None:
            self.encryption = encryption
        if crop is not None:
            self.crop = crop
        if audio_track is not None:
            self.audio_track = audio_track
        if multi_audio is not None:
            self.multi_audio = multi_audio
        if video_process is not None:
            self.video_process = video_process
        if audio_process is not None:
            self.audio_process = audio_process
        if quality_enhance is not None:
            self.quality_enhance = quality_enhance
        if system_process is not None:
            self.system_process = system_process
        if template_extend is not None:
            self.template_extend = template_extend

    @property
    def input(self):
        """Gets the input of this CreateTranscodingReq.


        :return: The input of this CreateTranscodingReq.
        :rtype: ObsObjInfo
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this CreateTranscodingReq.


        :param input: The input of this CreateTranscodingReq.
        :type: ObsObjInfo
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this CreateTranscodingReq.


        :return: The output of this CreateTranscodingReq.
        :rtype: ObsObjInfo
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CreateTranscodingReq.


        :param output: The output of this CreateTranscodingReq.
        :type: ObsObjInfo
        """
        self._output = output

    @property
    def trans_template_id(self):
        """Gets the trans_template_id of this CreateTranscodingReq.

        转码模板ID，没带av_parameter参数时，必须带该参数，数组，每一路转码输出对应一个转码配置模板ID，最多支持9个模板ID。  多个转码模板中如下参数可变，其他都必须一致：  - 视频bitrate，height，width。 

        :return: The trans_template_id of this CreateTranscodingReq.
        :rtype: list[int]
        """
        return self._trans_template_id

    @trans_template_id.setter
    def trans_template_id(self, trans_template_id):
        """Sets the trans_template_id of this CreateTranscodingReq.

        转码模板ID，没带av_parameter参数时，必须带该参数，数组，每一路转码输出对应一个转码配置模板ID，最多支持9个模板ID。  多个转码模板中如下参数可变，其他都必须一致：  - 视频bitrate，height，width。 

        :param trans_template_id: The trans_template_id of this CreateTranscodingReq.
        :type: list[int]
        """
        self._trans_template_id = trans_template_id

    @property
    def av_parameters(self):
        """Gets the av_parameters of this CreateTranscodingReq.

        转码参数。  若同时设置“trans_template_id”和此参数，则优先使用此参数进行转码，不带trans_template_id时，该参数必选。 

        :return: The av_parameters of this CreateTranscodingReq.
        :rtype: list[AvParameters]
        """
        return self._av_parameters

    @av_parameters.setter
    def av_parameters(self, av_parameters):
        """Sets the av_parameters of this CreateTranscodingReq.

        转码参数。  若同时设置“trans_template_id”和此参数，则优先使用此参数进行转码，不带trans_template_id时，该参数必选。 

        :param av_parameters: The av_parameters of this CreateTranscodingReq.
        :type: list[AvParameters]
        """
        self._av_parameters = av_parameters

    @property
    def output_filenames(self):
        """Gets the output_filenames of this CreateTranscodingReq.

        输出文件名称，每一路转码输出对应一个名称，需要与转码模板ID数组的顺序对应。  - 若设置该参数，表示输出文件按该参数命名。 - 若不设置该参数，表示输出文件按默认方式命名。 

        :return: The output_filenames of this CreateTranscodingReq.
        :rtype: list[str]
        """
        return self._output_filenames

    @output_filenames.setter
    def output_filenames(self, output_filenames):
        """Sets the output_filenames of this CreateTranscodingReq.

        输出文件名称，每一路转码输出对应一个名称，需要与转码模板ID数组的顺序对应。  - 若设置该参数，表示输出文件按该参数命名。 - 若不设置该参数，表示输出文件按默认方式命名。 

        :param output_filenames: The output_filenames of this CreateTranscodingReq.
        :type: list[str]
        """
        self._output_filenames = output_filenames

    @property
    def user_data(self):
        """Gets the user_data of this CreateTranscodingReq.

        用户自定义数据，该字段可在查询接口或消息通知中按原内容透传给用户。 

        :return: The user_data of this CreateTranscodingReq.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this CreateTranscodingReq.

        用户自定义数据，该字段可在查询接口或消息通知中按原内容透传给用户。 

        :param user_data: The user_data of this CreateTranscodingReq.
        :type: str
        """
        self._user_data = user_data

    @property
    def watermarks(self):
        """Gets the watermarks of this CreateTranscodingReq.

        图片水印参数，数组，最多支持20个成员。 

        :return: The watermarks of this CreateTranscodingReq.
        :rtype: list[WatermarkRequest]
        """
        return self._watermarks

    @watermarks.setter
    def watermarks(self, watermarks):
        """Sets the watermarks of this CreateTranscodingReq.

        图片水印参数，数组，最多支持20个成员。 

        :param watermarks: The watermarks of this CreateTranscodingReq.
        :type: list[WatermarkRequest]
        """
        self._watermarks = watermarks

    @property
    def thumbnail(self):
        """Gets the thumbnail of this CreateTranscodingReq.


        :return: The thumbnail of this CreateTranscodingReq.
        :rtype: Thumbnail
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this CreateTranscodingReq.


        :param thumbnail: The thumbnail of this CreateTranscodingReq.
        :type: Thumbnail
        """
        self._thumbnail = thumbnail

    @property
    def digital_watermark(self):
        """Gets the digital_watermark of this CreateTranscodingReq.


        :return: The digital_watermark of this CreateTranscodingReq.
        :rtype: DigitalWatermark
        """
        return self._digital_watermark

    @digital_watermark.setter
    def digital_watermark(self, digital_watermark):
        """Sets the digital_watermark of this CreateTranscodingReq.


        :param digital_watermark: The digital_watermark of this CreateTranscodingReq.
        :type: DigitalWatermark
        """
        self._digital_watermark = digital_watermark

    @property
    def priority(self):
        """Gets the priority of this CreateTranscodingReq.

        任务优先级，取值如下： - 9代表高优先级。 - 6代表中优先级，默认为6。  暂时只支持6和9。 

        :return: The priority of this CreateTranscodingReq.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CreateTranscodingReq.

        任务优先级，取值如下： - 9代表高优先级。 - 6代表中优先级，默认为6。  暂时只支持6和9。 

        :param priority: The priority of this CreateTranscodingReq.
        :type: int
        """
        self._priority = priority

    @property
    def audit(self):
        """Gets the audit of this CreateTranscodingReq.


        :return: The audit of this CreateTranscodingReq.
        :rtype: Audit
        """
        return self._audit

    @audit.setter
    def audit(self, audit):
        """Sets the audit of this CreateTranscodingReq.


        :param audit: The audit of this CreateTranscodingReq.
        :type: Audit
        """
        self._audit = audit

    @property
    def subtitle(self):
        """Gets the subtitle of this CreateTranscodingReq.


        :return: The subtitle of this CreateTranscodingReq.
        :rtype: Subtitle
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle):
        """Sets the subtitle of this CreateTranscodingReq.


        :param subtitle: The subtitle of this CreateTranscodingReq.
        :type: Subtitle
        """
        self._subtitle = subtitle

    @property
    def special_effect(self):
        """Gets the special_effect of this CreateTranscodingReq.


        :return: The special_effect of this CreateTranscodingReq.
        :rtype: SpecialEffect
        """
        return self._special_effect

    @special_effect.setter
    def special_effect(self, special_effect):
        """Sets the special_effect of this CreateTranscodingReq.


        :param special_effect: The special_effect of this CreateTranscodingReq.
        :type: SpecialEffect
        """
        self._special_effect = special_effect

    @property
    def encryption(self):
        """Gets the encryption of this CreateTranscodingReq.


        :return: The encryption of this CreateTranscodingReq.
        :rtype: Encryption
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this CreateTranscodingReq.


        :param encryption: The encryption of this CreateTranscodingReq.
        :type: Encryption
        """
        self._encryption = encryption

    @property
    def crop(self):
        """Gets the crop of this CreateTranscodingReq.


        :return: The crop of this CreateTranscodingReq.
        :rtype: Crop
        """
        return self._crop

    @crop.setter
    def crop(self, crop):
        """Sets the crop of this CreateTranscodingReq.


        :param crop: The crop of this CreateTranscodingReq.
        :type: Crop
        """
        self._crop = crop

    @property
    def audio_track(self):
        """Gets the audio_track of this CreateTranscodingReq.


        :return: The audio_track of this CreateTranscodingReq.
        :rtype: AudioTrack
        """
        return self._audio_track

    @audio_track.setter
    def audio_track(self, audio_track):
        """Sets the audio_track of this CreateTranscodingReq.


        :param audio_track: The audio_track of this CreateTranscodingReq.
        :type: AudioTrack
        """
        self._audio_track = audio_track

    @property
    def multi_audio(self):
        """Gets the multi_audio of this CreateTranscodingReq.


        :return: The multi_audio of this CreateTranscodingReq.
        :rtype: MultiAudio
        """
        return self._multi_audio

    @multi_audio.setter
    def multi_audio(self, multi_audio):
        """Sets the multi_audio of this CreateTranscodingReq.


        :param multi_audio: The multi_audio of this CreateTranscodingReq.
        :type: MultiAudio
        """
        self._multi_audio = multi_audio

    @property
    def video_process(self):
        """Gets the video_process of this CreateTranscodingReq.


        :return: The video_process of this CreateTranscodingReq.
        :rtype: VideoProcess
        """
        return self._video_process

    @video_process.setter
    def video_process(self, video_process):
        """Sets the video_process of this CreateTranscodingReq.


        :param video_process: The video_process of this CreateTranscodingReq.
        :type: VideoProcess
        """
        self._video_process = video_process

    @property
    def audio_process(self):
        """Gets the audio_process of this CreateTranscodingReq.


        :return: The audio_process of this CreateTranscodingReq.
        :rtype: AudioProcess
        """
        return self._audio_process

    @audio_process.setter
    def audio_process(self, audio_process):
        """Sets the audio_process of this CreateTranscodingReq.


        :param audio_process: The audio_process of this CreateTranscodingReq.
        :type: AudioProcess
        """
        self._audio_process = audio_process

    @property
    def quality_enhance(self):
        """Gets the quality_enhance of this CreateTranscodingReq.


        :return: The quality_enhance of this CreateTranscodingReq.
        :rtype: QualityEnhance
        """
        return self._quality_enhance

    @quality_enhance.setter
    def quality_enhance(self, quality_enhance):
        """Sets the quality_enhance of this CreateTranscodingReq.


        :param quality_enhance: The quality_enhance of this CreateTranscodingReq.
        :type: QualityEnhance
        """
        self._quality_enhance = quality_enhance

    @property
    def system_process(self):
        """Gets the system_process of this CreateTranscodingReq.


        :return: The system_process of this CreateTranscodingReq.
        :rtype: SystemProcess
        """
        return self._system_process

    @system_process.setter
    def system_process(self, system_process):
        """Sets the system_process of this CreateTranscodingReq.


        :param system_process: The system_process of this CreateTranscodingReq.
        :type: SystemProcess
        """
        self._system_process = system_process

    @property
    def template_extend(self):
        """Gets the template_extend of this CreateTranscodingReq.


        :return: The template_extend of this CreateTranscodingReq.
        :rtype: TemplateExtend
        """
        return self._template_extend

    @template_extend.setter
    def template_extend(self, template_extend):
        """Sets the template_extend of this CreateTranscodingReq.


        :param template_extend: The template_extend of this CreateTranscodingReq.
        :type: TemplateExtend
        """
        self._template_extend = template_extend

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateTranscodingReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
