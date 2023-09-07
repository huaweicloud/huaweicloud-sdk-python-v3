# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesResourceMetricsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine': 'str',
        'search_field': 'str',
        'offset': 'str',
        'limit': 'str',
        'order': 'str',
        'sort_field': 'str'
    }

    attribute_map = {
        'engine': 'engine',
        'search_field': 'search_field',
        'offset': 'offset',
        'limit': 'limit',
        'order': 'order',
        'sort_field': 'sort_field'
    }

    def __init__(self, engine=None, search_field=None, offset=None, limit=None, order=None, sort_field=None):
        """ListInstancesResourceMetricsRequest

        The model defined in huaweicloud sdk

        :param engine: 引擎类型
        :type engine: str
        :param search_field: 搜索字段
        :type search_field: str
        :param offset: 索引位置，偏移量
        :type offset: str
        :param limit: 查询数据条数
        :type limit: str
        :param order: 排序方式
        :type order: str
        :param sort_field: 排序字段
        :type sort_field: str
        """
        
        

        self._engine = None
        self._search_field = None
        self._offset = None
        self._limit = None
        self._order = None
        self._sort_field = None
        self.discriminator = None

        self.engine = engine
        if search_field is not None:
            self.search_field = search_field
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order is not None:
            self.order = order
        if sort_field is not None:
            self.sort_field = sort_field

    @property
    def engine(self):
        """Gets the engine of this ListInstancesResourceMetricsRequest.

        引擎类型

        :return: The engine of this ListInstancesResourceMetricsRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ListInstancesResourceMetricsRequest.

        引擎类型

        :param engine: The engine of this ListInstancesResourceMetricsRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def search_field(self):
        """Gets the search_field of this ListInstancesResourceMetricsRequest.

        搜索字段

        :return: The search_field of this ListInstancesResourceMetricsRequest.
        :rtype: str
        """
        return self._search_field

    @search_field.setter
    def search_field(self, search_field):
        """Sets the search_field of this ListInstancesResourceMetricsRequest.

        搜索字段

        :param search_field: The search_field of this ListInstancesResourceMetricsRequest.
        :type search_field: str
        """
        self._search_field = search_field

    @property
    def offset(self):
        """Gets the offset of this ListInstancesResourceMetricsRequest.

        索引位置，偏移量

        :return: The offset of this ListInstancesResourceMetricsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListInstancesResourceMetricsRequest.

        索引位置，偏移量

        :param offset: The offset of this ListInstancesResourceMetricsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListInstancesResourceMetricsRequest.

        查询数据条数

        :return: The limit of this ListInstancesResourceMetricsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListInstancesResourceMetricsRequest.

        查询数据条数

        :param limit: The limit of this ListInstancesResourceMetricsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def order(self):
        """Gets the order of this ListInstancesResourceMetricsRequest.

        排序方式

        :return: The order of this ListInstancesResourceMetricsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListInstancesResourceMetricsRequest.

        排序方式

        :param order: The order of this ListInstancesResourceMetricsRequest.
        :type order: str
        """
        self._order = order

    @property
    def sort_field(self):
        """Gets the sort_field of this ListInstancesResourceMetricsRequest.

        排序字段

        :return: The sort_field of this ListInstancesResourceMetricsRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this ListInstancesResourceMetricsRequest.

        排序字段

        :param sort_field: The sort_field of this ListInstancesResourceMetricsRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

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
        if not isinstance(other, ListInstancesResourceMetricsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
