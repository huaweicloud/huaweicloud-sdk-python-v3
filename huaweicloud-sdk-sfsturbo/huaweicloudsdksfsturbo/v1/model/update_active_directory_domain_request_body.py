# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateActiveDirectoryDomainRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_account': 'str',
        'password': 'str',
        'domain_name': 'str',
        'system_name': 'str',
        'overwrite_same_account': 'bool',
        'dns_server': 'list[str]',
        'organization_unit': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'service_account': 'service_account',
        'password': 'password',
        'domain_name': 'domain_name',
        'system_name': 'system_name',
        'overwrite_same_account': 'overwrite_same_account',
        'dns_server': 'dns_server',
        'organization_unit': 'organization_unit',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, service_account=None, password=None, domain_name=None, system_name=None, overwrite_same_account=None, dns_server=None, organization_unit=None, vpc_id=None):
        r"""UpdateActiveDirectoryDomainRequestBody

        The model defined in huaweicloud sdk

        :param service_account: 服务账号，在创建域服务器时指定，一般默认为administrator
        :type service_account: str
        :param password: 账号对应密码
        :type password: str
        :param domain_name: 域控服务器的域名，在创建域服务器时指定
        :type domain_name: str
        :param system_name: 存储系统在AD域中的名称
        :type system_name: str
        :param overwrite_same_account: 如果域控制器中已存在同系统名称的存储系统，开启该选项后，将覆盖原有的存储系统信息。
        :type overwrite_same_account: bool
        :param dns_server: DNS服务器IP地址，用于解析AD域的域名
        :type dns_server: list[str]
        :param organization_unit: 域中包含的一类目录对象如用户、计算机、打印机等资源的总称，加入后将作为其中的一员。若不填，则默认加入到computers组织单元。
        :type organization_unit: str
        :param vpc_id: vpc的id
        :type vpc_id: str
        """
        
        

        self._service_account = None
        self._password = None
        self._domain_name = None
        self._system_name = None
        self._overwrite_same_account = None
        self._dns_server = None
        self._organization_unit = None
        self._vpc_id = None
        self.discriminator = None

        self.service_account = service_account
        self.password = password
        self.domain_name = domain_name
        self.system_name = system_name
        if overwrite_same_account is not None:
            self.overwrite_same_account = overwrite_same_account
        self.dns_server = dns_server
        if organization_unit is not None:
            self.organization_unit = organization_unit
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def service_account(self):
        r"""Gets the service_account of this UpdateActiveDirectoryDomainRequestBody.

        服务账号，在创建域服务器时指定，一般默认为administrator

        :return: The service_account of this UpdateActiveDirectoryDomainRequestBody.
        :rtype: str
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        r"""Sets the service_account of this UpdateActiveDirectoryDomainRequestBody.

        服务账号，在创建域服务器时指定，一般默认为administrator

        :param service_account: The service_account of this UpdateActiveDirectoryDomainRequestBody.
        :type service_account: str
        """
        self._service_account = service_account

    @property
    def password(self):
        r"""Gets the password of this UpdateActiveDirectoryDomainRequestBody.

        账号对应密码

        :return: The password of this UpdateActiveDirectoryDomainRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this UpdateActiveDirectoryDomainRequestBody.

        账号对应密码

        :param password: The password of this UpdateActiveDirectoryDomainRequestBody.
        :type password: str
        """
        self._password = password

    @property
    def domain_name(self):
        r"""Gets the domain_name of this UpdateActiveDirectoryDomainRequestBody.

        域控服务器的域名，在创建域服务器时指定

        :return: The domain_name of this UpdateActiveDirectoryDomainRequestBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this UpdateActiveDirectoryDomainRequestBody.

        域控服务器的域名，在创建域服务器时指定

        :param domain_name: The domain_name of this UpdateActiveDirectoryDomainRequestBody.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def system_name(self):
        r"""Gets the system_name of this UpdateActiveDirectoryDomainRequestBody.

        存储系统在AD域中的名称

        :return: The system_name of this UpdateActiveDirectoryDomainRequestBody.
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        r"""Sets the system_name of this UpdateActiveDirectoryDomainRequestBody.

        存储系统在AD域中的名称

        :param system_name: The system_name of this UpdateActiveDirectoryDomainRequestBody.
        :type system_name: str
        """
        self._system_name = system_name

    @property
    def overwrite_same_account(self):
        r"""Gets the overwrite_same_account of this UpdateActiveDirectoryDomainRequestBody.

        如果域控制器中已存在同系统名称的存储系统，开启该选项后，将覆盖原有的存储系统信息。

        :return: The overwrite_same_account of this UpdateActiveDirectoryDomainRequestBody.
        :rtype: bool
        """
        return self._overwrite_same_account

    @overwrite_same_account.setter
    def overwrite_same_account(self, overwrite_same_account):
        r"""Sets the overwrite_same_account of this UpdateActiveDirectoryDomainRequestBody.

        如果域控制器中已存在同系统名称的存储系统，开启该选项后，将覆盖原有的存储系统信息。

        :param overwrite_same_account: The overwrite_same_account of this UpdateActiveDirectoryDomainRequestBody.
        :type overwrite_same_account: bool
        """
        self._overwrite_same_account = overwrite_same_account

    @property
    def dns_server(self):
        r"""Gets the dns_server of this UpdateActiveDirectoryDomainRequestBody.

        DNS服务器IP地址，用于解析AD域的域名

        :return: The dns_server of this UpdateActiveDirectoryDomainRequestBody.
        :rtype: list[str]
        """
        return self._dns_server

    @dns_server.setter
    def dns_server(self, dns_server):
        r"""Sets the dns_server of this UpdateActiveDirectoryDomainRequestBody.

        DNS服务器IP地址，用于解析AD域的域名

        :param dns_server: The dns_server of this UpdateActiveDirectoryDomainRequestBody.
        :type dns_server: list[str]
        """
        self._dns_server = dns_server

    @property
    def organization_unit(self):
        r"""Gets the organization_unit of this UpdateActiveDirectoryDomainRequestBody.

        域中包含的一类目录对象如用户、计算机、打印机等资源的总称，加入后将作为其中的一员。若不填，则默认加入到computers组织单元。

        :return: The organization_unit of this UpdateActiveDirectoryDomainRequestBody.
        :rtype: str
        """
        return self._organization_unit

    @organization_unit.setter
    def organization_unit(self, organization_unit):
        r"""Sets the organization_unit of this UpdateActiveDirectoryDomainRequestBody.

        域中包含的一类目录对象如用户、计算机、打印机等资源的总称，加入后将作为其中的一员。若不填，则默认加入到computers组织单元。

        :param organization_unit: The organization_unit of this UpdateActiveDirectoryDomainRequestBody.
        :type organization_unit: str
        """
        self._organization_unit = organization_unit

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this UpdateActiveDirectoryDomainRequestBody.

        vpc的id

        :return: The vpc_id of this UpdateActiveDirectoryDomainRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this UpdateActiveDirectoryDomainRequestBody.

        vpc的id

        :param vpc_id: The vpc_id of this UpdateActiveDirectoryDomainRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, UpdateActiveDirectoryDomainRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
