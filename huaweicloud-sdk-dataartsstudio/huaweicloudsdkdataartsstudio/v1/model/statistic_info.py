# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'atomic_index': 'StatisticSchema',
        'derivative_index': 'StatisticSchema',
        'compound_metric': 'StatisticSchema',
        'biz_index': 'StatisticSchema',
        'dimension': 'StatisticSchema',
        'condition_group': 'StatisticSchema',
        'time_condition': 'StatisticSchema',
        'common_condition': 'StatisticSchema',
        'dimension_logic_table': 'StatisticSchema',
        'fact_logic_table': 'StatisticSchema',
        'aggregation_logic_table': 'StatisticSchema',
        'data_standard': 'StatisticSchema',
        'table_model': 'StatisticSchema',
        'lookup_table': 'StatisticSchema',
        'pending_review': 'int',
        'my_applications': 'int'
    }

    attribute_map = {
        'atomic_index': 'atomic_index',
        'derivative_index': 'derivative_index',
        'compound_metric': 'compound_metric',
        'biz_index': 'biz_index',
        'dimension': 'dimension',
        'condition_group': 'condition_group',
        'time_condition': 'time_condition',
        'common_condition': 'common_condition',
        'dimension_logic_table': 'dimension_logic_table',
        'fact_logic_table': 'fact_logic_table',
        'aggregation_logic_table': 'aggregation_logic_table',
        'data_standard': 'data_standard',
        'table_model': 'table_model',
        'lookup_table': 'lookup_table',
        'pending_review': 'pending_review',
        'my_applications': 'my_applications'
    }

    def __init__(self, atomic_index=None, derivative_index=None, compound_metric=None, biz_index=None, dimension=None, condition_group=None, time_condition=None, common_condition=None, dimension_logic_table=None, fact_logic_table=None, aggregation_logic_table=None, data_standard=None, table_model=None, lookup_table=None, pending_review=None, my_applications=None):
        """StatisticInfo

        The model defined in huaweicloud sdk

        :param atomic_index: 
        :type atomic_index: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        :param derivative_index: 
        :type derivative_index: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        :param compound_metric: 
        :type compound_metric: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        :param biz_index: 
        :type biz_index: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        :param dimension: 
        :type dimension: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        :param condition_group: 
        :type condition_group: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        :param time_condition: 
        :type time_condition: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        :param common_condition: 
        :type common_condition: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        :param dimension_logic_table: 
        :type dimension_logic_table: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        :param fact_logic_table: 
        :type fact_logic_table: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        :param aggregation_logic_table: 
        :type aggregation_logic_table: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        :param data_standard: 
        :type data_standard: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        :param table_model: 
        :type table_model: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        :param lookup_table: 
        :type lookup_table: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        :param pending_review: 待我审核。
        :type pending_review: int
        :param my_applications: 我的申请。
        :type my_applications: int
        """
        
        

        self._atomic_index = None
        self._derivative_index = None
        self._compound_metric = None
        self._biz_index = None
        self._dimension = None
        self._condition_group = None
        self._time_condition = None
        self._common_condition = None
        self._dimension_logic_table = None
        self._fact_logic_table = None
        self._aggregation_logic_table = None
        self._data_standard = None
        self._table_model = None
        self._lookup_table = None
        self._pending_review = None
        self._my_applications = None
        self.discriminator = None

        if atomic_index is not None:
            self.atomic_index = atomic_index
        if derivative_index is not None:
            self.derivative_index = derivative_index
        if compound_metric is not None:
            self.compound_metric = compound_metric
        if biz_index is not None:
            self.biz_index = biz_index
        if dimension is not None:
            self.dimension = dimension
        if condition_group is not None:
            self.condition_group = condition_group
        if time_condition is not None:
            self.time_condition = time_condition
        if common_condition is not None:
            self.common_condition = common_condition
        if dimension_logic_table is not None:
            self.dimension_logic_table = dimension_logic_table
        if fact_logic_table is not None:
            self.fact_logic_table = fact_logic_table
        if aggregation_logic_table is not None:
            self.aggregation_logic_table = aggregation_logic_table
        if data_standard is not None:
            self.data_standard = data_standard
        if table_model is not None:
            self.table_model = table_model
        if lookup_table is not None:
            self.lookup_table = lookup_table
        if pending_review is not None:
            self.pending_review = pending_review
        if my_applications is not None:
            self.my_applications = my_applications

    @property
    def atomic_index(self):
        """Gets the atomic_index of this StatisticInfo.

        :return: The atomic_index of this StatisticInfo.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        return self._atomic_index

    @atomic_index.setter
    def atomic_index(self, atomic_index):
        """Sets the atomic_index of this StatisticInfo.

        :param atomic_index: The atomic_index of this StatisticInfo.
        :type atomic_index: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        self._atomic_index = atomic_index

    @property
    def derivative_index(self):
        """Gets the derivative_index of this StatisticInfo.

        :return: The derivative_index of this StatisticInfo.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        return self._derivative_index

    @derivative_index.setter
    def derivative_index(self, derivative_index):
        """Sets the derivative_index of this StatisticInfo.

        :param derivative_index: The derivative_index of this StatisticInfo.
        :type derivative_index: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        self._derivative_index = derivative_index

    @property
    def compound_metric(self):
        """Gets the compound_metric of this StatisticInfo.

        :return: The compound_metric of this StatisticInfo.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        return self._compound_metric

    @compound_metric.setter
    def compound_metric(self, compound_metric):
        """Sets the compound_metric of this StatisticInfo.

        :param compound_metric: The compound_metric of this StatisticInfo.
        :type compound_metric: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        self._compound_metric = compound_metric

    @property
    def biz_index(self):
        """Gets the biz_index of this StatisticInfo.

        :return: The biz_index of this StatisticInfo.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        return self._biz_index

    @biz_index.setter
    def biz_index(self, biz_index):
        """Sets the biz_index of this StatisticInfo.

        :param biz_index: The biz_index of this StatisticInfo.
        :type biz_index: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        self._biz_index = biz_index

    @property
    def dimension(self):
        """Gets the dimension of this StatisticInfo.

        :return: The dimension of this StatisticInfo.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this StatisticInfo.

        :param dimension: The dimension of this StatisticInfo.
        :type dimension: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        self._dimension = dimension

    @property
    def condition_group(self):
        """Gets the condition_group of this StatisticInfo.

        :return: The condition_group of this StatisticInfo.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        return self._condition_group

    @condition_group.setter
    def condition_group(self, condition_group):
        """Sets the condition_group of this StatisticInfo.

        :param condition_group: The condition_group of this StatisticInfo.
        :type condition_group: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        self._condition_group = condition_group

    @property
    def time_condition(self):
        """Gets the time_condition of this StatisticInfo.

        :return: The time_condition of this StatisticInfo.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        return self._time_condition

    @time_condition.setter
    def time_condition(self, time_condition):
        """Sets the time_condition of this StatisticInfo.

        :param time_condition: The time_condition of this StatisticInfo.
        :type time_condition: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        self._time_condition = time_condition

    @property
    def common_condition(self):
        """Gets the common_condition of this StatisticInfo.

        :return: The common_condition of this StatisticInfo.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        return self._common_condition

    @common_condition.setter
    def common_condition(self, common_condition):
        """Sets the common_condition of this StatisticInfo.

        :param common_condition: The common_condition of this StatisticInfo.
        :type common_condition: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        self._common_condition = common_condition

    @property
    def dimension_logic_table(self):
        """Gets the dimension_logic_table of this StatisticInfo.

        :return: The dimension_logic_table of this StatisticInfo.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        return self._dimension_logic_table

    @dimension_logic_table.setter
    def dimension_logic_table(self, dimension_logic_table):
        """Sets the dimension_logic_table of this StatisticInfo.

        :param dimension_logic_table: The dimension_logic_table of this StatisticInfo.
        :type dimension_logic_table: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        self._dimension_logic_table = dimension_logic_table

    @property
    def fact_logic_table(self):
        """Gets the fact_logic_table of this StatisticInfo.

        :return: The fact_logic_table of this StatisticInfo.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        return self._fact_logic_table

    @fact_logic_table.setter
    def fact_logic_table(self, fact_logic_table):
        """Sets the fact_logic_table of this StatisticInfo.

        :param fact_logic_table: The fact_logic_table of this StatisticInfo.
        :type fact_logic_table: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        self._fact_logic_table = fact_logic_table

    @property
    def aggregation_logic_table(self):
        """Gets the aggregation_logic_table of this StatisticInfo.

        :return: The aggregation_logic_table of this StatisticInfo.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        return self._aggregation_logic_table

    @aggregation_logic_table.setter
    def aggregation_logic_table(self, aggregation_logic_table):
        """Sets the aggregation_logic_table of this StatisticInfo.

        :param aggregation_logic_table: The aggregation_logic_table of this StatisticInfo.
        :type aggregation_logic_table: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        self._aggregation_logic_table = aggregation_logic_table

    @property
    def data_standard(self):
        """Gets the data_standard of this StatisticInfo.

        :return: The data_standard of this StatisticInfo.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        return self._data_standard

    @data_standard.setter
    def data_standard(self, data_standard):
        """Sets the data_standard of this StatisticInfo.

        :param data_standard: The data_standard of this StatisticInfo.
        :type data_standard: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        self._data_standard = data_standard

    @property
    def table_model(self):
        """Gets the table_model of this StatisticInfo.

        :return: The table_model of this StatisticInfo.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        return self._table_model

    @table_model.setter
    def table_model(self, table_model):
        """Sets the table_model of this StatisticInfo.

        :param table_model: The table_model of this StatisticInfo.
        :type table_model: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        self._table_model = table_model

    @property
    def lookup_table(self):
        """Gets the lookup_table of this StatisticInfo.

        :return: The lookup_table of this StatisticInfo.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        return self._lookup_table

    @lookup_table.setter
    def lookup_table(self, lookup_table):
        """Sets the lookup_table of this StatisticInfo.

        :param lookup_table: The lookup_table of this StatisticInfo.
        :type lookup_table: :class:`huaweicloudsdkdataartsstudio.v1.StatisticSchema`
        """
        self._lookup_table = lookup_table

    @property
    def pending_review(self):
        """Gets the pending_review of this StatisticInfo.

        待我审核。

        :return: The pending_review of this StatisticInfo.
        :rtype: int
        """
        return self._pending_review

    @pending_review.setter
    def pending_review(self, pending_review):
        """Sets the pending_review of this StatisticInfo.

        待我审核。

        :param pending_review: The pending_review of this StatisticInfo.
        :type pending_review: int
        """
        self._pending_review = pending_review

    @property
    def my_applications(self):
        """Gets the my_applications of this StatisticInfo.

        我的申请。

        :return: The my_applications of this StatisticInfo.
        :rtype: int
        """
        return self._my_applications

    @my_applications.setter
    def my_applications(self, my_applications):
        """Sets the my_applications of this StatisticInfo.

        我的申请。

        :param my_applications: The my_applications of this StatisticInfo.
        :type my_applications: int
        """
        self._my_applications = my_applications

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
        if not isinstance(other, StatisticInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
