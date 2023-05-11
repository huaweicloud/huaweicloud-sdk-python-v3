# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'video_name': 'str',
        'description': 'str',
        'category_id': 'int',
        'category_name': 'str',
        'create_time': 'str',
        'last_modified': 'str',
        'video_type': 'str',
        'tags': 'str',
        'meta_data': 'MetaData',
        'video_url': 'str',
        'sign_url': 'str',
        'cover_info_array': 'list[CoverInfo]',
        'subtitle_info': 'list[SubtitleInfo]',
        'source_path': 'FileAddr',
        'output_path': 'FileAddr'
    }

    attribute_map = {
        'title': 'title',
        'video_name': 'video_name',
        'description': 'description',
        'category_id': 'category_id',
        'category_name': 'category_name',
        'create_time': 'create_time',
        'last_modified': 'last_modified',
        'video_type': 'video_type',
        'tags': 'tags',
        'meta_data': 'meta_data',
        'video_url': 'video_url',
        'sign_url': 'sign_url',
        'cover_info_array': 'cover_info_array',
        'subtitle_info': 'subtitle_info',
        'source_path': 'source_path',
        'output_path': 'output_path'
    }

    def __init__(self, title=None, video_name=None, description=None, category_id=None, category_name=None, create_time=None, last_modified=None, video_type=None, tags=None, meta_data=None, video_url=None, sign_url=None, cover_info_array=None, subtitle_info=None, source_path=None, output_path=None):
        """BaseInfo

        The model defined in huaweicloud sdk

        :param title: 媒资标题。  长度不超过128个字节，UTF8编码。
        :type title: str
        :param video_name: 媒资文件名。
        :type video_name: str
        :param description: 媒资描述。  长度不超过1024个字节。
        :type description: str
        :param category_id: 媒资分类id。
        :type category_id: int
        :param category_name: 媒资分类名称。
        :type category_name: str
        :param create_time: 媒资创建时间。  格式为yyyymmddhhmmss。必须是与时区无关的UTC时间。
        :type create_time: str
        :param last_modified: 媒资最近修改时间。  格式为yyyymmddhhmmss。必须是与时区无关的UTC时间。
        :type last_modified: str
        :param video_type: 音视频文件类型。  取值如下： - 视频文件：MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG、3GP、ASF、MKV。 - 音频文件：MP3、OGG、WAV、WMA、APE、FLAC、AAC、AC3、MMF、AMR、M4A、M4R、WV、MP2。
        :type video_type: str
        :param tags: 媒资标签。  单个标签不超过16个字节，最多不超过16个标签。  多个用逗号分隔，UTF8编码。
        :type tags: str
        :param meta_data: 
        :type meta_data: :class:`huaweicloudsdkvod.v1.MetaData`
        :param video_url: 原始视频文件的访问地址。
        :type video_url: str
        :param sign_url: 原视频文件的OBS临时访问地址,仅媒资详情接口生效
        :type sign_url: str
        :param cover_info_array: 封面信息。
        :type cover_info_array: list[:class:`huaweicloudsdkvod.v1.CoverInfo`]
        :param subtitle_info: 字幕信息数组
        :type subtitle_info: list[:class:`huaweicloudsdkvod.v1.SubtitleInfo`]
        :param source_path: 
        :type source_path: :class:`huaweicloudsdkvod.v1.FileAddr`
        :param output_path: 
        :type output_path: :class:`huaweicloudsdkvod.v1.FileAddr`
        """
        
        

        self._title = None
        self._video_name = None
        self._description = None
        self._category_id = None
        self._category_name = None
        self._create_time = None
        self._last_modified = None
        self._video_type = None
        self._tags = None
        self._meta_data = None
        self._video_url = None
        self._sign_url = None
        self._cover_info_array = None
        self._subtitle_info = None
        self._source_path = None
        self._output_path = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if video_name is not None:
            self.video_name = video_name
        if description is not None:
            self.description = description
        if category_id is not None:
            self.category_id = category_id
        if category_name is not None:
            self.category_name = category_name
        if create_time is not None:
            self.create_time = create_time
        if last_modified is not None:
            self.last_modified = last_modified
        if video_type is not None:
            self.video_type = video_type
        if tags is not None:
            self.tags = tags
        if meta_data is not None:
            self.meta_data = meta_data
        if video_url is not None:
            self.video_url = video_url
        if sign_url is not None:
            self.sign_url = sign_url
        if cover_info_array is not None:
            self.cover_info_array = cover_info_array
        if subtitle_info is not None:
            self.subtitle_info = subtitle_info
        if source_path is not None:
            self.source_path = source_path
        if output_path is not None:
            self.output_path = output_path

    @property
    def title(self):
        """Gets the title of this BaseInfo.

        媒资标题。  长度不超过128个字节，UTF8编码。

        :return: The title of this BaseInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this BaseInfo.

        媒资标题。  长度不超过128个字节，UTF8编码。

        :param title: The title of this BaseInfo.
        :type title: str
        """
        self._title = title

    @property
    def video_name(self):
        """Gets the video_name of this BaseInfo.

        媒资文件名。

        :return: The video_name of this BaseInfo.
        :rtype: str
        """
        return self._video_name

    @video_name.setter
    def video_name(self, video_name):
        """Sets the video_name of this BaseInfo.

        媒资文件名。

        :param video_name: The video_name of this BaseInfo.
        :type video_name: str
        """
        self._video_name = video_name

    @property
    def description(self):
        """Gets the description of this BaseInfo.

        媒资描述。  长度不超过1024个字节。

        :return: The description of this BaseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BaseInfo.

        媒资描述。  长度不超过1024个字节。

        :param description: The description of this BaseInfo.
        :type description: str
        """
        self._description = description

    @property
    def category_id(self):
        """Gets the category_id of this BaseInfo.

        媒资分类id。

        :return: The category_id of this BaseInfo.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this BaseInfo.

        媒资分类id。

        :param category_id: The category_id of this BaseInfo.
        :type category_id: int
        """
        self._category_id = category_id

    @property
    def category_name(self):
        """Gets the category_name of this BaseInfo.

        媒资分类名称。

        :return: The category_name of this BaseInfo.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this BaseInfo.

        媒资分类名称。

        :param category_name: The category_name of this BaseInfo.
        :type category_name: str
        """
        self._category_name = category_name

    @property
    def create_time(self):
        """Gets the create_time of this BaseInfo.

        媒资创建时间。  格式为yyyymmddhhmmss。必须是与时区无关的UTC时间。

        :return: The create_time of this BaseInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this BaseInfo.

        媒资创建时间。  格式为yyyymmddhhmmss。必须是与时区无关的UTC时间。

        :param create_time: The create_time of this BaseInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_modified(self):
        """Gets the last_modified of this BaseInfo.

        媒资最近修改时间。  格式为yyyymmddhhmmss。必须是与时区无关的UTC时间。

        :return: The last_modified of this BaseInfo.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this BaseInfo.

        媒资最近修改时间。  格式为yyyymmddhhmmss。必须是与时区无关的UTC时间。

        :param last_modified: The last_modified of this BaseInfo.
        :type last_modified: str
        """
        self._last_modified = last_modified

    @property
    def video_type(self):
        """Gets the video_type of this BaseInfo.

        音视频文件类型。  取值如下： - 视频文件：MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG、3GP、ASF、MKV。 - 音频文件：MP3、OGG、WAV、WMA、APE、FLAC、AAC、AC3、MMF、AMR、M4A、M4R、WV、MP2。

        :return: The video_type of this BaseInfo.
        :rtype: str
        """
        return self._video_type

    @video_type.setter
    def video_type(self, video_type):
        """Sets the video_type of this BaseInfo.

        音视频文件类型。  取值如下： - 视频文件：MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG、3GP、ASF、MKV。 - 音频文件：MP3、OGG、WAV、WMA、APE、FLAC、AAC、AC3、MMF、AMR、M4A、M4R、WV、MP2。

        :param video_type: The video_type of this BaseInfo.
        :type video_type: str
        """
        self._video_type = video_type

    @property
    def tags(self):
        """Gets the tags of this BaseInfo.

        媒资标签。  单个标签不超过16个字节，最多不超过16个标签。  多个用逗号分隔，UTF8编码。

        :return: The tags of this BaseInfo.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BaseInfo.

        媒资标签。  单个标签不超过16个字节，最多不超过16个标签。  多个用逗号分隔，UTF8编码。

        :param tags: The tags of this BaseInfo.
        :type tags: str
        """
        self._tags = tags

    @property
    def meta_data(self):
        """Gets the meta_data of this BaseInfo.

        :return: The meta_data of this BaseInfo.
        :rtype: :class:`huaweicloudsdkvod.v1.MetaData`
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this BaseInfo.

        :param meta_data: The meta_data of this BaseInfo.
        :type meta_data: :class:`huaweicloudsdkvod.v1.MetaData`
        """
        self._meta_data = meta_data

    @property
    def video_url(self):
        """Gets the video_url of this BaseInfo.

        原始视频文件的访问地址。

        :return: The video_url of this BaseInfo.
        :rtype: str
        """
        return self._video_url

    @video_url.setter
    def video_url(self, video_url):
        """Sets the video_url of this BaseInfo.

        原始视频文件的访问地址。

        :param video_url: The video_url of this BaseInfo.
        :type video_url: str
        """
        self._video_url = video_url

    @property
    def sign_url(self):
        """Gets the sign_url of this BaseInfo.

        原视频文件的OBS临时访问地址,仅媒资详情接口生效

        :return: The sign_url of this BaseInfo.
        :rtype: str
        """
        return self._sign_url

    @sign_url.setter
    def sign_url(self, sign_url):
        """Sets the sign_url of this BaseInfo.

        原视频文件的OBS临时访问地址,仅媒资详情接口生效

        :param sign_url: The sign_url of this BaseInfo.
        :type sign_url: str
        """
        self._sign_url = sign_url

    @property
    def cover_info_array(self):
        """Gets the cover_info_array of this BaseInfo.

        封面信息。

        :return: The cover_info_array of this BaseInfo.
        :rtype: list[:class:`huaweicloudsdkvod.v1.CoverInfo`]
        """
        return self._cover_info_array

    @cover_info_array.setter
    def cover_info_array(self, cover_info_array):
        """Sets the cover_info_array of this BaseInfo.

        封面信息。

        :param cover_info_array: The cover_info_array of this BaseInfo.
        :type cover_info_array: list[:class:`huaweicloudsdkvod.v1.CoverInfo`]
        """
        self._cover_info_array = cover_info_array

    @property
    def subtitle_info(self):
        """Gets the subtitle_info of this BaseInfo.

        字幕信息数组

        :return: The subtitle_info of this BaseInfo.
        :rtype: list[:class:`huaweicloudsdkvod.v1.SubtitleInfo`]
        """
        return self._subtitle_info

    @subtitle_info.setter
    def subtitle_info(self, subtitle_info):
        """Sets the subtitle_info of this BaseInfo.

        字幕信息数组

        :param subtitle_info: The subtitle_info of this BaseInfo.
        :type subtitle_info: list[:class:`huaweicloudsdkvod.v1.SubtitleInfo`]
        """
        self._subtitle_info = subtitle_info

    @property
    def source_path(self):
        """Gets the source_path of this BaseInfo.

        :return: The source_path of this BaseInfo.
        :rtype: :class:`huaweicloudsdkvod.v1.FileAddr`
        """
        return self._source_path

    @source_path.setter
    def source_path(self, source_path):
        """Sets the source_path of this BaseInfo.

        :param source_path: The source_path of this BaseInfo.
        :type source_path: :class:`huaweicloudsdkvod.v1.FileAddr`
        """
        self._source_path = source_path

    @property
    def output_path(self):
        """Gets the output_path of this BaseInfo.

        :return: The output_path of this BaseInfo.
        :rtype: :class:`huaweicloudsdkvod.v1.FileAddr`
        """
        return self._output_path

    @output_path.setter
    def output_path(self, output_path):
        """Sets the output_path of this BaseInfo.

        :param output_path: The output_path of this BaseInfo.
        :type output_path: :class:`huaweicloudsdkvod.v1.FileAddr`
        """
        self._output_path = output_path

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
        if not isinstance(other, BaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
