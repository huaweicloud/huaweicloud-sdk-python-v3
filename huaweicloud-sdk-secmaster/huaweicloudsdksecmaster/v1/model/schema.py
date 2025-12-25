# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Schema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'columns': 'list[SchemaColumns]',
        'partition': 'list[str]',
        'primary_key': 'list[str]',
        'time_filter': 'str',
        'watermark_column': 'str',
        'watermark_interval': 'float'
    }

    attribute_map = {
        'columns': 'columns',
        'partition': 'partition',
        'primary_key': 'primary_key',
        'time_filter': 'time_filter',
        'watermark_column': 'watermark_column',
        'watermark_interval': 'watermark_interval'
    }

    def __init__(self, columns=None, partition=None, primary_key=None, time_filter=None, watermark_column=None, watermark_interval=None):
        r"""Schema

        The model defined in huaweicloud sdk

        :param columns: 列
        :type columns: list[:class:`huaweicloudsdksecmaster.v1.SchemaColumns`]
        :param partition: 分区
        :type partition: list[str]
        :param primary_key: 主键
        :type primary_key: list[str]
        :param time_filter: 时间过滤列
        :type time_filter: str
        :param watermark_column: 水印列
        :type watermark_column: str
        :param watermark_interval: 水印间隔
        :type watermark_interval: float
        """
        
        

        self._columns = None
        self._partition = None
        self._primary_key = None
        self._time_filter = None
        self._watermark_column = None
        self._watermark_interval = None
        self.discriminator = None

        if columns is not None:
            self.columns = columns
        if partition is not None:
            self.partition = partition
        if primary_key is not None:
            self.primary_key = primary_key
        if time_filter is not None:
            self.time_filter = time_filter
        if watermark_column is not None:
            self.watermark_column = watermark_column
        if watermark_interval is not None:
            self.watermark_interval = watermark_interval

    @property
    def columns(self):
        r"""Gets the columns of this Schema.

        列

        :return: The columns of this Schema.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.SchemaColumns`]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        r"""Sets the columns of this Schema.

        列

        :param columns: The columns of this Schema.
        :type columns: list[:class:`huaweicloudsdksecmaster.v1.SchemaColumns`]
        """
        self._columns = columns

    @property
    def partition(self):
        r"""Gets the partition of this Schema.

        分区

        :return: The partition of this Schema.
        :rtype: list[str]
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this Schema.

        分区

        :param partition: The partition of this Schema.
        :type partition: list[str]
        """
        self._partition = partition

    @property
    def primary_key(self):
        r"""Gets the primary_key of this Schema.

        主键

        :return: The primary_key of this Schema.
        :rtype: list[str]
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        r"""Sets the primary_key of this Schema.

        主键

        :param primary_key: The primary_key of this Schema.
        :type primary_key: list[str]
        """
        self._primary_key = primary_key

    @property
    def time_filter(self):
        r"""Gets the time_filter of this Schema.

        时间过滤列

        :return: The time_filter of this Schema.
        :rtype: str
        """
        return self._time_filter

    @time_filter.setter
    def time_filter(self, time_filter):
        r"""Sets the time_filter of this Schema.

        时间过滤列

        :param time_filter: The time_filter of this Schema.
        :type time_filter: str
        """
        self._time_filter = time_filter

    @property
    def watermark_column(self):
        r"""Gets the watermark_column of this Schema.

        水印列

        :return: The watermark_column of this Schema.
        :rtype: str
        """
        return self._watermark_column

    @watermark_column.setter
    def watermark_column(self, watermark_column):
        r"""Sets the watermark_column of this Schema.

        水印列

        :param watermark_column: The watermark_column of this Schema.
        :type watermark_column: str
        """
        self._watermark_column = watermark_column

    @property
    def watermark_interval(self):
        r"""Gets the watermark_interval of this Schema.

        水印间隔

        :return: The watermark_interval of this Schema.
        :rtype: float
        """
        return self._watermark_interval

    @watermark_interval.setter
    def watermark_interval(self, watermark_interval):
        r"""Sets the watermark_interval of this Schema.

        水印间隔

        :param watermark_interval: The watermark_interval of this Schema.
        :type watermark_interval: float
        """
        self._watermark_interval = watermark_interval

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
        if not isinstance(other, Schema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
