# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoginProtectResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'user_id': 'str',
        'verification_method': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'user_id': 'user_id',
        'verification_method': 'verification_method'
    }

    def __init__(self, enabled=None, user_id=None, verification_method=None):
        r"""LoginProtectResult

        The model defined in huaweicloud sdk

        :param enabled: IAM用户是否开启登录保护，开启为\&quot;true\&quot;，未开启为\&quot;false\&quot;。
        :type enabled: bool
        :param user_id: IAM用户ID。
        :type user_id: str
        :param verification_method: IAM用户登录验证方式。
        :type verification_method: str
        """
        
        

        self._enabled = None
        self._user_id = None
        self._verification_method = None
        self.discriminator = None

        self.enabled = enabled
        self.user_id = user_id
        self.verification_method = verification_method

    @property
    def enabled(self):
        r"""Gets the enabled of this LoginProtectResult.

        IAM用户是否开启登录保护，开启为\"true\"，未开启为\"false\"。

        :return: The enabled of this LoginProtectResult.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this LoginProtectResult.

        IAM用户是否开启登录保护，开启为\"true\"，未开启为\"false\"。

        :param enabled: The enabled of this LoginProtectResult.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def user_id(self):
        r"""Gets the user_id of this LoginProtectResult.

        IAM用户ID。

        :return: The user_id of this LoginProtectResult.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this LoginProtectResult.

        IAM用户ID。

        :param user_id: The user_id of this LoginProtectResult.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def verification_method(self):
        r"""Gets the verification_method of this LoginProtectResult.

        IAM用户登录验证方式。

        :return: The verification_method of this LoginProtectResult.
        :rtype: str
        """
        return self._verification_method

    @verification_method.setter
    def verification_method(self, verification_method):
        r"""Sets the verification_method of this LoginProtectResult.

        IAM用户登录验证方式。

        :param verification_method: The verification_method of this LoginProtectResult.
        :type verification_method: str
        """
        self._verification_method = verification_method

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
        if not isinstance(other, LoginProtectResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
