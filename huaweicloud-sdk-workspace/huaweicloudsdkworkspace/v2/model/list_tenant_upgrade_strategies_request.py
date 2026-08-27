# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTenantUpgradeStrategiesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_accurate_name': 'bool',
        'strategy_name': 'str',
        'strategy_type': 'int',
        'is_force_upgrade': 'int',
        'status': 'int',
        'strategy_priority': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'is_accurate_name': 'is_accurate_name',
        'strategy_name': 'strategy_name',
        'strategy_type': 'strategy_type',
        'is_force_upgrade': 'is_force_upgrade',
        'status': 'status',
        'strategy_priority': 'strategy_priority',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, is_accurate_name=None, strategy_name=None, strategy_type=None, is_force_upgrade=None, status=None, strategy_priority=None, offset=None, limit=None):
        r"""ListTenantUpgradeStrategiesRequest

        The model defined in huaweicloud sdk

        :param is_accurate_name: 是否精确匹配名称
        :type is_accurate_name: bool
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
        :param offset: 偏移量，默认0
        :type offset: int
        :param limit: 每页数量，默认10，最大100
        :type limit: int
        """
        
        

        self._is_accurate_name = None
        self._strategy_name = None
        self._strategy_type = None
        self._is_force_upgrade = None
        self._status = None
        self._strategy_priority = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if is_accurate_name is not None:
            self.is_accurate_name = is_accurate_name
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
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def is_accurate_name(self):
        r"""Gets the is_accurate_name of this ListTenantUpgradeStrategiesRequest.

        是否精确匹配名称

        :return: The is_accurate_name of this ListTenantUpgradeStrategiesRequest.
        :rtype: bool
        """
        return self._is_accurate_name

    @is_accurate_name.setter
    def is_accurate_name(self, is_accurate_name):
        r"""Sets the is_accurate_name of this ListTenantUpgradeStrategiesRequest.

        是否精确匹配名称

        :param is_accurate_name: The is_accurate_name of this ListTenantUpgradeStrategiesRequest.
        :type is_accurate_name: bool
        """
        self._is_accurate_name = is_accurate_name

    @property
    def strategy_name(self):
        r"""Gets the strategy_name of this ListTenantUpgradeStrategiesRequest.

        策略名称（支持模糊查询）

        :return: The strategy_name of this ListTenantUpgradeStrategiesRequest.
        :rtype: str
        """
        return self._strategy_name

    @strategy_name.setter
    def strategy_name(self, strategy_name):
        r"""Sets the strategy_name of this ListTenantUpgradeStrategiesRequest.

        策略名称（支持模糊查询）

        :param strategy_name: The strategy_name of this ListTenantUpgradeStrategiesRequest.
        :type strategy_name: str
        """
        self._strategy_name = strategy_name

    @property
    def strategy_type(self):
        r"""Gets the strategy_type of this ListTenantUpgradeStrategiesRequest.

        策略类型：0-服务端 1-客户端

        :return: The strategy_type of this ListTenantUpgradeStrategiesRequest.
        :rtype: int
        """
        return self._strategy_type

    @strategy_type.setter
    def strategy_type(self, strategy_type):
        r"""Sets the strategy_type of this ListTenantUpgradeStrategiesRequest.

        策略类型：0-服务端 1-客户端

        :param strategy_type: The strategy_type of this ListTenantUpgradeStrategiesRequest.
        :type strategy_type: int
        """
        self._strategy_type = strategy_type

    @property
    def is_force_upgrade(self):
        r"""Gets the is_force_upgrade of this ListTenantUpgradeStrategiesRequest.

        是否强制升级：0-否 1-是

        :return: The is_force_upgrade of this ListTenantUpgradeStrategiesRequest.
        :rtype: int
        """
        return self._is_force_upgrade

    @is_force_upgrade.setter
    def is_force_upgrade(self, is_force_upgrade):
        r"""Sets the is_force_upgrade of this ListTenantUpgradeStrategiesRequest.

        是否强制升级：0-否 1-是

        :param is_force_upgrade: The is_force_upgrade of this ListTenantUpgradeStrategiesRequest.
        :type is_force_upgrade: int
        """
        self._is_force_upgrade = is_force_upgrade

    @property
    def status(self):
        r"""Gets the status of this ListTenantUpgradeStrategiesRequest.

        启用状态：0-禁用 1-启用

        :return: The status of this ListTenantUpgradeStrategiesRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListTenantUpgradeStrategiesRequest.

        启用状态：0-禁用 1-启用

        :param status: The status of this ListTenantUpgradeStrategiesRequest.
        :type status: int
        """
        self._status = status

    @property
    def strategy_priority(self):
        r"""Gets the strategy_priority of this ListTenantUpgradeStrategiesRequest.

        协议策略优先级

        :return: The strategy_priority of this ListTenantUpgradeStrategiesRequest.
        :rtype: int
        """
        return self._strategy_priority

    @strategy_priority.setter
    def strategy_priority(self, strategy_priority):
        r"""Sets the strategy_priority of this ListTenantUpgradeStrategiesRequest.

        协议策略优先级

        :param strategy_priority: The strategy_priority of this ListTenantUpgradeStrategiesRequest.
        :type strategy_priority: int
        """
        self._strategy_priority = strategy_priority

    @property
    def offset(self):
        r"""Gets the offset of this ListTenantUpgradeStrategiesRequest.

        偏移量，默认0

        :return: The offset of this ListTenantUpgradeStrategiesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTenantUpgradeStrategiesRequest.

        偏移量，默认0

        :param offset: The offset of this ListTenantUpgradeStrategiesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTenantUpgradeStrategiesRequest.

        每页数量，默认10，最大100

        :return: The limit of this ListTenantUpgradeStrategiesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTenantUpgradeStrategiesRequest.

        每页数量，默认10，最大100

        :param limit: The limit of this ListTenantUpgradeStrategiesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListTenantUpgradeStrategiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
