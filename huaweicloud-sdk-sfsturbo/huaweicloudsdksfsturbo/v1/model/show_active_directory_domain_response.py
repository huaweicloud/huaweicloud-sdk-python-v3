# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowActiveDirectoryDomainResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'system_name': 'str',
        'dns_server': 'list[str]',
        'organization_unit': 'str',
        'vpc_id': 'str',
        'status': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'system_name': 'system_name',
        'dns_server': 'dns_server',
        'organization_unit': 'organization_unit',
        'vpc_id': 'vpc_id',
        'status': 'status',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, domain_name=None, system_name=None, dns_server=None, organization_unit=None, vpc_id=None, status=None, x_request_id=None):
        r"""ShowActiveDirectoryDomainResponse

        The model defined in huaweicloud sdk

        :param domain_name: 域控服务器的域名，在创建域服务器时指定
        :type domain_name: str
        :param system_name: 存储系统在AD域中的名称
        :type system_name: str
        :param dns_server: DNS服务器IP地址，用于解析AD域的域名
        :type dns_server: list[str]
        :param organization_unit: 域中包含的一类目录对象如用户、计算机、打印机等资源的总称，加入后将作为其中的一员。若不填，则默认加入到computers组织单元。
        :type organization_unit: str
        :param vpc_id: vpc的id
        :type vpc_id: str
        :param status: AD域当前状态信息
        :type status: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowActiveDirectoryDomainResponse, self).__init__()

        self._domain_name = None
        self._system_name = None
        self._dns_server = None
        self._organization_unit = None
        self._vpc_id = None
        self._status = None
        self._x_request_id = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if system_name is not None:
            self.system_name = system_name
        if dns_server is not None:
            self.dns_server = dns_server
        if organization_unit is not None:
            self.organization_unit = organization_unit
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if status is not None:
            self.status = status
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowActiveDirectoryDomainResponse.

        域控服务器的域名，在创建域服务器时指定

        :return: The domain_name of this ShowActiveDirectoryDomainResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowActiveDirectoryDomainResponse.

        域控服务器的域名，在创建域服务器时指定

        :param domain_name: The domain_name of this ShowActiveDirectoryDomainResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def system_name(self):
        r"""Gets the system_name of this ShowActiveDirectoryDomainResponse.

        存储系统在AD域中的名称

        :return: The system_name of this ShowActiveDirectoryDomainResponse.
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        r"""Sets the system_name of this ShowActiveDirectoryDomainResponse.

        存储系统在AD域中的名称

        :param system_name: The system_name of this ShowActiveDirectoryDomainResponse.
        :type system_name: str
        """
        self._system_name = system_name

    @property
    def dns_server(self):
        r"""Gets the dns_server of this ShowActiveDirectoryDomainResponse.

        DNS服务器IP地址，用于解析AD域的域名

        :return: The dns_server of this ShowActiveDirectoryDomainResponse.
        :rtype: list[str]
        """
        return self._dns_server

    @dns_server.setter
    def dns_server(self, dns_server):
        r"""Sets the dns_server of this ShowActiveDirectoryDomainResponse.

        DNS服务器IP地址，用于解析AD域的域名

        :param dns_server: The dns_server of this ShowActiveDirectoryDomainResponse.
        :type dns_server: list[str]
        """
        self._dns_server = dns_server

    @property
    def organization_unit(self):
        r"""Gets the organization_unit of this ShowActiveDirectoryDomainResponse.

        域中包含的一类目录对象如用户、计算机、打印机等资源的总称，加入后将作为其中的一员。若不填，则默认加入到computers组织单元。

        :return: The organization_unit of this ShowActiveDirectoryDomainResponse.
        :rtype: str
        """
        return self._organization_unit

    @organization_unit.setter
    def organization_unit(self, organization_unit):
        r"""Sets the organization_unit of this ShowActiveDirectoryDomainResponse.

        域中包含的一类目录对象如用户、计算机、打印机等资源的总称，加入后将作为其中的一员。若不填，则默认加入到computers组织单元。

        :param organization_unit: The organization_unit of this ShowActiveDirectoryDomainResponse.
        :type organization_unit: str
        """
        self._organization_unit = organization_unit

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ShowActiveDirectoryDomainResponse.

        vpc的id

        :return: The vpc_id of this ShowActiveDirectoryDomainResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ShowActiveDirectoryDomainResponse.

        vpc的id

        :param vpc_id: The vpc_id of this ShowActiveDirectoryDomainResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def status(self):
        r"""Gets the status of this ShowActiveDirectoryDomainResponse.

        AD域当前状态信息

        :return: The status of this ShowActiveDirectoryDomainResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowActiveDirectoryDomainResponse.

        AD域当前状态信息

        :param status: The status of this ShowActiveDirectoryDomainResponse.
        :type status: str
        """
        self._status = status

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowActiveDirectoryDomainResponse.

        :return: The x_request_id of this ShowActiveDirectoryDomainResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowActiveDirectoryDomainResponse.

        :param x_request_id: The x_request_id of this ShowActiveDirectoryDomainResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowActiveDirectoryDomainResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
