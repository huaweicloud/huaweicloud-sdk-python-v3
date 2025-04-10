# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Update2dModelTrainingJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'contact': 'str',
        'command_message': 'str',
        'video_multipart_count': 'int',
        'action_video_multipart_count': 'int',
        'is_background_replacement': 'bool',
        'batch_name': 'str',
        'tags': 'list[str]',
        'samples_basic_info': 'list[ActionBasicSampleInfo]',
        'supported_service': 'list[SupportedServiceEnum]',
        'audio_source_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'contact': 'contact',
        'command_message': 'command_message',
        'video_multipart_count': 'video_multipart_count',
        'action_video_multipart_count': 'action_video_multipart_count',
        'is_background_replacement': 'is_background_replacement',
        'batch_name': 'batch_name',
        'tags': 'tags',
        'samples_basic_info': 'samples_basic_info',
        'supported_service': 'supported_service',
        'audio_source_type': 'audio_source_type'
    }

    def __init__(self, name=None, contact=None, command_message=None, video_multipart_count=None, action_video_multipart_count=None, is_background_replacement=None, batch_name=None, tags=None, samples_basic_info=None, supported_service=None, audio_source_type=None):
        r"""Update2dModelTrainingJobReq

        The model defined in huaweicloud sdk

        :param name: 分身数字人模型名称。该名称会作为资产库中分身数字人模型资产名称。
        :type name: str
        :param contact: 分身数字人训练任务创建者的手机号。
        :type contact: str
        :param command_message: 命令类型： * UPDATE_VIDEO: 更新视频 * UPLOAD_VIDEO：上传视频 * CONFIRM_ACTION_VIDEO: 确认动作编排视频 * GET_ACTION_VIDEO_MULTIPART: 获取动作编排视频分片
        :type command_message: str
        :param video_multipart_count: 训练视频上传分片数（上传时对唯一训练视频文件的数据分片，用于对该文件的并发上传，不是分多个视频文件上传）。
        :type video_multipart_count: int
        :param action_video_multipart_count: 动作视频上传分片数。
        :type action_video_multipart_count: int
        :param is_background_replacement: 分身数字人是否需要背景替换。需要背景替换的分身数字人训练视频需要绿幕拍摄。
        :type is_background_replacement: bool
        :param batch_name: 分身数字人训练任务的批次名称。
        :type batch_name: str
        :param tags: 分身数字人训练任务标签。
        :type tags: list[str]
        :param samples_basic_info: 动作视频样例可修改信息。
        :type samples_basic_info: list[:class:`huaweicloudsdkmetastudio.v1.ActionBasicSampleInfo`]
        :param supported_service: 该任务所生成的模型支持的业务类型，可多选。  Flexus版数字人仅支持选择“VIDEO_2D”。
        :type supported_service: list[:class:`huaweicloudsdkmetastudio.v1.SupportedServiceEnum`]
        :param audio_source_type: 声音来源类型 * VIDEO：视频中抽取音频 * AUDIO：单独上传的音频
        :type audio_source_type: str
        """
        
        

        self._name = None
        self._contact = None
        self._command_message = None
        self._video_multipart_count = None
        self._action_video_multipart_count = None
        self._is_background_replacement = None
        self._batch_name = None
        self._tags = None
        self._samples_basic_info = None
        self._supported_service = None
        self._audio_source_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if contact is not None:
            self.contact = contact
        if command_message is not None:
            self.command_message = command_message
        if video_multipart_count is not None:
            self.video_multipart_count = video_multipart_count
        if action_video_multipart_count is not None:
            self.action_video_multipart_count = action_video_multipart_count
        if is_background_replacement is not None:
            self.is_background_replacement = is_background_replacement
        if batch_name is not None:
            self.batch_name = batch_name
        if tags is not None:
            self.tags = tags
        if samples_basic_info is not None:
            self.samples_basic_info = samples_basic_info
        if supported_service is not None:
            self.supported_service = supported_service
        if audio_source_type is not None:
            self.audio_source_type = audio_source_type

    @property
    def name(self):
        r"""Gets the name of this Update2dModelTrainingJobReq.

        分身数字人模型名称。该名称会作为资产库中分身数字人模型资产名称。

        :return: The name of this Update2dModelTrainingJobReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Update2dModelTrainingJobReq.

        分身数字人模型名称。该名称会作为资产库中分身数字人模型资产名称。

        :param name: The name of this Update2dModelTrainingJobReq.
        :type name: str
        """
        self._name = name

    @property
    def contact(self):
        r"""Gets the contact of this Update2dModelTrainingJobReq.

        分身数字人训练任务创建者的手机号。

        :return: The contact of this Update2dModelTrainingJobReq.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        r"""Sets the contact of this Update2dModelTrainingJobReq.

        分身数字人训练任务创建者的手机号。

        :param contact: The contact of this Update2dModelTrainingJobReq.
        :type contact: str
        """
        self._contact = contact

    @property
    def command_message(self):
        r"""Gets the command_message of this Update2dModelTrainingJobReq.

        命令类型： * UPDATE_VIDEO: 更新视频 * UPLOAD_VIDEO：上传视频 * CONFIRM_ACTION_VIDEO: 确认动作编排视频 * GET_ACTION_VIDEO_MULTIPART: 获取动作编排视频分片

        :return: The command_message of this Update2dModelTrainingJobReq.
        :rtype: str
        """
        return self._command_message

    @command_message.setter
    def command_message(self, command_message):
        r"""Sets the command_message of this Update2dModelTrainingJobReq.

        命令类型： * UPDATE_VIDEO: 更新视频 * UPLOAD_VIDEO：上传视频 * CONFIRM_ACTION_VIDEO: 确认动作编排视频 * GET_ACTION_VIDEO_MULTIPART: 获取动作编排视频分片

        :param command_message: The command_message of this Update2dModelTrainingJobReq.
        :type command_message: str
        """
        self._command_message = command_message

    @property
    def video_multipart_count(self):
        r"""Gets the video_multipart_count of this Update2dModelTrainingJobReq.

        训练视频上传分片数（上传时对唯一训练视频文件的数据分片，用于对该文件的并发上传，不是分多个视频文件上传）。

        :return: The video_multipart_count of this Update2dModelTrainingJobReq.
        :rtype: int
        """
        return self._video_multipart_count

    @video_multipart_count.setter
    def video_multipart_count(self, video_multipart_count):
        r"""Sets the video_multipart_count of this Update2dModelTrainingJobReq.

        训练视频上传分片数（上传时对唯一训练视频文件的数据分片，用于对该文件的并发上传，不是分多个视频文件上传）。

        :param video_multipart_count: The video_multipart_count of this Update2dModelTrainingJobReq.
        :type video_multipart_count: int
        """
        self._video_multipart_count = video_multipart_count

    @property
    def action_video_multipart_count(self):
        r"""Gets the action_video_multipart_count of this Update2dModelTrainingJobReq.

        动作视频上传分片数。

        :return: The action_video_multipart_count of this Update2dModelTrainingJobReq.
        :rtype: int
        """
        return self._action_video_multipart_count

    @action_video_multipart_count.setter
    def action_video_multipart_count(self, action_video_multipart_count):
        r"""Sets the action_video_multipart_count of this Update2dModelTrainingJobReq.

        动作视频上传分片数。

        :param action_video_multipart_count: The action_video_multipart_count of this Update2dModelTrainingJobReq.
        :type action_video_multipart_count: int
        """
        self._action_video_multipart_count = action_video_multipart_count

    @property
    def is_background_replacement(self):
        r"""Gets the is_background_replacement of this Update2dModelTrainingJobReq.

        分身数字人是否需要背景替换。需要背景替换的分身数字人训练视频需要绿幕拍摄。

        :return: The is_background_replacement of this Update2dModelTrainingJobReq.
        :rtype: bool
        """
        return self._is_background_replacement

    @is_background_replacement.setter
    def is_background_replacement(self, is_background_replacement):
        r"""Sets the is_background_replacement of this Update2dModelTrainingJobReq.

        分身数字人是否需要背景替换。需要背景替换的分身数字人训练视频需要绿幕拍摄。

        :param is_background_replacement: The is_background_replacement of this Update2dModelTrainingJobReq.
        :type is_background_replacement: bool
        """
        self._is_background_replacement = is_background_replacement

    @property
    def batch_name(self):
        r"""Gets the batch_name of this Update2dModelTrainingJobReq.

        分身数字人训练任务的批次名称。

        :return: The batch_name of this Update2dModelTrainingJobReq.
        :rtype: str
        """
        return self._batch_name

    @batch_name.setter
    def batch_name(self, batch_name):
        r"""Sets the batch_name of this Update2dModelTrainingJobReq.

        分身数字人训练任务的批次名称。

        :param batch_name: The batch_name of this Update2dModelTrainingJobReq.
        :type batch_name: str
        """
        self._batch_name = batch_name

    @property
    def tags(self):
        r"""Gets the tags of this Update2dModelTrainingJobReq.

        分身数字人训练任务标签。

        :return: The tags of this Update2dModelTrainingJobReq.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this Update2dModelTrainingJobReq.

        分身数字人训练任务标签。

        :param tags: The tags of this Update2dModelTrainingJobReq.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def samples_basic_info(self):
        r"""Gets the samples_basic_info of this Update2dModelTrainingJobReq.

        动作视频样例可修改信息。

        :return: The samples_basic_info of this Update2dModelTrainingJobReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ActionBasicSampleInfo`]
        """
        return self._samples_basic_info

    @samples_basic_info.setter
    def samples_basic_info(self, samples_basic_info):
        r"""Sets the samples_basic_info of this Update2dModelTrainingJobReq.

        动作视频样例可修改信息。

        :param samples_basic_info: The samples_basic_info of this Update2dModelTrainingJobReq.
        :type samples_basic_info: list[:class:`huaweicloudsdkmetastudio.v1.ActionBasicSampleInfo`]
        """
        self._samples_basic_info = samples_basic_info

    @property
    def supported_service(self):
        r"""Gets the supported_service of this Update2dModelTrainingJobReq.

        该任务所生成的模型支持的业务类型，可多选。  Flexus版数字人仅支持选择“VIDEO_2D”。

        :return: The supported_service of this Update2dModelTrainingJobReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.SupportedServiceEnum`]
        """
        return self._supported_service

    @supported_service.setter
    def supported_service(self, supported_service):
        r"""Sets the supported_service of this Update2dModelTrainingJobReq.

        该任务所生成的模型支持的业务类型，可多选。  Flexus版数字人仅支持选择“VIDEO_2D”。

        :param supported_service: The supported_service of this Update2dModelTrainingJobReq.
        :type supported_service: list[:class:`huaweicloudsdkmetastudio.v1.SupportedServiceEnum`]
        """
        self._supported_service = supported_service

    @property
    def audio_source_type(self):
        r"""Gets the audio_source_type of this Update2dModelTrainingJobReq.

        声音来源类型 * VIDEO：视频中抽取音频 * AUDIO：单独上传的音频

        :return: The audio_source_type of this Update2dModelTrainingJobReq.
        :rtype: str
        """
        return self._audio_source_type

    @audio_source_type.setter
    def audio_source_type(self, audio_source_type):
        r"""Sets the audio_source_type of this Update2dModelTrainingJobReq.

        声音来源类型 * VIDEO：视频中抽取音频 * AUDIO：单独上传的音频

        :param audio_source_type: The audio_source_type of this Update2dModelTrainingJobReq.
        :type audio_source_type: str
        """
        self._audio_source_type = audio_source_type

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
        if not isinstance(other, Update2dModelTrainingJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
