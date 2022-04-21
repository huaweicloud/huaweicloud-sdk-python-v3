# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigTransformationVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'db_table_name': 'str',
        'db_name': 'str',
        'table_name': 'str',
        'col_names': 'str',
        'prim_key_or_index': 'str',
        'indexs': 'str',
        'values': 'str'
    }

    attribute_map = {
        'db_table_name': 'db_table_name',
        'db_name': 'db_name',
        'table_name': 'table_name',
        'col_names': 'col_names',
        'prim_key_or_index': 'prim_key_or_index',
        'indexs': 'indexs',
        'values': 'values'
    }

    def __init__(self, db_table_name=None, db_name=None, table_name=None, col_names=None, prim_key_or_index=None, indexs=None, values=None):
        """ConfigTransformationVo

        The model defined in huaweicloud sdk

        :param db_table_name: 库名.表名。
        :type db_table_name: str
        :param db_name: 库名。长度限制256。
        :type db_name: str
        :param table_name: 表名。长度限制256。
        :type table_name: str
        :param col_names: 列名。长度限制256。
        :type col_names: str
        :param prim_key_or_index: 主键或唯一索引。长度限制256。
        :type prim_key_or_index: str
        :param indexs: 优化查询所需的索引。长度限制256。
        :type indexs: str
        :param values: 过滤条件。长度限制256。
        :type values: str
        """
        
        

        self._db_table_name = None
        self._db_name = None
        self._table_name = None
        self._col_names = None
        self._prim_key_or_index = None
        self._indexs = None
        self._values = None
        self.discriminator = None

        self.db_table_name = db_table_name
        self.db_name = db_name
        self.table_name = table_name
        self.col_names = col_names
        self.prim_key_or_index = prim_key_or_index
        self.indexs = indexs
        self.values = values

    @property
    def db_table_name(self):
        """Gets the db_table_name of this ConfigTransformationVo.

        库名.表名。

        :return: The db_table_name of this ConfigTransformationVo.
        :rtype: str
        """
        return self._db_table_name

    @db_table_name.setter
    def db_table_name(self, db_table_name):
        """Sets the db_table_name of this ConfigTransformationVo.

        库名.表名。

        :param db_table_name: The db_table_name of this ConfigTransformationVo.
        :type db_table_name: str
        """
        self._db_table_name = db_table_name

    @property
    def db_name(self):
        """Gets the db_name of this ConfigTransformationVo.

        库名。长度限制256。

        :return: The db_name of this ConfigTransformationVo.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this ConfigTransformationVo.

        库名。长度限制256。

        :param db_name: The db_name of this ConfigTransformationVo.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def table_name(self):
        """Gets the table_name of this ConfigTransformationVo.

        表名。长度限制256。

        :return: The table_name of this ConfigTransformationVo.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ConfigTransformationVo.

        表名。长度限制256。

        :param table_name: The table_name of this ConfigTransformationVo.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def col_names(self):
        """Gets the col_names of this ConfigTransformationVo.

        列名。长度限制256。

        :return: The col_names of this ConfigTransformationVo.
        :rtype: str
        """
        return self._col_names

    @col_names.setter
    def col_names(self, col_names):
        """Sets the col_names of this ConfigTransformationVo.

        列名。长度限制256。

        :param col_names: The col_names of this ConfigTransformationVo.
        :type col_names: str
        """
        self._col_names = col_names

    @property
    def prim_key_or_index(self):
        """Gets the prim_key_or_index of this ConfigTransformationVo.

        主键或唯一索引。长度限制256。

        :return: The prim_key_or_index of this ConfigTransformationVo.
        :rtype: str
        """
        return self._prim_key_or_index

    @prim_key_or_index.setter
    def prim_key_or_index(self, prim_key_or_index):
        """Sets the prim_key_or_index of this ConfigTransformationVo.

        主键或唯一索引。长度限制256。

        :param prim_key_or_index: The prim_key_or_index of this ConfigTransformationVo.
        :type prim_key_or_index: str
        """
        self._prim_key_or_index = prim_key_or_index

    @property
    def indexs(self):
        """Gets the indexs of this ConfigTransformationVo.

        优化查询所需的索引。长度限制256。

        :return: The indexs of this ConfigTransformationVo.
        :rtype: str
        """
        return self._indexs

    @indexs.setter
    def indexs(self, indexs):
        """Sets the indexs of this ConfigTransformationVo.

        优化查询所需的索引。长度限制256。

        :param indexs: The indexs of this ConfigTransformationVo.
        :type indexs: str
        """
        self._indexs = indexs

    @property
    def values(self):
        """Gets the values of this ConfigTransformationVo.

        过滤条件。长度限制256。

        :return: The values of this ConfigTransformationVo.
        :rtype: str
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ConfigTransformationVo.

        过滤条件。长度限制256。

        :param values: The values of this ConfigTransformationVo.
        :type values: str
        """
        self._values = values

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
        if not isinstance(other, ConfigTransformationVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
