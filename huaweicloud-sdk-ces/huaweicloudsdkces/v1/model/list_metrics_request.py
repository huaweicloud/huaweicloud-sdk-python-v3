# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMetricsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dim_0': 'str',
        'dim_1': 'str',
        'dim_2': 'str',
        'limit': 'int',
        'metric_name': 'str',
        'namespace': 'str',
        'order': 'str',
        'start': 'str'
    }

    attribute_map = {
        'dim_0': 'dim.0',
        'dim_1': 'dim.1',
        'dim_2': 'dim.2',
        'limit': 'limit',
        'metric_name': 'metric_name',
        'namespace': 'namespace',
        'order': 'order',
        'start': 'start'
    }

    def __init__(self, dim_0=None, dim_1=None, dim_2=None, limit=None, metric_name=None, namespace=None, order=None, start=None):
        """ListMetricsRequest

        The model defined in huaweicloud sdk

        :param dim_0: 指标的维度，目前最大支持3个维度，从0开始；维度格式为dim.{i}&#x3D;key,value，最大值为256。 例如：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d；各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type dim_0: str
        :param dim_1: 指标的维度，目前最大支持3个维度，从0开始；维度格式为dim.{i}&#x3D;key,value，最大值为256。 例如：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d；各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type dim_1: str
        :param dim_2: 指标的维度，目前最大支持3个维度，从0开始；维度格式为dim.{i}&#x3D;key,value，最大值为256。 例如：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d；各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type dim_2: str
        :param limit: 取值范围(0,1000]，默认值为1000。  用于限制结果数据条数。
        :type limit: int
        :param metric_name: 指标名称，例如弹性云服务器监控指标中的cpu_util；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type metric_name: str
        :param namespace: 指标命名空间，格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，总长度最短为3，最大为32；各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type namespace: str
        :param order: 用于标识结果排序方法。  取值说明，默认为desc：  asc，升序 desc，降序
        :type order: str
        :param start: 分页起始值，格式为：namespace.metric_name.key:value 例如：start&#x3D;SYS.ECS.cpu_util.instance_id:d9112af5-6913-4f3b-bd0a-3f96711e004d
        :type start: str
        """
        
        

        self._dim_0 = None
        self._dim_1 = None
        self._dim_2 = None
        self._limit = None
        self._metric_name = None
        self._namespace = None
        self._order = None
        self._start = None
        self.discriminator = None

        if dim_0 is not None:
            self.dim_0 = dim_0
        if dim_1 is not None:
            self.dim_1 = dim_1
        if dim_2 is not None:
            self.dim_2 = dim_2
        if limit is not None:
            self.limit = limit
        if metric_name is not None:
            self.metric_name = metric_name
        if namespace is not None:
            self.namespace = namespace
        if order is not None:
            self.order = order
        if start is not None:
            self.start = start

    @property
    def dim_0(self):
        """Gets the dim_0 of this ListMetricsRequest.

        指标的维度，目前最大支持3个维度，从0开始；维度格式为dim.{i}=key,value，最大值为256。 例如：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d；各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The dim_0 of this ListMetricsRequest.
        :rtype: str
        """
        return self._dim_0

    @dim_0.setter
    def dim_0(self, dim_0):
        """Sets the dim_0 of this ListMetricsRequest.

        指标的维度，目前最大支持3个维度，从0开始；维度格式为dim.{i}=key,value，最大值为256。 例如：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d；各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param dim_0: The dim_0 of this ListMetricsRequest.
        :type dim_0: str
        """
        self._dim_0 = dim_0

    @property
    def dim_1(self):
        """Gets the dim_1 of this ListMetricsRequest.

        指标的维度，目前最大支持3个维度，从0开始；维度格式为dim.{i}=key,value，最大值为256。 例如：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d；各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The dim_1 of this ListMetricsRequest.
        :rtype: str
        """
        return self._dim_1

    @dim_1.setter
    def dim_1(self, dim_1):
        """Sets the dim_1 of this ListMetricsRequest.

        指标的维度，目前最大支持3个维度，从0开始；维度格式为dim.{i}=key,value，最大值为256。 例如：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d；各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param dim_1: The dim_1 of this ListMetricsRequest.
        :type dim_1: str
        """
        self._dim_1 = dim_1

    @property
    def dim_2(self):
        """Gets the dim_2 of this ListMetricsRequest.

        指标的维度，目前最大支持3个维度，从0开始；维度格式为dim.{i}=key,value，最大值为256。 例如：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d；各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The dim_2 of this ListMetricsRequest.
        :rtype: str
        """
        return self._dim_2

    @dim_2.setter
    def dim_2(self, dim_2):
        """Sets the dim_2 of this ListMetricsRequest.

        指标的维度，目前最大支持3个维度，从0开始；维度格式为dim.{i}=key,value，最大值为256。 例如：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d；各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param dim_2: The dim_2 of this ListMetricsRequest.
        :type dim_2: str
        """
        self._dim_2 = dim_2

    @property
    def limit(self):
        """Gets the limit of this ListMetricsRequest.

        取值范围(0,1000]，默认值为1000。  用于限制结果数据条数。

        :return: The limit of this ListMetricsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListMetricsRequest.

        取值范围(0,1000]，默认值为1000。  用于限制结果数据条数。

        :param limit: The limit of this ListMetricsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def metric_name(self):
        """Gets the metric_name of this ListMetricsRequest.

        指标名称，例如弹性云服务器监控指标中的cpu_util；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The metric_name of this ListMetricsRequest.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this ListMetricsRequest.

        指标名称，例如弹性云服务器监控指标中的cpu_util；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param metric_name: The metric_name of this ListMetricsRequest.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def namespace(self):
        """Gets the namespace of this ListMetricsRequest.

        指标命名空间，格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，总长度最短为3，最大为32；各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The namespace of this ListMetricsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListMetricsRequest.

        指标命名空间，格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，总长度最短为3，最大为32；各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param namespace: The namespace of this ListMetricsRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def order(self):
        """Gets the order of this ListMetricsRequest.

        用于标识结果排序方法。  取值说明，默认为desc：  asc，升序 desc，降序

        :return: The order of this ListMetricsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListMetricsRequest.

        用于标识结果排序方法。  取值说明，默认为desc：  asc，升序 desc，降序

        :param order: The order of this ListMetricsRequest.
        :type order: str
        """
        self._order = order

    @property
    def start(self):
        """Gets the start of this ListMetricsRequest.

        分页起始值，格式为：namespace.metric_name.key:value 例如：start=SYS.ECS.cpu_util.instance_id:d9112af5-6913-4f3b-bd0a-3f96711e004d

        :return: The start of this ListMetricsRequest.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ListMetricsRequest.

        分页起始值，格式为：namespace.metric_name.key:value 例如：start=SYS.ECS.cpu_util.instance_id:d9112af5-6913-4f3b-bd0a-3f96711e004d

        :param start: The start of this ListMetricsRequest.
        :type start: str
        """
        self._start = start

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
        if not isinstance(other, ListMetricsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
