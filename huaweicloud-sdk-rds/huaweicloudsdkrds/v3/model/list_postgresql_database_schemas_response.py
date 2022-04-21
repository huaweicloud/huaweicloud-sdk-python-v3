# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPostgresqlDatabaseSchemasResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'database_schemas': 'list[PostgresqlDatabaseForListSchema]',
        'total_count': 'int'
    }

    attribute_map = {
        'database_schemas': 'database_schemas',
        'total_count': 'total_count'
    }

    def __init__(self, database_schemas=None, total_count=None):
        """ListPostgresqlDatabaseSchemasResponse

        The model defined in huaweicloud sdk

        :param database_schemas: 列表中每个元素表示一个数据库schema。
        :type database_schemas: list[:class:`huaweicloudsdkrds.v3.PostgresqlDatabaseForListSchema`]
        :param total_count: 数据库schema总数。
        :type total_count: int
        """
        
        super(ListPostgresqlDatabaseSchemasResponse, self).__init__()

        self._database_schemas = None
        self._total_count = None
        self.discriminator = None

        if database_schemas is not None:
            self.database_schemas = database_schemas
        if total_count is not None:
            self.total_count = total_count

    @property
    def database_schemas(self):
        """Gets the database_schemas of this ListPostgresqlDatabaseSchemasResponse.

        列表中每个元素表示一个数据库schema。

        :return: The database_schemas of this ListPostgresqlDatabaseSchemasResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.PostgresqlDatabaseForListSchema`]
        """
        return self._database_schemas

    @database_schemas.setter
    def database_schemas(self, database_schemas):
        """Sets the database_schemas of this ListPostgresqlDatabaseSchemasResponse.

        列表中每个元素表示一个数据库schema。

        :param database_schemas: The database_schemas of this ListPostgresqlDatabaseSchemasResponse.
        :type database_schemas: list[:class:`huaweicloudsdkrds.v3.PostgresqlDatabaseForListSchema`]
        """
        self._database_schemas = database_schemas

    @property
    def total_count(self):
        """Gets the total_count of this ListPostgresqlDatabaseSchemasResponse.

        数据库schema总数。

        :return: The total_count of this ListPostgresqlDatabaseSchemasResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListPostgresqlDatabaseSchemasResponse.

        数据库schema总数。

        :param total_count: The total_count of this ListPostgresqlDatabaseSchemasResponse.
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
        if not isinstance(other, ListPostgresqlDatabaseSchemasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
