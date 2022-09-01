# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoginPolicyOption:

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
        """LoginPolicyOption

        The model defined in huaweicloud sdk

        :param account_validity_period: 账号在该值设置的有效期内未使用，则被停用。
        :type account_validity_period: int
        :param custom_info_for_login: 登录提示信息。
        :type custom_info_for_login: str
        :param lockout_duration: 帐号锁定时长（分钟），取值范围[15,30]。
        :type lockout_duration: int
        :param login_failed_times: 限定时间内登录失败次数，取值范围[3,10]。
        :type login_failed_times: int
        :param period_with_login_failures: 限定时间长度（分钟），取值范围[15,60]。
        :type period_with_login_failures: int
        :param session_timeout: 登录会话失效时间，取值范围[15,1440]。
        :type session_timeout: int
        :param show_recent_login_info: 显示最近一次的登录信息。取值范围true或false。
        :type show_recent_login_info: bool
        """
        
        

        self._account_validity_period = None
        self._custom_info_for_login = None
        self._lockout_duration = None
        self._login_failed_times = None
        self._period_with_login_failures = None
        self._session_timeout = None
        self._show_recent_login_info = None
        self.discriminator = None

        if account_validity_period is not None:
            self.account_validity_period = account_validity_period
        if custom_info_for_login is not None:
            self.custom_info_for_login = custom_info_for_login
        if lockout_duration is not None:
            self.lockout_duration = lockout_duration
        if login_failed_times is not None:
            self.login_failed_times = login_failed_times
        if period_with_login_failures is not None:
            self.period_with_login_failures = period_with_login_failures
        if session_timeout is not None:
            self.session_timeout = session_timeout
        if show_recent_login_info is not None:
            self.show_recent_login_info = show_recent_login_info

    @property
    def account_validity_period(self):
        """Gets the account_validity_period of this LoginPolicyOption.

        账号在该值设置的有效期内未使用，则被停用。

        :return: The account_validity_period of this LoginPolicyOption.
        :rtype: int
        """
        return self._account_validity_period

    @account_validity_period.setter
    def account_validity_period(self, account_validity_period):
        """Sets the account_validity_period of this LoginPolicyOption.

        账号在该值设置的有效期内未使用，则被停用。

        :param account_validity_period: The account_validity_period of this LoginPolicyOption.
        :type account_validity_period: int
        """
        self._account_validity_period = account_validity_period

    @property
    def custom_info_for_login(self):
        """Gets the custom_info_for_login of this LoginPolicyOption.

        登录提示信息。

        :return: The custom_info_for_login of this LoginPolicyOption.
        :rtype: str
        """
        return self._custom_info_for_login

    @custom_info_for_login.setter
    def custom_info_for_login(self, custom_info_for_login):
        """Sets the custom_info_for_login of this LoginPolicyOption.

        登录提示信息。

        :param custom_info_for_login: The custom_info_for_login of this LoginPolicyOption.
        :type custom_info_for_login: str
        """
        self._custom_info_for_login = custom_info_for_login

    @property
    def lockout_duration(self):
        """Gets the lockout_duration of this LoginPolicyOption.

        帐号锁定时长（分钟），取值范围[15,30]。

        :return: The lockout_duration of this LoginPolicyOption.
        :rtype: int
        """
        return self._lockout_duration

    @lockout_duration.setter
    def lockout_duration(self, lockout_duration):
        """Sets the lockout_duration of this LoginPolicyOption.

        帐号锁定时长（分钟），取值范围[15,30]。

        :param lockout_duration: The lockout_duration of this LoginPolicyOption.
        :type lockout_duration: int
        """
        self._lockout_duration = lockout_duration

    @property
    def login_failed_times(self):
        """Gets the login_failed_times of this LoginPolicyOption.

        限定时间内登录失败次数，取值范围[3,10]。

        :return: The login_failed_times of this LoginPolicyOption.
        :rtype: int
        """
        return self._login_failed_times

    @login_failed_times.setter
    def login_failed_times(self, login_failed_times):
        """Sets the login_failed_times of this LoginPolicyOption.

        限定时间内登录失败次数，取值范围[3,10]。

        :param login_failed_times: The login_failed_times of this LoginPolicyOption.
        :type login_failed_times: int
        """
        self._login_failed_times = login_failed_times

    @property
    def period_with_login_failures(self):
        """Gets the period_with_login_failures of this LoginPolicyOption.

        限定时间长度（分钟），取值范围[15,60]。

        :return: The period_with_login_failures of this LoginPolicyOption.
        :rtype: int
        """
        return self._period_with_login_failures

    @period_with_login_failures.setter
    def period_with_login_failures(self, period_with_login_failures):
        """Sets the period_with_login_failures of this LoginPolicyOption.

        限定时间长度（分钟），取值范围[15,60]。

        :param period_with_login_failures: The period_with_login_failures of this LoginPolicyOption.
        :type period_with_login_failures: int
        """
        self._period_with_login_failures = period_with_login_failures

    @property
    def session_timeout(self):
        """Gets the session_timeout of this LoginPolicyOption.

        登录会话失效时间，取值范围[15,1440]。

        :return: The session_timeout of this LoginPolicyOption.
        :rtype: int
        """
        return self._session_timeout

    @session_timeout.setter
    def session_timeout(self, session_timeout):
        """Sets the session_timeout of this LoginPolicyOption.

        登录会话失效时间，取值范围[15,1440]。

        :param session_timeout: The session_timeout of this LoginPolicyOption.
        :type session_timeout: int
        """
        self._session_timeout = session_timeout

    @property
    def show_recent_login_info(self):
        """Gets the show_recent_login_info of this LoginPolicyOption.

        显示最近一次的登录信息。取值范围true或false。

        :return: The show_recent_login_info of this LoginPolicyOption.
        :rtype: bool
        """
        return self._show_recent_login_info

    @show_recent_login_info.setter
    def show_recent_login_info(self, show_recent_login_info):
        """Sets the show_recent_login_info of this LoginPolicyOption.

        显示最近一次的登录信息。取值范围true或false。

        :param show_recent_login_info: The show_recent_login_info of this LoginPolicyOption.
        :type show_recent_login_info: bool
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
        if not isinstance(other, LoginPolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
