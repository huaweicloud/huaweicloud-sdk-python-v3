# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopnRequstBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'end_time': 'int',
        'is_desc': 'bool',
        'resource_type': 'str',
        'sort_by': 'str',
        'start_time': 'int',
        'topn': 'int',
        'filter': 'dict(str, str)',
        'search_list': 'list[str]'
    }

    attribute_map = {
        'end_time': 'end_time',
        'is_desc': 'is_desc',
        'resource_type': 'resource_type',
        'sort_by': 'sort_by',
        'start_time': 'start_time',
        'topn': 'topn',
        'filter': 'filter',
        'search_list': 'search_list'
    }

    def __init__(self, end_time=None, is_desc=None, resource_type=None, sort_by=None, start_time=None, topn=None, filter=None, search_list=None):
        """TopnRequstBody

        The model defined in huaweicloud sdk

        :param end_time: 结束时间时间戳，毫秒时间
        :type end_time: int
        :param is_desc: 是否降序  true / false
        :type is_desc: bool
        :param resource_type: 资源类型，log_group / log_stream / tenant
        :type resource_type: str
        :param sort_by: 排序依据，index/write/storage/basicTransfer/seniorTransfer/coldStorage，必须是search_list中存在的数据
        :type sort_by: str
        :param start_time: 开始时间时间戳，毫秒时间，最多支持30天范围内的查询
        :type start_time: int
        :param topn: 查询前多少数据，范围1~100
        :type topn: int
        :param filter: 过滤条件 {     \&quot;log_group_id\&quot;: \&quot;xxxxxx\&quot; }过滤器，为一个map结构，键为过滤属性，值为属性值，不支持模糊匹配
        :type filter: dict(str, str)
        :param search_list: 查询数据类型，字符串数组可多种搭配，只能在index/write/storage/basicTransfer/seniorTransfer/coldStorage中选填
        :type search_list: list[str]
        """
        
        

        self._end_time = None
        self._is_desc = None
        self._resource_type = None
        self._sort_by = None
        self._start_time = None
        self._topn = None
        self._filter = None
        self._search_list = None
        self.discriminator = None

        self.end_time = end_time
        self.is_desc = is_desc
        self.resource_type = resource_type
        self.sort_by = sort_by
        self.start_time = start_time
        self.topn = topn
        self.filter = filter
        self.search_list = search_list

    @property
    def end_time(self):
        """Gets the end_time of this TopnRequstBody.

        结束时间时间戳，毫秒时间

        :return: The end_time of this TopnRequstBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TopnRequstBody.

        结束时间时间戳，毫秒时间

        :param end_time: The end_time of this TopnRequstBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def is_desc(self):
        """Gets the is_desc of this TopnRequstBody.

        是否降序  true / false

        :return: The is_desc of this TopnRequstBody.
        :rtype: bool
        """
        return self._is_desc

    @is_desc.setter
    def is_desc(self, is_desc):
        """Sets the is_desc of this TopnRequstBody.

        是否降序  true / false

        :param is_desc: The is_desc of this TopnRequstBody.
        :type is_desc: bool
        """
        self._is_desc = is_desc

    @property
    def resource_type(self):
        """Gets the resource_type of this TopnRequstBody.

        资源类型，log_group / log_stream / tenant

        :return: The resource_type of this TopnRequstBody.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this TopnRequstBody.

        资源类型，log_group / log_stream / tenant

        :param resource_type: The resource_type of this TopnRequstBody.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def sort_by(self):
        """Gets the sort_by of this TopnRequstBody.

        排序依据，index/write/storage/basicTransfer/seniorTransfer/coldStorage，必须是search_list中存在的数据

        :return: The sort_by of this TopnRequstBody.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this TopnRequstBody.

        排序依据，index/write/storage/basicTransfer/seniorTransfer/coldStorage，必须是search_list中存在的数据

        :param sort_by: The sort_by of this TopnRequstBody.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def start_time(self):
        """Gets the start_time of this TopnRequstBody.

        开始时间时间戳，毫秒时间，最多支持30天范围内的查询

        :return: The start_time of this TopnRequstBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TopnRequstBody.

        开始时间时间戳，毫秒时间，最多支持30天范围内的查询

        :param start_time: The start_time of this TopnRequstBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def topn(self):
        """Gets the topn of this TopnRequstBody.

        查询前多少数据，范围1~100

        :return: The topn of this TopnRequstBody.
        :rtype: int
        """
        return self._topn

    @topn.setter
    def topn(self, topn):
        """Sets the topn of this TopnRequstBody.

        查询前多少数据，范围1~100

        :param topn: The topn of this TopnRequstBody.
        :type topn: int
        """
        self._topn = topn

    @property
    def filter(self):
        """Gets the filter of this TopnRequstBody.

        过滤条件 {     \"log_group_id\": \"xxxxxx\" }过滤器，为一个map结构，键为过滤属性，值为属性值，不支持模糊匹配

        :return: The filter of this TopnRequstBody.
        :rtype: dict(str, str)
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this TopnRequstBody.

        过滤条件 {     \"log_group_id\": \"xxxxxx\" }过滤器，为一个map结构，键为过滤属性，值为属性值，不支持模糊匹配

        :param filter: The filter of this TopnRequstBody.
        :type filter: dict(str, str)
        """
        self._filter = filter

    @property
    def search_list(self):
        """Gets the search_list of this TopnRequstBody.

        查询数据类型，字符串数组可多种搭配，只能在index/write/storage/basicTransfer/seniorTransfer/coldStorage中选填

        :return: The search_list of this TopnRequstBody.
        :rtype: list[str]
        """
        return self._search_list

    @search_list.setter
    def search_list(self, search_list):
        """Sets the search_list of this TopnRequstBody.

        查询数据类型，字符串数组可多种搭配，只能在index/write/storage/basicTransfer/seniorTransfer/coldStorage中选填

        :param search_list: The search_list of this TopnRequstBody.
        :type search_list: list[str]
        """
        self._search_list = search_list

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
        if not isinstance(other, TopnRequstBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
