# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostgreSQLHistoryDatabaseInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'total_tables': 'int',
        'databases': 'list[PostgreSQLHistoryDatabaseInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'total_tables': 'total_tables',
        'databases': 'databases'
    }

    def __init__(self, id=None, name=None, total_tables=None, databases=None):
        """PostgreSQLHistoryDatabaseInstance

        The model defined in huaweicloud sdk

        :param id: 实例ID
        :type id: str
        :param name: 实例名称
        :type name: str
        :param total_tables: 表的个数
        :type total_tables: int
        :param databases: 数据库信息
        :type databases: list[:class:`huaweicloudsdkrds.v3.PostgreSQLHistoryDatabaseInfo`]
        """
        
        

        self._id = None
        self._name = None
        self._total_tables = None
        self._databases = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if total_tables is not None:
            self.total_tables = total_tables
        if databases is not None:
            self.databases = databases

    @property
    def id(self):
        """Gets the id of this PostgreSQLHistoryDatabaseInstance.

        实例ID

        :return: The id of this PostgreSQLHistoryDatabaseInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PostgreSQLHistoryDatabaseInstance.

        实例ID

        :param id: The id of this PostgreSQLHistoryDatabaseInstance.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this PostgreSQLHistoryDatabaseInstance.

        实例名称

        :return: The name of this PostgreSQLHistoryDatabaseInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostgreSQLHistoryDatabaseInstance.

        实例名称

        :param name: The name of this PostgreSQLHistoryDatabaseInstance.
        :type name: str
        """
        self._name = name

    @property
    def total_tables(self):
        """Gets the total_tables of this PostgreSQLHistoryDatabaseInstance.

        表的个数

        :return: The total_tables of this PostgreSQLHistoryDatabaseInstance.
        :rtype: int
        """
        return self._total_tables

    @total_tables.setter
    def total_tables(self, total_tables):
        """Sets the total_tables of this PostgreSQLHistoryDatabaseInstance.

        表的个数

        :param total_tables: The total_tables of this PostgreSQLHistoryDatabaseInstance.
        :type total_tables: int
        """
        self._total_tables = total_tables

    @property
    def databases(self):
        """Gets the databases of this PostgreSQLHistoryDatabaseInstance.

        数据库信息

        :return: The databases of this PostgreSQLHistoryDatabaseInstance.
        :rtype: list[:class:`huaweicloudsdkrds.v3.PostgreSQLHistoryDatabaseInfo`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this PostgreSQLHistoryDatabaseInstance.

        数据库信息

        :param databases: The databases of this PostgreSQLHistoryDatabaseInstance.
        :type databases: list[:class:`huaweicloudsdkrds.v3.PostgreSQLHistoryDatabaseInfo`]
        """
        self._databases = databases

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
        if not isinstance(other, PostgreSQLHistoryDatabaseInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
