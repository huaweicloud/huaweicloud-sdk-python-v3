# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRedisDisabledCommandsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'str',
        'disabled_type': 'str',
        'commands': 'list[str]',
        'keys': 'list[RedisDisabledCommandsDetail]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'disabled_type': 'disabled_type',
        'commands': 'commands',
        'keys': 'keys'
    }

    def __init__(self, total_count=None, disabled_type=None, commands=None, keys=None):
        """ShowRedisDisabledCommandsResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数。
        :type total_count: str
        :param disabled_type: 禁用类型。
        :type disabled_type: str
        :param commands: disabled_type为command时展示该参数。
        :type commands: list[str]
        :param keys: disabled_type为key时展示该参数，最多20个。
        :type keys: list[:class:`huaweicloudsdkgaussdbfornosql.v3.RedisDisabledCommandsDetail`]
        """
        
        super(ShowRedisDisabledCommandsResponse, self).__init__()

        self._total_count = None
        self._disabled_type = None
        self._commands = None
        self._keys = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if disabled_type is not None:
            self.disabled_type = disabled_type
        if commands is not None:
            self.commands = commands
        if keys is not None:
            self.keys = keys

    @property
    def total_count(self):
        """Gets the total_count of this ShowRedisDisabledCommandsResponse.

        总数。

        :return: The total_count of this ShowRedisDisabledCommandsResponse.
        :rtype: str
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ShowRedisDisabledCommandsResponse.

        总数。

        :param total_count: The total_count of this ShowRedisDisabledCommandsResponse.
        :type total_count: str
        """
        self._total_count = total_count

    @property
    def disabled_type(self):
        """Gets the disabled_type of this ShowRedisDisabledCommandsResponse.

        禁用类型。

        :return: The disabled_type of this ShowRedisDisabledCommandsResponse.
        :rtype: str
        """
        return self._disabled_type

    @disabled_type.setter
    def disabled_type(self, disabled_type):
        """Sets the disabled_type of this ShowRedisDisabledCommandsResponse.

        禁用类型。

        :param disabled_type: The disabled_type of this ShowRedisDisabledCommandsResponse.
        :type disabled_type: str
        """
        self._disabled_type = disabled_type

    @property
    def commands(self):
        """Gets the commands of this ShowRedisDisabledCommandsResponse.

        disabled_type为command时展示该参数。

        :return: The commands of this ShowRedisDisabledCommandsResponse.
        :rtype: list[str]
        """
        return self._commands

    @commands.setter
    def commands(self, commands):
        """Sets the commands of this ShowRedisDisabledCommandsResponse.

        disabled_type为command时展示该参数。

        :param commands: The commands of this ShowRedisDisabledCommandsResponse.
        :type commands: list[str]
        """
        self._commands = commands

    @property
    def keys(self):
        """Gets the keys of this ShowRedisDisabledCommandsResponse.

        disabled_type为key时展示该参数，最多20个。

        :return: The keys of this ShowRedisDisabledCommandsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.RedisDisabledCommandsDetail`]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this ShowRedisDisabledCommandsResponse.

        disabled_type为key时展示该参数，最多20个。

        :param keys: The keys of this ShowRedisDisabledCommandsResponse.
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
        if not isinstance(other, ShowRedisDisabledCommandsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
