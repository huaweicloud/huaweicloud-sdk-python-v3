# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReadConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_read_configs': 'list[ImageReadConfig]',
        'read_type': 'int',
        'read_content': 'str',
        'character_position': 'int',
        'read_content_paragraph_interval': 'int',
        'image_frame_id': 'str',
        'audio_url': 'str'
    }

    attribute_map = {
        'image_read_configs': 'image_read_configs',
        'read_type': 'read_type',
        'read_content': 'read_content',
        'character_position': 'character_position',
        'read_content_paragraph_interval': 'read_content_paragraph_interval',
        'image_frame_id': 'image_frame_id',
        'audio_url': 'audio_url'
    }

    def __init__(self, image_read_configs=None, read_type=None, read_content=None, character_position=None, read_content_paragraph_interval=None, image_frame_id=None, audio_url=None):
        """ReadConfig

        The model defined in huaweicloud sdk

        :param image_read_configs: 插图播报配置
        :type image_read_configs: list[:class:`huaweicloudsdkcbs.v1.ImageReadConfig`]
        :param read_type: 播报选项： 0：纯文本播报（使用read_content 字段） 1：插图播报（使用image_read_configs字段） 3：自定义音频播报（使用audio字段） 会根据选项进行具体的字段校验
        :type read_type: int
        :param read_content: 纯文本播报内容
        :type read_content: str
        :param character_position: 0：左 1：中 2：右 默认：1
        :type character_position: int
        :param read_content_paragraph_interval: 段落播报间隔 单位：ms 范围：0~5000 默认：400
        :type read_content_paragraph_interval: int
        :param image_frame_id: 播报框id
        :type image_frame_id: str
        :param audio_url: 用户的音频文件obs地址，为https格式（如：https://cbs-digital-human-cn-north-4.obs.myhuaweicloud.com:443/audio.wav），当字段不为空时，表示将使用用户自己的音频文件。  不支持PPT和图片播报，不支持字幕。音频格式文件格式为wav 音频最长支持20分钟，支持100m大小 注意：该功能的使用需要用户启动OBS授权
        :type audio_url: str
        """
        
        

        self._image_read_configs = None
        self._read_type = None
        self._read_content = None
        self._character_position = None
        self._read_content_paragraph_interval = None
        self._image_frame_id = None
        self._audio_url = None
        self.discriminator = None

        if image_read_configs is not None:
            self.image_read_configs = image_read_configs
        self.read_type = read_type
        if read_content is not None:
            self.read_content = read_content
        if character_position is not None:
            self.character_position = character_position
        if read_content_paragraph_interval is not None:
            self.read_content_paragraph_interval = read_content_paragraph_interval
        if image_frame_id is not None:
            self.image_frame_id = image_frame_id
        if audio_url is not None:
            self.audio_url = audio_url

    @property
    def image_read_configs(self):
        """Gets the image_read_configs of this ReadConfig.

        插图播报配置

        :return: The image_read_configs of this ReadConfig.
        :rtype: list[:class:`huaweicloudsdkcbs.v1.ImageReadConfig`]
        """
        return self._image_read_configs

    @image_read_configs.setter
    def image_read_configs(self, image_read_configs):
        """Sets the image_read_configs of this ReadConfig.

        插图播报配置

        :param image_read_configs: The image_read_configs of this ReadConfig.
        :type image_read_configs: list[:class:`huaweicloudsdkcbs.v1.ImageReadConfig`]
        """
        self._image_read_configs = image_read_configs

    @property
    def read_type(self):
        """Gets the read_type of this ReadConfig.

        播报选项： 0：纯文本播报（使用read_content 字段） 1：插图播报（使用image_read_configs字段） 3：自定义音频播报（使用audio字段） 会根据选项进行具体的字段校验

        :return: The read_type of this ReadConfig.
        :rtype: int
        """
        return self._read_type

    @read_type.setter
    def read_type(self, read_type):
        """Sets the read_type of this ReadConfig.

        播报选项： 0：纯文本播报（使用read_content 字段） 1：插图播报（使用image_read_configs字段） 3：自定义音频播报（使用audio字段） 会根据选项进行具体的字段校验

        :param read_type: The read_type of this ReadConfig.
        :type read_type: int
        """
        self._read_type = read_type

    @property
    def read_content(self):
        """Gets the read_content of this ReadConfig.

        纯文本播报内容

        :return: The read_content of this ReadConfig.
        :rtype: str
        """
        return self._read_content

    @read_content.setter
    def read_content(self, read_content):
        """Sets the read_content of this ReadConfig.

        纯文本播报内容

        :param read_content: The read_content of this ReadConfig.
        :type read_content: str
        """
        self._read_content = read_content

    @property
    def character_position(self):
        """Gets the character_position of this ReadConfig.

        0：左 1：中 2：右 默认：1

        :return: The character_position of this ReadConfig.
        :rtype: int
        """
        return self._character_position

    @character_position.setter
    def character_position(self, character_position):
        """Sets the character_position of this ReadConfig.

        0：左 1：中 2：右 默认：1

        :param character_position: The character_position of this ReadConfig.
        :type character_position: int
        """
        self._character_position = character_position

    @property
    def read_content_paragraph_interval(self):
        """Gets the read_content_paragraph_interval of this ReadConfig.

        段落播报间隔 单位：ms 范围：0~5000 默认：400

        :return: The read_content_paragraph_interval of this ReadConfig.
        :rtype: int
        """
        return self._read_content_paragraph_interval

    @read_content_paragraph_interval.setter
    def read_content_paragraph_interval(self, read_content_paragraph_interval):
        """Sets the read_content_paragraph_interval of this ReadConfig.

        段落播报间隔 单位：ms 范围：0~5000 默认：400

        :param read_content_paragraph_interval: The read_content_paragraph_interval of this ReadConfig.
        :type read_content_paragraph_interval: int
        """
        self._read_content_paragraph_interval = read_content_paragraph_interval

    @property
    def image_frame_id(self):
        """Gets the image_frame_id of this ReadConfig.

        播报框id

        :return: The image_frame_id of this ReadConfig.
        :rtype: str
        """
        return self._image_frame_id

    @image_frame_id.setter
    def image_frame_id(self, image_frame_id):
        """Sets the image_frame_id of this ReadConfig.

        播报框id

        :param image_frame_id: The image_frame_id of this ReadConfig.
        :type image_frame_id: str
        """
        self._image_frame_id = image_frame_id

    @property
    def audio_url(self):
        """Gets the audio_url of this ReadConfig.

        用户的音频文件obs地址，为https格式（如：https://cbs-digital-human-cn-north-4.obs.myhuaweicloud.com:443/audio.wav），当字段不为空时，表示将使用用户自己的音频文件。  不支持PPT和图片播报，不支持字幕。音频格式文件格式为wav 音频最长支持20分钟，支持100m大小 注意：该功能的使用需要用户启动OBS授权

        :return: The audio_url of this ReadConfig.
        :rtype: str
        """
        return self._audio_url

    @audio_url.setter
    def audio_url(self, audio_url):
        """Sets the audio_url of this ReadConfig.

        用户的音频文件obs地址，为https格式（如：https://cbs-digital-human-cn-north-4.obs.myhuaweicloud.com:443/audio.wav），当字段不为空时，表示将使用用户自己的音频文件。  不支持PPT和图片播报，不支持字幕。音频格式文件格式为wav 音频最长支持20分钟，支持100m大小 注意：该功能的使用需要用户启动OBS授权

        :param audio_url: The audio_url of this ReadConfig.
        :type audio_url: str
        """
        self._audio_url = audio_url

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
        if not isinstance(other, ReadConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
