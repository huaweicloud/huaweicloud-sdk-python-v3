# coding: utf-8

import six

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
        'reverse_page': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'catalog_name': 'catalog_name',
        'database_name_pattern': 'database_name_pattern',
        'limit': 'limit',
        'marker': 'marker',
        'reverse_page': 'reverse_page'
    }

    def __init__(self, instance_id=None, catalog_name=None, database_name_pattern=None, limit=None, marker=None, reverse_page=None):
        """ListDatabasesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例Id
        :type instance_id: str
        :param catalog_name: catalog名字
        :type catalog_name: str
        :param database_name_pattern: 数据库名字通配符
        :type database_name_pattern: str
        :param limit: 返回的条目数量
        :type limit: int
        :param marker: 查询的起始记录ID
        :type marker: str
        :param reverse_page: 是否查询上一页
        :type reverse_page: bool
        """
        
        

        self._instance_id = None
        self._catalog_name = None
        self._database_name_pattern = None
        self._limit = None
        self._marker = None
        self._reverse_page = None
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

    @property
    def instance_id(self):
        """Gets the instance_id of this ListDatabasesRequest.

        实例Id

        :return: The instance_id of this ListDatabasesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListDatabasesRequest.

        实例Id

        :param instance_id: The instance_id of this ListDatabasesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def catalog_name(self):
        """Gets the catalog_name of this ListDatabasesRequest.

        catalog名字

        :return: The catalog_name of this ListDatabasesRequest.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        """Sets the catalog_name of this ListDatabasesRequest.

        catalog名字

        :param catalog_name: The catalog_name of this ListDatabasesRequest.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name_pattern(self):
        """Gets the database_name_pattern of this ListDatabasesRequest.

        数据库名字通配符

        :return: The database_name_pattern of this ListDatabasesRequest.
        :rtype: str
        """
        return self._database_name_pattern

    @database_name_pattern.setter
    def database_name_pattern(self, database_name_pattern):
        """Sets the database_name_pattern of this ListDatabasesRequest.

        数据库名字通配符

        :param database_name_pattern: The database_name_pattern of this ListDatabasesRequest.
        :type database_name_pattern: str
        """
        self._database_name_pattern = database_name_pattern

    @property
    def limit(self):
        """Gets the limit of this ListDatabasesRequest.

        返回的条目数量

        :return: The limit of this ListDatabasesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDatabasesRequest.

        返回的条目数量

        :param limit: The limit of this ListDatabasesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListDatabasesRequest.

        查询的起始记录ID

        :return: The marker of this ListDatabasesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListDatabasesRequest.

        查询的起始记录ID

        :param marker: The marker of this ListDatabasesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def reverse_page(self):
        """Gets the reverse_page of this ListDatabasesRequest.

        是否查询上一页

        :return: The reverse_page of this ListDatabasesRequest.
        :rtype: bool
        """
        return self._reverse_page

    @reverse_page.setter
    def reverse_page(self, reverse_page):
        """Sets the reverse_page of this ListDatabasesRequest.

        是否查询上一页

        :param reverse_page: The reverse_page of this ListDatabasesRequest.
        :type reverse_page: bool
        """
        self._reverse_page = reverse_page

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
        if not isinstance(other, ListDatabasesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
