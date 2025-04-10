# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrationRabbitBindingMetadata:

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
        'source': 'str',
        'destination': 'str',
        'destination_type': 'str',
        'routing_key': 'str'
    }

    attribute_map = {
        'vhost': 'vhost',
        'source': 'source',
        'destination': 'destination',
        'destination_type': 'destination_type',
        'routing_key': 'routing_key'
    }

    def __init__(self, vhost=None, source=None, destination=None, destination_type=None, routing_key=None):
        r"""MigrationRabbitBindingMetadata

        The model defined in huaweicloud sdk

        :param vhost: vhost名称。
        :type vhost: str
        :param source: 消息的来源。
        :type source: str
        :param destination: 消息的目标。
        :type destination: str
        :param destination_type: 目标的类型。
        :type destination_type: str
        :param routing_key: 路由键。
        :type routing_key: str
        """
        
        

        self._vhost = None
        self._source = None
        self._destination = None
        self._destination_type = None
        self._routing_key = None
        self.discriminator = None

        if vhost is not None:
            self.vhost = vhost
        if source is not None:
            self.source = source
        if destination is not None:
            self.destination = destination
        if destination_type is not None:
            self.destination_type = destination_type
        if routing_key is not None:
            self.routing_key = routing_key

    @property
    def vhost(self):
        r"""Gets the vhost of this MigrationRabbitBindingMetadata.

        vhost名称。

        :return: The vhost of this MigrationRabbitBindingMetadata.
        :rtype: str
        """
        return self._vhost

    @vhost.setter
    def vhost(self, vhost):
        r"""Sets the vhost of this MigrationRabbitBindingMetadata.

        vhost名称。

        :param vhost: The vhost of this MigrationRabbitBindingMetadata.
        :type vhost: str
        """
        self._vhost = vhost

    @property
    def source(self):
        r"""Gets the source of this MigrationRabbitBindingMetadata.

        消息的来源。

        :return: The source of this MigrationRabbitBindingMetadata.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this MigrationRabbitBindingMetadata.

        消息的来源。

        :param source: The source of this MigrationRabbitBindingMetadata.
        :type source: str
        """
        self._source = source

    @property
    def destination(self):
        r"""Gets the destination of this MigrationRabbitBindingMetadata.

        消息的目标。

        :return: The destination of this MigrationRabbitBindingMetadata.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        r"""Sets the destination of this MigrationRabbitBindingMetadata.

        消息的目标。

        :param destination: The destination of this MigrationRabbitBindingMetadata.
        :type destination: str
        """
        self._destination = destination

    @property
    def destination_type(self):
        r"""Gets the destination_type of this MigrationRabbitBindingMetadata.

        目标的类型。

        :return: The destination_type of this MigrationRabbitBindingMetadata.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        r"""Sets the destination_type of this MigrationRabbitBindingMetadata.

        目标的类型。

        :param destination_type: The destination_type of this MigrationRabbitBindingMetadata.
        :type destination_type: str
        """
        self._destination_type = destination_type

    @property
    def routing_key(self):
        r"""Gets the routing_key of this MigrationRabbitBindingMetadata.

        路由键。

        :return: The routing_key of this MigrationRabbitBindingMetadata.
        :rtype: str
        """
        return self._routing_key

    @routing_key.setter
    def routing_key(self, routing_key):
        r"""Sets the routing_key of this MigrationRabbitBindingMetadata.

        路由键。

        :param routing_key: The routing_key of this MigrationRabbitBindingMetadata.
        :type routing_key: str
        """
        self._routing_key = routing_key

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
        if not isinstance(other, MigrationRabbitBindingMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
