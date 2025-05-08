# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdditionalObjectProcessReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'output': 'ObsInfo',
        'transcode_task': 'list[ObjectTranscodeTask]',
        'watermarks': 'list[WatermarkRequest]',
        'thumbnail_task': 'list[ObjectThumbnailTask]',
        'image_sprite_task': 'list[ObjectImageSpriteTask]',
        'video_process': 'VideoProcess',
        'callback_url': 'str',
        'session_context': 'str'
    }

    attribute_map = {
        'output': 'output',
        'transcode_task': 'transcode_task',
        'watermarks': 'watermarks',
        'thumbnail_task': 'thumbnail_task',
        'image_sprite_task': 'image_sprite_task',
        'video_process': 'video_process',
        'callback_url': 'callback_url',
        'session_context': 'session_context'
    }

    def __init__(self, output=None, transcode_task=None, watermarks=None, thumbnail_task=None, image_sprite_task=None, video_process=None, callback_url=None, session_context=None):
        r"""AdditionalObjectProcessReq

        The model defined in huaweicloud sdk

        :param output: 
        :type output: :class:`huaweicloudsdkvod.v1.ObsInfo`
        :param transcode_task: 转码任务列表 
        :type transcode_task: list[:class:`huaweicloudsdkvod.v1.ObjectTranscodeTask`]
        :param watermarks: 水印设置 
        :type watermarks: list[:class:`huaweicloudsdkvod.v1.WatermarkRequest`]
        :param thumbnail_task: 转码任务列表 
        :type thumbnail_task: list[:class:`huaweicloudsdkvod.v1.ObjectThumbnailTask`]
        :param image_sprite_task: 转码任务列表 
        :type image_sprite_task: list[:class:`huaweicloudsdkvod.v1.ObjectImageSpriteTask`]
        :param video_process: 
        :type video_process: :class:`huaweicloudsdkvod.v1.VideoProcess`
        :param callback_url: 回调url 
        :type callback_url: str
        :param session_context: 自定义上下文，回调时会回调给用户，透传信息
        :type session_context: str
        """
        
        

        self._output = None
        self._transcode_task = None
        self._watermarks = None
        self._thumbnail_task = None
        self._image_sprite_task = None
        self._video_process = None
        self._callback_url = None
        self._session_context = None
        self.discriminator = None

        self.output = output
        if transcode_task is not None:
            self.transcode_task = transcode_task
        if watermarks is not None:
            self.watermarks = watermarks
        if thumbnail_task is not None:
            self.thumbnail_task = thumbnail_task
        if image_sprite_task is not None:
            self.image_sprite_task = image_sprite_task
        if video_process is not None:
            self.video_process = video_process
        if callback_url is not None:
            self.callback_url = callback_url
        if session_context is not None:
            self.session_context = session_context

    @property
    def output(self):
        r"""Gets the output of this AdditionalObjectProcessReq.

        :return: The output of this AdditionalObjectProcessReq.
        :rtype: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this AdditionalObjectProcessReq.

        :param output: The output of this AdditionalObjectProcessReq.
        :type output: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        self._output = output

    @property
    def transcode_task(self):
        r"""Gets the transcode_task of this AdditionalObjectProcessReq.

        转码任务列表 

        :return: The transcode_task of this AdditionalObjectProcessReq.
        :rtype: list[:class:`huaweicloudsdkvod.v1.ObjectTranscodeTask`]
        """
        return self._transcode_task

    @transcode_task.setter
    def transcode_task(self, transcode_task):
        r"""Sets the transcode_task of this AdditionalObjectProcessReq.

        转码任务列表 

        :param transcode_task: The transcode_task of this AdditionalObjectProcessReq.
        :type transcode_task: list[:class:`huaweicloudsdkvod.v1.ObjectTranscodeTask`]
        """
        self._transcode_task = transcode_task

    @property
    def watermarks(self):
        r"""Gets the watermarks of this AdditionalObjectProcessReq.

        水印设置 

        :return: The watermarks of this AdditionalObjectProcessReq.
        :rtype: list[:class:`huaweicloudsdkvod.v1.WatermarkRequest`]
        """
        return self._watermarks

    @watermarks.setter
    def watermarks(self, watermarks):
        r"""Sets the watermarks of this AdditionalObjectProcessReq.

        水印设置 

        :param watermarks: The watermarks of this AdditionalObjectProcessReq.
        :type watermarks: list[:class:`huaweicloudsdkvod.v1.WatermarkRequest`]
        """
        self._watermarks = watermarks

    @property
    def thumbnail_task(self):
        r"""Gets the thumbnail_task of this AdditionalObjectProcessReq.

        转码任务列表 

        :return: The thumbnail_task of this AdditionalObjectProcessReq.
        :rtype: list[:class:`huaweicloudsdkvod.v1.ObjectThumbnailTask`]
        """
        return self._thumbnail_task

    @thumbnail_task.setter
    def thumbnail_task(self, thumbnail_task):
        r"""Sets the thumbnail_task of this AdditionalObjectProcessReq.

        转码任务列表 

        :param thumbnail_task: The thumbnail_task of this AdditionalObjectProcessReq.
        :type thumbnail_task: list[:class:`huaweicloudsdkvod.v1.ObjectThumbnailTask`]
        """
        self._thumbnail_task = thumbnail_task

    @property
    def image_sprite_task(self):
        r"""Gets the image_sprite_task of this AdditionalObjectProcessReq.

        转码任务列表 

        :return: The image_sprite_task of this AdditionalObjectProcessReq.
        :rtype: list[:class:`huaweicloudsdkvod.v1.ObjectImageSpriteTask`]
        """
        return self._image_sprite_task

    @image_sprite_task.setter
    def image_sprite_task(self, image_sprite_task):
        r"""Sets the image_sprite_task of this AdditionalObjectProcessReq.

        转码任务列表 

        :param image_sprite_task: The image_sprite_task of this AdditionalObjectProcessReq.
        :type image_sprite_task: list[:class:`huaweicloudsdkvod.v1.ObjectImageSpriteTask`]
        """
        self._image_sprite_task = image_sprite_task

    @property
    def video_process(self):
        r"""Gets the video_process of this AdditionalObjectProcessReq.

        :return: The video_process of this AdditionalObjectProcessReq.
        :rtype: :class:`huaweicloudsdkvod.v1.VideoProcess`
        """
        return self._video_process

    @video_process.setter
    def video_process(self, video_process):
        r"""Sets the video_process of this AdditionalObjectProcessReq.

        :param video_process: The video_process of this AdditionalObjectProcessReq.
        :type video_process: :class:`huaweicloudsdkvod.v1.VideoProcess`
        """
        self._video_process = video_process

    @property
    def callback_url(self):
        r"""Gets the callback_url of this AdditionalObjectProcessReq.

        回调url 

        :return: The callback_url of this AdditionalObjectProcessReq.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        r"""Sets the callback_url of this AdditionalObjectProcessReq.

        回调url 

        :param callback_url: The callback_url of this AdditionalObjectProcessReq.
        :type callback_url: str
        """
        self._callback_url = callback_url

    @property
    def session_context(self):
        r"""Gets the session_context of this AdditionalObjectProcessReq.

        自定义上下文，回调时会回调给用户，透传信息

        :return: The session_context of this AdditionalObjectProcessReq.
        :rtype: str
        """
        return self._session_context

    @session_context.setter
    def session_context(self, session_context):
        r"""Sets the session_context of this AdditionalObjectProcessReq.

        自定义上下文，回调时会回调给用户，透传信息

        :param session_context: The session_context of this AdditionalObjectProcessReq.
        :type session_context: str
        """
        self._session_context = session_context

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
        if not isinstance(other, AdditionalObjectProcessReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
