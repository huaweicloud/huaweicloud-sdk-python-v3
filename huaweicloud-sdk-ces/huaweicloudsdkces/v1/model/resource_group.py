# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceGroup:

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
        'dimensions': 'list[MetricsDimension]',
        'status': 'str',
        'event_type': 'int'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dimensions': 'dimensions',
        'status': 'status',
        'event_type': 'event_type'
    }

    def __init__(self, namespace=None, dimensions=None, status=None, event_type=None):
        r"""ResourceGroup

        The model defined in huaweicloud sdk

        :param namespace: 资源类型。即命名空间，如弹性云服务器的资源命名空间为：SYS.ECS；各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type namespace: str
        :param dimensions: 一个或者多个资源维度。
        :type dimensions: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        :param status: 资源分组中该资源的当前状态，值可为health、unhealth、no_alarm_rule；health表示健康，unhealth表示不健康，no_alarm_rule表示未设置告警规则。
        :type status: str
        :param event_type: 事件类型，默认为0。
        :type event_type: int
        """
        
        

        self._namespace = None
        self._dimensions = None
        self._status = None
        self._event_type = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if dimensions is not None:
            self.dimensions = dimensions
        if status is not None:
            self.status = status
        if event_type is not None:
            self.event_type = event_type

    @property
    def namespace(self):
        r"""Gets the namespace of this ResourceGroup.

        资源类型。即命名空间，如弹性云服务器的资源命名空间为：SYS.ECS；各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The namespace of this ResourceGroup.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ResourceGroup.

        资源类型。即命名空间，如弹性云服务器的资源命名空间为：SYS.ECS；各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param namespace: The namespace of this ResourceGroup.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimensions(self):
        r"""Gets the dimensions of this ResourceGroup.

        一个或者多个资源维度。

        :return: The dimensions of this ResourceGroup.
        :rtype: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this ResourceGroup.

        一个或者多个资源维度。

        :param dimensions: The dimensions of this ResourceGroup.
        :type dimensions: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        """
        self._dimensions = dimensions

    @property
    def status(self):
        r"""Gets the status of this ResourceGroup.

        资源分组中该资源的当前状态，值可为health、unhealth、no_alarm_rule；health表示健康，unhealth表示不健康，no_alarm_rule表示未设置告警规则。

        :return: The status of this ResourceGroup.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ResourceGroup.

        资源分组中该资源的当前状态，值可为health、unhealth、no_alarm_rule；health表示健康，unhealth表示不健康，no_alarm_rule表示未设置告警规则。

        :param status: The status of this ResourceGroup.
        :type status: str
        """
        self._status = status

    @property
    def event_type(self):
        r"""Gets the event_type of this ResourceGroup.

        事件类型，默认为0。

        :return: The event_type of this ResourceGroup.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ResourceGroup.

        事件类型，默认为0。

        :param event_type: The event_type of this ResourceGroup.
        :type event_type: int
        """
        self._event_type = event_type

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
        if not isinstance(other, ResourceGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
