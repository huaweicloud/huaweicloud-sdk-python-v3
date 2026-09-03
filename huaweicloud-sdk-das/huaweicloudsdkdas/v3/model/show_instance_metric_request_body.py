# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceMetricRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_type': 'str',
        'infos': 'list[InstanceInfoForMetric]',
        'metric_names': 'list[str]'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'infos': 'infos',
        'metric_names': 'metric_names'
    }

    def __init__(self, engine_type=None, infos=None, metric_names=None):
        r"""ShowInstanceMetricRequestBody

        The model defined in huaweicloud sdk

        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param infos: 实例信息列表
        :type infos: list[:class:`huaweicloudsdkdas.v3.InstanceInfoForMetric`]
        :param metric_names: 指标名称
        :type metric_names: list[str]
        """
        
        

        self._engine_type = None
        self._infos = None
        self._metric_names = None
        self.discriminator = None

        self.engine_type = engine_type
        self.infos = infos
        self.metric_names = metric_names

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ShowInstanceMetricRequestBody.

        数据库引擎类型

        :return: The engine_type of this ShowInstanceMetricRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ShowInstanceMetricRequestBody.

        数据库引擎类型

        :param engine_type: The engine_type of this ShowInstanceMetricRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def infos(self):
        r"""Gets the infos of this ShowInstanceMetricRequestBody.

        实例信息列表

        :return: The infos of this ShowInstanceMetricRequestBody.
        :rtype: list[:class:`huaweicloudsdkdas.v3.InstanceInfoForMetric`]
        """
        return self._infos

    @infos.setter
    def infos(self, infos):
        r"""Sets the infos of this ShowInstanceMetricRequestBody.

        实例信息列表

        :param infos: The infos of this ShowInstanceMetricRequestBody.
        :type infos: list[:class:`huaweicloudsdkdas.v3.InstanceInfoForMetric`]
        """
        self._infos = infos

    @property
    def metric_names(self):
        r"""Gets the metric_names of this ShowInstanceMetricRequestBody.

        指标名称

        :return: The metric_names of this ShowInstanceMetricRequestBody.
        :rtype: list[str]
        """
        return self._metric_names

    @metric_names.setter
    def metric_names(self, metric_names):
        r"""Sets the metric_names of this ShowInstanceMetricRequestBody.

        指标名称

        :param metric_names: The metric_names of this ShowInstanceMetricRequestBody.
        :type metric_names: list[str]
        """
        self._metric_names = metric_names

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
        if not isinstance(other, ShowInstanceMetricRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
