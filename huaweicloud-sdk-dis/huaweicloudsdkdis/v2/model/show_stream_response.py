# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStreamResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stream_name': 'str',
        'create_time': 'int',
        'last_modified_time': 'int',
        'status': 'str',
        'stream_type': 'str',
        'partitions': 'list[PartitionResult]',
        'has_more_partitions': 'bool',
        'retention_period': 'int',
        'stream_id': 'str',
        'data_type': 'str',
        'data_schema': 'str',
        'compression_format': 'str',
        'csv_properties': 'CSVProperties',
        'writable_partition_count': 'int',
        'readable_partition_count': 'int',
        'update_partition_counts': 'list[UpdatePartitionCount]',
        'tags': 'list[Tag]',
        'sys_tags': 'list[SysTag]',
        'auto_scale_enabled': 'bool',
        'auto_scale_min_partition_count': 'int',
        'auto_scale_max_partition_count': 'int'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'create_time': 'create_time',
        'last_modified_time': 'last_modified_time',
        'status': 'status',
        'stream_type': 'stream_type',
        'partitions': 'partitions',
        'has_more_partitions': 'has_more_partitions',
        'retention_period': 'retention_period',
        'stream_id': 'stream_id',
        'data_type': 'data_type',
        'data_schema': 'data_schema',
        'compression_format': 'compression_format',
        'csv_properties': 'csv_properties',
        'writable_partition_count': 'writable_partition_count',
        'readable_partition_count': 'readable_partition_count',
        'update_partition_counts': 'update_partition_counts',
        'tags': 'tags',
        'sys_tags': 'sys_tags',
        'auto_scale_enabled': 'auto_scale_enabled',
        'auto_scale_min_partition_count': 'auto_scale_min_partition_count',
        'auto_scale_max_partition_count': 'auto_scale_max_partition_count'
    }

    def __init__(self, stream_name=None, create_time=None, last_modified_time=None, status=None, stream_type=None, partitions=None, has_more_partitions=None, retention_period=None, stream_id=None, data_type=None, data_schema=None, compression_format=None, csv_properties=None, writable_partition_count=None, readable_partition_count=None, update_partition_counts=None, tags=None, sys_tags=None, auto_scale_enabled=None, auto_scale_min_partition_count=None, auto_scale_max_partition_count=None):
        """ShowStreamResponse

        The model defined in huaweicloud sdk

        :param stream_name: 通道名称。
        :type stream_name: str
        :param create_time: 通道创建的时间，13位时间戳。
        :type create_time: int
        :param last_modified_time: 通道最近一次修改的时间，13位时间戳。
        :type last_modified_time: int
        :param status: 通道的当前状态。  - CREATING：创建中 - RUNNING：运行中 - TERMINATING：删除中 - TERMINATED：已删除
        :type status: str
        :param stream_type: 通道类型。  - COMMON：普通通道，表示1MB带宽。 - ADVANCED：高级通道，表示5MB带宽。
        :type stream_type: str
        :param partitions: 通道的分区列表。
        :type partitions: list[:class:`huaweicloudsdkdis.v2.PartitionResult`]
        :param has_more_partitions: 是否还有更多满足请求条件的分区。  - 是：true。 - 否：false。
        :type has_more_partitions: bool
        :param retention_period: 数据保留时长，单位是小时。
        :type retention_period: int
        :param stream_id: 通道唯一标示符。
        :type stream_id: str
        :param data_type: 源数据类型。  - BLOB：存储在数据库管理系统中的一组二进制数据。 - JSON：一种开放的文件格式，以易读的文字为基础，用来传输由属性值或者序列性的值组成的数据对象。 - CSV：纯文本形式存储的表格数据，分隔符默认采用逗号。  缺省值：BLOB。
        :type data_type: str
        :param data_schema: 用于描述用户JSON、CSV格式的源数据结构，采用Avro Schema的语法描述。Avro介绍您也可以点击[这里](http://avro.apache.org/docs/current/#schemas)查看。
        :type data_schema: str
        :param compression_format: 数据的压缩类型，目前支持：  - snappy  - gzip  - zip  默认不压缩。
        :type compression_format: str
        :param csv_properties: 
        :type csv_properties: :class:`huaweicloudsdkdis.v2.CSVProperties`
        :param writable_partition_count: 可写分区总数量（只包含ACTIVE状态的分区）。
        :type writable_partition_count: int
        :param readable_partition_count: 可读分区总数量（包含ACTIVE与DELETED状态的分区）。
        :type readable_partition_count: int
        :param update_partition_counts: 扩缩容操作记录列表。
        :type update_partition_counts: list[:class:`huaweicloudsdkdis.v2.UpdatePartitionCount`]
        :param tags: 通道的标签列表。
        :type tags: list[:class:`huaweicloudsdkdis.v2.Tag`]
        :param sys_tags: 通道的企业项目。
        :type sys_tags: list[:class:`huaweicloudsdkdis.v2.SysTag`]
        :param auto_scale_enabled: 是否开启自动扩缩容。  - true：开启自动扩缩容。 - false：关闭自动扩缩容。  默认不开启。
        :type auto_scale_enabled: bool
        :param auto_scale_min_partition_count: 当自动扩缩容启用时，自动缩容的最小分片数。
        :type auto_scale_min_partition_count: int
        :param auto_scale_max_partition_count: 当自动扩缩容启用时，自动扩容的最大分片数。
        :type auto_scale_max_partition_count: int
        """
        
        super(ShowStreamResponse, self).__init__()

        self._stream_name = None
        self._create_time = None
        self._last_modified_time = None
        self._status = None
        self._stream_type = None
        self._partitions = None
        self._has_more_partitions = None
        self._retention_period = None
        self._stream_id = None
        self._data_type = None
        self._data_schema = None
        self._compression_format = None
        self._csv_properties = None
        self._writable_partition_count = None
        self._readable_partition_count = None
        self._update_partition_counts = None
        self._tags = None
        self._sys_tags = None
        self._auto_scale_enabled = None
        self._auto_scale_min_partition_count = None
        self._auto_scale_max_partition_count = None
        self.discriminator = None

        if stream_name is not None:
            self.stream_name = stream_name
        if create_time is not None:
            self.create_time = create_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if status is not None:
            self.status = status
        if stream_type is not None:
            self.stream_type = stream_type
        if partitions is not None:
            self.partitions = partitions
        if has_more_partitions is not None:
            self.has_more_partitions = has_more_partitions
        if retention_period is not None:
            self.retention_period = retention_period
        if stream_id is not None:
            self.stream_id = stream_id
        if data_type is not None:
            self.data_type = data_type
        if data_schema is not None:
            self.data_schema = data_schema
        if compression_format is not None:
            self.compression_format = compression_format
        if csv_properties is not None:
            self.csv_properties = csv_properties
        if writable_partition_count is not None:
            self.writable_partition_count = writable_partition_count
        if readable_partition_count is not None:
            self.readable_partition_count = readable_partition_count
        if update_partition_counts is not None:
            self.update_partition_counts = update_partition_counts
        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if auto_scale_enabled is not None:
            self.auto_scale_enabled = auto_scale_enabled
        if auto_scale_min_partition_count is not None:
            self.auto_scale_min_partition_count = auto_scale_min_partition_count
        if auto_scale_max_partition_count is not None:
            self.auto_scale_max_partition_count = auto_scale_max_partition_count

    @property
    def stream_name(self):
        """Gets the stream_name of this ShowStreamResponse.

        通道名称。

        :return: The stream_name of this ShowStreamResponse.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this ShowStreamResponse.

        通道名称。

        :param stream_name: The stream_name of this ShowStreamResponse.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def create_time(self):
        """Gets the create_time of this ShowStreamResponse.

        通道创建的时间，13位时间戳。

        :return: The create_time of this ShowStreamResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowStreamResponse.

        通道创建的时间，13位时间戳。

        :param create_time: The create_time of this ShowStreamResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this ShowStreamResponse.

        通道最近一次修改的时间，13位时间戳。

        :return: The last_modified_time of this ShowStreamResponse.
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this ShowStreamResponse.

        通道最近一次修改的时间，13位时间戳。

        :param last_modified_time: The last_modified_time of this ShowStreamResponse.
        :type last_modified_time: int
        """
        self._last_modified_time = last_modified_time

    @property
    def status(self):
        """Gets the status of this ShowStreamResponse.

        通道的当前状态。  - CREATING：创建中 - RUNNING：运行中 - TERMINATING：删除中 - TERMINATED：已删除

        :return: The status of this ShowStreamResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowStreamResponse.

        通道的当前状态。  - CREATING：创建中 - RUNNING：运行中 - TERMINATING：删除中 - TERMINATED：已删除

        :param status: The status of this ShowStreamResponse.
        :type status: str
        """
        self._status = status

    @property
    def stream_type(self):
        """Gets the stream_type of this ShowStreamResponse.

        通道类型。  - COMMON：普通通道，表示1MB带宽。 - ADVANCED：高级通道，表示5MB带宽。

        :return: The stream_type of this ShowStreamResponse.
        :rtype: str
        """
        return self._stream_type

    @stream_type.setter
    def stream_type(self, stream_type):
        """Sets the stream_type of this ShowStreamResponse.

        通道类型。  - COMMON：普通通道，表示1MB带宽。 - ADVANCED：高级通道，表示5MB带宽。

        :param stream_type: The stream_type of this ShowStreamResponse.
        :type stream_type: str
        """
        self._stream_type = stream_type

    @property
    def partitions(self):
        """Gets the partitions of this ShowStreamResponse.

        通道的分区列表。

        :return: The partitions of this ShowStreamResponse.
        :rtype: list[:class:`huaweicloudsdkdis.v2.PartitionResult`]
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        """Sets the partitions of this ShowStreamResponse.

        通道的分区列表。

        :param partitions: The partitions of this ShowStreamResponse.
        :type partitions: list[:class:`huaweicloudsdkdis.v2.PartitionResult`]
        """
        self._partitions = partitions

    @property
    def has_more_partitions(self):
        """Gets the has_more_partitions of this ShowStreamResponse.

        是否还有更多满足请求条件的分区。  - 是：true。 - 否：false。

        :return: The has_more_partitions of this ShowStreamResponse.
        :rtype: bool
        """
        return self._has_more_partitions

    @has_more_partitions.setter
    def has_more_partitions(self, has_more_partitions):
        """Sets the has_more_partitions of this ShowStreamResponse.

        是否还有更多满足请求条件的分区。  - 是：true。 - 否：false。

        :param has_more_partitions: The has_more_partitions of this ShowStreamResponse.
        :type has_more_partitions: bool
        """
        self._has_more_partitions = has_more_partitions

    @property
    def retention_period(self):
        """Gets the retention_period of this ShowStreamResponse.

        数据保留时长，单位是小时。

        :return: The retention_period of this ShowStreamResponse.
        :rtype: int
        """
        return self._retention_period

    @retention_period.setter
    def retention_period(self, retention_period):
        """Sets the retention_period of this ShowStreamResponse.

        数据保留时长，单位是小时。

        :param retention_period: The retention_period of this ShowStreamResponse.
        :type retention_period: int
        """
        self._retention_period = retention_period

    @property
    def stream_id(self):
        """Gets the stream_id of this ShowStreamResponse.

        通道唯一标示符。

        :return: The stream_id of this ShowStreamResponse.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this ShowStreamResponse.

        通道唯一标示符。

        :param stream_id: The stream_id of this ShowStreamResponse.
        :type stream_id: str
        """
        self._stream_id = stream_id

    @property
    def data_type(self):
        """Gets the data_type of this ShowStreamResponse.

        源数据类型。  - BLOB：存储在数据库管理系统中的一组二进制数据。 - JSON：一种开放的文件格式，以易读的文字为基础，用来传输由属性值或者序列性的值组成的数据对象。 - CSV：纯文本形式存储的表格数据，分隔符默认采用逗号。  缺省值：BLOB。

        :return: The data_type of this ShowStreamResponse.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ShowStreamResponse.

        源数据类型。  - BLOB：存储在数据库管理系统中的一组二进制数据。 - JSON：一种开放的文件格式，以易读的文字为基础，用来传输由属性值或者序列性的值组成的数据对象。 - CSV：纯文本形式存储的表格数据，分隔符默认采用逗号。  缺省值：BLOB。

        :param data_type: The data_type of this ShowStreamResponse.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def data_schema(self):
        """Gets the data_schema of this ShowStreamResponse.

        用于描述用户JSON、CSV格式的源数据结构，采用Avro Schema的语法描述。Avro介绍您也可以点击[这里](http://avro.apache.org/docs/current/#schemas)查看。

        :return: The data_schema of this ShowStreamResponse.
        :rtype: str
        """
        return self._data_schema

    @data_schema.setter
    def data_schema(self, data_schema):
        """Sets the data_schema of this ShowStreamResponse.

        用于描述用户JSON、CSV格式的源数据结构，采用Avro Schema的语法描述。Avro介绍您也可以点击[这里](http://avro.apache.org/docs/current/#schemas)查看。

        :param data_schema: The data_schema of this ShowStreamResponse.
        :type data_schema: str
        """
        self._data_schema = data_schema

    @property
    def compression_format(self):
        """Gets the compression_format of this ShowStreamResponse.

        数据的压缩类型，目前支持：  - snappy  - gzip  - zip  默认不压缩。

        :return: The compression_format of this ShowStreamResponse.
        :rtype: str
        """
        return self._compression_format

    @compression_format.setter
    def compression_format(self, compression_format):
        """Sets the compression_format of this ShowStreamResponse.

        数据的压缩类型，目前支持：  - snappy  - gzip  - zip  默认不压缩。

        :param compression_format: The compression_format of this ShowStreamResponse.
        :type compression_format: str
        """
        self._compression_format = compression_format

    @property
    def csv_properties(self):
        """Gets the csv_properties of this ShowStreamResponse.

        :return: The csv_properties of this ShowStreamResponse.
        :rtype: :class:`huaweicloudsdkdis.v2.CSVProperties`
        """
        return self._csv_properties

    @csv_properties.setter
    def csv_properties(self, csv_properties):
        """Sets the csv_properties of this ShowStreamResponse.

        :param csv_properties: The csv_properties of this ShowStreamResponse.
        :type csv_properties: :class:`huaweicloudsdkdis.v2.CSVProperties`
        """
        self._csv_properties = csv_properties

    @property
    def writable_partition_count(self):
        """Gets the writable_partition_count of this ShowStreamResponse.

        可写分区总数量（只包含ACTIVE状态的分区）。

        :return: The writable_partition_count of this ShowStreamResponse.
        :rtype: int
        """
        return self._writable_partition_count

    @writable_partition_count.setter
    def writable_partition_count(self, writable_partition_count):
        """Sets the writable_partition_count of this ShowStreamResponse.

        可写分区总数量（只包含ACTIVE状态的分区）。

        :param writable_partition_count: The writable_partition_count of this ShowStreamResponse.
        :type writable_partition_count: int
        """
        self._writable_partition_count = writable_partition_count

    @property
    def readable_partition_count(self):
        """Gets the readable_partition_count of this ShowStreamResponse.

        可读分区总数量（包含ACTIVE与DELETED状态的分区）。

        :return: The readable_partition_count of this ShowStreamResponse.
        :rtype: int
        """
        return self._readable_partition_count

    @readable_partition_count.setter
    def readable_partition_count(self, readable_partition_count):
        """Sets the readable_partition_count of this ShowStreamResponse.

        可读分区总数量（包含ACTIVE与DELETED状态的分区）。

        :param readable_partition_count: The readable_partition_count of this ShowStreamResponse.
        :type readable_partition_count: int
        """
        self._readable_partition_count = readable_partition_count

    @property
    def update_partition_counts(self):
        """Gets the update_partition_counts of this ShowStreamResponse.

        扩缩容操作记录列表。

        :return: The update_partition_counts of this ShowStreamResponse.
        :rtype: list[:class:`huaweicloudsdkdis.v2.UpdatePartitionCount`]
        """
        return self._update_partition_counts

    @update_partition_counts.setter
    def update_partition_counts(self, update_partition_counts):
        """Sets the update_partition_counts of this ShowStreamResponse.

        扩缩容操作记录列表。

        :param update_partition_counts: The update_partition_counts of this ShowStreamResponse.
        :type update_partition_counts: list[:class:`huaweicloudsdkdis.v2.UpdatePartitionCount`]
        """
        self._update_partition_counts = update_partition_counts

    @property
    def tags(self):
        """Gets the tags of this ShowStreamResponse.

        通道的标签列表。

        :return: The tags of this ShowStreamResponse.
        :rtype: list[:class:`huaweicloudsdkdis.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowStreamResponse.

        通道的标签列表。

        :param tags: The tags of this ShowStreamResponse.
        :type tags: list[:class:`huaweicloudsdkdis.v2.Tag`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        """Gets the sys_tags of this ShowStreamResponse.

        通道的企业项目。

        :return: The sys_tags of this ShowStreamResponse.
        :rtype: list[:class:`huaweicloudsdkdis.v2.SysTag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this ShowStreamResponse.

        通道的企业项目。

        :param sys_tags: The sys_tags of this ShowStreamResponse.
        :type sys_tags: list[:class:`huaweicloudsdkdis.v2.SysTag`]
        """
        self._sys_tags = sys_tags

    @property
    def auto_scale_enabled(self):
        """Gets the auto_scale_enabled of this ShowStreamResponse.

        是否开启自动扩缩容。  - true：开启自动扩缩容。 - false：关闭自动扩缩容。  默认不开启。

        :return: The auto_scale_enabled of this ShowStreamResponse.
        :rtype: bool
        """
        return self._auto_scale_enabled

    @auto_scale_enabled.setter
    def auto_scale_enabled(self, auto_scale_enabled):
        """Sets the auto_scale_enabled of this ShowStreamResponse.

        是否开启自动扩缩容。  - true：开启自动扩缩容。 - false：关闭自动扩缩容。  默认不开启。

        :param auto_scale_enabled: The auto_scale_enabled of this ShowStreamResponse.
        :type auto_scale_enabled: bool
        """
        self._auto_scale_enabled = auto_scale_enabled

    @property
    def auto_scale_min_partition_count(self):
        """Gets the auto_scale_min_partition_count of this ShowStreamResponse.

        当自动扩缩容启用时，自动缩容的最小分片数。

        :return: The auto_scale_min_partition_count of this ShowStreamResponse.
        :rtype: int
        """
        return self._auto_scale_min_partition_count

    @auto_scale_min_partition_count.setter
    def auto_scale_min_partition_count(self, auto_scale_min_partition_count):
        """Sets the auto_scale_min_partition_count of this ShowStreamResponse.

        当自动扩缩容启用时，自动缩容的最小分片数。

        :param auto_scale_min_partition_count: The auto_scale_min_partition_count of this ShowStreamResponse.
        :type auto_scale_min_partition_count: int
        """
        self._auto_scale_min_partition_count = auto_scale_min_partition_count

    @property
    def auto_scale_max_partition_count(self):
        """Gets the auto_scale_max_partition_count of this ShowStreamResponse.

        当自动扩缩容启用时，自动扩容的最大分片数。

        :return: The auto_scale_max_partition_count of this ShowStreamResponse.
        :rtype: int
        """
        return self._auto_scale_max_partition_count

    @auto_scale_max_partition_count.setter
    def auto_scale_max_partition_count(self, auto_scale_max_partition_count):
        """Sets the auto_scale_max_partition_count of this ShowStreamResponse.

        当自动扩缩容启用时，自动扩容的最大分片数。

        :param auto_scale_max_partition_count: The auto_scale_max_partition_count of this ShowStreamResponse.
        :type auto_scale_max_partition_count: int
        """
        self._auto_scale_max_partition_count = auto_scale_max_partition_count

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
        if not isinstance(other, ShowStreamResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
