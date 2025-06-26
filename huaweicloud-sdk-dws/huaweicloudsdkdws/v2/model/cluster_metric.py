# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scope': 'str',
        'fields': 'list[SimpleFieldDto]',
        'metric_name': 'str',
        'collect_rate': 'int',
        'collect_range': 'list[str]',
        'create_time': 'str'
    }

    attribute_map = {
        'scope': 'scope',
        'fields': 'fields',
        'metric_name': 'metric_name',
        'collect_rate': 'collect_rate',
        'collect_range': 'collect_range',
        'create_time': 'create_time'
    }

    def __init__(self, scope=None, fields=None, metric_name=None, collect_rate=None, collect_range=None, create_time=None):
        r"""ClusterMetric

        The model defined in huaweicloud sdk

        :param scope: **参数解释**： 指标名称。 **取值范围**： 不涉及。
        :type scope: str
        :param fields: **参数解释**： 指标表相关字段信息。 **取值范围**： 不涉及。
        :type fields: list[:class:`huaweicloudsdkdws.v2.SimpleFieldDto`]
        :param metric_name: **参数解释**： 作用域。 **取值范围**： 不涉及。
        :type metric_name: str
        :param collect_rate: **参数解释**： 采集速率。 **取值范围**： 不涉及。
        :type collect_rate: int
        :param collect_range: **参数解释**： 采集时间范围。 **取值范围**： 不涉及。
        :type collect_range: list[str]
        :param create_time: **参数解释**： 创建时间。 **取值范围**： 不涉及。
        :type create_time: str
        """
        
        

        self._scope = None
        self._fields = None
        self._metric_name = None
        self._collect_rate = None
        self._collect_range = None
        self._create_time = None
        self.discriminator = None

        if scope is not None:
            self.scope = scope
        if fields is not None:
            self.fields = fields
        if metric_name is not None:
            self.metric_name = metric_name
        if collect_rate is not None:
            self.collect_rate = collect_rate
        if collect_range is not None:
            self.collect_range = collect_range
        if create_time is not None:
            self.create_time = create_time

    @property
    def scope(self):
        r"""Gets the scope of this ClusterMetric.

        **参数解释**： 指标名称。 **取值范围**： 不涉及。

        :return: The scope of this ClusterMetric.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this ClusterMetric.

        **参数解释**： 指标名称。 **取值范围**： 不涉及。

        :param scope: The scope of this ClusterMetric.
        :type scope: str
        """
        self._scope = scope

    @property
    def fields(self):
        r"""Gets the fields of this ClusterMetric.

        **参数解释**： 指标表相关字段信息。 **取值范围**： 不涉及。

        :return: The fields of this ClusterMetric.
        :rtype: list[:class:`huaweicloudsdkdws.v2.SimpleFieldDto`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ClusterMetric.

        **参数解释**： 指标表相关字段信息。 **取值范围**： 不涉及。

        :param fields: The fields of this ClusterMetric.
        :type fields: list[:class:`huaweicloudsdkdws.v2.SimpleFieldDto`]
        """
        self._fields = fields

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ClusterMetric.

        **参数解释**： 作用域。 **取值范围**： 不涉及。

        :return: The metric_name of this ClusterMetric.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ClusterMetric.

        **参数解释**： 作用域。 **取值范围**： 不涉及。

        :param metric_name: The metric_name of this ClusterMetric.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def collect_rate(self):
        r"""Gets the collect_rate of this ClusterMetric.

        **参数解释**： 采集速率。 **取值范围**： 不涉及。

        :return: The collect_rate of this ClusterMetric.
        :rtype: int
        """
        return self._collect_rate

    @collect_rate.setter
    def collect_rate(self, collect_rate):
        r"""Sets the collect_rate of this ClusterMetric.

        **参数解释**： 采集速率。 **取值范围**： 不涉及。

        :param collect_rate: The collect_rate of this ClusterMetric.
        :type collect_rate: int
        """
        self._collect_rate = collect_rate

    @property
    def collect_range(self):
        r"""Gets the collect_range of this ClusterMetric.

        **参数解释**： 采集时间范围。 **取值范围**： 不涉及。

        :return: The collect_range of this ClusterMetric.
        :rtype: list[str]
        """
        return self._collect_range

    @collect_range.setter
    def collect_range(self, collect_range):
        r"""Sets the collect_range of this ClusterMetric.

        **参数解释**： 采集时间范围。 **取值范围**： 不涉及。

        :param collect_range: The collect_range of this ClusterMetric.
        :type collect_range: list[str]
        """
        self._collect_range = collect_range

    @property
    def create_time(self):
        r"""Gets the create_time of this ClusterMetric.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :return: The create_time of this ClusterMetric.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ClusterMetric.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :param create_time: The create_time of this ClusterMetric.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, ClusterMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
