# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableSchemaDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'columns': 'list[IsapTableColumnDto]',
        'primary_key_list': 'list[str]',
        'partition': 'list[str]',
        'watermark_column': 'str',
        'watermark_interval': 'float',
        'time_filter': 'str',
        'display_setting': 'list[IsapTableColumnDisplaySettingDto]',
        'column_tree_root': 'IsapTableColumnTreeNodeTableColumnDto',
        'primary_key': 'list[str]',
        'partition_key': 'str'
    }

    attribute_map = {
        'columns': 'columns',
        'primary_key_list': 'primary_key_list',
        'partition': 'partition',
        'watermark_column': 'watermark_column',
        'watermark_interval': 'watermark_interval',
        'time_filter': 'time_filter',
        'display_setting': 'display_setting',
        'column_tree_root': 'column_tree_root',
        'primary_key': 'primary_key',
        'partition_key': 'partition_key'
    }

    def __init__(self, columns=None, primary_key_list=None, partition=None, watermark_column=None, watermark_interval=None, time_filter=None, display_setting=None, column_tree_root=None, primary_key=None, partition_key=None):
        r"""TableSchemaDto

        The model defined in huaweicloud sdk

        :param columns: 表格列列表
        :type columns: list[:class:`huaweicloudsdksecmaster.v2.IsapTableColumnDto`]
        :param primary_key_list: 表主键列表
        :type primary_key_list: list[str]
        :param partition: 表分区列表
        :type partition: list[str]
        :param watermark_column: 表水位列
        :type watermark_column: str
        :param watermark_interval: 表水位延迟间隔
        :type watermark_interval: float
        :param time_filter: 表时间过滤列
        :type time_filter: str
        :param display_setting: 展示设置列表
        :type display_setting: list[:class:`huaweicloudsdksecmaster.v2.IsapTableColumnDisplaySettingDto`]
        :param column_tree_root: 
        :type column_tree_root: :class:`huaweicloudsdksecmaster.v2.IsapTableColumnTreeNodeTableColumnDto`
        :param primary_key: 表主键列表
        :type primary_key: list[str]
        :param partition_key: 分区键
        :type partition_key: str
        """
        
        

        self._columns = None
        self._primary_key_list = None
        self._partition = None
        self._watermark_column = None
        self._watermark_interval = None
        self._time_filter = None
        self._display_setting = None
        self._column_tree_root = None
        self._primary_key = None
        self._partition_key = None
        self.discriminator = None

        if columns is not None:
            self.columns = columns
        if primary_key_list is not None:
            self.primary_key_list = primary_key_list
        if partition is not None:
            self.partition = partition
        if watermark_column is not None:
            self.watermark_column = watermark_column
        if watermark_interval is not None:
            self.watermark_interval = watermark_interval
        if time_filter is not None:
            self.time_filter = time_filter
        if display_setting is not None:
            self.display_setting = display_setting
        if column_tree_root is not None:
            self.column_tree_root = column_tree_root
        if primary_key is not None:
            self.primary_key = primary_key
        if partition_key is not None:
            self.partition_key = partition_key

    @property
    def columns(self):
        r"""Gets the columns of this TableSchemaDto.

        表格列列表

        :return: The columns of this TableSchemaDto.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.IsapTableColumnDto`]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        r"""Sets the columns of this TableSchemaDto.

        表格列列表

        :param columns: The columns of this TableSchemaDto.
        :type columns: list[:class:`huaweicloudsdksecmaster.v2.IsapTableColumnDto`]
        """
        self._columns = columns

    @property
    def primary_key_list(self):
        r"""Gets the primary_key_list of this TableSchemaDto.

        表主键列表

        :return: The primary_key_list of this TableSchemaDto.
        :rtype: list[str]
        """
        return self._primary_key_list

    @primary_key_list.setter
    def primary_key_list(self, primary_key_list):
        r"""Sets the primary_key_list of this TableSchemaDto.

        表主键列表

        :param primary_key_list: The primary_key_list of this TableSchemaDto.
        :type primary_key_list: list[str]
        """
        self._primary_key_list = primary_key_list

    @property
    def partition(self):
        r"""Gets the partition of this TableSchemaDto.

        表分区列表

        :return: The partition of this TableSchemaDto.
        :rtype: list[str]
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this TableSchemaDto.

        表分区列表

        :param partition: The partition of this TableSchemaDto.
        :type partition: list[str]
        """
        self._partition = partition

    @property
    def watermark_column(self):
        r"""Gets the watermark_column of this TableSchemaDto.

        表水位列

        :return: The watermark_column of this TableSchemaDto.
        :rtype: str
        """
        return self._watermark_column

    @watermark_column.setter
    def watermark_column(self, watermark_column):
        r"""Sets the watermark_column of this TableSchemaDto.

        表水位列

        :param watermark_column: The watermark_column of this TableSchemaDto.
        :type watermark_column: str
        """
        self._watermark_column = watermark_column

    @property
    def watermark_interval(self):
        r"""Gets the watermark_interval of this TableSchemaDto.

        表水位延迟间隔

        :return: The watermark_interval of this TableSchemaDto.
        :rtype: float
        """
        return self._watermark_interval

    @watermark_interval.setter
    def watermark_interval(self, watermark_interval):
        r"""Sets the watermark_interval of this TableSchemaDto.

        表水位延迟间隔

        :param watermark_interval: The watermark_interval of this TableSchemaDto.
        :type watermark_interval: float
        """
        self._watermark_interval = watermark_interval

    @property
    def time_filter(self):
        r"""Gets the time_filter of this TableSchemaDto.

        表时间过滤列

        :return: The time_filter of this TableSchemaDto.
        :rtype: str
        """
        return self._time_filter

    @time_filter.setter
    def time_filter(self, time_filter):
        r"""Sets the time_filter of this TableSchemaDto.

        表时间过滤列

        :param time_filter: The time_filter of this TableSchemaDto.
        :type time_filter: str
        """
        self._time_filter = time_filter

    @property
    def display_setting(self):
        r"""Gets the display_setting of this TableSchemaDto.

        展示设置列表

        :return: The display_setting of this TableSchemaDto.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.IsapTableColumnDisplaySettingDto`]
        """
        return self._display_setting

    @display_setting.setter
    def display_setting(self, display_setting):
        r"""Sets the display_setting of this TableSchemaDto.

        展示设置列表

        :param display_setting: The display_setting of this TableSchemaDto.
        :type display_setting: list[:class:`huaweicloudsdksecmaster.v2.IsapTableColumnDisplaySettingDto`]
        """
        self._display_setting = display_setting

    @property
    def column_tree_root(self):
        r"""Gets the column_tree_root of this TableSchemaDto.

        :return: The column_tree_root of this TableSchemaDto.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IsapTableColumnTreeNodeTableColumnDto`
        """
        return self._column_tree_root

    @column_tree_root.setter
    def column_tree_root(self, column_tree_root):
        r"""Sets the column_tree_root of this TableSchemaDto.

        :param column_tree_root: The column_tree_root of this TableSchemaDto.
        :type column_tree_root: :class:`huaweicloudsdksecmaster.v2.IsapTableColumnTreeNodeTableColumnDto`
        """
        self._column_tree_root = column_tree_root

    @property
    def primary_key(self):
        r"""Gets the primary_key of this TableSchemaDto.

        表主键列表

        :return: The primary_key of this TableSchemaDto.
        :rtype: list[str]
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        r"""Sets the primary_key of this TableSchemaDto.

        表主键列表

        :param primary_key: The primary_key of this TableSchemaDto.
        :type primary_key: list[str]
        """
        self._primary_key = primary_key

    @property
    def partition_key(self):
        r"""Gets the partition_key of this TableSchemaDto.

        分区键

        :return: The partition_key of this TableSchemaDto.
        :rtype: str
        """
        return self._partition_key

    @partition_key.setter
    def partition_key(self, partition_key):
        r"""Sets the partition_key of this TableSchemaDto.

        分区键

        :param partition_key: The partition_key of this TableSchemaDto.
        :type partition_key: str
        """
        self._partition_key = partition_key

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
        if not isinstance(other, TableSchemaDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
