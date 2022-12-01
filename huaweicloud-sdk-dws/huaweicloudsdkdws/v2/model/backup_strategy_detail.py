# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupStrategyDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'policy_name': 'str',
        'backup_strategy': 'str',
        'backup_type': 'str',
        'backup_level': 'str',
        'next_fire_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'backup_strategy': 'backup_strategy',
        'backup_type': 'backup_type',
        'backup_level': 'backup_level',
        'next_fire_time': 'next_fire_time',
        'update_time': 'update_time'
    }

    def __init__(self, policy_id=None, policy_name=None, backup_strategy=None, backup_type=None, backup_level=None, next_fire_time=None, update_time=None):
        """BackupStrategyDetail

        The model defined in huaweicloud sdk

        :param policy_id: 策略ID。
        :type policy_id: str
        :param policy_name: 策略名称。
        :type policy_name: str
        :param backup_strategy: 执行策略。
        :type backup_strategy: str
        :param backup_type: 备份类型。
        :type backup_type: str
        :param backup_level: 备份级别。
        :type backup_level: str
        :param next_fire_time: 下次触发时间。
        :type next_fire_time: str
        :param update_time: 更新时间。
        :type update_time: str
        """
        
        

        self._policy_id = None
        self._policy_name = None
        self._backup_strategy = None
        self._backup_type = None
        self._backup_level = None
        self._next_fire_time = None
        self._update_time = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if backup_strategy is not None:
            self.backup_strategy = backup_strategy
        if backup_type is not None:
            self.backup_type = backup_type
        if backup_level is not None:
            self.backup_level = backup_level
        if next_fire_time is not None:
            self.next_fire_time = next_fire_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def policy_id(self):
        """Gets the policy_id of this BackupStrategyDetail.

        策略ID。

        :return: The policy_id of this BackupStrategyDetail.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this BackupStrategyDetail.

        策略ID。

        :param policy_id: The policy_id of this BackupStrategyDetail.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        """Gets the policy_name of this BackupStrategyDetail.

        策略名称。

        :return: The policy_name of this BackupStrategyDetail.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this BackupStrategyDetail.

        策略名称。

        :param policy_name: The policy_name of this BackupStrategyDetail.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this BackupStrategyDetail.

        执行策略。

        :return: The backup_strategy of this BackupStrategyDetail.
        :rtype: str
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this BackupStrategyDetail.

        执行策略。

        :param backup_strategy: The backup_strategy of this BackupStrategyDetail.
        :type backup_strategy: str
        """
        self._backup_strategy = backup_strategy

    @property
    def backup_type(self):
        """Gets the backup_type of this BackupStrategyDetail.

        备份类型。

        :return: The backup_type of this BackupStrategyDetail.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this BackupStrategyDetail.

        备份类型。

        :param backup_type: The backup_type of this BackupStrategyDetail.
        :type backup_type: str
        """
        self._backup_type = backup_type

    @property
    def backup_level(self):
        """Gets the backup_level of this BackupStrategyDetail.

        备份级别。

        :return: The backup_level of this BackupStrategyDetail.
        :rtype: str
        """
        return self._backup_level

    @backup_level.setter
    def backup_level(self, backup_level):
        """Sets the backup_level of this BackupStrategyDetail.

        备份级别。

        :param backup_level: The backup_level of this BackupStrategyDetail.
        :type backup_level: str
        """
        self._backup_level = backup_level

    @property
    def next_fire_time(self):
        """Gets the next_fire_time of this BackupStrategyDetail.

        下次触发时间。

        :return: The next_fire_time of this BackupStrategyDetail.
        :rtype: str
        """
        return self._next_fire_time

    @next_fire_time.setter
    def next_fire_time(self, next_fire_time):
        """Sets the next_fire_time of this BackupStrategyDetail.

        下次触发时间。

        :param next_fire_time: The next_fire_time of this BackupStrategyDetail.
        :type next_fire_time: str
        """
        self._next_fire_time = next_fire_time

    @property
    def update_time(self):
        """Gets the update_time of this BackupStrategyDetail.

        更新时间。

        :return: The update_time of this BackupStrategyDetail.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this BackupStrategyDetail.

        更新时间。

        :param update_time: The update_time of this BackupStrategyDetail.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, BackupStrategyDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
