# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'ConfigurationData',
        'type': 'str'
    }

    attribute_map = {
        'data': 'data',
        'type': 'type'
    }

    def __init__(self, data=None, type=None):
        """ConfigurationItem

        The model defined in huaweicloud sdk

        :param data: 
        :type data: :class:`huaweicloudsdkcae.v1.ConfigurationData`
        :param type: 组件配置类型，当前CAE支持组件配置如下11类。  - rds：云数据库RDS。  - cse：微服务引擎CSE。  - env：环境变量。  - access：访问方式。  - scaling：伸缩策略。  - volume：云存储配置。  - healthCheck：健康检查。  - lifecycle：生命周期管理。  - apm2：性能管理。  - log: 自定义日志路径。  - customMetric: 自定义监控指标。
        :type type: str
        """
        
        

        self._data = None
        self._type = None
        self.discriminator = None

        self.data = data
        self.type = type

    @property
    def data(self):
        """Gets the data of this ConfigurationItem.

        :return: The data of this ConfigurationItem.
        :rtype: :class:`huaweicloudsdkcae.v1.ConfigurationData`
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ConfigurationItem.

        :param data: The data of this ConfigurationItem.
        :type data: :class:`huaweicloudsdkcae.v1.ConfigurationData`
        """
        self._data = data

    @property
    def type(self):
        """Gets the type of this ConfigurationItem.

        组件配置类型，当前CAE支持组件配置如下11类。  - rds：云数据库RDS。  - cse：微服务引擎CSE。  - env：环境变量。  - access：访问方式。  - scaling：伸缩策略。  - volume：云存储配置。  - healthCheck：健康检查。  - lifecycle：生命周期管理。  - apm2：性能管理。  - log: 自定义日志路径。  - customMetric: 自定义监控指标。

        :return: The type of this ConfigurationItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConfigurationItem.

        组件配置类型，当前CAE支持组件配置如下11类。  - rds：云数据库RDS。  - cse：微服务引擎CSE。  - env：环境变量。  - access：访问方式。  - scaling：伸缩策略。  - volume：云存储配置。  - healthCheck：健康检查。  - lifecycle：生命周期管理。  - apm2：性能管理。  - log: 自定义日志路径。  - customMetric: 自定义监控指标。

        :param type: The type of this ConfigurationItem.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ConfigurationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
