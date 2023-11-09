# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpnGatewayCertificateConfig:

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
        'name': 'str',
        'vgw_id': 'str',
        'issuer': 'str',
        'signature_algorithm': 'str',
        'certificate_serial_number': 'str',
        'certificate_subject': 'str',
        'certificate_expire_time': 'datetime',
        'certificate_chain_serial_number': 'str',
        'certificate_chain_subject': 'str',
        'certificate_chain_expire_time': 'datetime',
        'enc_certificate_serial_number': 'str',
        'enc_certificate_subject': 'str',
        'enc_certificate_expire_time': 'datetime',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'vgw_id': 'vgw_id',
        'issuer': 'issuer',
        'signature_algorithm': 'signature_algorithm',
        'certificate_serial_number': 'certificate_serial_number',
        'certificate_subject': 'certificate_subject',
        'certificate_expire_time': 'certificate_expire_time',
        'certificate_chain_serial_number': 'certificate_chain_serial_number',
        'certificate_chain_subject': 'certificate_chain_subject',
        'certificate_chain_expire_time': 'certificate_chain_expire_time',
        'enc_certificate_serial_number': 'enc_certificate_serial_number',
        'enc_certificate_subject': 'enc_certificate_subject',
        'enc_certificate_expire_time': 'enc_certificate_expire_time',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, name=None, vgw_id=None, issuer=None, signature_algorithm=None, certificate_serial_number=None, certificate_subject=None, certificate_expire_time=None, certificate_chain_serial_number=None, certificate_chain_subject=None, certificate_chain_expire_time=None, enc_certificate_serial_number=None, enc_certificate_subject=None, enc_certificate_expire_time=None, created_at=None):
        """VpnGatewayCertificateConfig

        The model defined in huaweicloud sdk

        :param id: VPN网关证书ID
        :type id: str
        :param name: VPN网关证书名称
        :type name: str
        :param vgw_id: VPN网关ID
        :type vgw_id: str
        :param issuer: 签名证书颁发者，国密证书时为签名证书颁发者
        :type issuer: str
        :param signature_algorithm: 签名证书签名算法，国密证书时为签名证书签名算法
        :type signature_algorithm: str
        :param certificate_serial_number: 证书序列号，国密证书时为签名证书序列号
        :type certificate_serial_number: str
        :param certificate_subject: 签名证书主题，国密证书时为签名证书主题
        :type certificate_subject: str
        :param certificate_expire_time: 签名证书过期时间，国密证书时为签名证书过期时间
        :type certificate_expire_time: datetime
        :param certificate_chain_serial_number: CA证书序列号
        :type certificate_chain_serial_number: str
        :param certificate_chain_subject: CA证书主题
        :type certificate_chain_subject: str
        :param certificate_chain_expire_time: CA证书过期时间
        :type certificate_chain_expire_time: datetime
        :param enc_certificate_serial_number: 国密证书的加密证书序列号，
        :type enc_certificate_serial_number: str
        :param enc_certificate_subject: 国密证书的加密证书主题
        :type enc_certificate_subject: str
        :param enc_certificate_expire_time: 国密证书的加密证书过期时间
        :type enc_certificate_expire_time: datetime
        :param created_at: 创建时间
        :type created_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._vgw_id = None
        self._issuer = None
        self._signature_algorithm = None
        self._certificate_serial_number = None
        self._certificate_subject = None
        self._certificate_expire_time = None
        self._certificate_chain_serial_number = None
        self._certificate_chain_subject = None
        self._certificate_chain_expire_time = None
        self._enc_certificate_serial_number = None
        self._enc_certificate_subject = None
        self._enc_certificate_expire_time = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if vgw_id is not None:
            self.vgw_id = vgw_id
        if issuer is not None:
            self.issuer = issuer
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if certificate_serial_number is not None:
            self.certificate_serial_number = certificate_serial_number
        if certificate_subject is not None:
            self.certificate_subject = certificate_subject
        if certificate_expire_time is not None:
            self.certificate_expire_time = certificate_expire_time
        if certificate_chain_serial_number is not None:
            self.certificate_chain_serial_number = certificate_chain_serial_number
        if certificate_chain_subject is not None:
            self.certificate_chain_subject = certificate_chain_subject
        if certificate_chain_expire_time is not None:
            self.certificate_chain_expire_time = certificate_chain_expire_time
        if enc_certificate_serial_number is not None:
            self.enc_certificate_serial_number = enc_certificate_serial_number
        if enc_certificate_subject is not None:
            self.enc_certificate_subject = enc_certificate_subject
        if enc_certificate_expire_time is not None:
            self.enc_certificate_expire_time = enc_certificate_expire_time
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this VpnGatewayCertificateConfig.

        VPN网关证书ID

        :return: The id of this VpnGatewayCertificateConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VpnGatewayCertificateConfig.

        VPN网关证书ID

        :param id: The id of this VpnGatewayCertificateConfig.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this VpnGatewayCertificateConfig.

        VPN网关证书名称

        :return: The name of this VpnGatewayCertificateConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VpnGatewayCertificateConfig.

        VPN网关证书名称

        :param name: The name of this VpnGatewayCertificateConfig.
        :type name: str
        """
        self._name = name

    @property
    def vgw_id(self):
        """Gets the vgw_id of this VpnGatewayCertificateConfig.

        VPN网关ID

        :return: The vgw_id of this VpnGatewayCertificateConfig.
        :rtype: str
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        """Sets the vgw_id of this VpnGatewayCertificateConfig.

        VPN网关ID

        :param vgw_id: The vgw_id of this VpnGatewayCertificateConfig.
        :type vgw_id: str
        """
        self._vgw_id = vgw_id

    @property
    def issuer(self):
        """Gets the issuer of this VpnGatewayCertificateConfig.

        签名证书颁发者，国密证书时为签名证书颁发者

        :return: The issuer of this VpnGatewayCertificateConfig.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this VpnGatewayCertificateConfig.

        签名证书颁发者，国密证书时为签名证书颁发者

        :param issuer: The issuer of this VpnGatewayCertificateConfig.
        :type issuer: str
        """
        self._issuer = issuer

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this VpnGatewayCertificateConfig.

        签名证书签名算法，国密证书时为签名证书签名算法

        :return: The signature_algorithm of this VpnGatewayCertificateConfig.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this VpnGatewayCertificateConfig.

        签名证书签名算法，国密证书时为签名证书签名算法

        :param signature_algorithm: The signature_algorithm of this VpnGatewayCertificateConfig.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def certificate_serial_number(self):
        """Gets the certificate_serial_number of this VpnGatewayCertificateConfig.

        证书序列号，国密证书时为签名证书序列号

        :return: The certificate_serial_number of this VpnGatewayCertificateConfig.
        :rtype: str
        """
        return self._certificate_serial_number

    @certificate_serial_number.setter
    def certificate_serial_number(self, certificate_serial_number):
        """Sets the certificate_serial_number of this VpnGatewayCertificateConfig.

        证书序列号，国密证书时为签名证书序列号

        :param certificate_serial_number: The certificate_serial_number of this VpnGatewayCertificateConfig.
        :type certificate_serial_number: str
        """
        self._certificate_serial_number = certificate_serial_number

    @property
    def certificate_subject(self):
        """Gets the certificate_subject of this VpnGatewayCertificateConfig.

        签名证书主题，国密证书时为签名证书主题

        :return: The certificate_subject of this VpnGatewayCertificateConfig.
        :rtype: str
        """
        return self._certificate_subject

    @certificate_subject.setter
    def certificate_subject(self, certificate_subject):
        """Sets the certificate_subject of this VpnGatewayCertificateConfig.

        签名证书主题，国密证书时为签名证书主题

        :param certificate_subject: The certificate_subject of this VpnGatewayCertificateConfig.
        :type certificate_subject: str
        """
        self._certificate_subject = certificate_subject

    @property
    def certificate_expire_time(self):
        """Gets the certificate_expire_time of this VpnGatewayCertificateConfig.

        签名证书过期时间，国密证书时为签名证书过期时间

        :return: The certificate_expire_time of this VpnGatewayCertificateConfig.
        :rtype: datetime
        """
        return self._certificate_expire_time

    @certificate_expire_time.setter
    def certificate_expire_time(self, certificate_expire_time):
        """Sets the certificate_expire_time of this VpnGatewayCertificateConfig.

        签名证书过期时间，国密证书时为签名证书过期时间

        :param certificate_expire_time: The certificate_expire_time of this VpnGatewayCertificateConfig.
        :type certificate_expire_time: datetime
        """
        self._certificate_expire_time = certificate_expire_time

    @property
    def certificate_chain_serial_number(self):
        """Gets the certificate_chain_serial_number of this VpnGatewayCertificateConfig.

        CA证书序列号

        :return: The certificate_chain_serial_number of this VpnGatewayCertificateConfig.
        :rtype: str
        """
        return self._certificate_chain_serial_number

    @certificate_chain_serial_number.setter
    def certificate_chain_serial_number(self, certificate_chain_serial_number):
        """Sets the certificate_chain_serial_number of this VpnGatewayCertificateConfig.

        CA证书序列号

        :param certificate_chain_serial_number: The certificate_chain_serial_number of this VpnGatewayCertificateConfig.
        :type certificate_chain_serial_number: str
        """
        self._certificate_chain_serial_number = certificate_chain_serial_number

    @property
    def certificate_chain_subject(self):
        """Gets the certificate_chain_subject of this VpnGatewayCertificateConfig.

        CA证书主题

        :return: The certificate_chain_subject of this VpnGatewayCertificateConfig.
        :rtype: str
        """
        return self._certificate_chain_subject

    @certificate_chain_subject.setter
    def certificate_chain_subject(self, certificate_chain_subject):
        """Sets the certificate_chain_subject of this VpnGatewayCertificateConfig.

        CA证书主题

        :param certificate_chain_subject: The certificate_chain_subject of this VpnGatewayCertificateConfig.
        :type certificate_chain_subject: str
        """
        self._certificate_chain_subject = certificate_chain_subject

    @property
    def certificate_chain_expire_time(self):
        """Gets the certificate_chain_expire_time of this VpnGatewayCertificateConfig.

        CA证书过期时间

        :return: The certificate_chain_expire_time of this VpnGatewayCertificateConfig.
        :rtype: datetime
        """
        return self._certificate_chain_expire_time

    @certificate_chain_expire_time.setter
    def certificate_chain_expire_time(self, certificate_chain_expire_time):
        """Sets the certificate_chain_expire_time of this VpnGatewayCertificateConfig.

        CA证书过期时间

        :param certificate_chain_expire_time: The certificate_chain_expire_time of this VpnGatewayCertificateConfig.
        :type certificate_chain_expire_time: datetime
        """
        self._certificate_chain_expire_time = certificate_chain_expire_time

    @property
    def enc_certificate_serial_number(self):
        """Gets the enc_certificate_serial_number of this VpnGatewayCertificateConfig.

        国密证书的加密证书序列号，

        :return: The enc_certificate_serial_number of this VpnGatewayCertificateConfig.
        :rtype: str
        """
        return self._enc_certificate_serial_number

    @enc_certificate_serial_number.setter
    def enc_certificate_serial_number(self, enc_certificate_serial_number):
        """Sets the enc_certificate_serial_number of this VpnGatewayCertificateConfig.

        国密证书的加密证书序列号，

        :param enc_certificate_serial_number: The enc_certificate_serial_number of this VpnGatewayCertificateConfig.
        :type enc_certificate_serial_number: str
        """
        self._enc_certificate_serial_number = enc_certificate_serial_number

    @property
    def enc_certificate_subject(self):
        """Gets the enc_certificate_subject of this VpnGatewayCertificateConfig.

        国密证书的加密证书主题

        :return: The enc_certificate_subject of this VpnGatewayCertificateConfig.
        :rtype: str
        """
        return self._enc_certificate_subject

    @enc_certificate_subject.setter
    def enc_certificate_subject(self, enc_certificate_subject):
        """Sets the enc_certificate_subject of this VpnGatewayCertificateConfig.

        国密证书的加密证书主题

        :param enc_certificate_subject: The enc_certificate_subject of this VpnGatewayCertificateConfig.
        :type enc_certificate_subject: str
        """
        self._enc_certificate_subject = enc_certificate_subject

    @property
    def enc_certificate_expire_time(self):
        """Gets the enc_certificate_expire_time of this VpnGatewayCertificateConfig.

        国密证书的加密证书过期时间

        :return: The enc_certificate_expire_time of this VpnGatewayCertificateConfig.
        :rtype: datetime
        """
        return self._enc_certificate_expire_time

    @enc_certificate_expire_time.setter
    def enc_certificate_expire_time(self, enc_certificate_expire_time):
        """Sets the enc_certificate_expire_time of this VpnGatewayCertificateConfig.

        国密证书的加密证书过期时间

        :param enc_certificate_expire_time: The enc_certificate_expire_time of this VpnGatewayCertificateConfig.
        :type enc_certificate_expire_time: datetime
        """
        self._enc_certificate_expire_time = enc_certificate_expire_time

    @property
    def created_at(self):
        """Gets the created_at of this VpnGatewayCertificateConfig.

        创建时间

        :return: The created_at of this VpnGatewayCertificateConfig.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VpnGatewayCertificateConfig.

        创建时间

        :param created_at: The created_at of this VpnGatewayCertificateConfig.
        :type created_at: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, VpnGatewayCertificateConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
