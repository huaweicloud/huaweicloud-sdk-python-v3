# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTenantUpgradeStrategyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'strategy_name': 'str',
        'is_force_upgrade': 'int',
        'min_version': 'str',
        'target_version': 'str',
        'strategy_desc': 'str',
        'strategy_priority': 'int',
        'status': 'int',
        'apply_objects': 'list[ApplyObjectInfo]'
    }

    attribute_map = {
        'strategy_name': 'strategy_name',
        'is_force_upgrade': 'is_force_upgrade',
        'min_version': 'min_version',
        'target_version': 'target_version',
        'strategy_desc': 'strategy_desc',
        'strategy_priority': 'strategy_priority',
        'status': 'status',
        'apply_objects': 'apply_objects'
    }

    def __init__(self, strategy_name=None, is_force_upgrade=None, min_version=None, target_version=None, strategy_desc=None, strategy_priority=None, status=None, apply_objects=None):
        r"""UpdateTenantUpgradeStrategyRequestBody

        The model defined in huaweicloud sdk

        :param strategy_name: 策略名称
        :type strategy_name: str
        :param is_force_upgrade: 是否强制升级：0-否 1-是
        :type is_force_upgrade: int
        :param min_version: 低于此版本升级
        :type min_version: str
        :param target_version: 升级目标版本
        :type target_version: str
        :param strategy_desc: 策略描述
        :type strategy_desc: str
        :param strategy_priority: 优先级（数值越小优先级越高）
        :type strategy_priority: int
        :param status: 状态：0-禁用 1-启用
        :type status: int
        :param apply_objects: 应用对象列表
        :type apply_objects: list[:class:`huaweicloudsdkworkspace.v2.ApplyObjectInfo`]
        """
        
        

        self._strategy_name = None
        self._is_force_upgrade = None
        self._min_version = None
        self._target_version = None
        self._strategy_desc = None
        self._strategy_priority = None
        self._status = None
        self._apply_objects = None
        self.discriminator = None

        if strategy_name is not None:
            self.strategy_name = strategy_name
        if is_force_upgrade is not None:
            self.is_force_upgrade = is_force_upgrade
        if min_version is not None:
            self.min_version = min_version
        if target_version is not None:
            self.target_version = target_version
        if strategy_desc is not None:
            self.strategy_desc = strategy_desc
        if strategy_priority is not None:
            self.strategy_priority = strategy_priority
        if status is not None:
            self.status = status
        if apply_objects is not None:
            self.apply_objects = apply_objects

    @property
    def strategy_name(self):
        r"""Gets the strategy_name of this UpdateTenantUpgradeStrategyRequestBody.

        策略名称

        :return: The strategy_name of this UpdateTenantUpgradeStrategyRequestBody.
        :rtype: str
        """
        return self._strategy_name

    @strategy_name.setter
    def strategy_name(self, strategy_name):
        r"""Sets the strategy_name of this UpdateTenantUpgradeStrategyRequestBody.

        策略名称

        :param strategy_name: The strategy_name of this UpdateTenantUpgradeStrategyRequestBody.
        :type strategy_name: str
        """
        self._strategy_name = strategy_name

    @property
    def is_force_upgrade(self):
        r"""Gets the is_force_upgrade of this UpdateTenantUpgradeStrategyRequestBody.

        是否强制升级：0-否 1-是

        :return: The is_force_upgrade of this UpdateTenantUpgradeStrategyRequestBody.
        :rtype: int
        """
        return self._is_force_upgrade

    @is_force_upgrade.setter
    def is_force_upgrade(self, is_force_upgrade):
        r"""Sets the is_force_upgrade of this UpdateTenantUpgradeStrategyRequestBody.

        是否强制升级：0-否 1-是

        :param is_force_upgrade: The is_force_upgrade of this UpdateTenantUpgradeStrategyRequestBody.
        :type is_force_upgrade: int
        """
        self._is_force_upgrade = is_force_upgrade

    @property
    def min_version(self):
        r"""Gets the min_version of this UpdateTenantUpgradeStrategyRequestBody.

        低于此版本升级

        :return: The min_version of this UpdateTenantUpgradeStrategyRequestBody.
        :rtype: str
        """
        return self._min_version

    @min_version.setter
    def min_version(self, min_version):
        r"""Sets the min_version of this UpdateTenantUpgradeStrategyRequestBody.

        低于此版本升级

        :param min_version: The min_version of this UpdateTenantUpgradeStrategyRequestBody.
        :type min_version: str
        """
        self._min_version = min_version

    @property
    def target_version(self):
        r"""Gets the target_version of this UpdateTenantUpgradeStrategyRequestBody.

        升级目标版本

        :return: The target_version of this UpdateTenantUpgradeStrategyRequestBody.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this UpdateTenantUpgradeStrategyRequestBody.

        升级目标版本

        :param target_version: The target_version of this UpdateTenantUpgradeStrategyRequestBody.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def strategy_desc(self):
        r"""Gets the strategy_desc of this UpdateTenantUpgradeStrategyRequestBody.

        策略描述

        :return: The strategy_desc of this UpdateTenantUpgradeStrategyRequestBody.
        :rtype: str
        """
        return self._strategy_desc

    @strategy_desc.setter
    def strategy_desc(self, strategy_desc):
        r"""Sets the strategy_desc of this UpdateTenantUpgradeStrategyRequestBody.

        策略描述

        :param strategy_desc: The strategy_desc of this UpdateTenantUpgradeStrategyRequestBody.
        :type strategy_desc: str
        """
        self._strategy_desc = strategy_desc

    @property
    def strategy_priority(self):
        r"""Gets the strategy_priority of this UpdateTenantUpgradeStrategyRequestBody.

        优先级（数值越小优先级越高）

        :return: The strategy_priority of this UpdateTenantUpgradeStrategyRequestBody.
        :rtype: int
        """
        return self._strategy_priority

    @strategy_priority.setter
    def strategy_priority(self, strategy_priority):
        r"""Sets the strategy_priority of this UpdateTenantUpgradeStrategyRequestBody.

        优先级（数值越小优先级越高）

        :param strategy_priority: The strategy_priority of this UpdateTenantUpgradeStrategyRequestBody.
        :type strategy_priority: int
        """
        self._strategy_priority = strategy_priority

    @property
    def status(self):
        r"""Gets the status of this UpdateTenantUpgradeStrategyRequestBody.

        状态：0-禁用 1-启用

        :return: The status of this UpdateTenantUpgradeStrategyRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateTenantUpgradeStrategyRequestBody.

        状态：0-禁用 1-启用

        :param status: The status of this UpdateTenantUpgradeStrategyRequestBody.
        :type status: int
        """
        self._status = status

    @property
    def apply_objects(self):
        r"""Gets the apply_objects of this UpdateTenantUpgradeStrategyRequestBody.

        应用对象列表

        :return: The apply_objects of this UpdateTenantUpgradeStrategyRequestBody.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ApplyObjectInfo`]
        """
        return self._apply_objects

    @apply_objects.setter
    def apply_objects(self, apply_objects):
        r"""Sets the apply_objects of this UpdateTenantUpgradeStrategyRequestBody.

        应用对象列表

        :param apply_objects: The apply_objects of this UpdateTenantUpgradeStrategyRequestBody.
        :type apply_objects: list[:class:`huaweicloudsdkworkspace.v2.ApplyObjectInfo`]
        """
        self._apply_objects = apply_objects

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateTenantUpgradeStrategyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
