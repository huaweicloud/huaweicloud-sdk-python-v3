# coding: utf-8

import re
import six





class InstanceBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'hostname': 'str',
        'policyid': 'str',
        'server': 'list[PremiumWafServer]',
        'certificateid': 'str',
        'certificatename': 'str',
        'proxy': 'bool',
        'paid_type': 'object',
        'description': 'object',
        'exclusive_ip': 'object'
    }

    attribute_map = {
        'hostname': 'hostname',
        'policyid': 'policyid',
        'server': 'server',
        'certificateid': 'certificateid',
        'certificatename': 'certificatename',
        'proxy': 'proxy',
        'paid_type': 'paid_type',
        'description': 'description',
        'exclusive_ip': 'exclusive_ip'
    }

    def __init__(self, hostname=None, policyid=None, server=None, certificateid=None, certificatename=None, proxy=None, paid_type=None, description=None, exclusive_ip=None):
        """InstanceBody - a model defined in huaweicloud sdk"""
        
        

        self._hostname = None
        self._policyid = None
        self._server = None
        self._certificateid = None
        self._certificatename = None
        self._proxy = None
        self._paid_type = None
        self._description = None
        self._exclusive_ip = None
        self.discriminator = None

        if hostname is not None:
            self.hostname = hostname
        if policyid is not None:
            self.policyid = policyid
        if server is not None:
            self.server = server
        if certificateid is not None:
            self.certificateid = certificateid
        if certificatename is not None:
            self.certificatename = certificatename
        if proxy is not None:
            self.proxy = proxy
        if paid_type is not None:
            self.paid_type = paid_type
        if description is not None:
            self.description = description
        if exclusive_ip is not None:
            self.exclusive_ip = exclusive_ip

    @property
    def hostname(self):
        """Gets the hostname of this InstanceBody.

        域名信息

        :return: The hostname of this InstanceBody.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this InstanceBody.

        域名信息

        :param hostname: The hostname of this InstanceBody.
        :type: str
        """
        self._hostname = hostname

    @property
    def policyid(self):
        """Gets the policyid of this InstanceBody.

        防护域名初始绑定的策略ID

        :return: The policyid of this InstanceBody.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this InstanceBody.

        防护域名初始绑定的策略ID

        :param policyid: The policyid of this InstanceBody.
        :type: str
        """
        self._policyid = policyid

    @property
    def server(self):
        """Gets the server of this InstanceBody.

        源站信息

        :return: The server of this InstanceBody.
        :rtype: list[PremiumWafServer]
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this InstanceBody.

        源站信息

        :param server: The server of this InstanceBody.
        :type: list[PremiumWafServer]
        """
        self._server = server

    @property
    def certificateid(self):
        """Gets the certificateid of this InstanceBody.

        证书id

        :return: The certificateid of this InstanceBody.
        :rtype: str
        """
        return self._certificateid

    @certificateid.setter
    def certificateid(self, certificateid):
        """Sets the certificateid of this InstanceBody.

        证书id

        :param certificateid: The certificateid of this InstanceBody.
        :type: str
        """
        self._certificateid = certificateid

    @property
    def certificatename(self):
        """Gets the certificatename of this InstanceBody.

        证书名

        :return: The certificatename of this InstanceBody.
        :rtype: str
        """
        return self._certificatename

    @certificatename.setter
    def certificatename(self, certificatename):
        """Sets the certificatename of this InstanceBody.

        证书名

        :param certificatename: The certificatename of this InstanceBody.
        :type: str
        """
        self._certificatename = certificatename

    @property
    def proxy(self):
        """Gets the proxy of this InstanceBody.

        是否使用代理

        :return: The proxy of this InstanceBody.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this InstanceBody.

        是否使用代理

        :param proxy: The proxy of this InstanceBody.
        :type: bool
        """
        self._proxy = proxy

    @property
    def paid_type(self):
        """Gets the paid_type of this InstanceBody.

        模式

        :return: The paid_type of this InstanceBody.
        :rtype: object
        """
        return self._paid_type

    @paid_type.setter
    def paid_type(self, paid_type):
        """Sets the paid_type of this InstanceBody.

        模式

        :param paid_type: The paid_type of this InstanceBody.
        :type: object
        """
        self._paid_type = paid_type

    @property
    def description(self):
        """Gets the description of this InstanceBody.

        域名描述

        :return: The description of this InstanceBody.
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstanceBody.

        域名描述

        :param description: The description of this InstanceBody.
        :type: object
        """
        self._description = description

    @property
    def exclusive_ip(self):
        """Gets the exclusive_ip of this InstanceBody.

        使用独享IP

        :return: The exclusive_ip of this InstanceBody.
        :rtype: object
        """
        return self._exclusive_ip

    @exclusive_ip.setter
    def exclusive_ip(self, exclusive_ip):
        """Sets the exclusive_ip of this InstanceBody.

        使用独享IP

        :param exclusive_ip: The exclusive_ip of this InstanceBody.
        :type: object
        """
        self._exclusive_ip = exclusive_ip

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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InstanceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
