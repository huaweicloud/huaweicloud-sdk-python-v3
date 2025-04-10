# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPartitionsRequest:

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
        'catalog_name': 'str',
        'database_name': 'str',
        'table_name': 'str',
        'filter': 'str',
        'partition_values': 'list[str]',
        'limit': 'int',
        'marker': 'str',
        'reverse_page': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'filter': 'filter',
        'partition_values': 'partition_values',
        'limit': 'limit',
        'marker': 'marker',
        'reverse_page': 'reverse_page'
    }

    def __init__(self, instance_id=None, catalog_name=None, database_name=None, table_name=None, filter=None, partition_values=None, limit=None, marker=None, reverse_page=None):
        r"""ListPartitionsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param catalog_name: catalog名字
        :type catalog_name: str
        :param database_name: 数据库名字
        :type database_name: str
        :param table_name: 表名称
        :type table_name: str
        :param filter: 分区过滤条件
        :type filter: str
        :param partition_values: 分区的值列表
        :type partition_values: list[str]
        :param limit: 查询返回条数
        :type limit: int
        :param marker: 查询的起始记录ID
        :type marker: str
        :param reverse_page: 是否查询上一页
        :type reverse_page: bool
        """
        
        

        self._instance_id = None
        self._catalog_name = None
        self._database_name = None
        self._table_name = None
        self._filter = None
        self._partition_values = None
        self._limit = None
        self._marker = None
        self._reverse_page = None
        self.discriminator = None

        self.instance_id = instance_id
        self.catalog_name = catalog_name
        self.database_name = database_name
        self.table_name = table_name
        if filter is not None:
            self.filter = filter
        if partition_values is not None:
            self.partition_values = partition_values
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if reverse_page is not None:
            self.reverse_page = reverse_page

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListPartitionsRequest.

        实例ID

        :return: The instance_id of this ListPartitionsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListPartitionsRequest.

        实例ID

        :param instance_id: The instance_id of this ListPartitionsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def catalog_name(self):
        r"""Gets the catalog_name of this ListPartitionsRequest.

        catalog名字

        :return: The catalog_name of this ListPartitionsRequest.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        r"""Sets the catalog_name of this ListPartitionsRequest.

        catalog名字

        :param catalog_name: The catalog_name of this ListPartitionsRequest.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        r"""Gets the database_name of this ListPartitionsRequest.

        数据库名字

        :return: The database_name of this ListPartitionsRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListPartitionsRequest.

        数据库名字

        :param database_name: The database_name of this ListPartitionsRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ListPartitionsRequest.

        表名称

        :return: The table_name of this ListPartitionsRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ListPartitionsRequest.

        表名称

        :param table_name: The table_name of this ListPartitionsRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def filter(self):
        r"""Gets the filter of this ListPartitionsRequest.

        分区过滤条件

        :return: The filter of this ListPartitionsRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ListPartitionsRequest.

        分区过滤条件

        :param filter: The filter of this ListPartitionsRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def partition_values(self):
        r"""Gets the partition_values of this ListPartitionsRequest.

        分区的值列表

        :return: The partition_values of this ListPartitionsRequest.
        :rtype: list[str]
        """
        return self._partition_values

    @partition_values.setter
    def partition_values(self, partition_values):
        r"""Sets the partition_values of this ListPartitionsRequest.

        分区的值列表

        :param partition_values: The partition_values of this ListPartitionsRequest.
        :type partition_values: list[str]
        """
        self._partition_values = partition_values

    @property
    def limit(self):
        r"""Gets the limit of this ListPartitionsRequest.

        查询返回条数

        :return: The limit of this ListPartitionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPartitionsRequest.

        查询返回条数

        :param limit: The limit of this ListPartitionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListPartitionsRequest.

        查询的起始记录ID

        :return: The marker of this ListPartitionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListPartitionsRequest.

        查询的起始记录ID

        :param marker: The marker of this ListPartitionsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def reverse_page(self):
        r"""Gets the reverse_page of this ListPartitionsRequest.

        是否查询上一页

        :return: The reverse_page of this ListPartitionsRequest.
        :rtype: bool
        """
        return self._reverse_page

    @reverse_page.setter
    def reverse_page(self, reverse_page):
        r"""Sets the reverse_page of this ListPartitionsRequest.

        是否查询上一页

        :param reverse_page: The reverse_page of this ListPartitionsRequest.
        :type reverse_page: bool
        """
        self._reverse_page = reverse_page

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
        if not isinstance(other, ListPartitionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
