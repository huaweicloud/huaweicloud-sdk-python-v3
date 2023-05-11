# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskInstanceMetricDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_points': 'list[DataPointDto]'
    }

    attribute_map = {
        'data_points': 'data_points'
    }

    def __init__(self, data_points=None):
        """ShowTaskInstanceMetricDataResponse

        The model defined in huaweicloud sdk

        :param data_points: 监控数据列表
        :type data_points: list[:class:`huaweicloudsdkeihealth.v1.DataPointDto`]
        """
        
        super(ShowTaskInstanceMetricDataResponse, self).__init__()

        self._data_points = None
        self.discriminator = None

        if data_points is not None:
            self.data_points = data_points

    @property
    def data_points(self):
        """Gets the data_points of this ShowTaskInstanceMetricDataResponse.

        监控数据列表

        :return: The data_points of this ShowTaskInstanceMetricDataResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.DataPointDto`]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this ShowTaskInstanceMetricDataResponse.

        监控数据列表

        :param data_points: The data_points of this ShowTaskInstanceMetricDataResponse.
        :type data_points: list[:class:`huaweicloudsdkeihealth.v1.DataPointDto`]
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
        if not isinstance(other, ShowTaskInstanceMetricDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
