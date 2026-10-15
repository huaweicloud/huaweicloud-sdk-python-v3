# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataFilteringAdvancedSetting:

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
        'col_names': 'str',
        'prim_key_or_indexes': 'str',
        'indexes': 'str',
        'values': 'str'
    }

    attribute_map = {
        'db_name': 'db_name',
        'table_name': 'table_name',
        'col_names': 'col_names',
        'prim_key_or_indexes': 'prim_key_or_indexes',
        'indexes': 'indexes',
        'values': 'values'
    }

    def __init__(self, db_name=None, table_name=None, col_names=None, prim_key_or_indexes=None, indexes=None, values=None):
        r"""DataFilteringAdvancedSetting

        The model defined in huaweicloud sdk

        :param db_name: 库名
        :type db_name: str
        :param table_name: 表名
        :type table_name: str
        :param col_names: 列名
        :type col_names: str
        :param prim_key_or_indexes: 主键或唯一索引
        :type prim_key_or_indexes: str
        :param indexes: 优化查询所需的索引
        :type indexes: str
        :param values: 过滤条件
        :type values: str
        """
        
        

        self._db_name = None
        self._table_name = None
        self._col_names = None
        self._prim_key_or_indexes = None
        self._indexes = None
        self._values = None
        self.discriminator = None

        self.db_name = db_name
        self.table_name = table_name
        self.col_names = col_names
        self.prim_key_or_indexes = prim_key_or_indexes
        self.indexes = indexes
        self.values = values

    @property
    def db_name(self):
        r"""Gets the db_name of this DataFilteringAdvancedSetting.

        库名

        :return: The db_name of this DataFilteringAdvancedSetting.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this DataFilteringAdvancedSetting.

        库名

        :param db_name: The db_name of this DataFilteringAdvancedSetting.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def table_name(self):
        r"""Gets the table_name of this DataFilteringAdvancedSetting.

        表名

        :return: The table_name of this DataFilteringAdvancedSetting.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this DataFilteringAdvancedSetting.

        表名

        :param table_name: The table_name of this DataFilteringAdvancedSetting.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def col_names(self):
        r"""Gets the col_names of this DataFilteringAdvancedSetting.

        列名

        :return: The col_names of this DataFilteringAdvancedSetting.
        :rtype: str
        """
        return self._col_names

    @col_names.setter
    def col_names(self, col_names):
        r"""Sets the col_names of this DataFilteringAdvancedSetting.

        列名

        :param col_names: The col_names of this DataFilteringAdvancedSetting.
        :type col_names: str
        """
        self._col_names = col_names

    @property
    def prim_key_or_indexes(self):
        r"""Gets the prim_key_or_indexes of this DataFilteringAdvancedSetting.

        主键或唯一索引

        :return: The prim_key_or_indexes of this DataFilteringAdvancedSetting.
        :rtype: str
        """
        return self._prim_key_or_indexes

    @prim_key_or_indexes.setter
    def prim_key_or_indexes(self, prim_key_or_indexes):
        r"""Sets the prim_key_or_indexes of this DataFilteringAdvancedSetting.

        主键或唯一索引

        :param prim_key_or_indexes: The prim_key_or_indexes of this DataFilteringAdvancedSetting.
        :type prim_key_or_indexes: str
        """
        self._prim_key_or_indexes = prim_key_or_indexes

    @property
    def indexes(self):
        r"""Gets the indexes of this DataFilteringAdvancedSetting.

        优化查询所需的索引

        :return: The indexes of this DataFilteringAdvancedSetting.
        :rtype: str
        """
        return self._indexes

    @indexes.setter
    def indexes(self, indexes):
        r"""Sets the indexes of this DataFilteringAdvancedSetting.

        优化查询所需的索引

        :param indexes: The indexes of this DataFilteringAdvancedSetting.
        :type indexes: str
        """
        self._indexes = indexes

    @property
    def values(self):
        r"""Gets the values of this DataFilteringAdvancedSetting.

        过滤条件

        :return: The values of this DataFilteringAdvancedSetting.
        :rtype: str
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this DataFilteringAdvancedSetting.

        过滤条件

        :param values: The values of this DataFilteringAdvancedSetting.
        :type values: str
        """
        self._values = values

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
        if not isinstance(other, DataFilteringAdvancedSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
