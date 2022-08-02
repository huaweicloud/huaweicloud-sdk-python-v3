# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertificateAuthorities:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ca_id': 'str',
        'type': 'str',
        'status': 'str',
        'path_length': 'int',
        'issuer_id': 'str',
        'issuer_name': 'str',
        'key_algorithm': 'str',
        'signature_algorithm': 'str',
        'freeze_flag': 'int',
        'gen_mode': 'str',
        'serial_number': 'str',
        'create_time': 'int',
        'delete_time': 'int',
        'not_before': 'int',
        'not_after': 'int',
        'distinguished_name': 'DistinguishedName',
        'crl_configuration': 'ListCrlConfiguration'
    }

    attribute_map = {
        'ca_id': 'ca_id',
        'type': 'type',
        'status': 'status',
        'path_length': 'path_length',
        'issuer_id': 'issuer_id',
        'issuer_name': 'issuer_name',
        'key_algorithm': 'key_algorithm',
        'signature_algorithm': 'signature_algorithm',
        'freeze_flag': 'freeze_flag',
        'gen_mode': 'gen_mode',
        'serial_number': 'serial_number',
        'create_time': 'create_time',
        'delete_time': 'delete_time',
        'not_before': 'not_before',
        'not_after': 'not_after',
        'distinguished_name': 'distinguished_name',
        'crl_configuration': 'crl_configuration'
    }

    def __init__(self, ca_id=None, type=None, status=None, path_length=None, issuer_id=None, issuer_name=None, key_algorithm=None, signature_algorithm=None, freeze_flag=None, gen_mode=None, serial_number=None, create_time=None, delete_time=None, not_before=None, not_after=None, distinguished_name=None, crl_configuration=None):
        """CertificateAuthorities

        The model defined in huaweicloud sdk

        :param ca_id: CA证书ID。
        :type ca_id: str
        :param type: CA类型:   - **ROOT**: 根CA   - **SUBORDINATE**: 从属CA
        :type type: str
        :param status: CA证书状态：   - **PENDING** : 待激活，此状态下，不可用于签发证书；   - **ACTIVED** : 已激活，此状态下，可用于签发证书；   - **DISABLED** : 已禁用，此状态下，不可用于签发证书；   - **DELETED** : 计划删除，此状态下，不可用于签发证书；   - **EXPIRED** : 已过期，此状态下，不可用于签发证书。
        :type status: str
        :param path_length: CA路径长度。 &gt; 注：生成的根CA证书，其路径长度不做限制，但本字段在数据库中统一置为7。从属CA的路径长度在创建时由用户指定，缺省值为0。
        :type path_length: int
        :param issuer_id: 父CA证书ID，即签发此证书的CA证书ID。根CA中，此参数为**null**。
        :type issuer_id: str
        :param issuer_name: 父CA证书名称。根CA中，此参数为**null**。
        :type issuer_name: str
        :param key_algorithm: 密钥算法。
        :type key_algorithm: str
        :param signature_algorithm: 签名哈希算法。
        :type signature_algorithm: str
        :param freeze_flag: 冻结标识:   - **0** : 非冻结状态；   - **其它值** : 冻结状态，当前预留。
        :type freeze_flag: int
        :param gen_mode: 证书生成方式：  - **GENERATE** : PCA系统生成；  - **IMPORT** : 外部导入；  - **CSR** : 外部提供CSR，内部CA进行签发，即私钥不在PCA进行托管。
        :type gen_mode: str
        :param serial_number: 证书序列号。
        :type serial_number: str
        :param create_time: 证书创建时间，格式为时间戳（毫秒级）。
        :type create_time: int
        :param delete_time: 证书删除时间，格式为时间戳（毫秒级）。
        :type delete_time: int
        :param not_before: 证书创建时间，格式为时间戳（毫秒级）。
        :type not_before: int
        :param not_after: 证书到期时间，格式为时间戳（毫秒级）。
        :type not_after: int
        :param distinguished_name: 
        :type distinguished_name: :class:`huaweicloudsdkccm.v1.DistinguishedName`
        :param crl_configuration: 
        :type crl_configuration: :class:`huaweicloudsdkccm.v1.ListCrlConfiguration`
        """
        
        

        self._ca_id = None
        self._type = None
        self._status = None
        self._path_length = None
        self._issuer_id = None
        self._issuer_name = None
        self._key_algorithm = None
        self._signature_algorithm = None
        self._freeze_flag = None
        self._gen_mode = None
        self._serial_number = None
        self._create_time = None
        self._delete_time = None
        self._not_before = None
        self._not_after = None
        self._distinguished_name = None
        self._crl_configuration = None
        self.discriminator = None

        self.ca_id = ca_id
        self.type = type
        self.status = status
        self.path_length = path_length
        self.issuer_id = issuer_id
        self.issuer_name = issuer_name
        self.key_algorithm = key_algorithm
        self.signature_algorithm = signature_algorithm
        self.freeze_flag = freeze_flag
        self.gen_mode = gen_mode
        self.serial_number = serial_number
        self.create_time = create_time
        self.delete_time = delete_time
        self.not_before = not_before
        self.not_after = not_after
        self.distinguished_name = distinguished_name
        self.crl_configuration = crl_configuration

    @property
    def ca_id(self):
        """Gets the ca_id of this CertificateAuthorities.

        CA证书ID。

        :return: The ca_id of this CertificateAuthorities.
        :rtype: str
        """
        return self._ca_id

    @ca_id.setter
    def ca_id(self, ca_id):
        """Sets the ca_id of this CertificateAuthorities.

        CA证书ID。

        :param ca_id: The ca_id of this CertificateAuthorities.
        :type ca_id: str
        """
        self._ca_id = ca_id

    @property
    def type(self):
        """Gets the type of this CertificateAuthorities.

        CA类型:   - **ROOT**: 根CA   - **SUBORDINATE**: 从属CA

        :return: The type of this CertificateAuthorities.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CertificateAuthorities.

        CA类型:   - **ROOT**: 根CA   - **SUBORDINATE**: 从属CA

        :param type: The type of this CertificateAuthorities.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this CertificateAuthorities.

        CA证书状态：   - **PENDING** : 待激活，此状态下，不可用于签发证书；   - **ACTIVED** : 已激活，此状态下，可用于签发证书；   - **DISABLED** : 已禁用，此状态下，不可用于签发证书；   - **DELETED** : 计划删除，此状态下，不可用于签发证书；   - **EXPIRED** : 已过期，此状态下，不可用于签发证书。

        :return: The status of this CertificateAuthorities.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CertificateAuthorities.

        CA证书状态：   - **PENDING** : 待激活，此状态下，不可用于签发证书；   - **ACTIVED** : 已激活，此状态下，可用于签发证书；   - **DISABLED** : 已禁用，此状态下，不可用于签发证书；   - **DELETED** : 计划删除，此状态下，不可用于签发证书；   - **EXPIRED** : 已过期，此状态下，不可用于签发证书。

        :param status: The status of this CertificateAuthorities.
        :type status: str
        """
        self._status = status

    @property
    def path_length(self):
        """Gets the path_length of this CertificateAuthorities.

        CA路径长度。 > 注：生成的根CA证书，其路径长度不做限制，但本字段在数据库中统一置为7。从属CA的路径长度在创建时由用户指定，缺省值为0。

        :return: The path_length of this CertificateAuthorities.
        :rtype: int
        """
        return self._path_length

    @path_length.setter
    def path_length(self, path_length):
        """Sets the path_length of this CertificateAuthorities.

        CA路径长度。 > 注：生成的根CA证书，其路径长度不做限制，但本字段在数据库中统一置为7。从属CA的路径长度在创建时由用户指定，缺省值为0。

        :param path_length: The path_length of this CertificateAuthorities.
        :type path_length: int
        """
        self._path_length = path_length

    @property
    def issuer_id(self):
        """Gets the issuer_id of this CertificateAuthorities.

        父CA证书ID，即签发此证书的CA证书ID。根CA中，此参数为**null**。

        :return: The issuer_id of this CertificateAuthorities.
        :rtype: str
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id):
        """Sets the issuer_id of this CertificateAuthorities.

        父CA证书ID，即签发此证书的CA证书ID。根CA中，此参数为**null**。

        :param issuer_id: The issuer_id of this CertificateAuthorities.
        :type issuer_id: str
        """
        self._issuer_id = issuer_id

    @property
    def issuer_name(self):
        """Gets the issuer_name of this CertificateAuthorities.

        父CA证书名称。根CA中，此参数为**null**。

        :return: The issuer_name of this CertificateAuthorities.
        :rtype: str
        """
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, issuer_name):
        """Sets the issuer_name of this CertificateAuthorities.

        父CA证书名称。根CA中，此参数为**null**。

        :param issuer_name: The issuer_name of this CertificateAuthorities.
        :type issuer_name: str
        """
        self._issuer_name = issuer_name

    @property
    def key_algorithm(self):
        """Gets the key_algorithm of this CertificateAuthorities.

        密钥算法。

        :return: The key_algorithm of this CertificateAuthorities.
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        """Sets the key_algorithm of this CertificateAuthorities.

        密钥算法。

        :param key_algorithm: The key_algorithm of this CertificateAuthorities.
        :type key_algorithm: str
        """
        self._key_algorithm = key_algorithm

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this CertificateAuthorities.

        签名哈希算法。

        :return: The signature_algorithm of this CertificateAuthorities.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this CertificateAuthorities.

        签名哈希算法。

        :param signature_algorithm: The signature_algorithm of this CertificateAuthorities.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def freeze_flag(self):
        """Gets the freeze_flag of this CertificateAuthorities.

        冻结标识:   - **0** : 非冻结状态；   - **其它值** : 冻结状态，当前预留。

        :return: The freeze_flag of this CertificateAuthorities.
        :rtype: int
        """
        return self._freeze_flag

    @freeze_flag.setter
    def freeze_flag(self, freeze_flag):
        """Sets the freeze_flag of this CertificateAuthorities.

        冻结标识:   - **0** : 非冻结状态；   - **其它值** : 冻结状态，当前预留。

        :param freeze_flag: The freeze_flag of this CertificateAuthorities.
        :type freeze_flag: int
        """
        self._freeze_flag = freeze_flag

    @property
    def gen_mode(self):
        """Gets the gen_mode of this CertificateAuthorities.

        证书生成方式：  - **GENERATE** : PCA系统生成；  - **IMPORT** : 外部导入；  - **CSR** : 外部提供CSR，内部CA进行签发，即私钥不在PCA进行托管。

        :return: The gen_mode of this CertificateAuthorities.
        :rtype: str
        """
        return self._gen_mode

    @gen_mode.setter
    def gen_mode(self, gen_mode):
        """Sets the gen_mode of this CertificateAuthorities.

        证书生成方式：  - **GENERATE** : PCA系统生成；  - **IMPORT** : 外部导入；  - **CSR** : 外部提供CSR，内部CA进行签发，即私钥不在PCA进行托管。

        :param gen_mode: The gen_mode of this CertificateAuthorities.
        :type gen_mode: str
        """
        self._gen_mode = gen_mode

    @property
    def serial_number(self):
        """Gets the serial_number of this CertificateAuthorities.

        证书序列号。

        :return: The serial_number of this CertificateAuthorities.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this CertificateAuthorities.

        证书序列号。

        :param serial_number: The serial_number of this CertificateAuthorities.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def create_time(self):
        """Gets the create_time of this CertificateAuthorities.

        证书创建时间，格式为时间戳（毫秒级）。

        :return: The create_time of this CertificateAuthorities.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CertificateAuthorities.

        证书创建时间，格式为时间戳（毫秒级）。

        :param create_time: The create_time of this CertificateAuthorities.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def delete_time(self):
        """Gets the delete_time of this CertificateAuthorities.

        证书删除时间，格式为时间戳（毫秒级）。

        :return: The delete_time of this CertificateAuthorities.
        :rtype: int
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        """Sets the delete_time of this CertificateAuthorities.

        证书删除时间，格式为时间戳（毫秒级）。

        :param delete_time: The delete_time of this CertificateAuthorities.
        :type delete_time: int
        """
        self._delete_time = delete_time

    @property
    def not_before(self):
        """Gets the not_before of this CertificateAuthorities.

        证书创建时间，格式为时间戳（毫秒级）。

        :return: The not_before of this CertificateAuthorities.
        :rtype: int
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """Sets the not_before of this CertificateAuthorities.

        证书创建时间，格式为时间戳（毫秒级）。

        :param not_before: The not_before of this CertificateAuthorities.
        :type not_before: int
        """
        self._not_before = not_before

    @property
    def not_after(self):
        """Gets the not_after of this CertificateAuthorities.

        证书到期时间，格式为时间戳（毫秒级）。

        :return: The not_after of this CertificateAuthorities.
        :rtype: int
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this CertificateAuthorities.

        证书到期时间，格式为时间戳（毫秒级）。

        :param not_after: The not_after of this CertificateAuthorities.
        :type not_after: int
        """
        self._not_after = not_after

    @property
    def distinguished_name(self):
        """Gets the distinguished_name of this CertificateAuthorities.


        :return: The distinguished_name of this CertificateAuthorities.
        :rtype: :class:`huaweicloudsdkccm.v1.DistinguishedName`
        """
        return self._distinguished_name

    @distinguished_name.setter
    def distinguished_name(self, distinguished_name):
        """Sets the distinguished_name of this CertificateAuthorities.


        :param distinguished_name: The distinguished_name of this CertificateAuthorities.
        :type distinguished_name: :class:`huaweicloudsdkccm.v1.DistinguishedName`
        """
        self._distinguished_name = distinguished_name

    @property
    def crl_configuration(self):
        """Gets the crl_configuration of this CertificateAuthorities.


        :return: The crl_configuration of this CertificateAuthorities.
        :rtype: :class:`huaweicloudsdkccm.v1.ListCrlConfiguration`
        """
        return self._crl_configuration

    @crl_configuration.setter
    def crl_configuration(self, crl_configuration):
        """Sets the crl_configuration of this CertificateAuthorities.


        :param crl_configuration: The crl_configuration of this CertificateAuthorities.
        :type crl_configuration: :class:`huaweicloudsdkccm.v1.ListCrlConfiguration`
        """
        self._crl_configuration = crl_configuration

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
        if not isinstance(other, CertificateAuthorities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
