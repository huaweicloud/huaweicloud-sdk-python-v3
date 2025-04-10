# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RocketMQExtendProductPropertiesEntity:

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
        'max_topic_per_broker': 'str',
        'max_consumer_per_broker': 'str',
        'max_storage_per_node': 'str',
        'min_broker': 'str',
        'engine_versions': 'str',
        'min_storage_per_node': 'str',
        'product_alias': 'str'
    }

    attribute_map = {
        'max_broker': 'max_broker',
        'max_topic_per_broker': 'max_topic_per_broker',
        'max_consumer_per_broker': 'max_consumer_per_broker',
        'max_storage_per_node': 'max_storage_per_node',
        'min_broker': 'min_broker',
        'engine_versions': 'engine_versions',
        'min_storage_per_node': 'min_storage_per_node',
        'product_alias': 'product_alias'
    }

    def __init__(self, max_broker=None, max_topic_per_broker=None, max_consumer_per_broker=None, max_storage_per_node=None, min_broker=None, engine_versions=None, min_storage_per_node=None, product_alias=None):
        r"""RocketMQExtendProductPropertiesEntity

        The model defined in huaweicloud sdk

        :param max_broker: Broker的最大个数。
        :type max_broker: str
        :param max_topic_per_broker: 每个节点最多能创建的Topic个数。
        :type max_topic_per_broker: str
        :param max_consumer_per_broker: 每个节点的最大消费者数。
        :type max_consumer_per_broker: str
        :param max_storage_per_node: 每个节点的最大存储。单位为GB
        :type max_storage_per_node: str
        :param min_broker: Broker的最小个数。
        :type min_broker: str
        :param engine_versions: 消息引擎版本。
        :type engine_versions: str
        :param min_storage_per_node: 每个节点的最小存储。单位为GB。
        :type min_storage_per_node: str
        :param product_alias: product_id的别名。
        :type product_alias: str
        """
        
        

        self._max_broker = None
        self._max_topic_per_broker = None
        self._max_consumer_per_broker = None
        self._max_storage_per_node = None
        self._min_broker = None
        self._engine_versions = None
        self._min_storage_per_node = None
        self._product_alias = None
        self.discriminator = None

        if max_broker is not None:
            self.max_broker = max_broker
        if max_topic_per_broker is not None:
            self.max_topic_per_broker = max_topic_per_broker
        if max_consumer_per_broker is not None:
            self.max_consumer_per_broker = max_consumer_per_broker
        if max_storage_per_node is not None:
            self.max_storage_per_node = max_storage_per_node
        if min_broker is not None:
            self.min_broker = min_broker
        if engine_versions is not None:
            self.engine_versions = engine_versions
        if min_storage_per_node is not None:
            self.min_storage_per_node = min_storage_per_node
        if product_alias is not None:
            self.product_alias = product_alias

    @property
    def max_broker(self):
        r"""Gets the max_broker of this RocketMQExtendProductPropertiesEntity.

        Broker的最大个数。

        :return: The max_broker of this RocketMQExtendProductPropertiesEntity.
        :rtype: str
        """
        return self._max_broker

    @max_broker.setter
    def max_broker(self, max_broker):
        r"""Sets the max_broker of this RocketMQExtendProductPropertiesEntity.

        Broker的最大个数。

        :param max_broker: The max_broker of this RocketMQExtendProductPropertiesEntity.
        :type max_broker: str
        """
        self._max_broker = max_broker

    @property
    def max_topic_per_broker(self):
        r"""Gets the max_topic_per_broker of this RocketMQExtendProductPropertiesEntity.

        每个节点最多能创建的Topic个数。

        :return: The max_topic_per_broker of this RocketMQExtendProductPropertiesEntity.
        :rtype: str
        """
        return self._max_topic_per_broker

    @max_topic_per_broker.setter
    def max_topic_per_broker(self, max_topic_per_broker):
        r"""Sets the max_topic_per_broker of this RocketMQExtendProductPropertiesEntity.

        每个节点最多能创建的Topic个数。

        :param max_topic_per_broker: The max_topic_per_broker of this RocketMQExtendProductPropertiesEntity.
        :type max_topic_per_broker: str
        """
        self._max_topic_per_broker = max_topic_per_broker

    @property
    def max_consumer_per_broker(self):
        r"""Gets the max_consumer_per_broker of this RocketMQExtendProductPropertiesEntity.

        每个节点的最大消费者数。

        :return: The max_consumer_per_broker of this RocketMQExtendProductPropertiesEntity.
        :rtype: str
        """
        return self._max_consumer_per_broker

    @max_consumer_per_broker.setter
    def max_consumer_per_broker(self, max_consumer_per_broker):
        r"""Sets the max_consumer_per_broker of this RocketMQExtendProductPropertiesEntity.

        每个节点的最大消费者数。

        :param max_consumer_per_broker: The max_consumer_per_broker of this RocketMQExtendProductPropertiesEntity.
        :type max_consumer_per_broker: str
        """
        self._max_consumer_per_broker = max_consumer_per_broker

    @property
    def max_storage_per_node(self):
        r"""Gets the max_storage_per_node of this RocketMQExtendProductPropertiesEntity.

        每个节点的最大存储。单位为GB

        :return: The max_storage_per_node of this RocketMQExtendProductPropertiesEntity.
        :rtype: str
        """
        return self._max_storage_per_node

    @max_storage_per_node.setter
    def max_storage_per_node(self, max_storage_per_node):
        r"""Sets the max_storage_per_node of this RocketMQExtendProductPropertiesEntity.

        每个节点的最大存储。单位为GB

        :param max_storage_per_node: The max_storage_per_node of this RocketMQExtendProductPropertiesEntity.
        :type max_storage_per_node: str
        """
        self._max_storage_per_node = max_storage_per_node

    @property
    def min_broker(self):
        r"""Gets the min_broker of this RocketMQExtendProductPropertiesEntity.

        Broker的最小个数。

        :return: The min_broker of this RocketMQExtendProductPropertiesEntity.
        :rtype: str
        """
        return self._min_broker

    @min_broker.setter
    def min_broker(self, min_broker):
        r"""Sets the min_broker of this RocketMQExtendProductPropertiesEntity.

        Broker的最小个数。

        :param min_broker: The min_broker of this RocketMQExtendProductPropertiesEntity.
        :type min_broker: str
        """
        self._min_broker = min_broker

    @property
    def engine_versions(self):
        r"""Gets the engine_versions of this RocketMQExtendProductPropertiesEntity.

        消息引擎版本。

        :return: The engine_versions of this RocketMQExtendProductPropertiesEntity.
        :rtype: str
        """
        return self._engine_versions

    @engine_versions.setter
    def engine_versions(self, engine_versions):
        r"""Sets the engine_versions of this RocketMQExtendProductPropertiesEntity.

        消息引擎版本。

        :param engine_versions: The engine_versions of this RocketMQExtendProductPropertiesEntity.
        :type engine_versions: str
        """
        self._engine_versions = engine_versions

    @property
    def min_storage_per_node(self):
        r"""Gets the min_storage_per_node of this RocketMQExtendProductPropertiesEntity.

        每个节点的最小存储。单位为GB。

        :return: The min_storage_per_node of this RocketMQExtendProductPropertiesEntity.
        :rtype: str
        """
        return self._min_storage_per_node

    @min_storage_per_node.setter
    def min_storage_per_node(self, min_storage_per_node):
        r"""Sets the min_storage_per_node of this RocketMQExtendProductPropertiesEntity.

        每个节点的最小存储。单位为GB。

        :param min_storage_per_node: The min_storage_per_node of this RocketMQExtendProductPropertiesEntity.
        :type min_storage_per_node: str
        """
        self._min_storage_per_node = min_storage_per_node

    @property
    def product_alias(self):
        r"""Gets the product_alias of this RocketMQExtendProductPropertiesEntity.

        product_id的别名。

        :return: The product_alias of this RocketMQExtendProductPropertiesEntity.
        :rtype: str
        """
        return self._product_alias

    @product_alias.setter
    def product_alias(self, product_alias):
        r"""Sets the product_alias of this RocketMQExtendProductPropertiesEntity.

        product_id的别名。

        :param product_alias: The product_alias of this RocketMQExtendProductPropertiesEntity.
        :type product_alias: str
        """
        self._product_alias = product_alias

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
        if not isinstance(other, RocketMQExtendProductPropertiesEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
