# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicationTableInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_name': 'str',
        'schema': 'str',
        'columns': 'list[str]',
        'primary_key': 'list[str]',
        'filter_statement': 'str',
        'filter': 'PublicationTableFilterInfoRequest',
        'article_properties': 'ArticlePropertiesRequest'
    }

    attribute_map = {
        'table_name': 'table_name',
        'schema': 'schema',
        'columns': 'columns',
        'primary_key': 'primary_key',
        'filter_statement': 'filter_statement',
        'filter': 'filter',
        'article_properties': 'article_properties'
    }

    def __init__(self, table_name=None, schema=None, columns=None, primary_key=None, filter_statement=None, filter=None, article_properties=None):
        r"""PublicationTableInfoRequest

        The model defined in huaweicloud sdk

        :param table_name: 表名。  表名长度可在1～64个字符之间，由字母、数字或下划线组成，不能包含其他特殊字符
        :type table_name: str
        :param schema: 命名空间。默认值dbo。
        :type schema: str
        :param columns: 发布的字段（不传或为空说明选择所有字段）。  字段名称长度可在1～64个字符之间，由字母、数字或下划线组成，不能包含其他特殊字符
        :type columns: list[str]
        :param primary_key: 主键。
        :type primary_key: list[str]
        :param filter_statement: 筛选语句。不能包含英文单引号&#39;。
        :type filter_statement: str
        :param filter: 
        :type filter: :class:`huaweicloudsdkrds.v3.PublicationTableFilterInfoRequest`
        :param article_properties: 
        :type article_properties: :class:`huaweicloudsdkrds.v3.ArticlePropertiesRequest`
        """
        
        

        self._table_name = None
        self._schema = None
        self._columns = None
        self._primary_key = None
        self._filter_statement = None
        self._filter = None
        self._article_properties = None
        self.discriminator = None

        self.table_name = table_name
        if schema is not None:
            self.schema = schema
        if columns is not None:
            self.columns = columns
        if primary_key is not None:
            self.primary_key = primary_key
        if filter_statement is not None:
            self.filter_statement = filter_statement
        if filter is not None:
            self.filter = filter
        if article_properties is not None:
            self.article_properties = article_properties

    @property
    def table_name(self):
        r"""Gets the table_name of this PublicationTableInfoRequest.

        表名。  表名长度可在1～64个字符之间，由字母、数字或下划线组成，不能包含其他特殊字符

        :return: The table_name of this PublicationTableInfoRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this PublicationTableInfoRequest.

        表名。  表名长度可在1～64个字符之间，由字母、数字或下划线组成，不能包含其他特殊字符

        :param table_name: The table_name of this PublicationTableInfoRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def schema(self):
        r"""Gets the schema of this PublicationTableInfoRequest.

        命名空间。默认值dbo。

        :return: The schema of this PublicationTableInfoRequest.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this PublicationTableInfoRequest.

        命名空间。默认值dbo。

        :param schema: The schema of this PublicationTableInfoRequest.
        :type schema: str
        """
        self._schema = schema

    @property
    def columns(self):
        r"""Gets the columns of this PublicationTableInfoRequest.

        发布的字段（不传或为空说明选择所有字段）。  字段名称长度可在1～64个字符之间，由字母、数字或下划线组成，不能包含其他特殊字符

        :return: The columns of this PublicationTableInfoRequest.
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        r"""Sets the columns of this PublicationTableInfoRequest.

        发布的字段（不传或为空说明选择所有字段）。  字段名称长度可在1～64个字符之间，由字母、数字或下划线组成，不能包含其他特殊字符

        :param columns: The columns of this PublicationTableInfoRequest.
        :type columns: list[str]
        """
        self._columns = columns

    @property
    def primary_key(self):
        r"""Gets the primary_key of this PublicationTableInfoRequest.

        主键。

        :return: The primary_key of this PublicationTableInfoRequest.
        :rtype: list[str]
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        r"""Sets the primary_key of this PublicationTableInfoRequest.

        主键。

        :param primary_key: The primary_key of this PublicationTableInfoRequest.
        :type primary_key: list[str]
        """
        self._primary_key = primary_key

    @property
    def filter_statement(self):
        r"""Gets the filter_statement of this PublicationTableInfoRequest.

        筛选语句。不能包含英文单引号'。

        :return: The filter_statement of this PublicationTableInfoRequest.
        :rtype: str
        """
        return self._filter_statement

    @filter_statement.setter
    def filter_statement(self, filter_statement):
        r"""Sets the filter_statement of this PublicationTableInfoRequest.

        筛选语句。不能包含英文单引号'。

        :param filter_statement: The filter_statement of this PublicationTableInfoRequest.
        :type filter_statement: str
        """
        self._filter_statement = filter_statement

    @property
    def filter(self):
        r"""Gets the filter of this PublicationTableInfoRequest.

        :return: The filter of this PublicationTableInfoRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.PublicationTableFilterInfoRequest`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this PublicationTableInfoRequest.

        :param filter: The filter of this PublicationTableInfoRequest.
        :type filter: :class:`huaweicloudsdkrds.v3.PublicationTableFilterInfoRequest`
        """
        self._filter = filter

    @property
    def article_properties(self):
        r"""Gets the article_properties of this PublicationTableInfoRequest.

        :return: The article_properties of this PublicationTableInfoRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.ArticlePropertiesRequest`
        """
        return self._article_properties

    @article_properties.setter
    def article_properties(self, article_properties):
        r"""Sets the article_properties of this PublicationTableInfoRequest.

        :param article_properties: The article_properties of this PublicationTableInfoRequest.
        :type article_properties: :class:`huaweicloudsdkrds.v3.ArticlePropertiesRequest`
        """
        self._article_properties = article_properties

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
        if not isinstance(other, PublicationTableInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
