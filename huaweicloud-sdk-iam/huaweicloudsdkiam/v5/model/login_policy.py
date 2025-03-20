# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoginPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_validity_period': 'int',
        'custom_info_for_login': 'str',
        'lockout_duration': 'int',
        'login_failed_times': 'int',
        'period_with_login_failures': 'int',
        'session_timeout': 'int',
        'show_recent_login_info': 'bool',
        'allow_address_netmasks': 'list[AllowAddressNetmask]',
        'allow_ip_ranges': 'list[AllowIpRange]'
    }

    attribute_map = {
        'user_validity_period': 'user_validity_period',
        'custom_info_for_login': 'custom_info_for_login',
        'lockout_duration': 'lockout_duration',
        'login_failed_times': 'login_failed_times',
        'period_with_login_failures': 'period_with_login_failures',
        'session_timeout': 'session_timeout',
        'show_recent_login_info': 'show_recent_login_info',
        'allow_address_netmasks': 'allow_address_netmasks',
        'allow_ip_ranges': 'allow_ip_ranges'
    }

    def __init__(self, user_validity_period=None, custom_info_for_login=None, lockout_duration=None, login_failed_times=None, period_with_login_failures=None, session_timeout=None, show_recent_login_info=None, allow_address_netmasks=None, allow_ip_ranges=None):
        """LoginPolicy

        The model defined in huaweicloud sdk

        :param user_validity_period: 如果IAM用户在该值设置的有效期（天）内未登录，则被停用，不适用于根用户。
        :type user_validity_period: int
        :param custom_info_for_login: 登录提示信息。
        :type custom_info_for_login: str
        :param lockout_duration: IAM用户登录锁定时长（分钟）。
        :type lockout_duration: int
        :param login_failed_times: 限定时间内登录失败次数。
        :type login_failed_times: int
        :param period_with_login_failures: 限定时间长度（分钟）。
        :type period_with_login_failures: int
        :param session_timeout: 登录会话失效时间。
        :type session_timeout: int
        :param show_recent_login_info: 是否显示最近一次的登录信息。
        :type show_recent_login_info: bool
        :param allow_address_netmasks: 允许访问的IP地址或网段。
        :type allow_address_netmasks: list[:class:`huaweicloudsdkiam.v5.AllowAddressNetmask`]
        :param allow_ip_ranges: 允许访问的IP地址区间。
        :type allow_ip_ranges: list[:class:`huaweicloudsdkiam.v5.AllowIpRange`]
        """
        
        

        self._user_validity_period = None
        self._custom_info_for_login = None
        self._lockout_duration = None
        self._login_failed_times = None
        self._period_with_login_failures = None
        self._session_timeout = None
        self._show_recent_login_info = None
        self._allow_address_netmasks = None
        self._allow_ip_ranges = None
        self.discriminator = None

        self.user_validity_period = user_validity_period
        self.custom_info_for_login = custom_info_for_login
        self.lockout_duration = lockout_duration
        self.login_failed_times = login_failed_times
        self.period_with_login_failures = period_with_login_failures
        self.session_timeout = session_timeout
        self.show_recent_login_info = show_recent_login_info
        if allow_address_netmasks is not None:
            self.allow_address_netmasks = allow_address_netmasks
        if allow_ip_ranges is not None:
            self.allow_ip_ranges = allow_ip_ranges

    @property
    def user_validity_period(self):
        """Gets the user_validity_period of this LoginPolicy.

        如果IAM用户在该值设置的有效期（天）内未登录，则被停用，不适用于根用户。

        :return: The user_validity_period of this LoginPolicy.
        :rtype: int
        """
        return self._user_validity_period

    @user_validity_period.setter
    def user_validity_period(self, user_validity_period):
        """Sets the user_validity_period of this LoginPolicy.

        如果IAM用户在该值设置的有效期（天）内未登录，则被停用，不适用于根用户。

        :param user_validity_period: The user_validity_period of this LoginPolicy.
        :type user_validity_period: int
        """
        self._user_validity_period = user_validity_period

    @property
    def custom_info_for_login(self):
        """Gets the custom_info_for_login of this LoginPolicy.

        登录提示信息。

        :return: The custom_info_for_login of this LoginPolicy.
        :rtype: str
        """
        return self._custom_info_for_login

    @custom_info_for_login.setter
    def custom_info_for_login(self, custom_info_for_login):
        """Sets the custom_info_for_login of this LoginPolicy.

        登录提示信息。

        :param custom_info_for_login: The custom_info_for_login of this LoginPolicy.
        :type custom_info_for_login: str
        """
        self._custom_info_for_login = custom_info_for_login

    @property
    def lockout_duration(self):
        """Gets the lockout_duration of this LoginPolicy.

        IAM用户登录锁定时长（分钟）。

        :return: The lockout_duration of this LoginPolicy.
        :rtype: int
        """
        return self._lockout_duration

    @lockout_duration.setter
    def lockout_duration(self, lockout_duration):
        """Sets the lockout_duration of this LoginPolicy.

        IAM用户登录锁定时长（分钟）。

        :param lockout_duration: The lockout_duration of this LoginPolicy.
        :type lockout_duration: int
        """
        self._lockout_duration = lockout_duration

    @property
    def login_failed_times(self):
        """Gets the login_failed_times of this LoginPolicy.

        限定时间内登录失败次数。

        :return: The login_failed_times of this LoginPolicy.
        :rtype: int
        """
        return self._login_failed_times

    @login_failed_times.setter
    def login_failed_times(self, login_failed_times):
        """Sets the login_failed_times of this LoginPolicy.

        限定时间内登录失败次数。

        :param login_failed_times: The login_failed_times of this LoginPolicy.
        :type login_failed_times: int
        """
        self._login_failed_times = login_failed_times

    @property
    def period_with_login_failures(self):
        """Gets the period_with_login_failures of this LoginPolicy.

        限定时间长度（分钟）。

        :return: The period_with_login_failures of this LoginPolicy.
        :rtype: int
        """
        return self._period_with_login_failures

    @period_with_login_failures.setter
    def period_with_login_failures(self, period_with_login_failures):
        """Sets the period_with_login_failures of this LoginPolicy.

        限定时间长度（分钟）。

        :param period_with_login_failures: The period_with_login_failures of this LoginPolicy.
        :type period_with_login_failures: int
        """
        self._period_with_login_failures = period_with_login_failures

    @property
    def session_timeout(self):
        """Gets the session_timeout of this LoginPolicy.

        登录会话失效时间。

        :return: The session_timeout of this LoginPolicy.
        :rtype: int
        """
        return self._session_timeout

    @session_timeout.setter
    def session_timeout(self, session_timeout):
        """Sets the session_timeout of this LoginPolicy.

        登录会话失效时间。

        :param session_timeout: The session_timeout of this LoginPolicy.
        :type session_timeout: int
        """
        self._session_timeout = session_timeout

    @property
    def show_recent_login_info(self):
        """Gets the show_recent_login_info of this LoginPolicy.

        是否显示最近一次的登录信息。

        :return: The show_recent_login_info of this LoginPolicy.
        :rtype: bool
        """
        return self._show_recent_login_info

    @show_recent_login_info.setter
    def show_recent_login_info(self, show_recent_login_info):
        """Sets the show_recent_login_info of this LoginPolicy.

        是否显示最近一次的登录信息。

        :param show_recent_login_info: The show_recent_login_info of this LoginPolicy.
        :type show_recent_login_info: bool
        """
        self._show_recent_login_info = show_recent_login_info

    @property
    def allow_address_netmasks(self):
        """Gets the allow_address_netmasks of this LoginPolicy.

        允许访问的IP地址或网段。

        :return: The allow_address_netmasks of this LoginPolicy.
        :rtype: list[:class:`huaweicloudsdkiam.v5.AllowAddressNetmask`]
        """
        return self._allow_address_netmasks

    @allow_address_netmasks.setter
    def allow_address_netmasks(self, allow_address_netmasks):
        """Sets the allow_address_netmasks of this LoginPolicy.

        允许访问的IP地址或网段。

        :param allow_address_netmasks: The allow_address_netmasks of this LoginPolicy.
        :type allow_address_netmasks: list[:class:`huaweicloudsdkiam.v5.AllowAddressNetmask`]
        """
        self._allow_address_netmasks = allow_address_netmasks

    @property
    def allow_ip_ranges(self):
        """Gets the allow_ip_ranges of this LoginPolicy.

        允许访问的IP地址区间。

        :return: The allow_ip_ranges of this LoginPolicy.
        :rtype: list[:class:`huaweicloudsdkiam.v5.AllowIpRange`]
        """
        return self._allow_ip_ranges

    @allow_ip_ranges.setter
    def allow_ip_ranges(self, allow_ip_ranges):
        """Sets the allow_ip_ranges of this LoginPolicy.

        允许访问的IP地址区间。

        :param allow_ip_ranges: The allow_ip_ranges of this LoginPolicy.
        :type allow_ip_ranges: list[:class:`huaweicloudsdkiam.v5.AllowIpRange`]
        """
        self._allow_ip_ranges = allow_ip_ranges

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
        if not isinstance(other, LoginPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
