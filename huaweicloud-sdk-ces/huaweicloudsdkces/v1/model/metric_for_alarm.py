# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricForAlarm:

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
        'dimensions': 'list[MetricsDimension]',
        'resource_group_id': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'metric_name': 'metric_name',
        'dimensions': 'dimensions',
        'resource_group_id': 'resource_group_id'
    }

    def __init__(self, namespace=None, metric_name=None, dimensions=None, resource_group_id=None):
        r"""MetricForAlarm

        The model defined in huaweicloud sdk

        :param namespace: 服务指标命名空间，格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符总长度最短为3，最大为32。说明： 当alarm_type为（EVENT.SYS| EVENT.CUSTOM）时允许为空；如：弹性云服务器的命名空间为SYS.ECS，文档数据库的命名空间为SYS.DDS，各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type namespace: str
        :param metric_name: 资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type metric_name: str
        :param dimensions: 指标维度，目前最大可添加4个维度；如果使用资源分组ID：resource_group_id创建告警规则，dimensions可为空，alarm_type值为RESOURCE_GROUP；如果不使用resource_group_id，则dimensions值必填。
        :type dimensions: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        :param resource_group_id: 创建告警规则时选择的资源分组ID；如果根据资源分组创建告警规则，则resource_group_id不能为空，dimensions中至少指定一个维度信息，name不能为空，且alarm_type值为RESOURCE_GROUP；如：rg1603786526428bWbVmk4rP。
        :type resource_group_id: str
        """
        
        

        self._namespace = None
        self._metric_name = None
        self._dimensions = None
        self._resource_group_id = None
        self.discriminator = None

        self.namespace = namespace
        self.metric_name = metric_name
        if dimensions is not None:
            self.dimensions = dimensions
        if resource_group_id is not None:
            self.resource_group_id = resource_group_id

    @property
    def namespace(self):
        r"""Gets the namespace of this MetricForAlarm.

        服务指标命名空间，格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符总长度最短为3，最大为32。说明： 当alarm_type为（EVENT.SYS| EVENT.CUSTOM）时允许为空；如：弹性云服务器的命名空间为SYS.ECS，文档数据库的命名空间为SYS.DDS，各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The namespace of this MetricForAlarm.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this MetricForAlarm.

        服务指标命名空间，格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符总长度最短为3，最大为32。说明： 当alarm_type为（EVENT.SYS| EVENT.CUSTOM）时允许为空；如：弹性云服务器的命名空间为SYS.ECS，文档数据库的命名空间为SYS.DDS，各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param namespace: The namespace of this MetricForAlarm.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def metric_name(self):
        r"""Gets the metric_name of this MetricForAlarm.

        资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The metric_name of this MetricForAlarm.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this MetricForAlarm.

        资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param metric_name: The metric_name of this MetricForAlarm.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def dimensions(self):
        r"""Gets the dimensions of this MetricForAlarm.

        指标维度，目前最大可添加4个维度；如果使用资源分组ID：resource_group_id创建告警规则，dimensions可为空，alarm_type值为RESOURCE_GROUP；如果不使用resource_group_id，则dimensions值必填。

        :return: The dimensions of this MetricForAlarm.
        :rtype: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this MetricForAlarm.

        指标维度，目前最大可添加4个维度；如果使用资源分组ID：resource_group_id创建告警规则，dimensions可为空，alarm_type值为RESOURCE_GROUP；如果不使用resource_group_id，则dimensions值必填。

        :param dimensions: The dimensions of this MetricForAlarm.
        :type dimensions: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        """
        self._dimensions = dimensions

    @property
    def resource_group_id(self):
        r"""Gets the resource_group_id of this MetricForAlarm.

        创建告警规则时选择的资源分组ID；如果根据资源分组创建告警规则，则resource_group_id不能为空，dimensions中至少指定一个维度信息，name不能为空，且alarm_type值为RESOURCE_GROUP；如：rg1603786526428bWbVmk4rP。

        :return: The resource_group_id of this MetricForAlarm.
        :rtype: str
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        r"""Sets the resource_group_id of this MetricForAlarm.

        创建告警规则时选择的资源分组ID；如果根据资源分组创建告警规则，则resource_group_id不能为空，dimensions中至少指定一个维度信息，name不能为空，且alarm_type值为RESOURCE_GROUP；如：rg1603786526428bWbVmk4rP。

        :param resource_group_id: The resource_group_id of this MetricForAlarm.
        :type resource_group_id: str
        """
        self._resource_group_id = resource_group_id

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
        if not isinstance(other, MetricForAlarm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
