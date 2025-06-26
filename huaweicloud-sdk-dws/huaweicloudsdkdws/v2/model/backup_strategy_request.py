# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupStrategyRequest:

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
        'backup_level': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'backup_strategy': 'backup_strategy',
        'backup_type': 'backup_type',
        'backup_level': 'backup_level'
    }

    def __init__(self, policy_id=None, policy_name=None, backup_strategy=None, backup_type=None, backup_level=None):
        r"""BackupStrategyRequest

        The model defined in huaweicloud sdk

        :param policy_id: **参数解释**： 策略ID。 **取值范围**： 不涉及。
        :type policy_id: str
        :param policy_name: **参数解释**： 策略名称。添加备份策略时为必选字段。策略名称在4位到92位之间，必须以字母开头，不区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他特殊字符，并且名称唯一。 **取值范围**： 不涉及。
        :type policy_name: str
        :param backup_strategy: **参数解释**： 执行策略。添加备份策略时为必选字段。符合Cron表达式格式。 **取值范围**： 不涉及。
        :type backup_strategy: str
        :param backup_type: **参数解释**： 备份类型。 **取值范围**： full：全量。 increment：增量。
        :type backup_type: str
        :param backup_level: **参数解释**： 备份级别。 **取值范围**： cluster：集群级。
        :type backup_level: str
        """
        
        

        self._policy_id = None
        self._policy_name = None
        self._backup_strategy = None
        self._backup_type = None
        self._backup_level = None
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

    @property
    def policy_id(self):
        r"""Gets the policy_id of this BackupStrategyRequest.

        **参数解释**： 策略ID。 **取值范围**： 不涉及。

        :return: The policy_id of this BackupStrategyRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this BackupStrategyRequest.

        **参数解释**： 策略ID。 **取值范围**： 不涉及。

        :param policy_id: The policy_id of this BackupStrategyRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this BackupStrategyRequest.

        **参数解释**： 策略名称。添加备份策略时为必选字段。策略名称在4位到92位之间，必须以字母开头，不区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他特殊字符，并且名称唯一。 **取值范围**： 不涉及。

        :return: The policy_name of this BackupStrategyRequest.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this BackupStrategyRequest.

        **参数解释**： 策略名称。添加备份策略时为必选字段。策略名称在4位到92位之间，必须以字母开头，不区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他特殊字符，并且名称唯一。 **取值范围**： 不涉及。

        :param policy_name: The policy_name of this BackupStrategyRequest.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def backup_strategy(self):
        r"""Gets the backup_strategy of this BackupStrategyRequest.

        **参数解释**： 执行策略。添加备份策略时为必选字段。符合Cron表达式格式。 **取值范围**： 不涉及。

        :return: The backup_strategy of this BackupStrategyRequest.
        :rtype: str
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        r"""Sets the backup_strategy of this BackupStrategyRequest.

        **参数解释**： 执行策略。添加备份策略时为必选字段。符合Cron表达式格式。 **取值范围**： 不涉及。

        :param backup_strategy: The backup_strategy of this BackupStrategyRequest.
        :type backup_strategy: str
        """
        self._backup_strategy = backup_strategy

    @property
    def backup_type(self):
        r"""Gets the backup_type of this BackupStrategyRequest.

        **参数解释**： 备份类型。 **取值范围**： full：全量。 increment：增量。

        :return: The backup_type of this BackupStrategyRequest.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        r"""Sets the backup_type of this BackupStrategyRequest.

        **参数解释**： 备份类型。 **取值范围**： full：全量。 increment：增量。

        :param backup_type: The backup_type of this BackupStrategyRequest.
        :type backup_type: str
        """
        self._backup_type = backup_type

    @property
    def backup_level(self):
        r"""Gets the backup_level of this BackupStrategyRequest.

        **参数解释**： 备份级别。 **取值范围**： cluster：集群级。

        :return: The backup_level of this BackupStrategyRequest.
        :rtype: str
        """
        return self._backup_level

    @backup_level.setter
    def backup_level(self, backup_level):
        r"""Sets the backup_level of this BackupStrategyRequest.

        **参数解释**： 备份级别。 **取值范围**： cluster：集群级。

        :param backup_level: The backup_level of this BackupStrategyRequest.
        :type backup_level: str
        """
        self._backup_level = backup_level

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
        if not isinstance(other, BackupStrategyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
