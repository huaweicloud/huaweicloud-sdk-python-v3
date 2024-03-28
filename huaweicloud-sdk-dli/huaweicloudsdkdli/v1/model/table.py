# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Table:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'int',
        'data_type': 'str',
        'data_location': 'str',
        'last_access_time': 'int',
        'location': 'str',
        'owner': 'str',
        'table_name': 'str',
        'table_size': 'int',
        'table_type': 'str',
        'partition_columns': 'list[str]',
        'page_size': 'int',
        'current_page': 'int'
    }

    attribute_map = {
        'create_time': 'create_time',
        'data_type': 'data_type',
        'data_location': 'data_location',
        'last_access_time': 'last_access_time',
        'location': 'location',
        'owner': 'owner',
        'table_name': 'table_name',
        'table_size': 'table_size',
        'table_type': 'table_type',
        'partition_columns': 'partition_columns',
        'page_size': 'page-size',
        'current_page': 'current-page'
    }

    def __init__(self, create_time=None, data_type=None, data_location=None, last_access_time=None, location=None, owner=None, table_name=None, table_size=None, table_type=None, partition_columns=None, page_size=None, current_page=None):
        """Table

        The model defined in huaweicloud sdk

        :param create_time: 表创建时间。是单位为“毫秒”的时间戳。
        :type create_time: int
        :param data_type: 所列OBS表数据的类型，目前支持：parquet、ORC、CSV、JSON、Carbon、Avro格式。只有OBS表有该参数，其他表没有该参数。
        :type data_type: str
        :param data_location: 数据存储位置，分为MANAGED，EXTERNAL和VIEW，其中EXTERNAL包括OBS表、CLoudTable表。
        :type data_location: str
        :param last_access_time: 最近更新时间。是单位为“毫秒”的时间戳。
        :type last_access_time: int
        :param location: OBS表上的存储路径。
        :type location: str
        :param owner: 表创建者。
        :type owner: str
        :param table_name: 表名称。
        :type table_name: str
        :param table_size: DLI表的大小。非DLI表该参数值为0。
        :type table_size: int
        :param table_type: 表类型： OBS表为EXTERNAL DLI表为MANAGED View为VIEW
        :type table_type: str
        :param partition_columns: 分区字段。只有OBS分区表有该参数，其他表没有该参数。
        :type partition_columns: list[str]
        :param page_size: 分页大小，最小为1，最大为100。
        :type page_size: int
        :param current_page: 当前页码，最小为1。
        :type current_page: int
        """
        
        

        self._create_time = None
        self._data_type = None
        self._data_location = None
        self._last_access_time = None
        self._location = None
        self._owner = None
        self._table_name = None
        self._table_size = None
        self._table_type = None
        self._partition_columns = None
        self._page_size = None
        self._current_page = None
        self.discriminator = None

        self.create_time = create_time
        if data_type is not None:
            self.data_type = data_type
        self.data_location = data_location
        self.last_access_time = last_access_time
        if location is not None:
            self.location = location
        self.owner = owner
        self.table_name = table_name
        self.table_size = table_size
        self.table_type = table_type
        if partition_columns is not None:
            self.partition_columns = partition_columns
        if page_size is not None:
            self.page_size = page_size
        if current_page is not None:
            self.current_page = current_page

    @property
    def create_time(self):
        """Gets the create_time of this Table.

        表创建时间。是单位为“毫秒”的时间戳。

        :return: The create_time of this Table.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Table.

        表创建时间。是单位为“毫秒”的时间戳。

        :param create_time: The create_time of this Table.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def data_type(self):
        """Gets the data_type of this Table.

        所列OBS表数据的类型，目前支持：parquet、ORC、CSV、JSON、Carbon、Avro格式。只有OBS表有该参数，其他表没有该参数。

        :return: The data_type of this Table.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this Table.

        所列OBS表数据的类型，目前支持：parquet、ORC、CSV、JSON、Carbon、Avro格式。只有OBS表有该参数，其他表没有该参数。

        :param data_type: The data_type of this Table.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def data_location(self):
        """Gets the data_location of this Table.

        数据存储位置，分为MANAGED，EXTERNAL和VIEW，其中EXTERNAL包括OBS表、CLoudTable表。

        :return: The data_location of this Table.
        :rtype: str
        """
        return self._data_location

    @data_location.setter
    def data_location(self, data_location):
        """Sets the data_location of this Table.

        数据存储位置，分为MANAGED，EXTERNAL和VIEW，其中EXTERNAL包括OBS表、CLoudTable表。

        :param data_location: The data_location of this Table.
        :type data_location: str
        """
        self._data_location = data_location

    @property
    def last_access_time(self):
        """Gets the last_access_time of this Table.

        最近更新时间。是单位为“毫秒”的时间戳。

        :return: The last_access_time of this Table.
        :rtype: int
        """
        return self._last_access_time

    @last_access_time.setter
    def last_access_time(self, last_access_time):
        """Sets the last_access_time of this Table.

        最近更新时间。是单位为“毫秒”的时间戳。

        :param last_access_time: The last_access_time of this Table.
        :type last_access_time: int
        """
        self._last_access_time = last_access_time

    @property
    def location(self):
        """Gets the location of this Table.

        OBS表上的存储路径。

        :return: The location of this Table.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Table.

        OBS表上的存储路径。

        :param location: The location of this Table.
        :type location: str
        """
        self._location = location

    @property
    def owner(self):
        """Gets the owner of this Table.

        表创建者。

        :return: The owner of this Table.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Table.

        表创建者。

        :param owner: The owner of this Table.
        :type owner: str
        """
        self._owner = owner

    @property
    def table_name(self):
        """Gets the table_name of this Table.

        表名称。

        :return: The table_name of this Table.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this Table.

        表名称。

        :param table_name: The table_name of this Table.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def table_size(self):
        """Gets the table_size of this Table.

        DLI表的大小。非DLI表该参数值为0。

        :return: The table_size of this Table.
        :rtype: int
        """
        return self._table_size

    @table_size.setter
    def table_size(self, table_size):
        """Sets the table_size of this Table.

        DLI表的大小。非DLI表该参数值为0。

        :param table_size: The table_size of this Table.
        :type table_size: int
        """
        self._table_size = table_size

    @property
    def table_type(self):
        """Gets the table_type of this Table.

        表类型： OBS表为EXTERNAL DLI表为MANAGED View为VIEW

        :return: The table_type of this Table.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        """Sets the table_type of this Table.

        表类型： OBS表为EXTERNAL DLI表为MANAGED View为VIEW

        :param table_type: The table_type of this Table.
        :type table_type: str
        """
        self._table_type = table_type

    @property
    def partition_columns(self):
        """Gets the partition_columns of this Table.

        分区字段。只有OBS分区表有该参数，其他表没有该参数。

        :return: The partition_columns of this Table.
        :rtype: list[str]
        """
        return self._partition_columns

    @partition_columns.setter
    def partition_columns(self, partition_columns):
        """Sets the partition_columns of this Table.

        分区字段。只有OBS分区表有该参数，其他表没有该参数。

        :param partition_columns: The partition_columns of this Table.
        :type partition_columns: list[str]
        """
        self._partition_columns = partition_columns

    @property
    def page_size(self):
        """Gets the page_size of this Table.

        分页大小，最小为1，最大为100。

        :return: The page_size of this Table.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this Table.

        分页大小，最小为1，最大为100。

        :param page_size: The page_size of this Table.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def current_page(self):
        """Gets the current_page of this Table.

        当前页码，最小为1。

        :return: The current_page of this Table.
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this Table.

        当前页码，最小为1。

        :param current_page: The current_page of this Table.
        :type current_page: int
        """
        self._current_page = current_page

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
        if not isinstance(other, Table):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
