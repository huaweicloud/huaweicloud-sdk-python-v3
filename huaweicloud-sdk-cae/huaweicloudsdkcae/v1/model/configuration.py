# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Configuration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'ListComponentConfigurationsResponseData',
        'operated_at': 'datetime',
        'operation_id': 'str',
        'type': 'str',
        'is_activated': 'bool'
    }

    attribute_map = {
        'data': 'data',
        'operated_at': 'operated_at',
        'operation_id': 'operation_id',
        'type': 'type',
        'is_activated': 'is_activated'
    }

    def __init__(self, data=None, operated_at=None, operation_id=None, type=None, is_activated=None):
        """Configuration

        The model defined in huaweicloud sdk

        :param data: 
        :type data: :class:`huaweicloudsdkcae.v1.ListComponentConfigurationsResponseData`
        :param operated_at: 操作时间。
        :type operated_at: datetime
        :param operation_id: 操作ID。
        :type operation_id: str
        :param type: 组件配置类型，当前CAE支持组件配置如下11类。  - rds：云数据库RDS。  - cse：微服务引擎CSE。  - env：环境变量。  - access：访问方式。  - scaling：伸缩策略。  - volume：云存储配置。  - healthCheck：健康检查。  - lifecycle：生命周期管理。  - apm2：性能管理。  - log: 自定义日志路径。  - customMetric: 自定义监控指标。
        :type type: str
        :param is_activated: 配置是否生效。
        :type is_activated: bool
        """
        
        

        self._data = None
        self._operated_at = None
        self._operation_id = None
        self._type = None
        self._is_activated = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if operated_at is not None:
            self.operated_at = operated_at
        if operation_id is not None:
            self.operation_id = operation_id
        if type is not None:
            self.type = type
        if is_activated is not None:
            self.is_activated = is_activated

    @property
    def data(self):
        """Gets the data of this Configuration.

        :return: The data of this Configuration.
        :rtype: :class:`huaweicloudsdkcae.v1.ListComponentConfigurationsResponseData`
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Configuration.

        :param data: The data of this Configuration.
        :type data: :class:`huaweicloudsdkcae.v1.ListComponentConfigurationsResponseData`
        """
        self._data = data

    @property
    def operated_at(self):
        """Gets the operated_at of this Configuration.

        操作时间。

        :return: The operated_at of this Configuration.
        :rtype: datetime
        """
        return self._operated_at

    @operated_at.setter
    def operated_at(self, operated_at):
        """Sets the operated_at of this Configuration.

        操作时间。

        :param operated_at: The operated_at of this Configuration.
        :type operated_at: datetime
        """
        self._operated_at = operated_at

    @property
    def operation_id(self):
        """Gets the operation_id of this Configuration.

        操作ID。

        :return: The operation_id of this Configuration.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        """Sets the operation_id of this Configuration.

        操作ID。

        :param operation_id: The operation_id of this Configuration.
        :type operation_id: str
        """
        self._operation_id = operation_id

    @property
    def type(self):
        """Gets the type of this Configuration.

        组件配置类型，当前CAE支持组件配置如下11类。  - rds：云数据库RDS。  - cse：微服务引擎CSE。  - env：环境变量。  - access：访问方式。  - scaling：伸缩策略。  - volume：云存储配置。  - healthCheck：健康检查。  - lifecycle：生命周期管理。  - apm2：性能管理。  - log: 自定义日志路径。  - customMetric: 自定义监控指标。

        :return: The type of this Configuration.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Configuration.

        组件配置类型，当前CAE支持组件配置如下11类。  - rds：云数据库RDS。  - cse：微服务引擎CSE。  - env：环境变量。  - access：访问方式。  - scaling：伸缩策略。  - volume：云存储配置。  - healthCheck：健康检查。  - lifecycle：生命周期管理。  - apm2：性能管理。  - log: 自定义日志路径。  - customMetric: 自定义监控指标。

        :param type: The type of this Configuration.
        :type type: str
        """
        self._type = type

    @property
    def is_activated(self):
        """Gets the is_activated of this Configuration.

        配置是否生效。

        :return: The is_activated of this Configuration.
        :rtype: bool
        """
        return self._is_activated

    @is_activated.setter
    def is_activated(self, is_activated):
        """Sets the is_activated of this Configuration.

        配置是否生效。

        :param is_activated: The is_activated of this Configuration.
        :type is_activated: bool
        """
        self._is_activated = is_activated

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
        if not isinstance(other, Configuration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
