# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TenantUpgradeStrategyDetailRsp:

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
        'project_id': 'str',
        'strategy_type': 'int',
        'strategy_name': 'str',
        'is_force_upgrade': 'int',
        'min_version': 'str',
        'target_version': 'str',
        'strategy_desc': 'str',
        'strategy_priority': 'int',
        'status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'strategy_type': 'strategy_type',
        'strategy_name': 'strategy_name',
        'is_force_upgrade': 'is_force_upgrade',
        'min_version': 'min_version',
        'target_version': 'target_version',
        'strategy_desc': 'strategy_desc',
        'strategy_priority': 'strategy_priority',
        'status': 'status'
    }

    def __init__(self, id=None, project_id=None, strategy_type=None, strategy_name=None, is_force_upgrade=None, min_version=None, target_version=None, strategy_desc=None, strategy_priority=None, status=None):
        r"""TenantUpgradeStrategyDetailRsp

        The model defined in huaweicloud sdk

        :param id: 策略ID
        :type id: str
        :param project_id: 项目ID
        :type project_id: str
        :param strategy_type: 策略类型：0-服务端 1-客户端
        :type strategy_type: int
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
        """
        
        

        self._id = None
        self._project_id = None
        self._strategy_type = None
        self._strategy_name = None
        self._is_force_upgrade = None
        self._min_version = None
        self._target_version = None
        self._strategy_desc = None
        self._strategy_priority = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if strategy_type is not None:
            self.strategy_type = strategy_type
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

    @property
    def id(self):
        r"""Gets the id of this TenantUpgradeStrategyDetailRsp.

        策略ID

        :return: The id of this TenantUpgradeStrategyDetailRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TenantUpgradeStrategyDetailRsp.

        策略ID

        :param id: The id of this TenantUpgradeStrategyDetailRsp.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this TenantUpgradeStrategyDetailRsp.

        项目ID

        :return: The project_id of this TenantUpgradeStrategyDetailRsp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TenantUpgradeStrategyDetailRsp.

        项目ID

        :param project_id: The project_id of this TenantUpgradeStrategyDetailRsp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def strategy_type(self):
        r"""Gets the strategy_type of this TenantUpgradeStrategyDetailRsp.

        策略类型：0-服务端 1-客户端

        :return: The strategy_type of this TenantUpgradeStrategyDetailRsp.
        :rtype: int
        """
        return self._strategy_type

    @strategy_type.setter
    def strategy_type(self, strategy_type):
        r"""Sets the strategy_type of this TenantUpgradeStrategyDetailRsp.

        策略类型：0-服务端 1-客户端

        :param strategy_type: The strategy_type of this TenantUpgradeStrategyDetailRsp.
        :type strategy_type: int
        """
        self._strategy_type = strategy_type

    @property
    def strategy_name(self):
        r"""Gets the strategy_name of this TenantUpgradeStrategyDetailRsp.

        策略名称

        :return: The strategy_name of this TenantUpgradeStrategyDetailRsp.
        :rtype: str
        """
        return self._strategy_name

    @strategy_name.setter
    def strategy_name(self, strategy_name):
        r"""Sets the strategy_name of this TenantUpgradeStrategyDetailRsp.

        策略名称

        :param strategy_name: The strategy_name of this TenantUpgradeStrategyDetailRsp.
        :type strategy_name: str
        """
        self._strategy_name = strategy_name

    @property
    def is_force_upgrade(self):
        r"""Gets the is_force_upgrade of this TenantUpgradeStrategyDetailRsp.

        是否强制升级：0-否 1-是

        :return: The is_force_upgrade of this TenantUpgradeStrategyDetailRsp.
        :rtype: int
        """
        return self._is_force_upgrade

    @is_force_upgrade.setter
    def is_force_upgrade(self, is_force_upgrade):
        r"""Sets the is_force_upgrade of this TenantUpgradeStrategyDetailRsp.

        是否强制升级：0-否 1-是

        :param is_force_upgrade: The is_force_upgrade of this TenantUpgradeStrategyDetailRsp.
        :type is_force_upgrade: int
        """
        self._is_force_upgrade = is_force_upgrade

    @property
    def min_version(self):
        r"""Gets the min_version of this TenantUpgradeStrategyDetailRsp.

        低于此版本升级

        :return: The min_version of this TenantUpgradeStrategyDetailRsp.
        :rtype: str
        """
        return self._min_version

    @min_version.setter
    def min_version(self, min_version):
        r"""Sets the min_version of this TenantUpgradeStrategyDetailRsp.

        低于此版本升级

        :param min_version: The min_version of this TenantUpgradeStrategyDetailRsp.
        :type min_version: str
        """
        self._min_version = min_version

    @property
    def target_version(self):
        r"""Gets the target_version of this TenantUpgradeStrategyDetailRsp.

        升级目标版本

        :return: The target_version of this TenantUpgradeStrategyDetailRsp.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this TenantUpgradeStrategyDetailRsp.

        升级目标版本

        :param target_version: The target_version of this TenantUpgradeStrategyDetailRsp.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def strategy_desc(self):
        r"""Gets the strategy_desc of this TenantUpgradeStrategyDetailRsp.

        策略描述

        :return: The strategy_desc of this TenantUpgradeStrategyDetailRsp.
        :rtype: str
        """
        return self._strategy_desc

    @strategy_desc.setter
    def strategy_desc(self, strategy_desc):
        r"""Sets the strategy_desc of this TenantUpgradeStrategyDetailRsp.

        策略描述

        :param strategy_desc: The strategy_desc of this TenantUpgradeStrategyDetailRsp.
        :type strategy_desc: str
        """
        self._strategy_desc = strategy_desc

    @property
    def strategy_priority(self):
        r"""Gets the strategy_priority of this TenantUpgradeStrategyDetailRsp.

        优先级（数值越小优先级越高）

        :return: The strategy_priority of this TenantUpgradeStrategyDetailRsp.
        :rtype: int
        """
        return self._strategy_priority

    @strategy_priority.setter
    def strategy_priority(self, strategy_priority):
        r"""Sets the strategy_priority of this TenantUpgradeStrategyDetailRsp.

        优先级（数值越小优先级越高）

        :param strategy_priority: The strategy_priority of this TenantUpgradeStrategyDetailRsp.
        :type strategy_priority: int
        """
        self._strategy_priority = strategy_priority

    @property
    def status(self):
        r"""Gets the status of this TenantUpgradeStrategyDetailRsp.

        状态：0-禁用 1-启用

        :return: The status of this TenantUpgradeStrategyDetailRsp.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TenantUpgradeStrategyDetailRsp.

        状态：0-禁用 1-启用

        :param status: The status of this TenantUpgradeStrategyDetailRsp.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, TenantUpgradeStrategyDetailRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
