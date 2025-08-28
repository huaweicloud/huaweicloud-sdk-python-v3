# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFlavorReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_flavor_id': 'str',
        'operation_type': 'str',
        'need_check_replica': 'bool',
        'is_auto_pay': 'int',
        'need_check_cluster_status': 'bool',
        'cluster_load_check': 'bool'
    }

    attribute_map = {
        'new_flavor_id': 'newFlavorId',
        'operation_type': 'operationType',
        'need_check_replica': 'needCheckReplica',
        'is_auto_pay': 'isAutoPay',
        'need_check_cluster_status': 'needCheckClusterStatus',
        'cluster_load_check': 'clusterLoadCheck'
    }

    def __init__(self, new_flavor_id=None, operation_type=None, need_check_replica=None, is_auto_pay=None, need_check_cluster_status=None, cluster_load_check=None):
        r"""UpdateFlavorReq

        The model defined in huaweicloud sdk

        :param new_flavor_id: 变更后节点规格ID。 该参数通过 该参数通过[获取实例规格列表](ListFlavors.xml)接口获取，根据name属性所需要的规格，选择对应的flavor_id。 仅支持同一个Esasticsearch引擎版本下的节点规格变更。
        :type new_flavor_id: str
        :param operation_type: **参数解释**： 变更规格的操作类型。
        :type operation_type: str
        :param need_check_replica: 是否需要检查副本，取值范围为true或false。默认开启校验。 - true: 开启副本校验。 - false: 忽略副本校验。
        :type need_check_replica: bool
        :param is_auto_pay: 是否自动支付。下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。该参数适用于包周期集群。  - 1: 是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券)。  - 0: 否（需要客户手动去支付，客户可以选择折扣和优惠券）。默认值为“0”。
        :type is_auto_pay: int
        :param need_check_cluster_status: **参数解释**： 集群变更规格是否需要检查集群状态。
        :type need_check_cluster_status: bool
        :param cluster_load_check: **参数解释**： 集群变更规格是否需要检查集群负载。
        :type cluster_load_check: bool
        """
        
        

        self._new_flavor_id = None
        self._operation_type = None
        self._need_check_replica = None
        self._is_auto_pay = None
        self._need_check_cluster_status = None
        self._cluster_load_check = None
        self.discriminator = None

        self.new_flavor_id = new_flavor_id
        if operation_type is not None:
            self.operation_type = operation_type
        if need_check_replica is not None:
            self.need_check_replica = need_check_replica
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if need_check_cluster_status is not None:
            self.need_check_cluster_status = need_check_cluster_status
        if cluster_load_check is not None:
            self.cluster_load_check = cluster_load_check

    @property
    def new_flavor_id(self):
        r"""Gets the new_flavor_id of this UpdateFlavorReq.

        变更后节点规格ID。 该参数通过 该参数通过[获取实例规格列表](ListFlavors.xml)接口获取，根据name属性所需要的规格，选择对应的flavor_id。 仅支持同一个Esasticsearch引擎版本下的节点规格变更。

        :return: The new_flavor_id of this UpdateFlavorReq.
        :rtype: str
        """
        return self._new_flavor_id

    @new_flavor_id.setter
    def new_flavor_id(self, new_flavor_id):
        r"""Sets the new_flavor_id of this UpdateFlavorReq.

        变更后节点规格ID。 该参数通过 该参数通过[获取实例规格列表](ListFlavors.xml)接口获取，根据name属性所需要的规格，选择对应的flavor_id。 仅支持同一个Esasticsearch引擎版本下的节点规格变更。

        :param new_flavor_id: The new_flavor_id of this UpdateFlavorReq.
        :type new_flavor_id: str
        """
        self._new_flavor_id = new_flavor_id

    @property
    def operation_type(self):
        r"""Gets the operation_type of this UpdateFlavorReq.

        **参数解释**： 变更规格的操作类型。

        :return: The operation_type of this UpdateFlavorReq.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this UpdateFlavorReq.

        **参数解释**： 变更规格的操作类型。

        :param operation_type: The operation_type of this UpdateFlavorReq.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def need_check_replica(self):
        r"""Gets the need_check_replica of this UpdateFlavorReq.

        是否需要检查副本，取值范围为true或false。默认开启校验。 - true: 开启副本校验。 - false: 忽略副本校验。

        :return: The need_check_replica of this UpdateFlavorReq.
        :rtype: bool
        """
        return self._need_check_replica

    @need_check_replica.setter
    def need_check_replica(self, need_check_replica):
        r"""Sets the need_check_replica of this UpdateFlavorReq.

        是否需要检查副本，取值范围为true或false。默认开启校验。 - true: 开启副本校验。 - false: 忽略副本校验。

        :param need_check_replica: The need_check_replica of this UpdateFlavorReq.
        :type need_check_replica: bool
        """
        self._need_check_replica = need_check_replica

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this UpdateFlavorReq.

        是否自动支付。下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。该参数适用于包周期集群。  - 1: 是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券)。  - 0: 否（需要客户手动去支付，客户可以选择折扣和优惠券）。默认值为“0”。

        :return: The is_auto_pay of this UpdateFlavorReq.
        :rtype: int
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this UpdateFlavorReq.

        是否自动支付。下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。该参数适用于包周期集群。  - 1: 是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券)。  - 0: 否（需要客户手动去支付，客户可以选择折扣和优惠券）。默认值为“0”。

        :param is_auto_pay: The is_auto_pay of this UpdateFlavorReq.
        :type is_auto_pay: int
        """
        self._is_auto_pay = is_auto_pay

    @property
    def need_check_cluster_status(self):
        r"""Gets the need_check_cluster_status of this UpdateFlavorReq.

        **参数解释**： 集群变更规格是否需要检查集群状态。

        :return: The need_check_cluster_status of this UpdateFlavorReq.
        :rtype: bool
        """
        return self._need_check_cluster_status

    @need_check_cluster_status.setter
    def need_check_cluster_status(self, need_check_cluster_status):
        r"""Sets the need_check_cluster_status of this UpdateFlavorReq.

        **参数解释**： 集群变更规格是否需要检查集群状态。

        :param need_check_cluster_status: The need_check_cluster_status of this UpdateFlavorReq.
        :type need_check_cluster_status: bool
        """
        self._need_check_cluster_status = need_check_cluster_status

    @property
    def cluster_load_check(self):
        r"""Gets the cluster_load_check of this UpdateFlavorReq.

        **参数解释**： 集群变更规格是否需要检查集群负载。

        :return: The cluster_load_check of this UpdateFlavorReq.
        :rtype: bool
        """
        return self._cluster_load_check

    @cluster_load_check.setter
    def cluster_load_check(self, cluster_load_check):
        r"""Sets the cluster_load_check of this UpdateFlavorReq.

        **参数解释**： 集群变更规格是否需要检查集群负载。

        :param cluster_load_check: The cluster_load_check of this UpdateFlavorReq.
        :type cluster_load_check: bool
        """
        self._cluster_load_check = cluster_load_check

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
        if not isinstance(other, UpdateFlavorReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
