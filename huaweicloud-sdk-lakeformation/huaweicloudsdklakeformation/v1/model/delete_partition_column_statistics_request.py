# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeletePartitionColumnStatisticsRequest:

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
        'partition_values': 'list[str]',
        'column_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'partition_values': 'partition_values',
        'column_name': 'column_name'
    }

    def __init__(self, instance_id=None, catalog_name=None, database_name=None, table_name=None, partition_values=None, column_name=None):
        """DeletePartitionColumnStatisticsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param catalog_name: catalog名字
        :type catalog_name: str
        :param database_name: 数据库名字
        :type database_name: str
        :param table_name: 表名称
        :type table_name: str
        :param partition_values: 分区的值列表
        :type partition_values: list[str]
        :param column_name: 列名
        :type column_name: str
        """
        
        

        self._instance_id = None
        self._catalog_name = None
        self._database_name = None
        self._table_name = None
        self._partition_values = None
        self._column_name = None
        self.discriminator = None

        self.instance_id = instance_id
        self.catalog_name = catalog_name
        self.database_name = database_name
        self.table_name = table_name
        self.partition_values = partition_values
        if column_name is not None:
            self.column_name = column_name

    @property
    def instance_id(self):
        """Gets the instance_id of this DeletePartitionColumnStatisticsRequest.

        实例ID

        :return: The instance_id of this DeletePartitionColumnStatisticsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeletePartitionColumnStatisticsRequest.

        实例ID

        :param instance_id: The instance_id of this DeletePartitionColumnStatisticsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def catalog_name(self):
        """Gets the catalog_name of this DeletePartitionColumnStatisticsRequest.

        catalog名字

        :return: The catalog_name of this DeletePartitionColumnStatisticsRequest.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        """Sets the catalog_name of this DeletePartitionColumnStatisticsRequest.

        catalog名字

        :param catalog_name: The catalog_name of this DeletePartitionColumnStatisticsRequest.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        """Gets the database_name of this DeletePartitionColumnStatisticsRequest.

        数据库名字

        :return: The database_name of this DeletePartitionColumnStatisticsRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this DeletePartitionColumnStatisticsRequest.

        数据库名字

        :param database_name: The database_name of this DeletePartitionColumnStatisticsRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        """Gets the table_name of this DeletePartitionColumnStatisticsRequest.

        表名称

        :return: The table_name of this DeletePartitionColumnStatisticsRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this DeletePartitionColumnStatisticsRequest.

        表名称

        :param table_name: The table_name of this DeletePartitionColumnStatisticsRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def partition_values(self):
        """Gets the partition_values of this DeletePartitionColumnStatisticsRequest.

        分区的值列表

        :return: The partition_values of this DeletePartitionColumnStatisticsRequest.
        :rtype: list[str]
        """
        return self._partition_values

    @partition_values.setter
    def partition_values(self, partition_values):
        """Sets the partition_values of this DeletePartitionColumnStatisticsRequest.

        分区的值列表

        :param partition_values: The partition_values of this DeletePartitionColumnStatisticsRequest.
        :type partition_values: list[str]
        """
        self._partition_values = partition_values

    @property
    def column_name(self):
        """Gets the column_name of this DeletePartitionColumnStatisticsRequest.

        列名

        :return: The column_name of this DeletePartitionColumnStatisticsRequest.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this DeletePartitionColumnStatisticsRequest.

        列名

        :param column_name: The column_name of this DeletePartitionColumnStatisticsRequest.
        :type column_name: str
        """
        self._column_name = column_name

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
        if not isinstance(other, DeletePartitionColumnStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
