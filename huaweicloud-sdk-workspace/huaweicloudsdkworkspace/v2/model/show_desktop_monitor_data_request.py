# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDesktopMonitorDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'metric_name': 'str'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'metric_name': 'metric_name'
    }

    def __init__(self, desktop_id=None, start_time=None, end_time=None, metric_name=None):
        r"""ShowDesktopMonitorDataRequest

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param start_time: 监控开始时间：由日期加时间组成，UTC格式，例如“2021-05-11T11:45:42Z”。
        :type start_time: str
        :param end_time: 监控结束时间：由日期加时间组成，UTC格式，例如“2021-05-11T11:45:42Z”。
        :type end_time: str
        :param metric_name: 监控查询指标：例如 \&quot;cpu_util\&quot;，详情见下表；当metric_name为空时，为批量查询| 指标                                  | 指标名称          | 测量对象     | 监控周期 || ------------------------------------- | ----------------- | ------------ | -------- || cpu_util                              | CPU使用率         |    云桌面    | 5分钟    || mem_util                              | 内存使用率        |    云桌面    | 5分钟    || disk_util_inband                      | 磁盘使用率        |    云桌面    | 5分钟    || disk_read_bytes_rate                  | 磁盘读带宽        |    云桌面    | 5分钟    || disk_write_bytes_rate                 | 磁盘写带宽        |    云桌面    | 5分钟    || disk_read_requests_rate               | 磁盘读IOPS        |    云桌面    | 5分钟    || disk_write_requests_rate              | 磁盘写IOPS        |    云桌面    | 5分钟    || network_incoming_bytes_rate_inband    | 带内网络流入速率  |    云桌面    | 5分钟    || network_outgoing_bytes_rate_inband    | 带内网络流出速率  |    云桌面    | 5分钟    || network_incoming_bytes_aggregate_rate | 带外网络流入速率  |    云桌面    | 5分钟    || network_outgoing_bytes_aggregate_rate | 带外网络流出速率  |    云桌面    | 5分钟    || network_vm_connections                | 网络连接数        |    云桌面    | 5分钟    || cpu_credit_usage                      | CPU积分使用量     |    云桌面    | 5分钟    || cpu_credit_balance                    | CPU积分累积量     |    云桌面    | 5分钟    || cpu_surplus_credit_balance            | CPU超额积分累积量 |    云桌面    | 5分钟    || cpu_surplus_credit_charged            | CPU超额积分收费量 |    云桌面    | 5分钟    || user_online_info                      | 用户在线信息      |    云桌面    | -        |
        :type metric_name: str
        """
        
        

        self._desktop_id = None
        self._start_time = None
        self._end_time = None
        self._metric_name = None
        self.discriminator = None

        self.desktop_id = desktop_id
        self.start_time = start_time
        self.end_time = end_time
        if metric_name is not None:
            self.metric_name = metric_name

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this ShowDesktopMonitorDataRequest.

        桌面ID。

        :return: The desktop_id of this ShowDesktopMonitorDataRequest.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this ShowDesktopMonitorDataRequest.

        桌面ID。

        :param desktop_id: The desktop_id of this ShowDesktopMonitorDataRequest.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowDesktopMonitorDataRequest.

        监控开始时间：由日期加时间组成，UTC格式，例如“2021-05-11T11:45:42Z”。

        :return: The start_time of this ShowDesktopMonitorDataRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowDesktopMonitorDataRequest.

        监控开始时间：由日期加时间组成，UTC格式，例如“2021-05-11T11:45:42Z”。

        :param start_time: The start_time of this ShowDesktopMonitorDataRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowDesktopMonitorDataRequest.

        监控结束时间：由日期加时间组成，UTC格式，例如“2021-05-11T11:45:42Z”。

        :return: The end_time of this ShowDesktopMonitorDataRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowDesktopMonitorDataRequest.

        监控结束时间：由日期加时间组成，UTC格式，例如“2021-05-11T11:45:42Z”。

        :param end_time: The end_time of this ShowDesktopMonitorDataRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowDesktopMonitorDataRequest.

        监控查询指标：例如 \"cpu_util\"，详情见下表；当metric_name为空时，为批量查询| 指标                                  | 指标名称          | 测量对象     | 监控周期 || ------------------------------------- | ----------------- | ------------ | -------- || cpu_util                              | CPU使用率         |    云桌面    | 5分钟    || mem_util                              | 内存使用率        |    云桌面    | 5分钟    || disk_util_inband                      | 磁盘使用率        |    云桌面    | 5分钟    || disk_read_bytes_rate                  | 磁盘读带宽        |    云桌面    | 5分钟    || disk_write_bytes_rate                 | 磁盘写带宽        |    云桌面    | 5分钟    || disk_read_requests_rate               | 磁盘读IOPS        |    云桌面    | 5分钟    || disk_write_requests_rate              | 磁盘写IOPS        |    云桌面    | 5分钟    || network_incoming_bytes_rate_inband    | 带内网络流入速率  |    云桌面    | 5分钟    || network_outgoing_bytes_rate_inband    | 带内网络流出速率  |    云桌面    | 5分钟    || network_incoming_bytes_aggregate_rate | 带外网络流入速率  |    云桌面    | 5分钟    || network_outgoing_bytes_aggregate_rate | 带外网络流出速率  |    云桌面    | 5分钟    || network_vm_connections                | 网络连接数        |    云桌面    | 5分钟    || cpu_credit_usage                      | CPU积分使用量     |    云桌面    | 5分钟    || cpu_credit_balance                    | CPU积分累积量     |    云桌面    | 5分钟    || cpu_surplus_credit_balance            | CPU超额积分累积量 |    云桌面    | 5分钟    || cpu_surplus_credit_charged            | CPU超额积分收费量 |    云桌面    | 5分钟    || user_online_info                      | 用户在线信息      |    云桌面    | -        |

        :return: The metric_name of this ShowDesktopMonitorDataRequest.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowDesktopMonitorDataRequest.

        监控查询指标：例如 \"cpu_util\"，详情见下表；当metric_name为空时，为批量查询| 指标                                  | 指标名称          | 测量对象     | 监控周期 || ------------------------------------- | ----------------- | ------------ | -------- || cpu_util                              | CPU使用率         |    云桌面    | 5分钟    || mem_util                              | 内存使用率        |    云桌面    | 5分钟    || disk_util_inband                      | 磁盘使用率        |    云桌面    | 5分钟    || disk_read_bytes_rate                  | 磁盘读带宽        |    云桌面    | 5分钟    || disk_write_bytes_rate                 | 磁盘写带宽        |    云桌面    | 5分钟    || disk_read_requests_rate               | 磁盘读IOPS        |    云桌面    | 5分钟    || disk_write_requests_rate              | 磁盘写IOPS        |    云桌面    | 5分钟    || network_incoming_bytes_rate_inband    | 带内网络流入速率  |    云桌面    | 5分钟    || network_outgoing_bytes_rate_inband    | 带内网络流出速率  |    云桌面    | 5分钟    || network_incoming_bytes_aggregate_rate | 带外网络流入速率  |    云桌面    | 5分钟    || network_outgoing_bytes_aggregate_rate | 带外网络流出速率  |    云桌面    | 5分钟    || network_vm_connections                | 网络连接数        |    云桌面    | 5分钟    || cpu_credit_usage                      | CPU积分使用量     |    云桌面    | 5分钟    || cpu_credit_balance                    | CPU积分累积量     |    云桌面    | 5分钟    || cpu_surplus_credit_balance            | CPU超额积分累积量 |    云桌面    | 5分钟    || cpu_surplus_credit_charged            | CPU超额积分收费量 |    云桌面    | 5分钟    || user_online_info                      | 用户在线信息      |    云桌面    | -        |

        :param metric_name: The metric_name of this ShowDesktopMonitorDataRequest.
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
        if not isinstance(other, ShowDesktopMonitorDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
