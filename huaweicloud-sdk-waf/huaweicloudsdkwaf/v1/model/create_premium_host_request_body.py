# coding: utf-8

import re
import six





class CreatePremiumHostRequestBody:


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
        'proxy': 'bool',
        'policyid': 'str',
        'certificateid': 'str',
        'certificatename': 'str',
        'server': 'list[PremiumWafServer]',
        'mode': 'str',
        'pool_ids': 'list[str]'
    }

    attribute_map = {
        'hostname': 'hostname',
        'proxy': 'proxy',
        'policyid': 'policyid',
        'certificateid': 'certificateid',
        'certificatename': 'certificatename',
        'server': 'server',
        'mode': 'mode',
        'pool_ids': 'pool_ids'
    }

    def __init__(self, hostname=None, proxy=None, policyid=None, certificateid=None, certificatename=None, server=None, mode=None, pool_ids=None):
        """CreatePremiumHostRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._hostname = None
        self._proxy = None
        self._policyid = None
        self._certificateid = None
        self._certificatename = None
        self._server = None
        self._mode = None
        self._pool_ids = None
        self.discriminator = None

        self.hostname = hostname
        if proxy is not None:
            self.proxy = proxy
        if policyid is not None:
            self.policyid = policyid
        if certificateid is not None:
            self.certificateid = certificateid
        if certificatename is not None:
            self.certificatename = certificatename
        if server is not None:
            self.server = server
        if mode is not None:
            self.mode = mode
        if pool_ids is not None:
            self.pool_ids = pool_ids

    @property
    def hostname(self):
        """Gets the hostname of this CreatePremiumHostRequestBody.

        防护域名或IP（可带端口）

        :return: The hostname of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this CreatePremiumHostRequestBody.

        防护域名或IP（可带端口）

        :param hostname: The hostname of this CreatePremiumHostRequestBody.
        :type: str
        """
        self._hostname = hostname

    @property
    def proxy(self):
        """Gets the proxy of this CreatePremiumHostRequestBody.

        是否使用代理

        :return: The proxy of this CreatePremiumHostRequestBody.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this CreatePremiumHostRequestBody.

        是否使用代理

        :param proxy: The proxy of this CreatePremiumHostRequestBody.
        :type: bool
        """
        self._proxy = proxy

    @property
    def policyid(self):
        """Gets the policyid of this CreatePremiumHostRequestBody.

        防护域名初始绑定的策略ID

        :return: The policyid of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this CreatePremiumHostRequestBody.

        防护域名初始绑定的策略ID

        :param policyid: The policyid of this CreatePremiumHostRequestBody.
        :type: str
        """
        self._policyid = policyid

    @property
    def certificateid(self):
        """Gets the certificateid of this CreatePremiumHostRequestBody.

        证书ID

        :return: The certificateid of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._certificateid

    @certificateid.setter
    def certificateid(self, certificateid):
        """Sets the certificateid of this CreatePremiumHostRequestBody.

        证书ID

        :param certificateid: The certificateid of this CreatePremiumHostRequestBody.
        :type: str
        """
        self._certificateid = certificateid

    @property
    def certificatename(self):
        """Gets the certificatename of this CreatePremiumHostRequestBody.

        证书名称

        :return: The certificatename of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._certificatename

    @certificatename.setter
    def certificatename(self, certificatename):
        """Sets the certificatename of this CreatePremiumHostRequestBody.

        证书名称

        :param certificatename: The certificatename of this CreatePremiumHostRequestBody.
        :type: str
        """
        self._certificatename = certificatename

    @property
    def server(self):
        """Gets the server of this CreatePremiumHostRequestBody.

        独享模式回源服务器配置

        :return: The server of this CreatePremiumHostRequestBody.
        :rtype: list[PremiumWafServer]
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this CreatePremiumHostRequestBody.

        独享模式回源服务器配置

        :param server: The server of this CreatePremiumHostRequestBody.
        :type: list[PremiumWafServer]
        """
        self._server = server

    @property
    def mode(self):
        """Gets the mode of this CreatePremiumHostRequestBody.

        独享模式特殊域名模式（仅特殊模式需要，如elb）

        :return: The mode of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this CreatePremiumHostRequestBody.

        独享模式特殊域名模式（仅特殊模式需要，如elb）

        :param mode: The mode of this CreatePremiumHostRequestBody.
        :type: str
        """
        self._mode = mode

    @property
    def pool_ids(self):
        """Gets the pool_ids of this CreatePremiumHostRequestBody.

        域名关联的组ID（仅特殊模式需要，如elb）

        :return: The pool_ids of this CreatePremiumHostRequestBody.
        :rtype: list[str]
        """
        return self._pool_ids

    @pool_ids.setter
    def pool_ids(self, pool_ids):
        """Sets the pool_ids of this CreatePremiumHostRequestBody.

        域名关联的组ID（仅特殊模式需要，如elb）

        :param pool_ids: The pool_ids of this CreatePremiumHostRequestBody.
        :type: list[str]
        """
        self._pool_ids = pool_ids

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
        if not isinstance(other, CreatePremiumHostRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
