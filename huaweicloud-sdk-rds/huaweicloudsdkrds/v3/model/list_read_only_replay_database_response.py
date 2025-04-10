# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReadOnlyReplayDatabaseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_limit': 'int',
        'total_tables': 'int',
        'table_limit': 'int',
        'databases': 'list[DelayRestoreDatabase]'
    }

    attribute_map = {
        'database_limit': 'database_limit',
        'total_tables': 'total_tables',
        'table_limit': 'table_limit',
        'databases': 'databases'
    }

    def __init__(self, database_limit=None, total_tables=None, table_limit=None, databases=None):
        r"""ListReadOnlyReplayDatabaseResponse

        The model defined in huaweicloud sdk

        :param database_limit: 每次返回的库上限数量
        :type database_limit: int
        :param total_tables: 返回的总表数量
        :type total_tables: int
        :param table_limit: 每次返回的表上限数量
        :type table_limit: int
        :param databases: 可恢复到主实例的数据库列表
        :type databases: list[:class:`huaweicloudsdkrds.v3.DelayRestoreDatabase`]
        """
        
        super(ListReadOnlyReplayDatabaseResponse, self).__init__()

        self._database_limit = None
        self._total_tables = None
        self._table_limit = None
        self._databases = None
        self.discriminator = None

        if database_limit is not None:
            self.database_limit = database_limit
        if total_tables is not None:
            self.total_tables = total_tables
        if table_limit is not None:
            self.table_limit = table_limit
        if databases is not None:
            self.databases = databases

    @property
    def database_limit(self):
        r"""Gets the database_limit of this ListReadOnlyReplayDatabaseResponse.

        每次返回的库上限数量

        :return: The database_limit of this ListReadOnlyReplayDatabaseResponse.
        :rtype: int
        """
        return self._database_limit

    @database_limit.setter
    def database_limit(self, database_limit):
        r"""Sets the database_limit of this ListReadOnlyReplayDatabaseResponse.

        每次返回的库上限数量

        :param database_limit: The database_limit of this ListReadOnlyReplayDatabaseResponse.
        :type database_limit: int
        """
        self._database_limit = database_limit

    @property
    def total_tables(self):
        r"""Gets the total_tables of this ListReadOnlyReplayDatabaseResponse.

        返回的总表数量

        :return: The total_tables of this ListReadOnlyReplayDatabaseResponse.
        :rtype: int
        """
        return self._total_tables

    @total_tables.setter
    def total_tables(self, total_tables):
        r"""Sets the total_tables of this ListReadOnlyReplayDatabaseResponse.

        返回的总表数量

        :param total_tables: The total_tables of this ListReadOnlyReplayDatabaseResponse.
        :type total_tables: int
        """
        self._total_tables = total_tables

    @property
    def table_limit(self):
        r"""Gets the table_limit of this ListReadOnlyReplayDatabaseResponse.

        每次返回的表上限数量

        :return: The table_limit of this ListReadOnlyReplayDatabaseResponse.
        :rtype: int
        """
        return self._table_limit

    @table_limit.setter
    def table_limit(self, table_limit):
        r"""Sets the table_limit of this ListReadOnlyReplayDatabaseResponse.

        每次返回的表上限数量

        :param table_limit: The table_limit of this ListReadOnlyReplayDatabaseResponse.
        :type table_limit: int
        """
        self._table_limit = table_limit

    @property
    def databases(self):
        r"""Gets the databases of this ListReadOnlyReplayDatabaseResponse.

        可恢复到主实例的数据库列表

        :return: The databases of this ListReadOnlyReplayDatabaseResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.DelayRestoreDatabase`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this ListReadOnlyReplayDatabaseResponse.

        可恢复到主实例的数据库列表

        :param databases: The databases of this ListReadOnlyReplayDatabaseResponse.
        :type databases: list[:class:`huaweicloudsdkrds.v3.DelayRestoreDatabase`]
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
        if not isinstance(other, ListReadOnlyReplayDatabaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
