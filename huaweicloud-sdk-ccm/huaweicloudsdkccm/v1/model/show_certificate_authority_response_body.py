# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCertificateAuthorityResponseBody:


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
        'freeze_flag': 'int',
        'gen_mode': 'str',
        'serial_number': 'str',
        'create_time': 'str',
        'delete_time': 'str',
        'not_before': 'str',
        'not_after': 'str',
        'distinguished_name': 'DistinguishedName',
        'crl_configuration': 'CrlConfiguration',
        'issuer_id': 'str',
        'issuer_name': 'str',
        'key_algorithm': 'str',
        'signature_algorithm': 'str'
    }

    attribute_map = {
        'ca_id': 'ca_id',
        'type': 'type',
        'status': 'status',
        'path_length': 'path_length',
        'freeze_flag': 'freeze_flag',
        'gen_mode': 'gen_mode',
        'serial_number': 'serial_number',
        'create_time': 'create_time',
        'delete_time': 'delete_time',
        'not_before': 'not_before',
        'not_after': 'not_after',
        'distinguished_name': 'distinguished_name',
        'crl_configuration': 'crl_configuration',
        'issuer_id': 'issuer_id',
        'issuer_name': 'issuer_name',
        'key_algorithm': 'key_algorithm',
        'signature_algorithm': 'signature_algorithm'
    }

    def __init__(self, ca_id=None, type=None, status=None, path_length=None, freeze_flag=None, gen_mode=None, serial_number=None, create_time=None, delete_time=None, not_before=None, not_after=None, distinguished_name=None, crl_configuration=None, issuer_id=None, issuer_name=None, key_algorithm=None, signature_algorithm=None):
        """ShowCertificateAuthorityResponseBody - a model defined in huaweicloud sdk"""
        
        

        self._ca_id = None
        self._type = None
        self._status = None
        self._path_length = None
        self._freeze_flag = None
        self._gen_mode = None
        self._serial_number = None
        self._create_time = None
        self._delete_time = None
        self._not_before = None
        self._not_after = None
        self._distinguished_name = None
        self._crl_configuration = None
        self._issuer_id = None
        self._issuer_name = None
        self._key_algorithm = None
        self._signature_algorithm = None
        self.discriminator = None

        if ca_id is not None:
            self.ca_id = ca_id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if path_length is not None:
            self.path_length = path_length
        if freeze_flag is not None:
            self.freeze_flag = freeze_flag
        if gen_mode is not None:
            self.gen_mode = gen_mode
        if serial_number is not None:
            self.serial_number = serial_number
        if create_time is not None:
            self.create_time = create_time
        if delete_time is not None:
            self.delete_time = delete_time
        if not_before is not None:
            self.not_before = not_before
        if not_after is not None:
            self.not_after = not_after
        if distinguished_name is not None:
            self.distinguished_name = distinguished_name
        if crl_configuration is not None:
            self.crl_configuration = crl_configuration
        if issuer_id is not None:
            self.issuer_id = issuer_id
        if issuer_name is not None:
            self.issuer_name = issuer_name
        if key_algorithm is not None:
            self.key_algorithm = key_algorithm
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm

    @property
    def ca_id(self):
        """Gets the ca_id of this ShowCertificateAuthorityResponseBody.

        CA ID

        :return: The ca_id of this ShowCertificateAuthorityResponseBody.
        :rtype: str
        """
        return self._ca_id

    @ca_id.setter
    def ca_id(self, ca_id):
        """Sets the ca_id of this ShowCertificateAuthorityResponseBody.

        CA ID

        :param ca_id: The ca_id of this ShowCertificateAuthorityResponseBody.
        :type: str
        """
        self._ca_id = ca_id

    @property
    def type(self):
        """Gets the type of this ShowCertificateAuthorityResponseBody.

        CA类型

        :return: The type of this ShowCertificateAuthorityResponseBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowCertificateAuthorityResponseBody.

        CA类型

        :param type: The type of this ShowCertificateAuthorityResponseBody.
        :type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this ShowCertificateAuthorityResponseBody.

        证书状态

        :return: The status of this ShowCertificateAuthorityResponseBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowCertificateAuthorityResponseBody.

        证书状态

        :param status: The status of this ShowCertificateAuthorityResponseBody.
        :type: str
        """
        self._status = status

    @property
    def path_length(self):
        """Gets the path_length of this ShowCertificateAuthorityResponseBody.

        路径长度

        :return: The path_length of this ShowCertificateAuthorityResponseBody.
        :rtype: int
        """
        return self._path_length

    @path_length.setter
    def path_length(self, path_length):
        """Sets the path_length of this ShowCertificateAuthorityResponseBody.

        路径长度

        :param path_length: The path_length of this ShowCertificateAuthorityResponseBody.
        :type: int
        """
        self._path_length = path_length

    @property
    def freeze_flag(self):
        """Gets the freeze_flag of this ShowCertificateAuthorityResponseBody.

        冻结标识

        :return: The freeze_flag of this ShowCertificateAuthorityResponseBody.
        :rtype: int
        """
        return self._freeze_flag

    @freeze_flag.setter
    def freeze_flag(self, freeze_flag):
        """Sets the freeze_flag of this ShowCertificateAuthorityResponseBody.

        冻结标识

        :param freeze_flag: The freeze_flag of this ShowCertificateAuthorityResponseBody.
        :type: int
        """
        self._freeze_flag = freeze_flag

    @property
    def gen_mode(self):
        """Gets the gen_mode of this ShowCertificateAuthorityResponseBody.

        证书生成方式

        :return: The gen_mode of this ShowCertificateAuthorityResponseBody.
        :rtype: str
        """
        return self._gen_mode

    @gen_mode.setter
    def gen_mode(self, gen_mode):
        """Sets the gen_mode of this ShowCertificateAuthorityResponseBody.

        证书生成方式

        :param gen_mode: The gen_mode of this ShowCertificateAuthorityResponseBody.
        :type: str
        """
        self._gen_mode = gen_mode

    @property
    def serial_number(self):
        """Gets the serial_number of this ShowCertificateAuthorityResponseBody.

        序列号

        :return: The serial_number of this ShowCertificateAuthorityResponseBody.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this ShowCertificateAuthorityResponseBody.

        序列号

        :param serial_number: The serial_number of this ShowCertificateAuthorityResponseBody.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def create_time(self):
        """Gets the create_time of this ShowCertificateAuthorityResponseBody.

        创建时间

        :return: The create_time of this ShowCertificateAuthorityResponseBody.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowCertificateAuthorityResponseBody.

        创建时间

        :param create_time: The create_time of this ShowCertificateAuthorityResponseBody.
        :type: str
        """
        self._create_time = create_time

    @property
    def delete_time(self):
        """Gets the delete_time of this ShowCertificateAuthorityResponseBody.

        删除时间

        :return: The delete_time of this ShowCertificateAuthorityResponseBody.
        :rtype: str
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        """Sets the delete_time of this ShowCertificateAuthorityResponseBody.

        删除时间

        :param delete_time: The delete_time of this ShowCertificateAuthorityResponseBody.
        :type: str
        """
        self._delete_time = delete_time

    @property
    def not_before(self):
        """Gets the not_before of this ShowCertificateAuthorityResponseBody.

        生效时间

        :return: The not_before of this ShowCertificateAuthorityResponseBody.
        :rtype: str
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """Sets the not_before of this ShowCertificateAuthorityResponseBody.

        生效时间

        :param not_before: The not_before of this ShowCertificateAuthorityResponseBody.
        :type: str
        """
        self._not_before = not_before

    @property
    def not_after(self):
        """Gets the not_after of this ShowCertificateAuthorityResponseBody.

        失效时间

        :return: The not_after of this ShowCertificateAuthorityResponseBody.
        :rtype: str
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this ShowCertificateAuthorityResponseBody.

        失效时间

        :param not_after: The not_after of this ShowCertificateAuthorityResponseBody.
        :type: str
        """
        self._not_after = not_after

    @property
    def distinguished_name(self):
        """Gets the distinguished_name of this ShowCertificateAuthorityResponseBody.


        :return: The distinguished_name of this ShowCertificateAuthorityResponseBody.
        :rtype: DistinguishedName
        """
        return self._distinguished_name

    @distinguished_name.setter
    def distinguished_name(self, distinguished_name):
        """Sets the distinguished_name of this ShowCertificateAuthorityResponseBody.


        :param distinguished_name: The distinguished_name of this ShowCertificateAuthorityResponseBody.
        :type: DistinguishedName
        """
        self._distinguished_name = distinguished_name

    @property
    def crl_configuration(self):
        """Gets the crl_configuration of this ShowCertificateAuthorityResponseBody.


        :return: The crl_configuration of this ShowCertificateAuthorityResponseBody.
        :rtype: CrlConfiguration
        """
        return self._crl_configuration

    @crl_configuration.setter
    def crl_configuration(self, crl_configuration):
        """Sets the crl_configuration of this ShowCertificateAuthorityResponseBody.


        :param crl_configuration: The crl_configuration of this ShowCertificateAuthorityResponseBody.
        :type: CrlConfiguration
        """
        self._crl_configuration = crl_configuration

    @property
    def issuer_id(self):
        """Gets the issuer_id of this ShowCertificateAuthorityResponseBody.

        签发CA ID

        :return: The issuer_id of this ShowCertificateAuthorityResponseBody.
        :rtype: str
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id):
        """Sets the issuer_id of this ShowCertificateAuthorityResponseBody.

        签发CA ID

        :param issuer_id: The issuer_id of this ShowCertificateAuthorityResponseBody.
        :type: str
        """
        self._issuer_id = issuer_id

    @property
    def issuer_name(self):
        """Gets the issuer_name of this ShowCertificateAuthorityResponseBody.

        签发CA名称

        :return: The issuer_name of this ShowCertificateAuthorityResponseBody.
        :rtype: str
        """
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, issuer_name):
        """Sets the issuer_name of this ShowCertificateAuthorityResponseBody.

        签发CA名称

        :param issuer_name: The issuer_name of this ShowCertificateAuthorityResponseBody.
        :type: str
        """
        self._issuer_name = issuer_name

    @property
    def key_algorithm(self):
        """Gets the key_algorithm of this ShowCertificateAuthorityResponseBody.

        密钥算法

        :return: The key_algorithm of this ShowCertificateAuthorityResponseBody.
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        """Sets the key_algorithm of this ShowCertificateAuthorityResponseBody.

        密钥算法

        :param key_algorithm: The key_algorithm of this ShowCertificateAuthorityResponseBody.
        :type: str
        """
        self._key_algorithm = key_algorithm

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this ShowCertificateAuthorityResponseBody.

        签名算法

        :return: The signature_algorithm of this ShowCertificateAuthorityResponseBody.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this ShowCertificateAuthorityResponseBody.

        签名算法

        :param signature_algorithm: The signature_algorithm of this ShowCertificateAuthorityResponseBody.
        :type: str
        """
        self._signature_algorithm = signature_algorithm

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
        if not isinstance(other, ShowCertificateAuthorityResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
