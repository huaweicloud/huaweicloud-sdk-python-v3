# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterLogConfigLogConfigs:

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
        'enable': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'enable': 'enable'
    }

    def __init__(self, name=None, enable=None):
        """ClusterLogConfigLogConfigs

        The model defined in huaweicloud sdk

        :param name: 日志类型
        :type name: str
        :param enable: 是否采集
        :type enable: bool
        """
        
        

        self._name = None
        self._enable = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if enable is not None:
            self.enable = enable

    @property
    def name(self):
        """Gets the name of this ClusterLogConfigLogConfigs.

        日志类型

        :return: The name of this ClusterLogConfigLogConfigs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterLogConfigLogConfigs.

        日志类型

        :param name: The name of this ClusterLogConfigLogConfigs.
        :type name: str
        """
        self._name = name

    @property
    def enable(self):
        """Gets the enable of this ClusterLogConfigLogConfigs.

        是否采集

        :return: The enable of this ClusterLogConfigLogConfigs.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this ClusterLogConfigLogConfigs.

        是否采集

        :param enable: The enable of this ClusterLogConfigLogConfigs.
        :type enable: bool
        """
        self._enable = enable

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
        if not isinstance(other, ClusterLogConfigLogConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
