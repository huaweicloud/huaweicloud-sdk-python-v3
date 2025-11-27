# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RequiredInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'username': 'str',
        'master_1': 'str',
        'master_2': 'str',
        'master_3': 'str',
        'access_external_load_balance': 'bool',
        'cilium_ipv4_pool_cidr': 'str',
        'network_cidr': 'str',
        'dns_server_ip': 'str',
        'ntp_server_ip': 'str',
        'iam_domain_id': 'str'
    }

    attribute_map = {
        'username': 'USERNAME',
        'master_1': 'MASTER-1',
        'master_2': 'MASTER-2',
        'master_3': 'MASTER-3',
        'access_external_load_balance': 'ACCESS_EXTERNAL_LOAD_BALANCE',
        'cilium_ipv4_pool_cidr': 'CILIUM_IPV4POOL_CIDR',
        'network_cidr': 'NETWORK_CIDR',
        'dns_server_ip': 'DNS_SERVER_IP',
        'ntp_server_ip': 'NTP_SERVER_IP',
        'iam_domain_id': 'IAM_DOMAIN_ID'
    }

    def __init__(self, username=None, master_1=None, master_2=None, master_3=None, access_external_load_balance=None, cilium_ipv4_pool_cidr=None, network_cidr=None, dns_server_ip=None, ntp_server_ip=None, iam_domain_id=None):
        r"""RequiredInput

        The model defined in huaweicloud sdk

        :param username: 用户名
        :type username: str
        :param master_1: 控制节点1IP地址
        :type master_1: str
        :param master_2: 控制节点2IP地址
        :type master_2: str
        :param master_3: 控制节点3IP地址
        :type master_3: str
        :param access_external_load_balance: 是否启用外部负载均衡器
        :type access_external_load_balance: bool
        :param cilium_ipv4_pool_cidr: Cilium网络组件的IPv4地址池CIDR
        :type cilium_ipv4_pool_cidr: str
        :param network_cidr: 容器网络的CIDR范围
        :type network_cidr: str
        :param dns_server_ip: DNS服务器IP地址
        :type dns_server_ip: str
        :param ntp_server_ip: NTP服务器IP地址
        :type ntp_server_ip: str
        :param iam_domain_id: IAM域ID
        :type iam_domain_id: str
        """
        
        

        self._username = None
        self._master_1 = None
        self._master_2 = None
        self._master_3 = None
        self._access_external_load_balance = None
        self._cilium_ipv4_pool_cidr = None
        self._network_cidr = None
        self._dns_server_ip = None
        self._ntp_server_ip = None
        self._iam_domain_id = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if master_1 is not None:
            self.master_1 = master_1
        if master_2 is not None:
            self.master_2 = master_2
        if master_3 is not None:
            self.master_3 = master_3
        if access_external_load_balance is not None:
            self.access_external_load_balance = access_external_load_balance
        if cilium_ipv4_pool_cidr is not None:
            self.cilium_ipv4_pool_cidr = cilium_ipv4_pool_cidr
        if network_cidr is not None:
            self.network_cidr = network_cidr
        if dns_server_ip is not None:
            self.dns_server_ip = dns_server_ip
        if ntp_server_ip is not None:
            self.ntp_server_ip = ntp_server_ip
        if iam_domain_id is not None:
            self.iam_domain_id = iam_domain_id

    @property
    def username(self):
        r"""Gets the username of this RequiredInput.

        用户名

        :return: The username of this RequiredInput.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this RequiredInput.

        用户名

        :param username: The username of this RequiredInput.
        :type username: str
        """
        self._username = username

    @property
    def master_1(self):
        r"""Gets the master_1 of this RequiredInput.

        控制节点1IP地址

        :return: The master_1 of this RequiredInput.
        :rtype: str
        """
        return self._master_1

    @master_1.setter
    def master_1(self, master_1):
        r"""Sets the master_1 of this RequiredInput.

        控制节点1IP地址

        :param master_1: The master_1 of this RequiredInput.
        :type master_1: str
        """
        self._master_1 = master_1

    @property
    def master_2(self):
        r"""Gets the master_2 of this RequiredInput.

        控制节点2IP地址

        :return: The master_2 of this RequiredInput.
        :rtype: str
        """
        return self._master_2

    @master_2.setter
    def master_2(self, master_2):
        r"""Sets the master_2 of this RequiredInput.

        控制节点2IP地址

        :param master_2: The master_2 of this RequiredInput.
        :type master_2: str
        """
        self._master_2 = master_2

    @property
    def master_3(self):
        r"""Gets the master_3 of this RequiredInput.

        控制节点3IP地址

        :return: The master_3 of this RequiredInput.
        :rtype: str
        """
        return self._master_3

    @master_3.setter
    def master_3(self, master_3):
        r"""Sets the master_3 of this RequiredInput.

        控制节点3IP地址

        :param master_3: The master_3 of this RequiredInput.
        :type master_3: str
        """
        self._master_3 = master_3

    @property
    def access_external_load_balance(self):
        r"""Gets the access_external_load_balance of this RequiredInput.

        是否启用外部负载均衡器

        :return: The access_external_load_balance of this RequiredInput.
        :rtype: bool
        """
        return self._access_external_load_balance

    @access_external_load_balance.setter
    def access_external_load_balance(self, access_external_load_balance):
        r"""Sets the access_external_load_balance of this RequiredInput.

        是否启用外部负载均衡器

        :param access_external_load_balance: The access_external_load_balance of this RequiredInput.
        :type access_external_load_balance: bool
        """
        self._access_external_load_balance = access_external_load_balance

    @property
    def cilium_ipv4_pool_cidr(self):
        r"""Gets the cilium_ipv4_pool_cidr of this RequiredInput.

        Cilium网络组件的IPv4地址池CIDR

        :return: The cilium_ipv4_pool_cidr of this RequiredInput.
        :rtype: str
        """
        return self._cilium_ipv4_pool_cidr

    @cilium_ipv4_pool_cidr.setter
    def cilium_ipv4_pool_cidr(self, cilium_ipv4_pool_cidr):
        r"""Sets the cilium_ipv4_pool_cidr of this RequiredInput.

        Cilium网络组件的IPv4地址池CIDR

        :param cilium_ipv4_pool_cidr: The cilium_ipv4_pool_cidr of this RequiredInput.
        :type cilium_ipv4_pool_cidr: str
        """
        self._cilium_ipv4_pool_cidr = cilium_ipv4_pool_cidr

    @property
    def network_cidr(self):
        r"""Gets the network_cidr of this RequiredInput.

        容器网络的CIDR范围

        :return: The network_cidr of this RequiredInput.
        :rtype: str
        """
        return self._network_cidr

    @network_cidr.setter
    def network_cidr(self, network_cidr):
        r"""Sets the network_cidr of this RequiredInput.

        容器网络的CIDR范围

        :param network_cidr: The network_cidr of this RequiredInput.
        :type network_cidr: str
        """
        self._network_cidr = network_cidr

    @property
    def dns_server_ip(self):
        r"""Gets the dns_server_ip of this RequiredInput.

        DNS服务器IP地址

        :return: The dns_server_ip of this RequiredInput.
        :rtype: str
        """
        return self._dns_server_ip

    @dns_server_ip.setter
    def dns_server_ip(self, dns_server_ip):
        r"""Sets the dns_server_ip of this RequiredInput.

        DNS服务器IP地址

        :param dns_server_ip: The dns_server_ip of this RequiredInput.
        :type dns_server_ip: str
        """
        self._dns_server_ip = dns_server_ip

    @property
    def ntp_server_ip(self):
        r"""Gets the ntp_server_ip of this RequiredInput.

        NTP服务器IP地址

        :return: The ntp_server_ip of this RequiredInput.
        :rtype: str
        """
        return self._ntp_server_ip

    @ntp_server_ip.setter
    def ntp_server_ip(self, ntp_server_ip):
        r"""Sets the ntp_server_ip of this RequiredInput.

        NTP服务器IP地址

        :param ntp_server_ip: The ntp_server_ip of this RequiredInput.
        :type ntp_server_ip: str
        """
        self._ntp_server_ip = ntp_server_ip

    @property
    def iam_domain_id(self):
        r"""Gets the iam_domain_id of this RequiredInput.

        IAM域ID

        :return: The iam_domain_id of this RequiredInput.
        :rtype: str
        """
        return self._iam_domain_id

    @iam_domain_id.setter
    def iam_domain_id(self, iam_domain_id):
        r"""Sets the iam_domain_id of this RequiredInput.

        IAM域ID

        :param iam_domain_id: The iam_domain_id of this RequiredInput.
        :type iam_domain_id: str
        """
        self._iam_domain_id = iam_domain_id

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
        if not isinstance(other, RequiredInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
