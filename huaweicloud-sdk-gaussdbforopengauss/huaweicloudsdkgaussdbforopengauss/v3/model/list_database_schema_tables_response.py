# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseSchemaTablesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_tables': 'list[DatabaseForListTableResult]',
        'total_count': 'int'
    }

    attribute_map = {
        'database_tables': 'database_tables',
        'total_count': 'total_count'
    }

    def __init__(self, database_tables=None, total_count=None):
        r"""ListDatabaseSchemaTablesResponse

        The model defined in huaweicloud sdk

        :param database_tables: **参数解释**： 列表中每个元素表示一个数据库表。
        :type database_tables: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DatabaseForListTableResult`]
        :param total_count: **参数解释**： 数据库表总数。 **取值范围**： 不涉及。
        :type total_count: int
        """
        
        super(ListDatabaseSchemaTablesResponse, self).__init__()

        self._database_tables = None
        self._total_count = None
        self.discriminator = None

        if database_tables is not None:
            self.database_tables = database_tables
        if total_count is not None:
            self.total_count = total_count

    @property
    def database_tables(self):
        r"""Gets the database_tables of this ListDatabaseSchemaTablesResponse.

        **参数解释**： 列表中每个元素表示一个数据库表。

        :return: The database_tables of this ListDatabaseSchemaTablesResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DatabaseForListTableResult`]
        """
        return self._database_tables

    @database_tables.setter
    def database_tables(self, database_tables):
        r"""Sets the database_tables of this ListDatabaseSchemaTablesResponse.

        **参数解释**： 列表中每个元素表示一个数据库表。

        :param database_tables: The database_tables of this ListDatabaseSchemaTablesResponse.
        :type database_tables: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DatabaseForListTableResult`]
        """
        self._database_tables = database_tables

    @property
    def total_count(self):
        r"""Gets the total_count of this ListDatabaseSchemaTablesResponse.

        **参数解释**： 数据库表总数。 **取值范围**： 不涉及。

        :return: The total_count of this ListDatabaseSchemaTablesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListDatabaseSchemaTablesResponse.

        **参数解释**： 数据库表总数。 **取值范围**： 不涉及。

        :param total_count: The total_count of this ListDatabaseSchemaTablesResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListDatabaseSchemaTablesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
