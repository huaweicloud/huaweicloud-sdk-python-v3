# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableMeta:

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
        'table_type': 'str',
        'comments': 'str',
        'columns': 'list[Column]',
        'partition_keys': 'list[Column]'
    }

    attribute_map = {
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'table_type': 'table_type',
        'comments': 'comments',
        'columns': 'columns',
        'partition_keys': 'partition_keys'
    }

    def __init__(self, catalog_name=None, database_name=None, table_name=None, table_type=None, comments=None, columns=None, partition_keys=None):
        r"""TableMeta

        The model defined in huaweicloud sdk

        :param catalog_name: 表名
        :type catalog_name: str
        :param database_name: 数据库名字
        :type database_name: str
        :param table_name: 表名字
        :type table_name: str
        :param table_type: 表类型
        :type table_type: str
        :param comments: 表描述信息
        :type comments: str
        :param columns: 分区列以外的所有字段。
        :type columns: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        :param partition_keys: 分区列的信息。
        :type partition_keys: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        """
        
        

        self._catalog_name = None
        self._database_name = None
        self._table_name = None
        self._table_type = None
        self._comments = None
        self._columns = None
        self._partition_keys = None
        self.discriminator = None

        self.catalog_name = catalog_name
        self.database_name = database_name
        self.table_name = table_name
        self.table_type = table_type
        self.comments = comments
        if columns is not None:
            self.columns = columns
        if partition_keys is not None:
            self.partition_keys = partition_keys

    @property
    def catalog_name(self):
        r"""Gets the catalog_name of this TableMeta.

        表名

        :return: The catalog_name of this TableMeta.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        r"""Sets the catalog_name of this TableMeta.

        表名

        :param catalog_name: The catalog_name of this TableMeta.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        r"""Gets the database_name of this TableMeta.

        数据库名字

        :return: The database_name of this TableMeta.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this TableMeta.

        数据库名字

        :param database_name: The database_name of this TableMeta.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this TableMeta.

        表名字

        :return: The table_name of this TableMeta.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this TableMeta.

        表名字

        :param table_name: The table_name of this TableMeta.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def table_type(self):
        r"""Gets the table_type of this TableMeta.

        表类型

        :return: The table_type of this TableMeta.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        r"""Sets the table_type of this TableMeta.

        表类型

        :param table_type: The table_type of this TableMeta.
        :type table_type: str
        """
        self._table_type = table_type

    @property
    def comments(self):
        r"""Gets the comments of this TableMeta.

        表描述信息

        :return: The comments of this TableMeta.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        r"""Sets the comments of this TableMeta.

        表描述信息

        :param comments: The comments of this TableMeta.
        :type comments: str
        """
        self._comments = comments

    @property
    def columns(self):
        r"""Gets the columns of this TableMeta.

        分区列以外的所有字段。

        :return: The columns of this TableMeta.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        r"""Sets the columns of this TableMeta.

        分区列以外的所有字段。

        :param columns: The columns of this TableMeta.
        :type columns: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        """
        self._columns = columns

    @property
    def partition_keys(self):
        r"""Gets the partition_keys of this TableMeta.

        分区列的信息。

        :return: The partition_keys of this TableMeta.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        """
        return self._partition_keys

    @partition_keys.setter
    def partition_keys(self, partition_keys):
        r"""Sets the partition_keys of this TableMeta.

        分区列的信息。

        :param partition_keys: The partition_keys of this TableMeta.
        :type partition_keys: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        """
        self._partition_keys = partition_keys

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
        if not isinstance(other, TableMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
