# coding: utf-8

import pprint
import re

import six





class LoginPolicyResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'account_validity_period': 'int',
        'custom_info_for_login': 'str',
        'lockout_duration': 'int',
        'login_failed_times': 'int',
        'period_with_login_failures': 'int',
        'session_timeout': 'int',
        'show_recent_login_info': 'bool'
    }

    attribute_map = {
        'account_validity_period': 'account_validity_period',
        'custom_info_for_login': 'custom_info_for_login',
        'lockout_duration': 'lockout_duration',
        'login_failed_times': 'login_failed_times',
        'period_with_login_failures': 'period_with_login_failures',
        'session_timeout': 'session_timeout',
        'show_recent_login_info': 'show_recent_login_info'
    }

    def __init__(self, account_validity_period=None, custom_info_for_login=None, lockout_duration=None, login_failed_times=None, period_with_login_failures=None, session_timeout=None, show_recent_login_info=None):
        """LoginPolicyResult - a model defined in huaweicloud sdk"""
        
        

        self._account_validity_period = None
        self._custom_info_for_login = None
        self._lockout_duration = None
        self._login_failed_times = None
        self._period_with_login_failures = None
        self._session_timeout = None
        self._show_recent_login_info = None
        self.discriminator = None

        self.account_validity_period = account_validity_period
        self.custom_info_for_login = custom_info_for_login
        self.lockout_duration = lockout_duration
        self.login_failed_times = login_failed_times
        self.period_with_login_failures = period_with_login_failures
        self.session_timeout = session_timeout
        self.show_recent_login_info = show_recent_login_info

    @property
    def account_validity_period(self):
        """Gets the account_validity_period of this LoginPolicyResult.

        账号在该值设置的有效期内未使用，则被停用。

        :return: The account_validity_period of this LoginPolicyResult.
        :rtype: int
        """
        return self._account_validity_period

    @account_validity_period.setter
    def account_validity_period(self, account_validity_period):
        """Sets the account_validity_period of this LoginPolicyResult.

        账号在该值设置的有效期内未使用，则被停用。

        :param account_validity_period: The account_validity_period of this LoginPolicyResult.
        :type: int
        """
        self._account_validity_period = account_validity_period

    @property
    def custom_info_for_login(self):
        """Gets the custom_info_for_login of this LoginPolicyResult.

        登录提示信息。

        :return: The custom_info_for_login of this LoginPolicyResult.
        :rtype: str
        """
        return self._custom_info_for_login

    @custom_info_for_login.setter
    def custom_info_for_login(self, custom_info_for_login):
        """Sets the custom_info_for_login of this LoginPolicyResult.

        登录提示信息。

        :param custom_info_for_login: The custom_info_for_login of this LoginPolicyResult.
        :type: str
        """
        self._custom_info_for_login = custom_info_for_login

    @property
    def lockout_duration(self):
        """Gets the lockout_duration of this LoginPolicyResult.

        帐号锁定时长（分钟）。

        :return: The lockout_duration of this LoginPolicyResult.
        :rtype: int
        """
        return self._lockout_duration

    @lockout_duration.setter
    def lockout_duration(self, lockout_duration):
        """Sets the lockout_duration of this LoginPolicyResult.

        帐号锁定时长（分钟）。

        :param lockout_duration: The lockout_duration of this LoginPolicyResult.
        :type: int
        """
        self._lockout_duration = lockout_duration

    @property
    def login_failed_times(self):
        """Gets the login_failed_times of this LoginPolicyResult.

        限定时间内登录失败次数。

        :return: The login_failed_times of this LoginPolicyResult.
        :rtype: int
        """
        return self._login_failed_times

    @login_failed_times.setter
    def login_failed_times(self, login_failed_times):
        """Sets the login_failed_times of this LoginPolicyResult.

        限定时间内登录失败次数。

        :param login_failed_times: The login_failed_times of this LoginPolicyResult.
        :type: int
        """
        self._login_failed_times = login_failed_times

    @property
    def period_with_login_failures(self):
        """Gets the period_with_login_failures of this LoginPolicyResult.

        限定时间长度（分钟）。

        :return: The period_with_login_failures of this LoginPolicyResult.
        :rtype: int
        """
        return self._period_with_login_failures

    @period_with_login_failures.setter
    def period_with_login_failures(self, period_with_login_failures):
        """Sets the period_with_login_failures of this LoginPolicyResult.

        限定时间长度（分钟）。

        :param period_with_login_failures: The period_with_login_failures of this LoginPolicyResult.
        :type: int
        """
        self._period_with_login_failures = period_with_login_failures

    @property
    def session_timeout(self):
        """Gets the session_timeout of this LoginPolicyResult.

        登录会话失效时间。

        :return: The session_timeout of this LoginPolicyResult.
        :rtype: int
        """
        return self._session_timeout

    @session_timeout.setter
    def session_timeout(self, session_timeout):
        """Sets the session_timeout of this LoginPolicyResult.

        登录会话失效时间。

        :param session_timeout: The session_timeout of this LoginPolicyResult.
        :type: int
        """
        self._session_timeout = session_timeout

    @property
    def show_recent_login_info(self):
        """Gets the show_recent_login_info of this LoginPolicyResult.

        是否显示最近一次的登录信息。

        :return: The show_recent_login_info of this LoginPolicyResult.
        :rtype: bool
        """
        return self._show_recent_login_info

    @show_recent_login_info.setter
    def show_recent_login_info(self, show_recent_login_info):
        """Sets the show_recent_login_info of this LoginPolicyResult.

        是否显示最近一次的登录信息。

        :param show_recent_login_info: The show_recent_login_info of this LoginPolicyResult.
        :type: bool
        """
        self._show_recent_login_info = show_recent_login_info

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LoginPolicyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
