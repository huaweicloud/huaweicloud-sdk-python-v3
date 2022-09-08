# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllTablesRequest:

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
        'current_page': 'int',
        'keyword': 'str',
        'page_size': 'int',
        'table_type': 'str',
        'with_detail': 'bool',
        'with_priv': 'bool'
    }

    attribute_map = {
        'database_name': 'database_name',
        'current_page': 'current-page',
        'keyword': 'keyword',
        'page_size': 'page-size',
        'table_type': 'table-type',
        'with_detail': 'with-detail',
        'with_priv': 'with-priv'
    }

    def __init__(self, database_name=None, current_page=None, keyword=None, page_size=None, table_type=None, with_detail=None, with_priv=None):
        """ListAllTablesRequest

        The model defined in huaweicloud sdk

        :param database_name: 查看表所在的数据库名称。
        :type database_name: str
        :param current_page: 
        :type current_page: int
        :param keyword: 过滤表名称的关键词。
        :type keyword: str
        :param page_size: 
        :type page_size: int
        :param table_type: 
        :type table_type: str
        :param with_detail: 是否获取表的详细信息（所有者，size等）。
        :type with_detail: bool
        :param with_priv: 
        :type with_priv: bool
        """
        
        

        self._database_name = None
        self._current_page = None
        self._keyword = None
        self._page_size = None
        self._table_type = None
        self._with_detail = None
        self._with_priv = None
        self.discriminator = None

        self.database_name = database_name
        if current_page is not None:
            self.current_page = current_page
        if keyword is not None:
            self.keyword = keyword
        if page_size is not None:
            self.page_size = page_size
        if table_type is not None:
            self.table_type = table_type
        if with_detail is not None:
            self.with_detail = with_detail
        if with_priv is not None:
            self.with_priv = with_priv

    @property
    def database_name(self):
        """Gets the database_name of this ListAllTablesRequest.

        查看表所在的数据库名称。

        :return: The database_name of this ListAllTablesRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ListAllTablesRequest.

        查看表所在的数据库名称。

        :param database_name: The database_name of this ListAllTablesRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def current_page(self):
        """Gets the current_page of this ListAllTablesRequest.


        :return: The current_page of this ListAllTablesRequest.
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this ListAllTablesRequest.


        :param current_page: The current_page of this ListAllTablesRequest.
        :type current_page: int
        """
        self._current_page = current_page

    @property
    def keyword(self):
        """Gets the keyword of this ListAllTablesRequest.

        过滤表名称的关键词。

        :return: The keyword of this ListAllTablesRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this ListAllTablesRequest.

        过滤表名称的关键词。

        :param keyword: The keyword of this ListAllTablesRequest.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def page_size(self):
        """Gets the page_size of this ListAllTablesRequest.


        :return: The page_size of this ListAllTablesRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListAllTablesRequest.


        :param page_size: The page_size of this ListAllTablesRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def table_type(self):
        """Gets the table_type of this ListAllTablesRequest.


        :return: The table_type of this ListAllTablesRequest.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        """Sets the table_type of this ListAllTablesRequest.


        :param table_type: The table_type of this ListAllTablesRequest.
        :type table_type: str
        """
        self._table_type = table_type

    @property
    def with_detail(self):
        """Gets the with_detail of this ListAllTablesRequest.

        是否获取表的详细信息（所有者，size等）。

        :return: The with_detail of this ListAllTablesRequest.
        :rtype: bool
        """
        return self._with_detail

    @with_detail.setter
    def with_detail(self, with_detail):
        """Sets the with_detail of this ListAllTablesRequest.

        是否获取表的详细信息（所有者，size等）。

        :param with_detail: The with_detail of this ListAllTablesRequest.
        :type with_detail: bool
        """
        self._with_detail = with_detail

    @property
    def with_priv(self):
        """Gets the with_priv of this ListAllTablesRequest.


        :return: The with_priv of this ListAllTablesRequest.
        :rtype: bool
        """
        return self._with_priv

    @with_priv.setter
    def with_priv(self, with_priv):
        """Sets the with_priv of this ListAllTablesRequest.


        :param with_priv: The with_priv of this ListAllTablesRequest.
        :type with_priv: bool
        """
        self._with_priv = with_priv

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
        if not isinstance(other, ListAllTablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
