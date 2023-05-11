# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SumTableView:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'view_type': 'str',
        'collector_name': 'str',
        'metric_set': 'str',
        'title': 'str',
        'table_direction': 'str',
        'group_by': 'str',
        'filter': 'str',
        'field_item_list': 'list[FieldItem]',
        'span': 'bool',
        'span_field': 'str',
        'order_by': 'str',
        'latest': 'bool'
    }

    attribute_map = {
        'view_type': 'view_type',
        'collector_name': 'collector_name',
        'metric_set': 'metric_set',
        'title': 'title',
        'table_direction': 'table_direction',
        'group_by': 'group_by',
        'filter': 'filter',
        'field_item_list': 'field_item_list',
        'span': 'span',
        'span_field': 'span_field',
        'order_by': 'order_by',
        'latest': 'latest'
    }

    def __init__(self, view_type=None, collector_name=None, metric_set=None, title=None, table_direction=None, group_by=None, filter=None, field_item_list=None, span=None, span_field=None, order_by=None, latest=None):
        """SumTableView

        The model defined in huaweicloud sdk

        :param view_type: 视图类型。
        :type view_type: str
        :param collector_name: 采集器名称。
        :type collector_name: str
        :param metric_set: 视图对应的指标集的名称。
        :type metric_set: str
        :param title: 图标所需展示的标题。
        :type title: str
        :param table_direction: 表格的方向，H：默认，表头横向，V：表头纵向。
        :type table_direction: str
        :param group_by: 分组规则。
        :type group_by: str
        :param filter: 过滤列表模型。
        :type filter: str
        :param field_item_list: 所需展示的字段列表模型列表。
        :type field_item_list: list[:class:`huaweicloudsdkapm.v1.FieldItem`]
        :param span: 跨度。
        :type span: bool
        :param span_field: 跨度字段。
        :type span_field: str
        :param order_by: 排序规则。
        :type order_by: str
        :param latest: 是否只展示最近一笔数据。
        :type latest: bool
        """
        
        

        self._view_type = None
        self._collector_name = None
        self._metric_set = None
        self._title = None
        self._table_direction = None
        self._group_by = None
        self._filter = None
        self._field_item_list = None
        self._span = None
        self._span_field = None
        self._order_by = None
        self._latest = None
        self.discriminator = None

        self.view_type = view_type
        self.collector_name = collector_name
        self.metric_set = metric_set
        if title is not None:
            self.title = title
        if table_direction is not None:
            self.table_direction = table_direction
        if group_by is not None:
            self.group_by = group_by
        if filter is not None:
            self.filter = filter
        self.field_item_list = field_item_list
        if span is not None:
            self.span = span
        if span_field is not None:
            self.span_field = span_field
        if order_by is not None:
            self.order_by = order_by
        if latest is not None:
            self.latest = latest

    @property
    def view_type(self):
        """Gets the view_type of this SumTableView.

        视图类型。

        :return: The view_type of this SumTableView.
        :rtype: str
        """
        return self._view_type

    @view_type.setter
    def view_type(self, view_type):
        """Sets the view_type of this SumTableView.

        视图类型。

        :param view_type: The view_type of this SumTableView.
        :type view_type: str
        """
        self._view_type = view_type

    @property
    def collector_name(self):
        """Gets the collector_name of this SumTableView.

        采集器名称。

        :return: The collector_name of this SumTableView.
        :rtype: str
        """
        return self._collector_name

    @collector_name.setter
    def collector_name(self, collector_name):
        """Sets the collector_name of this SumTableView.

        采集器名称。

        :param collector_name: The collector_name of this SumTableView.
        :type collector_name: str
        """
        self._collector_name = collector_name

    @property
    def metric_set(self):
        """Gets the metric_set of this SumTableView.

        视图对应的指标集的名称。

        :return: The metric_set of this SumTableView.
        :rtype: str
        """
        return self._metric_set

    @metric_set.setter
    def metric_set(self, metric_set):
        """Sets the metric_set of this SumTableView.

        视图对应的指标集的名称。

        :param metric_set: The metric_set of this SumTableView.
        :type metric_set: str
        """
        self._metric_set = metric_set

    @property
    def title(self):
        """Gets the title of this SumTableView.

        图标所需展示的标题。

        :return: The title of this SumTableView.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SumTableView.

        图标所需展示的标题。

        :param title: The title of this SumTableView.
        :type title: str
        """
        self._title = title

    @property
    def table_direction(self):
        """Gets the table_direction of this SumTableView.

        表格的方向，H：默认，表头横向，V：表头纵向。

        :return: The table_direction of this SumTableView.
        :rtype: str
        """
        return self._table_direction

    @table_direction.setter
    def table_direction(self, table_direction):
        """Sets the table_direction of this SumTableView.

        表格的方向，H：默认，表头横向，V：表头纵向。

        :param table_direction: The table_direction of this SumTableView.
        :type table_direction: str
        """
        self._table_direction = table_direction

    @property
    def group_by(self):
        """Gets the group_by of this SumTableView.

        分组规则。

        :return: The group_by of this SumTableView.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this SumTableView.

        分组规则。

        :param group_by: The group_by of this SumTableView.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def filter(self):
        """Gets the filter of this SumTableView.

        过滤列表模型。

        :return: The filter of this SumTableView.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this SumTableView.

        过滤列表模型。

        :param filter: The filter of this SumTableView.
        :type filter: str
        """
        self._filter = filter

    @property
    def field_item_list(self):
        """Gets the field_item_list of this SumTableView.

        所需展示的字段列表模型列表。

        :return: The field_item_list of this SumTableView.
        :rtype: list[:class:`huaweicloudsdkapm.v1.FieldItem`]
        """
        return self._field_item_list

    @field_item_list.setter
    def field_item_list(self, field_item_list):
        """Sets the field_item_list of this SumTableView.

        所需展示的字段列表模型列表。

        :param field_item_list: The field_item_list of this SumTableView.
        :type field_item_list: list[:class:`huaweicloudsdkapm.v1.FieldItem`]
        """
        self._field_item_list = field_item_list

    @property
    def span(self):
        """Gets the span of this SumTableView.

        跨度。

        :return: The span of this SumTableView.
        :rtype: bool
        """
        return self._span

    @span.setter
    def span(self, span):
        """Sets the span of this SumTableView.

        跨度。

        :param span: The span of this SumTableView.
        :type span: bool
        """
        self._span = span

    @property
    def span_field(self):
        """Gets the span_field of this SumTableView.

        跨度字段。

        :return: The span_field of this SumTableView.
        :rtype: str
        """
        return self._span_field

    @span_field.setter
    def span_field(self, span_field):
        """Sets the span_field of this SumTableView.

        跨度字段。

        :param span_field: The span_field of this SumTableView.
        :type span_field: str
        """
        self._span_field = span_field

    @property
    def order_by(self):
        """Gets the order_by of this SumTableView.

        排序规则。

        :return: The order_by of this SumTableView.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this SumTableView.

        排序规则。

        :param order_by: The order_by of this SumTableView.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def latest(self):
        """Gets the latest of this SumTableView.

        是否只展示最近一笔数据。

        :return: The latest of this SumTableView.
        :rtype: bool
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        """Sets the latest of this SumTableView.

        是否只展示最近一笔数据。

        :param latest: The latest of this SumTableView.
        :type latest: bool
        """
        self._latest = latest

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
        if not isinstance(other, SumTableView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
