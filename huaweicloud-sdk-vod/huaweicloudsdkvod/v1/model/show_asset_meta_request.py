# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAssetMetaRequest:

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
        'transcode_status': 'list[str]',
        'asset_status': 'list[str]',
        'start_time': 'str',
        'end_time': 'str',
        'category_id': 'int',
        'tags': 'str',
        'query_string': 'str',
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'status': 'status',
        'transcode_status': 'transcodeStatus',
        'asset_status': 'assetStatus',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'category_id': 'category_id',
        'tags': 'tags',
        'query_string': 'query_string',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, asset_id=None, status=None, transcode_status=None, asset_status=None, start_time=None, end_time=None, category_id=None, tags=None, query_string=None, page=None, size=None):
        """ShowAssetMetaRequest

        The model defined in huaweicloud sdk

        :param asset_id: 媒资id，最多同时查询10个媒资。
        :type asset_id: list[str]
        :param status: 媒资状态。  取值如下： - UNCREATED：未创建（媒资ID不存在 ） - DELETED：已删除 - CANCELLED：上传取消 - SERVER_ERROR：上传失败（点播服务端故障） - UPLOAD_FAILED：上传失败（向OBS上传失败） - CREATING：创建中 - PUBLISHED：已发布 - TRANSCODING：待发布（转码中） - TRANSCODE_FAILED：待发布（转码失败） - TRANSCODE_SUCCEED：待发布（转码成功） - CREATED：待发布（未转码）
        :type status: list[str]
        :param transcode_status: 转码状态  取值如下： - TRANSCODING：转码中 - TRANSCODE_FAILED：转码失败 - TRANSCODE_SUCCEED：转码成功 - UN_TRANSCODE：未转码 - WAITING_TRANSCODE：等待转码
        :type transcode_status: list[str]
        :param asset_status: 媒资状态。  取值如下： - PUBLISHED：已发布 - CREATED：未发布
        :type asset_status: list[str]
        :param start_time: 起始时间，查询指定“**asset_id**”时，该参数无效。  格式为yyyymmddhhmmss。必须是与时区无关的UTC时间。
        :type start_time: str
        :param end_time: 结束时间，查询指定“**asset_id**”时，该参数无效。  格式为yyyymmddhhmmss。必须是与时区无关的UTC时间。
        :type end_time: str
        :param category_id: 分类ID。
        :type category_id: int
        :param tags: 媒资标签。  单个标签不超过16个字节，最多不超过16个标签。  多个用逗号分隔，UTF8编码。
        :type tags: str
        :param query_string: 在媒资标题、描述中模糊查询的字符串。
        :type query_string: str
        :param page: 分页编号，查询指定“asset_id”时，该参数无效。  默认值：0。
        :type page: int
        :param size: 每页记录数，查询指定“**asset_id**”时，该参数无效。  取值范围：[1,100]。  默认值：10。
        :type size: int
        """
        
        

        self._asset_id = None
        self._status = None
        self._transcode_status = None
        self._asset_status = None
        self._start_time = None
        self._end_time = None
        self._category_id = None
        self._tags = None
        self._query_string = None
        self._page = None
        self._size = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if status is not None:
            self.status = status
        if transcode_status is not None:
            self.transcode_status = transcode_status
        if asset_status is not None:
            self.asset_status = asset_status
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
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size

    @property
    def asset_id(self):
        """Gets the asset_id of this ShowAssetMetaRequest.

        媒资id，最多同时查询10个媒资。

        :return: The asset_id of this ShowAssetMetaRequest.
        :rtype: list[str]
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ShowAssetMetaRequest.

        媒资id，最多同时查询10个媒资。

        :param asset_id: The asset_id of this ShowAssetMetaRequest.
        :type asset_id: list[str]
        """
        self._asset_id = asset_id

    @property
    def status(self):
        """Gets the status of this ShowAssetMetaRequest.

        媒资状态。  取值如下： - UNCREATED：未创建（媒资ID不存在 ） - DELETED：已删除 - CANCELLED：上传取消 - SERVER_ERROR：上传失败（点播服务端故障） - UPLOAD_FAILED：上传失败（向OBS上传失败） - CREATING：创建中 - PUBLISHED：已发布 - TRANSCODING：待发布（转码中） - TRANSCODE_FAILED：待发布（转码失败） - TRANSCODE_SUCCEED：待发布（转码成功） - CREATED：待发布（未转码）

        :return: The status of this ShowAssetMetaRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowAssetMetaRequest.

        媒资状态。  取值如下： - UNCREATED：未创建（媒资ID不存在 ） - DELETED：已删除 - CANCELLED：上传取消 - SERVER_ERROR：上传失败（点播服务端故障） - UPLOAD_FAILED：上传失败（向OBS上传失败） - CREATING：创建中 - PUBLISHED：已发布 - TRANSCODING：待发布（转码中） - TRANSCODE_FAILED：待发布（转码失败） - TRANSCODE_SUCCEED：待发布（转码成功） - CREATED：待发布（未转码）

        :param status: The status of this ShowAssetMetaRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def transcode_status(self):
        """Gets the transcode_status of this ShowAssetMetaRequest.

        转码状态  取值如下： - TRANSCODING：转码中 - TRANSCODE_FAILED：转码失败 - TRANSCODE_SUCCEED：转码成功 - UN_TRANSCODE：未转码 - WAITING_TRANSCODE：等待转码

        :return: The transcode_status of this ShowAssetMetaRequest.
        :rtype: list[str]
        """
        return self._transcode_status

    @transcode_status.setter
    def transcode_status(self, transcode_status):
        """Sets the transcode_status of this ShowAssetMetaRequest.

        转码状态  取值如下： - TRANSCODING：转码中 - TRANSCODE_FAILED：转码失败 - TRANSCODE_SUCCEED：转码成功 - UN_TRANSCODE：未转码 - WAITING_TRANSCODE：等待转码

        :param transcode_status: The transcode_status of this ShowAssetMetaRequest.
        :type transcode_status: list[str]
        """
        self._transcode_status = transcode_status

    @property
    def asset_status(self):
        """Gets the asset_status of this ShowAssetMetaRequest.

        媒资状态。  取值如下： - PUBLISHED：已发布 - CREATED：未发布

        :return: The asset_status of this ShowAssetMetaRequest.
        :rtype: list[str]
        """
        return self._asset_status

    @asset_status.setter
    def asset_status(self, asset_status):
        """Sets the asset_status of this ShowAssetMetaRequest.

        媒资状态。  取值如下： - PUBLISHED：已发布 - CREATED：未发布

        :param asset_status: The asset_status of this ShowAssetMetaRequest.
        :type asset_status: list[str]
        """
        self._asset_status = asset_status

    @property
    def start_time(self):
        """Gets the start_time of this ShowAssetMetaRequest.

        起始时间，查询指定“**asset_id**”时，该参数无效。  格式为yyyymmddhhmmss。必须是与时区无关的UTC时间。

        :return: The start_time of this ShowAssetMetaRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowAssetMetaRequest.

        起始时间，查询指定“**asset_id**”时，该参数无效。  格式为yyyymmddhhmmss。必须是与时区无关的UTC时间。

        :param start_time: The start_time of this ShowAssetMetaRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowAssetMetaRequest.

        结束时间，查询指定“**asset_id**”时，该参数无效。  格式为yyyymmddhhmmss。必须是与时区无关的UTC时间。

        :return: The end_time of this ShowAssetMetaRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowAssetMetaRequest.

        结束时间，查询指定“**asset_id**”时，该参数无效。  格式为yyyymmddhhmmss。必须是与时区无关的UTC时间。

        :param end_time: The end_time of this ShowAssetMetaRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def category_id(self):
        """Gets the category_id of this ShowAssetMetaRequest.

        分类ID。

        :return: The category_id of this ShowAssetMetaRequest.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this ShowAssetMetaRequest.

        分类ID。

        :param category_id: The category_id of this ShowAssetMetaRequest.
        :type category_id: int
        """
        self._category_id = category_id

    @property
    def tags(self):
        """Gets the tags of this ShowAssetMetaRequest.

        媒资标签。  单个标签不超过16个字节，最多不超过16个标签。  多个用逗号分隔，UTF8编码。

        :return: The tags of this ShowAssetMetaRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowAssetMetaRequest.

        媒资标签。  单个标签不超过16个字节，最多不超过16个标签。  多个用逗号分隔，UTF8编码。

        :param tags: The tags of this ShowAssetMetaRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def query_string(self):
        """Gets the query_string of this ShowAssetMetaRequest.

        在媒资标题、描述中模糊查询的字符串。

        :return: The query_string of this ShowAssetMetaRequest.
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """Sets the query_string of this ShowAssetMetaRequest.

        在媒资标题、描述中模糊查询的字符串。

        :param query_string: The query_string of this ShowAssetMetaRequest.
        :type query_string: str
        """
        self._query_string = query_string

    @property
    def page(self):
        """Gets the page of this ShowAssetMetaRequest.

        分页编号，查询指定“asset_id”时，该参数无效。  默认值：0。

        :return: The page of this ShowAssetMetaRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ShowAssetMetaRequest.

        分页编号，查询指定“asset_id”时，该参数无效。  默认值：0。

        :param page: The page of this ShowAssetMetaRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this ShowAssetMetaRequest.

        每页记录数，查询指定“**asset_id**”时，该参数无效。  取值范围：[1,100]。  默认值：10。

        :return: The size of this ShowAssetMetaRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ShowAssetMetaRequest.

        每页记录数，查询指定“**asset_id**”时，该参数无效。  取值范围：[1,100]。  默认值：10。

        :param size: The size of this ShowAssetMetaRequest.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, ShowAssetMetaRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
