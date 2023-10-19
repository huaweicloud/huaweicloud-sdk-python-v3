# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query': 'str',
        'filter': 'DataMapFilterCriteria',
        'facets': 'list[str]',
        'limit': 'int',
        'offset': 'int',
        'relationship_attributes': 'list[str]',
        'sort': 'list[Sort]',
        'owner': 'str',
        'query_privilege': 'bool'
    }

    attribute_map = {
        'query': 'query',
        'filter': 'filter',
        'facets': 'facets',
        'limit': 'limit',
        'offset': 'offset',
        'relationship_attributes': 'relationship_attributes',
        'sort': 'sort',
        'owner': 'owner',
        'query_privilege': 'query_privilege'
    }

    def __init__(self, query=None, filter=None, facets=None, limit=None, offset=None, relationship_attributes=None, sort=None, owner=None, query_privilege=None):
        """SearchParameter

        The model defined in huaweicloud sdk

        :param query: 查询关键字
        :type query: str
        :param filter: 
        :type filter: :class:`huaweicloudsdkdataartsstudio.v1.DataMapFilterCriteria`
        :param facets: 条件参数列表
        :type facets: list[str]
        :param limit: 分页显示每页返回结果数。默认值100
        :type limit: int
        :param offset: 偏移量，默认值0
        :type offset: int
        :param relationship_attributes: 关联关系属性
        :type relationship_attributes: list[str]
        :param sort: 排序信息
        :type sort: list[:class:`huaweicloudsdkdataartsstudio.v1.Sort`]
        :param owner: 所有者
        :type owner: str
        :param query_privilege: 是否校验权限，默认值false
        :type query_privilege: bool
        """
        
        

        self._query = None
        self._filter = None
        self._facets = None
        self._limit = None
        self._offset = None
        self._relationship_attributes = None
        self._sort = None
        self._owner = None
        self._query_privilege = None
        self.discriminator = None

        if query is not None:
            self.query = query
        if filter is not None:
            self.filter = filter
        if facets is not None:
            self.facets = facets
        self.limit = limit
        self.offset = offset
        if relationship_attributes is not None:
            self.relationship_attributes = relationship_attributes
        if sort is not None:
            self.sort = sort
        if owner is not None:
            self.owner = owner
        if query_privilege is not None:
            self.query_privilege = query_privilege

    @property
    def query(self):
        """Gets the query of this SearchParameter.

        查询关键字

        :return: The query of this SearchParameter.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this SearchParameter.

        查询关键字

        :param query: The query of this SearchParameter.
        :type query: str
        """
        self._query = query

    @property
    def filter(self):
        """Gets the filter of this SearchParameter.

        :return: The filter of this SearchParameter.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DataMapFilterCriteria`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this SearchParameter.

        :param filter: The filter of this SearchParameter.
        :type filter: :class:`huaweicloudsdkdataartsstudio.v1.DataMapFilterCriteria`
        """
        self._filter = filter

    @property
    def facets(self):
        """Gets the facets of this SearchParameter.

        条件参数列表

        :return: The facets of this SearchParameter.
        :rtype: list[str]
        """
        return self._facets

    @facets.setter
    def facets(self, facets):
        """Sets the facets of this SearchParameter.

        条件参数列表

        :param facets: The facets of this SearchParameter.
        :type facets: list[str]
        """
        self._facets = facets

    @property
    def limit(self):
        """Gets the limit of this SearchParameter.

        分页显示每页返回结果数。默认值100

        :return: The limit of this SearchParameter.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchParameter.

        分页显示每页返回结果数。默认值100

        :param limit: The limit of this SearchParameter.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this SearchParameter.

        偏移量，默认值0

        :return: The offset of this SearchParameter.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchParameter.

        偏移量，默认值0

        :param offset: The offset of this SearchParameter.
        :type offset: int
        """
        self._offset = offset

    @property
    def relationship_attributes(self):
        """Gets the relationship_attributes of this SearchParameter.

        关联关系属性

        :return: The relationship_attributes of this SearchParameter.
        :rtype: list[str]
        """
        return self._relationship_attributes

    @relationship_attributes.setter
    def relationship_attributes(self, relationship_attributes):
        """Sets the relationship_attributes of this SearchParameter.

        关联关系属性

        :param relationship_attributes: The relationship_attributes of this SearchParameter.
        :type relationship_attributes: list[str]
        """
        self._relationship_attributes = relationship_attributes

    @property
    def sort(self):
        """Gets the sort of this SearchParameter.

        排序信息

        :return: The sort of this SearchParameter.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.Sort`]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this SearchParameter.

        排序信息

        :param sort: The sort of this SearchParameter.
        :type sort: list[:class:`huaweicloudsdkdataartsstudio.v1.Sort`]
        """
        self._sort = sort

    @property
    def owner(self):
        """Gets the owner of this SearchParameter.

        所有者

        :return: The owner of this SearchParameter.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this SearchParameter.

        所有者

        :param owner: The owner of this SearchParameter.
        :type owner: str
        """
        self._owner = owner

    @property
    def query_privilege(self):
        """Gets the query_privilege of this SearchParameter.

        是否校验权限，默认值false

        :return: The query_privilege of this SearchParameter.
        :rtype: bool
        """
        return self._query_privilege

    @query_privilege.setter
    def query_privilege(self, query_privilege):
        """Sets the query_privilege of this SearchParameter.

        是否校验权限，默认值false

        :param query_privilege: The query_privilege of this SearchParameter.
        :type query_privilege: bool
        """
        self._query_privilege = query_privilege

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
        if not isinstance(other, SearchParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
