# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScansInfoRes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vulnerabilities_statistics_info_list': 'list[object]',
        'account_change_history_info_list': 'list[object]',
        'danger_ports_info_list': 'list[object]',
        'weak_pwd_info_list': 'list[object]'
    }

    attribute_map = {
        'vulnerabilities_statistics_info_list': 'vulnerabilities_statistics_info_list',
        'account_change_history_info_list': 'account_change_history_info_list',
        'danger_ports_info_list': 'danger_ports_info_list',
        'weak_pwd_info_list': 'weak_pwd_info_list'
    }

    def __init__(self, vulnerabilities_statistics_info_list=None, account_change_history_info_list=None, danger_ports_info_list=None, weak_pwd_info_list=None):
        r"""ScansInfoRes

        The model defined in huaweicloud sdk

        :param vulnerabilities_statistics_info_list: **参数解释**： 漏洞统计列表 **取值范围**： 0-200个VulnerabilitiesStatisticsInfo对象 
        :type vulnerabilities_statistics_info_list: list[object]
        :param account_change_history_info_list: **参数解释**： 资产账号变动记录列表 **取值范围**： 0-200个AccountChangeHistoryInfo对象 
        :type account_change_history_info_list: list[object]
        :param danger_ports_info_list: **参数解释**： 危险开放端口列表 **取值范围**： 0-200个DangerPortsInfo对象 
        :type danger_ports_info_list: list[object]
        :param weak_pwd_info_list: **参数解释**： 弱口令列表 **取值范围**： 0-200个WeakPwdInfo对象 
        :type weak_pwd_info_list: list[object]
        """
        
        

        self._vulnerabilities_statistics_info_list = None
        self._account_change_history_info_list = None
        self._danger_ports_info_list = None
        self._weak_pwd_info_list = None
        self.discriminator = None

        if vulnerabilities_statistics_info_list is not None:
            self.vulnerabilities_statistics_info_list = vulnerabilities_statistics_info_list
        if account_change_history_info_list is not None:
            self.account_change_history_info_list = account_change_history_info_list
        if danger_ports_info_list is not None:
            self.danger_ports_info_list = danger_ports_info_list
        if weak_pwd_info_list is not None:
            self.weak_pwd_info_list = weak_pwd_info_list

    @property
    def vulnerabilities_statistics_info_list(self):
        r"""Gets the vulnerabilities_statistics_info_list of this ScansInfoRes.

        **参数解释**： 漏洞统计列表 **取值范围**： 0-200个VulnerabilitiesStatisticsInfo对象 

        :return: The vulnerabilities_statistics_info_list of this ScansInfoRes.
        :rtype: list[object]
        """
        return self._vulnerabilities_statistics_info_list

    @vulnerabilities_statistics_info_list.setter
    def vulnerabilities_statistics_info_list(self, vulnerabilities_statistics_info_list):
        r"""Sets the vulnerabilities_statistics_info_list of this ScansInfoRes.

        **参数解释**： 漏洞统计列表 **取值范围**： 0-200个VulnerabilitiesStatisticsInfo对象 

        :param vulnerabilities_statistics_info_list: The vulnerabilities_statistics_info_list of this ScansInfoRes.
        :type vulnerabilities_statistics_info_list: list[object]
        """
        self._vulnerabilities_statistics_info_list = vulnerabilities_statistics_info_list

    @property
    def account_change_history_info_list(self):
        r"""Gets the account_change_history_info_list of this ScansInfoRes.

        **参数解释**： 资产账号变动记录列表 **取值范围**： 0-200个AccountChangeHistoryInfo对象 

        :return: The account_change_history_info_list of this ScansInfoRes.
        :rtype: list[object]
        """
        return self._account_change_history_info_list

    @account_change_history_info_list.setter
    def account_change_history_info_list(self, account_change_history_info_list):
        r"""Sets the account_change_history_info_list of this ScansInfoRes.

        **参数解释**： 资产账号变动记录列表 **取值范围**： 0-200个AccountChangeHistoryInfo对象 

        :param account_change_history_info_list: The account_change_history_info_list of this ScansInfoRes.
        :type account_change_history_info_list: list[object]
        """
        self._account_change_history_info_list = account_change_history_info_list

    @property
    def danger_ports_info_list(self):
        r"""Gets the danger_ports_info_list of this ScansInfoRes.

        **参数解释**： 危险开放端口列表 **取值范围**： 0-200个DangerPortsInfo对象 

        :return: The danger_ports_info_list of this ScansInfoRes.
        :rtype: list[object]
        """
        return self._danger_ports_info_list

    @danger_ports_info_list.setter
    def danger_ports_info_list(self, danger_ports_info_list):
        r"""Sets the danger_ports_info_list of this ScansInfoRes.

        **参数解释**： 危险开放端口列表 **取值范围**： 0-200个DangerPortsInfo对象 

        :param danger_ports_info_list: The danger_ports_info_list of this ScansInfoRes.
        :type danger_ports_info_list: list[object]
        """
        self._danger_ports_info_list = danger_ports_info_list

    @property
    def weak_pwd_info_list(self):
        r"""Gets the weak_pwd_info_list of this ScansInfoRes.

        **参数解释**： 弱口令列表 **取值范围**： 0-200个WeakPwdInfo对象 

        :return: The weak_pwd_info_list of this ScansInfoRes.
        :rtype: list[object]
        """
        return self._weak_pwd_info_list

    @weak_pwd_info_list.setter
    def weak_pwd_info_list(self, weak_pwd_info_list):
        r"""Sets the weak_pwd_info_list of this ScansInfoRes.

        **参数解释**： 弱口令列表 **取值范围**： 0-200个WeakPwdInfo对象 

        :param weak_pwd_info_list: The weak_pwd_info_list of this ScansInfoRes.
        :type weak_pwd_info_list: list[object]
        """
        self._weak_pwd_info_list = weak_pwd_info_list

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
        if not isinstance(other, ScansInfoRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
