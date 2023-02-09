# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionsRequest:

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
        'function_name_pattern': 'str',
        'limit': 'int',
        'marker': 'str',
        'reverse_page': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'function_name_pattern': 'function_name_pattern',
        'limit': 'limit',
        'marker': 'marker',
        'reverse_page': 'reverse_page'
    }

    def __init__(self, instance_id=None, catalog_name=None, database_name=None, function_name_pattern=None, limit=None, marker=None, reverse_page=None):
        """ListFunctionsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例Id
        :type instance_id: str
        :param catalog_name: catalog名字
        :type catalog_name: str
        :param database_name: 数据库名字
        :type database_name: str
        :param function_name_pattern: 函数名通配符
        :type function_name_pattern: str
        :param limit: 查询返回满足条件的function数量
        :type limit: int
        :param marker: 当前查询的起始位置
        :type marker: str
        :param reverse_page: 是否查询上一页
        :type reverse_page: bool
        """
        
        

        self._instance_id = None
        self._catalog_name = None
        self._database_name = None
        self._function_name_pattern = None
        self._limit = None
        self._marker = None
        self._reverse_page = None
        self.discriminator = None

        self.instance_id = instance_id
        self.catalog_name = catalog_name
        self.database_name = database_name
        if function_name_pattern is not None:
            self.function_name_pattern = function_name_pattern
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if reverse_page is not None:
            self.reverse_page = reverse_page

    @property
    def instance_id(self):
        """Gets the instance_id of this ListFunctionsRequest.

        实例Id

        :return: The instance_id of this ListFunctionsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListFunctionsRequest.

        实例Id

        :param instance_id: The instance_id of this ListFunctionsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def catalog_name(self):
        """Gets the catalog_name of this ListFunctionsRequest.

        catalog名字

        :return: The catalog_name of this ListFunctionsRequest.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        """Sets the catalog_name of this ListFunctionsRequest.

        catalog名字

        :param catalog_name: The catalog_name of this ListFunctionsRequest.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        """Gets the database_name of this ListFunctionsRequest.

        数据库名字

        :return: The database_name of this ListFunctionsRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ListFunctionsRequest.

        数据库名字

        :param database_name: The database_name of this ListFunctionsRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def function_name_pattern(self):
        """Gets the function_name_pattern of this ListFunctionsRequest.

        函数名通配符

        :return: The function_name_pattern of this ListFunctionsRequest.
        :rtype: str
        """
        return self._function_name_pattern

    @function_name_pattern.setter
    def function_name_pattern(self, function_name_pattern):
        """Sets the function_name_pattern of this ListFunctionsRequest.

        函数名通配符

        :param function_name_pattern: The function_name_pattern of this ListFunctionsRequest.
        :type function_name_pattern: str
        """
        self._function_name_pattern = function_name_pattern

    @property
    def limit(self):
        """Gets the limit of this ListFunctionsRequest.

        查询返回满足条件的function数量

        :return: The limit of this ListFunctionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFunctionsRequest.

        查询返回满足条件的function数量

        :param limit: The limit of this ListFunctionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListFunctionsRequest.

        当前查询的起始位置

        :return: The marker of this ListFunctionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListFunctionsRequest.

        当前查询的起始位置

        :param marker: The marker of this ListFunctionsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def reverse_page(self):
        """Gets the reverse_page of this ListFunctionsRequest.

        是否查询上一页

        :return: The reverse_page of this ListFunctionsRequest.
        :rtype: bool
        """
        return self._reverse_page

    @reverse_page.setter
    def reverse_page(self, reverse_page):
        """Sets the reverse_page of this ListFunctionsRequest.

        是否查询上一页

        :param reverse_page: The reverse_page of this ListFunctionsRequest.
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
        if not isinstance(other, ListFunctionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
