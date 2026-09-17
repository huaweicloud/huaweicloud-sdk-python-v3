# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndexUsageDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_name': 'str',
        'index_name': 'str',
        'ix_type_desc': 'str',
        'fragmentation_percentage': 'float',
        'index_size_mb': 'float',
        'maintenance_operation': 'str',
        'page_count': 'int',
        'ix_seek_count': 'int',
        'ix_scan_count': 'int',
        'ix_key_lookup_count': 'int',
        'ix_update_count': 'int',
        'seek_percentage': 'float',
        'scan_percentage': 'float',
        'key_lookup_percentage': 'float',
        'update_percentage': 'float',
        'is_primary_key': 'bool',
        'is_disabled': 'bool',
        'column_list': 'str',
        'fill_factor': 'str',
        'create_date': 'int',
        'stats_last_updated': 'int'
    }

    attribute_map = {
        'table_name': 'table_name',
        'index_name': 'index_name',
        'ix_type_desc': 'ix_type_desc',
        'fragmentation_percentage': 'fragmentation_percentage',
        'index_size_mb': 'index_size_mb',
        'maintenance_operation': 'maintenance_operation',
        'page_count': 'page_count',
        'ix_seek_count': 'ix_seek_count',
        'ix_scan_count': 'ix_scan_count',
        'ix_key_lookup_count': 'ix_key_lookup_count',
        'ix_update_count': 'ix_update_count',
        'seek_percentage': 'seek_percentage',
        'scan_percentage': 'scan_percentage',
        'key_lookup_percentage': 'key_lookup_percentage',
        'update_percentage': 'update_percentage',
        'is_primary_key': 'is_primary_key',
        'is_disabled': 'is_disabled',
        'column_list': 'column_list',
        'fill_factor': 'fill_factor',
        'create_date': 'create_date',
        'stats_last_updated': 'stats_last_updated'
    }

    def __init__(self, table_name=None, index_name=None, ix_type_desc=None, fragmentation_percentage=None, index_size_mb=None, maintenance_operation=None, page_count=None, ix_seek_count=None, ix_scan_count=None, ix_key_lookup_count=None, ix_update_count=None, seek_percentage=None, scan_percentage=None, key_lookup_percentage=None, update_percentage=None, is_primary_key=None, is_disabled=None, column_list=None, fill_factor=None, create_date=None, stats_last_updated=None):
        r"""IndexUsageDetail

        The model defined in huaweicloud sdk

        :param table_name: 表名称
        :type table_name: str
        :param index_name: 索引名称
        :type index_name: str
        :param ix_type_desc: 索引类型描述
        :type ix_type_desc: str
        :param fragmentation_percentage: 碎片率
        :type fragmentation_percentage: float
        :param index_size_mb: 索引占用的空间大小(MB)
        :type index_size_mb: float
        :param maintenance_operation: 维护操作
        :type maintenance_operation: str
        :param page_count: 索引占用的空间页数
        :type page_count: int
        :param ix_seek_count: 通过用户查询执行的搜索次数
        :type ix_seek_count: int
        :param ix_scan_count: 未使用索引的用户查询的扫描数
        :type ix_scan_count: int
        :param ix_key_lookup_count: 由用户查询执行的书签查找次数
        :type ix_key_lookup_count: int
        :param ix_update_count: 通过用户查询执行的更新次数
        :type ix_update_count: int
        :param seek_percentage: 查找百分比
        :type seek_percentage: float
        :param scan_percentage: 扫描百分比
        :type scan_percentage: float
        :param key_lookup_percentage: 书签查找百分比
        :type key_lookup_percentage: float
        :param update_percentage: 更新百分比
        :type update_percentage: float
        :param is_primary_key: 索引是否是主键
        :type is_primary_key: bool
        :param is_disabled: 索引是否被禁用
        :type is_disabled: bool
        :param column_list: 列
        :type column_list: str
        :param fill_factor: 填充因子
        :type fill_factor: str
        :param create_date: 创建时间
        :type create_date: int
        :param stats_last_updated: 统计信息更新时间
        :type stats_last_updated: int
        """
        
        

        self._table_name = None
        self._index_name = None
        self._ix_type_desc = None
        self._fragmentation_percentage = None
        self._index_size_mb = None
        self._maintenance_operation = None
        self._page_count = None
        self._ix_seek_count = None
        self._ix_scan_count = None
        self._ix_key_lookup_count = None
        self._ix_update_count = None
        self._seek_percentage = None
        self._scan_percentage = None
        self._key_lookup_percentage = None
        self._update_percentage = None
        self._is_primary_key = None
        self._is_disabled = None
        self._column_list = None
        self._fill_factor = None
        self._create_date = None
        self._stats_last_updated = None
        self.discriminator = None

        if table_name is not None:
            self.table_name = table_name
        if index_name is not None:
            self.index_name = index_name
        if ix_type_desc is not None:
            self.ix_type_desc = ix_type_desc
        if fragmentation_percentage is not None:
            self.fragmentation_percentage = fragmentation_percentage
        if index_size_mb is not None:
            self.index_size_mb = index_size_mb
        if maintenance_operation is not None:
            self.maintenance_operation = maintenance_operation
        if page_count is not None:
            self.page_count = page_count
        if ix_seek_count is not None:
            self.ix_seek_count = ix_seek_count
        if ix_scan_count is not None:
            self.ix_scan_count = ix_scan_count
        if ix_key_lookup_count is not None:
            self.ix_key_lookup_count = ix_key_lookup_count
        if ix_update_count is not None:
            self.ix_update_count = ix_update_count
        if seek_percentage is not None:
            self.seek_percentage = seek_percentage
        if scan_percentage is not None:
            self.scan_percentage = scan_percentage
        if key_lookup_percentage is not None:
            self.key_lookup_percentage = key_lookup_percentage
        if update_percentage is not None:
            self.update_percentage = update_percentage
        if is_primary_key is not None:
            self.is_primary_key = is_primary_key
        if is_disabled is not None:
            self.is_disabled = is_disabled
        if column_list is not None:
            self.column_list = column_list
        if fill_factor is not None:
            self.fill_factor = fill_factor
        if create_date is not None:
            self.create_date = create_date
        if stats_last_updated is not None:
            self.stats_last_updated = stats_last_updated

    @property
    def table_name(self):
        r"""Gets the table_name of this IndexUsageDetail.

        表名称

        :return: The table_name of this IndexUsageDetail.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this IndexUsageDetail.

        表名称

        :param table_name: The table_name of this IndexUsageDetail.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def index_name(self):
        r"""Gets the index_name of this IndexUsageDetail.

        索引名称

        :return: The index_name of this IndexUsageDetail.
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        r"""Sets the index_name of this IndexUsageDetail.

        索引名称

        :param index_name: The index_name of this IndexUsageDetail.
        :type index_name: str
        """
        self._index_name = index_name

    @property
    def ix_type_desc(self):
        r"""Gets the ix_type_desc of this IndexUsageDetail.

        索引类型描述

        :return: The ix_type_desc of this IndexUsageDetail.
        :rtype: str
        """
        return self._ix_type_desc

    @ix_type_desc.setter
    def ix_type_desc(self, ix_type_desc):
        r"""Sets the ix_type_desc of this IndexUsageDetail.

        索引类型描述

        :param ix_type_desc: The ix_type_desc of this IndexUsageDetail.
        :type ix_type_desc: str
        """
        self._ix_type_desc = ix_type_desc

    @property
    def fragmentation_percentage(self):
        r"""Gets the fragmentation_percentage of this IndexUsageDetail.

        碎片率

        :return: The fragmentation_percentage of this IndexUsageDetail.
        :rtype: float
        """
        return self._fragmentation_percentage

    @fragmentation_percentage.setter
    def fragmentation_percentage(self, fragmentation_percentage):
        r"""Sets the fragmentation_percentage of this IndexUsageDetail.

        碎片率

        :param fragmentation_percentage: The fragmentation_percentage of this IndexUsageDetail.
        :type fragmentation_percentage: float
        """
        self._fragmentation_percentage = fragmentation_percentage

    @property
    def index_size_mb(self):
        r"""Gets the index_size_mb of this IndexUsageDetail.

        索引占用的空间大小(MB)

        :return: The index_size_mb of this IndexUsageDetail.
        :rtype: float
        """
        return self._index_size_mb

    @index_size_mb.setter
    def index_size_mb(self, index_size_mb):
        r"""Sets the index_size_mb of this IndexUsageDetail.

        索引占用的空间大小(MB)

        :param index_size_mb: The index_size_mb of this IndexUsageDetail.
        :type index_size_mb: float
        """
        self._index_size_mb = index_size_mb

    @property
    def maintenance_operation(self):
        r"""Gets the maintenance_operation of this IndexUsageDetail.

        维护操作

        :return: The maintenance_operation of this IndexUsageDetail.
        :rtype: str
        """
        return self._maintenance_operation

    @maintenance_operation.setter
    def maintenance_operation(self, maintenance_operation):
        r"""Sets the maintenance_operation of this IndexUsageDetail.

        维护操作

        :param maintenance_operation: The maintenance_operation of this IndexUsageDetail.
        :type maintenance_operation: str
        """
        self._maintenance_operation = maintenance_operation

    @property
    def page_count(self):
        r"""Gets the page_count of this IndexUsageDetail.

        索引占用的空间页数

        :return: The page_count of this IndexUsageDetail.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        r"""Sets the page_count of this IndexUsageDetail.

        索引占用的空间页数

        :param page_count: The page_count of this IndexUsageDetail.
        :type page_count: int
        """
        self._page_count = page_count

    @property
    def ix_seek_count(self):
        r"""Gets the ix_seek_count of this IndexUsageDetail.

        通过用户查询执行的搜索次数

        :return: The ix_seek_count of this IndexUsageDetail.
        :rtype: int
        """
        return self._ix_seek_count

    @ix_seek_count.setter
    def ix_seek_count(self, ix_seek_count):
        r"""Sets the ix_seek_count of this IndexUsageDetail.

        通过用户查询执行的搜索次数

        :param ix_seek_count: The ix_seek_count of this IndexUsageDetail.
        :type ix_seek_count: int
        """
        self._ix_seek_count = ix_seek_count

    @property
    def ix_scan_count(self):
        r"""Gets the ix_scan_count of this IndexUsageDetail.

        未使用索引的用户查询的扫描数

        :return: The ix_scan_count of this IndexUsageDetail.
        :rtype: int
        """
        return self._ix_scan_count

    @ix_scan_count.setter
    def ix_scan_count(self, ix_scan_count):
        r"""Sets the ix_scan_count of this IndexUsageDetail.

        未使用索引的用户查询的扫描数

        :param ix_scan_count: The ix_scan_count of this IndexUsageDetail.
        :type ix_scan_count: int
        """
        self._ix_scan_count = ix_scan_count

    @property
    def ix_key_lookup_count(self):
        r"""Gets the ix_key_lookup_count of this IndexUsageDetail.

        由用户查询执行的书签查找次数

        :return: The ix_key_lookup_count of this IndexUsageDetail.
        :rtype: int
        """
        return self._ix_key_lookup_count

    @ix_key_lookup_count.setter
    def ix_key_lookup_count(self, ix_key_lookup_count):
        r"""Sets the ix_key_lookup_count of this IndexUsageDetail.

        由用户查询执行的书签查找次数

        :param ix_key_lookup_count: The ix_key_lookup_count of this IndexUsageDetail.
        :type ix_key_lookup_count: int
        """
        self._ix_key_lookup_count = ix_key_lookup_count

    @property
    def ix_update_count(self):
        r"""Gets the ix_update_count of this IndexUsageDetail.

        通过用户查询执行的更新次数

        :return: The ix_update_count of this IndexUsageDetail.
        :rtype: int
        """
        return self._ix_update_count

    @ix_update_count.setter
    def ix_update_count(self, ix_update_count):
        r"""Sets the ix_update_count of this IndexUsageDetail.

        通过用户查询执行的更新次数

        :param ix_update_count: The ix_update_count of this IndexUsageDetail.
        :type ix_update_count: int
        """
        self._ix_update_count = ix_update_count

    @property
    def seek_percentage(self):
        r"""Gets the seek_percentage of this IndexUsageDetail.

        查找百分比

        :return: The seek_percentage of this IndexUsageDetail.
        :rtype: float
        """
        return self._seek_percentage

    @seek_percentage.setter
    def seek_percentage(self, seek_percentage):
        r"""Sets the seek_percentage of this IndexUsageDetail.

        查找百分比

        :param seek_percentage: The seek_percentage of this IndexUsageDetail.
        :type seek_percentage: float
        """
        self._seek_percentage = seek_percentage

    @property
    def scan_percentage(self):
        r"""Gets the scan_percentage of this IndexUsageDetail.

        扫描百分比

        :return: The scan_percentage of this IndexUsageDetail.
        :rtype: float
        """
        return self._scan_percentage

    @scan_percentage.setter
    def scan_percentage(self, scan_percentage):
        r"""Sets the scan_percentage of this IndexUsageDetail.

        扫描百分比

        :param scan_percentage: The scan_percentage of this IndexUsageDetail.
        :type scan_percentage: float
        """
        self._scan_percentage = scan_percentage

    @property
    def key_lookup_percentage(self):
        r"""Gets the key_lookup_percentage of this IndexUsageDetail.

        书签查找百分比

        :return: The key_lookup_percentage of this IndexUsageDetail.
        :rtype: float
        """
        return self._key_lookup_percentage

    @key_lookup_percentage.setter
    def key_lookup_percentage(self, key_lookup_percentage):
        r"""Sets the key_lookup_percentage of this IndexUsageDetail.

        书签查找百分比

        :param key_lookup_percentage: The key_lookup_percentage of this IndexUsageDetail.
        :type key_lookup_percentage: float
        """
        self._key_lookup_percentage = key_lookup_percentage

    @property
    def update_percentage(self):
        r"""Gets the update_percentage of this IndexUsageDetail.

        更新百分比

        :return: The update_percentage of this IndexUsageDetail.
        :rtype: float
        """
        return self._update_percentage

    @update_percentage.setter
    def update_percentage(self, update_percentage):
        r"""Sets the update_percentage of this IndexUsageDetail.

        更新百分比

        :param update_percentage: The update_percentage of this IndexUsageDetail.
        :type update_percentage: float
        """
        self._update_percentage = update_percentage

    @property
    def is_primary_key(self):
        r"""Gets the is_primary_key of this IndexUsageDetail.

        索引是否是主键

        :return: The is_primary_key of this IndexUsageDetail.
        :rtype: bool
        """
        return self._is_primary_key

    @is_primary_key.setter
    def is_primary_key(self, is_primary_key):
        r"""Sets the is_primary_key of this IndexUsageDetail.

        索引是否是主键

        :param is_primary_key: The is_primary_key of this IndexUsageDetail.
        :type is_primary_key: bool
        """
        self._is_primary_key = is_primary_key

    @property
    def is_disabled(self):
        r"""Gets the is_disabled of this IndexUsageDetail.

        索引是否被禁用

        :return: The is_disabled of this IndexUsageDetail.
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        r"""Sets the is_disabled of this IndexUsageDetail.

        索引是否被禁用

        :param is_disabled: The is_disabled of this IndexUsageDetail.
        :type is_disabled: bool
        """
        self._is_disabled = is_disabled

    @property
    def column_list(self):
        r"""Gets the column_list of this IndexUsageDetail.

        列

        :return: The column_list of this IndexUsageDetail.
        :rtype: str
        """
        return self._column_list

    @column_list.setter
    def column_list(self, column_list):
        r"""Sets the column_list of this IndexUsageDetail.

        列

        :param column_list: The column_list of this IndexUsageDetail.
        :type column_list: str
        """
        self._column_list = column_list

    @property
    def fill_factor(self):
        r"""Gets the fill_factor of this IndexUsageDetail.

        填充因子

        :return: The fill_factor of this IndexUsageDetail.
        :rtype: str
        """
        return self._fill_factor

    @fill_factor.setter
    def fill_factor(self, fill_factor):
        r"""Sets the fill_factor of this IndexUsageDetail.

        填充因子

        :param fill_factor: The fill_factor of this IndexUsageDetail.
        :type fill_factor: str
        """
        self._fill_factor = fill_factor

    @property
    def create_date(self):
        r"""Gets the create_date of this IndexUsageDetail.

        创建时间

        :return: The create_date of this IndexUsageDetail.
        :rtype: int
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        r"""Sets the create_date of this IndexUsageDetail.

        创建时间

        :param create_date: The create_date of this IndexUsageDetail.
        :type create_date: int
        """
        self._create_date = create_date

    @property
    def stats_last_updated(self):
        r"""Gets the stats_last_updated of this IndexUsageDetail.

        统计信息更新时间

        :return: The stats_last_updated of this IndexUsageDetail.
        :rtype: int
        """
        return self._stats_last_updated

    @stats_last_updated.setter
    def stats_last_updated(self, stats_last_updated):
        r"""Sets the stats_last_updated of this IndexUsageDetail.

        统计信息更新时间

        :param stats_last_updated: The stats_last_updated of this IndexUsageDetail.
        :type stats_last_updated: int
        """
        self._stats_last_updated = stats_last_updated

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
        if not isinstance(other, IndexUsageDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
