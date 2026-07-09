# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'require_eip': 'str',
        'iam_login': 'str',
        'admin_login': 'str',
        'float_ipv6': 'str'
    }

    attribute_map = {
        'require_eip': 'require_eip',
        'iam_login': 'iam_login',
        'admin_login': 'admin_login',
        'float_ipv6': 'float_ipv6'
    }

    def __init__(self, require_eip=None, iam_login=None, admin_login=None, float_ipv6=None):
        r"""VersionInfo

        The model defined in huaweicloud sdk

        :param require_eip: 支持EIP的实例版本。
        :type require_eip: str
        :param iam_login: 支持IAM登录的实例版本。
        :type iam_login: str
        :param admin_login: 支持管理员登录的实例版本。
        :type admin_login: str
        :param float_ipv6: 支持浮动IPv6的实例版本。
        :type float_ipv6: str
        """
        
        

        self._require_eip = None
        self._iam_login = None
        self._admin_login = None
        self._float_ipv6 = None
        self.discriminator = None

        if require_eip is not None:
            self.require_eip = require_eip
        if iam_login is not None:
            self.iam_login = iam_login
        if admin_login is not None:
            self.admin_login = admin_login
        if float_ipv6 is not None:
            self.float_ipv6 = float_ipv6

    @property
    def require_eip(self):
        r"""Gets the require_eip of this VersionInfo.

        支持EIP的实例版本。

        :return: The require_eip of this VersionInfo.
        :rtype: str
        """
        return self._require_eip

    @require_eip.setter
    def require_eip(self, require_eip):
        r"""Sets the require_eip of this VersionInfo.

        支持EIP的实例版本。

        :param require_eip: The require_eip of this VersionInfo.
        :type require_eip: str
        """
        self._require_eip = require_eip

    @property
    def iam_login(self):
        r"""Gets the iam_login of this VersionInfo.

        支持IAM登录的实例版本。

        :return: The iam_login of this VersionInfo.
        :rtype: str
        """
        return self._iam_login

    @iam_login.setter
    def iam_login(self, iam_login):
        r"""Sets the iam_login of this VersionInfo.

        支持IAM登录的实例版本。

        :param iam_login: The iam_login of this VersionInfo.
        :type iam_login: str
        """
        self._iam_login = iam_login

    @property
    def admin_login(self):
        r"""Gets the admin_login of this VersionInfo.

        支持管理员登录的实例版本。

        :return: The admin_login of this VersionInfo.
        :rtype: str
        """
        return self._admin_login

    @admin_login.setter
    def admin_login(self, admin_login):
        r"""Sets the admin_login of this VersionInfo.

        支持管理员登录的实例版本。

        :param admin_login: The admin_login of this VersionInfo.
        :type admin_login: str
        """
        self._admin_login = admin_login

    @property
    def float_ipv6(self):
        r"""Gets the float_ipv6 of this VersionInfo.

        支持浮动IPv6的实例版本。

        :return: The float_ipv6 of this VersionInfo.
        :rtype: str
        """
        return self._float_ipv6

    @float_ipv6.setter
    def float_ipv6(self, float_ipv6):
        r"""Sets the float_ipv6 of this VersionInfo.

        支持浮动IPv6的实例版本。

        :param float_ipv6: The float_ipv6 of this VersionInfo.
        :type float_ipv6: str
        """
        self._float_ipv6 = float_ipv6

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
        if not isinstance(other, VersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
