# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Database:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'database_guid': 'str',
        'database_qualified_name': 'str',
        'table_count': 'int',
        'data_size': 'float'
    }

    attribute_map = {
        'database_name': 'database_name',
        'database_guid': 'database_guid',
        'database_qualified_name': 'database_qualified_name',
        'table_count': 'table_count',
        'data_size': 'data_size'
    }

    def __init__(self, database_name=None, database_guid=None, database_qualified_name=None, table_count=None, data_size=None):
        """Database

        The model defined in huaweicloud sdk

        :param database_name: 数据库名称
        :type database_name: str
        :param database_guid: 数据库guid
        :type database_guid: str
        :param database_qualified_name: 数据库的唯一标识名称
        :type database_qualified_name: str
        :param table_count: 数据库中表数目
        :type table_count: int
        :param data_size: 数据量大小
        :type data_size: float
        """
        
        

        self._database_name = None
        self._database_guid = None
        self._database_qualified_name = None
        self._table_count = None
        self._data_size = None
        self.discriminator = None

        if database_name is not None:
            self.database_name = database_name
        if database_guid is not None:
            self.database_guid = database_guid
        if database_qualified_name is not None:
            self.database_qualified_name = database_qualified_name
        if table_count is not None:
            self.table_count = table_count
        if data_size is not None:
            self.data_size = data_size

    @property
    def database_name(self):
        """Gets the database_name of this Database.

        数据库名称

        :return: The database_name of this Database.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this Database.

        数据库名称

        :param database_name: The database_name of this Database.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def database_guid(self):
        """Gets the database_guid of this Database.

        数据库guid

        :return: The database_guid of this Database.
        :rtype: str
        """
        return self._database_guid

    @database_guid.setter
    def database_guid(self, database_guid):
        """Sets the database_guid of this Database.

        数据库guid

        :param database_guid: The database_guid of this Database.
        :type database_guid: str
        """
        self._database_guid = database_guid

    @property
    def database_qualified_name(self):
        """Gets the database_qualified_name of this Database.

        数据库的唯一标识名称

        :return: The database_qualified_name of this Database.
        :rtype: str
        """
        return self._database_qualified_name

    @database_qualified_name.setter
    def database_qualified_name(self, database_qualified_name):
        """Sets the database_qualified_name of this Database.

        数据库的唯一标识名称

        :param database_qualified_name: The database_qualified_name of this Database.
        :type database_qualified_name: str
        """
        self._database_qualified_name = database_qualified_name

    @property
    def table_count(self):
        """Gets the table_count of this Database.

        数据库中表数目

        :return: The table_count of this Database.
        :rtype: int
        """
        return self._table_count

    @table_count.setter
    def table_count(self, table_count):
        """Sets the table_count of this Database.

        数据库中表数目

        :param table_count: The table_count of this Database.
        :type table_count: int
        """
        self._table_count = table_count

    @property
    def data_size(self):
        """Gets the data_size of this Database.

        数据量大小

        :return: The data_size of this Database.
        :rtype: float
        """
        return self._data_size

    @data_size.setter
    def data_size(self, data_size):
        """Sets the data_size of this Database.

        数据量大小

        :param data_size: The data_size of this Database.
        :type data_size: float
        """
        self._data_size = data_size

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
        if not isinstance(other, Database):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
