# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedisConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'param_value': 'str',
        'param_name': 'str',
        'param_id': 'str'
    }

    attribute_map = {
        'param_value': 'param_value',
        'param_name': 'param_name',
        'param_id': 'param_id'
    }

    def __init__(self, param_value=None, param_name=None, param_id=None):
        """RedisConfig

        The model defined in huaweicloud sdk

        :param param_value: 实例配置项的值。
        :type param_value: str
        :param param_name: 实例配置项名。
        :type param_name: str
        :param param_id: 实例配置项ID。
        :type param_id: str
        """
        
        

        self._param_value = None
        self._param_name = None
        self._param_id = None
        self.discriminator = None

        self.param_value = param_value
        self.param_name = param_name
        self.param_id = param_id

    @property
    def param_value(self):
        """Gets the param_value of this RedisConfig.

        实例配置项的值。

        :return: The param_value of this RedisConfig.
        :rtype: str
        """
        return self._param_value

    @param_value.setter
    def param_value(self, param_value):
        """Sets the param_value of this RedisConfig.

        实例配置项的值。

        :param param_value: The param_value of this RedisConfig.
        :type param_value: str
        """
        self._param_value = param_value

    @property
    def param_name(self):
        """Gets the param_name of this RedisConfig.

        实例配置项名。

        :return: The param_name of this RedisConfig.
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        """Sets the param_name of this RedisConfig.

        实例配置项名。

        :param param_name: The param_name of this RedisConfig.
        :type param_name: str
        """
        self._param_name = param_name

    @property
    def param_id(self):
        """Gets the param_id of this RedisConfig.

        实例配置项ID。

        :return: The param_id of this RedisConfig.
        :rtype: str
        """
        return self._param_id

    @param_id.setter
    def param_id(self, param_id):
        """Sets the param_id of this RedisConfig.

        实例配置项ID。

        :param param_id: The param_id of this RedisConfig.
        :type param_id: str
        """
        self._param_id = param_id

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
        if not isinstance(other, RedisConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
