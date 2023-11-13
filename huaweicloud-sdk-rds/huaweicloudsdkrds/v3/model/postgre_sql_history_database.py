# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostgreSQLHistoryDatabase:

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
        'schemas': 'list[PostgreSQLHistorySchema]'
    }

    attribute_map = {
        'name': 'name',
        'total_tables': 'total_tables',
        'schemas': 'schemas'
    }

    def __init__(self, name=None, total_tables=None, schemas=None):
        """PostgreSQLHistoryDatabase

        The model defined in huaweicloud sdk

        :param name: 数据库名
        :type name: str
        :param total_tables: 可恢复表的数量
        :type total_tables: int
        :param schemas: 模式信息
        :type schemas: list[:class:`huaweicloudsdkrds.v3.PostgreSQLHistorySchema`]
        """
        
        

        self._name = None
        self._total_tables = None
        self._schemas = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if total_tables is not None:
            self.total_tables = total_tables
        if schemas is not None:
            self.schemas = schemas

    @property
    def name(self):
        """Gets the name of this PostgreSQLHistoryDatabase.

        数据库名

        :return: The name of this PostgreSQLHistoryDatabase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostgreSQLHistoryDatabase.

        数据库名

        :param name: The name of this PostgreSQLHistoryDatabase.
        :type name: str
        """
        self._name = name

    @property
    def total_tables(self):
        """Gets the total_tables of this PostgreSQLHistoryDatabase.

        可恢复表的数量

        :return: The total_tables of this PostgreSQLHistoryDatabase.
        :rtype: int
        """
        return self._total_tables

    @total_tables.setter
    def total_tables(self, total_tables):
        """Sets the total_tables of this PostgreSQLHistoryDatabase.

        可恢复表的数量

        :param total_tables: The total_tables of this PostgreSQLHistoryDatabase.
        :type total_tables: int
        """
        self._total_tables = total_tables

    @property
    def schemas(self):
        """Gets the schemas of this PostgreSQLHistoryDatabase.

        模式信息

        :return: The schemas of this PostgreSQLHistoryDatabase.
        :rtype: list[:class:`huaweicloudsdkrds.v3.PostgreSQLHistorySchema`]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """Sets the schemas of this PostgreSQLHistoryDatabase.

        模式信息

        :param schemas: The schemas of this PostgreSQLHistoryDatabase.
        :type schemas: list[:class:`huaweicloudsdkrds.v3.PostgreSQLHistorySchema`]
        """
        self._schemas = schemas

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
        if not isinstance(other, PostgreSQLHistoryDatabase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
