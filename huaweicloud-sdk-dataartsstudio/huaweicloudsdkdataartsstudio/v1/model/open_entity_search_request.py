# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenEntitySearchRequest:

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
        'type_names': 'list[str]',
        'connection_names': 'list[str]',
        'search_all_attributes': 'bool',
        'tags': 'list[str]',
        'limit': 'int',
        'offset': 'int',
        'attributes': 'object',
        'filter_criteria': 'FilterCriteria',
        'time_range': 'TimeRange',
        'scroll_id': 'str',
        'security_levels': 'list[str]',
        'is_import': 'bool',
        'classifications': 'list[str]',
        'description': 'str'
    }

    attribute_map = {
        'query': 'query',
        'type_names': 'type_names',
        'connection_names': 'connection_names',
        'search_all_attributes': 'search_all_attributes',
        'tags': 'tags',
        'limit': 'limit',
        'offset': 'offset',
        'attributes': 'attributes',
        'filter_criteria': 'filter_criteria',
        'time_range': 'time_range',
        'scroll_id': 'scroll_id',
        'security_levels': 'security_levels',
        'is_import': 'is_import',
        'classifications': 'classifications',
        'description': 'description'
    }

    def __init__(self, query=None, type_names=None, connection_names=None, search_all_attributes=None, tags=None, limit=None, offset=None, attributes=None, filter_criteria=None, time_range=None, scroll_id=None, security_levels=None, is_import=None, classifications=None, description=None):
        """OpenEntitySearchRequest

        The model defined in huaweicloud sdk

        :param query: 查询关键字
        :type query: str
        :param type_names: 分类名称 List&lt;String&gt;
        :type type_names: list[str]
        :param connection_names: List&lt;String&gt; 连接名称
        :type connection_names: list[str]
        :param search_all_attributes: 查询关键字是否匹配资产的名称描述信息，true:匹配所有属性，false:只匹配名称、描述，默认false
        :type search_all_attributes: bool
        :param tags: List&lt;String&gt; 标签的名称
        :type tags: list[str]
        :param limit: 分页显示每页返回结果数。默认值，10
        :type limit: int
        :param offset: 偏移量，默认值，0
        :type offset: int
        :param attributes: key当前支持Table，value可为以下中的一个或多个：rowCounts、tableSize、database、schema、namespace、ddlUpdateTime、dataUpdateTime、ddlCreateTime Map&lt;String,Set&lt;String&gt;&gt;
        :type attributes: object
        :param filter_criteria: 
        :type filter_criteria: :class:`huaweicloudsdkdataartsstudio.v1.FilterCriteria`
        :param time_range: 
        :type time_range: :class:`huaweicloudsdkdataartsstudio.v1.TimeRange`
        :param scroll_id: scroll_id
        :type scroll_id: str
        :param security_levels: List&lt;String&gt; 安全级别
        :type security_levels: list[str]
        :param is_import: 是否导入
        :type is_import: bool
        :param classifications: List&lt;String&gt; 分类
        :type classifications: list[str]
        :param description: 描述
        :type description: str
        """
        
        

        self._query = None
        self._type_names = None
        self._connection_names = None
        self._search_all_attributes = None
        self._tags = None
        self._limit = None
        self._offset = None
        self._attributes = None
        self._filter_criteria = None
        self._time_range = None
        self._scroll_id = None
        self._security_levels = None
        self._is_import = None
        self._classifications = None
        self._description = None
        self.discriminator = None

        self.query = query
        self.type_names = type_names
        if connection_names is not None:
            self.connection_names = connection_names
        if search_all_attributes is not None:
            self.search_all_attributes = search_all_attributes
        if tags is not None:
            self.tags = tags
        self.limit = limit
        if offset is not None:
            self.offset = offset
        if attributes is not None:
            self.attributes = attributes
        if filter_criteria is not None:
            self.filter_criteria = filter_criteria
        if time_range is not None:
            self.time_range = time_range
        if scroll_id is not None:
            self.scroll_id = scroll_id
        if security_levels is not None:
            self.security_levels = security_levels
        if is_import is not None:
            self.is_import = is_import
        if classifications is not None:
            self.classifications = classifications
        if description is not None:
            self.description = description

    @property
    def query(self):
        """Gets the query of this OpenEntitySearchRequest.

        查询关键字

        :return: The query of this OpenEntitySearchRequest.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this OpenEntitySearchRequest.

        查询关键字

        :param query: The query of this OpenEntitySearchRequest.
        :type query: str
        """
        self._query = query

    @property
    def type_names(self):
        """Gets the type_names of this OpenEntitySearchRequest.

        分类名称 List<String>

        :return: The type_names of this OpenEntitySearchRequest.
        :rtype: list[str]
        """
        return self._type_names

    @type_names.setter
    def type_names(self, type_names):
        """Sets the type_names of this OpenEntitySearchRequest.

        分类名称 List<String>

        :param type_names: The type_names of this OpenEntitySearchRequest.
        :type type_names: list[str]
        """
        self._type_names = type_names

    @property
    def connection_names(self):
        """Gets the connection_names of this OpenEntitySearchRequest.

        List<String> 连接名称

        :return: The connection_names of this OpenEntitySearchRequest.
        :rtype: list[str]
        """
        return self._connection_names

    @connection_names.setter
    def connection_names(self, connection_names):
        """Sets the connection_names of this OpenEntitySearchRequest.

        List<String> 连接名称

        :param connection_names: The connection_names of this OpenEntitySearchRequest.
        :type connection_names: list[str]
        """
        self._connection_names = connection_names

    @property
    def search_all_attributes(self):
        """Gets the search_all_attributes of this OpenEntitySearchRequest.

        查询关键字是否匹配资产的名称描述信息，true:匹配所有属性，false:只匹配名称、描述，默认false

        :return: The search_all_attributes of this OpenEntitySearchRequest.
        :rtype: bool
        """
        return self._search_all_attributes

    @search_all_attributes.setter
    def search_all_attributes(self, search_all_attributes):
        """Sets the search_all_attributes of this OpenEntitySearchRequest.

        查询关键字是否匹配资产的名称描述信息，true:匹配所有属性，false:只匹配名称、描述，默认false

        :param search_all_attributes: The search_all_attributes of this OpenEntitySearchRequest.
        :type search_all_attributes: bool
        """
        self._search_all_attributes = search_all_attributes

    @property
    def tags(self):
        """Gets the tags of this OpenEntitySearchRequest.

        List<String> 标签的名称

        :return: The tags of this OpenEntitySearchRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this OpenEntitySearchRequest.

        List<String> 标签的名称

        :param tags: The tags of this OpenEntitySearchRequest.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def limit(self):
        """Gets the limit of this OpenEntitySearchRequest.

        分页显示每页返回结果数。默认值，10

        :return: The limit of this OpenEntitySearchRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this OpenEntitySearchRequest.

        分页显示每页返回结果数。默认值，10

        :param limit: The limit of this OpenEntitySearchRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this OpenEntitySearchRequest.

        偏移量，默认值，0

        :return: The offset of this OpenEntitySearchRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this OpenEntitySearchRequest.

        偏移量，默认值，0

        :param offset: The offset of this OpenEntitySearchRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def attributes(self):
        """Gets the attributes of this OpenEntitySearchRequest.

        key当前支持Table，value可为以下中的一个或多个：rowCounts、tableSize、database、schema、namespace、ddlUpdateTime、dataUpdateTime、ddlCreateTime Map<String,Set<String>>

        :return: The attributes of this OpenEntitySearchRequest.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this OpenEntitySearchRequest.

        key当前支持Table，value可为以下中的一个或多个：rowCounts、tableSize、database、schema、namespace、ddlUpdateTime、dataUpdateTime、ddlCreateTime Map<String,Set<String>>

        :param attributes: The attributes of this OpenEntitySearchRequest.
        :type attributes: object
        """
        self._attributes = attributes

    @property
    def filter_criteria(self):
        """Gets the filter_criteria of this OpenEntitySearchRequest.

        :return: The filter_criteria of this OpenEntitySearchRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.FilterCriteria`
        """
        return self._filter_criteria

    @filter_criteria.setter
    def filter_criteria(self, filter_criteria):
        """Sets the filter_criteria of this OpenEntitySearchRequest.

        :param filter_criteria: The filter_criteria of this OpenEntitySearchRequest.
        :type filter_criteria: :class:`huaweicloudsdkdataartsstudio.v1.FilterCriteria`
        """
        self._filter_criteria = filter_criteria

    @property
    def time_range(self):
        """Gets the time_range of this OpenEntitySearchRequest.

        :return: The time_range of this OpenEntitySearchRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.TimeRange`
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this OpenEntitySearchRequest.

        :param time_range: The time_range of this OpenEntitySearchRequest.
        :type time_range: :class:`huaweicloudsdkdataartsstudio.v1.TimeRange`
        """
        self._time_range = time_range

    @property
    def scroll_id(self):
        """Gets the scroll_id of this OpenEntitySearchRequest.

        scroll_id

        :return: The scroll_id of this OpenEntitySearchRequest.
        :rtype: str
        """
        return self._scroll_id

    @scroll_id.setter
    def scroll_id(self, scroll_id):
        """Sets the scroll_id of this OpenEntitySearchRequest.

        scroll_id

        :param scroll_id: The scroll_id of this OpenEntitySearchRequest.
        :type scroll_id: str
        """
        self._scroll_id = scroll_id

    @property
    def security_levels(self):
        """Gets the security_levels of this OpenEntitySearchRequest.

        List<String> 安全级别

        :return: The security_levels of this OpenEntitySearchRequest.
        :rtype: list[str]
        """
        return self._security_levels

    @security_levels.setter
    def security_levels(self, security_levels):
        """Sets the security_levels of this OpenEntitySearchRequest.

        List<String> 安全级别

        :param security_levels: The security_levels of this OpenEntitySearchRequest.
        :type security_levels: list[str]
        """
        self._security_levels = security_levels

    @property
    def is_import(self):
        """Gets the is_import of this OpenEntitySearchRequest.

        是否导入

        :return: The is_import of this OpenEntitySearchRequest.
        :rtype: bool
        """
        return self._is_import

    @is_import.setter
    def is_import(self, is_import):
        """Sets the is_import of this OpenEntitySearchRequest.

        是否导入

        :param is_import: The is_import of this OpenEntitySearchRequest.
        :type is_import: bool
        """
        self._is_import = is_import

    @property
    def classifications(self):
        """Gets the classifications of this OpenEntitySearchRequest.

        List<String> 分类

        :return: The classifications of this OpenEntitySearchRequest.
        :rtype: list[str]
        """
        return self._classifications

    @classifications.setter
    def classifications(self, classifications):
        """Sets the classifications of this OpenEntitySearchRequest.

        List<String> 分类

        :param classifications: The classifications of this OpenEntitySearchRequest.
        :type classifications: list[str]
        """
        self._classifications = classifications

    @property
    def description(self):
        """Gets the description of this OpenEntitySearchRequest.

        描述

        :return: The description of this OpenEntitySearchRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OpenEntitySearchRequest.

        描述

        :param description: The description of this OpenEntitySearchRequest.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, OpenEntitySearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
