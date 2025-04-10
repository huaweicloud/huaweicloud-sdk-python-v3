# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SaveRedisDisabledCommandsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disabled_type': 'str',
        'commands': 'list[str]',
        'keys': 'list[RedisDisabledCommandsDetail]'
    }

    attribute_map = {
        'disabled_type': 'disabled_type',
        'commands': 'commands',
        'keys': 'keys'
    }

    def __init__(self, disabled_type=None, commands=None, keys=None):
        r"""SaveRedisDisabledCommandsRequestBody

        The model defined in huaweicloud sdk

        :param disabled_type: 禁用类型。
        :type disabled_type: str
        :param commands: disabled_type为command时传入该参数。
        :type commands: list[str]
        :param keys: disabled_type为key时传入该参数，最多20个。
        :type keys: list[:class:`huaweicloudsdkgaussdbfornosql.v3.RedisDisabledCommandsDetail`]
        """
        
        

        self._disabled_type = None
        self._commands = None
        self._keys = None
        self.discriminator = None

        self.disabled_type = disabled_type
        if commands is not None:
            self.commands = commands
        if keys is not None:
            self.keys = keys

    @property
    def disabled_type(self):
        r"""Gets the disabled_type of this SaveRedisDisabledCommandsRequestBody.

        禁用类型。

        :return: The disabled_type of this SaveRedisDisabledCommandsRequestBody.
        :rtype: str
        """
        return self._disabled_type

    @disabled_type.setter
    def disabled_type(self, disabled_type):
        r"""Sets the disabled_type of this SaveRedisDisabledCommandsRequestBody.

        禁用类型。

        :param disabled_type: The disabled_type of this SaveRedisDisabledCommandsRequestBody.
        :type disabled_type: str
        """
        self._disabled_type = disabled_type

    @property
    def commands(self):
        r"""Gets the commands of this SaveRedisDisabledCommandsRequestBody.

        disabled_type为command时传入该参数。

        :return: The commands of this SaveRedisDisabledCommandsRequestBody.
        :rtype: list[str]
        """
        return self._commands

    @commands.setter
    def commands(self, commands):
        r"""Sets the commands of this SaveRedisDisabledCommandsRequestBody.

        disabled_type为command时传入该参数。

        :param commands: The commands of this SaveRedisDisabledCommandsRequestBody.
        :type commands: list[str]
        """
        self._commands = commands

    @property
    def keys(self):
        r"""Gets the keys of this SaveRedisDisabledCommandsRequestBody.

        disabled_type为key时传入该参数，最多20个。

        :return: The keys of this SaveRedisDisabledCommandsRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.RedisDisabledCommandsDetail`]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        r"""Sets the keys of this SaveRedisDisabledCommandsRequestBody.

        disabled_type为key时传入该参数，最多20个。

        :param keys: The keys of this SaveRedisDisabledCommandsRequestBody.
        :type keys: list[:class:`huaweicloudsdkgaussdbfornosql.v3.RedisDisabledCommandsDetail`]
        """
        self._keys = keys

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
        if not isinstance(other, SaveRedisDisabledCommandsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
