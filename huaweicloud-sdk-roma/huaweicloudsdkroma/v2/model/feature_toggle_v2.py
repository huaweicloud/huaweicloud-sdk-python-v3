# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FeatureToggleV2:

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
        'enable': 'bool',
        'config': 'str'
    }

    attribute_map = {
        'name': 'name',
        'enable': 'enable',
        'config': 'config'
    }

    def __init__(self, name=None, enable=None, config=None):
        """FeatureToggleV2

        The model defined in huaweicloud sdk

        :param name: 特性名称
        :type name: str
        :param enable: 是否开启特性
        :type enable: bool
        :param config: 特性参数配置
        :type config: str
        """
        
        

        self._name = None
        self._enable = None
        self._config = None
        self.discriminator = None

        self.name = name
        self.enable = enable
        if config is not None:
            self.config = config

    @property
    def name(self):
        """Gets the name of this FeatureToggleV2.

        特性名称

        :return: The name of this FeatureToggleV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeatureToggleV2.

        特性名称

        :param name: The name of this FeatureToggleV2.
        :type name: str
        """
        self._name = name

    @property
    def enable(self):
        """Gets the enable of this FeatureToggleV2.

        是否开启特性

        :return: The enable of this FeatureToggleV2.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this FeatureToggleV2.

        是否开启特性

        :param enable: The enable of this FeatureToggleV2.
        :type enable: bool
        """
        self._enable = enable

    @property
    def config(self):
        """Gets the config of this FeatureToggleV2.

        特性参数配置

        :return: The config of this FeatureToggleV2.
        :rtype: str
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this FeatureToggleV2.

        特性参数配置

        :param config: The config of this FeatureToggleV2.
        :type config: str
        """
        self._config = config

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
        if not isinstance(other, FeatureToggleV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
