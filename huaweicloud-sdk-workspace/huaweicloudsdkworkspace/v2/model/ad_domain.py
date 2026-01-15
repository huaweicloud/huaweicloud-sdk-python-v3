# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdDomain:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'domain_type': 'str',
        'domain_name': 'str',
        'domain_admin_account': 'str',
        'domain_password': 'str',
        'active_domain_ip': 'str',
        'active_domain_name': 'str',
        'standby_domain_ip': 'str',
        'standby_domain_name': 'str',
        'active_dns_ip': 'str',
        'standby_dns_ip': 'str',
        'delete_computer_object': 'int',
        'use_ldaps': 'bool',
        'tls_config': 'TlsConfig',
        'cba_enabled': 'bool',
        'certificate_id': 'str',
        'domain_controllers': 'list[DomainController]'
    }

    attribute_map = {
        'id': 'id',
        'domain_type': 'domain_type',
        'domain_name': 'domain_name',
        'domain_admin_account': 'domain_admin_account',
        'domain_password': 'domain_password',
        'active_domain_ip': 'active_domain_ip',
        'active_domain_name': 'active_domain_name',
        'standby_domain_ip': 'standby_domain_ip',
        'standby_domain_name': 'standby_domain_name',
        'active_dns_ip': 'active_dns_ip',
        'standby_dns_ip': 'standby_dns_ip',
        'delete_computer_object': 'delete_computer_object',
        'use_ldaps': 'use_ldaps',
        'tls_config': 'tls_config',
        'cba_enabled': 'cba_enabled',
        'certificate_id': 'certificate_id',
        'domain_controllers': 'domain_controllers'
    }

    def __init__(self, id=None, domain_type=None, domain_name=None, domain_admin_account=None, domain_password=None, active_domain_ip=None, active_domain_name=None, standby_domain_ip=None, standby_domain_name=None, active_dns_ip=None, standby_dns_ip=None, delete_computer_object=None, use_ldaps=None, tls_config=None, cba_enabled=None, certificate_id=None, domain_controllers=None):
        r"""AdDomain

        The model defined in huaweicloud sdk

        :param id: 域id。
        :type id: str
        :param domain_type: 域类型。 - LITE_AS：本地认证。 - LOCAL_AD：本地AD。 说明：域类型为“LOCAL_AD”时，请确保所选VPC网络与AD所属网络可连通。
        :type domain_type: str
        :param domain_name: 域名称。域类型为LOCAL_AD时需要配置。 域名必须为AD服务器上已经存在的域名，且长度不超过55。
        :type domain_name: str
        :param domain_admin_account: 域管理员账号。域类型为LOCAL_AD时需要配置。 必须为AD服务器上已经存在的域管理员账号。
        :type domain_admin_account: str
        :param domain_password: 域管理员账号密码。域类型为LOCAL_AD时需要配置。
        :type domain_password: str
        :param active_domain_ip: 主域控制器IP地址。域类型为LOCAL_AD时需要配置。
        :type active_domain_ip: str
        :param active_domain_name: 主域控制器名称。域类型为LOCAL_AD时需要配置。
        :type active_domain_name: str
        :param standby_domain_ip: 备域控制器IP地址。域类型为LOCAL_AD时且配置备节点时需要配置。
        :type standby_domain_ip: str
        :param standby_domain_name: 备域控制器名称。域类型为LOCAL_AD时且配置备节点时需要配置。
        :type standby_domain_name: str
        :param active_dns_ip: 主DNS IP地址。域类型为LOCAL_AD时需要配置。
        :type active_dns_ip: str
        :param standby_dns_ip: 备DNS IP地址。域类型为LOCAL_AD时且配置备节点时需要配置。
        :type standby_dns_ip: str
        :param delete_computer_object: 是否在删除桌面的同时删除AD上对应的计算机对象，0代表不删除，1代表删除。
        :type delete_computer_object: int
        :param use_ldaps: 是否开启LDAPS。
        :type use_ldaps: bool
        :param tls_config: 
        :type tls_config: :class:`huaweicloudsdkworkspace.v2.TlsConfig`
        :param cba_enabled: 是否开启智能卡认证。
        :type cba_enabled: bool
        :param certificate_id: 智能卡证书id。
        :type certificate_id: str
        :param domain_controllers: 域控制器信息列表。有值时，active_domain_name、active_domain_ip、standby_domain_name、standby_domain_ip无效。
        :type domain_controllers: list[:class:`huaweicloudsdkworkspace.v2.DomainController`]
        """
        
        

        self._id = None
        self._domain_type = None
        self._domain_name = None
        self._domain_admin_account = None
        self._domain_password = None
        self._active_domain_ip = None
        self._active_domain_name = None
        self._standby_domain_ip = None
        self._standby_domain_name = None
        self._active_dns_ip = None
        self._standby_dns_ip = None
        self._delete_computer_object = None
        self._use_ldaps = None
        self._tls_config = None
        self._cba_enabled = None
        self._certificate_id = None
        self._domain_controllers = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.domain_type = domain_type
        if domain_name is not None:
            self.domain_name = domain_name
        if domain_admin_account is not None:
            self.domain_admin_account = domain_admin_account
        if domain_password is not None:
            self.domain_password = domain_password
        if active_domain_ip is not None:
            self.active_domain_ip = active_domain_ip
        if active_domain_name is not None:
            self.active_domain_name = active_domain_name
        if standby_domain_ip is not None:
            self.standby_domain_ip = standby_domain_ip
        if standby_domain_name is not None:
            self.standby_domain_name = standby_domain_name
        if active_dns_ip is not None:
            self.active_dns_ip = active_dns_ip
        if standby_dns_ip is not None:
            self.standby_dns_ip = standby_dns_ip
        if delete_computer_object is not None:
            self.delete_computer_object = delete_computer_object
        if use_ldaps is not None:
            self.use_ldaps = use_ldaps
        if tls_config is not None:
            self.tls_config = tls_config
        if cba_enabled is not None:
            self.cba_enabled = cba_enabled
        if certificate_id is not None:
            self.certificate_id = certificate_id
        if domain_controllers is not None:
            self.domain_controllers = domain_controllers

    @property
    def id(self):
        r"""Gets the id of this AdDomain.

        域id。

        :return: The id of this AdDomain.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AdDomain.

        域id。

        :param id: The id of this AdDomain.
        :type id: str
        """
        self._id = id

    @property
    def domain_type(self):
        r"""Gets the domain_type of this AdDomain.

        域类型。 - LITE_AS：本地认证。 - LOCAL_AD：本地AD。 说明：域类型为“LOCAL_AD”时，请确保所选VPC网络与AD所属网络可连通。

        :return: The domain_type of this AdDomain.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        r"""Sets the domain_type of this AdDomain.

        域类型。 - LITE_AS：本地认证。 - LOCAL_AD：本地AD。 说明：域类型为“LOCAL_AD”时，请确保所选VPC网络与AD所属网络可连通。

        :param domain_type: The domain_type of this AdDomain.
        :type domain_type: str
        """
        self._domain_type = domain_type

    @property
    def domain_name(self):
        r"""Gets the domain_name of this AdDomain.

        域名称。域类型为LOCAL_AD时需要配置。 域名必须为AD服务器上已经存在的域名，且长度不超过55。

        :return: The domain_name of this AdDomain.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this AdDomain.

        域名称。域类型为LOCAL_AD时需要配置。 域名必须为AD服务器上已经存在的域名，且长度不超过55。

        :param domain_name: The domain_name of this AdDomain.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def domain_admin_account(self):
        r"""Gets the domain_admin_account of this AdDomain.

        域管理员账号。域类型为LOCAL_AD时需要配置。 必须为AD服务器上已经存在的域管理员账号。

        :return: The domain_admin_account of this AdDomain.
        :rtype: str
        """
        return self._domain_admin_account

    @domain_admin_account.setter
    def domain_admin_account(self, domain_admin_account):
        r"""Sets the domain_admin_account of this AdDomain.

        域管理员账号。域类型为LOCAL_AD时需要配置。 必须为AD服务器上已经存在的域管理员账号。

        :param domain_admin_account: The domain_admin_account of this AdDomain.
        :type domain_admin_account: str
        """
        self._domain_admin_account = domain_admin_account

    @property
    def domain_password(self):
        r"""Gets the domain_password of this AdDomain.

        域管理员账号密码。域类型为LOCAL_AD时需要配置。

        :return: The domain_password of this AdDomain.
        :rtype: str
        """
        return self._domain_password

    @domain_password.setter
    def domain_password(self, domain_password):
        r"""Sets the domain_password of this AdDomain.

        域管理员账号密码。域类型为LOCAL_AD时需要配置。

        :param domain_password: The domain_password of this AdDomain.
        :type domain_password: str
        """
        self._domain_password = domain_password

    @property
    def active_domain_ip(self):
        r"""Gets the active_domain_ip of this AdDomain.

        主域控制器IP地址。域类型为LOCAL_AD时需要配置。

        :return: The active_domain_ip of this AdDomain.
        :rtype: str
        """
        return self._active_domain_ip

    @active_domain_ip.setter
    def active_domain_ip(self, active_domain_ip):
        r"""Sets the active_domain_ip of this AdDomain.

        主域控制器IP地址。域类型为LOCAL_AD时需要配置。

        :param active_domain_ip: The active_domain_ip of this AdDomain.
        :type active_domain_ip: str
        """
        self._active_domain_ip = active_domain_ip

    @property
    def active_domain_name(self):
        r"""Gets the active_domain_name of this AdDomain.

        主域控制器名称。域类型为LOCAL_AD时需要配置。

        :return: The active_domain_name of this AdDomain.
        :rtype: str
        """
        return self._active_domain_name

    @active_domain_name.setter
    def active_domain_name(self, active_domain_name):
        r"""Sets the active_domain_name of this AdDomain.

        主域控制器名称。域类型为LOCAL_AD时需要配置。

        :param active_domain_name: The active_domain_name of this AdDomain.
        :type active_domain_name: str
        """
        self._active_domain_name = active_domain_name

    @property
    def standby_domain_ip(self):
        r"""Gets the standby_domain_ip of this AdDomain.

        备域控制器IP地址。域类型为LOCAL_AD时且配置备节点时需要配置。

        :return: The standby_domain_ip of this AdDomain.
        :rtype: str
        """
        return self._standby_domain_ip

    @standby_domain_ip.setter
    def standby_domain_ip(self, standby_domain_ip):
        r"""Sets the standby_domain_ip of this AdDomain.

        备域控制器IP地址。域类型为LOCAL_AD时且配置备节点时需要配置。

        :param standby_domain_ip: The standby_domain_ip of this AdDomain.
        :type standby_domain_ip: str
        """
        self._standby_domain_ip = standby_domain_ip

    @property
    def standby_domain_name(self):
        r"""Gets the standby_domain_name of this AdDomain.

        备域控制器名称。域类型为LOCAL_AD时且配置备节点时需要配置。

        :return: The standby_domain_name of this AdDomain.
        :rtype: str
        """
        return self._standby_domain_name

    @standby_domain_name.setter
    def standby_domain_name(self, standby_domain_name):
        r"""Sets the standby_domain_name of this AdDomain.

        备域控制器名称。域类型为LOCAL_AD时且配置备节点时需要配置。

        :param standby_domain_name: The standby_domain_name of this AdDomain.
        :type standby_domain_name: str
        """
        self._standby_domain_name = standby_domain_name

    @property
    def active_dns_ip(self):
        r"""Gets the active_dns_ip of this AdDomain.

        主DNS IP地址。域类型为LOCAL_AD时需要配置。

        :return: The active_dns_ip of this AdDomain.
        :rtype: str
        """
        return self._active_dns_ip

    @active_dns_ip.setter
    def active_dns_ip(self, active_dns_ip):
        r"""Sets the active_dns_ip of this AdDomain.

        主DNS IP地址。域类型为LOCAL_AD时需要配置。

        :param active_dns_ip: The active_dns_ip of this AdDomain.
        :type active_dns_ip: str
        """
        self._active_dns_ip = active_dns_ip

    @property
    def standby_dns_ip(self):
        r"""Gets the standby_dns_ip of this AdDomain.

        备DNS IP地址。域类型为LOCAL_AD时且配置备节点时需要配置。

        :return: The standby_dns_ip of this AdDomain.
        :rtype: str
        """
        return self._standby_dns_ip

    @standby_dns_ip.setter
    def standby_dns_ip(self, standby_dns_ip):
        r"""Sets the standby_dns_ip of this AdDomain.

        备DNS IP地址。域类型为LOCAL_AD时且配置备节点时需要配置。

        :param standby_dns_ip: The standby_dns_ip of this AdDomain.
        :type standby_dns_ip: str
        """
        self._standby_dns_ip = standby_dns_ip

    @property
    def delete_computer_object(self):
        r"""Gets the delete_computer_object of this AdDomain.

        是否在删除桌面的同时删除AD上对应的计算机对象，0代表不删除，1代表删除。

        :return: The delete_computer_object of this AdDomain.
        :rtype: int
        """
        return self._delete_computer_object

    @delete_computer_object.setter
    def delete_computer_object(self, delete_computer_object):
        r"""Sets the delete_computer_object of this AdDomain.

        是否在删除桌面的同时删除AD上对应的计算机对象，0代表不删除，1代表删除。

        :param delete_computer_object: The delete_computer_object of this AdDomain.
        :type delete_computer_object: int
        """
        self._delete_computer_object = delete_computer_object

    @property
    def use_ldaps(self):
        r"""Gets the use_ldaps of this AdDomain.

        是否开启LDAPS。

        :return: The use_ldaps of this AdDomain.
        :rtype: bool
        """
        return self._use_ldaps

    @use_ldaps.setter
    def use_ldaps(self, use_ldaps):
        r"""Sets the use_ldaps of this AdDomain.

        是否开启LDAPS。

        :param use_ldaps: The use_ldaps of this AdDomain.
        :type use_ldaps: bool
        """
        self._use_ldaps = use_ldaps

    @property
    def tls_config(self):
        r"""Gets the tls_config of this AdDomain.

        :return: The tls_config of this AdDomain.
        :rtype: :class:`huaweicloudsdkworkspace.v2.TlsConfig`
        """
        return self._tls_config

    @tls_config.setter
    def tls_config(self, tls_config):
        r"""Sets the tls_config of this AdDomain.

        :param tls_config: The tls_config of this AdDomain.
        :type tls_config: :class:`huaweicloudsdkworkspace.v2.TlsConfig`
        """
        self._tls_config = tls_config

    @property
    def cba_enabled(self):
        r"""Gets the cba_enabled of this AdDomain.

        是否开启智能卡认证。

        :return: The cba_enabled of this AdDomain.
        :rtype: bool
        """
        return self._cba_enabled

    @cba_enabled.setter
    def cba_enabled(self, cba_enabled):
        r"""Sets the cba_enabled of this AdDomain.

        是否开启智能卡认证。

        :param cba_enabled: The cba_enabled of this AdDomain.
        :type cba_enabled: bool
        """
        self._cba_enabled = cba_enabled

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this AdDomain.

        智能卡证书id。

        :return: The certificate_id of this AdDomain.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this AdDomain.

        智能卡证书id。

        :param certificate_id: The certificate_id of this AdDomain.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def domain_controllers(self):
        r"""Gets the domain_controllers of this AdDomain.

        域控制器信息列表。有值时，active_domain_name、active_domain_ip、standby_domain_name、standby_domain_ip无效。

        :return: The domain_controllers of this AdDomain.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.DomainController`]
        """
        return self._domain_controllers

    @domain_controllers.setter
    def domain_controllers(self, domain_controllers):
        r"""Sets the domain_controllers of this AdDomain.

        域控制器信息列表。有值时，active_domain_name、active_domain_ip、standby_domain_name、standby_domain_ip无效。

        :param domain_controllers: The domain_controllers of this AdDomain.
        :type domain_controllers: list[:class:`huaweicloudsdkworkspace.v2.DomainController`]
        """
        self._domain_controllers = domain_controllers

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
        if not isinstance(other, AdDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
