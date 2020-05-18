# coding: utf-8

import pprint
import re

import six


class NovaQuotaSet(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'cores': 'int',
        'fixed_ips': 'int',
        'floating_ips': 'int',
        'id': 'str',
        'injected_file_content_bytes': 'int',
        'injected_file_path_bytes': 'int',
        'injected_files': 'int',
        'instances': 'int',
        'key_pairs': 'int',
        'metadata_items': 'int',
        'ram': 'int',
        'security_group_rules': 'int',
        'security_groups': 'int',
        'server_group_members': 'int',
        'server_groups': 'int'
    }

    attribute_map = {
        'cores': 'cores',
        'fixed_ips': 'fixed_ips',
        'floating_ips': 'floating_ips',
        'id': 'id',
        'injected_file_content_bytes': 'injected_file_content_bytes',
        'injected_file_path_bytes': 'injected_file_path_bytes',
        'injected_files': 'injected_files',
        'instances': 'instances',
        'key_pairs': 'key_pairs',
        'metadata_items': 'metadata_items',
        'ram': 'ram',
        'security_group_rules': 'security_group_rules',
        'security_groups': 'security_groups',
        'server_group_members': 'server_group_members',
        'server_groups': 'server_groups'
    }

    def __init__(self, cores=None, fixed_ips=None, floating_ips=None, id=None, injected_file_content_bytes=None, injected_file_path_bytes=None, injected_files=None, instances=None, key_pairs=None, metadata_items=None, ram=None, security_group_rules=None, security_groups=None, server_group_members=None, server_groups=None):  # noqa: E501
        """NovaQuotaSet - a model defined in huaweicloud sdk"""

        self._cores = None
        self._fixed_ips = None
        self._floating_ips = None
        self._id = None
        self._injected_file_content_bytes = None
        self._injected_file_path_bytes = None
        self._injected_files = None
        self._instances = None
        self._key_pairs = None
        self._metadata_items = None
        self._ram = None
        self._security_group_rules = None
        self._security_groups = None
        self._server_group_members = None
        self._server_groups = None
        self.discriminator = None

        self.cores = cores
        self.fixed_ips = fixed_ips
        self.floating_ips = floating_ips
        self.id = id
        self.injected_file_content_bytes = injected_file_content_bytes
        self.injected_file_path_bytes = injected_file_path_bytes
        self.injected_files = injected_files
        self.instances = instances
        self.key_pairs = key_pairs
        self.metadata_items = metadata_items
        self.ram = ram
        self.security_group_rules = security_group_rules
        self.security_groups = security_groups
        self.server_group_members = server_group_members
        self.server_groups = server_groups

    @property
    def cores(self):
        """Gets the cores of this NovaQuotaSet.

        vcpu数量配额。

        :return: The cores of this NovaQuotaSet.
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this NovaQuotaSet.

        vcpu数量配额。

        :param cores: The cores of this NovaQuotaSet.
        :type: int
        """
        self._cores = cores

    @property
    def fixed_ips(self):
        """Gets the fixed_ips of this NovaQuotaSet.

        固定IP数量配额，目前不支持此参数。

        :return: The fixed_ips of this NovaQuotaSet.
        :rtype: int
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        """Sets the fixed_ips of this NovaQuotaSet.

        固定IP数量配额，目前不支持此参数。

        :param fixed_ips: The fixed_ips of this NovaQuotaSet.
        :type: int
        """
        self._fixed_ips = fixed_ips

    @property
    def floating_ips(self):
        """Gets the floating_ips of this NovaQuotaSet.

        浮动IP数量配额，目前不支持此参数。

        :return: The floating_ips of this NovaQuotaSet.
        :rtype: int
        """
        return self._floating_ips

    @floating_ips.setter
    def floating_ips(self, floating_ips):
        """Sets the floating_ips of this NovaQuotaSet.

        浮动IP数量配额，目前不支持此参数。

        :param floating_ips: The floating_ips of this NovaQuotaSet.
        :type: int
        """
        self._floating_ips = floating_ips

    @property
    def id(self):
        """Gets the id of this NovaQuotaSet.

        project的UUID。

        :return: The id of this NovaQuotaSet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaQuotaSet.

        project的UUID。

        :param id: The id of this NovaQuotaSet.
        :type: str
        """
        self._id = id

    @property
    def injected_file_content_bytes(self):
        """Gets the injected_file_content_bytes of this NovaQuotaSet.

        注入文件的文件大小配额，单位字节。

        :return: The injected_file_content_bytes of this NovaQuotaSet.
        :rtype: int
        """
        return self._injected_file_content_bytes

    @injected_file_content_bytes.setter
    def injected_file_content_bytes(self, injected_file_content_bytes):
        """Sets the injected_file_content_bytes of this NovaQuotaSet.

        注入文件的文件大小配额，单位字节。

        :param injected_file_content_bytes: The injected_file_content_bytes of this NovaQuotaSet.
        :type: int
        """
        self._injected_file_content_bytes = injected_file_content_bytes

    @property
    def injected_file_path_bytes(self):
        """Gets the injected_file_path_bytes of this NovaQuotaSet.

        注入文件的路径大小配额，单位字节。

        :return: The injected_file_path_bytes of this NovaQuotaSet.
        :rtype: int
        """
        return self._injected_file_path_bytes

    @injected_file_path_bytes.setter
    def injected_file_path_bytes(self, injected_file_path_bytes):
        """Sets the injected_file_path_bytes of this NovaQuotaSet.

        注入文件的路径大小配额，单位字节。

        :param injected_file_path_bytes: The injected_file_path_bytes of this NovaQuotaSet.
        :type: int
        """
        self._injected_file_path_bytes = injected_file_path_bytes

    @property
    def injected_files(self):
        """Gets the injected_files of this NovaQuotaSet.

        注入文件数量配额。

        :return: The injected_files of this NovaQuotaSet.
        :rtype: int
        """
        return self._injected_files

    @injected_files.setter
    def injected_files(self, injected_files):
        """Sets the injected_files of this NovaQuotaSet.

        注入文件数量配额。

        :param injected_files: The injected_files of this NovaQuotaSet.
        :type: int
        """
        self._injected_files = injected_files

    @property
    def instances(self):
        """Gets the instances of this NovaQuotaSet.

        云服务器数量配额。

        :return: The instances of this NovaQuotaSet.
        :rtype: int
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this NovaQuotaSet.

        云服务器数量配额。

        :param instances: The instances of this NovaQuotaSet.
        :type: int
        """
        self._instances = instances

    @property
    def key_pairs(self):
        """Gets the key_pairs of this NovaQuotaSet.

        密钥对数量配额，目前不支持此参数。

        :return: The key_pairs of this NovaQuotaSet.
        :rtype: int
        """
        return self._key_pairs

    @key_pairs.setter
    def key_pairs(self, key_pairs):
        """Sets the key_pairs of this NovaQuotaSet.

        密钥对数量配额，目前不支持此参数。

        :param key_pairs: The key_pairs of this NovaQuotaSet.
        :type: int
        """
        self._key_pairs = key_pairs

    @property
    def metadata_items(self):
        """Gets the metadata_items of this NovaQuotaSet.

        元数据数量配额。

        :return: The metadata_items of this NovaQuotaSet.
        :rtype: int
        """
        return self._metadata_items

    @metadata_items.setter
    def metadata_items(self, metadata_items):
        """Sets the metadata_items of this NovaQuotaSet.

        元数据数量配额。

        :param metadata_items: The metadata_items of this NovaQuotaSet.
        :type: int
        """
        self._metadata_items = metadata_items

    @property
    def ram(self):
        """Gets the ram of this NovaQuotaSet.

        内存配额，单位MB。

        :return: The ram of this NovaQuotaSet.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this NovaQuotaSet.

        内存配额，单位MB。

        :param ram: The ram of this NovaQuotaSet.
        :type: int
        """
        self._ram = ram

    @property
    def security_group_rules(self):
        """Gets the security_group_rules of this NovaQuotaSet.

        每个安全组的规则配额，目前不支持此参数。

        :return: The security_group_rules of this NovaQuotaSet.
        :rtype: int
        """
        return self._security_group_rules

    @security_group_rules.setter
    def security_group_rules(self, security_group_rules):
        """Sets the security_group_rules of this NovaQuotaSet.

        每个安全组的规则配额，目前不支持此参数。

        :param security_group_rules: The security_group_rules of this NovaQuotaSet.
        :type: int
        """
        self._security_group_rules = security_group_rules

    @property
    def security_groups(self):
        """Gets the security_groups of this NovaQuotaSet.

        安全组数量配额，目前不支持此参数。

        :return: The security_groups of this NovaQuotaSet.
        :rtype: int
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this NovaQuotaSet.

        安全组数量配额，目前不支持此参数。

        :param security_groups: The security_groups of this NovaQuotaSet.
        :type: int
        """
        self._security_groups = security_groups

    @property
    def server_group_members(self):
        """Gets the server_group_members of this NovaQuotaSet.

        云服务器组大小配额。

        :return: The server_group_members of this NovaQuotaSet.
        :rtype: int
        """
        return self._server_group_members

    @server_group_members.setter
    def server_group_members(self, server_group_members):
        """Sets the server_group_members of this NovaQuotaSet.

        云服务器组大小配额。

        :param server_group_members: The server_group_members of this NovaQuotaSet.
        :type: int
        """
        self._server_group_members = server_group_members

    @property
    def server_groups(self):
        """Gets the server_groups of this NovaQuotaSet.

        云服务器组数量配额。

        :return: The server_groups of this NovaQuotaSet.
        :rtype: int
        """
        return self._server_groups

    @server_groups.setter
    def server_groups(self, server_groups):
        """Sets the server_groups of this NovaQuotaSet.

        云服务器组数量配额。

        :param server_groups: The server_groups of this NovaQuotaSet.
        :type: int
        """
        self._server_groups = server_groups

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
        if not isinstance(other, NovaQuotaSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
