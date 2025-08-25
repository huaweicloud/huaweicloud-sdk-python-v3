# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVmMonitorResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datapoints': 'list[Datapoint]',
        'metric_name': 'str'
    }

    attribute_map = {
        'datapoints': 'datapoints',
        'metric_name': 'metric_name'
    }

    def __init__(self, datapoints=None, metric_name=None):
        r"""ShowVmMonitorResponse

        The model defined in huaweicloud sdk

        :param datapoints: 指标的时间序列
        :type datapoints: list[:class:`huaweicloudsdkcpcs.v1.Datapoint`]
        :param metric_name: 指标名称，比如:cpu_util
        :type metric_name: str
        """
        
        super(ShowVmMonitorResponse, self).__init__()

        self._datapoints = None
        self._metric_name = None
        self.discriminator = None

        if datapoints is not None:
            self.datapoints = datapoints
        if metric_name is not None:
            self.metric_name = metric_name

    @property
    def datapoints(self):
        r"""Gets the datapoints of this ShowVmMonitorResponse.

        指标的时间序列

        :return: The datapoints of this ShowVmMonitorResponse.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.Datapoint`]
        """
        return self._datapoints

    @datapoints.setter
    def datapoints(self, datapoints):
        r"""Sets the datapoints of this ShowVmMonitorResponse.

        指标的时间序列

        :param datapoints: The datapoints of this ShowVmMonitorResponse.
        :type datapoints: list[:class:`huaweicloudsdkcpcs.v1.Datapoint`]
        """
        self._datapoints = datapoints

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowVmMonitorResponse.

        指标名称，比如:cpu_util

        :return: The metric_name of this ShowVmMonitorResponse.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowVmMonitorResponse.

        指标名称，比如:cpu_util

        :param metric_name: The metric_name of this ShowVmMonitorResponse.
        :type metric_name: str
        """
        self._metric_name = metric_name

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
        if not isinstance(other, ShowVmMonitorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
