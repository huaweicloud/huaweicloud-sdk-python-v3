# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dimension_name': 'str',
        'metric_name': 'str'
    }

    attribute_map = {
        'dimension_name': 'dimension_name',
        'metric_name': 'metric_name'
    }

    def __init__(self, dimension_name=None, metric_name=None):
        r"""ProductMetric

        The model defined in huaweicloud sdk

        :param dimension_name: 按云产品维度屏蔽时的指标维度信息，有多个时用\&quot;,\&quot;连接
        :type dimension_name: str
        :param metric_name: 资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。
        :type metric_name: str
        """
        
        

        self._dimension_name = None
        self._metric_name = None
        self.discriminator = None

        self.dimension_name = dimension_name
        self.metric_name = metric_name

    @property
    def dimension_name(self):
        r"""Gets the dimension_name of this ProductMetric.

        按云产品维度屏蔽时的指标维度信息，有多个时用\",\"连接

        :return: The dimension_name of this ProductMetric.
        :rtype: str
        """
        return self._dimension_name

    @dimension_name.setter
    def dimension_name(self, dimension_name):
        r"""Sets the dimension_name of this ProductMetric.

        按云产品维度屏蔽时的指标维度信息，有多个时用\",\"连接

        :param dimension_name: The dimension_name of this ProductMetric.
        :type dimension_name: str
        """
        self._dimension_name = dimension_name

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ProductMetric.

        资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。

        :return: The metric_name of this ProductMetric.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ProductMetric.

        资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。

        :param metric_name: The metric_name of this ProductMetric.
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
        if not isinstance(other, ProductMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
