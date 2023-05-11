# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RabbitMQExtendProductPropertiesEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_broker': 'str',
        'max_storage_per_node': 'str',
        'min_broker': 'str',
        'min_storage_per_node': 'str',
        'max_connection_per_broker': 'str',
        'step_length': 'str',
        'product_alias': 'str',
        'max_queue_per_broker': 'str'
    }

    attribute_map = {
        'max_broker': 'max_broker',
        'max_storage_per_node': 'max_storage_per_node',
        'min_broker': 'min_broker',
        'min_storage_per_node': 'min_storage_per_node',
        'max_connection_per_broker': 'max_connection_per_broker',
        'step_length': 'step_length',
        'product_alias': 'product_alias',
        'max_queue_per_broker': 'max_queue_per_broker'
    }

    def __init__(self, max_broker=None, max_storage_per_node=None, min_broker=None, min_storage_per_node=None, max_connection_per_broker=None, step_length=None, product_alias=None, max_queue_per_broker=None):
        """RabbitMQExtendProductPropertiesEntity

        The model defined in huaweicloud sdk

        :param max_broker: Broker的最大个数。
        :type max_broker: str
        :param max_storage_per_node: 每个节点的最大存储。单位为GB。
        :type max_storage_per_node: str
        :param min_broker: Broker的最小个数。
        :type min_broker: str
        :param min_storage_per_node: 每个节点的最小存储。单位为GB。
        :type min_storage_per_node: str
        :param max_connection_per_broker: 最大连接数
        :type max_connection_per_broker: str
        :param step_length: 步长
        :type step_length: str
        :param product_alias: product_id的别名。
        :type product_alias: str
        :param max_queue_per_broker: 最大队列
        :type max_queue_per_broker: str
        """
        
        

        self._max_broker = None
        self._max_storage_per_node = None
        self._min_broker = None
        self._min_storage_per_node = None
        self._max_connection_per_broker = None
        self._step_length = None
        self._product_alias = None
        self._max_queue_per_broker = None
        self.discriminator = None

        if max_broker is not None:
            self.max_broker = max_broker
        if max_storage_per_node is not None:
            self.max_storage_per_node = max_storage_per_node
        if min_broker is not None:
            self.min_broker = min_broker
        if min_storage_per_node is not None:
            self.min_storage_per_node = min_storage_per_node
        if max_connection_per_broker is not None:
            self.max_connection_per_broker = max_connection_per_broker
        if step_length is not None:
            self.step_length = step_length
        if product_alias is not None:
            self.product_alias = product_alias
        if max_queue_per_broker is not None:
            self.max_queue_per_broker = max_queue_per_broker

    @property
    def max_broker(self):
        """Gets the max_broker of this RabbitMQExtendProductPropertiesEntity.

        Broker的最大个数。

        :return: The max_broker of this RabbitMQExtendProductPropertiesEntity.
        :rtype: str
        """
        return self._max_broker

    @max_broker.setter
    def max_broker(self, max_broker):
        """Sets the max_broker of this RabbitMQExtendProductPropertiesEntity.

        Broker的最大个数。

        :param max_broker: The max_broker of this RabbitMQExtendProductPropertiesEntity.
        :type max_broker: str
        """
        self._max_broker = max_broker

    @property
    def max_storage_per_node(self):
        """Gets the max_storage_per_node of this RabbitMQExtendProductPropertiesEntity.

        每个节点的最大存储。单位为GB。

        :return: The max_storage_per_node of this RabbitMQExtendProductPropertiesEntity.
        :rtype: str
        """
        return self._max_storage_per_node

    @max_storage_per_node.setter
    def max_storage_per_node(self, max_storage_per_node):
        """Sets the max_storage_per_node of this RabbitMQExtendProductPropertiesEntity.

        每个节点的最大存储。单位为GB。

        :param max_storage_per_node: The max_storage_per_node of this RabbitMQExtendProductPropertiesEntity.
        :type max_storage_per_node: str
        """
        self._max_storage_per_node = max_storage_per_node

    @property
    def min_broker(self):
        """Gets the min_broker of this RabbitMQExtendProductPropertiesEntity.

        Broker的最小个数。

        :return: The min_broker of this RabbitMQExtendProductPropertiesEntity.
        :rtype: str
        """
        return self._min_broker

    @min_broker.setter
    def min_broker(self, min_broker):
        """Sets the min_broker of this RabbitMQExtendProductPropertiesEntity.

        Broker的最小个数。

        :param min_broker: The min_broker of this RabbitMQExtendProductPropertiesEntity.
        :type min_broker: str
        """
        self._min_broker = min_broker

    @property
    def min_storage_per_node(self):
        """Gets the min_storage_per_node of this RabbitMQExtendProductPropertiesEntity.

        每个节点的最小存储。单位为GB。

        :return: The min_storage_per_node of this RabbitMQExtendProductPropertiesEntity.
        :rtype: str
        """
        return self._min_storage_per_node

    @min_storage_per_node.setter
    def min_storage_per_node(self, min_storage_per_node):
        """Sets the min_storage_per_node of this RabbitMQExtendProductPropertiesEntity.

        每个节点的最小存储。单位为GB。

        :param min_storage_per_node: The min_storage_per_node of this RabbitMQExtendProductPropertiesEntity.
        :type min_storage_per_node: str
        """
        self._min_storage_per_node = min_storage_per_node

    @property
    def max_connection_per_broker(self):
        """Gets the max_connection_per_broker of this RabbitMQExtendProductPropertiesEntity.

        最大连接数

        :return: The max_connection_per_broker of this RabbitMQExtendProductPropertiesEntity.
        :rtype: str
        """
        return self._max_connection_per_broker

    @max_connection_per_broker.setter
    def max_connection_per_broker(self, max_connection_per_broker):
        """Sets the max_connection_per_broker of this RabbitMQExtendProductPropertiesEntity.

        最大连接数

        :param max_connection_per_broker: The max_connection_per_broker of this RabbitMQExtendProductPropertiesEntity.
        :type max_connection_per_broker: str
        """
        self._max_connection_per_broker = max_connection_per_broker

    @property
    def step_length(self):
        """Gets the step_length of this RabbitMQExtendProductPropertiesEntity.

        步长

        :return: The step_length of this RabbitMQExtendProductPropertiesEntity.
        :rtype: str
        """
        return self._step_length

    @step_length.setter
    def step_length(self, step_length):
        """Sets the step_length of this RabbitMQExtendProductPropertiesEntity.

        步长

        :param step_length: The step_length of this RabbitMQExtendProductPropertiesEntity.
        :type step_length: str
        """
        self._step_length = step_length

    @property
    def product_alias(self):
        """Gets the product_alias of this RabbitMQExtendProductPropertiesEntity.

        product_id的别名。

        :return: The product_alias of this RabbitMQExtendProductPropertiesEntity.
        :rtype: str
        """
        return self._product_alias

    @product_alias.setter
    def product_alias(self, product_alias):
        """Sets the product_alias of this RabbitMQExtendProductPropertiesEntity.

        product_id的别名。

        :param product_alias: The product_alias of this RabbitMQExtendProductPropertiesEntity.
        :type product_alias: str
        """
        self._product_alias = product_alias

    @property
    def max_queue_per_broker(self):
        """Gets the max_queue_per_broker of this RabbitMQExtendProductPropertiesEntity.

        最大队列

        :return: The max_queue_per_broker of this RabbitMQExtendProductPropertiesEntity.
        :rtype: str
        """
        return self._max_queue_per_broker

    @max_queue_per_broker.setter
    def max_queue_per_broker(self, max_queue_per_broker):
        """Sets the max_queue_per_broker of this RabbitMQExtendProductPropertiesEntity.

        最大队列

        :param max_queue_per_broker: The max_queue_per_broker of this RabbitMQExtendProductPropertiesEntity.
        :type max_queue_per_broker: str
        """
        self._max_queue_per_broker = max_queue_per_broker

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
        if not isinstance(other, RabbitMQExtendProductPropertiesEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
