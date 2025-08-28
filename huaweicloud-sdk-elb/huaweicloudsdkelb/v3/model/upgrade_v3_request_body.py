# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeV3RequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'l4_flavor_id': 'str',
        'l7_flavor_id': 'str',
        'availability_zone_list': 'list[str]',
        'ipv6_vip_virsubnet_id': 'str',
        'ipv6_vip_address': 'str',
        'elb_virsubnet_ids': 'list[str]'
    }

    attribute_map = {
        'action': 'action',
        'l4_flavor_id': 'l4_flavor_id',
        'l7_flavor_id': 'l7_flavor_id',
        'availability_zone_list': 'availability_zone_list',
        'ipv6_vip_virsubnet_id': 'ipv6_vip_virsubnet_id',
        'ipv6_vip_address': 'ipv6_vip_address',
        'elb_virsubnet_ids': 'elb_virsubnet_ids'
    }

    def __init__(self, action=None, l4_flavor_id=None, l7_flavor_id=None, availability_zone_list=None, ipv6_vip_virsubnet_id=None, ipv6_vip_address=None, elb_virsubnet_ids=None):
        r"""UpgradeV3RequestBody

        The model defined in huaweicloud sdk

        :param action: **参数解释**：升级过程的操作。  **约束限制**：不涉及  **取值范围**： - start：开始升级。只有当负载均衡器的provisioning_status为ACTIVE时，才能开始升级。 - complete：确认升级完成。只有当实例的provisioning_status为UPGRADED时，才能确认升级完成。确认后，实例无法再执行回退。 - rollback：回退升级，只有当实例的provisioning_status为UPGRADED、UPGRADE_FAILED或ROLLBACK_FAILED时，才能回退升级。  **默认取值**：不涉及
        :type action: str
        :param l4_flavor_id: **参数解释**：四层规格ID。仅action为start时生效。  **约束限制**： - 负载均衡器有四层监听器时该字段必须指定。 - l4_flavor_id和l7_flavor_id不能同时为空。  **取值范围**：不涉及  **默认取值**：不涉及
        :type l4_flavor_id: str
        :param l7_flavor_id: **参数解释**：七层规格ID。仅action为start时生效。  **约束限制**： - 负载均衡器有七层监听器时该字段必须指定。 - l4_flavor_id和l7_flavor_id不能同时为空。  **取值范围**：不涉及  **默认取值**：不涉及
        :type l7_flavor_id: str
        :param availability_zone_list: **参数解释**：可用区列表。仅在action为start时生效，且action为start时，该字段必传。 可通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/availability-zones 接口来查询可用区集合列表。创建负载均衡器时，从查询结果选择某一个可用区集合，并从中选择一个或多个可用区。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type availability_zone_list: list[str]
        :param ipv6_vip_virsubnet_id: **参数解释**：双栈类型负载均衡器所在子网的IPv6网络ID。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的id得到。  **约束限制**： - 若实例升级到独享型后期望使用IPv6功能，则升级时该字段必传。 - ipv6_vip_virsubnet_id所属VPC必须与原共享型实例所属VPC相同。 - ipv6_vip_virsubnet_id所属子网需要开启IPv6。  **取值范围**：不涉及  **默认取值**：不涉及 [不支持IPv6，请勿使用。](tag:dt)
        :type ipv6_vip_virsubnet_id: str
        :param ipv6_vip_address: **参数解释**：负载均衡器的IPv6私网IP。  **约束限制**： - 该地址必须包含在所属子网的IPv6网段内，且未被占用。 - 传入ipv6_vip_address时必须传入ipv6_vip_virsubnet_id。 - 不传入ipv6_vip_address，但传入ipv6_vip_virsubnet_id，则自动分配IPv6私网IP。 - 不传入ipv6_vip_address，且不传ipv6_vip_virsubnet_id，则不分配私网IP，ipv6_vip_address&#x3D;null。  **取值范围**：不涉及  **默认取值**：不涉及 [不支持IPv6，请勿使用。](tag:dt)
        :type ipv6_vip_address: str
        :param elb_virsubnet_ids: **参数解释**：下联面子网的网络ID列表。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到。  **约束限制**： - 仅action为start时生效。 - 若不指定该字段，则选择vip_subnet_cidr_id子网对应的网络ID。 - 下联面子网必须属于该LB所在的VPC。  **取值范围**：不涉及  **默认取值**：不涉及
        :type elb_virsubnet_ids: list[str]
        """
        
        

        self._action = None
        self._l4_flavor_id = None
        self._l7_flavor_id = None
        self._availability_zone_list = None
        self._ipv6_vip_virsubnet_id = None
        self._ipv6_vip_address = None
        self._elb_virsubnet_ids = None
        self.discriminator = None

        self.action = action
        if l4_flavor_id is not None:
            self.l4_flavor_id = l4_flavor_id
        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if availability_zone_list is not None:
            self.availability_zone_list = availability_zone_list
        if ipv6_vip_virsubnet_id is not None:
            self.ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id
        if ipv6_vip_address is not None:
            self.ipv6_vip_address = ipv6_vip_address
        if elb_virsubnet_ids is not None:
            self.elb_virsubnet_ids = elb_virsubnet_ids

    @property
    def action(self):
        r"""Gets the action of this UpgradeV3RequestBody.

        **参数解释**：升级过程的操作。  **约束限制**：不涉及  **取值范围**： - start：开始升级。只有当负载均衡器的provisioning_status为ACTIVE时，才能开始升级。 - complete：确认升级完成。只有当实例的provisioning_status为UPGRADED时，才能确认升级完成。确认后，实例无法再执行回退。 - rollback：回退升级，只有当实例的provisioning_status为UPGRADED、UPGRADE_FAILED或ROLLBACK_FAILED时，才能回退升级。  **默认取值**：不涉及

        :return: The action of this UpgradeV3RequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this UpgradeV3RequestBody.

        **参数解释**：升级过程的操作。  **约束限制**：不涉及  **取值范围**： - start：开始升级。只有当负载均衡器的provisioning_status为ACTIVE时，才能开始升级。 - complete：确认升级完成。只有当实例的provisioning_status为UPGRADED时，才能确认升级完成。确认后，实例无法再执行回退。 - rollback：回退升级，只有当实例的provisioning_status为UPGRADED、UPGRADE_FAILED或ROLLBACK_FAILED时，才能回退升级。  **默认取值**：不涉及

        :param action: The action of this UpgradeV3RequestBody.
        :type action: str
        """
        self._action = action

    @property
    def l4_flavor_id(self):
        r"""Gets the l4_flavor_id of this UpgradeV3RequestBody.

        **参数解释**：四层规格ID。仅action为start时生效。  **约束限制**： - 负载均衡器有四层监听器时该字段必须指定。 - l4_flavor_id和l7_flavor_id不能同时为空。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The l4_flavor_id of this UpgradeV3RequestBody.
        :rtype: str
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        r"""Sets the l4_flavor_id of this UpgradeV3RequestBody.

        **参数解释**：四层规格ID。仅action为start时生效。  **约束限制**： - 负载均衡器有四层监听器时该字段必须指定。 - l4_flavor_id和l7_flavor_id不能同时为空。  **取值范围**：不涉及  **默认取值**：不涉及

        :param l4_flavor_id: The l4_flavor_id of this UpgradeV3RequestBody.
        :type l4_flavor_id: str
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def l7_flavor_id(self):
        r"""Gets the l7_flavor_id of this UpgradeV3RequestBody.

        **参数解释**：七层规格ID。仅action为start时生效。  **约束限制**： - 负载均衡器有七层监听器时该字段必须指定。 - l4_flavor_id和l7_flavor_id不能同时为空。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The l7_flavor_id of this UpgradeV3RequestBody.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        r"""Sets the l7_flavor_id of this UpgradeV3RequestBody.

        **参数解释**：七层规格ID。仅action为start时生效。  **约束限制**： - 负载均衡器有七层监听器时该字段必须指定。 - l4_flavor_id和l7_flavor_id不能同时为空。  **取值范围**：不涉及  **默认取值**：不涉及

        :param l7_flavor_id: The l7_flavor_id of this UpgradeV3RequestBody.
        :type l7_flavor_id: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def availability_zone_list(self):
        r"""Gets the availability_zone_list of this UpgradeV3RequestBody.

        **参数解释**：可用区列表。仅在action为start时生效，且action为start时，该字段必传。 可通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/availability-zones 接口来查询可用区集合列表。创建负载均衡器时，从查询结果选择某一个可用区集合，并从中选择一个或多个可用区。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The availability_zone_list of this UpgradeV3RequestBody.
        :rtype: list[str]
        """
        return self._availability_zone_list

    @availability_zone_list.setter
    def availability_zone_list(self, availability_zone_list):
        r"""Sets the availability_zone_list of this UpgradeV3RequestBody.

        **参数解释**：可用区列表。仅在action为start时生效，且action为start时，该字段必传。 可通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/availability-zones 接口来查询可用区集合列表。创建负载均衡器时，从查询结果选择某一个可用区集合，并从中选择一个或多个可用区。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param availability_zone_list: The availability_zone_list of this UpgradeV3RequestBody.
        :type availability_zone_list: list[str]
        """
        self._availability_zone_list = availability_zone_list

    @property
    def ipv6_vip_virsubnet_id(self):
        r"""Gets the ipv6_vip_virsubnet_id of this UpgradeV3RequestBody.

        **参数解释**：双栈类型负载均衡器所在子网的IPv6网络ID。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的id得到。  **约束限制**： - 若实例升级到独享型后期望使用IPv6功能，则升级时该字段必传。 - ipv6_vip_virsubnet_id所属VPC必须与原共享型实例所属VPC相同。 - ipv6_vip_virsubnet_id所属子网需要开启IPv6。  **取值范围**：不涉及  **默认取值**：不涉及 [不支持IPv6，请勿使用。](tag:dt)

        :return: The ipv6_vip_virsubnet_id of this UpgradeV3RequestBody.
        :rtype: str
        """
        return self._ipv6_vip_virsubnet_id

    @ipv6_vip_virsubnet_id.setter
    def ipv6_vip_virsubnet_id(self, ipv6_vip_virsubnet_id):
        r"""Sets the ipv6_vip_virsubnet_id of this UpgradeV3RequestBody.

        **参数解释**：双栈类型负载均衡器所在子网的IPv6网络ID。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的id得到。  **约束限制**： - 若实例升级到独享型后期望使用IPv6功能，则升级时该字段必传。 - ipv6_vip_virsubnet_id所属VPC必须与原共享型实例所属VPC相同。 - ipv6_vip_virsubnet_id所属子网需要开启IPv6。  **取值范围**：不涉及  **默认取值**：不涉及 [不支持IPv6，请勿使用。](tag:dt)

        :param ipv6_vip_virsubnet_id: The ipv6_vip_virsubnet_id of this UpgradeV3RequestBody.
        :type ipv6_vip_virsubnet_id: str
        """
        self._ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id

    @property
    def ipv6_vip_address(self):
        r"""Gets the ipv6_vip_address of this UpgradeV3RequestBody.

        **参数解释**：负载均衡器的IPv6私网IP。  **约束限制**： - 该地址必须包含在所属子网的IPv6网段内，且未被占用。 - 传入ipv6_vip_address时必须传入ipv6_vip_virsubnet_id。 - 不传入ipv6_vip_address，但传入ipv6_vip_virsubnet_id，则自动分配IPv6私网IP。 - 不传入ipv6_vip_address，且不传ipv6_vip_virsubnet_id，则不分配私网IP，ipv6_vip_address=null。  **取值范围**：不涉及  **默认取值**：不涉及 [不支持IPv6，请勿使用。](tag:dt)

        :return: The ipv6_vip_address of this UpgradeV3RequestBody.
        :rtype: str
        """
        return self._ipv6_vip_address

    @ipv6_vip_address.setter
    def ipv6_vip_address(self, ipv6_vip_address):
        r"""Sets the ipv6_vip_address of this UpgradeV3RequestBody.

        **参数解释**：负载均衡器的IPv6私网IP。  **约束限制**： - 该地址必须包含在所属子网的IPv6网段内，且未被占用。 - 传入ipv6_vip_address时必须传入ipv6_vip_virsubnet_id。 - 不传入ipv6_vip_address，但传入ipv6_vip_virsubnet_id，则自动分配IPv6私网IP。 - 不传入ipv6_vip_address，且不传ipv6_vip_virsubnet_id，则不分配私网IP，ipv6_vip_address=null。  **取值范围**：不涉及  **默认取值**：不涉及 [不支持IPv6，请勿使用。](tag:dt)

        :param ipv6_vip_address: The ipv6_vip_address of this UpgradeV3RequestBody.
        :type ipv6_vip_address: str
        """
        self._ipv6_vip_address = ipv6_vip_address

    @property
    def elb_virsubnet_ids(self):
        r"""Gets the elb_virsubnet_ids of this UpgradeV3RequestBody.

        **参数解释**：下联面子网的网络ID列表。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到。  **约束限制**： - 仅action为start时生效。 - 若不指定该字段，则选择vip_subnet_cidr_id子网对应的网络ID。 - 下联面子网必须属于该LB所在的VPC。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The elb_virsubnet_ids of this UpgradeV3RequestBody.
        :rtype: list[str]
        """
        return self._elb_virsubnet_ids

    @elb_virsubnet_ids.setter
    def elb_virsubnet_ids(self, elb_virsubnet_ids):
        r"""Sets the elb_virsubnet_ids of this UpgradeV3RequestBody.

        **参数解释**：下联面子网的网络ID列表。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到。  **约束限制**： - 仅action为start时生效。 - 若不指定该字段，则选择vip_subnet_cidr_id子网对应的网络ID。 - 下联面子网必须属于该LB所在的VPC。  **取值范围**：不涉及  **默认取值**：不涉及

        :param elb_virsubnet_ids: The elb_virsubnet_ids of this UpgradeV3RequestBody.
        :type elb_virsubnet_ids: list[str]
        """
        self._elb_virsubnet_ids = elb_virsubnet_ids

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
        if not isinstance(other, UpgradeV3RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
