# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPartitionNamesWithoutLimitRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'catalog_name': 'str',
        'database_name': 'str',
        'table_name': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, catalog_name=None, database_name=None, table_name=None, limit=None):
        r"""ListPartitionNamesWithoutLimitRequest

        The model defined in huaweicloud sdk

        :param instance_id: LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。
        :type instance_id: str
        :param catalog_name: catalog名称。只能包含字母、数字和下划线，且长度为1~256个字符。
        :type catalog_name: str
        :param database_name: 数据库名称。只能包含中文、字母、数字和下划线，且长度为1~128个字符。
        :type database_name: str
        :param table_name: 表名称。只能包含中文、字母、数字和下划线，且长度为1~256个字符。
        :type table_name: str
        :param limit: 查询返回条数。默认值为1000。最小值为-1，最大值为9999999。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._catalog_name = None
        self._database_name = None
        self._table_name = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        self.catalog_name = catalog_name
        self.database_name = database_name
        self.table_name = table_name
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListPartitionNamesWithoutLimitRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :return: The instance_id of this ListPartitionNamesWithoutLimitRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListPartitionNamesWithoutLimitRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :param instance_id: The instance_id of this ListPartitionNamesWithoutLimitRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def catalog_name(self):
        r"""Gets the catalog_name of this ListPartitionNamesWithoutLimitRequest.

        catalog名称。只能包含字母、数字和下划线，且长度为1~256个字符。

        :return: The catalog_name of this ListPartitionNamesWithoutLimitRequest.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        r"""Sets the catalog_name of this ListPartitionNamesWithoutLimitRequest.

        catalog名称。只能包含字母、数字和下划线，且长度为1~256个字符。

        :param catalog_name: The catalog_name of this ListPartitionNamesWithoutLimitRequest.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        r"""Gets the database_name of this ListPartitionNamesWithoutLimitRequest.

        数据库名称。只能包含中文、字母、数字和下划线，且长度为1~128个字符。

        :return: The database_name of this ListPartitionNamesWithoutLimitRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListPartitionNamesWithoutLimitRequest.

        数据库名称。只能包含中文、字母、数字和下划线，且长度为1~128个字符。

        :param database_name: The database_name of this ListPartitionNamesWithoutLimitRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ListPartitionNamesWithoutLimitRequest.

        表名称。只能包含中文、字母、数字和下划线，且长度为1~256个字符。

        :return: The table_name of this ListPartitionNamesWithoutLimitRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ListPartitionNamesWithoutLimitRequest.

        表名称。只能包含中文、字母、数字和下划线，且长度为1~256个字符。

        :param table_name: The table_name of this ListPartitionNamesWithoutLimitRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def limit(self):
        r"""Gets the limit of this ListPartitionNamesWithoutLimitRequest.

        查询返回条数。默认值为1000。最小值为-1，最大值为9999999。

        :return: The limit of this ListPartitionNamesWithoutLimitRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPartitionNamesWithoutLimitRequest.

        查询返回条数。默认值为1000。最小值为-1，最大值为9999999。

        :param limit: The limit of this ListPartitionNamesWithoutLimitRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListPartitionNamesWithoutLimitRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
