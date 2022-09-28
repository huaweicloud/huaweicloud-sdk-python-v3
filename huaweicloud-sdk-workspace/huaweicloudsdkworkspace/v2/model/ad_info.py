# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdInfo:

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
        'domain_name': 'str',
        'domain_admin_account': 'str',
        'active_domain_name': 'str',
        'active_domain_ip': 'str',
        'standby_domain_name': 'str',
        'standby_domain_ip': 'str',
        'active_dns_ip': 'str',
        'standby_dns_ip': 'str',
        'delete_computer_object': 'str',
        'use_ldaps': 'bool',
        'tls_config': 'TlsConfig'
    }

    attribute_map = {
        'domain_type': 'domain_type',
        'domain_name': 'domain_name',
        'domain_admin_account': 'domain_admin_account',
        'active_domain_name': 'active_domain_name',
        'active_domain_ip': 'active_domain_ip',
        'standby_domain_name': 'standby_domain_name',
        'standby_domain_ip': 'standby_domain_ip',
        'active_dns_ip': 'active_dns_ip',
        'standby_dns_ip': 'standby_dns_ip',
        'delete_computer_object': 'delete_computer_object',
        'use_ldaps': 'use_ldaps',
        'tls_config': 'tls_config'
    }

    def __init__(self, domain_type=None, domain_name=None, domain_admin_account=None, active_domain_name=None, active_domain_ip=None, standby_domain_name=None, standby_domain_ip=None, active_dns_ip=None, standby_dns_ip=None, delete_computer_object=None, use_ldaps=None, tls_config=None):
        """AdInfo

        The model defined in huaweicloud sdk

        :param domain_type: 域类型。 - LITE_AS：本地认证。 - LOCAL_AD：本地AD。
        :type domain_type: str
        :param domain_name: 域名，域类型为LOCAL_AD时有值。
        :type domain_name: str
        :param domain_admin_account: 域管理员帐号，域类型为LOCAL_AD时有值。
        :type domain_admin_account: str
        :param active_domain_name: 主域控制器名称，域类型为LOCAL_AD时有值。
        :type active_domain_name: str
        :param active_domain_ip: 主域控制器IP地址，域类型为LOCAL_AD时有值。
        :type active_domain_ip: str
        :param standby_domain_name: 备域控制器名称，域类型为LOCAL_AD时有值。
        :type standby_domain_name: str
        :param standby_domain_ip: 备域控制器IP地址，域类型为LOCAL_AD时有值。
        :type standby_domain_ip: str
        :param active_dns_ip: 主DNS IP地址，域类型为LOCAL_AD时有值。
        :type active_dns_ip: str
        :param standby_dns_ip: 备DNS IP地址，域类型为LOCAL_AD时有值。
        :type standby_dns_ip: str
        :param delete_computer_object: 是否在删除桌面的同时删除AD上对应的计算机对象，&#39;0&#39;代表不删除，&#39;1&#39;代表删除。
        :type delete_computer_object: str
        :param use_ldaps: 是否开启LDAPS。
        :type use_ldaps: bool
        :param tls_config: 
        :type tls_config: :class:`huaweicloudsdkworkspace.v2.TlsConfig`
        """
        
        

        self._domain_type = None
        self._domain_name = None
        self._domain_admin_account = None
        self._active_domain_name = None
        self._active_domain_ip = None
        self._standby_domain_name = None
        self._standby_domain_ip = None
        self._active_dns_ip = None
        self._standby_dns_ip = None
        self._delete_computer_object = None
        self._use_ldaps = None
        self._tls_config = None
        self.discriminator = None

        if domain_type is not None:
            self.domain_type = domain_type
        if domain_name is not None:
            self.domain_name = domain_name
        if domain_admin_account is not None:
            self.domain_admin_account = domain_admin_account
        if active_domain_name is not None:
            self.active_domain_name = active_domain_name
        if active_domain_ip is not None:
            self.active_domain_ip = active_domain_ip
        if standby_domain_name is not None:
            self.standby_domain_name = standby_domain_name
        if standby_domain_ip is not None:
            self.standby_domain_ip = standby_domain_ip
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

    @property
    def domain_type(self):
        """Gets the domain_type of this AdInfo.

        域类型。 - LITE_AS：本地认证。 - LOCAL_AD：本地AD。

        :return: The domain_type of this AdInfo.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this AdInfo.

        域类型。 - LITE_AS：本地认证。 - LOCAL_AD：本地AD。

        :param domain_type: The domain_type of this AdInfo.
        :type domain_type: str
        """
        self._domain_type = domain_type

    @property
    def domain_name(self):
        """Gets the domain_name of this AdInfo.

        域名，域类型为LOCAL_AD时有值。

        :return: The domain_name of this AdInfo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this AdInfo.

        域名，域类型为LOCAL_AD时有值。

        :param domain_name: The domain_name of this AdInfo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def domain_admin_account(self):
        """Gets the domain_admin_account of this AdInfo.

        域管理员帐号，域类型为LOCAL_AD时有值。

        :return: The domain_admin_account of this AdInfo.
        :rtype: str
        """
        return self._domain_admin_account

    @domain_admin_account.setter
    def domain_admin_account(self, domain_admin_account):
        """Sets the domain_admin_account of this AdInfo.

        域管理员帐号，域类型为LOCAL_AD时有值。

        :param domain_admin_account: The domain_admin_account of this AdInfo.
        :type domain_admin_account: str
        """
        self._domain_admin_account = domain_admin_account

    @property
    def active_domain_name(self):
        """Gets the active_domain_name of this AdInfo.

        主域控制器名称，域类型为LOCAL_AD时有值。

        :return: The active_domain_name of this AdInfo.
        :rtype: str
        """
        return self._active_domain_name

    @active_domain_name.setter
    def active_domain_name(self, active_domain_name):
        """Sets the active_domain_name of this AdInfo.

        主域控制器名称，域类型为LOCAL_AD时有值。

        :param active_domain_name: The active_domain_name of this AdInfo.
        :type active_domain_name: str
        """
        self._active_domain_name = active_domain_name

    @property
    def active_domain_ip(self):
        """Gets the active_domain_ip of this AdInfo.

        主域控制器IP地址，域类型为LOCAL_AD时有值。

        :return: The active_domain_ip of this AdInfo.
        :rtype: str
        """
        return self._active_domain_ip

    @active_domain_ip.setter
    def active_domain_ip(self, active_domain_ip):
        """Sets the active_domain_ip of this AdInfo.

        主域控制器IP地址，域类型为LOCAL_AD时有值。

        :param active_domain_ip: The active_domain_ip of this AdInfo.
        :type active_domain_ip: str
        """
        self._active_domain_ip = active_domain_ip

    @property
    def standby_domain_name(self):
        """Gets the standby_domain_name of this AdInfo.

        备域控制器名称，域类型为LOCAL_AD时有值。

        :return: The standby_domain_name of this AdInfo.
        :rtype: str
        """
        return self._standby_domain_name

    @standby_domain_name.setter
    def standby_domain_name(self, standby_domain_name):
        """Sets the standby_domain_name of this AdInfo.

        备域控制器名称，域类型为LOCAL_AD时有值。

        :param standby_domain_name: The standby_domain_name of this AdInfo.
        :type standby_domain_name: str
        """
        self._standby_domain_name = standby_domain_name

    @property
    def standby_domain_ip(self):
        """Gets the standby_domain_ip of this AdInfo.

        备域控制器IP地址，域类型为LOCAL_AD时有值。

        :return: The standby_domain_ip of this AdInfo.
        :rtype: str
        """
        return self._standby_domain_ip

    @standby_domain_ip.setter
    def standby_domain_ip(self, standby_domain_ip):
        """Sets the standby_domain_ip of this AdInfo.

        备域控制器IP地址，域类型为LOCAL_AD时有值。

        :param standby_domain_ip: The standby_domain_ip of this AdInfo.
        :type standby_domain_ip: str
        """
        self._standby_domain_ip = standby_domain_ip

    @property
    def active_dns_ip(self):
        """Gets the active_dns_ip of this AdInfo.

        主DNS IP地址，域类型为LOCAL_AD时有值。

        :return: The active_dns_ip of this AdInfo.
        :rtype: str
        """
        return self._active_dns_ip

    @active_dns_ip.setter
    def active_dns_ip(self, active_dns_ip):
        """Sets the active_dns_ip of this AdInfo.

        主DNS IP地址，域类型为LOCAL_AD时有值。

        :param active_dns_ip: The active_dns_ip of this AdInfo.
        :type active_dns_ip: str
        """
        self._active_dns_ip = active_dns_ip

    @property
    def standby_dns_ip(self):
        """Gets the standby_dns_ip of this AdInfo.

        备DNS IP地址，域类型为LOCAL_AD时有值。

        :return: The standby_dns_ip of this AdInfo.
        :rtype: str
        """
        return self._standby_dns_ip

    @standby_dns_ip.setter
    def standby_dns_ip(self, standby_dns_ip):
        """Sets the standby_dns_ip of this AdInfo.

        备DNS IP地址，域类型为LOCAL_AD时有值。

        :param standby_dns_ip: The standby_dns_ip of this AdInfo.
        :type standby_dns_ip: str
        """
        self._standby_dns_ip = standby_dns_ip

    @property
    def delete_computer_object(self):
        """Gets the delete_computer_object of this AdInfo.

        是否在删除桌面的同时删除AD上对应的计算机对象，'0'代表不删除，'1'代表删除。

        :return: The delete_computer_object of this AdInfo.
        :rtype: str
        """
        return self._delete_computer_object

    @delete_computer_object.setter
    def delete_computer_object(self, delete_computer_object):
        """Sets the delete_computer_object of this AdInfo.

        是否在删除桌面的同时删除AD上对应的计算机对象，'0'代表不删除，'1'代表删除。

        :param delete_computer_object: The delete_computer_object of this AdInfo.
        :type delete_computer_object: str
        """
        self._delete_computer_object = delete_computer_object

    @property
    def use_ldaps(self):
        """Gets the use_ldaps of this AdInfo.

        是否开启LDAPS。

        :return: The use_ldaps of this AdInfo.
        :rtype: bool
        """
        return self._use_ldaps

    @use_ldaps.setter
    def use_ldaps(self, use_ldaps):
        """Sets the use_ldaps of this AdInfo.

        是否开启LDAPS。

        :param use_ldaps: The use_ldaps of this AdInfo.
        :type use_ldaps: bool
        """
        self._use_ldaps = use_ldaps

    @property
    def tls_config(self):
        """Gets the tls_config of this AdInfo.


        :return: The tls_config of this AdInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.TlsConfig`
        """
        return self._tls_config

    @tls_config.setter
    def tls_config(self, tls_config):
        """Sets the tls_config of this AdInfo.


        :param tls_config: The tls_config of this AdInfo.
        :type tls_config: :class:`huaweicloudsdkworkspace.v2.TlsConfig`
        """
        self._tls_config = tls_config

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
        if not isinstance(other, AdInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
