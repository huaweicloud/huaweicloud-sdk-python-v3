# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMetricsDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'metric_name': 'str',
        'offset': 'int',
        'limit': 'int',
        '_from': 'int',
        'to': 'int',
        'order_by': 'str',
        'sort_by': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'metric_name': 'metric_name',
        'offset': 'offset',
        'limit': 'limit',
        '_from': 'from',
        'to': 'to',
        'order_by': 'order_by',
        'sort_by': 'sort_by'
    }

    def __init__(self, cluster_id=None, metric_name=None, offset=None, limit=None, _from=None, to=None, order_by=None, sort_by=None):
        """ListMetricsDataRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID。
        :type cluster_id: str
        :param metric_name: 指标名称。
        :type metric_name: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset&gt;&#x3D;0。
        :type offset: int
        :param limit: 每页显示的条目数量，最大1000。
        :type limit: int
        :param _from: 采集开始时间，13位时间戳。
        :type _from: int
        :param to: 采集结束时间，13位时间戳。开始时间到结束时间最多不超过一天。
        :type to: int
        :param order_by: 排序字段。固定取值。 ctime：采集时间。
        :type order_by: str
        :param sort_by: 正序还是倒叙。固定取值。 asc：正序。 desc：倒序。
        :type sort_by: str
        """
        
        

        self._cluster_id = None
        self._metric_name = None
        self._offset = None
        self._limit = None
        self.__from = None
        self._to = None
        self._order_by = None
        self._sort_by = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.metric_name = metric_name
        self.offset = offset
        self.limit = limit
        self._from = _from
        self.to = to
        if order_by is not None:
            self.order_by = order_by
        if sort_by is not None:
            self.sort_by = sort_by

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListMetricsDataRequest.

        集群ID。

        :return: The cluster_id of this ListMetricsDataRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListMetricsDataRequest.

        集群ID。

        :param cluster_id: The cluster_id of this ListMetricsDataRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def metric_name(self):
        """Gets the metric_name of this ListMetricsDataRequest.

        指标名称。

        :return: The metric_name of this ListMetricsDataRequest.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this ListMetricsDataRequest.

        指标名称。

        :param metric_name: The metric_name of this ListMetricsDataRequest.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def offset(self):
        """Gets the offset of this ListMetricsDataRequest.

        偏移量，表示从此偏移量开始查询，offset>=0。

        :return: The offset of this ListMetricsDataRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListMetricsDataRequest.

        偏移量，表示从此偏移量开始查询，offset>=0。

        :param offset: The offset of this ListMetricsDataRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListMetricsDataRequest.

        每页显示的条目数量，最大1000。

        :return: The limit of this ListMetricsDataRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListMetricsDataRequest.

        每页显示的条目数量，最大1000。

        :param limit: The limit of this ListMetricsDataRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def _from(self):
        """Gets the _from of this ListMetricsDataRequest.

        采集开始时间，13位时间戳。

        :return: The _from of this ListMetricsDataRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ListMetricsDataRequest.

        采集开始时间，13位时间戳。

        :param _from: The _from of this ListMetricsDataRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this ListMetricsDataRequest.

        采集结束时间，13位时间戳。开始时间到结束时间最多不超过一天。

        :return: The to of this ListMetricsDataRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ListMetricsDataRequest.

        采集结束时间，13位时间戳。开始时间到结束时间最多不超过一天。

        :param to: The to of this ListMetricsDataRequest.
        :type to: int
        """
        self._to = to

    @property
    def order_by(self):
        """Gets the order_by of this ListMetricsDataRequest.

        排序字段。固定取值。 ctime：采集时间。

        :return: The order_by of this ListMetricsDataRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ListMetricsDataRequest.

        排序字段。固定取值。 ctime：采集时间。

        :param order_by: The order_by of this ListMetricsDataRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def sort_by(self):
        """Gets the sort_by of this ListMetricsDataRequest.

        正序还是倒叙。固定取值。 asc：正序。 desc：倒序。

        :return: The sort_by of this ListMetricsDataRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this ListMetricsDataRequest.

        正序还是倒叙。固定取值。 asc：正序。 desc：倒序。

        :param sort_by: The sort_by of this ListMetricsDataRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

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
        if not isinstance(other, ListMetricsDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
