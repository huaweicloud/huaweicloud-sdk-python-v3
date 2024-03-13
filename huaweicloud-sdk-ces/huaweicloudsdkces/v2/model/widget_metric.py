# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WidgetMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'dimensions': 'DimensionInfo',
        'metric_name': 'str',
        'alias': 'list[str]',
        'extra_info': 'ExtraInfo'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dimensions': 'dimensions',
        'metric_name': 'metric_name',
        'alias': 'alias',
        'extra_info': 'extra_info'
    }

    def __init__(self, namespace=None, dimensions=None, metric_name=None, alias=None, extra_info=None):
        """WidgetMetric

        The model defined in huaweicloud sdk

        :param namespace: 服务维度
        :type namespace: str
        :param dimensions: 
        :type dimensions: :class:`huaweicloudsdkces.v2.DimensionInfo`
        :param metric_name: 指标名称
        :type metric_name: str
        :param alias: 监控视图的指标别名列表
        :type alias: list[str]
        :param extra_info: 
        :type extra_info: :class:`huaweicloudsdkces.v2.ExtraInfo`
        """
        
        

        self._namespace = None
        self._dimensions = None
        self._metric_name = None
        self._alias = None
        self._extra_info = None
        self.discriminator = None

        self.namespace = namespace
        self.dimensions = dimensions
        self.metric_name = metric_name
        if alias is not None:
            self.alias = alias
        if extra_info is not None:
            self.extra_info = extra_info

    @property
    def namespace(self):
        """Gets the namespace of this WidgetMetric.

        服务维度

        :return: The namespace of this WidgetMetric.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this WidgetMetric.

        服务维度

        :param namespace: The namespace of this WidgetMetric.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimensions(self):
        """Gets the dimensions of this WidgetMetric.

        :return: The dimensions of this WidgetMetric.
        :rtype: :class:`huaweicloudsdkces.v2.DimensionInfo`
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this WidgetMetric.

        :param dimensions: The dimensions of this WidgetMetric.
        :type dimensions: :class:`huaweicloudsdkces.v2.DimensionInfo`
        """
        self._dimensions = dimensions

    @property
    def metric_name(self):
        """Gets the metric_name of this WidgetMetric.

        指标名称

        :return: The metric_name of this WidgetMetric.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this WidgetMetric.

        指标名称

        :param metric_name: The metric_name of this WidgetMetric.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def alias(self):
        """Gets the alias of this WidgetMetric.

        监控视图的指标别名列表

        :return: The alias of this WidgetMetric.
        :rtype: list[str]
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this WidgetMetric.

        监控视图的指标别名列表

        :param alias: The alias of this WidgetMetric.
        :type alias: list[str]
        """
        self._alias = alias

    @property
    def extra_info(self):
        """Gets the extra_info of this WidgetMetric.

        :return: The extra_info of this WidgetMetric.
        :rtype: :class:`huaweicloudsdkces.v2.ExtraInfo`
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this WidgetMetric.

        :param extra_info: The extra_info of this WidgetMetric.
        :type extra_info: :class:`huaweicloudsdkces.v2.ExtraInfo`
        """
        self._extra_info = extra_info

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
        if not isinstance(other, WidgetMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
