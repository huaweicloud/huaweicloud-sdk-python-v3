# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_name': 'str',
        'provider': 'str',
        'resource_level_name': 'str',
        'critical_level': 'str',
        'config_protection': 'bool',
        'backup_compliance': 'str',
        'local_vault_name': 'str',
        'remote_vault_name': 'str',
        'region_id': 'str',
        'create_time': 'str',
        'last_inventory_time': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'provider': 'provider',
        'resource_level_name': 'resource_level_name',
        'critical_level': 'critical_level',
        'config_protection': 'config_protection',
        'backup_compliance': 'backup_compliance',
        'local_vault_name': 'local_vault_name',
        'remote_vault_name': 'remote_vault_name',
        'region_id': 'region_id',
        'create_time': 'create_time',
        'last_inventory_time': 'last_inventory_time'
    }

    def __init__(self, resource_id=None, resource_name=None, provider=None, resource_level_name=None, critical_level=None, config_protection=None, backup_compliance=None, local_vault_name=None, remote_vault_name=None, region_id=None, create_time=None, last_inventory_time=None):
        r"""ResourceEntity

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param provider: 资源类型
        :type provider: str
        :param resource_level_name: 资源等级名称
        :type resource_level_name: str
        :param critical_level: 重要程度
        :type critical_level: str
        :param config_protection: 是否配置保护
        :type config_protection: bool
        :param backup_compliance: 备份合规性
        :type backup_compliance: str
        :param local_vault_name: 本地备份存储库名称
        :type local_vault_name: str
        :param remote_vault_name: 异地备份存储库名称
        :type remote_vault_name: str
        :param region_id: 资源归属区域
        :type region_id: str
        :param create_time: 资源创建时间
        :type create_time: str
        :param last_inventory_time: 上次盘点时间
        :type last_inventory_time: str
        """
        
        

        self._resource_id = None
        self._resource_name = None
        self._provider = None
        self._resource_level_name = None
        self._critical_level = None
        self._config_protection = None
        self._backup_compliance = None
        self._local_vault_name = None
        self._remote_vault_name = None
        self._region_id = None
        self._create_time = None
        self._last_inventory_time = None
        self.discriminator = None

        self.resource_id = resource_id
        self.resource_name = resource_name
        self.provider = provider
        if resource_level_name is not None:
            self.resource_level_name = resource_level_name
        if critical_level is not None:
            self.critical_level = critical_level
        self.config_protection = config_protection
        if backup_compliance is not None:
            self.backup_compliance = backup_compliance
        if local_vault_name is not None:
            self.local_vault_name = local_vault_name
        if remote_vault_name is not None:
            self.remote_vault_name = remote_vault_name
        self.region_id = region_id
        self.create_time = create_time
        self.last_inventory_time = last_inventory_time

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ResourceEntity.

        资源ID

        :return: The resource_id of this ResourceEntity.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ResourceEntity.

        资源ID

        :param resource_id: The resource_id of this ResourceEntity.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ResourceEntity.

        资源名称

        :return: The resource_name of this ResourceEntity.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ResourceEntity.

        资源名称

        :param resource_name: The resource_name of this ResourceEntity.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def provider(self):
        r"""Gets the provider of this ResourceEntity.

        资源类型

        :return: The provider of this ResourceEntity.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this ResourceEntity.

        资源类型

        :param provider: The provider of this ResourceEntity.
        :type provider: str
        """
        self._provider = provider

    @property
    def resource_level_name(self):
        r"""Gets the resource_level_name of this ResourceEntity.

        资源等级名称

        :return: The resource_level_name of this ResourceEntity.
        :rtype: str
        """
        return self._resource_level_name

    @resource_level_name.setter
    def resource_level_name(self, resource_level_name):
        r"""Sets the resource_level_name of this ResourceEntity.

        资源等级名称

        :param resource_level_name: The resource_level_name of this ResourceEntity.
        :type resource_level_name: str
        """
        self._resource_level_name = resource_level_name

    @property
    def critical_level(self):
        r"""Gets the critical_level of this ResourceEntity.

        重要程度

        :return: The critical_level of this ResourceEntity.
        :rtype: str
        """
        return self._critical_level

    @critical_level.setter
    def critical_level(self, critical_level):
        r"""Sets the critical_level of this ResourceEntity.

        重要程度

        :param critical_level: The critical_level of this ResourceEntity.
        :type critical_level: str
        """
        self._critical_level = critical_level

    @property
    def config_protection(self):
        r"""Gets the config_protection of this ResourceEntity.

        是否配置保护

        :return: The config_protection of this ResourceEntity.
        :rtype: bool
        """
        return self._config_protection

    @config_protection.setter
    def config_protection(self, config_protection):
        r"""Sets the config_protection of this ResourceEntity.

        是否配置保护

        :param config_protection: The config_protection of this ResourceEntity.
        :type config_protection: bool
        """
        self._config_protection = config_protection

    @property
    def backup_compliance(self):
        r"""Gets the backup_compliance of this ResourceEntity.

        备份合规性

        :return: The backup_compliance of this ResourceEntity.
        :rtype: str
        """
        return self._backup_compliance

    @backup_compliance.setter
    def backup_compliance(self, backup_compliance):
        r"""Sets the backup_compliance of this ResourceEntity.

        备份合规性

        :param backup_compliance: The backup_compliance of this ResourceEntity.
        :type backup_compliance: str
        """
        self._backup_compliance = backup_compliance

    @property
    def local_vault_name(self):
        r"""Gets the local_vault_name of this ResourceEntity.

        本地备份存储库名称

        :return: The local_vault_name of this ResourceEntity.
        :rtype: str
        """
        return self._local_vault_name

    @local_vault_name.setter
    def local_vault_name(self, local_vault_name):
        r"""Sets the local_vault_name of this ResourceEntity.

        本地备份存储库名称

        :param local_vault_name: The local_vault_name of this ResourceEntity.
        :type local_vault_name: str
        """
        self._local_vault_name = local_vault_name

    @property
    def remote_vault_name(self):
        r"""Gets the remote_vault_name of this ResourceEntity.

        异地备份存储库名称

        :return: The remote_vault_name of this ResourceEntity.
        :rtype: str
        """
        return self._remote_vault_name

    @remote_vault_name.setter
    def remote_vault_name(self, remote_vault_name):
        r"""Sets the remote_vault_name of this ResourceEntity.

        异地备份存储库名称

        :param remote_vault_name: The remote_vault_name of this ResourceEntity.
        :type remote_vault_name: str
        """
        self._remote_vault_name = remote_vault_name

    @property
    def region_id(self):
        r"""Gets the region_id of this ResourceEntity.

        资源归属区域

        :return: The region_id of this ResourceEntity.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ResourceEntity.

        资源归属区域

        :param region_id: The region_id of this ResourceEntity.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ResourceEntity.

        资源创建时间

        :return: The create_time of this ResourceEntity.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ResourceEntity.

        资源创建时间

        :param create_time: The create_time of this ResourceEntity.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_inventory_time(self):
        r"""Gets the last_inventory_time of this ResourceEntity.

        上次盘点时间

        :return: The last_inventory_time of this ResourceEntity.
        :rtype: str
        """
        return self._last_inventory_time

    @last_inventory_time.setter
    def last_inventory_time(self, last_inventory_time):
        r"""Sets the last_inventory_time of this ResourceEntity.

        上次盘点时间

        :param last_inventory_time: The last_inventory_time of this ResourceEntity.
        :type last_inventory_time: str
        """
        self._last_inventory_time = last_inventory_time

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
        if not isinstance(other, ResourceEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
