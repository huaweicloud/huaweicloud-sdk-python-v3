# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHostResponse(SdkResponse):


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
        'hostname': 'str',
        'policyid': 'str',
        'access_code': 'str',
        'protect_status': 'int',
        'access_status': 'int',
        'protocol': 'str',
        'certificateid': 'str',
        'certificatename': 'str',
        'server': 'list[CloudWafServer]',
        'proxy': 'bool',
        'timestamp': 'int',
        'exclusive_ip': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'hostname': 'hostname',
        'policyid': 'policyid',
        'access_code': 'access_code',
        'protect_status': 'protect_status',
        'access_status': 'access_status',
        'protocol': 'protocol',
        'certificateid': 'certificateid',
        'certificatename': 'certificatename',
        'server': 'server',
        'proxy': 'proxy',
        'timestamp': 'timestamp',
        'exclusive_ip': 'exclusive_ip'
    }

    def __init__(self, id=None, hostname=None, policyid=None, access_code=None, protect_status=None, access_status=None, protocol=None, certificateid=None, certificatename=None, server=None, proxy=None, timestamp=None, exclusive_ip=None):
        """CreateHostResponse - a model defined in huaweicloud sdk"""
        
        super(CreateHostResponse, self).__init__()

        self._id = None
        self._hostname = None
        self._policyid = None
        self._access_code = None
        self._protect_status = None
        self._access_status = None
        self._protocol = None
        self._certificateid = None
        self._certificatename = None
        self._server = None
        self._proxy = None
        self._timestamp = None
        self._exclusive_ip = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if hostname is not None:
            self.hostname = hostname
        if policyid is not None:
            self.policyid = policyid
        if access_code is not None:
            self.access_code = access_code
        if protect_status is not None:
            self.protect_status = protect_status
        if access_status is not None:
            self.access_status = access_status
        if protocol is not None:
            self.protocol = protocol
        if certificateid is not None:
            self.certificateid = certificateid
        if certificatename is not None:
            self.certificatename = certificatename
        if server is not None:
            self.server = server
        if proxy is not None:
            self.proxy = proxy
        if timestamp is not None:
            self.timestamp = timestamp
        if exclusive_ip is not None:
            self.exclusive_ip = exclusive_ip

    @property
    def id(self):
        """Gets the id of this CreateHostResponse.

        域名id

        :return: The id of this CreateHostResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateHostResponse.

        域名id

        :param id: The id of this CreateHostResponse.
        :type: str
        """
        self._id = id

    @property
    def hostname(self):
        """Gets the hostname of this CreateHostResponse.

        创建的云模式防护域名

        :return: The hostname of this CreateHostResponse.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this CreateHostResponse.

        创建的云模式防护域名

        :param hostname: The hostname of this CreateHostResponse.
        :type: str
        """
        self._hostname = hostname

    @property
    def policyid(self):
        """Gets the policyid of this CreateHostResponse.

        策略id

        :return: The policyid of this CreateHostResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this CreateHostResponse.

        策略id

        :param policyid: The policyid of this CreateHostResponse.
        :type: str
        """
        self._policyid = policyid

    @property
    def access_code(self):
        """Gets the access_code of this CreateHostResponse.

        cname前缀

        :return: The access_code of this CreateHostResponse.
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        """Sets the access_code of this CreateHostResponse.

        cname前缀

        :param access_code: The access_code of this CreateHostResponse.
        :type: str
        """
        self._access_code = access_code

    @property
    def protect_status(self):
        """Gets the protect_status of this CreateHostResponse.

        防护状态

        :return: The protect_status of this CreateHostResponse.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this CreateHostResponse.

        防护状态

        :param protect_status: The protect_status of this CreateHostResponse.
        :type: int
        """
        self._protect_status = protect_status

    @property
    def access_status(self):
        """Gets the access_status of this CreateHostResponse.

        接入状态

        :return: The access_status of this CreateHostResponse.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        """Sets the access_status of this CreateHostResponse.

        接入状态

        :param access_status: The access_status of this CreateHostResponse.
        :type: int
        """
        self._access_status = access_status

    @property
    def protocol(self):
        """Gets the protocol of this CreateHostResponse.

        返回的客户端协议类型

        :return: The protocol of this CreateHostResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateHostResponse.

        返回的客户端协议类型

        :param protocol: The protocol of this CreateHostResponse.
        :type: str
        """
        self._protocol = protocol

    @property
    def certificateid(self):
        """Gets the certificateid of this CreateHostResponse.

        返回的证书id

        :return: The certificateid of this CreateHostResponse.
        :rtype: str
        """
        return self._certificateid

    @certificateid.setter
    def certificateid(self, certificateid):
        """Sets the certificateid of this CreateHostResponse.

        返回的证书id

        :param certificateid: The certificateid of this CreateHostResponse.
        :type: str
        """
        self._certificateid = certificateid

    @property
    def certificatename(self):
        """Gets the certificatename of this CreateHostResponse.

        证书名称

        :return: The certificatename of this CreateHostResponse.
        :rtype: str
        """
        return self._certificatename

    @certificatename.setter
    def certificatename(self, certificatename):
        """Sets the certificatename of this CreateHostResponse.

        证书名称

        :param certificatename: The certificatename of this CreateHostResponse.
        :type: str
        """
        self._certificatename = certificatename

    @property
    def server(self):
        """Gets the server of this CreateHostResponse.

        源站信息

        :return: The server of this CreateHostResponse.
        :rtype: list[CloudWafServer]
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this CreateHostResponse.

        源站信息

        :param server: The server of this CreateHostResponse.
        :type: list[CloudWafServer]
        """
        self._server = server

    @property
    def proxy(self):
        """Gets the proxy of this CreateHostResponse.

        是否开启了代理

        :return: The proxy of this CreateHostResponse.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this CreateHostResponse.

        是否开启了代理

        :param proxy: The proxy of this CreateHostResponse.
        :type: bool
        """
        self._proxy = proxy

    @property
    def timestamp(self):
        """Gets the timestamp of this CreateHostResponse.

        创建防护域名的时间

        :return: The timestamp of this CreateHostResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CreateHostResponse.

        创建防护域名的时间

        :param timestamp: The timestamp of this CreateHostResponse.
        :type: int
        """
        self._timestamp = timestamp

    @property
    def exclusive_ip(self):
        """Gets the exclusive_ip of this CreateHostResponse.

        是否使用独享ip

        :return: The exclusive_ip of this CreateHostResponse.
        :rtype: bool
        """
        return self._exclusive_ip

    @exclusive_ip.setter
    def exclusive_ip(self, exclusive_ip):
        """Sets the exclusive_ip of this CreateHostResponse.

        是否使用独享ip

        :param exclusive_ip: The exclusive_ip of this CreateHostResponse.
        :type: bool
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
        if not isinstance(other, CreateHostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
