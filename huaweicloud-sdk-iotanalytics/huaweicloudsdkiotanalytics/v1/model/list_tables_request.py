# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTablesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keyword': 'str',
        'tag': 'str',
        'offset': 'int',
        'limit': 'int',
        'order_by': 'str',
        'order': 'str'
    }

    attribute_map = {
        'keyword': 'keyword',
        'tag': 'tag',
        'offset': 'offset',
        'limit': 'limit',
        'order_by': 'order_by',
        'order': 'order'
    }

    def __init__(self, keyword=None, tag=None, offset=None, limit=None, order_by=None, order=None):
        r"""ListTablesRequest

        The model defined in huaweicloud sdk

        :param keyword: 过滤表名称的关键词。
        :type keyword: str
        :param tag: 过滤标签的关键字
        :type tag: str
        :param offset: 当前偏移量，默认为0。
        :type offset: int
        :param limit: 每页显示的最大作业个数，范围: [1, 100]。默认值：10。
        :type limit: int
        :param order_by: 指定作业排序字段，默认为created_time（作业创建时间），支持created_time(作业创建时间)、modified_time（作业更新时间） 、job_name（作业名称）三种排序字段。
        :type order_by: str
        :param order: 指定作业排序的升降序，默认为desc（降序），支持asc（升序）、desc（降序）两种排序方式。
        :type order: str
        """
        
        

        self._keyword = None
        self._tag = None
        self._offset = None
        self._limit = None
        self._order_by = None
        self._order = None
        self.discriminator = None

        if keyword is not None:
            self.keyword = keyword
        if tag is not None:
            self.tag = tag
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order_by is not None:
            self.order_by = order_by
        if order is not None:
            self.order = order

    @property
    def keyword(self):
        r"""Gets the keyword of this ListTablesRequest.

        过滤表名称的关键词。

        :return: The keyword of this ListTablesRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this ListTablesRequest.

        过滤表名称的关键词。

        :param keyword: The keyword of this ListTablesRequest.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def tag(self):
        r"""Gets the tag of this ListTablesRequest.

        过滤标签的关键字

        :return: The tag of this ListTablesRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListTablesRequest.

        过滤标签的关键字

        :param tag: The tag of this ListTablesRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def offset(self):
        r"""Gets the offset of this ListTablesRequest.

        当前偏移量，默认为0。

        :return: The offset of this ListTablesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTablesRequest.

        当前偏移量，默认为0。

        :param offset: The offset of this ListTablesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTablesRequest.

        每页显示的最大作业个数，范围: [1, 100]。默认值：10。

        :return: The limit of this ListTablesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTablesRequest.

        每页显示的最大作业个数，范围: [1, 100]。默认值：10。

        :param limit: The limit of this ListTablesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order_by(self):
        r"""Gets the order_by of this ListTablesRequest.

        指定作业排序字段，默认为created_time（作业创建时间），支持created_time(作业创建时间)、modified_time（作业更新时间） 、job_name（作业名称）三种排序字段。

        :return: The order_by of this ListTablesRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListTablesRequest.

        指定作业排序字段，默认为created_time（作业创建时间），支持created_time(作业创建时间)、modified_time（作业更新时间） 、job_name（作业名称）三种排序字段。

        :param order_by: The order_by of this ListTablesRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order(self):
        r"""Gets the order of this ListTablesRequest.

        指定作业排序的升降序，默认为desc（降序），支持asc（升序）、desc（降序）两种排序方式。

        :return: The order of this ListTablesRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListTablesRequest.

        指定作业排序的升降序，默认为desc（降序），支持asc（升序）、desc（降序）两种排序方式。

        :param order: The order of this ListTablesRequest.
        :type order: str
        """
        self._order = order

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
        if not isinstance(other, ListTablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
