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
        """TargetLoadbalancerParam

        The model defined in huaweicloud sdk

        :param name: 新实例名称。 可选，不选时使用源负载均衡器名称加copy-x的后缀作为新实例名称。
        :type name: str
        :param availability_zone_list: 新实例所属可用区。 可选，不选时使用源负载均衡器的可用区。 只在独享型复制场景可配置。
        :type availability_zone_list: list[str]
        :param vip_subnet_cidr_id: 新实例所属子网的ipv4子网id。 可选，不选时使用源负载均衡器的ipv4子网。 所选子网需要与源负载均衡器在同一个vpc内。
        :type vip_subnet_cidr_id: str
        :param vip_address: 新实例的ipv4私网地址。 可选，不选时随机分配。 只在独享型复制场景、共享型复制为独享型场景可配。
        :type vip_address: str
        :param ipv6_vip_virsubnet_id: 新实例ipv6网络所属的子网网络id。 可选，不选时使用源负载均衡器的子网。 所选子网需要与源负载均衡器在同一个vpc内。 只在独享型复制场景可配。
        :type ipv6_vip_virsubnet_id: str
        :param ipv6_vip_address: 新实例的ipv6地址。 可选，不选时随机分配。 只在独享型复制场景可配。
        :type ipv6_vip_address: str
        :param elb_virsubnet_ids: 新实例后端子网的网络id。 可选，不选时使用源负载均衡器的后端子网。 所选子网需要与源负载均衡器在同一个vpc内。 只在独享型复制场景、共享型复制为独享型场景可配。
        :type elb_virsubnet_ids: list[str]
        :param l4_flavor_id: 新实例4层规格。 可选，不选时使用源负载均衡器的4层规格。 只在独享型复制场景、共享型复制为独享型场景可配。
        :type l4_flavor_id: str
        :param l7_flavor_id: 新实例7层规格。 可选，不选时使用源负载均衡器的7层规格。 只在独享型复制场景、共享型复制为独享型场景可配。
        :type l7_flavor_id: str
        :param enterprise_project_id: 新实例所属企业项目。 可选，不选时使用源负载均衡器的企业项目
        :type enterprise_project_id: str
        :param reuse_pool: 新实例是否复用源ELB的后端服务器组和后端服务器标识。 可选，配置为true时需要开启后端服务器组多实例挂载功能。 不选时默认新创建后端服务器组。 enterprise_project_id选项配置使用其他企业项目时，该选项失效。 只在独享型复制场景、共享型复制为独享型场景可配。
        :type reuse_pool: bool
        :param guaranteed: 新实例类型。 可选配置。 独享型复制场景默认为true，若显式指定，只能配置为true。 共享型复制场景默认为false，若显式指定，配置为false表示新复制共享型实例，配置为true表示新复制独享型实例。
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
        """Gets the name of this TargetLoadbalancerParam.

        新实例名称。 可选，不选时使用源负载均衡器名称加copy-x的后缀作为新实例名称。

        :return: The name of this TargetLoadbalancerParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TargetLoadbalancerParam.

        新实例名称。 可选，不选时使用源负载均衡器名称加copy-x的后缀作为新实例名称。

        :param name: The name of this TargetLoadbalancerParam.
        :type name: str
        """
        self._name = name

    @property
    def availability_zone_list(self):
        """Gets the availability_zone_list of this TargetLoadbalancerParam.

        新实例所属可用区。 可选，不选时使用源负载均衡器的可用区。 只在独享型复制场景可配置。

        :return: The availability_zone_list of this TargetLoadbalancerParam.
        :rtype: list[str]
        """
        return self._availability_zone_list

    @availability_zone_list.setter
    def availability_zone_list(self, availability_zone_list):
        """Sets the availability_zone_list of this TargetLoadbalancerParam.

        新实例所属可用区。 可选，不选时使用源负载均衡器的可用区。 只在独享型复制场景可配置。

        :param availability_zone_list: The availability_zone_list of this TargetLoadbalancerParam.
        :type availability_zone_list: list[str]
        """
        self._availability_zone_list = availability_zone_list

    @property
    def vip_subnet_cidr_id(self):
        """Gets the vip_subnet_cidr_id of this TargetLoadbalancerParam.

        新实例所属子网的ipv4子网id。 可选，不选时使用源负载均衡器的ipv4子网。 所选子网需要与源负载均衡器在同一个vpc内。

        :return: The vip_subnet_cidr_id of this TargetLoadbalancerParam.
        :rtype: str
        """
        return self._vip_subnet_cidr_id

    @vip_subnet_cidr_id.setter
    def vip_subnet_cidr_id(self, vip_subnet_cidr_id):
        """Sets the vip_subnet_cidr_id of this TargetLoadbalancerParam.

        新实例所属子网的ipv4子网id。 可选，不选时使用源负载均衡器的ipv4子网。 所选子网需要与源负载均衡器在同一个vpc内。

        :param vip_subnet_cidr_id: The vip_subnet_cidr_id of this TargetLoadbalancerParam.
        :type vip_subnet_cidr_id: str
        """
        self._vip_subnet_cidr_id = vip_subnet_cidr_id

    @property
    def vip_address(self):
        """Gets the vip_address of this TargetLoadbalancerParam.

        新实例的ipv4私网地址。 可选，不选时随机分配。 只在独享型复制场景、共享型复制为独享型场景可配。

        :return: The vip_address of this TargetLoadbalancerParam.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        """Sets the vip_address of this TargetLoadbalancerParam.

        新实例的ipv4私网地址。 可选，不选时随机分配。 只在独享型复制场景、共享型复制为独享型场景可配。

        :param vip_address: The vip_address of this TargetLoadbalancerParam.
        :type vip_address: str
        """
        self._vip_address = vip_address

    @property
    def ipv6_vip_virsubnet_id(self):
        """Gets the ipv6_vip_virsubnet_id of this TargetLoadbalancerParam.

        新实例ipv6网络所属的子网网络id。 可选，不选时使用源负载均衡器的子网。 所选子网需要与源负载均衡器在同一个vpc内。 只在独享型复制场景可配。

        :return: The ipv6_vip_virsubnet_id of this TargetLoadbalancerParam.
        :rtype: str
        """
        return self._ipv6_vip_virsubnet_id

    @ipv6_vip_virsubnet_id.setter
    def ipv6_vip_virsubnet_id(self, ipv6_vip_virsubnet_id):
        """Sets the ipv6_vip_virsubnet_id of this TargetLoadbalancerParam.

        新实例ipv6网络所属的子网网络id。 可选，不选时使用源负载均衡器的子网。 所选子网需要与源负载均衡器在同一个vpc内。 只在独享型复制场景可配。

        :param ipv6_vip_virsubnet_id: The ipv6_vip_virsubnet_id of this TargetLoadbalancerParam.
        :type ipv6_vip_virsubnet_id: str
        """
        self._ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id

    @property
    def ipv6_vip_address(self):
        """Gets the ipv6_vip_address of this TargetLoadbalancerParam.

        新实例的ipv6地址。 可选，不选时随机分配。 只在独享型复制场景可配。

        :return: The ipv6_vip_address of this TargetLoadbalancerParam.
        :rtype: str
        """
        return self._ipv6_vip_address

    @ipv6_vip_address.setter
    def ipv6_vip_address(self, ipv6_vip_address):
        """Sets the ipv6_vip_address of this TargetLoadbalancerParam.

        新实例的ipv6地址。 可选，不选时随机分配。 只在独享型复制场景可配。

        :param ipv6_vip_address: The ipv6_vip_address of this TargetLoadbalancerParam.
        :type ipv6_vip_address: str
        """
        self._ipv6_vip_address = ipv6_vip_address

    @property
    def elb_virsubnet_ids(self):
        """Gets the elb_virsubnet_ids of this TargetLoadbalancerParam.

        新实例后端子网的网络id。 可选，不选时使用源负载均衡器的后端子网。 所选子网需要与源负载均衡器在同一个vpc内。 只在独享型复制场景、共享型复制为独享型场景可配。

        :return: The elb_virsubnet_ids of this TargetLoadbalancerParam.
        :rtype: list[str]
        """
        return self._elb_virsubnet_ids

    @elb_virsubnet_ids.setter
    def elb_virsubnet_ids(self, elb_virsubnet_ids):
        """Sets the elb_virsubnet_ids of this TargetLoadbalancerParam.

        新实例后端子网的网络id。 可选，不选时使用源负载均衡器的后端子网。 所选子网需要与源负载均衡器在同一个vpc内。 只在独享型复制场景、共享型复制为独享型场景可配。

        :param elb_virsubnet_ids: The elb_virsubnet_ids of this TargetLoadbalancerParam.
        :type elb_virsubnet_ids: list[str]
        """
        self._elb_virsubnet_ids = elb_virsubnet_ids

    @property
    def l4_flavor_id(self):
        """Gets the l4_flavor_id of this TargetLoadbalancerParam.

        新实例4层规格。 可选，不选时使用源负载均衡器的4层规格。 只在独享型复制场景、共享型复制为独享型场景可配。

        :return: The l4_flavor_id of this TargetLoadbalancerParam.
        :rtype: str
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        """Sets the l4_flavor_id of this TargetLoadbalancerParam.

        新实例4层规格。 可选，不选时使用源负载均衡器的4层规格。 只在独享型复制场景、共享型复制为独享型场景可配。

        :param l4_flavor_id: The l4_flavor_id of this TargetLoadbalancerParam.
        :type l4_flavor_id: str
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def l7_flavor_id(self):
        """Gets the l7_flavor_id of this TargetLoadbalancerParam.

        新实例7层规格。 可选，不选时使用源负载均衡器的7层规格。 只在独享型复制场景、共享型复制为独享型场景可配。

        :return: The l7_flavor_id of this TargetLoadbalancerParam.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        """Sets the l7_flavor_id of this TargetLoadbalancerParam.

        新实例7层规格。 可选，不选时使用源负载均衡器的7层规格。 只在独享型复制场景、共享型复制为独享型场景可配。

        :param l7_flavor_id: The l7_flavor_id of this TargetLoadbalancerParam.
        :type l7_flavor_id: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this TargetLoadbalancerParam.

        新实例所属企业项目。 可选，不选时使用源负载均衡器的企业项目

        :return: The enterprise_project_id of this TargetLoadbalancerParam.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this TargetLoadbalancerParam.

        新实例所属企业项目。 可选，不选时使用源负载均衡器的企业项目

        :param enterprise_project_id: The enterprise_project_id of this TargetLoadbalancerParam.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def reuse_pool(self):
        """Gets the reuse_pool of this TargetLoadbalancerParam.

        新实例是否复用源ELB的后端服务器组和后端服务器标识。 可选，配置为true时需要开启后端服务器组多实例挂载功能。 不选时默认新创建后端服务器组。 enterprise_project_id选项配置使用其他企业项目时，该选项失效。 只在独享型复制场景、共享型复制为独享型场景可配。

        :return: The reuse_pool of this TargetLoadbalancerParam.
        :rtype: bool
        """
        return self._reuse_pool

    @reuse_pool.setter
    def reuse_pool(self, reuse_pool):
        """Sets the reuse_pool of this TargetLoadbalancerParam.

        新实例是否复用源ELB的后端服务器组和后端服务器标识。 可选，配置为true时需要开启后端服务器组多实例挂载功能。 不选时默认新创建后端服务器组。 enterprise_project_id选项配置使用其他企业项目时，该选项失效。 只在独享型复制场景、共享型复制为独享型场景可配。

        :param reuse_pool: The reuse_pool of this TargetLoadbalancerParam.
        :type reuse_pool: bool
        """
        self._reuse_pool = reuse_pool

    @property
    def guaranteed(self):
        """Gets the guaranteed of this TargetLoadbalancerParam.

        新实例类型。 可选配置。 独享型复制场景默认为true，若显式指定，只能配置为true。 共享型复制场景默认为false，若显式指定，配置为false表示新复制共享型实例，配置为true表示新复制独享型实例。

        :return: The guaranteed of this TargetLoadbalancerParam.
        :rtype: bool
        """
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, guaranteed):
        """Sets the guaranteed of this TargetLoadbalancerParam.

        新实例类型。 可选配置。 独享型复制场景默认为true，若显式指定，只能配置为true。 共享型复制场景默认为false，若显式指定，配置为false表示新复制共享型实例，配置为true表示新复制独享型实例。

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
