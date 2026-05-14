# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricInfo:

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
        'dimensions': 'list[MetricsDimension]'
    }

    attribute_map = {
        'namespace': 'namespace',
        'metric_name': 'metric_name',
        'dimensions': 'dimensions'
    }

    def __init__(self, namespace=None, metric_name=None, dimensions=None):
        r"""MetricInfo

        The model defined in huaweicloud sdk

        :param namespace: 自定义指标命名空间.格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，service.item总长度最短为3，最大为32，service不能为“SYS”。namespace不能为AGT.ECS、SERVICE.BMS
        :type namespace: str
        :param metric_name: 自定义指标名称
        :type metric_name: str
        :param dimensions: 指标维度列表
        :type dimensions: list[:class:`huaweicloudsdkiec.v1.MetricsDimension`]
        """
        
        

        self._namespace = None
        self._metric_name = None
        self._dimensions = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if metric_name is not None:
            self.metric_name = metric_name
        if dimensions is not None:
            self.dimensions = dimensions

    @property
    def namespace(self):
        r"""Gets the namespace of this MetricInfo.

        自定义指标命名空间.格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，service.item总长度最短为3，最大为32，service不能为“SYS”。namespace不能为AGT.ECS、SERVICE.BMS

        :return: The namespace of this MetricInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this MetricInfo.

        自定义指标命名空间.格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，service.item总长度最短为3，最大为32，service不能为“SYS”。namespace不能为AGT.ECS、SERVICE.BMS

        :param namespace: The namespace of this MetricInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def metric_name(self):
        r"""Gets the metric_name of this MetricInfo.

        自定义指标名称

        :return: The metric_name of this MetricInfo.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this MetricInfo.

        自定义指标名称

        :param metric_name: The metric_name of this MetricInfo.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def dimensions(self):
        r"""Gets the dimensions of this MetricInfo.

        指标维度列表

        :return: The dimensions of this MetricInfo.
        :rtype: list[:class:`huaweicloudsdkiec.v1.MetricsDimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this MetricInfo.

        指标维度列表

        :param dimensions: The dimensions of this MetricInfo.
        :type dimensions: list[:class:`huaweicloudsdkiec.v1.MetricsDimension`]
        """
        self._dimensions = dimensions

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MetricInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
