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
        'table_id': 'str',
        'table_name': 'str',
        'table_alias': 'str',
        'created_time': 'str',
        'modified_time': 'str',
        'data_location': 'str',
        'data_type': 'str',
        'data_source': 'str',
        'table_type': 'str',
        'description': 'str',
        'partition_columns': 'list[str]',
        'data_store_id': 'str',
        'tags': 'str'
    }

    attribute_map = {
        'table_id': 'table_id',
        'table_name': 'table_name',
        'table_alias': 'table_alias',
        'created_time': 'created_time',
        'modified_time': 'modified_time',
        'data_location': 'data_location',
        'data_type': 'data_type',
        'data_source': 'data_source',
        'table_type': 'table_type',
        'description': 'description',
        'partition_columns': 'partition_columns',
        'data_store_id': 'data_store_id',
        'tags': 'tags'
    }

    def __init__(self, table_id=None, table_name=None, table_alias=None, created_time=None, modified_time=None, data_location=None, data_type=None, data_source=None, table_type=None, description=None, partition_columns=None, data_store_id=None, tags=None):
        r"""Table

        The model defined in huaweicloud sdk

        :param table_id: 表ID。
        :type table_id: str
        :param table_name: 表名称。
        :type table_name: str
        :param table_alias: 表别名。
        :type table_alias: str
        :param created_time: 表创建时间。
        :type created_time: str
        :param modified_time: 表更新时间。
        :type modified_time: str
        :param data_location: 数据存储位置，分为IoTA和VIEW
        :type data_location: str
        :param data_type: 数据类型，包括“csv”，“parquet”。
        :type data_type: str
        :param data_source: 数据来源。来源类型有：pipeline, default. 默认为default.
        :type data_source: str
        :param table_type: 表类型:IoTA表为MANAGED, View为VIEW
        :type table_type: str
        :param description: 表的描述信息。
        :type description: str
        :param partition_columns: 分区字段。只有OBS分区表有该参数，其他表没有该参数。
        :type partition_columns: list[str]
        :param data_store_id: 仅当数据来源为pipeline时返回。Data Store ID.
        :type data_store_id: str
        :param tags: 标签。
        :type tags: str
        """
        
        

        self._table_id = None
        self._table_name = None
        self._table_alias = None
        self._created_time = None
        self._modified_time = None
        self._data_location = None
        self._data_type = None
        self._data_source = None
        self._table_type = None
        self._description = None
        self._partition_columns = None
        self._data_store_id = None
        self._tags = None
        self.discriminator = None

        if table_id is not None:
            self.table_id = table_id
        if table_name is not None:
            self.table_name = table_name
        if table_alias is not None:
            self.table_alias = table_alias
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time
        if data_location is not None:
            self.data_location = data_location
        if data_type is not None:
            self.data_type = data_type
        if data_source is not None:
            self.data_source = data_source
        if table_type is not None:
            self.table_type = table_type
        if description is not None:
            self.description = description
        if partition_columns is not None:
            self.partition_columns = partition_columns
        if data_store_id is not None:
            self.data_store_id = data_store_id
        if tags is not None:
            self.tags = tags

    @property
    def table_id(self):
        r"""Gets the table_id of this Table.

        表ID。

        :return: The table_id of this Table.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this Table.

        表ID。

        :param table_id: The table_id of this Table.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def table_name(self):
        r"""Gets the table_name of this Table.

        表名称。

        :return: The table_name of this Table.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this Table.

        表名称。

        :param table_name: The table_name of this Table.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def table_alias(self):
        r"""Gets the table_alias of this Table.

        表别名。

        :return: The table_alias of this Table.
        :rtype: str
        """
        return self._table_alias

    @table_alias.setter
    def table_alias(self, table_alias):
        r"""Sets the table_alias of this Table.

        表别名。

        :param table_alias: The table_alias of this Table.
        :type table_alias: str
        """
        self._table_alias = table_alias

    @property
    def created_time(self):
        r"""Gets the created_time of this Table.

        表创建时间。

        :return: The created_time of this Table.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this Table.

        表创建时间。

        :param created_time: The created_time of this Table.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        r"""Gets the modified_time of this Table.

        表更新时间。

        :return: The modified_time of this Table.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this Table.

        表更新时间。

        :param modified_time: The modified_time of this Table.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def data_location(self):
        r"""Gets the data_location of this Table.

        数据存储位置，分为IoTA和VIEW

        :return: The data_location of this Table.
        :rtype: str
        """
        return self._data_location

    @data_location.setter
    def data_location(self, data_location):
        r"""Sets the data_location of this Table.

        数据存储位置，分为IoTA和VIEW

        :param data_location: The data_location of this Table.
        :type data_location: str
        """
        self._data_location = data_location

    @property
    def data_type(self):
        r"""Gets the data_type of this Table.

        数据类型，包括“csv”，“parquet”。

        :return: The data_type of this Table.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this Table.

        数据类型，包括“csv”，“parquet”。

        :param data_type: The data_type of this Table.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def data_source(self):
        r"""Gets the data_source of this Table.

        数据来源。来源类型有：pipeline, default. 默认为default.

        :return: The data_source of this Table.
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        r"""Sets the data_source of this Table.

        数据来源。来源类型有：pipeline, default. 默认为default.

        :param data_source: The data_source of this Table.
        :type data_source: str
        """
        self._data_source = data_source

    @property
    def table_type(self):
        r"""Gets the table_type of this Table.

        表类型:IoTA表为MANAGED, View为VIEW

        :return: The table_type of this Table.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        r"""Sets the table_type of this Table.

        表类型:IoTA表为MANAGED, View为VIEW

        :param table_type: The table_type of this Table.
        :type table_type: str
        """
        self._table_type = table_type

    @property
    def description(self):
        r"""Gets the description of this Table.

        表的描述信息。

        :return: The description of this Table.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Table.

        表的描述信息。

        :param description: The description of this Table.
        :type description: str
        """
        self._description = description

    @property
    def partition_columns(self):
        r"""Gets the partition_columns of this Table.

        分区字段。只有OBS分区表有该参数，其他表没有该参数。

        :return: The partition_columns of this Table.
        :rtype: list[str]
        """
        return self._partition_columns

    @partition_columns.setter
    def partition_columns(self, partition_columns):
        r"""Sets the partition_columns of this Table.

        分区字段。只有OBS分区表有该参数，其他表没有该参数。

        :param partition_columns: The partition_columns of this Table.
        :type partition_columns: list[str]
        """
        self._partition_columns = partition_columns

    @property
    def data_store_id(self):
        r"""Gets the data_store_id of this Table.

        仅当数据来源为pipeline时返回。Data Store ID.

        :return: The data_store_id of this Table.
        :rtype: str
        """
        return self._data_store_id

    @data_store_id.setter
    def data_store_id(self, data_store_id):
        r"""Sets the data_store_id of this Table.

        仅当数据来源为pipeline时返回。Data Store ID.

        :param data_store_id: The data_store_id of this Table.
        :type data_store_id: str
        """
        self._data_store_id = data_store_id

    @property
    def tags(self):
        r"""Gets the tags of this Table.

        标签。

        :return: The tags of this Table.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this Table.

        标签。

        :param tags: The tags of this Table.
        :type tags: str
        """
        self._tags = tags

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
