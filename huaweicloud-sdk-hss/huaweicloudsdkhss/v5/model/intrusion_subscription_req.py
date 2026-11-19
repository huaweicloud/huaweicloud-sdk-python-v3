# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IntrusionSubscriptionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risky_account_status': 'bool',
        'abnormal_login_status': 'bool',
        'malicious_program_status': 'bool',
        'webshell_status': 'bool',
        'account_crack_status': 'bool',
        'critical_file_change_status': 'bool'
    }

    attribute_map = {
        'risky_account_status': 'risky_account_status',
        'abnormal_login_status': 'abnormal_login_status',
        'malicious_program_status': 'malicious_program_status',
        'webshell_status': 'webshell_status',
        'account_crack_status': 'account_crack_status',
        'critical_file_change_status': 'critical_file_change_status'
    }

    def __init__(self, risky_account_status=None, abnormal_login_status=None, malicious_program_status=None, webshell_status=None, account_crack_status=None, critical_file_change_status=None):
        r"""IntrusionSubscriptionReq

        The model defined in huaweicloud sdk

        :param risky_account_status: **参数解释**： 风险账号是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 
        :type risky_account_status: bool
        :param abnormal_login_status: **参数解释**： 异地登录是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 
        :type abnormal_login_status: bool
        :param malicious_program_status: **参数解释**： 恶意程序是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 
        :type malicious_program_status: bool
        :param webshell_status: **参数解释**： 网站后门是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 
        :type webshell_status: bool
        :param account_crack_status: **参数解释**： 账号破解是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 
        :type account_crack_status: bool
        :param critical_file_change_status: **参数解释**： 关键文件变更是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 
        :type critical_file_change_status: bool
        """
        
        

        self._risky_account_status = None
        self._abnormal_login_status = None
        self._malicious_program_status = None
        self._webshell_status = None
        self._account_crack_status = None
        self._critical_file_change_status = None
        self.discriminator = None

        if risky_account_status is not None:
            self.risky_account_status = risky_account_status
        if abnormal_login_status is not None:
            self.abnormal_login_status = abnormal_login_status
        if malicious_program_status is not None:
            self.malicious_program_status = malicious_program_status
        if webshell_status is not None:
            self.webshell_status = webshell_status
        if account_crack_status is not None:
            self.account_crack_status = account_crack_status
        if critical_file_change_status is not None:
            self.critical_file_change_status = critical_file_change_status

    @property
    def risky_account_status(self):
        r"""Gets the risky_account_status of this IntrusionSubscriptionReq.

        **参数解释**： 风险账号是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :return: The risky_account_status of this IntrusionSubscriptionReq.
        :rtype: bool
        """
        return self._risky_account_status

    @risky_account_status.setter
    def risky_account_status(self, risky_account_status):
        r"""Sets the risky_account_status of this IntrusionSubscriptionReq.

        **参数解释**： 风险账号是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :param risky_account_status: The risky_account_status of this IntrusionSubscriptionReq.
        :type risky_account_status: bool
        """
        self._risky_account_status = risky_account_status

    @property
    def abnormal_login_status(self):
        r"""Gets the abnormal_login_status of this IntrusionSubscriptionReq.

        **参数解释**： 异地登录是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :return: The abnormal_login_status of this IntrusionSubscriptionReq.
        :rtype: bool
        """
        return self._abnormal_login_status

    @abnormal_login_status.setter
    def abnormal_login_status(self, abnormal_login_status):
        r"""Sets the abnormal_login_status of this IntrusionSubscriptionReq.

        **参数解释**： 异地登录是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :param abnormal_login_status: The abnormal_login_status of this IntrusionSubscriptionReq.
        :type abnormal_login_status: bool
        """
        self._abnormal_login_status = abnormal_login_status

    @property
    def malicious_program_status(self):
        r"""Gets the malicious_program_status of this IntrusionSubscriptionReq.

        **参数解释**： 恶意程序是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :return: The malicious_program_status of this IntrusionSubscriptionReq.
        :rtype: bool
        """
        return self._malicious_program_status

    @malicious_program_status.setter
    def malicious_program_status(self, malicious_program_status):
        r"""Sets the malicious_program_status of this IntrusionSubscriptionReq.

        **参数解释**： 恶意程序是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :param malicious_program_status: The malicious_program_status of this IntrusionSubscriptionReq.
        :type malicious_program_status: bool
        """
        self._malicious_program_status = malicious_program_status

    @property
    def webshell_status(self):
        r"""Gets the webshell_status of this IntrusionSubscriptionReq.

        **参数解释**： 网站后门是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :return: The webshell_status of this IntrusionSubscriptionReq.
        :rtype: bool
        """
        return self._webshell_status

    @webshell_status.setter
    def webshell_status(self, webshell_status):
        r"""Sets the webshell_status of this IntrusionSubscriptionReq.

        **参数解释**： 网站后门是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :param webshell_status: The webshell_status of this IntrusionSubscriptionReq.
        :type webshell_status: bool
        """
        self._webshell_status = webshell_status

    @property
    def account_crack_status(self):
        r"""Gets the account_crack_status of this IntrusionSubscriptionReq.

        **参数解释**： 账号破解是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :return: The account_crack_status of this IntrusionSubscriptionReq.
        :rtype: bool
        """
        return self._account_crack_status

    @account_crack_status.setter
    def account_crack_status(self, account_crack_status):
        r"""Sets the account_crack_status of this IntrusionSubscriptionReq.

        **参数解释**： 账号破解是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :param account_crack_status: The account_crack_status of this IntrusionSubscriptionReq.
        :type account_crack_status: bool
        """
        self._account_crack_status = account_crack_status

    @property
    def critical_file_change_status(self):
        r"""Gets the critical_file_change_status of this IntrusionSubscriptionReq.

        **参数解释**： 关键文件变更是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :return: The critical_file_change_status of this IntrusionSubscriptionReq.
        :rtype: bool
        """
        return self._critical_file_change_status

    @critical_file_change_status.setter
    def critical_file_change_status(self, critical_file_change_status):
        r"""Sets the critical_file_change_status of this IntrusionSubscriptionReq.

        **参数解释**： 关键文件变更是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :param critical_file_change_status: The critical_file_change_status of this IntrusionSubscriptionReq.
        :type critical_file_change_status: bool
        """
        self._critical_file_change_status = critical_file_change_status

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
        if not isinstance(other, IntrusionSubscriptionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
