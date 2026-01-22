# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductEntityProperties:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_topic': 'str',
        'broker_num': 'str',
        'core': 'str',
        'max_consumer': 'str',
        'rcu': 'str',
        'max_storage': 'str',
        'max_storage_per_node': 'str',
        'product_alias': 'str',
        'max_tps_per_rcu': 'str',
        'engine_versions': 'str',
        'min_storage': 'str',
        'min_storage_per_node': 'str',
        'max_broker': 'str',
        'max_topic_per_broker': 'str',
        'max_consumer_per_broker': 'str',
        'min_broker': 'str'
    }

    attribute_map = {
        'max_topic': 'max_topic',
        'broker_num': 'broker_num',
        'core': 'core',
        'max_consumer': 'max_consumer',
        'rcu': 'rcu',
        'max_storage': 'max_storage',
        'max_storage_per_node': 'max_storage_per_node',
        'product_alias': 'product_alias',
        'max_tps_per_rcu': 'max_tps_per_rcu',
        'engine_versions': 'engine_versions',
        'min_storage': 'min_storage',
        'min_storage_per_node': 'min_storage_per_node',
        'max_broker': 'max_broker',
        'max_topic_per_broker': 'max_topic_per_broker',
        'max_consumer_per_broker': 'max_consumer_per_broker',
        'min_broker': 'min_broker'
    }

    def __init__(self, max_topic=None, broker_num=None, core=None, max_consumer=None, rcu=None, max_storage=None, max_storage_per_node=None, product_alias=None, max_tps_per_rcu=None, engine_versions=None, min_storage=None, min_storage_per_node=None, max_broker=None, max_topic_per_broker=None, max_consumer_per_broker=None, min_broker=None):
        r"""ProductEntityProperties

        The model defined in huaweicloud sdk

        :param max_topic: **参数解释**： 最大topic数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type max_topic: str
        :param broker_num: **参数解释**： broker数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type broker_num: str
        :param core: **参数解释**： 整个实例的计费核数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type core: str
        :param max_consumer: **参数解释**： 实例消费者的最大数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type max_consumer: str
        :param rcu: **参数解释**： 流量单元，rcu * max_tpc_per_rcu &#x3D; 规格最大TPS。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type rcu: str
        :param max_storage: **参数解释**： 最大存储空间，单位为GB。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type max_storage: str
        :param max_storage_per_node: **参数解释**： 每个节点的最大存储，单位为GB。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type max_storage_per_node: str
        :param product_alias: **参数解释**： product_id的别名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type product_alias: str
        :param max_tps_per_rcu: **参数解释**： 单个rcu最大TPS。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type max_tps_per_rcu: str
        :param engine_versions: **参数解释**： 消息引擎版本。  **约束限制**： 不涉及。  **取值范围**： [- 4.8.0](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- 5.x](tag:hws,hws_eu,hws_hk,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,srg) **默认取值**： 不涉及。
        :type engine_versions: str
        :param min_storage: **参数解释**： 最小存储空间，单位为GB。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type min_storage: str
        :param min_storage_per_node: **参数解释**： 每个节点的最小存储。单位为GB。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type min_storage_per_node: str
        :param max_broker: **参数解释**： Broker的最大个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type max_broker: str
        :param max_topic_per_broker: **参数解释**： 每个节点最多能创建的Topic个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type max_topic_per_broker: str
        :param max_consumer_per_broker: **参数解释**： 每个节点的最大消费者数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type max_consumer_per_broker: str
        :param min_broker: **参数解释**： Broker的最小个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type min_broker: str
        """
        
        

        self._max_topic = None
        self._broker_num = None
        self._core = None
        self._max_consumer = None
        self._rcu = None
        self._max_storage = None
        self._max_storage_per_node = None
        self._product_alias = None
        self._max_tps_per_rcu = None
        self._engine_versions = None
        self._min_storage = None
        self._min_storage_per_node = None
        self._max_broker = None
        self._max_topic_per_broker = None
        self._max_consumer_per_broker = None
        self._min_broker = None
        self.discriminator = None

        if max_topic is not None:
            self.max_topic = max_topic
        if broker_num is not None:
            self.broker_num = broker_num
        if core is not None:
            self.core = core
        if max_consumer is not None:
            self.max_consumer = max_consumer
        if rcu is not None:
            self.rcu = rcu
        if max_storage is not None:
            self.max_storage = max_storage
        if max_storage_per_node is not None:
            self.max_storage_per_node = max_storage_per_node
        if product_alias is not None:
            self.product_alias = product_alias
        if max_tps_per_rcu is not None:
            self.max_tps_per_rcu = max_tps_per_rcu
        if engine_versions is not None:
            self.engine_versions = engine_versions
        if min_storage is not None:
            self.min_storage = min_storage
        if min_storage_per_node is not None:
            self.min_storage_per_node = min_storage_per_node
        if max_broker is not None:
            self.max_broker = max_broker
        if max_topic_per_broker is not None:
            self.max_topic_per_broker = max_topic_per_broker
        if max_consumer_per_broker is not None:
            self.max_consumer_per_broker = max_consumer_per_broker
        if min_broker is not None:
            self.min_broker = min_broker

    @property
    def max_topic(self):
        r"""Gets the max_topic of this ProductEntityProperties.

        **参数解释**： 最大topic数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The max_topic of this ProductEntityProperties.
        :rtype: str
        """
        return self._max_topic

    @max_topic.setter
    def max_topic(self, max_topic):
        r"""Sets the max_topic of this ProductEntityProperties.

        **参数解释**： 最大topic数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param max_topic: The max_topic of this ProductEntityProperties.
        :type max_topic: str
        """
        self._max_topic = max_topic

    @property
    def broker_num(self):
        r"""Gets the broker_num of this ProductEntityProperties.

        **参数解释**： broker数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The broker_num of this ProductEntityProperties.
        :rtype: str
        """
        return self._broker_num

    @broker_num.setter
    def broker_num(self, broker_num):
        r"""Sets the broker_num of this ProductEntityProperties.

        **参数解释**： broker数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param broker_num: The broker_num of this ProductEntityProperties.
        :type broker_num: str
        """
        self._broker_num = broker_num

    @property
    def core(self):
        r"""Gets the core of this ProductEntityProperties.

        **参数解释**： 整个实例的计费核数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The core of this ProductEntityProperties.
        :rtype: str
        """
        return self._core

    @core.setter
    def core(self, core):
        r"""Sets the core of this ProductEntityProperties.

        **参数解释**： 整个实例的计费核数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param core: The core of this ProductEntityProperties.
        :type core: str
        """
        self._core = core

    @property
    def max_consumer(self):
        r"""Gets the max_consumer of this ProductEntityProperties.

        **参数解释**： 实例消费者的最大数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The max_consumer of this ProductEntityProperties.
        :rtype: str
        """
        return self._max_consumer

    @max_consumer.setter
    def max_consumer(self, max_consumer):
        r"""Sets the max_consumer of this ProductEntityProperties.

        **参数解释**： 实例消费者的最大数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param max_consumer: The max_consumer of this ProductEntityProperties.
        :type max_consumer: str
        """
        self._max_consumer = max_consumer

    @property
    def rcu(self):
        r"""Gets the rcu of this ProductEntityProperties.

        **参数解释**： 流量单元，rcu * max_tpc_per_rcu = 规格最大TPS。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The rcu of this ProductEntityProperties.
        :rtype: str
        """
        return self._rcu

    @rcu.setter
    def rcu(self, rcu):
        r"""Sets the rcu of this ProductEntityProperties.

        **参数解释**： 流量单元，rcu * max_tpc_per_rcu = 规格最大TPS。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param rcu: The rcu of this ProductEntityProperties.
        :type rcu: str
        """
        self._rcu = rcu

    @property
    def max_storage(self):
        r"""Gets the max_storage of this ProductEntityProperties.

        **参数解释**： 最大存储空间，单位为GB。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The max_storage of this ProductEntityProperties.
        :rtype: str
        """
        return self._max_storage

    @max_storage.setter
    def max_storage(self, max_storage):
        r"""Sets the max_storage of this ProductEntityProperties.

        **参数解释**： 最大存储空间，单位为GB。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param max_storage: The max_storage of this ProductEntityProperties.
        :type max_storage: str
        """
        self._max_storage = max_storage

    @property
    def max_storage_per_node(self):
        r"""Gets the max_storage_per_node of this ProductEntityProperties.

        **参数解释**： 每个节点的最大存储，单位为GB。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The max_storage_per_node of this ProductEntityProperties.
        :rtype: str
        """
        return self._max_storage_per_node

    @max_storage_per_node.setter
    def max_storage_per_node(self, max_storage_per_node):
        r"""Sets the max_storage_per_node of this ProductEntityProperties.

        **参数解释**： 每个节点的最大存储，单位为GB。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param max_storage_per_node: The max_storage_per_node of this ProductEntityProperties.
        :type max_storage_per_node: str
        """
        self._max_storage_per_node = max_storage_per_node

    @property
    def product_alias(self):
        r"""Gets the product_alias of this ProductEntityProperties.

        **参数解释**： product_id的别名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The product_alias of this ProductEntityProperties.
        :rtype: str
        """
        return self._product_alias

    @product_alias.setter
    def product_alias(self, product_alias):
        r"""Sets the product_alias of this ProductEntityProperties.

        **参数解释**： product_id的别名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param product_alias: The product_alias of this ProductEntityProperties.
        :type product_alias: str
        """
        self._product_alias = product_alias

    @property
    def max_tps_per_rcu(self):
        r"""Gets the max_tps_per_rcu of this ProductEntityProperties.

        **参数解释**： 单个rcu最大TPS。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The max_tps_per_rcu of this ProductEntityProperties.
        :rtype: str
        """
        return self._max_tps_per_rcu

    @max_tps_per_rcu.setter
    def max_tps_per_rcu(self, max_tps_per_rcu):
        r"""Sets the max_tps_per_rcu of this ProductEntityProperties.

        **参数解释**： 单个rcu最大TPS。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param max_tps_per_rcu: The max_tps_per_rcu of this ProductEntityProperties.
        :type max_tps_per_rcu: str
        """
        self._max_tps_per_rcu = max_tps_per_rcu

    @property
    def engine_versions(self):
        r"""Gets the engine_versions of this ProductEntityProperties.

        **参数解释**： 消息引擎版本。  **约束限制**： 不涉及。  **取值范围**： [- 4.8.0](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- 5.x](tag:hws,hws_eu,hws_hk,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,srg) **默认取值**： 不涉及。

        :return: The engine_versions of this ProductEntityProperties.
        :rtype: str
        """
        return self._engine_versions

    @engine_versions.setter
    def engine_versions(self, engine_versions):
        r"""Sets the engine_versions of this ProductEntityProperties.

        **参数解释**： 消息引擎版本。  **约束限制**： 不涉及。  **取值范围**： [- 4.8.0](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- 5.x](tag:hws,hws_eu,hws_hk,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,srg) **默认取值**： 不涉及。

        :param engine_versions: The engine_versions of this ProductEntityProperties.
        :type engine_versions: str
        """
        self._engine_versions = engine_versions

    @property
    def min_storage(self):
        r"""Gets the min_storage of this ProductEntityProperties.

        **参数解释**： 最小存储空间，单位为GB。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The min_storage of this ProductEntityProperties.
        :rtype: str
        """
        return self._min_storage

    @min_storage.setter
    def min_storage(self, min_storage):
        r"""Sets the min_storage of this ProductEntityProperties.

        **参数解释**： 最小存储空间，单位为GB。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param min_storage: The min_storage of this ProductEntityProperties.
        :type min_storage: str
        """
        self._min_storage = min_storage

    @property
    def min_storage_per_node(self):
        r"""Gets the min_storage_per_node of this ProductEntityProperties.

        **参数解释**： 每个节点的最小存储。单位为GB。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The min_storage_per_node of this ProductEntityProperties.
        :rtype: str
        """
        return self._min_storage_per_node

    @min_storage_per_node.setter
    def min_storage_per_node(self, min_storage_per_node):
        r"""Sets the min_storage_per_node of this ProductEntityProperties.

        **参数解释**： 每个节点的最小存储。单位为GB。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param min_storage_per_node: The min_storage_per_node of this ProductEntityProperties.
        :type min_storage_per_node: str
        """
        self._min_storage_per_node = min_storage_per_node

    @property
    def max_broker(self):
        r"""Gets the max_broker of this ProductEntityProperties.

        **参数解释**： Broker的最大个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The max_broker of this ProductEntityProperties.
        :rtype: str
        """
        return self._max_broker

    @max_broker.setter
    def max_broker(self, max_broker):
        r"""Sets the max_broker of this ProductEntityProperties.

        **参数解释**： Broker的最大个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param max_broker: The max_broker of this ProductEntityProperties.
        :type max_broker: str
        """
        self._max_broker = max_broker

    @property
    def max_topic_per_broker(self):
        r"""Gets the max_topic_per_broker of this ProductEntityProperties.

        **参数解释**： 每个节点最多能创建的Topic个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The max_topic_per_broker of this ProductEntityProperties.
        :rtype: str
        """
        return self._max_topic_per_broker

    @max_topic_per_broker.setter
    def max_topic_per_broker(self, max_topic_per_broker):
        r"""Sets the max_topic_per_broker of this ProductEntityProperties.

        **参数解释**： 每个节点最多能创建的Topic个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param max_topic_per_broker: The max_topic_per_broker of this ProductEntityProperties.
        :type max_topic_per_broker: str
        """
        self._max_topic_per_broker = max_topic_per_broker

    @property
    def max_consumer_per_broker(self):
        r"""Gets the max_consumer_per_broker of this ProductEntityProperties.

        **参数解释**： 每个节点的最大消费者数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The max_consumer_per_broker of this ProductEntityProperties.
        :rtype: str
        """
        return self._max_consumer_per_broker

    @max_consumer_per_broker.setter
    def max_consumer_per_broker(self, max_consumer_per_broker):
        r"""Sets the max_consumer_per_broker of this ProductEntityProperties.

        **参数解释**： 每个节点的最大消费者数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param max_consumer_per_broker: The max_consumer_per_broker of this ProductEntityProperties.
        :type max_consumer_per_broker: str
        """
        self._max_consumer_per_broker = max_consumer_per_broker

    @property
    def min_broker(self):
        r"""Gets the min_broker of this ProductEntityProperties.

        **参数解释**： Broker的最小个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The min_broker of this ProductEntityProperties.
        :rtype: str
        """
        return self._min_broker

    @min_broker.setter
    def min_broker(self, min_broker):
        r"""Sets the min_broker of this ProductEntityProperties.

        **参数解释**： Broker的最小个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param min_broker: The min_broker of this ProductEntityProperties.
        :type min_broker: str
        """
        self._min_broker = min_broker

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProductEntityProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
