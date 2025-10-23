# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComplianceRule:

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
        'is_system_embedded': 'bool',
        'domain_id': 'str',
        'resource_type': 'str',
        'backup_type': 'str',
        'local_backup_enabled': 'bool',
        'local_backup_retention': 'int',
        'local_backup_frequency': 'ComplianceRuleLocalBackupFrequency',
        'remote_backup_enabled': 'bool',
        'remote_backup_retention': 'int',
        'local_worm_enabled': 'bool',
        'remote_worm_enabled': 'bool',
        'is_cross_account_backup_forced': 'bool',
        'description': 'str',
        'created': 'int',
        'updated': 'int',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'is_system_embedded': 'is_system_embedded',
        'domain_id': 'domain_id',
        'resource_type': 'resource_type',
        'backup_type': 'backup_type',
        'local_backup_enabled': 'local_backup_enabled',
        'local_backup_retention': 'local_backup_retention',
        'local_backup_frequency': 'local_backup_frequency',
        'remote_backup_enabled': 'remote_backup_enabled',
        'remote_backup_retention': 'remote_backup_retention',
        'local_worm_enabled': 'local_worm_enabled',
        'remote_worm_enabled': 'remote_worm_enabled',
        'is_cross_account_backup_forced': 'is_cross_account_backup_forced',
        'description': 'description',
        'created': 'created',
        'updated': 'updated',
        'name': 'name'
    }

    def __init__(self, id=None, is_system_embedded=None, domain_id=None, resource_type=None, backup_type=None, local_backup_enabled=None, local_backup_retention=None, local_backup_frequency=None, remote_backup_enabled=None, remote_backup_retention=None, local_worm_enabled=None, remote_worm_enabled=None, is_cross_account_backup_forced=None, description=None, created=None, updated=None, name=None):
        r"""ComplianceRule

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param is_system_embedded: 是否系统内置规则
        :type is_system_embedded: bool
        :param domain_id: 账号ID
        :type domain_id: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param backup_type: 备份类型
        :type backup_type: str
        :param local_backup_enabled: 是否启用本地备份
        :type local_backup_enabled: bool
        :param local_backup_retention: 本地备份副本保留时长
        :type local_backup_retention: int
        :param local_backup_frequency: 
        :type local_backup_frequency: :class:`huaweicloudsdkbcc.v1.ComplianceRuleLocalBackupFrequency`
        :param remote_backup_enabled: 是否启用异地复制。
        :type remote_backup_enabled: bool
        :param remote_backup_retention: 异地复制副本保留时长。
        :type remote_backup_retention: int
        :param local_worm_enabled: 本地副本是否启用WORM特性。
        :type local_worm_enabled: bool
        :param remote_worm_enabled: 异地复制副本是否启用WORM特性。
        :type remote_worm_enabled: bool
        :param is_cross_account_backup_forced: 是否开启强制跨账号备份
        :type is_cross_account_backup_forced: bool
        :param description: 规则描述
        :type description: str
        :param created: 规则创建时间
        :type created: int
        :param updated: 规则更新时间
        :type updated: int
        :param name: 合规规则名称
        :type name: str
        """
        
        

        self._id = None
        self._is_system_embedded = None
        self._domain_id = None
        self._resource_type = None
        self._backup_type = None
        self._local_backup_enabled = None
        self._local_backup_retention = None
        self._local_backup_frequency = None
        self._remote_backup_enabled = None
        self._remote_backup_retention = None
        self._local_worm_enabled = None
        self._remote_worm_enabled = None
        self._is_cross_account_backup_forced = None
        self._description = None
        self._created = None
        self._updated = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if is_system_embedded is not None:
            self.is_system_embedded = is_system_embedded
        if domain_id is not None:
            self.domain_id = domain_id
        if resource_type is not None:
            self.resource_type = resource_type
        if backup_type is not None:
            self.backup_type = backup_type
        if local_backup_enabled is not None:
            self.local_backup_enabled = local_backup_enabled
        if local_backup_retention is not None:
            self.local_backup_retention = local_backup_retention
        if local_backup_frequency is not None:
            self.local_backup_frequency = local_backup_frequency
        if remote_backup_enabled is not None:
            self.remote_backup_enabled = remote_backup_enabled
        if remote_backup_retention is not None:
            self.remote_backup_retention = remote_backup_retention
        if local_worm_enabled is not None:
            self.local_worm_enabled = local_worm_enabled
        if remote_worm_enabled is not None:
            self.remote_worm_enabled = remote_worm_enabled
        if is_cross_account_backup_forced is not None:
            self.is_cross_account_backup_forced = is_cross_account_backup_forced
        if description is not None:
            self.description = description
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if name is not None:
            self.name = name

    @property
    def id(self):
        r"""Gets the id of this ComplianceRule.

        id

        :return: The id of this ComplianceRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ComplianceRule.

        id

        :param id: The id of this ComplianceRule.
        :type id: str
        """
        self._id = id

    @property
    def is_system_embedded(self):
        r"""Gets the is_system_embedded of this ComplianceRule.

        是否系统内置规则

        :return: The is_system_embedded of this ComplianceRule.
        :rtype: bool
        """
        return self._is_system_embedded

    @is_system_embedded.setter
    def is_system_embedded(self, is_system_embedded):
        r"""Sets the is_system_embedded of this ComplianceRule.

        是否系统内置规则

        :param is_system_embedded: The is_system_embedded of this ComplianceRule.
        :type is_system_embedded: bool
        """
        self._is_system_embedded = is_system_embedded

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ComplianceRule.

        账号ID

        :return: The domain_id of this ComplianceRule.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ComplianceRule.

        账号ID

        :param domain_id: The domain_id of this ComplianceRule.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ComplianceRule.

        资源类型

        :return: The resource_type of this ComplianceRule.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ComplianceRule.

        资源类型

        :param resource_type: The resource_type of this ComplianceRule.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def backup_type(self):
        r"""Gets the backup_type of this ComplianceRule.

        备份类型

        :return: The backup_type of this ComplianceRule.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        r"""Sets the backup_type of this ComplianceRule.

        备份类型

        :param backup_type: The backup_type of this ComplianceRule.
        :type backup_type: str
        """
        self._backup_type = backup_type

    @property
    def local_backup_enabled(self):
        r"""Gets the local_backup_enabled of this ComplianceRule.

        是否启用本地备份

        :return: The local_backup_enabled of this ComplianceRule.
        :rtype: bool
        """
        return self._local_backup_enabled

    @local_backup_enabled.setter
    def local_backup_enabled(self, local_backup_enabled):
        r"""Sets the local_backup_enabled of this ComplianceRule.

        是否启用本地备份

        :param local_backup_enabled: The local_backup_enabled of this ComplianceRule.
        :type local_backup_enabled: bool
        """
        self._local_backup_enabled = local_backup_enabled

    @property
    def local_backup_retention(self):
        r"""Gets the local_backup_retention of this ComplianceRule.

        本地备份副本保留时长

        :return: The local_backup_retention of this ComplianceRule.
        :rtype: int
        """
        return self._local_backup_retention

    @local_backup_retention.setter
    def local_backup_retention(self, local_backup_retention):
        r"""Sets the local_backup_retention of this ComplianceRule.

        本地备份副本保留时长

        :param local_backup_retention: The local_backup_retention of this ComplianceRule.
        :type local_backup_retention: int
        """
        self._local_backup_retention = local_backup_retention

    @property
    def local_backup_frequency(self):
        r"""Gets the local_backup_frequency of this ComplianceRule.

        :return: The local_backup_frequency of this ComplianceRule.
        :rtype: :class:`huaweicloudsdkbcc.v1.ComplianceRuleLocalBackupFrequency`
        """
        return self._local_backup_frequency

    @local_backup_frequency.setter
    def local_backup_frequency(self, local_backup_frequency):
        r"""Sets the local_backup_frequency of this ComplianceRule.

        :param local_backup_frequency: The local_backup_frequency of this ComplianceRule.
        :type local_backup_frequency: :class:`huaweicloudsdkbcc.v1.ComplianceRuleLocalBackupFrequency`
        """
        self._local_backup_frequency = local_backup_frequency

    @property
    def remote_backup_enabled(self):
        r"""Gets the remote_backup_enabled of this ComplianceRule.

        是否启用异地复制。

        :return: The remote_backup_enabled of this ComplianceRule.
        :rtype: bool
        """
        return self._remote_backup_enabled

    @remote_backup_enabled.setter
    def remote_backup_enabled(self, remote_backup_enabled):
        r"""Sets the remote_backup_enabled of this ComplianceRule.

        是否启用异地复制。

        :param remote_backup_enabled: The remote_backup_enabled of this ComplianceRule.
        :type remote_backup_enabled: bool
        """
        self._remote_backup_enabled = remote_backup_enabled

    @property
    def remote_backup_retention(self):
        r"""Gets the remote_backup_retention of this ComplianceRule.

        异地复制副本保留时长。

        :return: The remote_backup_retention of this ComplianceRule.
        :rtype: int
        """
        return self._remote_backup_retention

    @remote_backup_retention.setter
    def remote_backup_retention(self, remote_backup_retention):
        r"""Sets the remote_backup_retention of this ComplianceRule.

        异地复制副本保留时长。

        :param remote_backup_retention: The remote_backup_retention of this ComplianceRule.
        :type remote_backup_retention: int
        """
        self._remote_backup_retention = remote_backup_retention

    @property
    def local_worm_enabled(self):
        r"""Gets the local_worm_enabled of this ComplianceRule.

        本地副本是否启用WORM特性。

        :return: The local_worm_enabled of this ComplianceRule.
        :rtype: bool
        """
        return self._local_worm_enabled

    @local_worm_enabled.setter
    def local_worm_enabled(self, local_worm_enabled):
        r"""Sets the local_worm_enabled of this ComplianceRule.

        本地副本是否启用WORM特性。

        :param local_worm_enabled: The local_worm_enabled of this ComplianceRule.
        :type local_worm_enabled: bool
        """
        self._local_worm_enabled = local_worm_enabled

    @property
    def remote_worm_enabled(self):
        r"""Gets the remote_worm_enabled of this ComplianceRule.

        异地复制副本是否启用WORM特性。

        :return: The remote_worm_enabled of this ComplianceRule.
        :rtype: bool
        """
        return self._remote_worm_enabled

    @remote_worm_enabled.setter
    def remote_worm_enabled(self, remote_worm_enabled):
        r"""Sets the remote_worm_enabled of this ComplianceRule.

        异地复制副本是否启用WORM特性。

        :param remote_worm_enabled: The remote_worm_enabled of this ComplianceRule.
        :type remote_worm_enabled: bool
        """
        self._remote_worm_enabled = remote_worm_enabled

    @property
    def is_cross_account_backup_forced(self):
        r"""Gets the is_cross_account_backup_forced of this ComplianceRule.

        是否开启强制跨账号备份

        :return: The is_cross_account_backup_forced of this ComplianceRule.
        :rtype: bool
        """
        return self._is_cross_account_backup_forced

    @is_cross_account_backup_forced.setter
    def is_cross_account_backup_forced(self, is_cross_account_backup_forced):
        r"""Sets the is_cross_account_backup_forced of this ComplianceRule.

        是否开启强制跨账号备份

        :param is_cross_account_backup_forced: The is_cross_account_backup_forced of this ComplianceRule.
        :type is_cross_account_backup_forced: bool
        """
        self._is_cross_account_backup_forced = is_cross_account_backup_forced

    @property
    def description(self):
        r"""Gets the description of this ComplianceRule.

        规则描述

        :return: The description of this ComplianceRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ComplianceRule.

        规则描述

        :param description: The description of this ComplianceRule.
        :type description: str
        """
        self._description = description

    @property
    def created(self):
        r"""Gets the created of this ComplianceRule.

        规则创建时间

        :return: The created of this ComplianceRule.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ComplianceRule.

        规则创建时间

        :param created: The created of this ComplianceRule.
        :type created: int
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ComplianceRule.

        规则更新时间

        :return: The updated of this ComplianceRule.
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ComplianceRule.

        规则更新时间

        :param updated: The updated of this ComplianceRule.
        :type updated: int
        """
        self._updated = updated

    @property
    def name(self):
        r"""Gets the name of this ComplianceRule.

        合规规则名称

        :return: The name of this ComplianceRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ComplianceRule.

        合规规则名称

        :param name: The name of this ComplianceRule.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ComplianceRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
