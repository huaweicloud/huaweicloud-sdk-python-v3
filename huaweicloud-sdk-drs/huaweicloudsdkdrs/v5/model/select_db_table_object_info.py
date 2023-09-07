# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SelectDbTableObjectInfo:

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
        'schema_name': 'str',
        'table_name': 'str'
    }

    attribute_map = {
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name'
    }

    def __init__(self, db_name=None, schema_name=None, table_name=None):
        """SelectDbTableObjectInfo

        The model defined in huaweicloud sdk

        :param db_name: 数据库名称。
        :type db_name: str
        :param schema_name: 数据库schema名称。
        :type schema_name: str
        :param table_name: 数据库表名称。
        :type table_name: str
        """
        
        

        self._db_name = None
        self._schema_name = None
        self._table_name = None
        self.discriminator = None

        self.db_name = db_name
        if schema_name is not None:
            self.schema_name = schema_name
        self.table_name = table_name

    @property
    def db_name(self):
        """Gets the db_name of this SelectDbTableObjectInfo.

        数据库名称。

        :return: The db_name of this SelectDbTableObjectInfo.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this SelectDbTableObjectInfo.

        数据库名称。

        :param db_name: The db_name of this SelectDbTableObjectInfo.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        """Gets the schema_name of this SelectDbTableObjectInfo.

        数据库schema名称。

        :return: The schema_name of this SelectDbTableObjectInfo.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this SelectDbTableObjectInfo.

        数据库schema名称。

        :param schema_name: The schema_name of this SelectDbTableObjectInfo.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        """Gets the table_name of this SelectDbTableObjectInfo.

        数据库表名称。

        :return: The table_name of this SelectDbTableObjectInfo.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this SelectDbTableObjectInfo.

        数据库表名称。

        :param table_name: The table_name of this SelectDbTableObjectInfo.
        :type table_name: str
        """
        self._table_name = table_name

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
        if not isinstance(other, SelectDbTableObjectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
