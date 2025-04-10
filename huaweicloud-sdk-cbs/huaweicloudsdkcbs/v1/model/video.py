# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Video:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'update_time': 'str',
        'error_msg': 'str',
        'id': 'str',
        'name': 'str',
        'progress': 'int',
        'status': 'int',
        'subtitle_url': 'str',
        'video_url': 'str',
        'video_shot': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'update_time': 'update_time',
        'error_msg': 'error_msg',
        'id': 'id',
        'name': 'name',
        'progress': 'progress',
        'status': 'status',
        'subtitle_url': 'subtitle_url',
        'video_url': 'video_url',
        'video_shot': 'video_shot'
    }

    def __init__(self, create_time=None, update_time=None, error_msg=None, id=None, name=None, progress=None, status=None, subtitle_url=None, video_url=None, video_shot=None):
        r"""Video

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param error_msg: 错误信息 如: {\\\&quot;error_code\\\&quot;:\\\&quot;0001\\\&quot;,\\\&quot;error_msg\\\&quot;:\\\&quot;播报内容超过10分钟，请重新调整播报内容。\\\&quot;}
        :type error_msg: str
        :param id: 
        :type id: str
        :param name: 视频名称
        :type name: str
        :param progress: 视频生成进度 0~100
        :type progress: int
        :param status: 0：未初始化 1：生成中 2：生成成功 3：生成失败
        :type status: int
        :param subtitle_url: 字幕地址
        :type subtitle_url: str
        :param video_url: 视频的obs地址，当视频生成成功时返回
        :type video_url: str
        :param video_shot: 视频截图地址，jpg格式 分辨率480 * 270 当status&#x3D;2：生成成功时返回
        :type video_shot: str
        """
        
        

        self._create_time = None
        self._update_time = None
        self._error_msg = None
        self._id = None
        self._name = None
        self._progress = None
        self._status = None
        self._subtitle_url = None
        self._video_url = None
        self._video_shot = None
        self.discriminator = None

        self.create_time = create_time
        self.update_time = update_time
        if error_msg is not None:
            self.error_msg = error_msg
        self.id = id
        self.name = name
        if progress is not None:
            self.progress = progress
        self.status = status
        self.subtitle_url = subtitle_url
        if video_url is not None:
            self.video_url = video_url
        if video_shot is not None:
            self.video_shot = video_shot

    @property
    def create_time(self):
        r"""Gets the create_time of this Video.

        创建时间

        :return: The create_time of this Video.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Video.

        创建时间

        :param create_time: The create_time of this Video.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this Video.

        更新时间

        :return: The update_time of this Video.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this Video.

        更新时间

        :param update_time: The update_time of this Video.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def error_msg(self):
        r"""Gets the error_msg of this Video.

        错误信息 如: {\\\"error_code\\\":\\\"0001\\\",\\\"error_msg\\\":\\\"播报内容超过10分钟，请重新调整播报内容。\\\"}

        :return: The error_msg of this Video.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this Video.

        错误信息 如: {\\\"error_code\\\":\\\"0001\\\",\\\"error_msg\\\":\\\"播报内容超过10分钟，请重新调整播报内容。\\\"}

        :param error_msg: The error_msg of this Video.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def id(self):
        r"""Gets the id of this Video.

        

        :return: The id of this Video.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Video.

        

        :param id: The id of this Video.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Video.

        视频名称

        :return: The name of this Video.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Video.

        视频名称

        :param name: The name of this Video.
        :type name: str
        """
        self._name = name

    @property
    def progress(self):
        r"""Gets the progress of this Video.

        视频生成进度 0~100

        :return: The progress of this Video.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this Video.

        视频生成进度 0~100

        :param progress: The progress of this Video.
        :type progress: int
        """
        self._progress = progress

    @property
    def status(self):
        r"""Gets the status of this Video.

        0：未初始化 1：生成中 2：生成成功 3：生成失败

        :return: The status of this Video.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Video.

        0：未初始化 1：生成中 2：生成成功 3：生成失败

        :param status: The status of this Video.
        :type status: int
        """
        self._status = status

    @property
    def subtitle_url(self):
        r"""Gets the subtitle_url of this Video.

        字幕地址

        :return: The subtitle_url of this Video.
        :rtype: str
        """
        return self._subtitle_url

    @subtitle_url.setter
    def subtitle_url(self, subtitle_url):
        r"""Sets the subtitle_url of this Video.

        字幕地址

        :param subtitle_url: The subtitle_url of this Video.
        :type subtitle_url: str
        """
        self._subtitle_url = subtitle_url

    @property
    def video_url(self):
        r"""Gets the video_url of this Video.

        视频的obs地址，当视频生成成功时返回

        :return: The video_url of this Video.
        :rtype: str
        """
        return self._video_url

    @video_url.setter
    def video_url(self, video_url):
        r"""Sets the video_url of this Video.

        视频的obs地址，当视频生成成功时返回

        :param video_url: The video_url of this Video.
        :type video_url: str
        """
        self._video_url = video_url

    @property
    def video_shot(self):
        r"""Gets the video_shot of this Video.

        视频截图地址，jpg格式 分辨率480 * 270 当status=2：生成成功时返回

        :return: The video_shot of this Video.
        :rtype: str
        """
        return self._video_shot

    @video_shot.setter
    def video_shot(self, video_shot):
        r"""Sets the video_shot of this Video.

        视频截图地址，jpg格式 分辨率480 * 270 当status=2：生成成功时返回

        :param video_shot: The video_shot of this Video.
        :type video_shot: str
        """
        self._video_shot = video_shot

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
        if not isinstance(other, Video):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
