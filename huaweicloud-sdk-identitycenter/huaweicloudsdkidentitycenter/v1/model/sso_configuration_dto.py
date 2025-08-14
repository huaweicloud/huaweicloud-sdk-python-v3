# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SSOConfigurationDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mfa_mode': 'str',
        'no_mfa_signin_behavior': 'str',
        'no_password_signin_behavior': 'str',
        'allowed_mfa_types': 'list[str]',
        'session_configuration': 'SessionConfigurationDto'
    }

    attribute_map = {
        'mfa_mode': 'mfa_mode',
        'no_mfa_signin_behavior': 'no_mfa_signin_behavior',
        'no_password_signin_behavior': 'no_password_signin_behavior',
        'allowed_mfa_types': 'allowed_mfa_types',
        'session_configuration': 'session_configuration'
    }

    def __init__(self, mfa_mode=None, no_mfa_signin_behavior=None, no_password_signin_behavior=None, allowed_mfa_types=None, session_configuration=None):
        r"""SSOConfigurationDto

        The model defined in huaweicloud sdk

        :param mfa_mode: MFA生效模式
        :type mfa_mode: str
        :param no_mfa_signin_behavior: 未注册MFA情况下，可选择的登录行为
        :type no_mfa_signin_behavior: str
        :param no_password_signin_behavior: 没有密码情况下登录的行为
        :type no_password_signin_behavior: str
        :param allowed_mfa_types: 允许的MFA类型
        :type allowed_mfa_types: list[str]
        :param session_configuration: 
        :type session_configuration: :class:`huaweicloudsdkidentitycenter.v1.SessionConfigurationDto`
        """
        
        

        self._mfa_mode = None
        self._no_mfa_signin_behavior = None
        self._no_password_signin_behavior = None
        self._allowed_mfa_types = None
        self._session_configuration = None
        self.discriminator = None

        if mfa_mode is not None:
            self.mfa_mode = mfa_mode
        if no_mfa_signin_behavior is not None:
            self.no_mfa_signin_behavior = no_mfa_signin_behavior
        if no_password_signin_behavior is not None:
            self.no_password_signin_behavior = no_password_signin_behavior
        if allowed_mfa_types is not None:
            self.allowed_mfa_types = allowed_mfa_types
        if session_configuration is not None:
            self.session_configuration = session_configuration

    @property
    def mfa_mode(self):
        r"""Gets the mfa_mode of this SSOConfigurationDto.

        MFA生效模式

        :return: The mfa_mode of this SSOConfigurationDto.
        :rtype: str
        """
        return self._mfa_mode

    @mfa_mode.setter
    def mfa_mode(self, mfa_mode):
        r"""Sets the mfa_mode of this SSOConfigurationDto.

        MFA生效模式

        :param mfa_mode: The mfa_mode of this SSOConfigurationDto.
        :type mfa_mode: str
        """
        self._mfa_mode = mfa_mode

    @property
    def no_mfa_signin_behavior(self):
        r"""Gets the no_mfa_signin_behavior of this SSOConfigurationDto.

        未注册MFA情况下，可选择的登录行为

        :return: The no_mfa_signin_behavior of this SSOConfigurationDto.
        :rtype: str
        """
        return self._no_mfa_signin_behavior

    @no_mfa_signin_behavior.setter
    def no_mfa_signin_behavior(self, no_mfa_signin_behavior):
        r"""Sets the no_mfa_signin_behavior of this SSOConfigurationDto.

        未注册MFA情况下，可选择的登录行为

        :param no_mfa_signin_behavior: The no_mfa_signin_behavior of this SSOConfigurationDto.
        :type no_mfa_signin_behavior: str
        """
        self._no_mfa_signin_behavior = no_mfa_signin_behavior

    @property
    def no_password_signin_behavior(self):
        r"""Gets the no_password_signin_behavior of this SSOConfigurationDto.

        没有密码情况下登录的行为

        :return: The no_password_signin_behavior of this SSOConfigurationDto.
        :rtype: str
        """
        return self._no_password_signin_behavior

    @no_password_signin_behavior.setter
    def no_password_signin_behavior(self, no_password_signin_behavior):
        r"""Sets the no_password_signin_behavior of this SSOConfigurationDto.

        没有密码情况下登录的行为

        :param no_password_signin_behavior: The no_password_signin_behavior of this SSOConfigurationDto.
        :type no_password_signin_behavior: str
        """
        self._no_password_signin_behavior = no_password_signin_behavior

    @property
    def allowed_mfa_types(self):
        r"""Gets the allowed_mfa_types of this SSOConfigurationDto.

        允许的MFA类型

        :return: The allowed_mfa_types of this SSOConfigurationDto.
        :rtype: list[str]
        """
        return self._allowed_mfa_types

    @allowed_mfa_types.setter
    def allowed_mfa_types(self, allowed_mfa_types):
        r"""Sets the allowed_mfa_types of this SSOConfigurationDto.

        允许的MFA类型

        :param allowed_mfa_types: The allowed_mfa_types of this SSOConfigurationDto.
        :type allowed_mfa_types: list[str]
        """
        self._allowed_mfa_types = allowed_mfa_types

    @property
    def session_configuration(self):
        r"""Gets the session_configuration of this SSOConfigurationDto.

        :return: The session_configuration of this SSOConfigurationDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.SessionConfigurationDto`
        """
        return self._session_configuration

    @session_configuration.setter
    def session_configuration(self, session_configuration):
        r"""Sets the session_configuration of this SSOConfigurationDto.

        :param session_configuration: The session_configuration of this SSOConfigurationDto.
        :type session_configuration: :class:`huaweicloudsdkidentitycenter.v1.SessionConfigurationDto`
        """
        self._session_configuration = session_configuration

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
        if not isinstance(other, SSOConfigurationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
