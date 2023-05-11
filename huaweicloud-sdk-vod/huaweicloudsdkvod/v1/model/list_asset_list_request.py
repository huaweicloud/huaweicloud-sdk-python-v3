# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssetListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'list[str]',
        'status': 'list[str]',
        'start_time': 'str',
        'end_time': 'str',
        'category_id': 'int',
        'tags': 'str',
        'query_string': 'str',
        'media_type': 'list[str]',
        'page': 'int',
        'size': 'int',
        'order': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'category_id': 'category_id',
        'tags': 'tags',
        'query_string': 'query_string',
        'media_type': 'media_type',
        'page': 'page',
        'size': 'size',
        'order': 'order'
    }

    def __init__(self, asset_id=None, status=None, start_time=None, end_time=None, category_id=None, tags=None, query_string=None, media_type=None, page=None, size=None, order=None):
        """ListAssetListRequest

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID，最多同时查询10个。
        :type asset_id: list[str]
        :param status: 媒资状态，同时查询多个状态的媒资。  取值如下： - CREATING：上传中 - FAILED：上传失败 - CREATED：上传成功 - PUBLISHED：已发布 - TRANSCODING：转码中 - TRANSCODE_SUCCEED：转码成功 - TRANSCODE_FAILED：转码失败 - THUMBNAILING：截图中 - THUMBNAIL_SUCCEED：截图成功 - THUMBNAIL_FAILED：截图失败 - UN_REVIEW：未审核 - REVIEWING：审核中 - REVIEW_SUSPICIOUS ：审核不过，待人工复审 - REVIEW_PASSED：审核通过 - REVIEW_FAILED：审核任务失败 - REVIEW_BLOCKED：已屏蔽
        :type status: list[str]
        :param start_time: 起始时间。  格式为yyyymmddhhm mss。必须是与时区无关的UTC时间。
        :type start_time: str
        :param end_time: 结束时间。  格式为yyyymmddhhm mss。必须是与时区无关的UTC时间。
        :type end_time: str
        :param category_id: 分类ID。
        :type category_id: int
        :param tags: 媒资标签。 单个标签不超过16个字节， 最多不超过16 个标签。 多个用英文逗号分隔，UTF8编码。
        :type tags: str
        :param query_string: 在媒资标题、 描述、分类名称中模糊查询的字符串。
        :type query_string: str
        :param media_type: 音视频文件的格式，支持多格式查询，最多不超过20个。  取值如下： - 视频文件格式：MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG - 音频文件格式：MP3、OGG、WAV、WMA、APE、FLAC、AAC、AC3、MMF、AMR、M4A、M4R、WV、MP2
        :type media_type: list[str]
        :param page: 分页编号。  默认值：0。
        :type page: int
        :param size: 每页记录数。  取值范围：[1,100]。  默认值：10。
        :type size: int
        :param order: 查询顺序，按createTime顺序还是倒序
        :type order: str
        """
        
        

        self._asset_id = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._category_id = None
        self._tags = None
        self._query_string = None
        self._media_type = None
        self._page = None
        self._size = None
        self._order = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if category_id is not None:
            self.category_id = category_id
        if tags is not None:
            self.tags = tags
        if query_string is not None:
            self.query_string = query_string
        if media_type is not None:
            self.media_type = media_type
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size
        if order is not None:
            self.order = order

    @property
    def asset_id(self):
        """Gets the asset_id of this ListAssetListRequest.

        媒资ID，最多同时查询10个。

        :return: The asset_id of this ListAssetListRequest.
        :rtype: list[str]
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ListAssetListRequest.

        媒资ID，最多同时查询10个。

        :param asset_id: The asset_id of this ListAssetListRequest.
        :type asset_id: list[str]
        """
        self._asset_id = asset_id

    @property
    def status(self):
        """Gets the status of this ListAssetListRequest.

        媒资状态，同时查询多个状态的媒资。  取值如下： - CREATING：上传中 - FAILED：上传失败 - CREATED：上传成功 - PUBLISHED：已发布 - TRANSCODING：转码中 - TRANSCODE_SUCCEED：转码成功 - TRANSCODE_FAILED：转码失败 - THUMBNAILING：截图中 - THUMBNAIL_SUCCEED：截图成功 - THUMBNAIL_FAILED：截图失败 - UN_REVIEW：未审核 - REVIEWING：审核中 - REVIEW_SUSPICIOUS ：审核不过，待人工复审 - REVIEW_PASSED：审核通过 - REVIEW_FAILED：审核任务失败 - REVIEW_BLOCKED：已屏蔽

        :return: The status of this ListAssetListRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListAssetListRequest.

        媒资状态，同时查询多个状态的媒资。  取值如下： - CREATING：上传中 - FAILED：上传失败 - CREATED：上传成功 - PUBLISHED：已发布 - TRANSCODING：转码中 - TRANSCODE_SUCCEED：转码成功 - TRANSCODE_FAILED：转码失败 - THUMBNAILING：截图中 - THUMBNAIL_SUCCEED：截图成功 - THUMBNAIL_FAILED：截图失败 - UN_REVIEW：未审核 - REVIEWING：审核中 - REVIEW_SUSPICIOUS ：审核不过，待人工复审 - REVIEW_PASSED：审核通过 - REVIEW_FAILED：审核任务失败 - REVIEW_BLOCKED：已屏蔽

        :param status: The status of this ListAssetListRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def start_time(self):
        """Gets the start_time of this ListAssetListRequest.

        起始时间。  格式为yyyymmddhhm mss。必须是与时区无关的UTC时间。

        :return: The start_time of this ListAssetListRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListAssetListRequest.

        起始时间。  格式为yyyymmddhhm mss。必须是与时区无关的UTC时间。

        :param start_time: The start_time of this ListAssetListRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListAssetListRequest.

        结束时间。  格式为yyyymmddhhm mss。必须是与时区无关的UTC时间。

        :return: The end_time of this ListAssetListRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListAssetListRequest.

        结束时间。  格式为yyyymmddhhm mss。必须是与时区无关的UTC时间。

        :param end_time: The end_time of this ListAssetListRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def category_id(self):
        """Gets the category_id of this ListAssetListRequest.

        分类ID。

        :return: The category_id of this ListAssetListRequest.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this ListAssetListRequest.

        分类ID。

        :param category_id: The category_id of this ListAssetListRequest.
        :type category_id: int
        """
        self._category_id = category_id

    @property
    def tags(self):
        """Gets the tags of this ListAssetListRequest.

        媒资标签。 单个标签不超过16个字节， 最多不超过16 个标签。 多个用英文逗号分隔，UTF8编码。

        :return: The tags of this ListAssetListRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListAssetListRequest.

        媒资标签。 单个标签不超过16个字节， 最多不超过16 个标签。 多个用英文逗号分隔，UTF8编码。

        :param tags: The tags of this ListAssetListRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def query_string(self):
        """Gets the query_string of this ListAssetListRequest.

        在媒资标题、 描述、分类名称中模糊查询的字符串。

        :return: The query_string of this ListAssetListRequest.
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """Sets the query_string of this ListAssetListRequest.

        在媒资标题、 描述、分类名称中模糊查询的字符串。

        :param query_string: The query_string of this ListAssetListRequest.
        :type query_string: str
        """
        self._query_string = query_string

    @property
    def media_type(self):
        """Gets the media_type of this ListAssetListRequest.

        音视频文件的格式，支持多格式查询，最多不超过20个。  取值如下： - 视频文件格式：MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG - 音频文件格式：MP3、OGG、WAV、WMA、APE、FLAC、AAC、AC3、MMF、AMR、M4A、M4R、WV、MP2

        :return: The media_type of this ListAssetListRequest.
        :rtype: list[str]
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this ListAssetListRequest.

        音视频文件的格式，支持多格式查询，最多不超过20个。  取值如下： - 视频文件格式：MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG - 音频文件格式：MP3、OGG、WAV、WMA、APE、FLAC、AAC、AC3、MMF、AMR、M4A、M4R、WV、MP2

        :param media_type: The media_type of this ListAssetListRequest.
        :type media_type: list[str]
        """
        self._media_type = media_type

    @property
    def page(self):
        """Gets the page of this ListAssetListRequest.

        分页编号。  默认值：0。

        :return: The page of this ListAssetListRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListAssetListRequest.

        分页编号。  默认值：0。

        :param page: The page of this ListAssetListRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this ListAssetListRequest.

        每页记录数。  取值范围：[1,100]。  默认值：10。

        :return: The size of this ListAssetListRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListAssetListRequest.

        每页记录数。  取值范围：[1,100]。  默认值：10。

        :param size: The size of this ListAssetListRequest.
        :type size: int
        """
        self._size = size

    @property
    def order(self):
        """Gets the order of this ListAssetListRequest.

        查询顺序，按createTime顺序还是倒序

        :return: The order of this ListAssetListRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListAssetListRequest.

        查询顺序，按createTime顺序还是倒序

        :param order: The order of this ListAssetListRequest.
        :type order: str
        """
        self._order = order

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
        if not isinstance(other, ListAssetListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
