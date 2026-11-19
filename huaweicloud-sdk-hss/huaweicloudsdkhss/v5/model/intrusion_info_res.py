# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IntrusionInfoRes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risky_account_info_list': 'list[object]',
        'abnormal_login_info_list': 'list[object]',
        'malicious_program_info_list': 'list[object]',
        'webshell_info_list': 'list[object]',
        'account_crack_info_list': 'list[object]',
        'critical_file_change_info_list': 'list[object]'
    }

    attribute_map = {
        'risky_account_info_list': 'risky_account_info_list',
        'abnormal_login_info_list': 'abnormal_login_info_list',
        'malicious_program_info_list': 'malicious_program_info_list',
        'webshell_info_list': 'webshell_info_list',
        'account_crack_info_list': 'account_crack_info_list',
        'critical_file_change_info_list': 'critical_file_change_info_list'
    }

    def __init__(self, risky_account_info_list=None, abnormal_login_info_list=None, malicious_program_info_list=None, webshell_info_list=None, account_crack_info_list=None, critical_file_change_info_list=None):
        r"""IntrusionInfoRes

        The model defined in huaweicloud sdk

        :param risky_account_info_list: **参数解释**： 风险账号列表 **取值范围**： 0-200个RiskyAccountInfo对象 
        :type risky_account_info_list: list[object]
        :param abnormal_login_info_list: **参数解释**： 异地登录列表 **取值范围**： 0-200个AbnormalLoginInfo对象 
        :type abnormal_login_info_list: list[object]
        :param malicious_program_info_list: **参数解释**： 恶意程序列表 **取值范围**： 0-200个MaliciousProgramInfo对象 
        :type malicious_program_info_list: list[object]
        :param webshell_info_list: **参数解释**： 网站后门列表 **取值范围**： 0-200个WebshellInfo对象 
        :type webshell_info_list: list[object]
        :param account_crack_info_list: **参数解释**： 账号破解列表 **取值范围**： 0-200个AccountCrackInfo对象 
        :type account_crack_info_list: list[object]
        :param critical_file_change_info_list: **参数解释**： 关键文件变更列表 **取值范围**： 0-200个CriticalFileChangeInfo对象 
        :type critical_file_change_info_list: list[object]
        """
        
        

        self._risky_account_info_list = None
        self._abnormal_login_info_list = None
        self._malicious_program_info_list = None
        self._webshell_info_list = None
        self._account_crack_info_list = None
        self._critical_file_change_info_list = None
        self.discriminator = None

        if risky_account_info_list is not None:
            self.risky_account_info_list = risky_account_info_list
        if abnormal_login_info_list is not None:
            self.abnormal_login_info_list = abnormal_login_info_list
        if malicious_program_info_list is not None:
            self.malicious_program_info_list = malicious_program_info_list
        if webshell_info_list is not None:
            self.webshell_info_list = webshell_info_list
        if account_crack_info_list is not None:
            self.account_crack_info_list = account_crack_info_list
        if critical_file_change_info_list is not None:
            self.critical_file_change_info_list = critical_file_change_info_list

    @property
    def risky_account_info_list(self):
        r"""Gets the risky_account_info_list of this IntrusionInfoRes.

        **参数解释**： 风险账号列表 **取值范围**： 0-200个RiskyAccountInfo对象 

        :return: The risky_account_info_list of this IntrusionInfoRes.
        :rtype: list[object]
        """
        return self._risky_account_info_list

    @risky_account_info_list.setter
    def risky_account_info_list(self, risky_account_info_list):
        r"""Sets the risky_account_info_list of this IntrusionInfoRes.

        **参数解释**： 风险账号列表 **取值范围**： 0-200个RiskyAccountInfo对象 

        :param risky_account_info_list: The risky_account_info_list of this IntrusionInfoRes.
        :type risky_account_info_list: list[object]
        """
        self._risky_account_info_list = risky_account_info_list

    @property
    def abnormal_login_info_list(self):
        r"""Gets the abnormal_login_info_list of this IntrusionInfoRes.

        **参数解释**： 异地登录列表 **取值范围**： 0-200个AbnormalLoginInfo对象 

        :return: The abnormal_login_info_list of this IntrusionInfoRes.
        :rtype: list[object]
        """
        return self._abnormal_login_info_list

    @abnormal_login_info_list.setter
    def abnormal_login_info_list(self, abnormal_login_info_list):
        r"""Sets the abnormal_login_info_list of this IntrusionInfoRes.

        **参数解释**： 异地登录列表 **取值范围**： 0-200个AbnormalLoginInfo对象 

        :param abnormal_login_info_list: The abnormal_login_info_list of this IntrusionInfoRes.
        :type abnormal_login_info_list: list[object]
        """
        self._abnormal_login_info_list = abnormal_login_info_list

    @property
    def malicious_program_info_list(self):
        r"""Gets the malicious_program_info_list of this IntrusionInfoRes.

        **参数解释**： 恶意程序列表 **取值范围**： 0-200个MaliciousProgramInfo对象 

        :return: The malicious_program_info_list of this IntrusionInfoRes.
        :rtype: list[object]
        """
        return self._malicious_program_info_list

    @malicious_program_info_list.setter
    def malicious_program_info_list(self, malicious_program_info_list):
        r"""Sets the malicious_program_info_list of this IntrusionInfoRes.

        **参数解释**： 恶意程序列表 **取值范围**： 0-200个MaliciousProgramInfo对象 

        :param malicious_program_info_list: The malicious_program_info_list of this IntrusionInfoRes.
        :type malicious_program_info_list: list[object]
        """
        self._malicious_program_info_list = malicious_program_info_list

    @property
    def webshell_info_list(self):
        r"""Gets the webshell_info_list of this IntrusionInfoRes.

        **参数解释**： 网站后门列表 **取值范围**： 0-200个WebshellInfo对象 

        :return: The webshell_info_list of this IntrusionInfoRes.
        :rtype: list[object]
        """
        return self._webshell_info_list

    @webshell_info_list.setter
    def webshell_info_list(self, webshell_info_list):
        r"""Sets the webshell_info_list of this IntrusionInfoRes.

        **参数解释**： 网站后门列表 **取值范围**： 0-200个WebshellInfo对象 

        :param webshell_info_list: The webshell_info_list of this IntrusionInfoRes.
        :type webshell_info_list: list[object]
        """
        self._webshell_info_list = webshell_info_list

    @property
    def account_crack_info_list(self):
        r"""Gets the account_crack_info_list of this IntrusionInfoRes.

        **参数解释**： 账号破解列表 **取值范围**： 0-200个AccountCrackInfo对象 

        :return: The account_crack_info_list of this IntrusionInfoRes.
        :rtype: list[object]
        """
        return self._account_crack_info_list

    @account_crack_info_list.setter
    def account_crack_info_list(self, account_crack_info_list):
        r"""Sets the account_crack_info_list of this IntrusionInfoRes.

        **参数解释**： 账号破解列表 **取值范围**： 0-200个AccountCrackInfo对象 

        :param account_crack_info_list: The account_crack_info_list of this IntrusionInfoRes.
        :type account_crack_info_list: list[object]
        """
        self._account_crack_info_list = account_crack_info_list

    @property
    def critical_file_change_info_list(self):
        r"""Gets the critical_file_change_info_list of this IntrusionInfoRes.

        **参数解释**： 关键文件变更列表 **取值范围**： 0-200个CriticalFileChangeInfo对象 

        :return: The critical_file_change_info_list of this IntrusionInfoRes.
        :rtype: list[object]
        """
        return self._critical_file_change_info_list

    @critical_file_change_info_list.setter
    def critical_file_change_info_list(self, critical_file_change_info_list):
        r"""Sets the critical_file_change_info_list of this IntrusionInfoRes.

        **参数解释**： 关键文件变更列表 **取值范围**： 0-200个CriticalFileChangeInfo对象 

        :param critical_file_change_info_list: The critical_file_change_info_list of this IntrusionInfoRes.
        :type critical_file_change_info_list: list[object]
        """
        self._critical_file_change_info_list = critical_file_change_info_list

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
        if not isinstance(other, IntrusionInfoRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
