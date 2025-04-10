# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateStreamReq:

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
        'partition_count': 'int',
        'stream_type': 'str',
        'data_type': 'str',
        'data_duration': 'int',
        'auto_scale_enabled': 'bool',
        'auto_scale_min_partition_count': 'int',
        'auto_scale_max_partition_count': 'int',
        'data_schema': 'str',
        'csv_properties': 'CSVProperties',
        'compression_format': 'str',
        'tags': 'list[Tag]',
        'sys_tags': 'list[SysTag]'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'partition_count': 'partition_count',
        'stream_type': 'stream_type',
        'data_type': 'data_type',
        'data_duration': 'data_duration',
        'auto_scale_enabled': 'auto_scale_enabled',
        'auto_scale_min_partition_count': 'auto_scale_min_partition_count',
        'auto_scale_max_partition_count': 'auto_scale_max_partition_count',
        'data_schema': 'data_schema',
        'csv_properties': 'csv_properties',
        'compression_format': 'compression_format',
        'tags': 'tags',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, stream_name=None, partition_count=None, stream_type=None, data_type=None, data_duration=None, auto_scale_enabled=None, auto_scale_min_partition_count=None, auto_scale_max_partition_count=None, data_schema=None, csv_properties=None, compression_format=None, tags=None, sys_tags=None):
        r"""CreateStreamReq

        The model defined in huaweicloud sdk

        :param stream_name: 通道名称。  通道名称由字母、数字、下划线和中划线组成，长度为1～64字符。
        :type stream_name: str
        :param partition_count: 分区数量。  分区是DIS数据通道的基本吞吐量单位。
        :type partition_count: int
        :param stream_type: 通道类型。  - COMMON：普通通道，表示1MB带宽。 - ADVANCED：高级通道，表示5MB带宽。
        :type stream_type: str
        :param data_type: 源数据类型。  - BLOB：存储在数据库管理系统中的一组二进制数据。 - JSON：一种开放的文件格式，以易读的文字为基础，用来传输由属性值或者序列性的值组成的数据对象。 - CSV：纯文本形式存储的表格数据，分隔符默认采用逗号。  缺省值：BLOB。
        :type data_type: str
        :param data_duration: 数据保留时长。  取值范围：24~72。  单位：小时。  空表示使用缺省值。
        :type data_duration: int
        :param auto_scale_enabled: 是否开启自动扩缩容。  - true：开启自动扩缩容。 - false：关闭自动扩缩容。  默认不开启。
        :type auto_scale_enabled: bool
        :param auto_scale_min_partition_count: 当自动扩缩容启用时，自动缩容的最小分片数。
        :type auto_scale_min_partition_count: int
        :param auto_scale_max_partition_count: 当自动扩缩容启用时，自动扩容的最大分片数。
        :type auto_scale_max_partition_count: int
        :param data_schema: 用于描述用户JSON、CSV格式的源数据结构，采用Avro Schema的语法描述。
        :type data_schema: str
        :param csv_properties: 
        :type csv_properties: :class:`huaweicloudsdkdis.v2.CSVProperties`
        :param compression_format: 数据的压缩类型，目前支持：  - snappy  - gzip  - zip  默认不压缩。
        :type compression_format: str
        :param tags: 通道标签列表。
        :type tags: list[:class:`huaweicloudsdkdis.v2.Tag`]
        :param sys_tags: 通道企业项目列表。
        :type sys_tags: list[:class:`huaweicloudsdkdis.v2.SysTag`]
        """
        
        

        self._stream_name = None
        self._partition_count = None
        self._stream_type = None
        self._data_type = None
        self._data_duration = None
        self._auto_scale_enabled = None
        self._auto_scale_min_partition_count = None
        self._auto_scale_max_partition_count = None
        self._data_schema = None
        self._csv_properties = None
        self._compression_format = None
        self._tags = None
        self._sys_tags = None
        self.discriminator = None

        self.stream_name = stream_name
        self.partition_count = partition_count
        if stream_type is not None:
            self.stream_type = stream_type
        if data_type is not None:
            self.data_type = data_type
        if data_duration is not None:
            self.data_duration = data_duration
        if auto_scale_enabled is not None:
            self.auto_scale_enabled = auto_scale_enabled
        if auto_scale_min_partition_count is not None:
            self.auto_scale_min_partition_count = auto_scale_min_partition_count
        if auto_scale_max_partition_count is not None:
            self.auto_scale_max_partition_count = auto_scale_max_partition_count
        if data_schema is not None:
            self.data_schema = data_schema
        if csv_properties is not None:
            self.csv_properties = csv_properties
        if compression_format is not None:
            self.compression_format = compression_format
        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags

    @property
    def stream_name(self):
        r"""Gets the stream_name of this CreateStreamReq.

        通道名称。  通道名称由字母、数字、下划线和中划线组成，长度为1～64字符。

        :return: The stream_name of this CreateStreamReq.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this CreateStreamReq.

        通道名称。  通道名称由字母、数字、下划线和中划线组成，长度为1～64字符。

        :param stream_name: The stream_name of this CreateStreamReq.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def partition_count(self):
        r"""Gets the partition_count of this CreateStreamReq.

        分区数量。  分区是DIS数据通道的基本吞吐量单位。

        :return: The partition_count of this CreateStreamReq.
        :rtype: int
        """
        return self._partition_count

    @partition_count.setter
    def partition_count(self, partition_count):
        r"""Sets the partition_count of this CreateStreamReq.

        分区数量。  分区是DIS数据通道的基本吞吐量单位。

        :param partition_count: The partition_count of this CreateStreamReq.
        :type partition_count: int
        """
        self._partition_count = partition_count

    @property
    def stream_type(self):
        r"""Gets the stream_type of this CreateStreamReq.

        通道类型。  - COMMON：普通通道，表示1MB带宽。 - ADVANCED：高级通道，表示5MB带宽。

        :return: The stream_type of this CreateStreamReq.
        :rtype: str
        """
        return self._stream_type

    @stream_type.setter
    def stream_type(self, stream_type):
        r"""Sets the stream_type of this CreateStreamReq.

        通道类型。  - COMMON：普通通道，表示1MB带宽。 - ADVANCED：高级通道，表示5MB带宽。

        :param stream_type: The stream_type of this CreateStreamReq.
        :type stream_type: str
        """
        self._stream_type = stream_type

    @property
    def data_type(self):
        r"""Gets the data_type of this CreateStreamReq.

        源数据类型。  - BLOB：存储在数据库管理系统中的一组二进制数据。 - JSON：一种开放的文件格式，以易读的文字为基础，用来传输由属性值或者序列性的值组成的数据对象。 - CSV：纯文本形式存储的表格数据，分隔符默认采用逗号。  缺省值：BLOB。

        :return: The data_type of this CreateStreamReq.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this CreateStreamReq.

        源数据类型。  - BLOB：存储在数据库管理系统中的一组二进制数据。 - JSON：一种开放的文件格式，以易读的文字为基础，用来传输由属性值或者序列性的值组成的数据对象。 - CSV：纯文本形式存储的表格数据，分隔符默认采用逗号。  缺省值：BLOB。

        :param data_type: The data_type of this CreateStreamReq.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def data_duration(self):
        r"""Gets the data_duration of this CreateStreamReq.

        数据保留时长。  取值范围：24~72。  单位：小时。  空表示使用缺省值。

        :return: The data_duration of this CreateStreamReq.
        :rtype: int
        """
        return self._data_duration

    @data_duration.setter
    def data_duration(self, data_duration):
        r"""Sets the data_duration of this CreateStreamReq.

        数据保留时长。  取值范围：24~72。  单位：小时。  空表示使用缺省值。

        :param data_duration: The data_duration of this CreateStreamReq.
        :type data_duration: int
        """
        self._data_duration = data_duration

    @property
    def auto_scale_enabled(self):
        r"""Gets the auto_scale_enabled of this CreateStreamReq.

        是否开启自动扩缩容。  - true：开启自动扩缩容。 - false：关闭自动扩缩容。  默认不开启。

        :return: The auto_scale_enabled of this CreateStreamReq.
        :rtype: bool
        """
        return self._auto_scale_enabled

    @auto_scale_enabled.setter
    def auto_scale_enabled(self, auto_scale_enabled):
        r"""Sets the auto_scale_enabled of this CreateStreamReq.

        是否开启自动扩缩容。  - true：开启自动扩缩容。 - false：关闭自动扩缩容。  默认不开启。

        :param auto_scale_enabled: The auto_scale_enabled of this CreateStreamReq.
        :type auto_scale_enabled: bool
        """
        self._auto_scale_enabled = auto_scale_enabled

    @property
    def auto_scale_min_partition_count(self):
        r"""Gets the auto_scale_min_partition_count of this CreateStreamReq.

        当自动扩缩容启用时，自动缩容的最小分片数。

        :return: The auto_scale_min_partition_count of this CreateStreamReq.
        :rtype: int
        """
        return self._auto_scale_min_partition_count

    @auto_scale_min_partition_count.setter
    def auto_scale_min_partition_count(self, auto_scale_min_partition_count):
        r"""Sets the auto_scale_min_partition_count of this CreateStreamReq.

        当自动扩缩容启用时，自动缩容的最小分片数。

        :param auto_scale_min_partition_count: The auto_scale_min_partition_count of this CreateStreamReq.
        :type auto_scale_min_partition_count: int
        """
        self._auto_scale_min_partition_count = auto_scale_min_partition_count

    @property
    def auto_scale_max_partition_count(self):
        r"""Gets the auto_scale_max_partition_count of this CreateStreamReq.

        当自动扩缩容启用时，自动扩容的最大分片数。

        :return: The auto_scale_max_partition_count of this CreateStreamReq.
        :rtype: int
        """
        return self._auto_scale_max_partition_count

    @auto_scale_max_partition_count.setter
    def auto_scale_max_partition_count(self, auto_scale_max_partition_count):
        r"""Sets the auto_scale_max_partition_count of this CreateStreamReq.

        当自动扩缩容启用时，自动扩容的最大分片数。

        :param auto_scale_max_partition_count: The auto_scale_max_partition_count of this CreateStreamReq.
        :type auto_scale_max_partition_count: int
        """
        self._auto_scale_max_partition_count = auto_scale_max_partition_count

    @property
    def data_schema(self):
        r"""Gets the data_schema of this CreateStreamReq.

        用于描述用户JSON、CSV格式的源数据结构，采用Avro Schema的语法描述。

        :return: The data_schema of this CreateStreamReq.
        :rtype: str
        """
        return self._data_schema

    @data_schema.setter
    def data_schema(self, data_schema):
        r"""Sets the data_schema of this CreateStreamReq.

        用于描述用户JSON、CSV格式的源数据结构，采用Avro Schema的语法描述。

        :param data_schema: The data_schema of this CreateStreamReq.
        :type data_schema: str
        """
        self._data_schema = data_schema

    @property
    def csv_properties(self):
        r"""Gets the csv_properties of this CreateStreamReq.

        :return: The csv_properties of this CreateStreamReq.
        :rtype: :class:`huaweicloudsdkdis.v2.CSVProperties`
        """
        return self._csv_properties

    @csv_properties.setter
    def csv_properties(self, csv_properties):
        r"""Sets the csv_properties of this CreateStreamReq.

        :param csv_properties: The csv_properties of this CreateStreamReq.
        :type csv_properties: :class:`huaweicloudsdkdis.v2.CSVProperties`
        """
        self._csv_properties = csv_properties

    @property
    def compression_format(self):
        r"""Gets the compression_format of this CreateStreamReq.

        数据的压缩类型，目前支持：  - snappy  - gzip  - zip  默认不压缩。

        :return: The compression_format of this CreateStreamReq.
        :rtype: str
        """
        return self._compression_format

    @compression_format.setter
    def compression_format(self, compression_format):
        r"""Sets the compression_format of this CreateStreamReq.

        数据的压缩类型，目前支持：  - snappy  - gzip  - zip  默认不压缩。

        :param compression_format: The compression_format of this CreateStreamReq.
        :type compression_format: str
        """
        self._compression_format = compression_format

    @property
    def tags(self):
        r"""Gets the tags of this CreateStreamReq.

        通道标签列表。

        :return: The tags of this CreateStreamReq.
        :rtype: list[:class:`huaweicloudsdkdis.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateStreamReq.

        通道标签列表。

        :param tags: The tags of this CreateStreamReq.
        :type tags: list[:class:`huaweicloudsdkdis.v2.Tag`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this CreateStreamReq.

        通道企业项目列表。

        :return: The sys_tags of this CreateStreamReq.
        :rtype: list[:class:`huaweicloudsdkdis.v2.SysTag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this CreateStreamReq.

        通道企业项目列表。

        :param sys_tags: The sys_tags of this CreateStreamReq.
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
        if not isinstance(other, CreateStreamReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
