# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_pool_id': 'str',
        'resource_name': 'str',
        'metric': 'list[Metric]'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_pool_id': 'resource_pool_id',
        'resource_name': 'resource_name',
        'metric': 'metric'
    }

    def __init__(self, resource_id=None, resource_pool_id=None, resource_name=None, metric=None):
        r"""DesktopMetric

        The model defined in huaweicloud sdk

        :param resource_id: 桌面ID
        :type resource_id: str
        :param resource_pool_id: 桌面池ID(仅桌面池中的桌面存在该字段)
        :type resource_pool_id: str
        :param resource_name: 桌面名称
        :type resource_name: str
        :param metric: 统计信息 * &#x60;desktop_usage&#x60; -  桌面使用时长(单位:秒) * &#x60;desktop_idle_duration&#x60; -  桌面空闲时长(单位:秒)
        :type metric: list[:class:`huaweicloudsdkworkspace.v2.Metric`]
        """
        
        

        self._resource_id = None
        self._resource_pool_id = None
        self._resource_name = None
        self._metric = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resource_pool_id is not None:
            self.resource_pool_id = resource_pool_id
        if resource_name is not None:
            self.resource_name = resource_name
        if metric is not None:
            self.metric = metric

    @property
    def resource_id(self):
        r"""Gets the resource_id of this DesktopMetric.

        桌面ID

        :return: The resource_id of this DesktopMetric.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this DesktopMetric.

        桌面ID

        :param resource_id: The resource_id of this DesktopMetric.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_pool_id(self):
        r"""Gets the resource_pool_id of this DesktopMetric.

        桌面池ID(仅桌面池中的桌面存在该字段)

        :return: The resource_pool_id of this DesktopMetric.
        :rtype: str
        """
        return self._resource_pool_id

    @resource_pool_id.setter
    def resource_pool_id(self, resource_pool_id):
        r"""Sets the resource_pool_id of this DesktopMetric.

        桌面池ID(仅桌面池中的桌面存在该字段)

        :param resource_pool_id: The resource_pool_id of this DesktopMetric.
        :type resource_pool_id: str
        """
        self._resource_pool_id = resource_pool_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this DesktopMetric.

        桌面名称

        :return: The resource_name of this DesktopMetric.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this DesktopMetric.

        桌面名称

        :param resource_name: The resource_name of this DesktopMetric.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def metric(self):
        r"""Gets the metric of this DesktopMetric.

        统计信息 * `desktop_usage` -  桌面使用时长(单位:秒) * `desktop_idle_duration` -  桌面空闲时长(单位:秒)

        :return: The metric of this DesktopMetric.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Metric`]
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this DesktopMetric.

        统计信息 * `desktop_usage` -  桌面使用时长(单位:秒) * `desktop_idle_duration` -  桌面空闲时长(单位:秒)

        :param metric: The metric of this DesktopMetric.
        :type metric: list[:class:`huaweicloudsdkworkspace.v2.Metric`]
        """
        self._metric = metric

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
        if not isinstance(other, DesktopMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
