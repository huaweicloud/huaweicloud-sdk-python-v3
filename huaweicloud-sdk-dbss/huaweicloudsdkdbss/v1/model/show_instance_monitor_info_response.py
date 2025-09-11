# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceMonitorInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disk_infos': 'DiskInfo',
        'system_infos': 'list[SystemInfo]',
        'traffic_infos': 'list[TrafficInfo]'
    }

    attribute_map = {
        'disk_infos': 'disk_infos',
        'system_infos': 'system_infos',
        'traffic_infos': 'traffic_infos'
    }

    def __init__(self, disk_infos=None, system_infos=None, traffic_infos=None):
        r"""ShowInstanceMonitorInfoResponse

        The model defined in huaweicloud sdk

        :param disk_infos: 
        :type disk_infos: :class:`huaweicloudsdkdbss.v1.DiskInfo`
        :param system_infos: 系统信息
        :type system_infos: list[:class:`huaweicloudsdkdbss.v1.SystemInfo`]
        :param traffic_infos: 流量统计
        :type traffic_infos: list[:class:`huaweicloudsdkdbss.v1.TrafficInfo`]
        """
        
        super(ShowInstanceMonitorInfoResponse, self).__init__()

        self._disk_infos = None
        self._system_infos = None
        self._traffic_infos = None
        self.discriminator = None

        if disk_infos is not None:
            self.disk_infos = disk_infos
        if system_infos is not None:
            self.system_infos = system_infos
        if traffic_infos is not None:
            self.traffic_infos = traffic_infos

    @property
    def disk_infos(self):
        r"""Gets the disk_infos of this ShowInstanceMonitorInfoResponse.

        :return: The disk_infos of this ShowInstanceMonitorInfoResponse.
        :rtype: :class:`huaweicloudsdkdbss.v1.DiskInfo`
        """
        return self._disk_infos

    @disk_infos.setter
    def disk_infos(self, disk_infos):
        r"""Sets the disk_infos of this ShowInstanceMonitorInfoResponse.

        :param disk_infos: The disk_infos of this ShowInstanceMonitorInfoResponse.
        :type disk_infos: :class:`huaweicloudsdkdbss.v1.DiskInfo`
        """
        self._disk_infos = disk_infos

    @property
    def system_infos(self):
        r"""Gets the system_infos of this ShowInstanceMonitorInfoResponse.

        系统信息

        :return: The system_infos of this ShowInstanceMonitorInfoResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.SystemInfo`]
        """
        return self._system_infos

    @system_infos.setter
    def system_infos(self, system_infos):
        r"""Sets the system_infos of this ShowInstanceMonitorInfoResponse.

        系统信息

        :param system_infos: The system_infos of this ShowInstanceMonitorInfoResponse.
        :type system_infos: list[:class:`huaweicloudsdkdbss.v1.SystemInfo`]
        """
        self._system_infos = system_infos

    @property
    def traffic_infos(self):
        r"""Gets the traffic_infos of this ShowInstanceMonitorInfoResponse.

        流量统计

        :return: The traffic_infos of this ShowInstanceMonitorInfoResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.TrafficInfo`]
        """
        return self._traffic_infos

    @traffic_infos.setter
    def traffic_infos(self, traffic_infos):
        r"""Sets the traffic_infos of this ShowInstanceMonitorInfoResponse.

        流量统计

        :param traffic_infos: The traffic_infos of this ShowInstanceMonitorInfoResponse.
        :type traffic_infos: list[:class:`huaweicloudsdkdbss.v1.TrafficInfo`]
        """
        self._traffic_infos = traffic_infos

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
        if not isinstance(other, ShowInstanceMonitorInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
