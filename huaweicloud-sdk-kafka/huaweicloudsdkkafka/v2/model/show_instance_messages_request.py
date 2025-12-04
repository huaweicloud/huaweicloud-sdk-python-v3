# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceMessagesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'topic': 'str',
        'asc': 'bool',
        'start_time': 'str',
        'end_time': 'str',
        'limit': 'str',
        'offset': 'str',
        'download': 'bool',
        'message_offset': 'str',
        'partition': 'str',
        'keyword': 'str',
        'key': 'str',
        'include': 'str',
        'exclude': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'topic': 'topic',
        'asc': 'asc',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'download': 'download',
        'message_offset': 'message_offset',
        'partition': 'partition',
        'keyword': 'keyword',
        'key': 'key',
        'include': 'include',
        'exclude': 'exclude'
    }

    def __init__(self, instance_id=None, topic=None, asc=None, start_time=None, end_time=None, limit=None, offset=None, download=None, message_offset=None, partition=None, keyword=None, key=None, include=None, exclude=None):
        r"""ShowInstanceMessagesRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**： 实例ID。获取方法如下：调用“查询所有实例列表”接口，从响应体中获取实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type instance_id: str
        :param topic: **参数解释**： Topic名称。 **约束限制**： Topic名称必须以字母开头且只支持大小写字母、中横线、下划线以及数字。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type topic: str
        :param asc: **参数解释**： 是否按照时间排序。 **约束限制**： 不涉及。 **取值范围**： - true：按照时间排序。 - false：不按照时间排序。 **默认取值**： 不涉及。
        :type asc: bool
        :param start_time: **参数解释**： 开始时间。  Unix毫秒时间戳。  **约束限制**： 查询消息偏移量时，为必选参数。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type start_time: str
        :param end_time: **参数解释**： 结束时间。  Unix毫秒时间戳。  **约束限制**： 查询消息偏移量时，为必选参数。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type end_time: str
        :param limit: **参数解释**： 每一页显示的消息数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type limit: str
        :param offset: **参数解释**： 页数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type offset: str
        :param download: **参数解释**： 是否下载消息到本地。 **约束限制**： 不涉及。 **取值范围**： - true：下载。 - false：不下载。 **默认取值**： 不涉及。
        :type download: bool
        :param message_offset: **参数解释**： 消息偏移量。 **约束限制**： 查询消息内容时，为必选参数。  若start_time、end_time参数不为空，该参数无效。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type message_offset: str
        :param partition: **参数解释**： 分区。 **约束限制**： 查询消息内容时，为必选参数。  若start_time、end_time参数不为空，该参数无效。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type partition: str
        :param keyword: **参数解释**： 设置查询消息的关键词。 **约束限制**： 不涉及。 **取值范围**： 0~50字符。 **默认取值**： 不涉及。
        :type keyword: str
        :param key: **参数解释**： 设置消息的KEY，查询结果为包含KEY的所有消息。 **约束限制**： 由于查询资源和性能限制，最大搜索10000条消息且所有消息总大小不超过200MB，最多返回包含KEY的前10条消息。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type key: str
        :param include: **参数解释**： 设置消息正文中包含的关键词，查询结果为包含此关键词的消息。 **约束限制**： 多个关键字用%2C隔开，%2C是“,”的URL编码形式。 **取值范围**： include与exclude的关键词总数不得超过20个。 **默认取值**： 不涉及。
        :type include: str
        :param exclude: **参数解释**： 设置消息正文中需要排除的关键词，查询结果为不包含此关键词的消息。 **约束限制**： 多个关键字用%2C隔开，%2C是“,”的URL编码形式。 **取值范围**： include与exclude的关键词总数不得超过20个。 **默认取值**： 不涉及。
        :type exclude: str
        """
        
        

        self._instance_id = None
        self._topic = None
        self._asc = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._download = None
        self._message_offset = None
        self._partition = None
        self._keyword = None
        self._key = None
        self._include = None
        self._exclude = None
        self.discriminator = None

        self.instance_id = instance_id
        self.topic = topic
        if asc is not None:
            self.asc = asc
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if download is not None:
            self.download = download
        if message_offset is not None:
            self.message_offset = message_offset
        if partition is not None:
            self.partition = partition
        if keyword is not None:
            self.keyword = keyword
        if key is not None:
            self.key = key
        if include is not None:
            self.include = include
        if exclude is not None:
            self.exclude = exclude

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowInstanceMessagesRequest.

        **参数解释**： 实例ID。获取方法如下：调用“查询所有实例列表”接口，从响应体中获取实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The instance_id of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowInstanceMessagesRequest.

        **参数解释**： 实例ID。获取方法如下：调用“查询所有实例列表”接口，从响应体中获取实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param instance_id: The instance_id of this ShowInstanceMessagesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def topic(self):
        r"""Gets the topic of this ShowInstanceMessagesRequest.

        **参数解释**： Topic名称。 **约束限制**： Topic名称必须以字母开头且只支持大小写字母、中横线、下划线以及数字。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The topic of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this ShowInstanceMessagesRequest.

        **参数解释**： Topic名称。 **约束限制**： Topic名称必须以字母开头且只支持大小写字母、中横线、下划线以及数字。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param topic: The topic of this ShowInstanceMessagesRequest.
        :type topic: str
        """
        self._topic = topic

    @property
    def asc(self):
        r"""Gets the asc of this ShowInstanceMessagesRequest.

        **参数解释**： 是否按照时间排序。 **约束限制**： 不涉及。 **取值范围**： - true：按照时间排序。 - false：不按照时间排序。 **默认取值**： 不涉及。

        :return: The asc of this ShowInstanceMessagesRequest.
        :rtype: bool
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        r"""Sets the asc of this ShowInstanceMessagesRequest.

        **参数解释**： 是否按照时间排序。 **约束限制**： 不涉及。 **取值范围**： - true：按照时间排序。 - false：不按照时间排序。 **默认取值**： 不涉及。

        :param asc: The asc of this ShowInstanceMessagesRequest.
        :type asc: bool
        """
        self._asc = asc

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowInstanceMessagesRequest.

        **参数解释**： 开始时间。  Unix毫秒时间戳。  **约束限制**： 查询消息偏移量时，为必选参数。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The start_time of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowInstanceMessagesRequest.

        **参数解释**： 开始时间。  Unix毫秒时间戳。  **约束限制**： 查询消息偏移量时，为必选参数。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param start_time: The start_time of this ShowInstanceMessagesRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowInstanceMessagesRequest.

        **参数解释**： 结束时间。  Unix毫秒时间戳。  **约束限制**： 查询消息偏移量时，为必选参数。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The end_time of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowInstanceMessagesRequest.

        **参数解释**： 结束时间。  Unix毫秒时间戳。  **约束限制**： 查询消息偏移量时，为必选参数。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param end_time: The end_time of this ShowInstanceMessagesRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ShowInstanceMessagesRequest.

        **参数解释**： 每一页显示的消息数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The limit of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowInstanceMessagesRequest.

        **参数解释**： 每一页显示的消息数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param limit: The limit of this ShowInstanceMessagesRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowInstanceMessagesRequest.

        **参数解释**： 页数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The offset of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowInstanceMessagesRequest.

        **参数解释**： 页数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param offset: The offset of this ShowInstanceMessagesRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def download(self):
        r"""Gets the download of this ShowInstanceMessagesRequest.

        **参数解释**： 是否下载消息到本地。 **约束限制**： 不涉及。 **取值范围**： - true：下载。 - false：不下载。 **默认取值**： 不涉及。

        :return: The download of this ShowInstanceMessagesRequest.
        :rtype: bool
        """
        return self._download

    @download.setter
    def download(self, download):
        r"""Sets the download of this ShowInstanceMessagesRequest.

        **参数解释**： 是否下载消息到本地。 **约束限制**： 不涉及。 **取值范围**： - true：下载。 - false：不下载。 **默认取值**： 不涉及。

        :param download: The download of this ShowInstanceMessagesRequest.
        :type download: bool
        """
        self._download = download

    @property
    def message_offset(self):
        r"""Gets the message_offset of this ShowInstanceMessagesRequest.

        **参数解释**： 消息偏移量。 **约束限制**： 查询消息内容时，为必选参数。  若start_time、end_time参数不为空，该参数无效。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The message_offset of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._message_offset

    @message_offset.setter
    def message_offset(self, message_offset):
        r"""Sets the message_offset of this ShowInstanceMessagesRequest.

        **参数解释**： 消息偏移量。 **约束限制**： 查询消息内容时，为必选参数。  若start_time、end_time参数不为空，该参数无效。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param message_offset: The message_offset of this ShowInstanceMessagesRequest.
        :type message_offset: str
        """
        self._message_offset = message_offset

    @property
    def partition(self):
        r"""Gets the partition of this ShowInstanceMessagesRequest.

        **参数解释**： 分区。 **约束限制**： 查询消息内容时，为必选参数。  若start_time、end_time参数不为空，该参数无效。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The partition of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this ShowInstanceMessagesRequest.

        **参数解释**： 分区。 **约束限制**： 查询消息内容时，为必选参数。  若start_time、end_time参数不为空，该参数无效。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param partition: The partition of this ShowInstanceMessagesRequest.
        :type partition: str
        """
        self._partition = partition

    @property
    def keyword(self):
        r"""Gets the keyword of this ShowInstanceMessagesRequest.

        **参数解释**： 设置查询消息的关键词。 **约束限制**： 不涉及。 **取值范围**： 0~50字符。 **默认取值**： 不涉及。

        :return: The keyword of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this ShowInstanceMessagesRequest.

        **参数解释**： 设置查询消息的关键词。 **约束限制**： 不涉及。 **取值范围**： 0~50字符。 **默认取值**： 不涉及。

        :param keyword: The keyword of this ShowInstanceMessagesRequest.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def key(self):
        r"""Gets the key of this ShowInstanceMessagesRequest.

        **参数解释**： 设置消息的KEY，查询结果为包含KEY的所有消息。 **约束限制**： 由于查询资源和性能限制，最大搜索10000条消息且所有消息总大小不超过200MB，最多返回包含KEY的前10条消息。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The key of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ShowInstanceMessagesRequest.

        **参数解释**： 设置消息的KEY，查询结果为包含KEY的所有消息。 **约束限制**： 由于查询资源和性能限制，最大搜索10000条消息且所有消息总大小不超过200MB，最多返回包含KEY的前10条消息。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param key: The key of this ShowInstanceMessagesRequest.
        :type key: str
        """
        self._key = key

    @property
    def include(self):
        r"""Gets the include of this ShowInstanceMessagesRequest.

        **参数解释**： 设置消息正文中包含的关键词，查询结果为包含此关键词的消息。 **约束限制**： 多个关键字用%2C隔开，%2C是“,”的URL编码形式。 **取值范围**： include与exclude的关键词总数不得超过20个。 **默认取值**： 不涉及。

        :return: The include of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._include

    @include.setter
    def include(self, include):
        r"""Sets the include of this ShowInstanceMessagesRequest.

        **参数解释**： 设置消息正文中包含的关键词，查询结果为包含此关键词的消息。 **约束限制**： 多个关键字用%2C隔开，%2C是“,”的URL编码形式。 **取值范围**： include与exclude的关键词总数不得超过20个。 **默认取值**： 不涉及。

        :param include: The include of this ShowInstanceMessagesRequest.
        :type include: str
        """
        self._include = include

    @property
    def exclude(self):
        r"""Gets the exclude of this ShowInstanceMessagesRequest.

        **参数解释**： 设置消息正文中需要排除的关键词，查询结果为不包含此关键词的消息。 **约束限制**： 多个关键字用%2C隔开，%2C是“,”的URL编码形式。 **取值范围**： include与exclude的关键词总数不得超过20个。 **默认取值**： 不涉及。

        :return: The exclude of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._exclude

    @exclude.setter
    def exclude(self, exclude):
        r"""Sets the exclude of this ShowInstanceMessagesRequest.

        **参数解释**： 设置消息正文中需要排除的关键词，查询结果为不包含此关键词的消息。 **约束限制**： 多个关键字用%2C隔开，%2C是“,”的URL编码形式。 **取值范围**： include与exclude的关键词总数不得超过20个。 **默认取值**： 不涉及。

        :param exclude: The exclude of this ShowInstanceMessagesRequest.
        :type exclude: str
        """
        self._exclude = exclude

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
        if not isinstance(other, ShowInstanceMessagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
