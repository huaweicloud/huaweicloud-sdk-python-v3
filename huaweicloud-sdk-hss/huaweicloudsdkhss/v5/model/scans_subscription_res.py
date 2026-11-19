# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScansSubscriptionRes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vulnerabilities_statistics_status': 'bool',
        'account_change_history_status': 'bool',
        'danger_ports_status': 'bool',
        'weak_pwd_status': 'bool'
    }

    attribute_map = {
        'vulnerabilities_statistics_status': 'vulnerabilities_statistics_status',
        'account_change_history_status': 'account_change_history_status',
        'danger_ports_status': 'danger_ports_status',
        'weak_pwd_status': 'weak_pwd_status'
    }

    def __init__(self, vulnerabilities_statistics_status=None, account_change_history_status=None, danger_ports_status=None, weak_pwd_status=None):
        r"""ScansSubscriptionRes

        The model defined in huaweicloud sdk

        :param vulnerabilities_statistics_status: **参数解释**: 漏洞统计 **取值范围**: - true：开启 - false：关闭 
        :type vulnerabilities_statistics_status: bool
        :param account_change_history_status: **参数解释**: 资产账号变动记录 **取值范围**: - true：开启 - false：关闭 
        :type account_change_history_status: bool
        :param danger_ports_status: **参数解释**: 危险开放端口 **取值范围**: - true：开启 - false：关闭 
        :type danger_ports_status: bool
        :param weak_pwd_status: **参数解释**: 弱口令 **取值范围**: - true：开启 - false：关闭 
        :type weak_pwd_status: bool
        """
        
        

        self._vulnerabilities_statistics_status = None
        self._account_change_history_status = None
        self._danger_ports_status = None
        self._weak_pwd_status = None
        self.discriminator = None

        if vulnerabilities_statistics_status is not None:
            self.vulnerabilities_statistics_status = vulnerabilities_statistics_status
        if account_change_history_status is not None:
            self.account_change_history_status = account_change_history_status
        if danger_ports_status is not None:
            self.danger_ports_status = danger_ports_status
        if weak_pwd_status is not None:
            self.weak_pwd_status = weak_pwd_status

    @property
    def vulnerabilities_statistics_status(self):
        r"""Gets the vulnerabilities_statistics_status of this ScansSubscriptionRes.

        **参数解释**: 漏洞统计 **取值范围**: - true：开启 - false：关闭 

        :return: The vulnerabilities_statistics_status of this ScansSubscriptionRes.
        :rtype: bool
        """
        return self._vulnerabilities_statistics_status

    @vulnerabilities_statistics_status.setter
    def vulnerabilities_statistics_status(self, vulnerabilities_statistics_status):
        r"""Sets the vulnerabilities_statistics_status of this ScansSubscriptionRes.

        **参数解释**: 漏洞统计 **取值范围**: - true：开启 - false：关闭 

        :param vulnerabilities_statistics_status: The vulnerabilities_statistics_status of this ScansSubscriptionRes.
        :type vulnerabilities_statistics_status: bool
        """
        self._vulnerabilities_statistics_status = vulnerabilities_statistics_status

    @property
    def account_change_history_status(self):
        r"""Gets the account_change_history_status of this ScansSubscriptionRes.

        **参数解释**: 资产账号变动记录 **取值范围**: - true：开启 - false：关闭 

        :return: The account_change_history_status of this ScansSubscriptionRes.
        :rtype: bool
        """
        return self._account_change_history_status

    @account_change_history_status.setter
    def account_change_history_status(self, account_change_history_status):
        r"""Sets the account_change_history_status of this ScansSubscriptionRes.

        **参数解释**: 资产账号变动记录 **取值范围**: - true：开启 - false：关闭 

        :param account_change_history_status: The account_change_history_status of this ScansSubscriptionRes.
        :type account_change_history_status: bool
        """
        self._account_change_history_status = account_change_history_status

    @property
    def danger_ports_status(self):
        r"""Gets the danger_ports_status of this ScansSubscriptionRes.

        **参数解释**: 危险开放端口 **取值范围**: - true：开启 - false：关闭 

        :return: The danger_ports_status of this ScansSubscriptionRes.
        :rtype: bool
        """
        return self._danger_ports_status

    @danger_ports_status.setter
    def danger_ports_status(self, danger_ports_status):
        r"""Sets the danger_ports_status of this ScansSubscriptionRes.

        **参数解释**: 危险开放端口 **取值范围**: - true：开启 - false：关闭 

        :param danger_ports_status: The danger_ports_status of this ScansSubscriptionRes.
        :type danger_ports_status: bool
        """
        self._danger_ports_status = danger_ports_status

    @property
    def weak_pwd_status(self):
        r"""Gets the weak_pwd_status of this ScansSubscriptionRes.

        **参数解释**: 弱口令 **取值范围**: - true：开启 - false：关闭 

        :return: The weak_pwd_status of this ScansSubscriptionRes.
        :rtype: bool
        """
        return self._weak_pwd_status

    @weak_pwd_status.setter
    def weak_pwd_status(self, weak_pwd_status):
        r"""Sets the weak_pwd_status of this ScansSubscriptionRes.

        **参数解释**: 弱口令 **取值范围**: - true：开启 - false：关闭 

        :param weak_pwd_status: The weak_pwd_status of this ScansSubscriptionRes.
        :type weak_pwd_status: bool
        """
        self._weak_pwd_status = weak_pwd_status

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
        if not isinstance(other, ScansSubscriptionRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
