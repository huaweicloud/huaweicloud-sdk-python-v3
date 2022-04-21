# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'title': 'str',
        'description': 'str',
        'duration': 'int',
        'size': 'int',
        'original_url': 'str',
        'category': 'str',
        'covers': 'list[CoverInfo]',
        'create_time': 'str',
        'asset_status': 'str',
        'transcode_status': 'str',
        'thumbnail_status': 'str',
        'review_status': 'str',
        'exec_desc': 'str',
        'media_type': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'title': 'title',
        'description': 'description',
        'duration': 'duration',
        'size': 'size',
        'original_url': 'original_url',
        'category': 'category',
        'covers': 'covers',
        'create_time': 'create_time',
        'asset_status': 'asset_status',
        'transcode_status': 'transcode_status',
        'thumbnail_status': 'thumbnail_status',
        'review_status': 'review_status',
        'exec_desc': 'exec_desc',
        'media_type': 'media_type'
    }

    def __init__(self, asset_id=None, title=None, description=None, duration=None, size=None, original_url=None, category=None, covers=None, create_time=None, asset_status=None, transcode_status=None, thumbnail_status=None, review_status=None, exec_desc=None, media_type=None):
        """AssetSummary

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID。
        :type asset_id: str
        :param title: 媒资标题。长度不超过128个字节，UTF-8编码。
        :type title: str
        :param description: 媒资描述。长度不超过1024个字节。
        :type description: str
        :param duration: 媒资时长。  单位：秒。
        :type duration: int
        :param size: 媒资大小。  单位：字节。
        :type size: int
        :param original_url: 原始播放url。
        :type original_url: str
        :param category: 媒资分类名称。
        :type category: str
        :param covers: 封面信息。
        :type covers: list[:class:`huaweicloudsdkvod.v1.CoverInfo`]
        :param create_time: 媒资创建时间。  格式为yyyymmddhhmmss。必须是与时区无关的UTC时间。
        :type create_time: str
        :param asset_status: 媒资状态。  取值如下： - CREATING：上传中。 - FAILED：上传失败。 - CREATED：上传成功。 - PUBLISHED：已发布。 - DELETED：已删除。
        :type asset_status: str
        :param transcode_status: 转码状态。  取值如下： - UN_TRANSCODE：未转码。 - WAITING_TRANSCODE：待转码 - TRANSCODING：转码中。 - TRANSCODE_SUCCEED：转码成功。 - TRANSCODE_FAILED：转码失败。
        :type transcode_status: str
        :param thumbnail_status: 截图状态。  取值如下： - UN_THUMBNAIL：未截图。 - THUMBNAILING：截图中。 - THUMBNAIL_SUCCEED：截图成功。 - THUMBNAIL_FAILED：截图失败。
        :type thumbnail_status: str
        :param review_status: 内容审核状态  取值如下： - UN_REVIEW：未审核。 - REVIEWING：审核中。 - REVIEW_SUSPICIOUS：审核可疑，需要人工复审。 - REVIEW_PASSED：审核通过。 - REVIEW_FAILED：审核失败。 - REVIEW_BLOCKED：已屏蔽。
        :type review_status: str
        :param exec_desc: 媒资的任务执行描述汇总。  示例： - asset_exec_desc: upload success，媒资任务执行描述信息。 - transcode_exec_desc: transcode success，转码任务执行描述信息。 - thumbnail_exec_desc: thumbnail failed，截图任务执行描述信息。 - review_exec_desc: review pass，审核任务执行描述信息。
        :type exec_desc: str
        :param media_type: 音视频文件的格式。  取值如下： - 视频文件格式：MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG - 音频文件格式：MP3、OGG、WAV、WMA、APE、FLAC、AAC、AC3、MMF、AMR、M4A、M4R、WV、MP2
        :type media_type: str
        """
        
        

        self._asset_id = None
        self._title = None
        self._description = None
        self._duration = None
        self._size = None
        self._original_url = None
        self._category = None
        self._covers = None
        self._create_time = None
        self._asset_status = None
        self._transcode_status = None
        self._thumbnail_status = None
        self._review_status = None
        self._exec_desc = None
        self._media_type = None
        self.discriminator = None

        self.asset_id = asset_id
        self.title = title
        if description is not None:
            self.description = description
        self.duration = duration
        self.size = size
        if original_url is not None:
            self.original_url = original_url
        if category is not None:
            self.category = category
        if covers is not None:
            self.covers = covers
        if create_time is not None:
            self.create_time = create_time
        self.asset_status = asset_status
        if transcode_status is not None:
            self.transcode_status = transcode_status
        if thumbnail_status is not None:
            self.thumbnail_status = thumbnail_status
        if review_status is not None:
            self.review_status = review_status
        if exec_desc is not None:
            self.exec_desc = exec_desc
        if media_type is not None:
            self.media_type = media_type

    @property
    def asset_id(self):
        """Gets the asset_id of this AssetSummary.

        媒资ID。

        :return: The asset_id of this AssetSummary.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this AssetSummary.

        媒资ID。

        :param asset_id: The asset_id of this AssetSummary.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def title(self):
        """Gets the title of this AssetSummary.

        媒资标题。长度不超过128个字节，UTF-8编码。

        :return: The title of this AssetSummary.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AssetSummary.

        媒资标题。长度不超过128个字节，UTF-8编码。

        :param title: The title of this AssetSummary.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        """Gets the description of this AssetSummary.

        媒资描述。长度不超过1024个字节。

        :return: The description of this AssetSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AssetSummary.

        媒资描述。长度不超过1024个字节。

        :param description: The description of this AssetSummary.
        :type description: str
        """
        self._description = description

    @property
    def duration(self):
        """Gets the duration of this AssetSummary.

        媒资时长。  单位：秒。

        :return: The duration of this AssetSummary.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AssetSummary.

        媒资时长。  单位：秒。

        :param duration: The duration of this AssetSummary.
        :type duration: int
        """
        self._duration = duration

    @property
    def size(self):
        """Gets the size of this AssetSummary.

        媒资大小。  单位：字节。

        :return: The size of this AssetSummary.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this AssetSummary.

        媒资大小。  单位：字节。

        :param size: The size of this AssetSummary.
        :type size: int
        """
        self._size = size

    @property
    def original_url(self):
        """Gets the original_url of this AssetSummary.

        原始播放url。

        :return: The original_url of this AssetSummary.
        :rtype: str
        """
        return self._original_url

    @original_url.setter
    def original_url(self, original_url):
        """Sets the original_url of this AssetSummary.

        原始播放url。

        :param original_url: The original_url of this AssetSummary.
        :type original_url: str
        """
        self._original_url = original_url

    @property
    def category(self):
        """Gets the category of this AssetSummary.

        媒资分类名称。

        :return: The category of this AssetSummary.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this AssetSummary.

        媒资分类名称。

        :param category: The category of this AssetSummary.
        :type category: str
        """
        self._category = category

    @property
    def covers(self):
        """Gets the covers of this AssetSummary.

        封面信息。

        :return: The covers of this AssetSummary.
        :rtype: list[:class:`huaweicloudsdkvod.v1.CoverInfo`]
        """
        return self._covers

    @covers.setter
    def covers(self, covers):
        """Sets the covers of this AssetSummary.

        封面信息。

        :param covers: The covers of this AssetSummary.
        :type covers: list[:class:`huaweicloudsdkvod.v1.CoverInfo`]
        """
        self._covers = covers

    @property
    def create_time(self):
        """Gets the create_time of this AssetSummary.

        媒资创建时间。  格式为yyyymmddhhmmss。必须是与时区无关的UTC时间。

        :return: The create_time of this AssetSummary.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AssetSummary.

        媒资创建时间。  格式为yyyymmddhhmmss。必须是与时区无关的UTC时间。

        :param create_time: The create_time of this AssetSummary.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def asset_status(self):
        """Gets the asset_status of this AssetSummary.

        媒资状态。  取值如下： - CREATING：上传中。 - FAILED：上传失败。 - CREATED：上传成功。 - PUBLISHED：已发布。 - DELETED：已删除。

        :return: The asset_status of this AssetSummary.
        :rtype: str
        """
        return self._asset_status

    @asset_status.setter
    def asset_status(self, asset_status):
        """Sets the asset_status of this AssetSummary.

        媒资状态。  取值如下： - CREATING：上传中。 - FAILED：上传失败。 - CREATED：上传成功。 - PUBLISHED：已发布。 - DELETED：已删除。

        :param asset_status: The asset_status of this AssetSummary.
        :type asset_status: str
        """
        self._asset_status = asset_status

    @property
    def transcode_status(self):
        """Gets the transcode_status of this AssetSummary.

        转码状态。  取值如下： - UN_TRANSCODE：未转码。 - WAITING_TRANSCODE：待转码 - TRANSCODING：转码中。 - TRANSCODE_SUCCEED：转码成功。 - TRANSCODE_FAILED：转码失败。

        :return: The transcode_status of this AssetSummary.
        :rtype: str
        """
        return self._transcode_status

    @transcode_status.setter
    def transcode_status(self, transcode_status):
        """Sets the transcode_status of this AssetSummary.

        转码状态。  取值如下： - UN_TRANSCODE：未转码。 - WAITING_TRANSCODE：待转码 - TRANSCODING：转码中。 - TRANSCODE_SUCCEED：转码成功。 - TRANSCODE_FAILED：转码失败。

        :param transcode_status: The transcode_status of this AssetSummary.
        :type transcode_status: str
        """
        self._transcode_status = transcode_status

    @property
    def thumbnail_status(self):
        """Gets the thumbnail_status of this AssetSummary.

        截图状态。  取值如下： - UN_THUMBNAIL：未截图。 - THUMBNAILING：截图中。 - THUMBNAIL_SUCCEED：截图成功。 - THUMBNAIL_FAILED：截图失败。

        :return: The thumbnail_status of this AssetSummary.
        :rtype: str
        """
        return self._thumbnail_status

    @thumbnail_status.setter
    def thumbnail_status(self, thumbnail_status):
        """Sets the thumbnail_status of this AssetSummary.

        截图状态。  取值如下： - UN_THUMBNAIL：未截图。 - THUMBNAILING：截图中。 - THUMBNAIL_SUCCEED：截图成功。 - THUMBNAIL_FAILED：截图失败。

        :param thumbnail_status: The thumbnail_status of this AssetSummary.
        :type thumbnail_status: str
        """
        self._thumbnail_status = thumbnail_status

    @property
    def review_status(self):
        """Gets the review_status of this AssetSummary.

        内容审核状态  取值如下： - UN_REVIEW：未审核。 - REVIEWING：审核中。 - REVIEW_SUSPICIOUS：审核可疑，需要人工复审。 - REVIEW_PASSED：审核通过。 - REVIEW_FAILED：审核失败。 - REVIEW_BLOCKED：已屏蔽。

        :return: The review_status of this AssetSummary.
        :rtype: str
        """
        return self._review_status

    @review_status.setter
    def review_status(self, review_status):
        """Sets the review_status of this AssetSummary.

        内容审核状态  取值如下： - UN_REVIEW：未审核。 - REVIEWING：审核中。 - REVIEW_SUSPICIOUS：审核可疑，需要人工复审。 - REVIEW_PASSED：审核通过。 - REVIEW_FAILED：审核失败。 - REVIEW_BLOCKED：已屏蔽。

        :param review_status: The review_status of this AssetSummary.
        :type review_status: str
        """
        self._review_status = review_status

    @property
    def exec_desc(self):
        """Gets the exec_desc of this AssetSummary.

        媒资的任务执行描述汇总。  示例： - asset_exec_desc: upload success，媒资任务执行描述信息。 - transcode_exec_desc: transcode success，转码任务执行描述信息。 - thumbnail_exec_desc: thumbnail failed，截图任务执行描述信息。 - review_exec_desc: review pass，审核任务执行描述信息。

        :return: The exec_desc of this AssetSummary.
        :rtype: str
        """
        return self._exec_desc

    @exec_desc.setter
    def exec_desc(self, exec_desc):
        """Sets the exec_desc of this AssetSummary.

        媒资的任务执行描述汇总。  示例： - asset_exec_desc: upload success，媒资任务执行描述信息。 - transcode_exec_desc: transcode success，转码任务执行描述信息。 - thumbnail_exec_desc: thumbnail failed，截图任务执行描述信息。 - review_exec_desc: review pass，审核任务执行描述信息。

        :param exec_desc: The exec_desc of this AssetSummary.
        :type exec_desc: str
        """
        self._exec_desc = exec_desc

    @property
    def media_type(self):
        """Gets the media_type of this AssetSummary.

        音视频文件的格式。  取值如下： - 视频文件格式：MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG - 音频文件格式：MP3、OGG、WAV、WMA、APE、FLAC、AAC、AC3、MMF、AMR、M4A、M4R、WV、MP2

        :return: The media_type of this AssetSummary.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this AssetSummary.

        音视频文件的格式。  取值如下： - 视频文件格式：MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG - 音频文件格式：MP3、OGG、WAV、WMA、APE、FLAC、AAC、AC3、MMF、AMR、M4A、M4R、WV、MP2

        :param media_type: The media_type of this AssetSummary.
        :type media_type: str
        """
        self._media_type = media_type

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
        if not isinstance(other, AssetSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
