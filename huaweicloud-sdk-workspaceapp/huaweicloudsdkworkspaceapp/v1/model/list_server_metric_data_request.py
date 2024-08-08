# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServerMetricDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'namespace': 'str',
        'metric_name': 'str',
        '_from': 'str',
        'to': 'str',
        'period': 'int',
        'filter': 'str'
    }

    attribute_map = {
        'server_id': 'server_id',
        'namespace': 'namespace',
        'metric_name': 'metric_name',
        '_from': 'from',
        'to': 'to',
        'period': 'period',
        'filter': 'filter'
    }

    def __init__(self, server_id=None, namespace=None, metric_name=None, _from=None, to=None, period=None, filter=None):
        """ListServerMetricDataRequest

        The model defined in huaweicloud sdk

        :param server_id: 服务器唯一标识。
        :type server_id: str
        :param namespace: 服务的命名空间：例如 \&quot;SYS.ECS/AGT.ECS\&quot;，当namespace为AGT.ECS，则查询GPU监控指标：  - SYS.ECS：弹性云服务器的基础监控指标。  - AGT.ECS：弹性云服务器操作系统监控的监控指标（GPU指标）。
        :type namespace: str
        :param metric_name: 监控查询指标名称:  - SYS.ECS命名空间的指标名称,请参考帮助文档：“[弹性云服务器支持的基础监控指标](https://support.huaweicloud.com/usermanual-ecs/ecs_03_1002.html)”。  - AGT.ECS命名空间的指标名称,请参考帮助文档：“[操作系统监控指标：GPU](https://support.huaweicloud.com/usermanual-ecs/ecs_03_1003.html#section11)”。
        :type metric_name: str
        :param _from: 查询数据起始时间，UNIX时间戳，单位毫秒。
        :type _from: str
        :param to: 查询数据截止时间UNIX时间戳，单位毫秒。from必须小于to。
        :type to: str
        :param period: 监控数据粒度。 取值范围：  - 1: 实时数据。  - 300: 5分钟粒度。  - 1200: 20分钟粒度。  - 3600: 1小时粒度。  - 14400: 4小时粒度。  - 86400: 1天粒度。
        :type period: int
        :param filter: 数据聚合方式，支持的聚合方式如下:  - average：聚合周期内指标数据的平均值。  - max：聚合周期内指标数据的最大值。  - min：聚合周期内指标数据的最小值。  - sum：聚合周期内指标数据的求和值。  - variance：聚合周期内指标数据的方差。
        :type filter: str
        """
        
        

        self._server_id = None
        self._namespace = None
        self._metric_name = None
        self.__from = None
        self._to = None
        self._period = None
        self._filter = None
        self.discriminator = None

        self.server_id = server_id
        self.namespace = namespace
        self.metric_name = metric_name
        self._from = _from
        self.to = to
        self.period = period
        self.filter = filter

    @property
    def server_id(self):
        """Gets the server_id of this ListServerMetricDataRequest.

        服务器唯一标识。

        :return: The server_id of this ListServerMetricDataRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ListServerMetricDataRequest.

        服务器唯一标识。

        :param server_id: The server_id of this ListServerMetricDataRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def namespace(self):
        """Gets the namespace of this ListServerMetricDataRequest.

        服务的命名空间：例如 \"SYS.ECS/AGT.ECS\"，当namespace为AGT.ECS，则查询GPU监控指标：  - SYS.ECS：弹性云服务器的基础监控指标。  - AGT.ECS：弹性云服务器操作系统监控的监控指标（GPU指标）。

        :return: The namespace of this ListServerMetricDataRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListServerMetricDataRequest.

        服务的命名空间：例如 \"SYS.ECS/AGT.ECS\"，当namespace为AGT.ECS，则查询GPU监控指标：  - SYS.ECS：弹性云服务器的基础监控指标。  - AGT.ECS：弹性云服务器操作系统监控的监控指标（GPU指标）。

        :param namespace: The namespace of this ListServerMetricDataRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def metric_name(self):
        """Gets the metric_name of this ListServerMetricDataRequest.

        监控查询指标名称:  - SYS.ECS命名空间的指标名称,请参考帮助文档：“[弹性云服务器支持的基础监控指标](https://support.huaweicloud.com/usermanual-ecs/ecs_03_1002.html)”。  - AGT.ECS命名空间的指标名称,请参考帮助文档：“[操作系统监控指标：GPU](https://support.huaweicloud.com/usermanual-ecs/ecs_03_1003.html#section11)”。

        :return: The metric_name of this ListServerMetricDataRequest.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this ListServerMetricDataRequest.

        监控查询指标名称:  - SYS.ECS命名空间的指标名称,请参考帮助文档：“[弹性云服务器支持的基础监控指标](https://support.huaweicloud.com/usermanual-ecs/ecs_03_1002.html)”。  - AGT.ECS命名空间的指标名称,请参考帮助文档：“[操作系统监控指标：GPU](https://support.huaweicloud.com/usermanual-ecs/ecs_03_1003.html#section11)”。

        :param metric_name: The metric_name of this ListServerMetricDataRequest.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def _from(self):
        """Gets the _from of this ListServerMetricDataRequest.

        查询数据起始时间，UNIX时间戳，单位毫秒。

        :return: The _from of this ListServerMetricDataRequest.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ListServerMetricDataRequest.

        查询数据起始时间，UNIX时间戳，单位毫秒。

        :param _from: The _from of this ListServerMetricDataRequest.
        :type _from: str
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this ListServerMetricDataRequest.

        查询数据截止时间UNIX时间戳，单位毫秒。from必须小于to。

        :return: The to of this ListServerMetricDataRequest.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ListServerMetricDataRequest.

        查询数据截止时间UNIX时间戳，单位毫秒。from必须小于to。

        :param to: The to of this ListServerMetricDataRequest.
        :type to: str
        """
        self._to = to

    @property
    def period(self):
        """Gets the period of this ListServerMetricDataRequest.

        监控数据粒度。 取值范围：  - 1: 实时数据。  - 300: 5分钟粒度。  - 1200: 20分钟粒度。  - 3600: 1小时粒度。  - 14400: 4小时粒度。  - 86400: 1天粒度。

        :return: The period of this ListServerMetricDataRequest.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ListServerMetricDataRequest.

        监控数据粒度。 取值范围：  - 1: 实时数据。  - 300: 5分钟粒度。  - 1200: 20分钟粒度。  - 3600: 1小时粒度。  - 14400: 4小时粒度。  - 86400: 1天粒度。

        :param period: The period of this ListServerMetricDataRequest.
        :type period: int
        """
        self._period = period

    @property
    def filter(self):
        """Gets the filter of this ListServerMetricDataRequest.

        数据聚合方式，支持的聚合方式如下:  - average：聚合周期内指标数据的平均值。  - max：聚合周期内指标数据的最大值。  - min：聚合周期内指标数据的最小值。  - sum：聚合周期内指标数据的求和值。  - variance：聚合周期内指标数据的方差。

        :return: The filter of this ListServerMetricDataRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ListServerMetricDataRequest.

        数据聚合方式，支持的聚合方式如下:  - average：聚合周期内指标数据的平均值。  - max：聚合周期内指标数据的最大值。  - min：聚合周期内指标数据的最小值。  - sum：聚合周期内指标数据的求和值。  - variance：聚合周期内指标数据的方差。

        :param filter: The filter of this ListServerMetricDataRequest.
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
        if not isinstance(other, ListServerMetricDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
