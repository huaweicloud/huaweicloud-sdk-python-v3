# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatasetFileFormat:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'format': 'str',
        'content_types': 'list[str]'
    }

    attribute_map = {
        'format': 'format',
        'content_types': 'content_types'
    }

    def __init__(self, format=None, content_types=None):
        r"""DatasetFileFormat

        The model defined in huaweicloud sdk

        :param format: 文件格式： ROW-行存储文件, TEXT-无格式文本文件, IMAGE-图片文件, AUDIO-音频文件, VIDEO-视频文件, CUSTOM-其他文件
        :type format: str
        :param content_types: 文件内容类型。行存文件格式,format为ROW时设置,可选值: CSV-Comma Separated Values文件,JSONL-Json对象行文件,AVRO-AVRO行存文件 图片文件格式，format为IMAGE时设置,可选值: JPG-JPG图片,PNG-PNG图片,TIFF-TIFF图片 音频文件格式，format为AUDIO时设置,可选值: WAV-WAV音频,MP3-MP3音频,FLAC-FLAC音频 视频文件格式，format为VIDEO时设置,可选值: MP4-MP4视频,MOV-MOV视频,AVI-AVI视频
        :type content_types: list[str]
        """
        
        

        self._format = None
        self._content_types = None
        self.discriminator = None

        self.format = format
        self.content_types = content_types

    @property
    def format(self):
        r"""Gets the format of this DatasetFileFormat.

        文件格式： ROW-行存储文件, TEXT-无格式文本文件, IMAGE-图片文件, AUDIO-音频文件, VIDEO-视频文件, CUSTOM-其他文件

        :return: The format of this DatasetFileFormat.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this DatasetFileFormat.

        文件格式： ROW-行存储文件, TEXT-无格式文本文件, IMAGE-图片文件, AUDIO-音频文件, VIDEO-视频文件, CUSTOM-其他文件

        :param format: The format of this DatasetFileFormat.
        :type format: str
        """
        self._format = format

    @property
    def content_types(self):
        r"""Gets the content_types of this DatasetFileFormat.

        文件内容类型。行存文件格式,format为ROW时设置,可选值: CSV-Comma Separated Values文件,JSONL-Json对象行文件,AVRO-AVRO行存文件 图片文件格式，format为IMAGE时设置,可选值: JPG-JPG图片,PNG-PNG图片,TIFF-TIFF图片 音频文件格式，format为AUDIO时设置,可选值: WAV-WAV音频,MP3-MP3音频,FLAC-FLAC音频 视频文件格式，format为VIDEO时设置,可选值: MP4-MP4视频,MOV-MOV视频,AVI-AVI视频

        :return: The content_types of this DatasetFileFormat.
        :rtype: list[str]
        """
        return self._content_types

    @content_types.setter
    def content_types(self, content_types):
        r"""Sets the content_types of this DatasetFileFormat.

        文件内容类型。行存文件格式,format为ROW时设置,可选值: CSV-Comma Separated Values文件,JSONL-Json对象行文件,AVRO-AVRO行存文件 图片文件格式，format为IMAGE时设置,可选值: JPG-JPG图片,PNG-PNG图片,TIFF-TIFF图片 音频文件格式，format为AUDIO时设置,可选值: WAV-WAV音频,MP3-MP3音频,FLAC-FLAC音频 视频文件格式，format为VIDEO时设置,可选值: MP4-MP4视频,MOV-MOV视频,AVI-AVI视频

        :param content_types: The content_types of this DatasetFileFormat.
        :type content_types: list[str]
        """
        self._content_types = content_types

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DatasetFileFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
