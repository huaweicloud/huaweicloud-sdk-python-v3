# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateDcRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'dc_ip': 'str',
        'dc_name': 'str',
        'domain_admin_account': 'str',
        'domain_password': 'str',
        'is_ldaps_enable': 'bool',
        'ldaps_certificate': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'dc_ip': 'dc_ip',
        'dc_name': 'dc_name',
        'domain_admin_account': 'domain_admin_account',
        'domain_password': 'domain_password',
        'is_ldaps_enable': 'is_ldaps_enable',
        'ldaps_certificate': 'ldaps_certificate'
    }

    def __init__(self, domain=None, dc_ip=None, dc_name=None, domain_admin_account=None, domain_password=None, is_ldaps_enable=None, ldaps_certificate=None):
        r"""ValidateDcRequestBody

        The model defined in huaweicloud sdk

        :param domain: 域名。
        :type domain: str
        :param dc_ip: 域控制器IP地址。
        :type dc_ip: str
        :param dc_name: 域控制器名称。
        :type dc_name: str
        :param domain_admin_account: 域管理员账号。
        :type domain_admin_account: str
        :param domain_password: 域管理员账号密码。
        :type domain_password: str
        :param is_ldaps_enable: 是否开启LDAPS。
        :type is_ldaps_enable: bool
        :param ldaps_certificate: LDAPS用的密钥证书。
        :type ldaps_certificate: str
        """
        
        

        self._domain = None
        self._dc_ip = None
        self._dc_name = None
        self._domain_admin_account = None
        self._domain_password = None
        self._is_ldaps_enable = None
        self._ldaps_certificate = None
        self.discriminator = None

        self.domain = domain
        self.dc_ip = dc_ip
        self.dc_name = dc_name
        if domain_admin_account is not None:
            self.domain_admin_account = domain_admin_account
        if domain_password is not None:
            self.domain_password = domain_password
        if is_ldaps_enable is not None:
            self.is_ldaps_enable = is_ldaps_enable
        if ldaps_certificate is not None:
            self.ldaps_certificate = ldaps_certificate

    @property
    def domain(self):
        r"""Gets the domain of this ValidateDcRequestBody.

        域名。

        :return: The domain of this ValidateDcRequestBody.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ValidateDcRequestBody.

        域名。

        :param domain: The domain of this ValidateDcRequestBody.
        :type domain: str
        """
        self._domain = domain

    @property
    def dc_ip(self):
        r"""Gets the dc_ip of this ValidateDcRequestBody.

        域控制器IP地址。

        :return: The dc_ip of this ValidateDcRequestBody.
        :rtype: str
        """
        return self._dc_ip

    @dc_ip.setter
    def dc_ip(self, dc_ip):
        r"""Sets the dc_ip of this ValidateDcRequestBody.

        域控制器IP地址。

        :param dc_ip: The dc_ip of this ValidateDcRequestBody.
        :type dc_ip: str
        """
        self._dc_ip = dc_ip

    @property
    def dc_name(self):
        r"""Gets the dc_name of this ValidateDcRequestBody.

        域控制器名称。

        :return: The dc_name of this ValidateDcRequestBody.
        :rtype: str
        """
        return self._dc_name

    @dc_name.setter
    def dc_name(self, dc_name):
        r"""Sets the dc_name of this ValidateDcRequestBody.

        域控制器名称。

        :param dc_name: The dc_name of this ValidateDcRequestBody.
        :type dc_name: str
        """
        self._dc_name = dc_name

    @property
    def domain_admin_account(self):
        r"""Gets the domain_admin_account of this ValidateDcRequestBody.

        域管理员账号。

        :return: The domain_admin_account of this ValidateDcRequestBody.
        :rtype: str
        """
        return self._domain_admin_account

    @domain_admin_account.setter
    def domain_admin_account(self, domain_admin_account):
        r"""Sets the domain_admin_account of this ValidateDcRequestBody.

        域管理员账号。

        :param domain_admin_account: The domain_admin_account of this ValidateDcRequestBody.
        :type domain_admin_account: str
        """
        self._domain_admin_account = domain_admin_account

    @property
    def domain_password(self):
        r"""Gets the domain_password of this ValidateDcRequestBody.

        域管理员账号密码。

        :return: The domain_password of this ValidateDcRequestBody.
        :rtype: str
        """
        return self._domain_password

    @domain_password.setter
    def domain_password(self, domain_password):
        r"""Sets the domain_password of this ValidateDcRequestBody.

        域管理员账号密码。

        :param domain_password: The domain_password of this ValidateDcRequestBody.
        :type domain_password: str
        """
        self._domain_password = domain_password

    @property
    def is_ldaps_enable(self):
        r"""Gets the is_ldaps_enable of this ValidateDcRequestBody.

        是否开启LDAPS。

        :return: The is_ldaps_enable of this ValidateDcRequestBody.
        :rtype: bool
        """
        return self._is_ldaps_enable

    @is_ldaps_enable.setter
    def is_ldaps_enable(self, is_ldaps_enable):
        r"""Sets the is_ldaps_enable of this ValidateDcRequestBody.

        是否开启LDAPS。

        :param is_ldaps_enable: The is_ldaps_enable of this ValidateDcRequestBody.
        :type is_ldaps_enable: bool
        """
        self._is_ldaps_enable = is_ldaps_enable

    @property
    def ldaps_certificate(self):
        r"""Gets the ldaps_certificate of this ValidateDcRequestBody.

        LDAPS用的密钥证书。

        :return: The ldaps_certificate of this ValidateDcRequestBody.
        :rtype: str
        """
        return self._ldaps_certificate

    @ldaps_certificate.setter
    def ldaps_certificate(self, ldaps_certificate):
        r"""Sets the ldaps_certificate of this ValidateDcRequestBody.

        LDAPS用的密钥证书。

        :param ldaps_certificate: The ldaps_certificate of this ValidateDcRequestBody.
        :type ldaps_certificate: str
        """
        self._ldaps_certificate = ldaps_certificate

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
        if not isinstance(other, ValidateDcRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
