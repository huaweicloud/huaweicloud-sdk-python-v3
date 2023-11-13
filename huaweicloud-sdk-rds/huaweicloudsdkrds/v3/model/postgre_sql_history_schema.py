# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostgreSQLHistorySchema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'total_tables': 'int',
        'tables': 'list[PostgreSQLHistoryTable]'
    }

    attribute_map = {
        'name': 'name',
        'total_tables': 'total_tables',
        'tables': 'tables'
    }

    def __init__(self, name=None, total_tables=None, tables=None):
        """PostgreSQLHistorySchema

        The model defined in huaweicloud sdk

        :param name: 模式名
        :type name: str
        :param total_tables: 可恢复表的数量
        :type total_tables: int
        :param tables: 表信息
        :type tables: list[:class:`huaweicloudsdkrds.v3.PostgreSQLHistoryTable`]
        """
        
        

        self._name = None
        self._total_tables = None
        self._tables = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if total_tables is not None:
            self.total_tables = total_tables
        if tables is not None:
            self.tables = tables

    @property
    def name(self):
        """Gets the name of this PostgreSQLHistorySchema.

        模式名

        :return: The name of this PostgreSQLHistorySchema.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostgreSQLHistorySchema.

        模式名

        :param name: The name of this PostgreSQLHistorySchema.
        :type name: str
        """
        self._name = name

    @property
    def total_tables(self):
        """Gets the total_tables of this PostgreSQLHistorySchema.

        可恢复表的数量

        :return: The total_tables of this PostgreSQLHistorySchema.
        :rtype: int
        """
        return self._total_tables

    @total_tables.setter
    def total_tables(self, total_tables):
        """Sets the total_tables of this PostgreSQLHistorySchema.

        可恢复表的数量

        :param total_tables: The total_tables of this PostgreSQLHistorySchema.
        :type total_tables: int
        """
        self._total_tables = total_tables

    @property
    def tables(self):
        """Gets the tables of this PostgreSQLHistorySchema.

        表信息

        :return: The tables of this PostgreSQLHistorySchema.
        :rtype: list[:class:`huaweicloudsdkrds.v3.PostgreSQLHistoryTable`]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this PostgreSQLHistorySchema.

        表信息

        :param tables: The tables of this PostgreSQLHistorySchema.
        :type tables: list[:class:`huaweicloudsdkrds.v3.PostgreSQLHistoryTable`]
        """
        self._tables = tables

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
        if not isinstance(other, PostgreSQLHistorySchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
