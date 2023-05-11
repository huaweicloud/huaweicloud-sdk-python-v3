# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTableSchemaResponse(SdkResponse):

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
        'tags': 'str',
        'column_count': 'int',
        'columns': 'list[Column]',
        'table_type': 'str',
        'data_type': 'str',
        'data_location': 'str',
        'storage_properties': 'list[KeyValue]'
    }

    attribute_map = {
        'table_id': 'table_id',
        'table_name': 'table_name',
        'table_alias': 'table_alias',
        'tags': 'tags',
        'column_count': 'column_count',
        'columns': 'columns',
        'table_type': 'table_type',
        'data_type': 'data_type',
        'data_location': 'data_location',
        'storage_properties': 'storage_properties'
    }

    def __init__(self, table_id=None, table_name=None, table_alias=None, tags=None, column_count=None, columns=None, table_type=None, data_type=None, data_location=None, storage_properties=None):
        """ShowTableSchemaResponse

        The model defined in huaweicloud sdk

        :param table_id: 表ID。
        :type table_id: str
        :param table_name: 表名。
        :type table_name: str
        :param table_alias: 表别名。
        :type table_alias: str
        :param tags: 标签。
        :type tags: str
        :param column_count: 表的总列数。
        :type column_count: int
        :param columns: 表的列信息，包含列名称、类型和描述信息。
        :type columns: list[:class:`huaweicloudsdkiotanalytics.v1.Column`]
        :param table_type: 表类型，包括“MANAGED”，“EXTERNAL”和“VIEW”。
        :type table_type: str
        :param data_type: 数据类型，包括“csv”，“parquet”。
        :type data_type: str
        :param data_location: 数据存储的路径，以“s3a”开头。
        :type data_location: str
        :param storage_properties: 
        :type storage_properties: list[:class:`huaweicloudsdkiotanalytics.v1.KeyValue`]
        """
        
        super(ShowTableSchemaResponse, self).__init__()

        self._table_id = None
        self._table_name = None
        self._table_alias = None
        self._tags = None
        self._column_count = None
        self._columns = None
        self._table_type = None
        self._data_type = None
        self._data_location = None
        self._storage_properties = None
        self.discriminator = None

        if table_id is not None:
            self.table_id = table_id
        if table_name is not None:
            self.table_name = table_name
        if table_alias is not None:
            self.table_alias = table_alias
        if tags is not None:
            self.tags = tags
        if column_count is not None:
            self.column_count = column_count
        if columns is not None:
            self.columns = columns
        if table_type is not None:
            self.table_type = table_type
        if data_type is not None:
            self.data_type = data_type
        if data_location is not None:
            self.data_location = data_location
        if storage_properties is not None:
            self.storage_properties = storage_properties

    @property
    def table_id(self):
        """Gets the table_id of this ShowTableSchemaResponse.

        表ID。

        :return: The table_id of this ShowTableSchemaResponse.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this ShowTableSchemaResponse.

        表ID。

        :param table_id: The table_id of this ShowTableSchemaResponse.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def table_name(self):
        """Gets the table_name of this ShowTableSchemaResponse.

        表名。

        :return: The table_name of this ShowTableSchemaResponse.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ShowTableSchemaResponse.

        表名。

        :param table_name: The table_name of this ShowTableSchemaResponse.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def table_alias(self):
        """Gets the table_alias of this ShowTableSchemaResponse.

        表别名。

        :return: The table_alias of this ShowTableSchemaResponse.
        :rtype: str
        """
        return self._table_alias

    @table_alias.setter
    def table_alias(self, table_alias):
        """Sets the table_alias of this ShowTableSchemaResponse.

        表别名。

        :param table_alias: The table_alias of this ShowTableSchemaResponse.
        :type table_alias: str
        """
        self._table_alias = table_alias

    @property
    def tags(self):
        """Gets the tags of this ShowTableSchemaResponse.

        标签。

        :return: The tags of this ShowTableSchemaResponse.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowTableSchemaResponse.

        标签。

        :param tags: The tags of this ShowTableSchemaResponse.
        :type tags: str
        """
        self._tags = tags

    @property
    def column_count(self):
        """Gets the column_count of this ShowTableSchemaResponse.

        表的总列数。

        :return: The column_count of this ShowTableSchemaResponse.
        :rtype: int
        """
        return self._column_count

    @column_count.setter
    def column_count(self, column_count):
        """Sets the column_count of this ShowTableSchemaResponse.

        表的总列数。

        :param column_count: The column_count of this ShowTableSchemaResponse.
        :type column_count: int
        """
        self._column_count = column_count

    @property
    def columns(self):
        """Gets the columns of this ShowTableSchemaResponse.

        表的列信息，包含列名称、类型和描述信息。

        :return: The columns of this ShowTableSchemaResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.Column`]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this ShowTableSchemaResponse.

        表的列信息，包含列名称、类型和描述信息。

        :param columns: The columns of this ShowTableSchemaResponse.
        :type columns: list[:class:`huaweicloudsdkiotanalytics.v1.Column`]
        """
        self._columns = columns

    @property
    def table_type(self):
        """Gets the table_type of this ShowTableSchemaResponse.

        表类型，包括“MANAGED”，“EXTERNAL”和“VIEW”。

        :return: The table_type of this ShowTableSchemaResponse.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        """Sets the table_type of this ShowTableSchemaResponse.

        表类型，包括“MANAGED”，“EXTERNAL”和“VIEW”。

        :param table_type: The table_type of this ShowTableSchemaResponse.
        :type table_type: str
        """
        self._table_type = table_type

    @property
    def data_type(self):
        """Gets the data_type of this ShowTableSchemaResponse.

        数据类型，包括“csv”，“parquet”。

        :return: The data_type of this ShowTableSchemaResponse.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ShowTableSchemaResponse.

        数据类型，包括“csv”，“parquet”。

        :param data_type: The data_type of this ShowTableSchemaResponse.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def data_location(self):
        """Gets the data_location of this ShowTableSchemaResponse.

        数据存储的路径，以“s3a”开头。

        :return: The data_location of this ShowTableSchemaResponse.
        :rtype: str
        """
        return self._data_location

    @data_location.setter
    def data_location(self, data_location):
        """Sets the data_location of this ShowTableSchemaResponse.

        数据存储的路径，以“s3a”开头。

        :param data_location: The data_location of this ShowTableSchemaResponse.
        :type data_location: str
        """
        self._data_location = data_location

    @property
    def storage_properties(self):
        """Gets the storage_properties of this ShowTableSchemaResponse.

        :return: The storage_properties of this ShowTableSchemaResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.KeyValue`]
        """
        return self._storage_properties

    @storage_properties.setter
    def storage_properties(self, storage_properties):
        """Sets the storage_properties of this ShowTableSchemaResponse.

        :param storage_properties: The storage_properties of this ShowTableSchemaResponse.
        :type storage_properties: list[:class:`huaweicloudsdkiotanalytics.v1.KeyValue`]
        """
        self._storage_properties = storage_properties

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
        if not isinstance(other, ShowTableSchemaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
