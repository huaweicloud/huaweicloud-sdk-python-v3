# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHostRequestBody:


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
        'server': 'list[CloudWafServer]',
        'certificateid': 'str',
        'certificatename': 'str',
        'proxy': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'hostname': 'hostname',
        'policyid': 'policyid',
        'server': 'server',
        'certificateid': 'certificateid',
        'certificatename': 'certificatename',
        'proxy': 'proxy',
        'description': 'description'
    }

    def __init__(self, hostname=None, policyid=None, server=None, certificateid=None, certificatename=None, proxy=None, description=None):
        """CreateHostRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._hostname = None
        self._policyid = None
        self._server = None
        self._certificateid = None
        self._certificatename = None
        self._proxy = None
        self._description = None
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
        if description is not None:
            self.description = description

    @property
    def hostname(self):
        """Gets the hostname of this CreateHostRequestBody.

        域名

        :return: The hostname of this CreateHostRequestBody.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this CreateHostRequestBody.

        域名

        :param hostname: The hostname of this CreateHostRequestBody.
        :type: str
        """
        self._hostname = hostname

    @property
    def policyid(self):
        """Gets the policyid of this CreateHostRequestBody.

        防护域名初始绑定的策略ID

        :return: The policyid of this CreateHostRequestBody.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this CreateHostRequestBody.

        防护域名初始绑定的策略ID

        :param policyid: The policyid of this CreateHostRequestBody.
        :type: str
        """
        self._policyid = policyid

    @property
    def server(self):
        """Gets the server of this CreateHostRequestBody.

        源站信息

        :return: The server of this CreateHostRequestBody.
        :rtype: list[CloudWafServer]
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this CreateHostRequestBody.

        源站信息

        :param server: The server of this CreateHostRequestBody.
        :type: list[CloudWafServer]
        """
        self._server = server

    @property
    def certificateid(self):
        """Gets the certificateid of this CreateHostRequestBody.

        证书id

        :return: The certificateid of this CreateHostRequestBody.
        :rtype: str
        """
        return self._certificateid

    @certificateid.setter
    def certificateid(self, certificateid):
        """Sets the certificateid of this CreateHostRequestBody.

        证书id

        :param certificateid: The certificateid of this CreateHostRequestBody.
        :type: str
        """
        self._certificateid = certificateid

    @property
    def certificatename(self):
        """Gets the certificatename of this CreateHostRequestBody.

        证书名

        :return: The certificatename of this CreateHostRequestBody.
        :rtype: str
        """
        return self._certificatename

    @certificatename.setter
    def certificatename(self, certificatename):
        """Sets the certificatename of this CreateHostRequestBody.

        证书名

        :param certificatename: The certificatename of this CreateHostRequestBody.
        :type: str
        """
        self._certificatename = certificatename

    @property
    def proxy(self):
        """Gets the proxy of this CreateHostRequestBody.

        是否使用代理

        :return: The proxy of this CreateHostRequestBody.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this CreateHostRequestBody.

        是否使用代理

        :param proxy: The proxy of this CreateHostRequestBody.
        :type: bool
        """
        self._proxy = proxy

    @property
    def description(self):
        """Gets the description of this CreateHostRequestBody.

        域名描述

        :return: The description of this CreateHostRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateHostRequestBody.

        域名描述

        :param description: The description of this CreateHostRequestBody.
        :type: str
        """
        self._description = description

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
        if not isinstance(other, CreateHostRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
