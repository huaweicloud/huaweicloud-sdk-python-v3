# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'protocol_type': 'ValueInAttributes',
        'protocol_name': 'ValueInAttributes',
        'slave_id': 'ValueInAttributes',
        'ip': 'ValueInAttributes',
        'port': 'ValueInAttributes',
        'serial_port': 'ValueInAttributes',
        'baud_rate': 'ValueInAttributes',
        'data_bits': 'ValueInAttributes',
        'stop_bits': 'ValueInAttributes',
        'parity_bits': 'ValueInAttributes',
        'url': 'ValueInAttributes',
        'sec_mode': 'ValueInAttributes',
        'sec_policy': 'ValueInAttributes',
        'auth_type': 'ValueInAttributes',
        'username': 'ValueInAttributes',
        'password': 'ValueInAttributes',
        'private_key': 'ValueInAttributes',
        'certificate': 'ValueInAttributes',
        'timeout': 'ValueInAttributes'
    }

    attribute_map = {
        'protocol_type': 'protocol_type',
        'protocol_name': 'protocol_name',
        'slave_id': 'slave_id',
        'ip': 'ip',
        'port': 'port',
        'serial_port': 'serial_port',
        'baud_rate': 'baud_rate',
        'data_bits': 'data_bits',
        'stop_bits': 'stop_bits',
        'parity_bits': 'parity_bits',
        'url': 'url',
        'sec_mode': 'sec_mode',
        'sec_policy': 'sec_policy',
        'auth_type': 'auth_type',
        'username': 'username',
        'password': 'password',
        'private_key': 'private_key',
        'certificate': 'certificate',
        'timeout': 'timeout'
    }

    def __init__(self, protocol_type=None, protocol_name=None, slave_id=None, ip=None, port=None, serial_port=None, baud_rate=None, data_bits=None, stop_bits=None, parity_bits=None, url=None, sec_mode=None, sec_policy=None, auth_type=None, username=None, password=None, private_key=None, certificate=None, timeout=None):
        """AccessConfig

        The model defined in huaweicloud sdk

        :param protocol_type: 
        :type protocol_type: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param protocol_name: 
        :type protocol_name: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param slave_id: 
        :type slave_id: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param ip: 
        :type ip: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param port: 
        :type port: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param serial_port: 
        :type serial_port: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param baud_rate: 
        :type baud_rate: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param data_bits: 
        :type data_bits: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param stop_bits: 
        :type stop_bits: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param parity_bits: 
        :type parity_bits: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param url: 
        :type url: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param sec_mode: 
        :type sec_mode: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param sec_policy: 
        :type sec_policy: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param auth_type: 
        :type auth_type: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param username: 
        :type username: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param password: 
        :type password: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param private_key: 
        :type private_key: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param certificate: 
        :type certificate: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        :param timeout: 
        :type timeout: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        
        

        self._protocol_type = None
        self._protocol_name = None
        self._slave_id = None
        self._ip = None
        self._port = None
        self._serial_port = None
        self._baud_rate = None
        self._data_bits = None
        self._stop_bits = None
        self._parity_bits = None
        self._url = None
        self._sec_mode = None
        self._sec_policy = None
        self._auth_type = None
        self._username = None
        self._password = None
        self._private_key = None
        self._certificate = None
        self._timeout = None
        self.discriminator = None

        self.protocol_type = protocol_type
        if protocol_name is not None:
            self.protocol_name = protocol_name
        if slave_id is not None:
            self.slave_id = slave_id
        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port
        if serial_port is not None:
            self.serial_port = serial_port
        if baud_rate is not None:
            self.baud_rate = baud_rate
        if data_bits is not None:
            self.data_bits = data_bits
        if stop_bits is not None:
            self.stop_bits = stop_bits
        if parity_bits is not None:
            self.parity_bits = parity_bits
        if url is not None:
            self.url = url
        if sec_mode is not None:
            self.sec_mode = sec_mode
        if sec_policy is not None:
            self.sec_policy = sec_policy
        if auth_type is not None:
            self.auth_type = auth_type
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if private_key is not None:
            self.private_key = private_key
        if certificate is not None:
            self.certificate = certificate
        if timeout is not None:
            self.timeout = timeout

    @property
    def protocol_type(self):
        """Gets the protocol_type of this AccessConfig.


        :return: The protocol_type of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this AccessConfig.


        :param protocol_type: The protocol_type of this AccessConfig.
        :type protocol_type: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._protocol_type = protocol_type

    @property
    def protocol_name(self):
        """Gets the protocol_name of this AccessConfig.


        :return: The protocol_name of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._protocol_name

    @protocol_name.setter
    def protocol_name(self, protocol_name):
        """Sets the protocol_name of this AccessConfig.


        :param protocol_name: The protocol_name of this AccessConfig.
        :type protocol_name: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._protocol_name = protocol_name

    @property
    def slave_id(self):
        """Gets the slave_id of this AccessConfig.


        :return: The slave_id of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._slave_id

    @slave_id.setter
    def slave_id(self, slave_id):
        """Sets the slave_id of this AccessConfig.


        :param slave_id: The slave_id of this AccessConfig.
        :type slave_id: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._slave_id = slave_id

    @property
    def ip(self):
        """Gets the ip of this AccessConfig.


        :return: The ip of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this AccessConfig.


        :param ip: The ip of this AccessConfig.
        :type ip: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._ip = ip

    @property
    def port(self):
        """Gets the port of this AccessConfig.


        :return: The port of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this AccessConfig.


        :param port: The port of this AccessConfig.
        :type port: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._port = port

    @property
    def serial_port(self):
        """Gets the serial_port of this AccessConfig.


        :return: The serial_port of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._serial_port

    @serial_port.setter
    def serial_port(self, serial_port):
        """Sets the serial_port of this AccessConfig.


        :param serial_port: The serial_port of this AccessConfig.
        :type serial_port: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._serial_port = serial_port

    @property
    def baud_rate(self):
        """Gets the baud_rate of this AccessConfig.


        :return: The baud_rate of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._baud_rate

    @baud_rate.setter
    def baud_rate(self, baud_rate):
        """Sets the baud_rate of this AccessConfig.


        :param baud_rate: The baud_rate of this AccessConfig.
        :type baud_rate: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._baud_rate = baud_rate

    @property
    def data_bits(self):
        """Gets the data_bits of this AccessConfig.


        :return: The data_bits of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._data_bits

    @data_bits.setter
    def data_bits(self, data_bits):
        """Sets the data_bits of this AccessConfig.


        :param data_bits: The data_bits of this AccessConfig.
        :type data_bits: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._data_bits = data_bits

    @property
    def stop_bits(self):
        """Gets the stop_bits of this AccessConfig.


        :return: The stop_bits of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._stop_bits

    @stop_bits.setter
    def stop_bits(self, stop_bits):
        """Sets the stop_bits of this AccessConfig.


        :param stop_bits: The stop_bits of this AccessConfig.
        :type stop_bits: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._stop_bits = stop_bits

    @property
    def parity_bits(self):
        """Gets the parity_bits of this AccessConfig.


        :return: The parity_bits of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._parity_bits

    @parity_bits.setter
    def parity_bits(self, parity_bits):
        """Sets the parity_bits of this AccessConfig.


        :param parity_bits: The parity_bits of this AccessConfig.
        :type parity_bits: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._parity_bits = parity_bits

    @property
    def url(self):
        """Gets the url of this AccessConfig.


        :return: The url of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AccessConfig.


        :param url: The url of this AccessConfig.
        :type url: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._url = url

    @property
    def sec_mode(self):
        """Gets the sec_mode of this AccessConfig.


        :return: The sec_mode of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._sec_mode

    @sec_mode.setter
    def sec_mode(self, sec_mode):
        """Sets the sec_mode of this AccessConfig.


        :param sec_mode: The sec_mode of this AccessConfig.
        :type sec_mode: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._sec_mode = sec_mode

    @property
    def sec_policy(self):
        """Gets the sec_policy of this AccessConfig.


        :return: The sec_policy of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._sec_policy

    @sec_policy.setter
    def sec_policy(self, sec_policy):
        """Sets the sec_policy of this AccessConfig.


        :param sec_policy: The sec_policy of this AccessConfig.
        :type sec_policy: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._sec_policy = sec_policy

    @property
    def auth_type(self):
        """Gets the auth_type of this AccessConfig.


        :return: The auth_type of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this AccessConfig.


        :param auth_type: The auth_type of this AccessConfig.
        :type auth_type: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._auth_type = auth_type

    @property
    def username(self):
        """Gets the username of this AccessConfig.


        :return: The username of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AccessConfig.


        :param username: The username of this AccessConfig.
        :type username: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._username = username

    @property
    def password(self):
        """Gets the password of this AccessConfig.


        :return: The password of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AccessConfig.


        :param password: The password of this AccessConfig.
        :type password: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._password = password

    @property
    def private_key(self):
        """Gets the private_key of this AccessConfig.


        :return: The private_key of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this AccessConfig.


        :param private_key: The private_key of this AccessConfig.
        :type private_key: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._private_key = private_key

    @property
    def certificate(self):
        """Gets the certificate of this AccessConfig.


        :return: The certificate of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this AccessConfig.


        :param certificate: The certificate of this AccessConfig.
        :type certificate: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._certificate = certificate

    @property
    def timeout(self):
        """Gets the timeout of this AccessConfig.


        :return: The timeout of this AccessConfig.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this AccessConfig.


        :param timeout: The timeout of this AccessConfig.
        :type timeout: :class:`huaweicloudsdkief.v1.ValueInAttributes`
        """
        self._timeout = timeout

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
        if not isinstance(other, AccessConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
