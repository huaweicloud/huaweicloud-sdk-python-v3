# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVmMonitorRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'metric_name': 'str',
        'instance_id': 'str',
        'vsm_id': 'str',
        '_from': 'int',
        'to': 'int',
        'period': 'int',
        'filter': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'metric_name': 'metric_name',
        'instance_id': 'instance_id',
        'vsm_id': 'vsm_id',
        '_from': 'from',
        'to': 'to',
        'period': 'period',
        'filter': 'filter'
    }

    def __init__(self, namespace=None, metric_name=None, instance_id=None, vsm_id=None, _from=None, to=None, period=None, filter=None):
        r"""ShowVmMonitorRequest

        The model defined in huaweicloud sdk

        :param namespace: 所属空间，分别从不同的来源获取监控数据，有：ECS，DHSM
        :type namespace: str
        :param metric_name: 指标名称，有：mem_util，cpu_uttl，network_outgoing_bytes_rate_inband
        :type metric_name: str
        :param instance_id: 实例id，默认空字符串，默认查询所有实例。
        :type instance_id: str
        :param vsm_id: 虚拟机id
        :type vsm_id: str
        :param _from: 查询时间范围的起始时间，毫秒时间戳，默认0，默认查询从三天前。
        :type _from: int
        :param to: 查询时间范围的终止时间，毫秒时间戳，默认0，默认查询到当前时间。
        :type to: int
        :param period: 统计数据周期，默认0，默认周期为5分钟
        :type period: int
        :param filter: 统计值类型，默认min，默认查询最小值
        :type filter: str
        """
        
        

        self._namespace = None
        self._metric_name = None
        self._instance_id = None
        self._vsm_id = None
        self.__from = None
        self._to = None
        self._period = None
        self._filter = None
        self.discriminator = None

        self.namespace = namespace
        self.metric_name = metric_name
        if instance_id is not None:
            self.instance_id = instance_id
        if vsm_id is not None:
            self.vsm_id = vsm_id
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if period is not None:
            self.period = period
        if filter is not None:
            self.filter = filter

    @property
    def namespace(self):
        r"""Gets the namespace of this ShowVmMonitorRequest.

        所属空间，分别从不同的来源获取监控数据，有：ECS，DHSM

        :return: The namespace of this ShowVmMonitorRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ShowVmMonitorRequest.

        所属空间，分别从不同的来源获取监控数据，有：ECS，DHSM

        :param namespace: The namespace of this ShowVmMonitorRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowVmMonitorRequest.

        指标名称，有：mem_util，cpu_uttl，network_outgoing_bytes_rate_inband

        :return: The metric_name of this ShowVmMonitorRequest.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowVmMonitorRequest.

        指标名称，有：mem_util，cpu_uttl，network_outgoing_bytes_rate_inband

        :param metric_name: The metric_name of this ShowVmMonitorRequest.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowVmMonitorRequest.

        实例id，默认空字符串，默认查询所有实例。

        :return: The instance_id of this ShowVmMonitorRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowVmMonitorRequest.

        实例id，默认空字符串，默认查询所有实例。

        :param instance_id: The instance_id of this ShowVmMonitorRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def vsm_id(self):
        r"""Gets the vsm_id of this ShowVmMonitorRequest.

        虚拟机id

        :return: The vsm_id of this ShowVmMonitorRequest.
        :rtype: str
        """
        return self._vsm_id

    @vsm_id.setter
    def vsm_id(self, vsm_id):
        r"""Sets the vsm_id of this ShowVmMonitorRequest.

        虚拟机id

        :param vsm_id: The vsm_id of this ShowVmMonitorRequest.
        :type vsm_id: str
        """
        self._vsm_id = vsm_id

    @property
    def _from(self):
        r"""Gets the _from of this ShowVmMonitorRequest.

        查询时间范围的起始时间，毫秒时间戳，默认0，默认查询从三天前。

        :return: The _from of this ShowVmMonitorRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ShowVmMonitorRequest.

        查询时间范围的起始时间，毫秒时间戳，默认0，默认查询从三天前。

        :param _from: The _from of this ShowVmMonitorRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ShowVmMonitorRequest.

        查询时间范围的终止时间，毫秒时间戳，默认0，默认查询到当前时间。

        :return: The to of this ShowVmMonitorRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ShowVmMonitorRequest.

        查询时间范围的终止时间，毫秒时间戳，默认0，默认查询到当前时间。

        :param to: The to of this ShowVmMonitorRequest.
        :type to: int
        """
        self._to = to

    @property
    def period(self):
        r"""Gets the period of this ShowVmMonitorRequest.

        统计数据周期，默认0，默认周期为5分钟

        :return: The period of this ShowVmMonitorRequest.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this ShowVmMonitorRequest.

        统计数据周期，默认0，默认周期为5分钟

        :param period: The period of this ShowVmMonitorRequest.
        :type period: int
        """
        self._period = period

    @property
    def filter(self):
        r"""Gets the filter of this ShowVmMonitorRequest.

        统计值类型，默认min，默认查询最小值

        :return: The filter of this ShowVmMonitorRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ShowVmMonitorRequest.

        统计值类型，默认min，默认查询最小值

        :param filter: The filter of this ShowVmMonitorRequest.
        :type filter: str
        """
        self._filter = filter

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
        if not isinstance(other, ShowVmMonitorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
