# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricInfoList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dimensions': 'list[MetricsDimension]',
        'metric_name': 'str',
        'namespace': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'dimensions': 'dimensions',
        'metric_name': 'metric_name',
        'namespace': 'namespace',
        'unit': 'unit'
    }

    def __init__(self, dimensions=None, metric_name=None, namespace=None, unit=None):
        """MetricInfoList

        The model defined in huaweicloud sdk

        :param dimensions: 指标维度
        :type dimensions: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        :param metric_name: 指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，长度最短为1，最大为64；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type metric_name: str
        :param namespace: 指标命名空间，例如弹性云服务器命名空间SYS.ECS；格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，总长度最短为3，最大为32。说明： 当alarm_type为（EVENT.SYS| EVENT.CUSTOM）时允许为空；各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type namespace: str
        :param unit: 指标单位。
        :type unit: str
        """
        
        

        self._dimensions = None
        self._metric_name = None
        self._namespace = None
        self._unit = None
        self.discriminator = None

        self.dimensions = dimensions
        self.metric_name = metric_name
        self.namespace = namespace
        self.unit = unit

    @property
    def dimensions(self):
        """Gets the dimensions of this MetricInfoList.

        指标维度

        :return: The dimensions of this MetricInfoList.
        :rtype: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this MetricInfoList.

        指标维度

        :param dimensions: The dimensions of this MetricInfoList.
        :type dimensions: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        """
        self._dimensions = dimensions

    @property
    def metric_name(self):
        """Gets the metric_name of this MetricInfoList.

        指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，长度最短为1，最大为64；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The metric_name of this MetricInfoList.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this MetricInfoList.

        指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，长度最短为1，最大为64；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param metric_name: The metric_name of this MetricInfoList.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def namespace(self):
        """Gets the namespace of this MetricInfoList.

        指标命名空间，例如弹性云服务器命名空间SYS.ECS；格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，总长度最短为3，最大为32。说明： 当alarm_type为（EVENT.SYS| EVENT.CUSTOM）时允许为空；各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The namespace of this MetricInfoList.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this MetricInfoList.

        指标命名空间，例如弹性云服务器命名空间SYS.ECS；格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，总长度最短为3，最大为32。说明： 当alarm_type为（EVENT.SYS| EVENT.CUSTOM）时允许为空；各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param namespace: The namespace of this MetricInfoList.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def unit(self):
        """Gets the unit of this MetricInfoList.

        指标单位。

        :return: The unit of this MetricInfoList.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this MetricInfoList.

        指标单位。

        :param unit: The unit of this MetricInfoList.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, MetricInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
