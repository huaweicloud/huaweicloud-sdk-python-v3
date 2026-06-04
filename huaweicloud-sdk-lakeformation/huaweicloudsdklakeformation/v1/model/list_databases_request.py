# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabasesRequest:

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
        'database_name_pattern': 'str',
        'limit': 'int',
        'marker': 'str',
        'reverse_page': 'bool',
        'external_database_id': 'str',
        'deleted': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'catalog_name': 'catalog_name',
        'database_name_pattern': 'database_name_pattern',
        'limit': 'limit',
        'marker': 'marker',
        'reverse_page': 'reverse_page',
        'external_database_id': 'external_database_id',
        'deleted': 'deleted'
    }

    def __init__(self, instance_id=None, catalog_name=None, database_name_pattern=None, limit=None, marker=None, reverse_page=None, external_database_id=None, deleted=None):
        r"""ListDatabasesRequest

        The model defined in huaweicloud sdk

        :param instance_id: LakeFormation实例ID。创建实例时自动生成。例如:2180518f-42b8-4947-b20b-adfc53981a25。
        :type instance_id: str
        :param catalog_name: catalog名称。只能包含字母、数字和下划线,且长度为1~256个字符。
        :type catalog_name: str
        :param database_name_pattern: 数据库名称通配符。只能包含中文、字母、数字和_|*.-特殊字符,且长度为1~128个字符。
        :type database_name_pattern: str
        :param limit: 查询返回条数。默认值为1000。最小值为0,最大值为1000。
        :type limit: int
        :param marker: 查询的起始记录ID。最小长度为0,最大长度为256。
        :type marker: str
        :param reverse_page: 是否倒序查询。
        :type reverse_page: bool
        :param external_database_id: 用户端数据库id,创建时指定,不可修改。
        :type external_database_id: str
        :param deleted: 是否查询被删除元数据。
        :type deleted: bool
        """
        
        

        self._instance_id = None
        self._catalog_name = None
        self._database_name_pattern = None
        self._limit = None
        self._marker = None
        self._reverse_page = None
        self._external_database_id = None
        self._deleted = None
        self.discriminator = None

        self.instance_id = instance_id
        self.catalog_name = catalog_name
        if database_name_pattern is not None:
            self.database_name_pattern = database_name_pattern
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if reverse_page is not None:
            self.reverse_page = reverse_page
        if external_database_id is not None:
            self.external_database_id = external_database_id
        if deleted is not None:
            self.deleted = deleted

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListDatabasesRequest.

        LakeFormation实例ID。创建实例时自动生成。例如:2180518f-42b8-4947-b20b-adfc53981a25。

        :return: The instance_id of this ListDatabasesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListDatabasesRequest.

        LakeFormation实例ID。创建实例时自动生成。例如:2180518f-42b8-4947-b20b-adfc53981a25。

        :param instance_id: The instance_id of this ListDatabasesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def catalog_name(self):
        r"""Gets the catalog_name of this ListDatabasesRequest.

        catalog名称。只能包含字母、数字和下划线,且长度为1~256个字符。

        :return: The catalog_name of this ListDatabasesRequest.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        r"""Sets the catalog_name of this ListDatabasesRequest.

        catalog名称。只能包含字母、数字和下划线,且长度为1~256个字符。

        :param catalog_name: The catalog_name of this ListDatabasesRequest.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name_pattern(self):
        r"""Gets the database_name_pattern of this ListDatabasesRequest.

        数据库名称通配符。只能包含中文、字母、数字和_|*.-特殊字符,且长度为1~128个字符。

        :return: The database_name_pattern of this ListDatabasesRequest.
        :rtype: str
        """
        return self._database_name_pattern

    @database_name_pattern.setter
    def database_name_pattern(self, database_name_pattern):
        r"""Sets the database_name_pattern of this ListDatabasesRequest.

        数据库名称通配符。只能包含中文、字母、数字和_|*.-特殊字符,且长度为1~128个字符。

        :param database_name_pattern: The database_name_pattern of this ListDatabasesRequest.
        :type database_name_pattern: str
        """
        self._database_name_pattern = database_name_pattern

    @property
    def limit(self):
        r"""Gets the limit of this ListDatabasesRequest.

        查询返回条数。默认值为1000。最小值为0,最大值为1000。

        :return: The limit of this ListDatabasesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDatabasesRequest.

        查询返回条数。默认值为1000。最小值为0,最大值为1000。

        :param limit: The limit of this ListDatabasesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListDatabasesRequest.

        查询的起始记录ID。最小长度为0,最大长度为256。

        :return: The marker of this ListDatabasesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListDatabasesRequest.

        查询的起始记录ID。最小长度为0,最大长度为256。

        :param marker: The marker of this ListDatabasesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def reverse_page(self):
        r"""Gets the reverse_page of this ListDatabasesRequest.

        是否倒序查询。

        :return: The reverse_page of this ListDatabasesRequest.
        :rtype: bool
        """
        return self._reverse_page

    @reverse_page.setter
    def reverse_page(self, reverse_page):
        r"""Sets the reverse_page of this ListDatabasesRequest.

        是否倒序查询。

        :param reverse_page: The reverse_page of this ListDatabasesRequest.
        :type reverse_page: bool
        """
        self._reverse_page = reverse_page

    @property
    def external_database_id(self):
        r"""Gets the external_database_id of this ListDatabasesRequest.

        用户端数据库id,创建时指定,不可修改。

        :return: The external_database_id of this ListDatabasesRequest.
        :rtype: str
        """
        return self._external_database_id

    @external_database_id.setter
    def external_database_id(self, external_database_id):
        r"""Sets the external_database_id of this ListDatabasesRequest.

        用户端数据库id,创建时指定,不可修改。

        :param external_database_id: The external_database_id of this ListDatabasesRequest.
        :type external_database_id: str
        """
        self._external_database_id = external_database_id

    @property
    def deleted(self):
        r"""Gets the deleted of this ListDatabasesRequest.

        是否查询被删除元数据。

        :return: The deleted of this ListDatabasesRequest.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this ListDatabasesRequest.

        是否查询被删除元数据。

        :param deleted: The deleted of this ListDatabasesRequest.
        :type deleted: bool
        """
        self._deleted = deleted

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListDatabasesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
