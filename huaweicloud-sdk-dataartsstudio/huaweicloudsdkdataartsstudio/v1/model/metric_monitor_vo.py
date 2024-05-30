# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricMonitorVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'other_metric_ids': 'list[str]',
        'other_metric_names': 'list[str]',
        'other_compound_metric_ids': 'list[str]',
        'other_compound_metric_names': 'list[str]',
        'expression': 'str',
        'metric_id': 'str',
        'front_configs': 'str',
        'metric_type': 'BizTypeEnum'
    }

    attribute_map = {
        'id': 'id',
        'other_metric_ids': 'other_metric_ids',
        'other_metric_names': 'other_metric_names',
        'other_compound_metric_ids': 'other_compound_metric_ids',
        'other_compound_metric_names': 'other_compound_metric_names',
        'expression': 'expression',
        'metric_id': 'metric_id',
        'front_configs': 'front_configs',
        'metric_type': 'metric_type'
    }

    def __init__(self, id=None, other_metric_ids=None, other_metric_names=None, other_compound_metric_ids=None, other_compound_metric_names=None, expression=None, metric_id=None, front_configs=None, metric_type=None):
        """MetricMonitorVO

        The model defined in huaweicloud sdk

        :param id: 编码，填写String类型替代Long类型。
        :type id: str
        :param other_metric_ids: 其他指标ID，填写String类型替代Long类型。
        :type other_metric_ids: list[str]
        :param other_metric_names: 其他指标名称，只读。
        :type other_metric_names: list[str]
        :param other_compound_metric_ids: 其他复合指标ID。
        :type other_compound_metric_ids: list[str]
        :param other_compound_metric_names: 其他复合指标名称。
        :type other_compound_metric_names: list[str]
        :param expression: 告警表达式。
        :type expression: str
        :param metric_id: 挂载指ID，填写String类型替代Long类型。
        :type metric_id: str
        :param front_configs: 前端表达式配置，用于前端数据恢复。
        :type front_configs: str
        :param metric_type: 
        :type metric_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        
        

        self._id = None
        self._other_metric_ids = None
        self._other_metric_names = None
        self._other_compound_metric_ids = None
        self._other_compound_metric_names = None
        self._expression = None
        self._metric_id = None
        self._front_configs = None
        self._metric_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if other_metric_ids is not None:
            self.other_metric_ids = other_metric_ids
        if other_metric_names is not None:
            self.other_metric_names = other_metric_names
        if other_compound_metric_ids is not None:
            self.other_compound_metric_ids = other_compound_metric_ids
        if other_compound_metric_names is not None:
            self.other_compound_metric_names = other_compound_metric_names
        if expression is not None:
            self.expression = expression
        if metric_id is not None:
            self.metric_id = metric_id
        if front_configs is not None:
            self.front_configs = front_configs
        if metric_type is not None:
            self.metric_type = metric_type

    @property
    def id(self):
        """Gets the id of this MetricMonitorVO.

        编码，填写String类型替代Long类型。

        :return: The id of this MetricMonitorVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MetricMonitorVO.

        编码，填写String类型替代Long类型。

        :param id: The id of this MetricMonitorVO.
        :type id: str
        """
        self._id = id

    @property
    def other_metric_ids(self):
        """Gets the other_metric_ids of this MetricMonitorVO.

        其他指标ID，填写String类型替代Long类型。

        :return: The other_metric_ids of this MetricMonitorVO.
        :rtype: list[str]
        """
        return self._other_metric_ids

    @other_metric_ids.setter
    def other_metric_ids(self, other_metric_ids):
        """Sets the other_metric_ids of this MetricMonitorVO.

        其他指标ID，填写String类型替代Long类型。

        :param other_metric_ids: The other_metric_ids of this MetricMonitorVO.
        :type other_metric_ids: list[str]
        """
        self._other_metric_ids = other_metric_ids

    @property
    def other_metric_names(self):
        """Gets the other_metric_names of this MetricMonitorVO.

        其他指标名称，只读。

        :return: The other_metric_names of this MetricMonitorVO.
        :rtype: list[str]
        """
        return self._other_metric_names

    @other_metric_names.setter
    def other_metric_names(self, other_metric_names):
        """Sets the other_metric_names of this MetricMonitorVO.

        其他指标名称，只读。

        :param other_metric_names: The other_metric_names of this MetricMonitorVO.
        :type other_metric_names: list[str]
        """
        self._other_metric_names = other_metric_names

    @property
    def other_compound_metric_ids(self):
        """Gets the other_compound_metric_ids of this MetricMonitorVO.

        其他复合指标ID。

        :return: The other_compound_metric_ids of this MetricMonitorVO.
        :rtype: list[str]
        """
        return self._other_compound_metric_ids

    @other_compound_metric_ids.setter
    def other_compound_metric_ids(self, other_compound_metric_ids):
        """Sets the other_compound_metric_ids of this MetricMonitorVO.

        其他复合指标ID。

        :param other_compound_metric_ids: The other_compound_metric_ids of this MetricMonitorVO.
        :type other_compound_metric_ids: list[str]
        """
        self._other_compound_metric_ids = other_compound_metric_ids

    @property
    def other_compound_metric_names(self):
        """Gets the other_compound_metric_names of this MetricMonitorVO.

        其他复合指标名称。

        :return: The other_compound_metric_names of this MetricMonitorVO.
        :rtype: list[str]
        """
        return self._other_compound_metric_names

    @other_compound_metric_names.setter
    def other_compound_metric_names(self, other_compound_metric_names):
        """Sets the other_compound_metric_names of this MetricMonitorVO.

        其他复合指标名称。

        :param other_compound_metric_names: The other_compound_metric_names of this MetricMonitorVO.
        :type other_compound_metric_names: list[str]
        """
        self._other_compound_metric_names = other_compound_metric_names

    @property
    def expression(self):
        """Gets the expression of this MetricMonitorVO.

        告警表达式。

        :return: The expression of this MetricMonitorVO.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this MetricMonitorVO.

        告警表达式。

        :param expression: The expression of this MetricMonitorVO.
        :type expression: str
        """
        self._expression = expression

    @property
    def metric_id(self):
        """Gets the metric_id of this MetricMonitorVO.

        挂载指ID，填写String类型替代Long类型。

        :return: The metric_id of this MetricMonitorVO.
        :rtype: str
        """
        return self._metric_id

    @metric_id.setter
    def metric_id(self, metric_id):
        """Sets the metric_id of this MetricMonitorVO.

        挂载指ID，填写String类型替代Long类型。

        :param metric_id: The metric_id of this MetricMonitorVO.
        :type metric_id: str
        """
        self._metric_id = metric_id

    @property
    def front_configs(self):
        """Gets the front_configs of this MetricMonitorVO.

        前端表达式配置，用于前端数据恢复。

        :return: The front_configs of this MetricMonitorVO.
        :rtype: str
        """
        return self._front_configs

    @front_configs.setter
    def front_configs(self, front_configs):
        """Sets the front_configs of this MetricMonitorVO.

        前端表达式配置，用于前端数据恢复。

        :param front_configs: The front_configs of this MetricMonitorVO.
        :type front_configs: str
        """
        self._front_configs = front_configs

    @property
    def metric_type(self):
        """Gets the metric_type of this MetricMonitorVO.

        :return: The metric_type of this MetricMonitorVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        """Sets the metric_type of this MetricMonitorVO.

        :param metric_type: The metric_type of this MetricMonitorVO.
        :type metric_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        self._metric_type = metric_type

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
        if not isinstance(other, MetricMonitorVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
