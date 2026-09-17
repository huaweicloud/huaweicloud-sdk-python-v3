# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopDataInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'table_name': 'str',
        'file': 'float',
        'data': 'float',
        'free': 'float',
        'free_rate': 'float',
        'index': 'float',
        'rows_count': 'float',
        'time': 'float',
        'growth': 'float'
    }

    attribute_map = {
        'db_name': 'db_name',
        'table_name': 'table_name',
        'file': 'file',
        'data': 'data',
        'free': 'free',
        'free_rate': 'free_rate',
        'index': 'index',
        'rows_count': 'rows_count',
        'time': 'time',
        'growth': 'growth'
    }

    def __init__(self, db_name=None, table_name=None, file=None, data=None, free=None, free_rate=None, index=None, rows_count=None, time=None, growth=None):
        r"""TopDataInfo

        The model defined in huaweicloud sdk

        :param db_name: 库名
        :type db_name: str
        :param table_name: 表名
        :type table_name: str
        :param file: 物理文件大小，单位MB
        :type file: float
        :param data: 数据空间，单位MB
        :type data: float
        :param free: 碎片空间，单位MB
        :type free: float
        :param free_rate: 碎片率
        :type free_rate: float
        :param index: 索引空间，单位MB
        :type index: float
        :param rows_count: 行数
        :type rows_count: float
        :param time: 采集时间（Unix timestamp），单位：毫秒
        :type time: float
        :param growth: 增长量，单位MB
        :type growth: float
        """
        
        

        self._db_name = None
        self._table_name = None
        self._file = None
        self._data = None
        self._free = None
        self._free_rate = None
        self._index = None
        self._rows_count = None
        self._time = None
        self._growth = None
        self.discriminator = None

        if db_name is not None:
            self.db_name = db_name
        if table_name is not None:
            self.table_name = table_name
        if file is not None:
            self.file = file
        if data is not None:
            self.data = data
        if free is not None:
            self.free = free
        if free_rate is not None:
            self.free_rate = free_rate
        if index is not None:
            self.index = index
        if rows_count is not None:
            self.rows_count = rows_count
        if time is not None:
            self.time = time
        if growth is not None:
            self.growth = growth

    @property
    def db_name(self):
        r"""Gets the db_name of this TopDataInfo.

        库名

        :return: The db_name of this TopDataInfo.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this TopDataInfo.

        库名

        :param db_name: The db_name of this TopDataInfo.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def table_name(self):
        r"""Gets the table_name of this TopDataInfo.

        表名

        :return: The table_name of this TopDataInfo.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this TopDataInfo.

        表名

        :param table_name: The table_name of this TopDataInfo.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def file(self):
        r"""Gets the file of this TopDataInfo.

        物理文件大小，单位MB

        :return: The file of this TopDataInfo.
        :rtype: float
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this TopDataInfo.

        物理文件大小，单位MB

        :param file: The file of this TopDataInfo.
        :type file: float
        """
        self._file = file

    @property
    def data(self):
        r"""Gets the data of this TopDataInfo.

        数据空间，单位MB

        :return: The data of this TopDataInfo.
        :rtype: float
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this TopDataInfo.

        数据空间，单位MB

        :param data: The data of this TopDataInfo.
        :type data: float
        """
        self._data = data

    @property
    def free(self):
        r"""Gets the free of this TopDataInfo.

        碎片空间，单位MB

        :return: The free of this TopDataInfo.
        :rtype: float
        """
        return self._free

    @free.setter
    def free(self, free):
        r"""Sets the free of this TopDataInfo.

        碎片空间，单位MB

        :param free: The free of this TopDataInfo.
        :type free: float
        """
        self._free = free

    @property
    def free_rate(self):
        r"""Gets the free_rate of this TopDataInfo.

        碎片率

        :return: The free_rate of this TopDataInfo.
        :rtype: float
        """
        return self._free_rate

    @free_rate.setter
    def free_rate(self, free_rate):
        r"""Sets the free_rate of this TopDataInfo.

        碎片率

        :param free_rate: The free_rate of this TopDataInfo.
        :type free_rate: float
        """
        self._free_rate = free_rate

    @property
    def index(self):
        r"""Gets the index of this TopDataInfo.

        索引空间，单位MB

        :return: The index of this TopDataInfo.
        :rtype: float
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this TopDataInfo.

        索引空间，单位MB

        :param index: The index of this TopDataInfo.
        :type index: float
        """
        self._index = index

    @property
    def rows_count(self):
        r"""Gets the rows_count of this TopDataInfo.

        行数

        :return: The rows_count of this TopDataInfo.
        :rtype: float
        """
        return self._rows_count

    @rows_count.setter
    def rows_count(self, rows_count):
        r"""Sets the rows_count of this TopDataInfo.

        行数

        :param rows_count: The rows_count of this TopDataInfo.
        :type rows_count: float
        """
        self._rows_count = rows_count

    @property
    def time(self):
        r"""Gets the time of this TopDataInfo.

        采集时间（Unix timestamp），单位：毫秒

        :return: The time of this TopDataInfo.
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this TopDataInfo.

        采集时间（Unix timestamp），单位：毫秒

        :param time: The time of this TopDataInfo.
        :type time: float
        """
        self._time = time

    @property
    def growth(self):
        r"""Gets the growth of this TopDataInfo.

        增长量，单位MB

        :return: The growth of this TopDataInfo.
        :rtype: float
        """
        return self._growth

    @growth.setter
    def growth(self, growth):
        r"""Sets the growth of this TopDataInfo.

        增长量，单位MB

        :param growth: The growth of this TopDataInfo.
        :type growth: float
        """
        self._growth = growth

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
        if not isinstance(other, TopDataInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
