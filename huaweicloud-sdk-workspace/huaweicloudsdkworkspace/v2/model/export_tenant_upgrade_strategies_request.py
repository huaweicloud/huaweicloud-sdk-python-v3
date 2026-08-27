# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportTenantUpgradeStrategiesRequest:

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
        'strategy_type': 'int',
        'is_force_upgrade': 'int',
        'status': 'int',
        'strategy_priority': 'int',
        'language': 'str'
    }

    attribute_map = {
        'strategy_name': 'strategy_name',
        'strategy_type': 'strategy_type',
        'is_force_upgrade': 'is_force_upgrade',
        'status': 'status',
        'strategy_priority': 'strategy_priority',
        'language': 'language'
    }

    def __init__(self, strategy_name=None, strategy_type=None, is_force_upgrade=None, status=None, strategy_priority=None, language=None):
        r"""ExportTenantUpgradeStrategiesRequest

        The model defined in huaweicloud sdk

        :param strategy_name: 策略名称（支持模糊查询）
        :type strategy_name: str
        :param strategy_type: 策略类型：0-服务端 1-客户端
        :type strategy_type: int
        :param is_force_upgrade: 是否强制升级：0-否 1-是
        :type is_force_upgrade: int
        :param status: 启用状态：0-禁用 1-启用
        :type status: int
        :param strategy_priority: 协议策略优先级
        :type strategy_priority: int
        :param language: 语言。   - zh_CN：中文 - en_US：英文
        :type language: str
        """
        
        

        self._strategy_name = None
        self._strategy_type = None
        self._is_force_upgrade = None
        self._status = None
        self._strategy_priority = None
        self._language = None
        self.discriminator = None

        if strategy_name is not None:
            self.strategy_name = strategy_name
        if strategy_type is not None:
            self.strategy_type = strategy_type
        if is_force_upgrade is not None:
            self.is_force_upgrade = is_force_upgrade
        if status is not None:
            self.status = status
        if strategy_priority is not None:
            self.strategy_priority = strategy_priority
        self.language = language

    @property
    def strategy_name(self):
        r"""Gets the strategy_name of this ExportTenantUpgradeStrategiesRequest.

        策略名称（支持模糊查询）

        :return: The strategy_name of this ExportTenantUpgradeStrategiesRequest.
        :rtype: str
        """
        return self._strategy_name

    @strategy_name.setter
    def strategy_name(self, strategy_name):
        r"""Sets the strategy_name of this ExportTenantUpgradeStrategiesRequest.

        策略名称（支持模糊查询）

        :param strategy_name: The strategy_name of this ExportTenantUpgradeStrategiesRequest.
        :type strategy_name: str
        """
        self._strategy_name = strategy_name

    @property
    def strategy_type(self):
        r"""Gets the strategy_type of this ExportTenantUpgradeStrategiesRequest.

        策略类型：0-服务端 1-客户端

        :return: The strategy_type of this ExportTenantUpgradeStrategiesRequest.
        :rtype: int
        """
        return self._strategy_type

    @strategy_type.setter
    def strategy_type(self, strategy_type):
        r"""Sets the strategy_type of this ExportTenantUpgradeStrategiesRequest.

        策略类型：0-服务端 1-客户端

        :param strategy_type: The strategy_type of this ExportTenantUpgradeStrategiesRequest.
        :type strategy_type: int
        """
        self._strategy_type = strategy_type

    @property
    def is_force_upgrade(self):
        r"""Gets the is_force_upgrade of this ExportTenantUpgradeStrategiesRequest.

        是否强制升级：0-否 1-是

        :return: The is_force_upgrade of this ExportTenantUpgradeStrategiesRequest.
        :rtype: int
        """
        return self._is_force_upgrade

    @is_force_upgrade.setter
    def is_force_upgrade(self, is_force_upgrade):
        r"""Sets the is_force_upgrade of this ExportTenantUpgradeStrategiesRequest.

        是否强制升级：0-否 1-是

        :param is_force_upgrade: The is_force_upgrade of this ExportTenantUpgradeStrategiesRequest.
        :type is_force_upgrade: int
        """
        self._is_force_upgrade = is_force_upgrade

    @property
    def status(self):
        r"""Gets the status of this ExportTenantUpgradeStrategiesRequest.

        启用状态：0-禁用 1-启用

        :return: The status of this ExportTenantUpgradeStrategiesRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExportTenantUpgradeStrategiesRequest.

        启用状态：0-禁用 1-启用

        :param status: The status of this ExportTenantUpgradeStrategiesRequest.
        :type status: int
        """
        self._status = status

    @property
    def strategy_priority(self):
        r"""Gets the strategy_priority of this ExportTenantUpgradeStrategiesRequest.

        协议策略优先级

        :return: The strategy_priority of this ExportTenantUpgradeStrategiesRequest.
        :rtype: int
        """
        return self._strategy_priority

    @strategy_priority.setter
    def strategy_priority(self, strategy_priority):
        r"""Sets the strategy_priority of this ExportTenantUpgradeStrategiesRequest.

        协议策略优先级

        :param strategy_priority: The strategy_priority of this ExportTenantUpgradeStrategiesRequest.
        :type strategy_priority: int
        """
        self._strategy_priority = strategy_priority

    @property
    def language(self):
        r"""Gets the language of this ExportTenantUpgradeStrategiesRequest.

        语言。   - zh_CN：中文 - en_US：英文

        :return: The language of this ExportTenantUpgradeStrategiesRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ExportTenantUpgradeStrategiesRequest.

        语言。   - zh_CN：中文 - en_US：英文

        :param language: The language of this ExportTenantUpgradeStrategiesRequest.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, ExportTenantUpgradeStrategiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
