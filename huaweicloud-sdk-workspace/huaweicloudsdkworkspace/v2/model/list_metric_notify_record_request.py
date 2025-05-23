# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMetricNotifyRecordRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_name': 'str',
        'rule_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'rule_id': 'rule_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, metric_name=None, rule_id=None, offset=None, limit=None):
        r"""ListMetricNotifyRecordRequest

        The model defined in huaweicloud sdk

        :param metric_name: 指标名称(精确匹配) (metric_name和rule_id不允许同时为空)
        :type metric_name: str
        :param rule_id: 通知规则ID (metric_name和rule_id不允许同时为空)
        :type rule_id: str
        :param offset: 查询的偏移量,默认值0
        :type offset: int
        :param limit: 单次查询的大小[1-100],默认值10
        :type limit: int
        """
        
        

        self._metric_name = None
        self._rule_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if rule_id is not None:
            self.rule_id = rule_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ListMetricNotifyRecordRequest.

        指标名称(精确匹配) (metric_name和rule_id不允许同时为空)

        :return: The metric_name of this ListMetricNotifyRecordRequest.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ListMetricNotifyRecordRequest.

        指标名称(精确匹配) (metric_name和rule_id不允许同时为空)

        :param metric_name: The metric_name of this ListMetricNotifyRecordRequest.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def rule_id(self):
        r"""Gets the rule_id of this ListMetricNotifyRecordRequest.

        通知规则ID (metric_name和rule_id不允许同时为空)

        :return: The rule_id of this ListMetricNotifyRecordRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this ListMetricNotifyRecordRequest.

        通知规则ID (metric_name和rule_id不允许同时为空)

        :param rule_id: The rule_id of this ListMetricNotifyRecordRequest.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def offset(self):
        r"""Gets the offset of this ListMetricNotifyRecordRequest.

        查询的偏移量,默认值0

        :return: The offset of this ListMetricNotifyRecordRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListMetricNotifyRecordRequest.

        查询的偏移量,默认值0

        :param offset: The offset of this ListMetricNotifyRecordRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListMetricNotifyRecordRequest.

        单次查询的大小[1-100],默认值10

        :return: The limit of this ListMetricNotifyRecordRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListMetricNotifyRecordRequest.

        单次查询的大小[1-100],默认值10

        :param limit: The limit of this ListMetricNotifyRecordRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListMetricNotifyRecordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
