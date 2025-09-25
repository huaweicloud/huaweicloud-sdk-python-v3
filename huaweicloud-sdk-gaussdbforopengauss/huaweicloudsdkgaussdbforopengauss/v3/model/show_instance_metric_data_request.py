# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceMetricDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'metric': 'str',
        'node_id': 'str',
        'component_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'metric': 'metric',
        'node_id': 'node_id',
        'component_id': 'component_id'
    }

    def __init__(self, x_language=None, instance_id=None, start_time=None, end_time=None, metric=None, node_id=None, component_id=None):
        r"""ShowInstanceMetricDataRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us
        :type x_language: str
        :param instance_id: **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。
        :type instance_id: str
        :param start_time: **参数解释**: 开始时间，时间戳格式，例如：1756971683303。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type start_time: str
        :param end_time: **参数解释**: 结束时间，时间戳格式，例如：1756975283303。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type end_time: str
        :param metric: **参数解释**: 指标ID，可通过“查询指标分组的指标名称”接口获取，例如查询CPU使用率，传值 rds001_cpu_util。 **约束限制**: 不涉及。
        :type metric: str
        :param node_id: **参数解释**: 节点ID。 **约束限制**: 不涉及。
        :type node_id: str
        :param component_id: **参数解释**: 组件ID，例如dn_6001。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type component_id: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._start_time = None
        self._end_time = None
        self._metric = None
        self._node_id = None
        self._component_id = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        self.metric = metric
        self.node_id = node_id
        if component_id is not None:
            self.component_id = component_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowInstanceMetricDataRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :return: The x_language of this ShowInstanceMetricDataRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowInstanceMetricDataRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :param x_language: The x_language of this ShowInstanceMetricDataRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowInstanceMetricDataRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :return: The instance_id of this ShowInstanceMetricDataRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowInstanceMetricDataRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this ShowInstanceMetricDataRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowInstanceMetricDataRequest.

        **参数解释**: 开始时间，时间戳格式，例如：1756971683303。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The start_time of this ShowInstanceMetricDataRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowInstanceMetricDataRequest.

        **参数解释**: 开始时间，时间戳格式，例如：1756971683303。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param start_time: The start_time of this ShowInstanceMetricDataRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowInstanceMetricDataRequest.

        **参数解释**: 结束时间，时间戳格式，例如：1756975283303。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The end_time of this ShowInstanceMetricDataRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowInstanceMetricDataRequest.

        **参数解释**: 结束时间，时间戳格式，例如：1756975283303。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param end_time: The end_time of this ShowInstanceMetricDataRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def metric(self):
        r"""Gets the metric of this ShowInstanceMetricDataRequest.

        **参数解释**: 指标ID，可通过“查询指标分组的指标名称”接口获取，例如查询CPU使用率，传值 rds001_cpu_util。 **约束限制**: 不涉及。

        :return: The metric of this ShowInstanceMetricDataRequest.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this ShowInstanceMetricDataRequest.

        **参数解释**: 指标ID，可通过“查询指标分组的指标名称”接口获取，例如查询CPU使用率，传值 rds001_cpu_util。 **约束限制**: 不涉及。

        :param metric: The metric of this ShowInstanceMetricDataRequest.
        :type metric: str
        """
        self._metric = metric

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowInstanceMetricDataRequest.

        **参数解释**: 节点ID。 **约束限制**: 不涉及。

        :return: The node_id of this ShowInstanceMetricDataRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowInstanceMetricDataRequest.

        **参数解释**: 节点ID。 **约束限制**: 不涉及。

        :param node_id: The node_id of this ShowInstanceMetricDataRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def component_id(self):
        r"""Gets the component_id of this ShowInstanceMetricDataRequest.

        **参数解释**: 组件ID，例如dn_6001。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The component_id of this ShowInstanceMetricDataRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this ShowInstanceMetricDataRequest.

        **参数解释**: 组件ID，例如dn_6001。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param component_id: The component_id of this ShowInstanceMetricDataRequest.
        :type component_id: str
        """
        self._component_id = component_id

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
        if not isinstance(other, ShowInstanceMetricDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
