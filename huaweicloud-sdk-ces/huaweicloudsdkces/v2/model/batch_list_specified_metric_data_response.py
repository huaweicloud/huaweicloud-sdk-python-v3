# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchListSpecifiedMetricDataResponse(SdkResponse):

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
        'metric_name': 'str',
        'metric_dimension': 'str',
        'data_points': 'list[MetricDataPoint]'
    }

    attribute_map = {
        'namespace': 'namespace',
        'metric_name': 'metric_name',
        'metric_dimension': 'metric_dimension',
        'data_points': 'data_points'
    }

    def __init__(self, namespace=None, metric_name=None, metric_dimension=None, data_points=None):
        r"""BatchListSpecifiedMetricDataResponse

        The model defined in huaweicloud sdk

        :param namespace: **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 
        :type namespace: str
        :param metric_name: **参数解释**： 资源的监控指标名称，各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_/-。字符长度最短为1，最大为96。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率。 
        :type metric_name: str
        :param metric_dimension: **参数解释**: 指标维度, 多维度逗号分隔。。 **取值范围**: 必须以字母开头，只能包含0-9/a-z/A-Z/_/-/,。每个维度必须以字母开头，每个维度长度最短1，最长32，多个维度直接用,分割。 
        :type metric_dimension: str
        :param data_points: ***参数解释*** 监控数据列表 
        :type data_points: list[:class:`huaweicloudsdkces.v2.MetricDataPoint`]
        """
        
        super(BatchListSpecifiedMetricDataResponse, self).__init__()

        self._namespace = None
        self._metric_name = None
        self._metric_dimension = None
        self._data_points = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if metric_name is not None:
            self.metric_name = metric_name
        if metric_dimension is not None:
            self.metric_dimension = metric_dimension
        if data_points is not None:
            self.data_points = data_points

    @property
    def namespace(self):
        r"""Gets the namespace of this BatchListSpecifiedMetricDataResponse.

        **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 

        :return: The namespace of this BatchListSpecifiedMetricDataResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this BatchListSpecifiedMetricDataResponse.

        **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 

        :param namespace: The namespace of this BatchListSpecifiedMetricDataResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def metric_name(self):
        r"""Gets the metric_name of this BatchListSpecifiedMetricDataResponse.

        **参数解释**： 资源的监控指标名称，各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_/-。字符长度最短为1，最大为96。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率。 

        :return: The metric_name of this BatchListSpecifiedMetricDataResponse.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this BatchListSpecifiedMetricDataResponse.

        **参数解释**： 资源的监控指标名称，各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_/-。字符长度最短为1，最大为96。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率。 

        :param metric_name: The metric_name of this BatchListSpecifiedMetricDataResponse.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def metric_dimension(self):
        r"""Gets the metric_dimension of this BatchListSpecifiedMetricDataResponse.

        **参数解释**: 指标维度, 多维度逗号分隔。。 **取值范围**: 必须以字母开头，只能包含0-9/a-z/A-Z/_/-/,。每个维度必须以字母开头，每个维度长度最短1，最长32，多个维度直接用,分割。 

        :return: The metric_dimension of this BatchListSpecifiedMetricDataResponse.
        :rtype: str
        """
        return self._metric_dimension

    @metric_dimension.setter
    def metric_dimension(self, metric_dimension):
        r"""Sets the metric_dimension of this BatchListSpecifiedMetricDataResponse.

        **参数解释**: 指标维度, 多维度逗号分隔。。 **取值范围**: 必须以字母开头，只能包含0-9/a-z/A-Z/_/-/,。每个维度必须以字母开头，每个维度长度最短1，最长32，多个维度直接用,分割。 

        :param metric_dimension: The metric_dimension of this BatchListSpecifiedMetricDataResponse.
        :type metric_dimension: str
        """
        self._metric_dimension = metric_dimension

    @property
    def data_points(self):
        r"""Gets the data_points of this BatchListSpecifiedMetricDataResponse.

        ***参数解释*** 监控数据列表 

        :return: The data_points of this BatchListSpecifiedMetricDataResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.MetricDataPoint`]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        r"""Sets the data_points of this BatchListSpecifiedMetricDataResponse.

        ***参数解释*** 监控数据列表 

        :param data_points: The data_points of this BatchListSpecifiedMetricDataResponse.
        :type data_points: list[:class:`huaweicloudsdkces.v2.MetricDataPoint`]
        """
        self._data_points = data_points

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
        if not isinstance(other, BatchListSpecifiedMetricDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
