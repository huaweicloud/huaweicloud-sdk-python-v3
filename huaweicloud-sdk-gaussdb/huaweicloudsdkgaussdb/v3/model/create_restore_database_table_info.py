# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRestoreDatabaseTableInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database': 'str',
        'tables': 'list[CreateRestoreTableInfo]'
    }

    attribute_map = {
        'database': 'database',
        'tables': 'tables'
    }

    def __init__(self, database=None, tables=None):
        r"""CreateRestoreDatabaseTableInfo

        The model defined in huaweicloud sdk

        :param database: 数据库名称。
        :type database: str
        :param tables: 表信息。
        :type tables: list[:class:`huaweicloudsdkgaussdb.v3.CreateRestoreTableInfo`]
        """
        
        

        self._database = None
        self._tables = None
        self.discriminator = None

        self.database = database
        self.tables = tables

    @property
    def database(self):
        r"""Gets the database of this CreateRestoreDatabaseTableInfo.

        数据库名称。

        :return: The database of this CreateRestoreDatabaseTableInfo.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this CreateRestoreDatabaseTableInfo.

        数据库名称。

        :param database: The database of this CreateRestoreDatabaseTableInfo.
        :type database: str
        """
        self._database = database

    @property
    def tables(self):
        r"""Gets the tables of this CreateRestoreDatabaseTableInfo.

        表信息。

        :return: The tables of this CreateRestoreDatabaseTableInfo.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.CreateRestoreTableInfo`]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        r"""Sets the tables of this CreateRestoreDatabaseTableInfo.

        表信息。

        :param tables: The tables of this CreateRestoreDatabaseTableInfo.
        :type tables: list[:class:`huaweicloudsdkgaussdb.v3.CreateRestoreTableInfo`]
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
        if not isinstance(other, CreateRestoreDatabaseTableInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
