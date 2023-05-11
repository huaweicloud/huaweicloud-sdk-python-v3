# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Partition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'catalog_name': 'str',
        'database_name': 'str',
        'table_name': 'str',
        'partition_values': 'list[str]',
        'create_time': 'datetime',
        'last_access_time': 'datetime',
        'parameters': 'dict(str, str)',
        'storage_descriptor': 'StorageDescriptor'
    }

    attribute_map = {
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'partition_values': 'partition_values',
        'create_time': 'create_time',
        'last_access_time': 'last_access_time',
        'parameters': 'parameters',
        'storage_descriptor': 'storage_descriptor'
    }

    def __init__(self, catalog_name=None, database_name=None, table_name=None, partition_values=None, create_time=None, last_access_time=None, parameters=None, storage_descriptor=None):
        """Partition

        The model defined in huaweicloud sdk

        :param catalog_name: catalog名字
        :type catalog_name: str
        :param database_name: 数据库名字
        :type database_name: str
        :param table_name: 表名字
        :type table_name: str
        :param partition_values: 分区值的列表
        :type partition_values: list[str]
        :param create_time: 创建时间
        :type create_time: datetime
        :param last_access_time: 最后访问时间
        :type last_access_time: datetime
        :param parameters: 参数表
        :type parameters: dict(str, str)
        :param storage_descriptor: 
        :type storage_descriptor: :class:`huaweicloudsdklakeformation.v1.StorageDescriptor`
        """
        
        

        self._catalog_name = None
        self._database_name = None
        self._table_name = None
        self._partition_values = None
        self._create_time = None
        self._last_access_time = None
        self._parameters = None
        self._storage_descriptor = None
        self.discriminator = None

        self.catalog_name = catalog_name
        self.database_name = database_name
        self.table_name = table_name
        self.partition_values = partition_values
        self.create_time = create_time
        self.last_access_time = last_access_time
        self.parameters = parameters
        self.storage_descriptor = storage_descriptor

    @property
    def catalog_name(self):
        """Gets the catalog_name of this Partition.

        catalog名字

        :return: The catalog_name of this Partition.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        """Sets the catalog_name of this Partition.

        catalog名字

        :param catalog_name: The catalog_name of this Partition.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        """Gets the database_name of this Partition.

        数据库名字

        :return: The database_name of this Partition.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this Partition.

        数据库名字

        :param database_name: The database_name of this Partition.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        """Gets the table_name of this Partition.

        表名字

        :return: The table_name of this Partition.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this Partition.

        表名字

        :param table_name: The table_name of this Partition.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def partition_values(self):
        """Gets the partition_values of this Partition.

        分区值的列表

        :return: The partition_values of this Partition.
        :rtype: list[str]
        """
        return self._partition_values

    @partition_values.setter
    def partition_values(self, partition_values):
        """Sets the partition_values of this Partition.

        分区值的列表

        :param partition_values: The partition_values of this Partition.
        :type partition_values: list[str]
        """
        self._partition_values = partition_values

    @property
    def create_time(self):
        """Gets the create_time of this Partition.

        创建时间

        :return: The create_time of this Partition.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Partition.

        创建时间

        :param create_time: The create_time of this Partition.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def last_access_time(self):
        """Gets the last_access_time of this Partition.

        最后访问时间

        :return: The last_access_time of this Partition.
        :rtype: datetime
        """
        return self._last_access_time

    @last_access_time.setter
    def last_access_time(self, last_access_time):
        """Sets the last_access_time of this Partition.

        最后访问时间

        :param last_access_time: The last_access_time of this Partition.
        :type last_access_time: datetime
        """
        self._last_access_time = last_access_time

    @property
    def parameters(self):
        """Gets the parameters of this Partition.

        参数表

        :return: The parameters of this Partition.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Partition.

        参数表

        :param parameters: The parameters of this Partition.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

    @property
    def storage_descriptor(self):
        """Gets the storage_descriptor of this Partition.

        :return: The storage_descriptor of this Partition.
        :rtype: :class:`huaweicloudsdklakeformation.v1.StorageDescriptor`
        """
        return self._storage_descriptor

    @storage_descriptor.setter
    def storage_descriptor(self, storage_descriptor):
        """Sets the storage_descriptor of this Partition.

        :param storage_descriptor: The storage_descriptor of this Partition.
        :type storage_descriptor: :class:`huaweicloudsdklakeformation.v1.StorageDescriptor`
        """
        self._storage_descriptor = storage_descriptor

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
        if not isinstance(other, Partition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
