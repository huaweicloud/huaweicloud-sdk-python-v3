# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdDomainInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_type': 'str',
        'domain_admin_account': 'str',
        'domain_password': 'str',
        'cba_enabled': 'bool',
        'certificate_id': 'str'
    }

    attribute_map = {
        'domain_type': 'domain_type',
        'domain_admin_account': 'domain_admin_account',
        'domain_password': 'domain_password',
        'cba_enabled': 'cba_enabled',
        'certificate_id': 'certificate_id'
    }

    def __init__(self, domain_type=None, domain_admin_account=None, domain_password=None, cba_enabled=None, certificate_id=None):
        r"""AdDomainInfo

        The model defined in huaweicloud sdk

        :param domain_type: 域类型。 - LITE_AS：LiteAS。 - LOCAL_AD：本地AD。 说明：域类型为“LOCAL_AD”时，请确保所选VPC网络与“LOCAL_AD”所属网络可连通。
        :type domain_type: str
        :param domain_admin_account: 域管理员账号。
        :type domain_admin_account: str
        :param domain_password: 域管理员账号密码。
        :type domain_password: str
        :param cba_enabled: 是否开启智能卡认证。
        :type cba_enabled: bool
        :param certificate_id: 智能卡证书id。
        :type certificate_id: str
        """
        
        

        self._domain_type = None
        self._domain_admin_account = None
        self._domain_password = None
        self._cba_enabled = None
        self._certificate_id = None
        self.discriminator = None

        self.domain_type = domain_type
        self.domain_admin_account = domain_admin_account
        self.domain_password = domain_password
        self.cba_enabled = cba_enabled
        if certificate_id is not None:
            self.certificate_id = certificate_id

    @property
    def domain_type(self):
        r"""Gets the domain_type of this AdDomainInfo.

        域类型。 - LITE_AS：LiteAS。 - LOCAL_AD：本地AD。 说明：域类型为“LOCAL_AD”时，请确保所选VPC网络与“LOCAL_AD”所属网络可连通。

        :return: The domain_type of this AdDomainInfo.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        r"""Sets the domain_type of this AdDomainInfo.

        域类型。 - LITE_AS：LiteAS。 - LOCAL_AD：本地AD。 说明：域类型为“LOCAL_AD”时，请确保所选VPC网络与“LOCAL_AD”所属网络可连通。

        :param domain_type: The domain_type of this AdDomainInfo.
        :type domain_type: str
        """
        self._domain_type = domain_type

    @property
    def domain_admin_account(self):
        r"""Gets the domain_admin_account of this AdDomainInfo.

        域管理员账号。

        :return: The domain_admin_account of this AdDomainInfo.
        :rtype: str
        """
        return self._domain_admin_account

    @domain_admin_account.setter
    def domain_admin_account(self, domain_admin_account):
        r"""Sets the domain_admin_account of this AdDomainInfo.

        域管理员账号。

        :param domain_admin_account: The domain_admin_account of this AdDomainInfo.
        :type domain_admin_account: str
        """
        self._domain_admin_account = domain_admin_account

    @property
    def domain_password(self):
        r"""Gets the domain_password of this AdDomainInfo.

        域管理员账号密码。

        :return: The domain_password of this AdDomainInfo.
        :rtype: str
        """
        return self._domain_password

    @domain_password.setter
    def domain_password(self, domain_password):
        r"""Sets the domain_password of this AdDomainInfo.

        域管理员账号密码。

        :param domain_password: The domain_password of this AdDomainInfo.
        :type domain_password: str
        """
        self._domain_password = domain_password

    @property
    def cba_enabled(self):
        r"""Gets the cba_enabled of this AdDomainInfo.

        是否开启智能卡认证。

        :return: The cba_enabled of this AdDomainInfo.
        :rtype: bool
        """
        return self._cba_enabled

    @cba_enabled.setter
    def cba_enabled(self, cba_enabled):
        r"""Sets the cba_enabled of this AdDomainInfo.

        是否开启智能卡认证。

        :param cba_enabled: The cba_enabled of this AdDomainInfo.
        :type cba_enabled: bool
        """
        self._cba_enabled = cba_enabled

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this AdDomainInfo.

        智能卡证书id。

        :return: The certificate_id of this AdDomainInfo.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this AdDomainInfo.

        智能卡证书id。

        :param certificate_id: The certificate_id of this AdDomainInfo.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

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
        if not isinstance(other, AdDomainInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
