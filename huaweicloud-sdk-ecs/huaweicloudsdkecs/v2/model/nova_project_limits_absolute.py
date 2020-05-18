# coding: utf-8

import pprint
import re

import six


class NovaProjectLimitsAbsolute(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'max_server_meta': 'str',
        'max_personality': 'str',
        'total_server_groups_used': 'str',
        'max_image_meta': 'str',
        'max_personality_size': 'str',
        'max_total_ram_size': 'str',
        'max_total_keypairs': 'str',
        'max_security_group_rules': 'str',
        'max_server_groups': 'str',
        'total_cores_used': 'str',
        'total_ram_used': 'str',
        'max_security_groups': 'str',
        'total_instances_used': 'str',
        'total_security_groups_used': 'str',
        'max_total_floating_ips': 'str',
        'total_floating_ips_used': 'str',
        'max_total_instances': 'str',
        'max_total_cores': 'str',
        'max_server_group_members': 'str'
    }

    attribute_map = {
        'max_server_meta': 'maxServerMeta',
        'max_personality': 'maxPersonality',
        'total_server_groups_used': 'totalServerGroupsUsed',
        'max_image_meta': 'maxImageMeta',
        'max_personality_size': 'maxPersonalitySize',
        'max_total_ram_size': 'maxTotalRAMSize',
        'max_total_keypairs': 'maxTotalKeypairs',
        'max_security_group_rules': 'maxSecurityGroupRules',
        'max_server_groups': 'maxServerGroups',
        'total_cores_used': 'totalCoresUsed',
        'total_ram_used': 'totalRAMUsed',
        'max_security_groups': 'maxSecurityGroups',
        'total_instances_used': 'totalInstancesUsed',
        'total_security_groups_used': 'totalSecurityGroupsUsed',
        'max_total_floating_ips': 'maxTotalFloatingIps',
        'total_floating_ips_used': 'totalFloatingIpsUsed',
        'max_total_instances': 'maxTotalInstances',
        'max_total_cores': 'maxTotalCores',
        'max_server_group_members': 'maxServerGroupMembers'
    }

    def __init__(self, max_server_meta=None, max_personality=None, total_server_groups_used=None, max_image_meta=None, max_personality_size=None, max_total_ram_size=None, max_total_keypairs=None, max_security_group_rules=None, max_server_groups=None, total_cores_used=None, total_ram_used=None, max_security_groups=None, total_instances_used=None, total_security_groups_used=None, max_total_floating_ips=None, total_floating_ips_used=None, max_total_instances=None, max_total_cores=None, max_server_group_members=None):  # noqa: E501
        """NovaProjectLimitsAbsolute - a model defined in huaweicloud sdk"""

        self._max_server_meta = None
        self._max_personality = None
        self._total_server_groups_used = None
        self._max_image_meta = None
        self._max_personality_size = None
        self._max_total_ram_size = None
        self._max_total_keypairs = None
        self._max_security_group_rules = None
        self._max_server_groups = None
        self._total_cores_used = None
        self._total_ram_used = None
        self._max_security_groups = None
        self._total_instances_used = None
        self._total_security_groups_used = None
        self._max_total_floating_ips = None
        self._total_floating_ips_used = None
        self._max_total_instances = None
        self._max_total_cores = None
        self._max_server_group_members = None
        self.discriminator = None

        self.max_server_meta = max_server_meta
        self.max_personality = max_personality
        self.total_server_groups_used = total_server_groups_used
        self.max_image_meta = max_image_meta
        self.max_personality_size = max_personality_size
        self.max_total_ram_size = max_total_ram_size
        self.max_total_keypairs = max_total_keypairs
        self.max_security_group_rules = max_security_group_rules
        self.max_server_groups = max_server_groups
        self.total_cores_used = total_cores_used
        self.total_ram_used = total_ram_used
        self.max_security_groups = max_security_groups
        self.total_instances_used = total_instances_used
        self.total_security_groups_used = total_security_groups_used
        self.max_total_floating_ips = max_total_floating_ips
        self.total_floating_ips_used = total_floating_ips_used
        self.max_total_instances = max_total_instances
        self.max_total_cores = max_total_cores
        self.max_server_group_members = max_server_group_members

    @property
    def max_server_meta(self):
        """Gets the max_server_meta of this NovaProjectLimitsAbsolute.

        云服务器元数据数量限制。  值为“-1”时，表示无数量限制。

        :return: The max_server_meta of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._max_server_meta

    @max_server_meta.setter
    def max_server_meta(self, max_server_meta):
        """Sets the max_server_meta of this NovaProjectLimitsAbsolute.

        云服务器元数据数量限制。  值为“-1”时，表示无数量限制。

        :param max_server_meta: The max_server_meta of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._max_server_meta = max_server_meta

    @property
    def max_personality(self):
        """Gets the max_personality of this NovaProjectLimitsAbsolute.

        注入文件数量限制。  值为“-1”时，表示无数量限制。

        :return: The max_personality of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._max_personality

    @max_personality.setter
    def max_personality(self, max_personality):
        """Sets the max_personality of this NovaProjectLimitsAbsolute.

        注入文件数量限制。  值为“-1”时，表示无数量限制。

        :param max_personality: The max_personality of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._max_personality = max_personality

    @property
    def total_server_groups_used(self):
        """Gets the total_server_groups_used of this NovaProjectLimitsAbsolute.

        已使用的云服务器组数量。

        :return: The total_server_groups_used of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._total_server_groups_used

    @total_server_groups_used.setter
    def total_server_groups_used(self, total_server_groups_used):
        """Sets the total_server_groups_used of this NovaProjectLimitsAbsolute.

        已使用的云服务器组数量。

        :param total_server_groups_used: The total_server_groups_used of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._total_server_groups_used = total_server_groups_used

    @property
    def max_image_meta(self):
        """Gets the max_image_meta of this NovaProjectLimitsAbsolute.

        镜像元数据数量限制。  值为“-1”时，表示无数量限制。

        :return: The max_image_meta of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._max_image_meta

    @max_image_meta.setter
    def max_image_meta(self, max_image_meta):
        """Sets the max_image_meta of this NovaProjectLimitsAbsolute.

        镜像元数据数量限制。  值为“-1”时，表示无数量限制。

        :param max_image_meta: The max_image_meta of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._max_image_meta = max_image_meta

    @property
    def max_personality_size(self):
        """Gets the max_personality_size of this NovaProjectLimitsAbsolute.

        注入文件大小限制。  值为“-1”时，表示无大小限制。

        :return: The max_personality_size of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._max_personality_size

    @max_personality_size.setter
    def max_personality_size(self, max_personality_size):
        """Sets the max_personality_size of this NovaProjectLimitsAbsolute.

        注入文件大小限制。  值为“-1”时，表示无大小限制。

        :param max_personality_size: The max_personality_size of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._max_personality_size = max_personality_size

    @property
    def max_total_ram_size(self):
        """Gets the max_total_ram_size of this NovaProjectLimitsAbsolute.

        总内存大小限制。  值为“-1”时，表示无大小限制。

        :return: The max_total_ram_size of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._max_total_ram_size

    @max_total_ram_size.setter
    def max_total_ram_size(self, max_total_ram_size):
        """Sets the max_total_ram_size of this NovaProjectLimitsAbsolute.

        总内存大小限制。  值为“-1”时，表示无大小限制。

        :param max_total_ram_size: The max_total_ram_size of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._max_total_ram_size = max_total_ram_size

    @property
    def max_total_keypairs(self):
        """Gets the max_total_keypairs of this NovaProjectLimitsAbsolute.

        keypair数量限制。  值为“-1”时，表示无数量限制。

        :return: The max_total_keypairs of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._max_total_keypairs

    @max_total_keypairs.setter
    def max_total_keypairs(self, max_total_keypairs):
        """Sets the max_total_keypairs of this NovaProjectLimitsAbsolute.

        keypair数量限制。  值为“-1”时，表示无数量限制。

        :param max_total_keypairs: The max_total_keypairs of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._max_total_keypairs = max_total_keypairs

    @property
    def max_security_group_rules(self):
        """Gets the max_security_group_rules of this NovaProjectLimitsAbsolute.

          安全组规则数量限制。  值为“-1”时，表示无数量限制。  在微版本2.35后不支持。

        :return: The max_security_group_rules of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._max_security_group_rules

    @max_security_group_rules.setter
    def max_security_group_rules(self, max_security_group_rules):
        """Sets the max_security_group_rules of this NovaProjectLimitsAbsolute.

          安全组规则数量限制。  值为“-1”时，表示无数量限制。  在微版本2.35后不支持。

        :param max_security_group_rules: The max_security_group_rules of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._max_security_group_rules = max_security_group_rules

    @property
    def max_server_groups(self):
        """Gets the max_server_groups of this NovaProjectLimitsAbsolute.

        云服务器组数量限制。  值为“-1”时，表示无数量限制。

        :return: The max_server_groups of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._max_server_groups

    @max_server_groups.setter
    def max_server_groups(self, max_server_groups):
        """Sets the max_server_groups of this NovaProjectLimitsAbsolute.

        云服务器组数量限制。  值为“-1”时，表示无数量限制。

        :param max_server_groups: The max_server_groups of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._max_server_groups = max_server_groups

    @property
    def total_cores_used(self):
        """Gets the total_cores_used of this NovaProjectLimitsAbsolute.

        已使用的核数。

        :return: The total_cores_used of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._total_cores_used

    @total_cores_used.setter
    def total_cores_used(self, total_cores_used):
        """Sets the total_cores_used of this NovaProjectLimitsAbsolute.

        已使用的核数。

        :param total_cores_used: The total_cores_used of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._total_cores_used = total_cores_used

    @property
    def total_ram_used(self):
        """Gets the total_ram_used of this NovaProjectLimitsAbsolute.

        已使用的内存大小。

        :return: The total_ram_used of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._total_ram_used

    @total_ram_used.setter
    def total_ram_used(self, total_ram_used):
        """Sets the total_ram_used of this NovaProjectLimitsAbsolute.

        已使用的内存大小。

        :param total_ram_used: The total_ram_used of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._total_ram_used = total_ram_used

    @property
    def max_security_groups(self):
        """Gets the max_security_groups of this NovaProjectLimitsAbsolute.

        安全组数量限制。  值为“-1”时，表示无数量限制。

        :return: The max_security_groups of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._max_security_groups

    @max_security_groups.setter
    def max_security_groups(self, max_security_groups):
        """Sets the max_security_groups of this NovaProjectLimitsAbsolute.

        安全组数量限制。  值为“-1”时，表示无数量限制。

        :param max_security_groups: The max_security_groups of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._max_security_groups = max_security_groups

    @property
    def total_instances_used(self):
        """Gets the total_instances_used of this NovaProjectLimitsAbsolute.

        已使用的弹性云服务器数量。

        :return: The total_instances_used of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._total_instances_used

    @total_instances_used.setter
    def total_instances_used(self, total_instances_used):
        """Sets the total_instances_used of this NovaProjectLimitsAbsolute.

        已使用的弹性云服务器数量。

        :param total_instances_used: The total_instances_used of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._total_instances_used = total_instances_used

    @property
    def total_security_groups_used(self):
        """Gets the total_security_groups_used of this NovaProjectLimitsAbsolute.

        已使用的安全组数量。

        :return: The total_security_groups_used of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._total_security_groups_used

    @total_security_groups_used.setter
    def total_security_groups_used(self, total_security_groups_used):
        """Sets the total_security_groups_used of this NovaProjectLimitsAbsolute.

        已使用的安全组数量。

        :param total_security_groups_used: The total_security_groups_used of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._total_security_groups_used = total_security_groups_used

    @property
    def max_total_floating_ips(self):
        """Gets the max_total_floating_ips of this NovaProjectLimitsAbsolute.

        浮动IP数量限制。  值为“-1”时，表示无数量限制。

        :return: The max_total_floating_ips of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._max_total_floating_ips

    @max_total_floating_ips.setter
    def max_total_floating_ips(self, max_total_floating_ips):
        """Sets the max_total_floating_ips of this NovaProjectLimitsAbsolute.

        浮动IP数量限制。  值为“-1”时，表示无数量限制。

        :param max_total_floating_ips: The max_total_floating_ips of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._max_total_floating_ips = max_total_floating_ips

    @property
    def total_floating_ips_used(self):
        """Gets the total_floating_ips_used of this NovaProjectLimitsAbsolute.

        已使用的浮动IP数量。

        :return: The total_floating_ips_used of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._total_floating_ips_used

    @total_floating_ips_used.setter
    def total_floating_ips_used(self, total_floating_ips_used):
        """Sets the total_floating_ips_used of this NovaProjectLimitsAbsolute.

        已使用的浮动IP数量。

        :param total_floating_ips_used: The total_floating_ips_used of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._total_floating_ips_used = total_floating_ips_used

    @property
    def max_total_instances(self):
        """Gets the max_total_instances of this NovaProjectLimitsAbsolute.

        云服务器数量限制。  值为“-1”时，表示无数量限制。

        :return: The max_total_instances of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._max_total_instances

    @max_total_instances.setter
    def max_total_instances(self, max_total_instances):
        """Sets the max_total_instances of this NovaProjectLimitsAbsolute.

        云服务器数量限制。  值为“-1”时，表示无数量限制。

        :param max_total_instances: The max_total_instances of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._max_total_instances = max_total_instances

    @property
    def max_total_cores(self):
        """Gets the max_total_cores of this NovaProjectLimitsAbsolute.

        总核数限制。  值为“-1”时，表示无数量限制。

        :return: The max_total_cores of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._max_total_cores

    @max_total_cores.setter
    def max_total_cores(self, max_total_cores):
        """Sets the max_total_cores of this NovaProjectLimitsAbsolute.

        总核数限制。  值为“-1”时，表示无数量限制。

        :param max_total_cores: The max_total_cores of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._max_total_cores = max_total_cores

    @property
    def max_server_group_members(self):
        """Gets the max_server_group_members of this NovaProjectLimitsAbsolute.

        云服务器组成员数量限制。  值为“-1”时，表示无数量限制。

        :return: The max_server_group_members of this NovaProjectLimitsAbsolute.
        :rtype: str
        """
        return self._max_server_group_members

    @max_server_group_members.setter
    def max_server_group_members(self, max_server_group_members):
        """Sets the max_server_group_members of this NovaProjectLimitsAbsolute.

        云服务器组成员数量限制。  值为“-1”时，表示无数量限制。

        :param max_server_group_members: The max_server_group_members of this NovaProjectLimitsAbsolute.
        :type: str
        """
        self._max_server_group_members = max_server_group_members

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
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NovaProjectLimitsAbsolute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
