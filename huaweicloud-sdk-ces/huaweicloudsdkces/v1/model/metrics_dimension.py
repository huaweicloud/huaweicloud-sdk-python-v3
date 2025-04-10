# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricsDimension:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, name=None, value=None):
        r"""MetricsDimension

        The model defined in huaweicloud sdk

        :param name: 资源维度，如：弹性云服务器，则维度为instance_id；目前最大支持4个维度，各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type name: str
        :param value: 资源维度值，为资源的实例ID，如：4270ff17-aba3-4138-89fa-820594c39755。
        :type value: str
        """
        
        

        self._name = None
        self._value = None
        self.discriminator = None

        self.name = name
        self.value = value

    @property
    def name(self):
        r"""Gets the name of this MetricsDimension.

        资源维度，如：弹性云服务器，则维度为instance_id；目前最大支持4个维度，各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The name of this MetricsDimension.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MetricsDimension.

        资源维度，如：弹性云服务器，则维度为instance_id；目前最大支持4个维度，各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param name: The name of this MetricsDimension.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this MetricsDimension.

        资源维度值，为资源的实例ID，如：4270ff17-aba3-4138-89fa-820594c39755。

        :return: The value of this MetricsDimension.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this MetricsDimension.

        资源维度值，为资源的实例ID，如：4270ff17-aba3-4138-89fa-820594c39755。

        :param value: The value of this MetricsDimension.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, MetricsDimension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
