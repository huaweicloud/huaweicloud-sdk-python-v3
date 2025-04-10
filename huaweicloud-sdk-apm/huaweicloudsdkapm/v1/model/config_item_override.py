# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigItemOverride:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'env_tag_id': 'int',
        'env_tag_name': 'str',
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'env_tag_id': 'env_tag_id',
        'env_tag_name': 'env_tag_name',
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, env_tag_id=None, env_tag_name=None, key=None, value=None):
        r"""ConfigItemOverride

        The model defined in huaweicloud sdk

        :param env_tag_id: 环境标签ID
        :type env_tag_id: int
        :param env_tag_name: 环境标签名
        :type env_tag_name: str
        :param key: 键
        :type key: str
        :param value: 值
        :type value: str
        """
        
        

        self._env_tag_id = None
        self._env_tag_name = None
        self._key = None
        self._value = None
        self.discriminator = None

        if env_tag_id is not None:
            self.env_tag_id = env_tag_id
        if env_tag_name is not None:
            self.env_tag_name = env_tag_name
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def env_tag_id(self):
        r"""Gets the env_tag_id of this ConfigItemOverride.

        环境标签ID

        :return: The env_tag_id of this ConfigItemOverride.
        :rtype: int
        """
        return self._env_tag_id

    @env_tag_id.setter
    def env_tag_id(self, env_tag_id):
        r"""Sets the env_tag_id of this ConfigItemOverride.

        环境标签ID

        :param env_tag_id: The env_tag_id of this ConfigItemOverride.
        :type env_tag_id: int
        """
        self._env_tag_id = env_tag_id

    @property
    def env_tag_name(self):
        r"""Gets the env_tag_name of this ConfigItemOverride.

        环境标签名

        :return: The env_tag_name of this ConfigItemOverride.
        :rtype: str
        """
        return self._env_tag_name

    @env_tag_name.setter
    def env_tag_name(self, env_tag_name):
        r"""Sets the env_tag_name of this ConfigItemOverride.

        环境标签名

        :param env_tag_name: The env_tag_name of this ConfigItemOverride.
        :type env_tag_name: str
        """
        self._env_tag_name = env_tag_name

    @property
    def key(self):
        r"""Gets the key of this ConfigItemOverride.

        键

        :return: The key of this ConfigItemOverride.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ConfigItemOverride.

        键

        :param key: The key of this ConfigItemOverride.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this ConfigItemOverride.

        值

        :return: The value of this ConfigItemOverride.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ConfigItemOverride.

        值

        :param value: The value of this ConfigItemOverride.
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
        if not isinstance(other, ConfigItemOverride):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
