# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateStreamReq:

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
        'data_duration': 'int',
        'data_type': 'str',
        'data_schema': 'str',
        'auto_scale_enabled': 'bool',
        'auto_scale_min_partition_count': 'int',
        'auto_scale_max_partition_count': 'int'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'data_duration': 'data_duration',
        'data_type': 'data_type',
        'data_schema': 'data_schema',
        'auto_scale_enabled': 'auto_scale_enabled',
        'auto_scale_min_partition_count': 'auto_scale_min_partition_count',
        'auto_scale_max_partition_count': 'auto_scale_max_partition_count'
    }

    def __init__(self, stream_name=None, data_duration=None, data_type=None, data_schema=None, auto_scale_enabled=None, auto_scale_min_partition_count=None, auto_scale_max_partition_count=None):
        """UpdateStreamReq

        The model defined in huaweicloud sdk

        :param stream_name: 待更新的通道名称。
        :type stream_name: str
        :param data_duration: 数据保留时长。  取值范围：24~72。  单位：小时。  空表示使用缺省值。
        :type data_duration: int
        :param data_type: 源数据类型。  - BLOB：存储在数据库管理系统中的一组二进制数据。 - JSON：一种开放的文件格式，以易读的文字为基础，用来传输由属性值或者序列性的值组成的数据对象。 - CSV：纯文本形式存储的表格数据，分隔符默认采用逗号。  缺省值：BLOB。
        :type data_type: str
        :param data_schema: 用于描述用户JSON、CSV格式的源数据结构，采用Avro Schema的语法描述。
        :type data_schema: str
        :param auto_scale_enabled: 是否开启自动扩缩容。  - true：开启自动扩缩容。 - false：关闭自动扩缩容。  默认不开启。
        :type auto_scale_enabled: bool
        :param auto_scale_min_partition_count: 当自动扩缩容启用时，自动缩容的最小分片数。
        :type auto_scale_min_partition_count: int
        :param auto_scale_max_partition_count: 当自动扩缩容启用时，自动扩容的最大分片数。
        :type auto_scale_max_partition_count: int
        """
        
        

        self._stream_name = None
        self._data_duration = None
        self._data_type = None
        self._data_schema = None
        self._auto_scale_enabled = None
        self._auto_scale_min_partition_count = None
        self._auto_scale_max_partition_count = None
        self.discriminator = None

        self.stream_name = stream_name
        if data_duration is not None:
            self.data_duration = data_duration
        if data_type is not None:
            self.data_type = data_type
        if data_schema is not None:
            self.data_schema = data_schema
        if auto_scale_enabled is not None:
            self.auto_scale_enabled = auto_scale_enabled
        if auto_scale_min_partition_count is not None:
            self.auto_scale_min_partition_count = auto_scale_min_partition_count
        if auto_scale_max_partition_count is not None:
            self.auto_scale_max_partition_count = auto_scale_max_partition_count

    @property
    def stream_name(self):
        """Gets the stream_name of this UpdateStreamReq.

        待更新的通道名称。

        :return: The stream_name of this UpdateStreamReq.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this UpdateStreamReq.

        待更新的通道名称。

        :param stream_name: The stream_name of this UpdateStreamReq.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def data_duration(self):
        """Gets the data_duration of this UpdateStreamReq.

        数据保留时长。  取值范围：24~72。  单位：小时。  空表示使用缺省值。

        :return: The data_duration of this UpdateStreamReq.
        :rtype: int
        """
        return self._data_duration

    @data_duration.setter
    def data_duration(self, data_duration):
        """Sets the data_duration of this UpdateStreamReq.

        数据保留时长。  取值范围：24~72。  单位：小时。  空表示使用缺省值。

        :param data_duration: The data_duration of this UpdateStreamReq.
        :type data_duration: int
        """
        self._data_duration = data_duration

    @property
    def data_type(self):
        """Gets the data_type of this UpdateStreamReq.

        源数据类型。  - BLOB：存储在数据库管理系统中的一组二进制数据。 - JSON：一种开放的文件格式，以易读的文字为基础，用来传输由属性值或者序列性的值组成的数据对象。 - CSV：纯文本形式存储的表格数据，分隔符默认采用逗号。  缺省值：BLOB。

        :return: The data_type of this UpdateStreamReq.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this UpdateStreamReq.

        源数据类型。  - BLOB：存储在数据库管理系统中的一组二进制数据。 - JSON：一种开放的文件格式，以易读的文字为基础，用来传输由属性值或者序列性的值组成的数据对象。 - CSV：纯文本形式存储的表格数据，分隔符默认采用逗号。  缺省值：BLOB。

        :param data_type: The data_type of this UpdateStreamReq.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def data_schema(self):
        """Gets the data_schema of this UpdateStreamReq.

        用于描述用户JSON、CSV格式的源数据结构，采用Avro Schema的语法描述。

        :return: The data_schema of this UpdateStreamReq.
        :rtype: str
        """
        return self._data_schema

    @data_schema.setter
    def data_schema(self, data_schema):
        """Sets the data_schema of this UpdateStreamReq.

        用于描述用户JSON、CSV格式的源数据结构，采用Avro Schema的语法描述。

        :param data_schema: The data_schema of this UpdateStreamReq.
        :type data_schema: str
        """
        self._data_schema = data_schema

    @property
    def auto_scale_enabled(self):
        """Gets the auto_scale_enabled of this UpdateStreamReq.

        是否开启自动扩缩容。  - true：开启自动扩缩容。 - false：关闭自动扩缩容。  默认不开启。

        :return: The auto_scale_enabled of this UpdateStreamReq.
        :rtype: bool
        """
        return self._auto_scale_enabled

    @auto_scale_enabled.setter
    def auto_scale_enabled(self, auto_scale_enabled):
        """Sets the auto_scale_enabled of this UpdateStreamReq.

        是否开启自动扩缩容。  - true：开启自动扩缩容。 - false：关闭自动扩缩容。  默认不开启。

        :param auto_scale_enabled: The auto_scale_enabled of this UpdateStreamReq.
        :type auto_scale_enabled: bool
        """
        self._auto_scale_enabled = auto_scale_enabled

    @property
    def auto_scale_min_partition_count(self):
        """Gets the auto_scale_min_partition_count of this UpdateStreamReq.

        当自动扩缩容启用时，自动缩容的最小分片数。

        :return: The auto_scale_min_partition_count of this UpdateStreamReq.
        :rtype: int
        """
        return self._auto_scale_min_partition_count

    @auto_scale_min_partition_count.setter
    def auto_scale_min_partition_count(self, auto_scale_min_partition_count):
        """Sets the auto_scale_min_partition_count of this UpdateStreamReq.

        当自动扩缩容启用时，自动缩容的最小分片数。

        :param auto_scale_min_partition_count: The auto_scale_min_partition_count of this UpdateStreamReq.
        :type auto_scale_min_partition_count: int
        """
        self._auto_scale_min_partition_count = auto_scale_min_partition_count

    @property
    def auto_scale_max_partition_count(self):
        """Gets the auto_scale_max_partition_count of this UpdateStreamReq.

        当自动扩缩容启用时，自动扩容的最大分片数。

        :return: The auto_scale_max_partition_count of this UpdateStreamReq.
        :rtype: int
        """
        return self._auto_scale_max_partition_count

    @auto_scale_max_partition_count.setter
    def auto_scale_max_partition_count(self, auto_scale_max_partition_count):
        """Sets the auto_scale_max_partition_count of this UpdateStreamReq.

        当自动扩缩容启用时，自动扩容的最大分片数。

        :param auto_scale_max_partition_count: The auto_scale_max_partition_count of this UpdateStreamReq.
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
        if not isinstance(other, UpdateStreamReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
