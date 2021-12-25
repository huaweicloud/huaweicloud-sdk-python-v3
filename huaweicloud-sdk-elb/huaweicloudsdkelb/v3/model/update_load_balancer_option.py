# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLoadBalancerOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'admin_state_up': 'bool',
        'description': 'str',
        'ipv6_vip_virsubnet_id': 'str',
        'vip_subnet_cidr_id': 'str',
        'vip_address': 'str',
        'l4_flavor_id': 'str',
        'l7_flavor_id': 'str',
        'ipv6_bandwidth': 'BandwidthRef',
        'ip_target_enable': 'bool',
        'elb_virsubnet_ids': 'list[str]',
        'deletion_protection_enable': 'bool',
        'prepaid_options': 'PrepaidUpdateOption',
        'autoscaling': 'UpdateLoadbalancerAutoscalingOption'
    }

    attribute_map = {
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'ipv6_vip_virsubnet_id': 'ipv6_vip_virsubnet_id',
        'vip_subnet_cidr_id': 'vip_subnet_cidr_id',
        'vip_address': 'vip_address',
        'l4_flavor_id': 'l4_flavor_id',
        'l7_flavor_id': 'l7_flavor_id',
        'ipv6_bandwidth': 'ipv6_bandwidth',
        'ip_target_enable': 'ip_target_enable',
        'elb_virsubnet_ids': 'elb_virsubnet_ids',
        'deletion_protection_enable': 'deletion_protection_enable',
        'prepaid_options': 'prepaid_options',
        'autoscaling': 'autoscaling'
    }

    def __init__(self, name=None, admin_state_up=None, description=None, ipv6_vip_virsubnet_id=None, vip_subnet_cidr_id=None, vip_address=None, l4_flavor_id=None, l7_flavor_id=None, ipv6_bandwidth=None, ip_target_enable=None, elb_virsubnet_ids=None, deletion_protection_enable=None, prepaid_options=None, autoscaling=None):
        """UpdateLoadBalancerOption - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._admin_state_up = None
        self._description = None
        self._ipv6_vip_virsubnet_id = None
        self._vip_subnet_cidr_id = None
        self._vip_address = None
        self._l4_flavor_id = None
        self._l7_flavor_id = None
        self._ipv6_bandwidth = None
        self._ip_target_enable = None
        self._elb_virsubnet_ids = None
        self._deletion_protection_enable = None
        self._prepaid_options = None
        self._autoscaling = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if description is not None:
            self.description = description
        if ipv6_vip_virsubnet_id is not None:
            self.ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id
        if vip_subnet_cidr_id is not None:
            self.vip_subnet_cidr_id = vip_subnet_cidr_id
        if vip_address is not None:
            self.vip_address = vip_address
        if l4_flavor_id is not None:
            self.l4_flavor_id = l4_flavor_id
        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth
        if ip_target_enable is not None:
            self.ip_target_enable = ip_target_enable
        if elb_virsubnet_ids is not None:
            self.elb_virsubnet_ids = elb_virsubnet_ids
        if deletion_protection_enable is not None:
            self.deletion_protection_enable = deletion_protection_enable
        if prepaid_options is not None:
            self.prepaid_options = prepaid_options
        if autoscaling is not None:
            self.autoscaling = autoscaling

    @property
    def name(self):
        """Gets the name of this UpdateLoadBalancerOption.

        负载均衡器的名称。

        :return: The name of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateLoadBalancerOption.

        负载均衡器的名称。

        :param name: The name of this UpdateLoadBalancerOption.
        :type: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateLoadBalancerOption.

        负载均衡器的管理状态。只能设置为true。  [不支持该字段，请勿使用。](tag:dt,dt_test)

        :return: The admin_state_up of this UpdateLoadBalancerOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateLoadBalancerOption.

        负载均衡器的管理状态。只能设置为true。  [不支持该字段，请勿使用。](tag:dt,dt_test)

        :param admin_state_up: The admin_state_up of this UpdateLoadBalancerOption.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this UpdateLoadBalancerOption.

        负载均衡器的描述。

        :return: The description of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateLoadBalancerOption.

        负载均衡器的描述。

        :param description: The description of this UpdateLoadBalancerOption.
        :type: str
        """
        self._description = description

    @property
    def ipv6_vip_virsubnet_id(self):
        """Gets the ipv6_vip_virsubnet_id of this UpdateLoadBalancerOption.

        双栈类型负载均衡器所在子网的IPv6网络ID。可以通过GET https&#58;//{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的id得到。 通过更新ipv6_vip_virsubnet_id可以更新负载均衡器所在IPv6子网，并且负载均衡器的内网IPv6地址将发生变化。 ipv6_vip_virsubnet_id对应的子网必须属于当前负载均衡器所在VPC。 注： 1.只有子网开启IPv6时才可以传入。 2.仅当guaranteed是true的场合，才支持更新。 3.传入为null表示解绑IPv6子网。 [不支持IPv6，请勿使用。](tag:dt,dt_test)

        :return: The ipv6_vip_virsubnet_id of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._ipv6_vip_virsubnet_id

    @ipv6_vip_virsubnet_id.setter
    def ipv6_vip_virsubnet_id(self, ipv6_vip_virsubnet_id):
        """Sets the ipv6_vip_virsubnet_id of this UpdateLoadBalancerOption.

        双栈类型负载均衡器所在子网的IPv6网络ID。可以通过GET https&#58;//{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的id得到。 通过更新ipv6_vip_virsubnet_id可以更新负载均衡器所在IPv6子网，并且负载均衡器的内网IPv6地址将发生变化。 ipv6_vip_virsubnet_id对应的子网必须属于当前负载均衡器所在VPC。 注： 1.只有子网开启IPv6时才可以传入。 2.仅当guaranteed是true的场合，才支持更新。 3.传入为null表示解绑IPv6子网。 [不支持IPv6，请勿使用。](tag:dt,dt_test)

        :param ipv6_vip_virsubnet_id: The ipv6_vip_virsubnet_id of this UpdateLoadBalancerOption.
        :type: str
        """
        self._ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id

    @property
    def vip_subnet_cidr_id(self):
        """Gets the vip_subnet_cidr_id of this UpdateLoadBalancerOption.

        负载均衡器所在的IPv4子网ID。可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_subnet_id得到。 通过更新vip_subnet_cidr_id可以更新负载均衡器所在IPv4子网，并且负载均衡器的内网IPv4地址将发生变化。 若同时设置了vip_address，则必须保证vip_address对应的IP在vip_subnet_cidr_id的子网网段中。更新后将使用vip_address对应的IP作为负载均衡器的内网IPv4地址。 vip_subnet_cidr_id对应的子网必须属于当前负载均衡器vpc_id对应的VPC。 注： 1.只有guaranteed是true的负载均衡器才支持更新vip_subnet_cidr_id。 2.传入null表示解绑IPv4子网。

        :return: The vip_subnet_cidr_id of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._vip_subnet_cidr_id

    @vip_subnet_cidr_id.setter
    def vip_subnet_cidr_id(self, vip_subnet_cidr_id):
        """Sets the vip_subnet_cidr_id of this UpdateLoadBalancerOption.

        负载均衡器所在的IPv4子网ID。可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_subnet_id得到。 通过更新vip_subnet_cidr_id可以更新负载均衡器所在IPv4子网，并且负载均衡器的内网IPv4地址将发生变化。 若同时设置了vip_address，则必须保证vip_address对应的IP在vip_subnet_cidr_id的子网网段中。更新后将使用vip_address对应的IP作为负载均衡器的内网IPv4地址。 vip_subnet_cidr_id对应的子网必须属于当前负载均衡器vpc_id对应的VPC。 注： 1.只有guaranteed是true的负载均衡器才支持更新vip_subnet_cidr_id。 2.传入null表示解绑IPv4子网。

        :param vip_subnet_cidr_id: The vip_subnet_cidr_id of this UpdateLoadBalancerOption.
        :type: str
        """
        self._vip_subnet_cidr_id = vip_subnet_cidr_id

    @property
    def vip_address(self):
        """Gets the vip_address of this UpdateLoadBalancerOption.

        负载均衡器的IPv4虚拟IP。该地址必须包含在所在子网的IPv4网段内，且未被占用。  注：仅当guaranteed是true的场合，才支持更新。

        :return: The vip_address of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        """Sets the vip_address of this UpdateLoadBalancerOption.

        负载均衡器的IPv4虚拟IP。该地址必须包含在所在子网的IPv4网段内，且未被占用。  注：仅当guaranteed是true的场合，才支持更新。

        :param vip_address: The vip_address of this UpdateLoadBalancerOption.
        :type: str
        """
        self._vip_address = vip_address

    @property
    def l4_flavor_id(self):
        """Gets the l4_flavor_id of this UpdateLoadBalancerOption.

        四层Flavor ID。  注： 1.仅当guaranteed是true的场合，才支持更新。 2.不允许非null变成null，null变成非null，只允许改大，不允许改小。  [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hws,hcso)

        :return: The l4_flavor_id of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        """Sets the l4_flavor_id of this UpdateLoadBalancerOption.

        四层Flavor ID。  注： 1.仅当guaranteed是true的场合，才支持更新。 2.不允许非null变成null，null变成非null，只允许改大，不允许改小。  [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hws,hcso)

        :param l4_flavor_id: The l4_flavor_id of this UpdateLoadBalancerOption.
        :type: str
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def l7_flavor_id(self):
        """Gets the l7_flavor_id of this UpdateLoadBalancerOption.

        七层Flavor ID。  注： 1.仅当guaranteed是true的场合，才支持更新。 2.不允许非null变成null，null变成非null；只允许改大，不允许改小。  [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hws,hcso)

        :return: The l7_flavor_id of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        """Sets the l7_flavor_id of this UpdateLoadBalancerOption.

        七层Flavor ID。  注： 1.仅当guaranteed是true的场合，才支持更新。 2.不允许非null变成null，null变成非null；只允许改大，不允许改小。  [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hws,hcso)

        :param l7_flavor_id: The l7_flavor_id of this UpdateLoadBalancerOption.
        :type: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def ipv6_bandwidth(self):
        """Gets the ipv6_bandwidth of this UpdateLoadBalancerOption.


        :return: The ipv6_bandwidth of this UpdateLoadBalancerOption.
        :rtype: BandwidthRef
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        """Sets the ipv6_bandwidth of this UpdateLoadBalancerOption.


        :param ipv6_bandwidth: The ipv6_bandwidth of this UpdateLoadBalancerOption.
        :type: BandwidthRef
        """
        self._ipv6_bandwidth = ipv6_bandwidth

    @property
    def ip_target_enable(self):
        """Gets the ip_target_enable of this UpdateLoadBalancerOption.

        是否启用跨VPC后端转发，开启跨VPC后端转发后，支持添加其他VPC、其他公有云、云下数据中心的服务器。取值： - true：开启。 - false：不开启。  仅独享型负载均衡器支持该特性，且只能更新为true，即开启后不支持关闭。  [不支持该字段，请勿使用。](tag:dt,dt_test)

        :return: The ip_target_enable of this UpdateLoadBalancerOption.
        :rtype: bool
        """
        return self._ip_target_enable

    @ip_target_enable.setter
    def ip_target_enable(self, ip_target_enable):
        """Sets the ip_target_enable of this UpdateLoadBalancerOption.

        是否启用跨VPC后端转发，开启跨VPC后端转发后，支持添加其他VPC、其他公有云、云下数据中心的服务器。取值： - true：开启。 - false：不开启。  仅独享型负载均衡器支持该特性，且只能更新为true，即开启后不支持关闭。  [不支持该字段，请勿使用。](tag:dt,dt_test)

        :param ip_target_enable: The ip_target_enable of this UpdateLoadBalancerOption.
        :type: bool
        """
        self._ip_target_enable = ip_target_enable

    @property
    def elb_virsubnet_ids(self):
        """Gets the elb_virsubnet_ids of this UpdateLoadBalancerOption.

        下联面子网的网络ID列表。可以通过GET https&#58;//{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的id得到。 已绑定的下联面子网也在传参elb_virsubnet_ids列表中，则绑定关系保留。 已绑定的下联面子网若不在传参elb_virsubnet_ids列表中，则将移除LB与该下联面子网的关联关系。但不允许移除已被ELB使用的子网，否则将报错，不做任何修改。 在传参elb_virsubnet_ids列表中但不在已绑定的下联面子网列表中，则将新增LB与下联面的绑定关系。  使用说明： - 所有ID同属于该LB所在的VPC。 - 不支持边缘云子网。

        :return: The elb_virsubnet_ids of this UpdateLoadBalancerOption.
        :rtype: list[str]
        """
        return self._elb_virsubnet_ids

    @elb_virsubnet_ids.setter
    def elb_virsubnet_ids(self, elb_virsubnet_ids):
        """Sets the elb_virsubnet_ids of this UpdateLoadBalancerOption.

        下联面子网的网络ID列表。可以通过GET https&#58;//{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的id得到。 已绑定的下联面子网也在传参elb_virsubnet_ids列表中，则绑定关系保留。 已绑定的下联面子网若不在传参elb_virsubnet_ids列表中，则将移除LB与该下联面子网的关联关系。但不允许移除已被ELB使用的子网，否则将报错，不做任何修改。 在传参elb_virsubnet_ids列表中但不在已绑定的下联面子网列表中，则将新增LB与下联面的绑定关系。  使用说明： - 所有ID同属于该LB所在的VPC。 - 不支持边缘云子网。

        :param elb_virsubnet_ids: The elb_virsubnet_ids of this UpdateLoadBalancerOption.
        :type: list[str]
        """
        self._elb_virsubnet_ids = elb_virsubnet_ids

    @property
    def deletion_protection_enable(self):
        """Gets the deletion_protection_enable of this UpdateLoadBalancerOption.

        是否开启删除保护。取值：false不开启，true开启。 > 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用](tag:dt,dt_test)

        :return: The deletion_protection_enable of this UpdateLoadBalancerOption.
        :rtype: bool
        """
        return self._deletion_protection_enable

    @deletion_protection_enable.setter
    def deletion_protection_enable(self, deletion_protection_enable):
        """Sets the deletion_protection_enable of this UpdateLoadBalancerOption.

        是否开启删除保护。取值：false不开启，true开启。 > 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用](tag:dt,dt_test)

        :param deletion_protection_enable: The deletion_protection_enable of this UpdateLoadBalancerOption.
        :type: bool
        """
        self._deletion_protection_enable = deletion_protection_enable

    @property
    def prepaid_options(self):
        """Gets the prepaid_options of this UpdateLoadBalancerOption.


        :return: The prepaid_options of this UpdateLoadBalancerOption.
        :rtype: PrepaidUpdateOption
        """
        return self._prepaid_options

    @prepaid_options.setter
    def prepaid_options(self, prepaid_options):
        """Sets the prepaid_options of this UpdateLoadBalancerOption.


        :param prepaid_options: The prepaid_options of this UpdateLoadBalancerOption.
        :type: PrepaidUpdateOption
        """
        self._prepaid_options = prepaid_options

    @property
    def autoscaling(self):
        """Gets the autoscaling of this UpdateLoadBalancerOption.


        :return: The autoscaling of this UpdateLoadBalancerOption.
        :rtype: UpdateLoadbalancerAutoscalingOption
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        """Sets the autoscaling of this UpdateLoadBalancerOption.


        :param autoscaling: The autoscaling of this UpdateLoadBalancerOption.
        :type: UpdateLoadbalancerAutoscalingOption
        """
        self._autoscaling = autoscaling

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
        if not isinstance(other, UpdateLoadBalancerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
