# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterElbInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'cluster_id': 'str',
        'name': 'str',
        'description': 'str',
        'vip_address': 'str',
        'vip_subnet_id': 'str',
        'tenant_id': 'str',
        'type': 'str',
        'admin_state_up': 'bool',
        'bandwidth': 'int',
        'vpc_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cluster_id': 'cluster_id',
        'name': 'name',
        'description': 'description',
        'vip_address': 'vip_address',
        'vip_subnet_id': 'vip_subnet_id',
        'tenant_id': 'tenant_id',
        'type': 'type',
        'admin_state_up': 'admin_state_up',
        'bandwidth': 'bandwidth',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, id=None, cluster_id=None, name=None, description=None, vip_address=None, vip_subnet_id=None, tenant_id=None, type=None, admin_state_up=None, bandwidth=None, vpc_id=None):
        r"""ClusterElbInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 弹性负载均衡ID。 **取值范围**： 不涉及。
        :type id: str
        :param cluster_id: **参数解释**： 集群ID。 **取值范围**： 36位UUID。
        :type cluster_id: str
        :param name: **参数解释**： 弹性负载均衡名称。 **取值范围**： 不涉及。
        :type name: str
        :param description: **参数解释**： 弹性负载均衡描述。 **取值范围**： 不涉及。
        :type description: str
        :param vip_address: **参数解释**： 弹性负载均衡地址。 **取值范围**： 不涉及。
        :type vip_address: str
        :param vip_subnet_id: **参数解释**： 子网ID。 **取值范围**： 不涉及。
        :type vip_subnet_id: str
        :param tenant_id: **参数解释**： 租户ID。 **取值范围**： 不涉及。
        :type tenant_id: str
        :param type: **参数解释**： 弹性负载均衡类型。 **取值范围**： Internal：独享型。 External：共享型。
        :type type: str
        :param admin_state_up: **参数解释**： 弹性负载均衡的管理状态。 **取值范围**： ACTIVE：使用中 PENDING_CREATE：创建中 ERROR：表示当前策略与同一监听器下的其他策略存在相同的规格配置。
        :type admin_state_up: bool
        :param bandwidth: **参数解释**： 带宽信息。 **取值范围**： 大于等于0的正整数。
        :type bandwidth: int
        :param vpc_id: **参数解释**： 虚拟私有云ID。 **取值范围**： 不涉及。
        :type vpc_id: str
        """
        
        

        self._id = None
        self._cluster_id = None
        self._name = None
        self._description = None
        self._vip_address = None
        self._vip_subnet_id = None
        self._tenant_id = None
        self._type = None
        self._admin_state_up = None
        self._bandwidth = None
        self._vpc_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if vip_address is not None:
            self.vip_address = vip_address
        if vip_subnet_id is not None:
            self.vip_subnet_id = vip_subnet_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if type is not None:
            self.type = type
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def id(self):
        r"""Gets the id of this ClusterElbInfo.

        **参数解释**： 弹性负载均衡ID。 **取值范围**： 不涉及。

        :return: The id of this ClusterElbInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ClusterElbInfo.

        **参数解释**： 弹性负载均衡ID。 **取值范围**： 不涉及。

        :param id: The id of this ClusterElbInfo.
        :type id: str
        """
        self._id = id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ClusterElbInfo.

        **参数解释**： 集群ID。 **取值范围**： 36位UUID。

        :return: The cluster_id of this ClusterElbInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ClusterElbInfo.

        **参数解释**： 集群ID。 **取值范围**： 36位UUID。

        :param cluster_id: The cluster_id of this ClusterElbInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def name(self):
        r"""Gets the name of this ClusterElbInfo.

        **参数解释**： 弹性负载均衡名称。 **取值范围**： 不涉及。

        :return: The name of this ClusterElbInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ClusterElbInfo.

        **参数解释**： 弹性负载均衡名称。 **取值范围**： 不涉及。

        :param name: The name of this ClusterElbInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ClusterElbInfo.

        **参数解释**： 弹性负载均衡描述。 **取值范围**： 不涉及。

        :return: The description of this ClusterElbInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ClusterElbInfo.

        **参数解释**： 弹性负载均衡描述。 **取值范围**： 不涉及。

        :param description: The description of this ClusterElbInfo.
        :type description: str
        """
        self._description = description

    @property
    def vip_address(self):
        r"""Gets the vip_address of this ClusterElbInfo.

        **参数解释**： 弹性负载均衡地址。 **取值范围**： 不涉及。

        :return: The vip_address of this ClusterElbInfo.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        r"""Sets the vip_address of this ClusterElbInfo.

        **参数解释**： 弹性负载均衡地址。 **取值范围**： 不涉及。

        :param vip_address: The vip_address of this ClusterElbInfo.
        :type vip_address: str
        """
        self._vip_address = vip_address

    @property
    def vip_subnet_id(self):
        r"""Gets the vip_subnet_id of this ClusterElbInfo.

        **参数解释**： 子网ID。 **取值范围**： 不涉及。

        :return: The vip_subnet_id of this ClusterElbInfo.
        :rtype: str
        """
        return self._vip_subnet_id

    @vip_subnet_id.setter
    def vip_subnet_id(self, vip_subnet_id):
        r"""Sets the vip_subnet_id of this ClusterElbInfo.

        **参数解释**： 子网ID。 **取值范围**： 不涉及。

        :param vip_subnet_id: The vip_subnet_id of this ClusterElbInfo.
        :type vip_subnet_id: str
        """
        self._vip_subnet_id = vip_subnet_id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ClusterElbInfo.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。

        :return: The tenant_id of this ClusterElbInfo.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ClusterElbInfo.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。

        :param tenant_id: The tenant_id of this ClusterElbInfo.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def type(self):
        r"""Gets the type of this ClusterElbInfo.

        **参数解释**： 弹性负载均衡类型。 **取值范围**： Internal：独享型。 External：共享型。

        :return: The type of this ClusterElbInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ClusterElbInfo.

        **参数解释**： 弹性负载均衡类型。 **取值范围**： Internal：独享型。 External：共享型。

        :param type: The type of this ClusterElbInfo.
        :type type: str
        """
        self._type = type

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this ClusterElbInfo.

        **参数解释**： 弹性负载均衡的管理状态。 **取值范围**： ACTIVE：使用中 PENDING_CREATE：创建中 ERROR：表示当前策略与同一监听器下的其他策略存在相同的规格配置。

        :return: The admin_state_up of this ClusterElbInfo.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this ClusterElbInfo.

        **参数解释**： 弹性负载均衡的管理状态。 **取值范围**： ACTIVE：使用中 PENDING_CREATE：创建中 ERROR：表示当前策略与同一监听器下的其他策略存在相同的规格配置。

        :param admin_state_up: The admin_state_up of this ClusterElbInfo.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this ClusterElbInfo.

        **参数解释**： 带宽信息。 **取值范围**： 大于等于0的正整数。

        :return: The bandwidth of this ClusterElbInfo.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this ClusterElbInfo.

        **参数解释**： 带宽信息。 **取值范围**： 大于等于0的正整数。

        :param bandwidth: The bandwidth of this ClusterElbInfo.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ClusterElbInfo.

        **参数解释**： 虚拟私有云ID。 **取值范围**： 不涉及。

        :return: The vpc_id of this ClusterElbInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ClusterElbInfo.

        **参数解释**： 虚拟私有云ID。 **取值范围**： 不涉及。

        :param vpc_id: The vpc_id of this ClusterElbInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, ClusterElbInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
