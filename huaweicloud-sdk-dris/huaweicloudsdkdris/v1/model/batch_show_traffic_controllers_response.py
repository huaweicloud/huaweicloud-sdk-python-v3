# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchShowTrafficControllersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'traffic_controller_devices': 'list[TrafficControllerDTO]'
    }

    attribute_map = {
        'count': 'count',
        'traffic_controller_devices': 'traffic_controller_devices'
    }

    def __init__(self, count=None, traffic_controller_devices=None):
        """BatchShowTrafficControllersResponse

        The model defined in huaweicloud sdk

        :param count: **参数说明**：返回信号机设备的总体数量。
        :type count: int
        :param traffic_controller_devices: **参数说明**：数据列表。
        :type traffic_controller_devices: list[:class:`huaweicloudsdkdris.v1.TrafficControllerDTO`]
        """
        
        super(BatchShowTrafficControllersResponse, self).__init__()

        self._count = None
        self._traffic_controller_devices = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if traffic_controller_devices is not None:
            self.traffic_controller_devices = traffic_controller_devices

    @property
    def count(self):
        """Gets the count of this BatchShowTrafficControllersResponse.

        **参数说明**：返回信号机设备的总体数量。

        :return: The count of this BatchShowTrafficControllersResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BatchShowTrafficControllersResponse.

        **参数说明**：返回信号机设备的总体数量。

        :param count: The count of this BatchShowTrafficControllersResponse.
        :type count: int
        """
        self._count = count

    @property
    def traffic_controller_devices(self):
        """Gets the traffic_controller_devices of this BatchShowTrafficControllersResponse.

        **参数说明**：数据列表。

        :return: The traffic_controller_devices of this BatchShowTrafficControllersResponse.
        :rtype: list[:class:`huaweicloudsdkdris.v1.TrafficControllerDTO`]
        """
        return self._traffic_controller_devices

    @traffic_controller_devices.setter
    def traffic_controller_devices(self, traffic_controller_devices):
        """Sets the traffic_controller_devices of this BatchShowTrafficControllersResponse.

        **参数说明**：数据列表。

        :param traffic_controller_devices: The traffic_controller_devices of this BatchShowTrafficControllersResponse.
        :type traffic_controller_devices: list[:class:`huaweicloudsdkdris.v1.TrafficControllerDTO`]
        """
        self._traffic_controller_devices = traffic_controller_devices

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
        if not isinstance(other, BatchShowTrafficControllersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
