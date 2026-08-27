# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupPolicyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'retention_days': 'int',
        'period': 'str',
        'policy_type': 'str'
    }

    attribute_map = {
        'retention_days': 'retention_days',
        'period': 'period',
        'policy_type': 'policy_type'
    }

    def __init__(self, retention_days=None, period=None, policy_type=None):
        r"""BackupPolicyInfo

        The model defined in huaweicloud sdk

        :param retention_days: **参数解释**：  指定已生成的备份文件可以保存的天数。  **取值范围**：  1-732。 您也可以联系客服申请开通最大保留天数为3660。
        :type retention_days: int
        :param period: **参数解释**：  备份周期配置。  **取值范围**：  格式必须为“日期 月份 星期”形式的Cron表达式，时区为UTC时区。 日期支持填写1~31、特殊字符*（表示任意值）、特殊字符L（表示最后一天）。填写1~31或L时支持填写多个，需以逗号隔开。 月份支持填写1~12、特殊字符*（表示任意值）。 星期支持填写1~7，需以逗号隔开。
        :type period: str
        :param policy_type: **参数解释**:  自动备份策略类型。  **取值范围**：   - base：表示基础策略。   - sparse：表示稀疏策略。
        :type policy_type: str
        """
        
        

        self._retention_days = None
        self._period = None
        self._policy_type = None
        self.discriminator = None

        self.retention_days = retention_days
        self.period = period
        self.policy_type = policy_type

    @property
    def retention_days(self):
        r"""Gets the retention_days of this BackupPolicyInfo.

        **参数解释**：  指定已生成的备份文件可以保存的天数。  **取值范围**：  1-732。 您也可以联系客服申请开通最大保留天数为3660。

        :return: The retention_days of this BackupPolicyInfo.
        :rtype: int
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        r"""Sets the retention_days of this BackupPolicyInfo.

        **参数解释**：  指定已生成的备份文件可以保存的天数。  **取值范围**：  1-732。 您也可以联系客服申请开通最大保留天数为3660。

        :param retention_days: The retention_days of this BackupPolicyInfo.
        :type retention_days: int
        """
        self._retention_days = retention_days

    @property
    def period(self):
        r"""Gets the period of this BackupPolicyInfo.

        **参数解释**：  备份周期配置。  **取值范围**：  格式必须为“日期 月份 星期”形式的Cron表达式，时区为UTC时区。 日期支持填写1~31、特殊字符*（表示任意值）、特殊字符L（表示最后一天）。填写1~31或L时支持填写多个，需以逗号隔开。 月份支持填写1~12、特殊字符*（表示任意值）。 星期支持填写1~7，需以逗号隔开。

        :return: The period of this BackupPolicyInfo.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this BackupPolicyInfo.

        **参数解释**：  备份周期配置。  **取值范围**：  格式必须为“日期 月份 星期”形式的Cron表达式，时区为UTC时区。 日期支持填写1~31、特殊字符*（表示任意值）、特殊字符L（表示最后一天）。填写1~31或L时支持填写多个，需以逗号隔开。 月份支持填写1~12、特殊字符*（表示任意值）。 星期支持填写1~7，需以逗号隔开。

        :param period: The period of this BackupPolicyInfo.
        :type period: str
        """
        self._period = period

    @property
    def policy_type(self):
        r"""Gets the policy_type of this BackupPolicyInfo.

        **参数解释**:  自动备份策略类型。  **取值范围**：   - base：表示基础策略。   - sparse：表示稀疏策略。

        :return: The policy_type of this BackupPolicyInfo.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this BackupPolicyInfo.

        **参数解释**:  自动备份策略类型。  **取值范围**：   - base：表示基础策略。   - sparse：表示稀疏策略。

        :param policy_type: The policy_type of this BackupPolicyInfo.
        :type policy_type: str
        """
        self._policy_type = policy_type

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
        if not isinstance(other, BackupPolicyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
