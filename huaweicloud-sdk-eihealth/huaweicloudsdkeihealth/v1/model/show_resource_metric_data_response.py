# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceMetricDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_points': 'list[DataPointDto]',
        'metric_name': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'data_points': 'data_points',
        'metric_name': 'metric_name',
        'resource_id': 'resource_id'
    }

    def __init__(self, data_points=None, metric_name=None, resource_id=None):
        """ShowResourceMetricDataResponse

        The model defined in huaweicloud sdk

        :param data_points: 监控数据列表
        :type data_points: list[:class:`huaweicloudsdkeihealth.v1.DataPointDto`]
        :param metric_name: 监控指标名称
        :type metric_name: str
        :param resource_id: 监控资源id
        :type resource_id: str
        """
        
        super(ShowResourceMetricDataResponse, self).__init__()

        self._data_points = None
        self._metric_name = None
        self._resource_id = None
        self.discriminator = None

        if data_points is not None:
            self.data_points = data_points
        if metric_name is not None:
            self.metric_name = metric_name
        if resource_id is not None:
            self.resource_id = resource_id

    @property
    def data_points(self):
        """Gets the data_points of this ShowResourceMetricDataResponse.

        监控数据列表

        :return: The data_points of this ShowResourceMetricDataResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.DataPointDto`]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this ShowResourceMetricDataResponse.

        监控数据列表

        :param data_points: The data_points of this ShowResourceMetricDataResponse.
        :type data_points: list[:class:`huaweicloudsdkeihealth.v1.DataPointDto`]
        """
        self._data_points = data_points

    @property
    def metric_name(self):
        """Gets the metric_name of this ShowResourceMetricDataResponse.

        监控指标名称

        :return: The metric_name of this ShowResourceMetricDataResponse.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this ShowResourceMetricDataResponse.

        监控指标名称

        :param metric_name: The metric_name of this ShowResourceMetricDataResponse.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def resource_id(self):
        """Gets the resource_id of this ShowResourceMetricDataResponse.

        监控资源id

        :return: The resource_id of this ShowResourceMetricDataResponse.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ShowResourceMetricDataResponse.

        监控资源id

        :param resource_id: The resource_id of this ShowResourceMetricDataResponse.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, ShowResourceMetricDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
