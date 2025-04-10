# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StreamInfo:

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
        'retention_period': 'int',
        'status': 'str',
        'stream_type': 'str',
        'data_type': 'str',
        'partition_count': 'int',
        'auto_scale_enabled': 'bool',
        'auto_scale_min_partition_count': 'int',
        'auto_scale_max_partition_count': 'int',
        'tags': 'list[Tag]',
        'sys_tags': 'list[SysTag]'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'create_time': 'create_time',
        'retention_period': 'retention_period',
        'status': 'status',
        'stream_type': 'stream_type',
        'data_type': 'data_type',
        'partition_count': 'partition_count',
        'auto_scale_enabled': 'auto_scale_enabled',
        'auto_scale_min_partition_count': 'auto_scale_min_partition_count',
        'auto_scale_max_partition_count': 'auto_scale_max_partition_count',
        'tags': 'tags',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, stream_name=None, create_time=None, retention_period=None, status=None, stream_type=None, data_type=None, partition_count=None, auto_scale_enabled=None, auto_scale_min_partition_count=None, auto_scale_max_partition_count=None, tags=None, sys_tags=None):
        r"""StreamInfo

        The model defined in huaweicloud sdk

        :param stream_name: 通道名称。
        :type stream_name: str
        :param create_time: 通道创建的时间，13位时间戳。
        :type create_time: int
        :param retention_period: 数据保留时长，单位是小时。
        :type retention_period: int
        :param status: 通道的当前状态。  - CREATING：创建中 - RUNNING：运行中 - TERMINATING：删除中 - TERMINATED：已删除
        :type status: str
        :param stream_type: 通道类型。  - COMMON：普通通道，表示1MB带宽。 - ADVANCED：高级通道，表示5MB带宽。
        :type stream_type: str
        :param data_type: 源数据类型。  - BLOB：存储在数据库管理系统中的一组二进制数据。 - JSON：一种开放的文件格式，以易读的文字为基础，用来传输由属性值或者序列性的值组成的数据对象。 - CSV：纯文本形式存储的表格数据，分隔符默认采用逗号。  缺省值：BLOB。
        :type data_type: str
        :param partition_count: 分区数量。  分区是DIS数据通道的基本吞吐量单位。
        :type partition_count: int
        :param auto_scale_enabled: 是否开启自动扩缩容。  - true：开启自动扩缩容。 - false：关闭自动扩缩容。  默认不开启。
        :type auto_scale_enabled: bool
        :param auto_scale_min_partition_count: 当自动扩缩容启用时，自动缩容的最小分片数。
        :type auto_scale_min_partition_count: int
        :param auto_scale_max_partition_count: 当自动扩缩容启用时，自动扩容的最大分片数。
        :type auto_scale_max_partition_count: int
        :param tags: 通道标签列表。
        :type tags: list[:class:`huaweicloudsdkdis.v2.Tag`]
        :param sys_tags: 通道企业项目列表。
        :type sys_tags: list[:class:`huaweicloudsdkdis.v2.SysTag`]
        """
        
        

        self._stream_name = None
        self._create_time = None
        self._retention_period = None
        self._status = None
        self._stream_type = None
        self._data_type = None
        self._partition_count = None
        self._auto_scale_enabled = None
        self._auto_scale_min_partition_count = None
        self._auto_scale_max_partition_count = None
        self._tags = None
        self._sys_tags = None
        self.discriminator = None

        if stream_name is not None:
            self.stream_name = stream_name
        if create_time is not None:
            self.create_time = create_time
        if retention_period is not None:
            self.retention_period = retention_period
        if status is not None:
            self.status = status
        if stream_type is not None:
            self.stream_type = stream_type
        if data_type is not None:
            self.data_type = data_type
        if partition_count is not None:
            self.partition_count = partition_count
        if auto_scale_enabled is not None:
            self.auto_scale_enabled = auto_scale_enabled
        if auto_scale_min_partition_count is not None:
            self.auto_scale_min_partition_count = auto_scale_min_partition_count
        if auto_scale_max_partition_count is not None:
            self.auto_scale_max_partition_count = auto_scale_max_partition_count
        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags

    @property
    def stream_name(self):
        r"""Gets the stream_name of this StreamInfo.

        通道名称。

        :return: The stream_name of this StreamInfo.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this StreamInfo.

        通道名称。

        :param stream_name: The stream_name of this StreamInfo.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def create_time(self):
        r"""Gets the create_time of this StreamInfo.

        通道创建的时间，13位时间戳。

        :return: The create_time of this StreamInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this StreamInfo.

        通道创建的时间，13位时间戳。

        :param create_time: The create_time of this StreamInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def retention_period(self):
        r"""Gets the retention_period of this StreamInfo.

        数据保留时长，单位是小时。

        :return: The retention_period of this StreamInfo.
        :rtype: int
        """
        return self._retention_period

    @retention_period.setter
    def retention_period(self, retention_period):
        r"""Sets the retention_period of this StreamInfo.

        数据保留时长，单位是小时。

        :param retention_period: The retention_period of this StreamInfo.
        :type retention_period: int
        """
        self._retention_period = retention_period

    @property
    def status(self):
        r"""Gets the status of this StreamInfo.

        通道的当前状态。  - CREATING：创建中 - RUNNING：运行中 - TERMINATING：删除中 - TERMINATED：已删除

        :return: The status of this StreamInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StreamInfo.

        通道的当前状态。  - CREATING：创建中 - RUNNING：运行中 - TERMINATING：删除中 - TERMINATED：已删除

        :param status: The status of this StreamInfo.
        :type status: str
        """
        self._status = status

    @property
    def stream_type(self):
        r"""Gets the stream_type of this StreamInfo.

        通道类型。  - COMMON：普通通道，表示1MB带宽。 - ADVANCED：高级通道，表示5MB带宽。

        :return: The stream_type of this StreamInfo.
        :rtype: str
        """
        return self._stream_type

    @stream_type.setter
    def stream_type(self, stream_type):
        r"""Sets the stream_type of this StreamInfo.

        通道类型。  - COMMON：普通通道，表示1MB带宽。 - ADVANCED：高级通道，表示5MB带宽。

        :param stream_type: The stream_type of this StreamInfo.
        :type stream_type: str
        """
        self._stream_type = stream_type

    @property
    def data_type(self):
        r"""Gets the data_type of this StreamInfo.

        源数据类型。  - BLOB：存储在数据库管理系统中的一组二进制数据。 - JSON：一种开放的文件格式，以易读的文字为基础，用来传输由属性值或者序列性的值组成的数据对象。 - CSV：纯文本形式存储的表格数据，分隔符默认采用逗号。  缺省值：BLOB。

        :return: The data_type of this StreamInfo.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this StreamInfo.

        源数据类型。  - BLOB：存储在数据库管理系统中的一组二进制数据。 - JSON：一种开放的文件格式，以易读的文字为基础，用来传输由属性值或者序列性的值组成的数据对象。 - CSV：纯文本形式存储的表格数据，分隔符默认采用逗号。  缺省值：BLOB。

        :param data_type: The data_type of this StreamInfo.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def partition_count(self):
        r"""Gets the partition_count of this StreamInfo.

        分区数量。  分区是DIS数据通道的基本吞吐量单位。

        :return: The partition_count of this StreamInfo.
        :rtype: int
        """
        return self._partition_count

    @partition_count.setter
    def partition_count(self, partition_count):
        r"""Sets the partition_count of this StreamInfo.

        分区数量。  分区是DIS数据通道的基本吞吐量单位。

        :param partition_count: The partition_count of this StreamInfo.
        :type partition_count: int
        """
        self._partition_count = partition_count

    @property
    def auto_scale_enabled(self):
        r"""Gets the auto_scale_enabled of this StreamInfo.

        是否开启自动扩缩容。  - true：开启自动扩缩容。 - false：关闭自动扩缩容。  默认不开启。

        :return: The auto_scale_enabled of this StreamInfo.
        :rtype: bool
        """
        return self._auto_scale_enabled

    @auto_scale_enabled.setter
    def auto_scale_enabled(self, auto_scale_enabled):
        r"""Sets the auto_scale_enabled of this StreamInfo.

        是否开启自动扩缩容。  - true：开启自动扩缩容。 - false：关闭自动扩缩容。  默认不开启。

        :param auto_scale_enabled: The auto_scale_enabled of this StreamInfo.
        :type auto_scale_enabled: bool
        """
        self._auto_scale_enabled = auto_scale_enabled

    @property
    def auto_scale_min_partition_count(self):
        r"""Gets the auto_scale_min_partition_count of this StreamInfo.

        当自动扩缩容启用时，自动缩容的最小分片数。

        :return: The auto_scale_min_partition_count of this StreamInfo.
        :rtype: int
        """
        return self._auto_scale_min_partition_count

    @auto_scale_min_partition_count.setter
    def auto_scale_min_partition_count(self, auto_scale_min_partition_count):
        r"""Sets the auto_scale_min_partition_count of this StreamInfo.

        当自动扩缩容启用时，自动缩容的最小分片数。

        :param auto_scale_min_partition_count: The auto_scale_min_partition_count of this StreamInfo.
        :type auto_scale_min_partition_count: int
        """
        self._auto_scale_min_partition_count = auto_scale_min_partition_count

    @property
    def auto_scale_max_partition_count(self):
        r"""Gets the auto_scale_max_partition_count of this StreamInfo.

        当自动扩缩容启用时，自动扩容的最大分片数。

        :return: The auto_scale_max_partition_count of this StreamInfo.
        :rtype: int
        """
        return self._auto_scale_max_partition_count

    @auto_scale_max_partition_count.setter
    def auto_scale_max_partition_count(self, auto_scale_max_partition_count):
        r"""Sets the auto_scale_max_partition_count of this StreamInfo.

        当自动扩缩容启用时，自动扩容的最大分片数。

        :param auto_scale_max_partition_count: The auto_scale_max_partition_count of this StreamInfo.
        :type auto_scale_max_partition_count: int
        """
        self._auto_scale_max_partition_count = auto_scale_max_partition_count

    @property
    def tags(self):
        r"""Gets the tags of this StreamInfo.

        通道标签列表。

        :return: The tags of this StreamInfo.
        :rtype: list[:class:`huaweicloudsdkdis.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this StreamInfo.

        通道标签列表。

        :param tags: The tags of this StreamInfo.
        :type tags: list[:class:`huaweicloudsdkdis.v2.Tag`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this StreamInfo.

        通道企业项目列表。

        :return: The sys_tags of this StreamInfo.
        :rtype: list[:class:`huaweicloudsdkdis.v2.SysTag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this StreamInfo.

        通道企业项目列表。

        :param sys_tags: The sys_tags of this StreamInfo.
        :type sys_tags: list[:class:`huaweicloudsdkdis.v2.SysTag`]
        """
        self._sys_tags = sys_tags

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
        if not isinstance(other, StreamInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
