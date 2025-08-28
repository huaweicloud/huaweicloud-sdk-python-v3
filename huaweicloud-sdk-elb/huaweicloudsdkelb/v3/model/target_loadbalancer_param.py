# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetLoadbalancerParam:

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
        'availability_zone_list': 'list[str]',
        'vip_subnet_cidr_id': 'str',
        'vip_address': 'str',
        'ipv6_vip_virsubnet_id': 'str',
        'ipv6_vip_address': 'str',
        'elb_virsubnet_ids': 'list[str]',
        'l4_flavor_id': 'str',
        'l7_flavor_id': 'str',
        'enterprise_project_id': 'str',
        'reuse_pool': 'bool',
        'guaranteed': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'availability_zone_list': 'availability_zone_list',
        'vip_subnet_cidr_id': 'vip_subnet_cidr_id',
        'vip_address': 'vip_address',
        'ipv6_vip_virsubnet_id': 'ipv6_vip_virsubnet_id',
        'ipv6_vip_address': 'ipv6_vip_address',
        'elb_virsubnet_ids': 'elb_virsubnet_ids',
        'l4_flavor_id': 'l4_flavor_id',
        'l7_flavor_id': 'l7_flavor_id',
        'enterprise_project_id': 'enterprise_project_id',
        'reuse_pool': 'reuse_pool',
        'guaranteed': 'guaranteed'
    }

    def __init__(self, name=None, availability_zone_list=None, vip_subnet_cidr_id=None, vip_address=None, ipv6_vip_virsubnet_id=None, ipv6_vip_address=None, elb_virsubnet_ids=None, l4_flavor_id=None, l7_flavor_id=None, enterprise_project_id=None, reuse_pool=None, guaranteed=None):
        r"""TargetLoadbalancerParam

        The model defined in huaweicloud sdk

        :param name: **参数解释**：新实例名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不传时使用源ELB名称加\&quot;-copy-{x}\&quot;的后缀作为新实例名称。{x}代表数字序号。
        :type name: str
        :param availability_zone_list: **参数解释**：新实例所属可用区。  **约束限制**：仅支持源ELB独享型复制场景设置该字段。  **取值范围**：不涉及  **默认取值**：不传时使用源ELB的availability_zone_list。
        :type availability_zone_list: list[str]
        :param vip_subnet_cidr_id: **参数解释**：新实例所属子网的ipv4子网ID。  **约束限制**：所选子网必须与源ELB在同一个vpc内。  **取值范围**：不涉及  **默认取值**：不传时使用源ELB的vip_subnet_cidr_id。
        :type vip_subnet_cidr_id: str
        :param vip_address: **参数解释**：新实例的ipv4私网地址。  **约束限制**：仅支持源ELB独享型复制场景、源ELB共享型复制为独享型场景支持设置该字段。  **取值范围**：不涉及  **默认取值**：不传时随机分配vip_subnet_cidr_id对应子网的可用IP地址。
        :type vip_address: str
        :param ipv6_vip_virsubnet_id: **参数解释**：新实例ipv6网络所属的子网网络ID。  **约束限制**： - 仅支持源ELB独享型复制场景设置该字段。 - 所选子网必须与源负载均衡器在同一个vpc内。  **取值范围**：不涉及  **默认取值**：不传时使用源ELB的ipv6_vip_virsubnet_id。
        :type ipv6_vip_virsubnet_id: str
        :param ipv6_vip_address: **参数解释**：新实例的ipv6地址。  **约束限制**：仅支持源ELB为独享型复制场景设置该字段。  **取值范围**：不涉及  **默认取值**：不传时随机分配ipv6_vip_virsubnet_id对应子网的可用IP地址。
        :type ipv6_vip_address: str
        :param elb_virsubnet_ids: **参数解释**：新实例后端子网的网络ID。  **约束限制**： - 仅支持源ELB独享型复制场景、源ELB共享型复制为独享型场景支持设置该字段。 - 所选子网必须与源负载均衡器在同一个vpc内。  **取值范围**：不涉及  **默认取值**：不传时使用源负载均衡器的后端子网。
        :type elb_virsubnet_ids: list[str]
        :param l4_flavor_id: **参数解释**：新实例4层规格。  **约束限制**：仅支持源ELB独享型复制场景、源ELB共享型复制为独享型场景支持设置该字段。  **取值范围**：不涉及  **默认取值**：不传时保持与源负载均衡器的4层规格一致。
        :type l4_flavor_id: str
        :param l7_flavor_id: **参数解释**：新实例7层规格。  **约束限制**：仅支持源ELB独享型复制场景、源ELB共享型复制为独享型场景支持设置该字段。  **取值范围**：不涉及  **默认取值**：不传时保持与源负载均衡器的7层规格一致。
        :type l7_flavor_id: str
        :param enterprise_project_id: **参数解释**：资源所属的企业项目ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不传时保持与源负载均衡器的企业项目一致。
        :type enterprise_project_id: str
        :param reuse_pool: **参数解释**：新实例是否复用源ELB的后端服务器组。  **约束限制**： - 设置为true时，需要开启后端服务器组的多实例挂载功能。 - 请求参数enterprise_project_id使用与源ELB不同的其他企业项目时，该参数失效。 - 仅源ELB独享型复制场景、源ELB共享型复制为独享型场景支持设置为true。  **取值范围**： - false：新创建后端服务器组。 - true：复用源ELB的后端服务器组。  **默认取值**：false
        :type reuse_pool: bool
        :param guaranteed: **参数解释**：新实例类型。  **约束限制**：不涉及  **取值范围**： - false：复制为共享型实例，此时源ELB必须是共享型。 - true：复制为独享型实例，源ELB可以是共享型或独享型。  **默认取值**： - 源ELB是独享型复制场景默认为true。 - 源ELB是共享型复制场景默认为false。
        :type guaranteed: bool
        """
        
        

        self._name = None
        self._availability_zone_list = None
        self._vip_subnet_cidr_id = None
        self._vip_address = None
        self._ipv6_vip_virsubnet_id = None
        self._ipv6_vip_address = None
        self._elb_virsubnet_ids = None
        self._l4_flavor_id = None
        self._l7_flavor_id = None
        self._enterprise_project_id = None
        self._reuse_pool = None
        self._guaranteed = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if availability_zone_list is not None:
            self.availability_zone_list = availability_zone_list
        if vip_subnet_cidr_id is not None:
            self.vip_subnet_cidr_id = vip_subnet_cidr_id
        if vip_address is not None:
            self.vip_address = vip_address
        if ipv6_vip_virsubnet_id is not None:
            self.ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id
        if ipv6_vip_address is not None:
            self.ipv6_vip_address = ipv6_vip_address
        if elb_virsubnet_ids is not None:
            self.elb_virsubnet_ids = elb_virsubnet_ids
        if l4_flavor_id is not None:
            self.l4_flavor_id = l4_flavor_id
        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if reuse_pool is not None:
            self.reuse_pool = reuse_pool
        if guaranteed is not None:
            self.guaranteed = guaranteed

    @property
    def name(self):
        r"""Gets the name of this TargetLoadbalancerParam.

        **参数解释**：新实例名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不传时使用源ELB名称加\"-copy-{x}\"的后缀作为新实例名称。{x}代表数字序号。

        :return: The name of this TargetLoadbalancerParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TargetLoadbalancerParam.

        **参数解释**：新实例名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不传时使用源ELB名称加\"-copy-{x}\"的后缀作为新实例名称。{x}代表数字序号。

        :param name: The name of this TargetLoadbalancerParam.
        :type name: str
        """
        self._name = name

    @property
    def availability_zone_list(self):
        r"""Gets the availability_zone_list of this TargetLoadbalancerParam.

        **参数解释**：新实例所属可用区。  **约束限制**：仅支持源ELB独享型复制场景设置该字段。  **取值范围**：不涉及  **默认取值**：不传时使用源ELB的availability_zone_list。

        :return: The availability_zone_list of this TargetLoadbalancerParam.
        :rtype: list[str]
        """
        return self._availability_zone_list

    @availability_zone_list.setter
    def availability_zone_list(self, availability_zone_list):
        r"""Sets the availability_zone_list of this TargetLoadbalancerParam.

        **参数解释**：新实例所属可用区。  **约束限制**：仅支持源ELB独享型复制场景设置该字段。  **取值范围**：不涉及  **默认取值**：不传时使用源ELB的availability_zone_list。

        :param availability_zone_list: The availability_zone_list of this TargetLoadbalancerParam.
        :type availability_zone_list: list[str]
        """
        self._availability_zone_list = availability_zone_list

    @property
    def vip_subnet_cidr_id(self):
        r"""Gets the vip_subnet_cidr_id of this TargetLoadbalancerParam.

        **参数解释**：新实例所属子网的ipv4子网ID。  **约束限制**：所选子网必须与源ELB在同一个vpc内。  **取值范围**：不涉及  **默认取值**：不传时使用源ELB的vip_subnet_cidr_id。

        :return: The vip_subnet_cidr_id of this TargetLoadbalancerParam.
        :rtype: str
        """
        return self._vip_subnet_cidr_id

    @vip_subnet_cidr_id.setter
    def vip_subnet_cidr_id(self, vip_subnet_cidr_id):
        r"""Sets the vip_subnet_cidr_id of this TargetLoadbalancerParam.

        **参数解释**：新实例所属子网的ipv4子网ID。  **约束限制**：所选子网必须与源ELB在同一个vpc内。  **取值范围**：不涉及  **默认取值**：不传时使用源ELB的vip_subnet_cidr_id。

        :param vip_subnet_cidr_id: The vip_subnet_cidr_id of this TargetLoadbalancerParam.
        :type vip_subnet_cidr_id: str
        """
        self._vip_subnet_cidr_id = vip_subnet_cidr_id

    @property
    def vip_address(self):
        r"""Gets the vip_address of this TargetLoadbalancerParam.

        **参数解释**：新实例的ipv4私网地址。  **约束限制**：仅支持源ELB独享型复制场景、源ELB共享型复制为独享型场景支持设置该字段。  **取值范围**：不涉及  **默认取值**：不传时随机分配vip_subnet_cidr_id对应子网的可用IP地址。

        :return: The vip_address of this TargetLoadbalancerParam.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        r"""Sets the vip_address of this TargetLoadbalancerParam.

        **参数解释**：新实例的ipv4私网地址。  **约束限制**：仅支持源ELB独享型复制场景、源ELB共享型复制为独享型场景支持设置该字段。  **取值范围**：不涉及  **默认取值**：不传时随机分配vip_subnet_cidr_id对应子网的可用IP地址。

        :param vip_address: The vip_address of this TargetLoadbalancerParam.
        :type vip_address: str
        """
        self._vip_address = vip_address

    @property
    def ipv6_vip_virsubnet_id(self):
        r"""Gets the ipv6_vip_virsubnet_id of this TargetLoadbalancerParam.

        **参数解释**：新实例ipv6网络所属的子网网络ID。  **约束限制**： - 仅支持源ELB独享型复制场景设置该字段。 - 所选子网必须与源负载均衡器在同一个vpc内。  **取值范围**：不涉及  **默认取值**：不传时使用源ELB的ipv6_vip_virsubnet_id。

        :return: The ipv6_vip_virsubnet_id of this TargetLoadbalancerParam.
        :rtype: str
        """
        return self._ipv6_vip_virsubnet_id

    @ipv6_vip_virsubnet_id.setter
    def ipv6_vip_virsubnet_id(self, ipv6_vip_virsubnet_id):
        r"""Sets the ipv6_vip_virsubnet_id of this TargetLoadbalancerParam.

        **参数解释**：新实例ipv6网络所属的子网网络ID。  **约束限制**： - 仅支持源ELB独享型复制场景设置该字段。 - 所选子网必须与源负载均衡器在同一个vpc内。  **取值范围**：不涉及  **默认取值**：不传时使用源ELB的ipv6_vip_virsubnet_id。

        :param ipv6_vip_virsubnet_id: The ipv6_vip_virsubnet_id of this TargetLoadbalancerParam.
        :type ipv6_vip_virsubnet_id: str
        """
        self._ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id

    @property
    def ipv6_vip_address(self):
        r"""Gets the ipv6_vip_address of this TargetLoadbalancerParam.

        **参数解释**：新实例的ipv6地址。  **约束限制**：仅支持源ELB为独享型复制场景设置该字段。  **取值范围**：不涉及  **默认取值**：不传时随机分配ipv6_vip_virsubnet_id对应子网的可用IP地址。

        :return: The ipv6_vip_address of this TargetLoadbalancerParam.
        :rtype: str
        """
        return self._ipv6_vip_address

    @ipv6_vip_address.setter
    def ipv6_vip_address(self, ipv6_vip_address):
        r"""Sets the ipv6_vip_address of this TargetLoadbalancerParam.

        **参数解释**：新实例的ipv6地址。  **约束限制**：仅支持源ELB为独享型复制场景设置该字段。  **取值范围**：不涉及  **默认取值**：不传时随机分配ipv6_vip_virsubnet_id对应子网的可用IP地址。

        :param ipv6_vip_address: The ipv6_vip_address of this TargetLoadbalancerParam.
        :type ipv6_vip_address: str
        """
        self._ipv6_vip_address = ipv6_vip_address

    @property
    def elb_virsubnet_ids(self):
        r"""Gets the elb_virsubnet_ids of this TargetLoadbalancerParam.

        **参数解释**：新实例后端子网的网络ID。  **约束限制**： - 仅支持源ELB独享型复制场景、源ELB共享型复制为独享型场景支持设置该字段。 - 所选子网必须与源负载均衡器在同一个vpc内。  **取值范围**：不涉及  **默认取值**：不传时使用源负载均衡器的后端子网。

        :return: The elb_virsubnet_ids of this TargetLoadbalancerParam.
        :rtype: list[str]
        """
        return self._elb_virsubnet_ids

    @elb_virsubnet_ids.setter
    def elb_virsubnet_ids(self, elb_virsubnet_ids):
        r"""Sets the elb_virsubnet_ids of this TargetLoadbalancerParam.

        **参数解释**：新实例后端子网的网络ID。  **约束限制**： - 仅支持源ELB独享型复制场景、源ELB共享型复制为独享型场景支持设置该字段。 - 所选子网必须与源负载均衡器在同一个vpc内。  **取值范围**：不涉及  **默认取值**：不传时使用源负载均衡器的后端子网。

        :param elb_virsubnet_ids: The elb_virsubnet_ids of this TargetLoadbalancerParam.
        :type elb_virsubnet_ids: list[str]
        """
        self._elb_virsubnet_ids = elb_virsubnet_ids

    @property
    def l4_flavor_id(self):
        r"""Gets the l4_flavor_id of this TargetLoadbalancerParam.

        **参数解释**：新实例4层规格。  **约束限制**：仅支持源ELB独享型复制场景、源ELB共享型复制为独享型场景支持设置该字段。  **取值范围**：不涉及  **默认取值**：不传时保持与源负载均衡器的4层规格一致。

        :return: The l4_flavor_id of this TargetLoadbalancerParam.
        :rtype: str
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        r"""Sets the l4_flavor_id of this TargetLoadbalancerParam.

        **参数解释**：新实例4层规格。  **约束限制**：仅支持源ELB独享型复制场景、源ELB共享型复制为独享型场景支持设置该字段。  **取值范围**：不涉及  **默认取值**：不传时保持与源负载均衡器的4层规格一致。

        :param l4_flavor_id: The l4_flavor_id of this TargetLoadbalancerParam.
        :type l4_flavor_id: str
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def l7_flavor_id(self):
        r"""Gets the l7_flavor_id of this TargetLoadbalancerParam.

        **参数解释**：新实例7层规格。  **约束限制**：仅支持源ELB独享型复制场景、源ELB共享型复制为独享型场景支持设置该字段。  **取值范围**：不涉及  **默认取值**：不传时保持与源负载均衡器的7层规格一致。

        :return: The l7_flavor_id of this TargetLoadbalancerParam.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        r"""Sets the l7_flavor_id of this TargetLoadbalancerParam.

        **参数解释**：新实例7层规格。  **约束限制**：仅支持源ELB独享型复制场景、源ELB共享型复制为独享型场景支持设置该字段。  **取值范围**：不涉及  **默认取值**：不传时保持与源负载均衡器的7层规格一致。

        :param l7_flavor_id: The l7_flavor_id of this TargetLoadbalancerParam.
        :type l7_flavor_id: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this TargetLoadbalancerParam.

        **参数解释**：资源所属的企业项目ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不传时保持与源负载均衡器的企业项目一致。

        :return: The enterprise_project_id of this TargetLoadbalancerParam.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this TargetLoadbalancerParam.

        **参数解释**：资源所属的企业项目ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不传时保持与源负载均衡器的企业项目一致。

        :param enterprise_project_id: The enterprise_project_id of this TargetLoadbalancerParam.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def reuse_pool(self):
        r"""Gets the reuse_pool of this TargetLoadbalancerParam.

        **参数解释**：新实例是否复用源ELB的后端服务器组。  **约束限制**： - 设置为true时，需要开启后端服务器组的多实例挂载功能。 - 请求参数enterprise_project_id使用与源ELB不同的其他企业项目时，该参数失效。 - 仅源ELB独享型复制场景、源ELB共享型复制为独享型场景支持设置为true。  **取值范围**： - false：新创建后端服务器组。 - true：复用源ELB的后端服务器组。  **默认取值**：false

        :return: The reuse_pool of this TargetLoadbalancerParam.
        :rtype: bool
        """
        return self._reuse_pool

    @reuse_pool.setter
    def reuse_pool(self, reuse_pool):
        r"""Sets the reuse_pool of this TargetLoadbalancerParam.

        **参数解释**：新实例是否复用源ELB的后端服务器组。  **约束限制**： - 设置为true时，需要开启后端服务器组的多实例挂载功能。 - 请求参数enterprise_project_id使用与源ELB不同的其他企业项目时，该参数失效。 - 仅源ELB独享型复制场景、源ELB共享型复制为独享型场景支持设置为true。  **取值范围**： - false：新创建后端服务器组。 - true：复用源ELB的后端服务器组。  **默认取值**：false

        :param reuse_pool: The reuse_pool of this TargetLoadbalancerParam.
        :type reuse_pool: bool
        """
        self._reuse_pool = reuse_pool

    @property
    def guaranteed(self):
        r"""Gets the guaranteed of this TargetLoadbalancerParam.

        **参数解释**：新实例类型。  **约束限制**：不涉及  **取值范围**： - false：复制为共享型实例，此时源ELB必须是共享型。 - true：复制为独享型实例，源ELB可以是共享型或独享型。  **默认取值**： - 源ELB是独享型复制场景默认为true。 - 源ELB是共享型复制场景默认为false。

        :return: The guaranteed of this TargetLoadbalancerParam.
        :rtype: bool
        """
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, guaranteed):
        r"""Sets the guaranteed of this TargetLoadbalancerParam.

        **参数解释**：新实例类型。  **约束限制**：不涉及  **取值范围**： - false：复制为共享型实例，此时源ELB必须是共享型。 - true：复制为独享型实例，源ELB可以是共享型或独享型。  **默认取值**： - 源ELB是独享型复制场景默认为true。 - 源ELB是共享型复制场景默认为false。

        :param guaranteed: The guaranteed of this TargetLoadbalancerParam.
        :type guaranteed: bool
        """
        self._guaranteed = guaranteed

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
        if not isinstance(other, TargetLoadbalancerParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
