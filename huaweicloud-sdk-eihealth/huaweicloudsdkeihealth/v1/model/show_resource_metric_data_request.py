# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceMetricDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'from_time': 'int',
        'to_time': 'int',
        'period': 'str',
        'method': 'str',
        'metric_name': 'str',
        'resource_id': 'str',
        'device_id': 'str'
    }

    attribute_map = {
        'from_time': 'from_time',
        'to_time': 'to_time',
        'period': 'period',
        'method': 'method',
        'metric_name': 'metric_name',
        'resource_id': 'resource_id',
        'device_id': 'device_id'
    }

    def __init__(self, from_time=None, to_time=None, period=None, method=None, metric_name=None, resource_id=None, device_id=None):
        """ShowResourceMetricDataRequest

        The model defined in huaweicloud sdk

        :param from_time: 查询监控数据起始时间，UNIX时间戳，单位毫秒，不填时默认为当前时间
        :type from_time: int
        :param to_time: 查询数据截止时间，UNIX时间戳，单位毫秒，不填时默认为当前时间
        :type to_time: int
        :param period: 监控数据周期。枚举值，取值范围：real_time（实时数据）、five_minutes（5分钟粒度）、fifteen_to_twenty_minutes（15-20分钟粒度）、one_hour（1小时粒度），不填时默认为real_time
        :type period: str
        :param method: 统计方法。枚举值，取值范围：max（最大值）、min（最小值）、average（平均值），不填时默认为max
        :type method: str
        :param metric_name: 查询的监控指标名称
        :type metric_name: str
        :param resource_id: 查询的监控资源对象id，当查询存储资源和计算节点资源中的集群监控数据时，不需要填写资源id
        :type resource_id: str
        :param device_id: 显卡id，仅查询裸金属节点的gpu监控时，需要指定
        :type device_id: str
        """
        
        

        self._from_time = None
        self._to_time = None
        self._period = None
        self._method = None
        self._metric_name = None
        self._resource_id = None
        self._device_id = None
        self.discriminator = None

        if from_time is not None:
            self.from_time = from_time
        if to_time is not None:
            self.to_time = to_time
        if period is not None:
            self.period = period
        if method is not None:
            self.method = method
        self.metric_name = metric_name
        if resource_id is not None:
            self.resource_id = resource_id
        if device_id is not None:
            self.device_id = device_id

    @property
    def from_time(self):
        """Gets the from_time of this ShowResourceMetricDataRequest.

        查询监控数据起始时间，UNIX时间戳，单位毫秒，不填时默认为当前时间

        :return: The from_time of this ShowResourceMetricDataRequest.
        :rtype: int
        """
        return self._from_time

    @from_time.setter
    def from_time(self, from_time):
        """Sets the from_time of this ShowResourceMetricDataRequest.

        查询监控数据起始时间，UNIX时间戳，单位毫秒，不填时默认为当前时间

        :param from_time: The from_time of this ShowResourceMetricDataRequest.
        :type from_time: int
        """
        self._from_time = from_time

    @property
    def to_time(self):
        """Gets the to_time of this ShowResourceMetricDataRequest.

        查询数据截止时间，UNIX时间戳，单位毫秒，不填时默认为当前时间

        :return: The to_time of this ShowResourceMetricDataRequest.
        :rtype: int
        """
        return self._to_time

    @to_time.setter
    def to_time(self, to_time):
        """Sets the to_time of this ShowResourceMetricDataRequest.

        查询数据截止时间，UNIX时间戳，单位毫秒，不填时默认为当前时间

        :param to_time: The to_time of this ShowResourceMetricDataRequest.
        :type to_time: int
        """
        self._to_time = to_time

    @property
    def period(self):
        """Gets the period of this ShowResourceMetricDataRequest.

        监控数据周期。枚举值，取值范围：real_time（实时数据）、five_minutes（5分钟粒度）、fifteen_to_twenty_minutes（15-20分钟粒度）、one_hour（1小时粒度），不填时默认为real_time

        :return: The period of this ShowResourceMetricDataRequest.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ShowResourceMetricDataRequest.

        监控数据周期。枚举值，取值范围：real_time（实时数据）、five_minutes（5分钟粒度）、fifteen_to_twenty_minutes（15-20分钟粒度）、one_hour（1小时粒度），不填时默认为real_time

        :param period: The period of this ShowResourceMetricDataRequest.
        :type period: str
        """
        self._period = period

    @property
    def method(self):
        """Gets the method of this ShowResourceMetricDataRequest.

        统计方法。枚举值，取值范围：max（最大值）、min（最小值）、average（平均值），不填时默认为max

        :return: The method of this ShowResourceMetricDataRequest.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ShowResourceMetricDataRequest.

        统计方法。枚举值，取值范围：max（最大值）、min（最小值）、average（平均值），不填时默认为max

        :param method: The method of this ShowResourceMetricDataRequest.
        :type method: str
        """
        self._method = method

    @property
    def metric_name(self):
        """Gets the metric_name of this ShowResourceMetricDataRequest.

        查询的监控指标名称

        :return: The metric_name of this ShowResourceMetricDataRequest.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this ShowResourceMetricDataRequest.

        查询的监控指标名称

        :param metric_name: The metric_name of this ShowResourceMetricDataRequest.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def resource_id(self):
        """Gets the resource_id of this ShowResourceMetricDataRequest.

        查询的监控资源对象id，当查询存储资源和计算节点资源中的集群监控数据时，不需要填写资源id

        :return: The resource_id of this ShowResourceMetricDataRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ShowResourceMetricDataRequest.

        查询的监控资源对象id，当查询存储资源和计算节点资源中的集群监控数据时，不需要填写资源id

        :param resource_id: The resource_id of this ShowResourceMetricDataRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def device_id(self):
        """Gets the device_id of this ShowResourceMetricDataRequest.

        显卡id，仅查询裸金属节点的gpu监控时，需要指定

        :return: The device_id of this ShowResourceMetricDataRequest.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ShowResourceMetricDataRequest.

        显卡id，仅查询裸金属节点的gpu监控时，需要指定

        :param device_id: The device_id of this ShowResourceMetricDataRequest.
        :type device_id: str
        """
        self._device_id = device_id

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
        if not isinstance(other, ShowResourceMetricDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
