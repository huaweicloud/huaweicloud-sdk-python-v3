# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrationRabbitExchangeMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vhost': 'str',
        'name': 'str',
        'type': 'str',
        'durable': 'bool'
    }

    attribute_map = {
        'vhost': 'vhost',
        'name': 'name',
        'type': 'type',
        'durable': 'durable'
    }

    def __init__(self, vhost=None, name=None, type=None, durable=None):
        r"""MigrationRabbitExchangeMetadata

        The model defined in huaweicloud sdk

        :param vhost: vhost名称。
        :type vhost: str
        :param name: 交换机名称。
        :type name: str
        :param type: 交换机类型。
        :type type: str
        :param durable: 是否持久化。
        :type durable: bool
        """
        
        

        self._vhost = None
        self._name = None
        self._type = None
        self._durable = None
        self.discriminator = None

        if vhost is not None:
            self.vhost = vhost
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if durable is not None:
            self.durable = durable

    @property
    def vhost(self):
        r"""Gets the vhost of this MigrationRabbitExchangeMetadata.

        vhost名称。

        :return: The vhost of this MigrationRabbitExchangeMetadata.
        :rtype: str
        """
        return self._vhost

    @vhost.setter
    def vhost(self, vhost):
        r"""Sets the vhost of this MigrationRabbitExchangeMetadata.

        vhost名称。

        :param vhost: The vhost of this MigrationRabbitExchangeMetadata.
        :type vhost: str
        """
        self._vhost = vhost

    @property
    def name(self):
        r"""Gets the name of this MigrationRabbitExchangeMetadata.

        交换机名称。

        :return: The name of this MigrationRabbitExchangeMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MigrationRabbitExchangeMetadata.

        交换机名称。

        :param name: The name of this MigrationRabbitExchangeMetadata.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this MigrationRabbitExchangeMetadata.

        交换机类型。

        :return: The type of this MigrationRabbitExchangeMetadata.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this MigrationRabbitExchangeMetadata.

        交换机类型。

        :param type: The type of this MigrationRabbitExchangeMetadata.
        :type type: str
        """
        self._type = type

    @property
    def durable(self):
        r"""Gets the durable of this MigrationRabbitExchangeMetadata.

        是否持久化。

        :return: The durable of this MigrationRabbitExchangeMetadata.
        :rtype: bool
        """
        return self._durable

    @durable.setter
    def durable(self, durable):
        r"""Sets the durable of this MigrationRabbitExchangeMetadata.

        是否持久化。

        :param durable: The durable of this MigrationRabbitExchangeMetadata.
        :type durable: bool
        """
        self._durable = durable

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
        if not isinstance(other, MigrationRabbitExchangeMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
