# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrationRabbitQueueMetadata:

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
        'durable': 'bool'
    }

    attribute_map = {
        'vhost': 'vhost',
        'name': 'name',
        'durable': 'durable'
    }

    def __init__(self, vhost=None, name=None, durable=None):
        r"""MigrationRabbitQueueMetadata

        The model defined in huaweicloud sdk

        :param vhost: vhost名称。
        :type vhost: str
        :param name: 队列名称。
        :type name: str
        :param durable: 是否持久化。
        :type durable: bool
        """
        
        

        self._vhost = None
        self._name = None
        self._durable = None
        self.discriminator = None

        if vhost is not None:
            self.vhost = vhost
        if name is not None:
            self.name = name
        if durable is not None:
            self.durable = durable

    @property
    def vhost(self):
        r"""Gets the vhost of this MigrationRabbitQueueMetadata.

        vhost名称。

        :return: The vhost of this MigrationRabbitQueueMetadata.
        :rtype: str
        """
        return self._vhost

    @vhost.setter
    def vhost(self, vhost):
        r"""Sets the vhost of this MigrationRabbitQueueMetadata.

        vhost名称。

        :param vhost: The vhost of this MigrationRabbitQueueMetadata.
        :type vhost: str
        """
        self._vhost = vhost

    @property
    def name(self):
        r"""Gets the name of this MigrationRabbitQueueMetadata.

        队列名称。

        :return: The name of this MigrationRabbitQueueMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MigrationRabbitQueueMetadata.

        队列名称。

        :param name: The name of this MigrationRabbitQueueMetadata.
        :type name: str
        """
        self._name = name

    @property
    def durable(self):
        r"""Gets the durable of this MigrationRabbitQueueMetadata.

        是否持久化。

        :return: The durable of this MigrationRabbitQueueMetadata.
        :rtype: bool
        """
        return self._durable

    @durable.setter
    def durable(self, durable):
        r"""Sets the durable of this MigrationRabbitQueueMetadata.

        是否持久化。

        :param durable: The durable of this MigrationRabbitQueueMetadata.
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
        if not isinstance(other, MigrationRabbitQueueMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
