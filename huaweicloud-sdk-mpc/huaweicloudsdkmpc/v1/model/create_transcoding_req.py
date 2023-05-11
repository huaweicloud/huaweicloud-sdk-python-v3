# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'priority': 'int',
        'subtitle': 'Subtitle',
        'encryption': 'Encryption',
        'crop': 'Crop',
        'audio_track': 'AudioTrack',
        'multi_audio': 'MultiAudio',
        'video_process': 'VideoProcess',
        'audio_process': 'AudioProcess'
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
        'priority': 'priority',
        'subtitle': 'subtitle',
        'encryption': 'encryption',
        'crop': 'crop',
        'audio_track': 'audio_track',
        'multi_audio': 'multi_audio',
        'video_process': 'video_process',
        'audio_process': 'audio_process'
    }

    def __init__(self, input=None, output=None, trans_template_id=None, av_parameters=None, output_filenames=None, user_data=None, watermarks=None, thumbnail=None, priority=None, subtitle=None, encryption=None, crop=None, audio_track=None, multi_audio=None, video_process=None, audio_process=None):
        """CreateTranscodingReq

        The model defined in huaweicloud sdk

        :param input: 
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param trans_template_id: 转码模板ID，没带av_parameter参数时，必须带该参数，数组，每一路转码输出对应一个转码配置模板ID，最多支持9个模板ID。  多个转码模板中如下参数可变，其他都必须一致：  视频bitrate，height，width。 
        :type trans_template_id: list[int]
        :param av_parameters: 转码参数。  若同时设置“trans_template_id”和此参数，则优先使用此参数进行转码，不带trans_template_id时，该参数必选。 
        :type av_parameters: list[:class:`huaweicloudsdkmpc.v1.AvParameters`]
        :param output_filenames: 输出文件名称，每一路转码输出对应一个名称，需要与转码模板ID数组的顺序对应。  - 若设置该参数，表示输出文件按该参数命名。 - 若不设置该参数，表示输出文件按默认方式命名。 
        :type output_filenames: list[str]
        :param user_data: 用户自定义数据，该字段可在查询接口或消息通知中按原内容透传给用户。 
        :type user_data: str
        :param watermarks: 图片水印参数，数组，最多支持20个成员。 
        :type watermarks: list[:class:`huaweicloudsdkmpc.v1.WatermarkRequest`]
        :param thumbnail: 
        :type thumbnail: :class:`huaweicloudsdkmpc.v1.Thumbnail`
        :param priority: 任务优先级，取值如下： - 9代表高优先级。 - 6代表中优先级，默认为6。  暂时只支持6和9。 
        :type priority: int
        :param subtitle: 
        :type subtitle: :class:`huaweicloudsdkmpc.v1.Subtitle`
        :param encryption: 
        :type encryption: :class:`huaweicloudsdkmpc.v1.Encryption`
        :param crop: 
        :type crop: :class:`huaweicloudsdkmpc.v1.Crop`
        :param audio_track: 
        :type audio_track: :class:`huaweicloudsdkmpc.v1.AudioTrack`
        :param multi_audio: 
        :type multi_audio: :class:`huaweicloudsdkmpc.v1.MultiAudio`
        :param video_process: 
        :type video_process: :class:`huaweicloudsdkmpc.v1.VideoProcess`
        :param audio_process: 
        :type audio_process: :class:`huaweicloudsdkmpc.v1.AudioProcess`
        """
        
        

        self._input = None
        self._output = None
        self._trans_template_id = None
        self._av_parameters = None
        self._output_filenames = None
        self._user_data = None
        self._watermarks = None
        self._thumbnail = None
        self._priority = None
        self._subtitle = None
        self._encryption = None
        self._crop = None
        self._audio_track = None
        self._multi_audio = None
        self._video_process = None
        self._audio_process = None
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
        if priority is not None:
            self.priority = priority
        if subtitle is not None:
            self.subtitle = subtitle
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

    @property
    def input(self):
        """Gets the input of this CreateTranscodingReq.

        :return: The input of this CreateTranscodingReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this CreateTranscodingReq.

        :param input: The input of this CreateTranscodingReq.
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this CreateTranscodingReq.

        :return: The output of this CreateTranscodingReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CreateTranscodingReq.

        :param output: The output of this CreateTranscodingReq.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def trans_template_id(self):
        """Gets the trans_template_id of this CreateTranscodingReq.

        转码模板ID，没带av_parameter参数时，必须带该参数，数组，每一路转码输出对应一个转码配置模板ID，最多支持9个模板ID。  多个转码模板中如下参数可变，其他都必须一致：  视频bitrate，height，width。 

        :return: The trans_template_id of this CreateTranscodingReq.
        :rtype: list[int]
        """
        return self._trans_template_id

    @trans_template_id.setter
    def trans_template_id(self, trans_template_id):
        """Sets the trans_template_id of this CreateTranscodingReq.

        转码模板ID，没带av_parameter参数时，必须带该参数，数组，每一路转码输出对应一个转码配置模板ID，最多支持9个模板ID。  多个转码模板中如下参数可变，其他都必须一致：  视频bitrate，height，width。 

        :param trans_template_id: The trans_template_id of this CreateTranscodingReq.
        :type trans_template_id: list[int]
        """
        self._trans_template_id = trans_template_id

    @property
    def av_parameters(self):
        """Gets the av_parameters of this CreateTranscodingReq.

        转码参数。  若同时设置“trans_template_id”和此参数，则优先使用此参数进行转码，不带trans_template_id时，该参数必选。 

        :return: The av_parameters of this CreateTranscodingReq.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.AvParameters`]
        """
        return self._av_parameters

    @av_parameters.setter
    def av_parameters(self, av_parameters):
        """Sets the av_parameters of this CreateTranscodingReq.

        转码参数。  若同时设置“trans_template_id”和此参数，则优先使用此参数进行转码，不带trans_template_id时，该参数必选。 

        :param av_parameters: The av_parameters of this CreateTranscodingReq.
        :type av_parameters: list[:class:`huaweicloudsdkmpc.v1.AvParameters`]
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
        :type output_filenames: list[str]
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
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def watermarks(self):
        """Gets the watermarks of this CreateTranscodingReq.

        图片水印参数，数组，最多支持20个成员。 

        :return: The watermarks of this CreateTranscodingReq.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.WatermarkRequest`]
        """
        return self._watermarks

    @watermarks.setter
    def watermarks(self, watermarks):
        """Sets the watermarks of this CreateTranscodingReq.

        图片水印参数，数组，最多支持20个成员。 

        :param watermarks: The watermarks of this CreateTranscodingReq.
        :type watermarks: list[:class:`huaweicloudsdkmpc.v1.WatermarkRequest`]
        """
        self._watermarks = watermarks

    @property
    def thumbnail(self):
        """Gets the thumbnail of this CreateTranscodingReq.

        :return: The thumbnail of this CreateTranscodingReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.Thumbnail`
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this CreateTranscodingReq.

        :param thumbnail: The thumbnail of this CreateTranscodingReq.
        :type thumbnail: :class:`huaweicloudsdkmpc.v1.Thumbnail`
        """
        self._thumbnail = thumbnail

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
        :type priority: int
        """
        self._priority = priority

    @property
    def subtitle(self):
        """Gets the subtitle of this CreateTranscodingReq.

        :return: The subtitle of this CreateTranscodingReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.Subtitle`
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle):
        """Sets the subtitle of this CreateTranscodingReq.

        :param subtitle: The subtitle of this CreateTranscodingReq.
        :type subtitle: :class:`huaweicloudsdkmpc.v1.Subtitle`
        """
        self._subtitle = subtitle

    @property
    def encryption(self):
        """Gets the encryption of this CreateTranscodingReq.

        :return: The encryption of this CreateTranscodingReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.Encryption`
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this CreateTranscodingReq.

        :param encryption: The encryption of this CreateTranscodingReq.
        :type encryption: :class:`huaweicloudsdkmpc.v1.Encryption`
        """
        self._encryption = encryption

    @property
    def crop(self):
        """Gets the crop of this CreateTranscodingReq.

        :return: The crop of this CreateTranscodingReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.Crop`
        """
        return self._crop

    @crop.setter
    def crop(self, crop):
        """Sets the crop of this CreateTranscodingReq.

        :param crop: The crop of this CreateTranscodingReq.
        :type crop: :class:`huaweicloudsdkmpc.v1.Crop`
        """
        self._crop = crop

    @property
    def audio_track(self):
        """Gets the audio_track of this CreateTranscodingReq.

        :return: The audio_track of this CreateTranscodingReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.AudioTrack`
        """
        return self._audio_track

    @audio_track.setter
    def audio_track(self, audio_track):
        """Sets the audio_track of this CreateTranscodingReq.

        :param audio_track: The audio_track of this CreateTranscodingReq.
        :type audio_track: :class:`huaweicloudsdkmpc.v1.AudioTrack`
        """
        self._audio_track = audio_track

    @property
    def multi_audio(self):
        """Gets the multi_audio of this CreateTranscodingReq.

        :return: The multi_audio of this CreateTranscodingReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.MultiAudio`
        """
        return self._multi_audio

    @multi_audio.setter
    def multi_audio(self, multi_audio):
        """Sets the multi_audio of this CreateTranscodingReq.

        :param multi_audio: The multi_audio of this CreateTranscodingReq.
        :type multi_audio: :class:`huaweicloudsdkmpc.v1.MultiAudio`
        """
        self._multi_audio = multi_audio

    @property
    def video_process(self):
        """Gets the video_process of this CreateTranscodingReq.

        :return: The video_process of this CreateTranscodingReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.VideoProcess`
        """
        return self._video_process

    @video_process.setter
    def video_process(self, video_process):
        """Sets the video_process of this CreateTranscodingReq.

        :param video_process: The video_process of this CreateTranscodingReq.
        :type video_process: :class:`huaweicloudsdkmpc.v1.VideoProcess`
        """
        self._video_process = video_process

    @property
    def audio_process(self):
        """Gets the audio_process of this CreateTranscodingReq.

        :return: The audio_process of this CreateTranscodingReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.AudioProcess`
        """
        return self._audio_process

    @audio_process.setter
    def audio_process(self, audio_process):
        """Sets the audio_process of this CreateTranscodingReq.

        :param audio_process: The audio_process of this CreateTranscodingReq.
        :type audio_process: :class:`huaweicloudsdkmpc.v1.AudioProcess`
        """
        self._audio_process = audio_process

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
        if not isinstance(other, CreateTranscodingReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
