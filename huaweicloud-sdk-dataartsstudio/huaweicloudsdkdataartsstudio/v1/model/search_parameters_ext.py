# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchParametersExt:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attributes': 'object',
        'classifications': 'list[str]',
        'connection_names': 'list[str]',
        'exclude_classifications': 'bool',
        'exclude_security_levels': 'bool',
        'exclude_tags': 'bool',
        'include_classification_attributes': 'bool',
        'include_sub_classifications': 'bool',
        'limit': 'int',
        'offset': 'int',
        'order': 'str',
        'query': 'str',
        'search_name_and_description': 'bool',
        'security_levels': 'list[str]',
        'term_names': 'list[str]',
        'type_names': 'list[str]'
    }

    attribute_map = {
        'attributes': 'attributes',
        'classifications': 'classifications',
        'connection_names': 'connection_names',
        'exclude_classifications': 'exclude_classifications',
        'exclude_security_levels': 'exclude_security_levels',
        'exclude_tags': 'exclude_tags',
        'include_classification_attributes': 'include_classification_attributes',
        'include_sub_classifications': 'include_sub_classifications',
        'limit': 'limit',
        'offset': 'offset',
        'order': 'order',
        'query': 'query',
        'search_name_and_description': 'search_name_and_description',
        'security_levels': 'security_levels',
        'term_names': 'term_names',
        'type_names': 'type_names'
    }

    def __init__(self, attributes=None, classifications=None, connection_names=None, exclude_classifications=None, exclude_security_levels=None, exclude_tags=None, include_classification_attributes=None, include_sub_classifications=None, limit=None, offset=None, order=None, query=None, search_name_and_description=None, security_levels=None, term_names=None, type_names=None):
        r"""SearchParametersExt

        The model defined in huaweicloud sdk

        :param attributes: 属性
        :type attributes: object
        :param classifications: 分类
        :type classifications: list[str]
        :param connection_names: 数据连接
        :type connection_names: list[str]
        :param exclude_classifications: 是否排除分类
        :type exclude_classifications: bool
        :param exclude_security_levels: 是否排除密级
        :type exclude_security_levels: bool
        :param exclude_tags: 是否排除标签
        :type exclude_tags: bool
        :param include_classification_attributes: 包含分类属性
        :type include_classification_attributes: bool
        :param include_sub_classifications: 包含子分类
        :type include_sub_classifications: bool
        :param limit: 分页参数，每页限制数量，默认查询所有
        :type limit: int
        :param offset: 分页参数，偏移量，默认查询所有
        :type offset: int
        :param order: 排序方式
        :type order: str
        :param query: 查询参数
        :type query: str
        :param search_name_and_description: 是否按名称和描述搜索
        :type search_name_and_description: bool
        :param security_levels: 安全密级列表
        :type security_levels: list[str]
        :param term_names: 标签列表
        :type term_names: list[str]
        :param type_names: 类型列表
        :type type_names: list[str]
        """
        
        

        self._attributes = None
        self._classifications = None
        self._connection_names = None
        self._exclude_classifications = None
        self._exclude_security_levels = None
        self._exclude_tags = None
        self._include_classification_attributes = None
        self._include_sub_classifications = None
        self._limit = None
        self._offset = None
        self._order = None
        self._query = None
        self._search_name_and_description = None
        self._security_levels = None
        self._term_names = None
        self._type_names = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        if classifications is not None:
            self.classifications = classifications
        if connection_names is not None:
            self.connection_names = connection_names
        if exclude_classifications is not None:
            self.exclude_classifications = exclude_classifications
        if exclude_security_levels is not None:
            self.exclude_security_levels = exclude_security_levels
        if exclude_tags is not None:
            self.exclude_tags = exclude_tags
        if include_classification_attributes is not None:
            self.include_classification_attributes = include_classification_attributes
        if include_sub_classifications is not None:
            self.include_sub_classifications = include_sub_classifications
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if order is not None:
            self.order = order
        if query is not None:
            self.query = query
        if search_name_and_description is not None:
            self.search_name_and_description = search_name_and_description
        if security_levels is not None:
            self.security_levels = security_levels
        if term_names is not None:
            self.term_names = term_names
        if type_names is not None:
            self.type_names = type_names

    @property
    def attributes(self):
        r"""Gets the attributes of this SearchParametersExt.

        属性

        :return: The attributes of this SearchParametersExt.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this SearchParametersExt.

        属性

        :param attributes: The attributes of this SearchParametersExt.
        :type attributes: object
        """
        self._attributes = attributes

    @property
    def classifications(self):
        r"""Gets the classifications of this SearchParametersExt.

        分类

        :return: The classifications of this SearchParametersExt.
        :rtype: list[str]
        """
        return self._classifications

    @classifications.setter
    def classifications(self, classifications):
        r"""Sets the classifications of this SearchParametersExt.

        分类

        :param classifications: The classifications of this SearchParametersExt.
        :type classifications: list[str]
        """
        self._classifications = classifications

    @property
    def connection_names(self):
        r"""Gets the connection_names of this SearchParametersExt.

        数据连接

        :return: The connection_names of this SearchParametersExt.
        :rtype: list[str]
        """
        return self._connection_names

    @connection_names.setter
    def connection_names(self, connection_names):
        r"""Sets the connection_names of this SearchParametersExt.

        数据连接

        :param connection_names: The connection_names of this SearchParametersExt.
        :type connection_names: list[str]
        """
        self._connection_names = connection_names

    @property
    def exclude_classifications(self):
        r"""Gets the exclude_classifications of this SearchParametersExt.

        是否排除分类

        :return: The exclude_classifications of this SearchParametersExt.
        :rtype: bool
        """
        return self._exclude_classifications

    @exclude_classifications.setter
    def exclude_classifications(self, exclude_classifications):
        r"""Sets the exclude_classifications of this SearchParametersExt.

        是否排除分类

        :param exclude_classifications: The exclude_classifications of this SearchParametersExt.
        :type exclude_classifications: bool
        """
        self._exclude_classifications = exclude_classifications

    @property
    def exclude_security_levels(self):
        r"""Gets the exclude_security_levels of this SearchParametersExt.

        是否排除密级

        :return: The exclude_security_levels of this SearchParametersExt.
        :rtype: bool
        """
        return self._exclude_security_levels

    @exclude_security_levels.setter
    def exclude_security_levels(self, exclude_security_levels):
        r"""Sets the exclude_security_levels of this SearchParametersExt.

        是否排除密级

        :param exclude_security_levels: The exclude_security_levels of this SearchParametersExt.
        :type exclude_security_levels: bool
        """
        self._exclude_security_levels = exclude_security_levels

    @property
    def exclude_tags(self):
        r"""Gets the exclude_tags of this SearchParametersExt.

        是否排除标签

        :return: The exclude_tags of this SearchParametersExt.
        :rtype: bool
        """
        return self._exclude_tags

    @exclude_tags.setter
    def exclude_tags(self, exclude_tags):
        r"""Sets the exclude_tags of this SearchParametersExt.

        是否排除标签

        :param exclude_tags: The exclude_tags of this SearchParametersExt.
        :type exclude_tags: bool
        """
        self._exclude_tags = exclude_tags

    @property
    def include_classification_attributes(self):
        r"""Gets the include_classification_attributes of this SearchParametersExt.

        包含分类属性

        :return: The include_classification_attributes of this SearchParametersExt.
        :rtype: bool
        """
        return self._include_classification_attributes

    @include_classification_attributes.setter
    def include_classification_attributes(self, include_classification_attributes):
        r"""Sets the include_classification_attributes of this SearchParametersExt.

        包含分类属性

        :param include_classification_attributes: The include_classification_attributes of this SearchParametersExt.
        :type include_classification_attributes: bool
        """
        self._include_classification_attributes = include_classification_attributes

    @property
    def include_sub_classifications(self):
        r"""Gets the include_sub_classifications of this SearchParametersExt.

        包含子分类

        :return: The include_sub_classifications of this SearchParametersExt.
        :rtype: bool
        """
        return self._include_sub_classifications

    @include_sub_classifications.setter
    def include_sub_classifications(self, include_sub_classifications):
        r"""Sets the include_sub_classifications of this SearchParametersExt.

        包含子分类

        :param include_sub_classifications: The include_sub_classifications of this SearchParametersExt.
        :type include_sub_classifications: bool
        """
        self._include_sub_classifications = include_sub_classifications

    @property
    def limit(self):
        r"""Gets the limit of this SearchParametersExt.

        分页参数，每页限制数量，默认查询所有

        :return: The limit of this SearchParametersExt.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this SearchParametersExt.

        分页参数，每页限制数量，默认查询所有

        :param limit: The limit of this SearchParametersExt.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this SearchParametersExt.

        分页参数，偏移量，默认查询所有

        :return: The offset of this SearchParametersExt.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this SearchParametersExt.

        分页参数，偏移量，默认查询所有

        :param offset: The offset of this SearchParametersExt.
        :type offset: int
        """
        self._offset = offset

    @property
    def order(self):
        r"""Gets the order of this SearchParametersExt.

        排序方式

        :return: The order of this SearchParametersExt.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this SearchParametersExt.

        排序方式

        :param order: The order of this SearchParametersExt.
        :type order: str
        """
        self._order = order

    @property
    def query(self):
        r"""Gets the query of this SearchParametersExt.

        查询参数

        :return: The query of this SearchParametersExt.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this SearchParametersExt.

        查询参数

        :param query: The query of this SearchParametersExt.
        :type query: str
        """
        self._query = query

    @property
    def search_name_and_description(self):
        r"""Gets the search_name_and_description of this SearchParametersExt.

        是否按名称和描述搜索

        :return: The search_name_and_description of this SearchParametersExt.
        :rtype: bool
        """
        return self._search_name_and_description

    @search_name_and_description.setter
    def search_name_and_description(self, search_name_and_description):
        r"""Sets the search_name_and_description of this SearchParametersExt.

        是否按名称和描述搜索

        :param search_name_and_description: The search_name_and_description of this SearchParametersExt.
        :type search_name_and_description: bool
        """
        self._search_name_and_description = search_name_and_description

    @property
    def security_levels(self):
        r"""Gets the security_levels of this SearchParametersExt.

        安全密级列表

        :return: The security_levels of this SearchParametersExt.
        :rtype: list[str]
        """
        return self._security_levels

    @security_levels.setter
    def security_levels(self, security_levels):
        r"""Sets the security_levels of this SearchParametersExt.

        安全密级列表

        :param security_levels: The security_levels of this SearchParametersExt.
        :type security_levels: list[str]
        """
        self._security_levels = security_levels

    @property
    def term_names(self):
        r"""Gets the term_names of this SearchParametersExt.

        标签列表

        :return: The term_names of this SearchParametersExt.
        :rtype: list[str]
        """
        return self._term_names

    @term_names.setter
    def term_names(self, term_names):
        r"""Sets the term_names of this SearchParametersExt.

        标签列表

        :param term_names: The term_names of this SearchParametersExt.
        :type term_names: list[str]
        """
        self._term_names = term_names

    @property
    def type_names(self):
        r"""Gets the type_names of this SearchParametersExt.

        类型列表

        :return: The type_names of this SearchParametersExt.
        :rtype: list[str]
        """
        return self._type_names

    @type_names.setter
    def type_names(self, type_names):
        r"""Sets the type_names of this SearchParametersExt.

        类型列表

        :param type_names: The type_names of this SearchParametersExt.
        :type type_names: list[str]
        """
        self._type_names = type_names

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
        if not isinstance(other, SearchParametersExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
