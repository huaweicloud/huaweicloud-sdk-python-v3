# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSingleMetricRequestBody:

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
        'start_at': 'int',
        'end_at': 'int',
        'instance_infos': 'list[InstanceInfoDtoForMetric]'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'instance_infos': 'instance_infos'
    }

    def __init__(self, metric_name=None, start_at=None, end_at=None, instance_infos=None):
        r"""ShowSingleMetricRequestBody

        The model defined in huaweicloud sdk

        :param metric_name: 指标名称
        :type metric_name: str
        :param start_at: 开始时间（Unix timestamp，毫秒）
        :type start_at: int
        :param end_at: 结束时间（Unix timestamp，毫秒）
        :type end_at: int
        :param instance_infos: 实例信息列表
        :type instance_infos: list[:class:`huaweicloudsdkdas.v3.InstanceInfoDtoForMetric`]
        """
        
        

        self._metric_name = None
        self._start_at = None
        self._end_at = None
        self._instance_infos = None
        self.discriminator = None

        self.metric_name = metric_name
        self.start_at = start_at
        self.end_at = end_at
        self.instance_infos = instance_infos

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowSingleMetricRequestBody.

        指标名称

        :return: The metric_name of this ShowSingleMetricRequestBody.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowSingleMetricRequestBody.

        指标名称

        :param metric_name: The metric_name of this ShowSingleMetricRequestBody.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def start_at(self):
        r"""Gets the start_at of this ShowSingleMetricRequestBody.

        开始时间（Unix timestamp，毫秒）

        :return: The start_at of this ShowSingleMetricRequestBody.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ShowSingleMetricRequestBody.

        开始时间（Unix timestamp，毫秒）

        :param start_at: The start_at of this ShowSingleMetricRequestBody.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ShowSingleMetricRequestBody.

        结束时间（Unix timestamp，毫秒）

        :return: The end_at of this ShowSingleMetricRequestBody.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ShowSingleMetricRequestBody.

        结束时间（Unix timestamp，毫秒）

        :param end_at: The end_at of this ShowSingleMetricRequestBody.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def instance_infos(self):
        r"""Gets the instance_infos of this ShowSingleMetricRequestBody.

        实例信息列表

        :return: The instance_infos of this ShowSingleMetricRequestBody.
        :rtype: list[:class:`huaweicloudsdkdas.v3.InstanceInfoDtoForMetric`]
        """
        return self._instance_infos

    @instance_infos.setter
    def instance_infos(self, instance_infos):
        r"""Sets the instance_infos of this ShowSingleMetricRequestBody.

        实例信息列表

        :param instance_infos: The instance_infos of this ShowSingleMetricRequestBody.
        :type instance_infos: list[:class:`huaweicloudsdkdas.v3.InstanceInfoDtoForMetric`]
        """
        self._instance_infos = instance_infos

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
        if not isinstance(other, ShowSingleMetricRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
