# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFlavorByTypeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'need_check_replica': 'bool',
        'new_flavor_id': 'str',
        'is_auto_pay': 'int'
    }

    attribute_map = {
        'need_check_replica': 'needCheckReplica',
        'new_flavor_id': 'newFlavorId',
        'is_auto_pay': 'isAutoPay'
    }

    def __init__(self, need_check_replica=None, new_flavor_id=None, is_auto_pay=None):
        """UpdateFlavorByTypeReq

        The model defined in huaweicloud sdk

        :param need_check_replica: 是否需要检查副本，取值范围为true或false。默认开启校验。 - ture: 开启副本校验。 - false: 忽略副本校验。  &gt;Master和Client节点不是数据节点，因此不需要进行副本校验。即使选择true，也不会进行副本校验。
        :type need_check_replica: bool
        :param new_flavor_id: 变更后节点规格ID。 该参数通过 [获取实例规格列表](ListFlavors.xml)接口获取根据name属性对比出比当前集群大的规格，选择对应的flavor_id。 仅支持同一个Esasticsearch引擎版本下的节点规格变更。
        :type new_flavor_id: str
        :param is_auto_pay:  是否自动支付。下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。该参数适用于包周期集群。   - 1: 是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券)。   - 0: 否（需要客户手动去支付，客户可以选择折扣和优惠券）。默认值为“0”。
        :type is_auto_pay: int
        """
        
        

        self._need_check_replica = None
        self._new_flavor_id = None
        self._is_auto_pay = None
        self.discriminator = None

        if need_check_replica is not None:
            self.need_check_replica = need_check_replica
        self.new_flavor_id = new_flavor_id
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def need_check_replica(self):
        """Gets the need_check_replica of this UpdateFlavorByTypeReq.

        是否需要检查副本，取值范围为true或false。默认开启校验。 - ture: 开启副本校验。 - false: 忽略副本校验。  >Master和Client节点不是数据节点，因此不需要进行副本校验。即使选择true，也不会进行副本校验。

        :return: The need_check_replica of this UpdateFlavorByTypeReq.
        :rtype: bool
        """
        return self._need_check_replica

    @need_check_replica.setter
    def need_check_replica(self, need_check_replica):
        """Sets the need_check_replica of this UpdateFlavorByTypeReq.

        是否需要检查副本，取值范围为true或false。默认开启校验。 - ture: 开启副本校验。 - false: 忽略副本校验。  >Master和Client节点不是数据节点，因此不需要进行副本校验。即使选择true，也不会进行副本校验。

        :param need_check_replica: The need_check_replica of this UpdateFlavorByTypeReq.
        :type need_check_replica: bool
        """
        self._need_check_replica = need_check_replica

    @property
    def new_flavor_id(self):
        """Gets the new_flavor_id of this UpdateFlavorByTypeReq.

        变更后节点规格ID。 该参数通过 [获取实例规格列表](ListFlavors.xml)接口获取根据name属性对比出比当前集群大的规格，选择对应的flavor_id。 仅支持同一个Esasticsearch引擎版本下的节点规格变更。

        :return: The new_flavor_id of this UpdateFlavorByTypeReq.
        :rtype: str
        """
        return self._new_flavor_id

    @new_flavor_id.setter
    def new_flavor_id(self, new_flavor_id):
        """Sets the new_flavor_id of this UpdateFlavorByTypeReq.

        变更后节点规格ID。 该参数通过 [获取实例规格列表](ListFlavors.xml)接口获取根据name属性对比出比当前集群大的规格，选择对应的flavor_id。 仅支持同一个Esasticsearch引擎版本下的节点规格变更。

        :param new_flavor_id: The new_flavor_id of this UpdateFlavorByTypeReq.
        :type new_flavor_id: str
        """
        self._new_flavor_id = new_flavor_id

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this UpdateFlavorByTypeReq.

         是否自动支付。下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。该参数适用于包周期集群。   - 1: 是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券)。   - 0: 否（需要客户手动去支付，客户可以选择折扣和优惠券）。默认值为“0”。

        :return: The is_auto_pay of this UpdateFlavorByTypeReq.
        :rtype: int
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this UpdateFlavorByTypeReq.

         是否自动支付。下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。该参数适用于包周期集群。   - 1: 是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券)。   - 0: 否（需要客户手动去支付，客户可以选择折扣和优惠券）。默认值为“0”。

        :param is_auto_pay: The is_auto_pay of this UpdateFlavorByTypeReq.
        :type is_auto_pay: int
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, UpdateFlavorByTypeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
