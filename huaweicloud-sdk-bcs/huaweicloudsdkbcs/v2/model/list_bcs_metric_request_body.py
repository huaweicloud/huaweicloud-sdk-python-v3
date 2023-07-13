# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBcsMetricRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_names': 'list[str]'
    }

    attribute_map = {
        'metric_names': 'metric_names'
    }

    def __init__(self, metric_names=None):
        """ListBcsMetricRequestBody

        The model defined in huaweicloud sdk

        :param metric_names: 指标列表 取值范围 cpuUsage：CPU使用率 diskUsedRate：磁盘使用率 memUsedRate：物理内存使用率 sendBytesRate：上行Bps recvBytesRate：下行Bps cpuCoreLimit：CPU内核总量 cpuCoreUsed：CPU内核占用 totalMem：物理内存总量 freeMem：可用物理内存 diskCapacity：磁盘空间容量 diskAvailableCapacity：可用磁盘空间 默认值：前5项 
        :type metric_names: list[str]
        """
        
        

        self._metric_names = None
        self.discriminator = None

        if metric_names is not None:
            self.metric_names = metric_names

    @property
    def metric_names(self):
        """Gets the metric_names of this ListBcsMetricRequestBody.

        指标列表 取值范围 cpuUsage：CPU使用率 diskUsedRate：磁盘使用率 memUsedRate：物理内存使用率 sendBytesRate：上行Bps recvBytesRate：下行Bps cpuCoreLimit：CPU内核总量 cpuCoreUsed：CPU内核占用 totalMem：物理内存总量 freeMem：可用物理内存 diskCapacity：磁盘空间容量 diskAvailableCapacity：可用磁盘空间 默认值：前5项 

        :return: The metric_names of this ListBcsMetricRequestBody.
        :rtype: list[str]
        """
        return self._metric_names

    @metric_names.setter
    def metric_names(self, metric_names):
        """Sets the metric_names of this ListBcsMetricRequestBody.

        指标列表 取值范围 cpuUsage：CPU使用率 diskUsedRate：磁盘使用率 memUsedRate：物理内存使用率 sendBytesRate：上行Bps recvBytesRate：下行Bps cpuCoreLimit：CPU内核总量 cpuCoreUsed：CPU内核占用 totalMem：物理内存总量 freeMem：可用物理内存 diskCapacity：磁盘空间容量 diskAvailableCapacity：可用磁盘空间 默认值：前5项 

        :param metric_names: The metric_names of this ListBcsMetricRequestBody.
        :type metric_names: list[str]
        """
        self._metric_names = metric_names

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
        if not isinstance(other, ListBcsMetricRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
