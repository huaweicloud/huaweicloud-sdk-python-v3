# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerLimits:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_image_meta': 'int',
        'max_personality': 'int',
        'max_personality_size': 'int',
        'max_security_group_rules': 'int',
        'max_security_groups': 'int',
        'max_server_group_members': 'int',
        'max_server_groups': 'int',
        'max_server_meta': 'int',
        'max_total_cores': 'int',
        'max_total_floating_ips': 'int',
        'max_total_instances': 'int',
        'max_total_keypairs': 'int',
        'max_total_ram_size': 'int',
        'total_cores_used': 'int',
        'total_floating_ips_used': 'int',
        'total_instances_used': 'int',
        'total_ram_used': 'int',
        'total_security_groups_used': 'int',
        'total_server_groups_used': 'int',
        'max_total_spot_instances': 'int',
        'max_total_spot_cores': 'int',
        'max_total_spot_ram_size': 'int',
        'total_spot_instances_used': 'int',
        'total_spot_cores_used': 'int',
        'total_spot_ram_used': 'int',
        'limit_by_flavor': 'list[ProjectFlavorLimit]'
    }

    attribute_map = {
        'max_image_meta': 'maxImageMeta',
        'max_personality': 'maxPersonality',
        'max_personality_size': 'maxPersonalitySize',
        'max_security_group_rules': 'maxSecurityGroupRules',
        'max_security_groups': 'maxSecurityGroups',
        'max_server_group_members': 'maxServerGroupMembers',
        'max_server_groups': 'maxServerGroups',
        'max_server_meta': 'maxServerMeta',
        'max_total_cores': 'maxTotalCores',
        'max_total_floating_ips': 'maxTotalFloatingIps',
        'max_total_instances': 'maxTotalInstances',
        'max_total_keypairs': 'maxTotalKeypairs',
        'max_total_ram_size': 'maxTotalRAMSize',
        'total_cores_used': 'totalCoresUsed',
        'total_floating_ips_used': 'totalFloatingIpsUsed',
        'total_instances_used': 'totalInstancesUsed',
        'total_ram_used': 'totalRAMUsed',
        'total_security_groups_used': 'totalSecurityGroupsUsed',
        'total_server_groups_used': 'totalServerGroupsUsed',
        'max_total_spot_instances': 'maxTotalSpotInstances',
        'max_total_spot_cores': 'maxTotalSpotCores',
        'max_total_spot_ram_size': 'maxTotalSpotRAMSize',
        'total_spot_instances_used': 'totalSpotInstancesUsed',
        'total_spot_cores_used': 'totalSpotCoresUsed',
        'total_spot_ram_used': 'totalSpotRAMUsed',
        'limit_by_flavor': 'limit_by_flavor'
    }

    def __init__(self, max_image_meta=None, max_personality=None, max_personality_size=None, max_security_group_rules=None, max_security_groups=None, max_server_group_members=None, max_server_groups=None, max_server_meta=None, max_total_cores=None, max_total_floating_ips=None, max_total_instances=None, max_total_keypairs=None, max_total_ram_size=None, total_cores_used=None, total_floating_ips_used=None, total_instances_used=None, total_ram_used=None, total_security_groups_used=None, total_server_groups_used=None, max_total_spot_instances=None, max_total_spot_cores=None, max_total_spot_ram_size=None, total_spot_instances_used=None, total_spot_cores_used=None, total_spot_ram_used=None, limit_by_flavor=None):
        r"""ServerLimits

        The model defined in huaweicloud sdk

        :param max_image_meta: 镜像元数据最大的长度。
        :type max_image_meta: int
        :param max_personality: 可注入文件的最大个数。
        :type max_personality: int
        :param max_personality_size: 注入文件内容的最大长度（单位：Byte）。
        :type max_personality_size: int
        :param max_security_group_rules: 安全组中安全组规则最大的配置个数。   &gt; 说明：  - 具体配额限制请以VPC配额限制为准。
        :type max_security_group_rules: int
        :param max_security_groups: 安全组最大使用个数。  &gt; 说明：  - 具体配额限制请以VPC配额限制为准。
        :type max_security_groups: int
        :param max_server_group_members: 服务器组中的最大虚拟机数。
        :type max_server_group_members: int
        :param max_server_groups: 服务器组的最大个数。
        :type max_server_groups: int
        :param max_server_meta: 可输入元数据的最大长度。
        :type max_server_meta: int
        :param max_total_cores: CPU核数最大申请数量。
        :type max_total_cores: int
        :param max_total_floating_ips: 最大的浮动IP使用个数。
        :type max_total_floating_ips: int
        :param max_total_instances: 云服务器最大申请数量。
        :type max_total_instances: int
        :param max_total_keypairs: 可以申请的SSH密钥对最大数量。
        :type max_total_keypairs: int
        :param max_total_ram_size: 内存最大申请容量（单位：MB）。
        :type max_total_ram_size: int
        :param total_cores_used: 当前已使用CPU核数。
        :type total_cores_used: int
        :param total_floating_ips_used: 当前浮动IP使用个数。
        :type total_floating_ips_used: int
        :param total_instances_used: 当前云服务器使用个数。
        :type total_instances_used: int
        :param total_ram_used: 当前内存使用容量（单位：MB）。
        :type total_ram_used: int
        :param total_security_groups_used: 当前安全组使用个数。
        :type total_security_groups_used: int
        :param total_server_groups_used: 已使用的服务器组个数。
        :type total_server_groups_used: int
        :param max_total_spot_instances: 竞价实例的最大申请数量。
        :type max_total_spot_instances: int
        :param max_total_spot_cores: 竞价实例的CPU核数最大申请数量。
        :type max_total_spot_cores: int
        :param max_total_spot_ram_size: 竞价实例的内存最大申请容量（单位：MB）。
        :type max_total_spot_ram_size: int
        :param total_spot_instances_used: 当前竞价实例的使用个数。
        :type total_spot_instances_used: int
        :param total_spot_cores_used: 当前竞价实例已使用的CPU核数。
        :type total_spot_cores_used: int
        :param total_spot_ram_used: 当前竞价实例的内存使用容量（单位：MB）。
        :type total_spot_ram_used: int
        :param limit_by_flavor: 使用该flavor可以申请的弹性云服务器数量。  值为“-1”时，表示无数量限制。
        :type limit_by_flavor: list[:class:`huaweicloudsdkecs.v2.ProjectFlavorLimit`]
        """
        
        

        self._max_image_meta = None
        self._max_personality = None
        self._max_personality_size = None
        self._max_security_group_rules = None
        self._max_security_groups = None
        self._max_server_group_members = None
        self._max_server_groups = None
        self._max_server_meta = None
        self._max_total_cores = None
        self._max_total_floating_ips = None
        self._max_total_instances = None
        self._max_total_keypairs = None
        self._max_total_ram_size = None
        self._total_cores_used = None
        self._total_floating_ips_used = None
        self._total_instances_used = None
        self._total_ram_used = None
        self._total_security_groups_used = None
        self._total_server_groups_used = None
        self._max_total_spot_instances = None
        self._max_total_spot_cores = None
        self._max_total_spot_ram_size = None
        self._total_spot_instances_used = None
        self._total_spot_cores_used = None
        self._total_spot_ram_used = None
        self._limit_by_flavor = None
        self.discriminator = None

        self.max_image_meta = max_image_meta
        self.max_personality = max_personality
        self.max_personality_size = max_personality_size
        self.max_security_group_rules = max_security_group_rules
        self.max_security_groups = max_security_groups
        self.max_server_group_members = max_server_group_members
        self.max_server_groups = max_server_groups
        self.max_server_meta = max_server_meta
        self.max_total_cores = max_total_cores
        self.max_total_floating_ips = max_total_floating_ips
        self.max_total_instances = max_total_instances
        self.max_total_keypairs = max_total_keypairs
        self.max_total_ram_size = max_total_ram_size
        self.total_cores_used = total_cores_used
        self.total_floating_ips_used = total_floating_ips_used
        self.total_instances_used = total_instances_used
        self.total_ram_used = total_ram_used
        self.total_security_groups_used = total_security_groups_used
        self.total_server_groups_used = total_server_groups_used
        if max_total_spot_instances is not None:
            self.max_total_spot_instances = max_total_spot_instances
        if max_total_spot_cores is not None:
            self.max_total_spot_cores = max_total_spot_cores
        if max_total_spot_ram_size is not None:
            self.max_total_spot_ram_size = max_total_spot_ram_size
        if total_spot_instances_used is not None:
            self.total_spot_instances_used = total_spot_instances_used
        if total_spot_cores_used is not None:
            self.total_spot_cores_used = total_spot_cores_used
        if total_spot_ram_used is not None:
            self.total_spot_ram_used = total_spot_ram_used
        if limit_by_flavor is not None:
            self.limit_by_flavor = limit_by_flavor

    @property
    def max_image_meta(self):
        r"""Gets the max_image_meta of this ServerLimits.

        镜像元数据最大的长度。

        :return: The max_image_meta of this ServerLimits.
        :rtype: int
        """
        return self._max_image_meta

    @max_image_meta.setter
    def max_image_meta(self, max_image_meta):
        r"""Sets the max_image_meta of this ServerLimits.

        镜像元数据最大的长度。

        :param max_image_meta: The max_image_meta of this ServerLimits.
        :type max_image_meta: int
        """
        self._max_image_meta = max_image_meta

    @property
    def max_personality(self):
        r"""Gets the max_personality of this ServerLimits.

        可注入文件的最大个数。

        :return: The max_personality of this ServerLimits.
        :rtype: int
        """
        return self._max_personality

    @max_personality.setter
    def max_personality(self, max_personality):
        r"""Sets the max_personality of this ServerLimits.

        可注入文件的最大个数。

        :param max_personality: The max_personality of this ServerLimits.
        :type max_personality: int
        """
        self._max_personality = max_personality

    @property
    def max_personality_size(self):
        r"""Gets the max_personality_size of this ServerLimits.

        注入文件内容的最大长度（单位：Byte）。

        :return: The max_personality_size of this ServerLimits.
        :rtype: int
        """
        return self._max_personality_size

    @max_personality_size.setter
    def max_personality_size(self, max_personality_size):
        r"""Sets the max_personality_size of this ServerLimits.

        注入文件内容的最大长度（单位：Byte）。

        :param max_personality_size: The max_personality_size of this ServerLimits.
        :type max_personality_size: int
        """
        self._max_personality_size = max_personality_size

    @property
    def max_security_group_rules(self):
        r"""Gets the max_security_group_rules of this ServerLimits.

        安全组中安全组规则最大的配置个数。   > 说明：  - 具体配额限制请以VPC配额限制为准。

        :return: The max_security_group_rules of this ServerLimits.
        :rtype: int
        """
        return self._max_security_group_rules

    @max_security_group_rules.setter
    def max_security_group_rules(self, max_security_group_rules):
        r"""Sets the max_security_group_rules of this ServerLimits.

        安全组中安全组规则最大的配置个数。   > 说明：  - 具体配额限制请以VPC配额限制为准。

        :param max_security_group_rules: The max_security_group_rules of this ServerLimits.
        :type max_security_group_rules: int
        """
        self._max_security_group_rules = max_security_group_rules

    @property
    def max_security_groups(self):
        r"""Gets the max_security_groups of this ServerLimits.

        安全组最大使用个数。  > 说明：  - 具体配额限制请以VPC配额限制为准。

        :return: The max_security_groups of this ServerLimits.
        :rtype: int
        """
        return self._max_security_groups

    @max_security_groups.setter
    def max_security_groups(self, max_security_groups):
        r"""Sets the max_security_groups of this ServerLimits.

        安全组最大使用个数。  > 说明：  - 具体配额限制请以VPC配额限制为准。

        :param max_security_groups: The max_security_groups of this ServerLimits.
        :type max_security_groups: int
        """
        self._max_security_groups = max_security_groups

    @property
    def max_server_group_members(self):
        r"""Gets the max_server_group_members of this ServerLimits.

        服务器组中的最大虚拟机数。

        :return: The max_server_group_members of this ServerLimits.
        :rtype: int
        """
        return self._max_server_group_members

    @max_server_group_members.setter
    def max_server_group_members(self, max_server_group_members):
        r"""Sets the max_server_group_members of this ServerLimits.

        服务器组中的最大虚拟机数。

        :param max_server_group_members: The max_server_group_members of this ServerLimits.
        :type max_server_group_members: int
        """
        self._max_server_group_members = max_server_group_members

    @property
    def max_server_groups(self):
        r"""Gets the max_server_groups of this ServerLimits.

        服务器组的最大个数。

        :return: The max_server_groups of this ServerLimits.
        :rtype: int
        """
        return self._max_server_groups

    @max_server_groups.setter
    def max_server_groups(self, max_server_groups):
        r"""Sets the max_server_groups of this ServerLimits.

        服务器组的最大个数。

        :param max_server_groups: The max_server_groups of this ServerLimits.
        :type max_server_groups: int
        """
        self._max_server_groups = max_server_groups

    @property
    def max_server_meta(self):
        r"""Gets the max_server_meta of this ServerLimits.

        可输入元数据的最大长度。

        :return: The max_server_meta of this ServerLimits.
        :rtype: int
        """
        return self._max_server_meta

    @max_server_meta.setter
    def max_server_meta(self, max_server_meta):
        r"""Sets the max_server_meta of this ServerLimits.

        可输入元数据的最大长度。

        :param max_server_meta: The max_server_meta of this ServerLimits.
        :type max_server_meta: int
        """
        self._max_server_meta = max_server_meta

    @property
    def max_total_cores(self):
        r"""Gets the max_total_cores of this ServerLimits.

        CPU核数最大申请数量。

        :return: The max_total_cores of this ServerLimits.
        :rtype: int
        """
        return self._max_total_cores

    @max_total_cores.setter
    def max_total_cores(self, max_total_cores):
        r"""Sets the max_total_cores of this ServerLimits.

        CPU核数最大申请数量。

        :param max_total_cores: The max_total_cores of this ServerLimits.
        :type max_total_cores: int
        """
        self._max_total_cores = max_total_cores

    @property
    def max_total_floating_ips(self):
        r"""Gets the max_total_floating_ips of this ServerLimits.

        最大的浮动IP使用个数。

        :return: The max_total_floating_ips of this ServerLimits.
        :rtype: int
        """
        return self._max_total_floating_ips

    @max_total_floating_ips.setter
    def max_total_floating_ips(self, max_total_floating_ips):
        r"""Sets the max_total_floating_ips of this ServerLimits.

        最大的浮动IP使用个数。

        :param max_total_floating_ips: The max_total_floating_ips of this ServerLimits.
        :type max_total_floating_ips: int
        """
        self._max_total_floating_ips = max_total_floating_ips

    @property
    def max_total_instances(self):
        r"""Gets the max_total_instances of this ServerLimits.

        云服务器最大申请数量。

        :return: The max_total_instances of this ServerLimits.
        :rtype: int
        """
        return self._max_total_instances

    @max_total_instances.setter
    def max_total_instances(self, max_total_instances):
        r"""Sets the max_total_instances of this ServerLimits.

        云服务器最大申请数量。

        :param max_total_instances: The max_total_instances of this ServerLimits.
        :type max_total_instances: int
        """
        self._max_total_instances = max_total_instances

    @property
    def max_total_keypairs(self):
        r"""Gets the max_total_keypairs of this ServerLimits.

        可以申请的SSH密钥对最大数量。

        :return: The max_total_keypairs of this ServerLimits.
        :rtype: int
        """
        return self._max_total_keypairs

    @max_total_keypairs.setter
    def max_total_keypairs(self, max_total_keypairs):
        r"""Sets the max_total_keypairs of this ServerLimits.

        可以申请的SSH密钥对最大数量。

        :param max_total_keypairs: The max_total_keypairs of this ServerLimits.
        :type max_total_keypairs: int
        """
        self._max_total_keypairs = max_total_keypairs

    @property
    def max_total_ram_size(self):
        r"""Gets the max_total_ram_size of this ServerLimits.

        内存最大申请容量（单位：MB）。

        :return: The max_total_ram_size of this ServerLimits.
        :rtype: int
        """
        return self._max_total_ram_size

    @max_total_ram_size.setter
    def max_total_ram_size(self, max_total_ram_size):
        r"""Sets the max_total_ram_size of this ServerLimits.

        内存最大申请容量（单位：MB）。

        :param max_total_ram_size: The max_total_ram_size of this ServerLimits.
        :type max_total_ram_size: int
        """
        self._max_total_ram_size = max_total_ram_size

    @property
    def total_cores_used(self):
        r"""Gets the total_cores_used of this ServerLimits.

        当前已使用CPU核数。

        :return: The total_cores_used of this ServerLimits.
        :rtype: int
        """
        return self._total_cores_used

    @total_cores_used.setter
    def total_cores_used(self, total_cores_used):
        r"""Sets the total_cores_used of this ServerLimits.

        当前已使用CPU核数。

        :param total_cores_used: The total_cores_used of this ServerLimits.
        :type total_cores_used: int
        """
        self._total_cores_used = total_cores_used

    @property
    def total_floating_ips_used(self):
        r"""Gets the total_floating_ips_used of this ServerLimits.

        当前浮动IP使用个数。

        :return: The total_floating_ips_used of this ServerLimits.
        :rtype: int
        """
        return self._total_floating_ips_used

    @total_floating_ips_used.setter
    def total_floating_ips_used(self, total_floating_ips_used):
        r"""Sets the total_floating_ips_used of this ServerLimits.

        当前浮动IP使用个数。

        :param total_floating_ips_used: The total_floating_ips_used of this ServerLimits.
        :type total_floating_ips_used: int
        """
        self._total_floating_ips_used = total_floating_ips_used

    @property
    def total_instances_used(self):
        r"""Gets the total_instances_used of this ServerLimits.

        当前云服务器使用个数。

        :return: The total_instances_used of this ServerLimits.
        :rtype: int
        """
        return self._total_instances_used

    @total_instances_used.setter
    def total_instances_used(self, total_instances_used):
        r"""Sets the total_instances_used of this ServerLimits.

        当前云服务器使用个数。

        :param total_instances_used: The total_instances_used of this ServerLimits.
        :type total_instances_used: int
        """
        self._total_instances_used = total_instances_used

    @property
    def total_ram_used(self):
        r"""Gets the total_ram_used of this ServerLimits.

        当前内存使用容量（单位：MB）。

        :return: The total_ram_used of this ServerLimits.
        :rtype: int
        """
        return self._total_ram_used

    @total_ram_used.setter
    def total_ram_used(self, total_ram_used):
        r"""Sets the total_ram_used of this ServerLimits.

        当前内存使用容量（单位：MB）。

        :param total_ram_used: The total_ram_used of this ServerLimits.
        :type total_ram_used: int
        """
        self._total_ram_used = total_ram_used

    @property
    def total_security_groups_used(self):
        r"""Gets the total_security_groups_used of this ServerLimits.

        当前安全组使用个数。

        :return: The total_security_groups_used of this ServerLimits.
        :rtype: int
        """
        return self._total_security_groups_used

    @total_security_groups_used.setter
    def total_security_groups_used(self, total_security_groups_used):
        r"""Sets the total_security_groups_used of this ServerLimits.

        当前安全组使用个数。

        :param total_security_groups_used: The total_security_groups_used of this ServerLimits.
        :type total_security_groups_used: int
        """
        self._total_security_groups_used = total_security_groups_used

    @property
    def total_server_groups_used(self):
        r"""Gets the total_server_groups_used of this ServerLimits.

        已使用的服务器组个数。

        :return: The total_server_groups_used of this ServerLimits.
        :rtype: int
        """
        return self._total_server_groups_used

    @total_server_groups_used.setter
    def total_server_groups_used(self, total_server_groups_used):
        r"""Sets the total_server_groups_used of this ServerLimits.

        已使用的服务器组个数。

        :param total_server_groups_used: The total_server_groups_used of this ServerLimits.
        :type total_server_groups_used: int
        """
        self._total_server_groups_used = total_server_groups_used

    @property
    def max_total_spot_instances(self):
        r"""Gets the max_total_spot_instances of this ServerLimits.

        竞价实例的最大申请数量。

        :return: The max_total_spot_instances of this ServerLimits.
        :rtype: int
        """
        return self._max_total_spot_instances

    @max_total_spot_instances.setter
    def max_total_spot_instances(self, max_total_spot_instances):
        r"""Sets the max_total_spot_instances of this ServerLimits.

        竞价实例的最大申请数量。

        :param max_total_spot_instances: The max_total_spot_instances of this ServerLimits.
        :type max_total_spot_instances: int
        """
        self._max_total_spot_instances = max_total_spot_instances

    @property
    def max_total_spot_cores(self):
        r"""Gets the max_total_spot_cores of this ServerLimits.

        竞价实例的CPU核数最大申请数量。

        :return: The max_total_spot_cores of this ServerLimits.
        :rtype: int
        """
        return self._max_total_spot_cores

    @max_total_spot_cores.setter
    def max_total_spot_cores(self, max_total_spot_cores):
        r"""Sets the max_total_spot_cores of this ServerLimits.

        竞价实例的CPU核数最大申请数量。

        :param max_total_spot_cores: The max_total_spot_cores of this ServerLimits.
        :type max_total_spot_cores: int
        """
        self._max_total_spot_cores = max_total_spot_cores

    @property
    def max_total_spot_ram_size(self):
        r"""Gets the max_total_spot_ram_size of this ServerLimits.

        竞价实例的内存最大申请容量（单位：MB）。

        :return: The max_total_spot_ram_size of this ServerLimits.
        :rtype: int
        """
        return self._max_total_spot_ram_size

    @max_total_spot_ram_size.setter
    def max_total_spot_ram_size(self, max_total_spot_ram_size):
        r"""Sets the max_total_spot_ram_size of this ServerLimits.

        竞价实例的内存最大申请容量（单位：MB）。

        :param max_total_spot_ram_size: The max_total_spot_ram_size of this ServerLimits.
        :type max_total_spot_ram_size: int
        """
        self._max_total_spot_ram_size = max_total_spot_ram_size

    @property
    def total_spot_instances_used(self):
        r"""Gets the total_spot_instances_used of this ServerLimits.

        当前竞价实例的使用个数。

        :return: The total_spot_instances_used of this ServerLimits.
        :rtype: int
        """
        return self._total_spot_instances_used

    @total_spot_instances_used.setter
    def total_spot_instances_used(self, total_spot_instances_used):
        r"""Sets the total_spot_instances_used of this ServerLimits.

        当前竞价实例的使用个数。

        :param total_spot_instances_used: The total_spot_instances_used of this ServerLimits.
        :type total_spot_instances_used: int
        """
        self._total_spot_instances_used = total_spot_instances_used

    @property
    def total_spot_cores_used(self):
        r"""Gets the total_spot_cores_used of this ServerLimits.

        当前竞价实例已使用的CPU核数。

        :return: The total_spot_cores_used of this ServerLimits.
        :rtype: int
        """
        return self._total_spot_cores_used

    @total_spot_cores_used.setter
    def total_spot_cores_used(self, total_spot_cores_used):
        r"""Sets the total_spot_cores_used of this ServerLimits.

        当前竞价实例已使用的CPU核数。

        :param total_spot_cores_used: The total_spot_cores_used of this ServerLimits.
        :type total_spot_cores_used: int
        """
        self._total_spot_cores_used = total_spot_cores_used

    @property
    def total_spot_ram_used(self):
        r"""Gets the total_spot_ram_used of this ServerLimits.

        当前竞价实例的内存使用容量（单位：MB）。

        :return: The total_spot_ram_used of this ServerLimits.
        :rtype: int
        """
        return self._total_spot_ram_used

    @total_spot_ram_used.setter
    def total_spot_ram_used(self, total_spot_ram_used):
        r"""Sets the total_spot_ram_used of this ServerLimits.

        当前竞价实例的内存使用容量（单位：MB）。

        :param total_spot_ram_used: The total_spot_ram_used of this ServerLimits.
        :type total_spot_ram_used: int
        """
        self._total_spot_ram_used = total_spot_ram_used

    @property
    def limit_by_flavor(self):
        r"""Gets the limit_by_flavor of this ServerLimits.

        使用该flavor可以申请的弹性云服务器数量。  值为“-1”时，表示无数量限制。

        :return: The limit_by_flavor of this ServerLimits.
        :rtype: list[:class:`huaweicloudsdkecs.v2.ProjectFlavorLimit`]
        """
        return self._limit_by_flavor

    @limit_by_flavor.setter
    def limit_by_flavor(self, limit_by_flavor):
        r"""Sets the limit_by_flavor of this ServerLimits.

        使用该flavor可以申请的弹性云服务器数量。  值为“-1”时，表示无数量限制。

        :param limit_by_flavor: The limit_by_flavor of this ServerLimits.
        :type limit_by_flavor: list[:class:`huaweicloudsdkecs.v2.ProjectFlavorLimit`]
        """
        self._limit_by_flavor = limit_by_flavor

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
        if not isinstance(other, ServerLimits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
