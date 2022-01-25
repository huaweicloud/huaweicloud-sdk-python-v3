# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Metric:


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
        'dimensions': 'list[Dimension]'
    }

    attribute_map = {
        'namespace': 'namespace',
        'metric_name': 'metric_name',
        'dimensions': 'dimensions'
    }

    def __init__(self, namespace=None, metric_name=None, dimensions=None):
        """Metric - a model defined in huaweicloud sdk"""
        
        

        self._namespace = None
        self._metric_name = None
        self._dimensions = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if metric_name is not None:
            self.metric_name = metric_name
        if dimensions is not None:
            self.dimensions = dimensions

    @property
    def namespace(self):
        """Gets the namespace of this Metric.

        服务指标命名空间，格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符总长度最短为3，最大为32。说明： 当alarm_type为（EVENT.SYS| EVENT.CUSTOM）时允许为空；如：弹性云服务器的命名空间为SYS.ECS，文档数据库的命名空间为SYS.DDS，各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The namespace of this Metric.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this Metric.

        服务指标命名空间，格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符总长度最短为3，最大为32。说明： 当alarm_type为（EVENT.SYS| EVENT.CUSTOM）时允许为空；如：弹性云服务器的命名空间为SYS.ECS，文档数据库的命名空间为SYS.DDS，各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param namespace: The namespace of this Metric.
        :type: str
        """
        self._namespace = namespace

    @property
    def metric_name(self):
        """Gets the metric_name of this Metric.

        资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。 minLength: 1 maxLength: 64

        :return: The metric_name of this Metric.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this Metric.

        资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。 minLength: 1 maxLength: 64

        :param metric_name: The metric_name of this Metric.
        :type: str
        """
        self._metric_name = metric_name

    @property
    def dimensions(self):
        """Gets the dimensions of this Metric.

        指标维度，目前最大可添加4个维度。

        :return: The dimensions of this Metric.
        :rtype: list[Dimension]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this Metric.

        指标维度，目前最大可添加4个维度。

        :param dimensions: The dimensions of this Metric.
        :type: list[Dimension]
        """
        self._dimensions = dimensions

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
        if not isinstance(other, Metric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
