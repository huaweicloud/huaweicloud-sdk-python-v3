# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKafkaProductCoresRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'product_id': 'str',
        'broker_num': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'product_id': 'product_id',
        'broker_num': 'broker_num'
    }

    def __init__(self, instance_id=None, product_id=None, broker_num=None):
        r"""ShowKafkaProductCoresRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param product_id: **参数解释**： 产品ID。 **约束限制**： 不涉及。 **取值范围**： - s6.2u4g.single.small：规格kafka.2u4g.single.small的产品ID。 - c6.2u4g.single：规格kafka.2u4g.single的产品ID。 [- s6.2u4g.cluster.small：规格kafka.2u4g.cluster.small的产品ID。](tag:hws,hws_hk,hws_eu,dt,ax) - c6.2u4g.cluster：规格kafka.2u4g.cluster的产品ID。 - c6.4u8g.cluster：规格kafka.4u8g.cluster的产品ID。 - c6.8u16g.cluster：规格kafka.8u16g.cluster的产品ID。 - c6.12u24g.cluster：规格kafka.12u24g.cluster的产品ID。 - c6.16u32g.cluster：规格kafka.16u32g.cluster的产品ID。  **默认取值**： 不涉及。
        :type product_id: str
        :param broker_num: **参数解释**： broker数量。 **约束限制**： 不涉及。 **取值范围**： - Kafka实例规格为kafka.2u4g.single.small时，代理数建议取值范围1。 - Kafka实例规格为kafka.2u4g.single时，代理数建议取值范围1。 [- Kafka实例规格为kafka.2u4g.cluster.small时，代理数取值范围3-30。](tag:hws,hws_hk,hws_eu,dt,ax) - Kafka实例规格为kafka.2u4g.cluster时，代理数取值范围3-30。 - Kafka实例规格为kafka.4u8g.cluster时，代理数取值范围3-30。 - Kafka实例规格为kafka.8u16g.cluster时，代理数取值范围3-50。 - Kafka实例规格为kafka.12u24g.cluster时，代理数取值范围3-50。 - Kafka实例规格为kafka.16u32g.cluster时，代理数取值范围3-50。 **默认取值**： 不涉及。
        :type broker_num: str
        """
        
        

        self._instance_id = None
        self._product_id = None
        self._broker_num = None
        self.discriminator = None

        self.instance_id = instance_id
        self.product_id = product_id
        self.broker_num = broker_num

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowKafkaProductCoresRequest.

        实例ID。

        :return: The instance_id of this ShowKafkaProductCoresRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowKafkaProductCoresRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowKafkaProductCoresRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def product_id(self):
        r"""Gets the product_id of this ShowKafkaProductCoresRequest.

        **参数解释**： 产品ID。 **约束限制**： 不涉及。 **取值范围**： - s6.2u4g.single.small：规格kafka.2u4g.single.small的产品ID。 - c6.2u4g.single：规格kafka.2u4g.single的产品ID。 [- s6.2u4g.cluster.small：规格kafka.2u4g.cluster.small的产品ID。](tag:hws,hws_hk,hws_eu,dt,ax) - c6.2u4g.cluster：规格kafka.2u4g.cluster的产品ID。 - c6.4u8g.cluster：规格kafka.4u8g.cluster的产品ID。 - c6.8u16g.cluster：规格kafka.8u16g.cluster的产品ID。 - c6.12u24g.cluster：规格kafka.12u24g.cluster的产品ID。 - c6.16u32g.cluster：规格kafka.16u32g.cluster的产品ID。  **默认取值**： 不涉及。

        :return: The product_id of this ShowKafkaProductCoresRequest.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ShowKafkaProductCoresRequest.

        **参数解释**： 产品ID。 **约束限制**： 不涉及。 **取值范围**： - s6.2u4g.single.small：规格kafka.2u4g.single.small的产品ID。 - c6.2u4g.single：规格kafka.2u4g.single的产品ID。 [- s6.2u4g.cluster.small：规格kafka.2u4g.cluster.small的产品ID。](tag:hws,hws_hk,hws_eu,dt,ax) - c6.2u4g.cluster：规格kafka.2u4g.cluster的产品ID。 - c6.4u8g.cluster：规格kafka.4u8g.cluster的产品ID。 - c6.8u16g.cluster：规格kafka.8u16g.cluster的产品ID。 - c6.12u24g.cluster：规格kafka.12u24g.cluster的产品ID。 - c6.16u32g.cluster：规格kafka.16u32g.cluster的产品ID。  **默认取值**： 不涉及。

        :param product_id: The product_id of this ShowKafkaProductCoresRequest.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def broker_num(self):
        r"""Gets the broker_num of this ShowKafkaProductCoresRequest.

        **参数解释**： broker数量。 **约束限制**： 不涉及。 **取值范围**： - Kafka实例规格为kafka.2u4g.single.small时，代理数建议取值范围1。 - Kafka实例规格为kafka.2u4g.single时，代理数建议取值范围1。 [- Kafka实例规格为kafka.2u4g.cluster.small时，代理数取值范围3-30。](tag:hws,hws_hk,hws_eu,dt,ax) - Kafka实例规格为kafka.2u4g.cluster时，代理数取值范围3-30。 - Kafka实例规格为kafka.4u8g.cluster时，代理数取值范围3-30。 - Kafka实例规格为kafka.8u16g.cluster时，代理数取值范围3-50。 - Kafka实例规格为kafka.12u24g.cluster时，代理数取值范围3-50。 - Kafka实例规格为kafka.16u32g.cluster时，代理数取值范围3-50。 **默认取值**： 不涉及。

        :return: The broker_num of this ShowKafkaProductCoresRequest.
        :rtype: str
        """
        return self._broker_num

    @broker_num.setter
    def broker_num(self, broker_num):
        r"""Sets the broker_num of this ShowKafkaProductCoresRequest.

        **参数解释**： broker数量。 **约束限制**： 不涉及。 **取值范围**： - Kafka实例规格为kafka.2u4g.single.small时，代理数建议取值范围1。 - Kafka实例规格为kafka.2u4g.single时，代理数建议取值范围1。 [- Kafka实例规格为kafka.2u4g.cluster.small时，代理数取值范围3-30。](tag:hws,hws_hk,hws_eu,dt,ax) - Kafka实例规格为kafka.2u4g.cluster时，代理数取值范围3-30。 - Kafka实例规格为kafka.4u8g.cluster时，代理数取值范围3-30。 - Kafka实例规格为kafka.8u16g.cluster时，代理数取值范围3-50。 - Kafka实例规格为kafka.12u24g.cluster时，代理数取值范围3-50。 - Kafka实例规格为kafka.16u32g.cluster时，代理数取值范围3-50。 **默认取值**： 不涉及。

        :param broker_num: The broker_num of this ShowKafkaProductCoresRequest.
        :type broker_num: str
        """
        self._broker_num = broker_num

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
        if not isinstance(other, ShowKafkaProductCoresRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
