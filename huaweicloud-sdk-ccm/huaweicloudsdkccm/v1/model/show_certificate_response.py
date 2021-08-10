# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCertificateResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'certificate_id': 'str',
        'status': 'str',
        'freeze_flag': 'int',
        'gen_mode': 'str',
        'serial_number': 'str',
        'create_time': 'str',
        'not_before': 'str',
        'not_after': 'str',
        'distinguished_name': 'DistinguishedName',
        'issuer_id': 'str',
        'issuer_name': 'str',
        'key_algorithm': 'str',
        'signature_algorithm': 'str'
    }

    attribute_map = {
        'certificate_id': 'certificate_id',
        'status': 'status',
        'freeze_flag': 'freeze_flag',
        'gen_mode': 'gen_mode',
        'serial_number': 'serial_number',
        'create_time': 'create_time',
        'not_before': 'not_before',
        'not_after': 'not_after',
        'distinguished_name': 'distinguished_name',
        'issuer_id': 'issuer_id',
        'issuer_name': 'issuer_name',
        'key_algorithm': 'key_algorithm',
        'signature_algorithm': 'signature_algorithm'
    }

    def __init__(self, certificate_id=None, status=None, freeze_flag=None, gen_mode=None, serial_number=None, create_time=None, not_before=None, not_after=None, distinguished_name=None, issuer_id=None, issuer_name=None, key_algorithm=None, signature_algorithm=None):
        """ShowCertificateResponse - a model defined in huaweicloud sdk"""
        
        super(ShowCertificateResponse, self).__init__()

        self._certificate_id = None
        self._status = None
        self._freeze_flag = None
        self._gen_mode = None
        self._serial_number = None
        self._create_time = None
        self._not_before = None
        self._not_after = None
        self._distinguished_name = None
        self._issuer_id = None
        self._issuer_name = None
        self._key_algorithm = None
        self._signature_algorithm = None
        self.discriminator = None

        if certificate_id is not None:
            self.certificate_id = certificate_id
        if status is not None:
            self.status = status
        if freeze_flag is not None:
            self.freeze_flag = freeze_flag
        if gen_mode is not None:
            self.gen_mode = gen_mode
        if serial_number is not None:
            self.serial_number = serial_number
        if create_time is not None:
            self.create_time = create_time
        if not_before is not None:
            self.not_before = not_before
        if not_after is not None:
            self.not_after = not_after
        if distinguished_name is not None:
            self.distinguished_name = distinguished_name
        if issuer_id is not None:
            self.issuer_id = issuer_id
        if issuer_name is not None:
            self.issuer_name = issuer_name
        if key_algorithm is not None:
            self.key_algorithm = key_algorithm
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm

    @property
    def certificate_id(self):
        """Gets the certificate_id of this ShowCertificateResponse.

        证书 ID

        :return: The certificate_id of this ShowCertificateResponse.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this ShowCertificateResponse.

        证书 ID

        :param certificate_id: The certificate_id of this ShowCertificateResponse.
        :type: str
        """
        self._certificate_id = certificate_id

    @property
    def status(self):
        """Gets the status of this ShowCertificateResponse.

        证书状态

        :return: The status of this ShowCertificateResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowCertificateResponse.

        证书状态

        :param status: The status of this ShowCertificateResponse.
        :type: str
        """
        self._status = status

    @property
    def freeze_flag(self):
        """Gets the freeze_flag of this ShowCertificateResponse.

        冻结标识

        :return: The freeze_flag of this ShowCertificateResponse.
        :rtype: int
        """
        return self._freeze_flag

    @freeze_flag.setter
    def freeze_flag(self, freeze_flag):
        """Sets the freeze_flag of this ShowCertificateResponse.

        冻结标识

        :param freeze_flag: The freeze_flag of this ShowCertificateResponse.
        :type: int
        """
        self._freeze_flag = freeze_flag

    @property
    def gen_mode(self):
        """Gets the gen_mode of this ShowCertificateResponse.

        证书生成方式

        :return: The gen_mode of this ShowCertificateResponse.
        :rtype: str
        """
        return self._gen_mode

    @gen_mode.setter
    def gen_mode(self, gen_mode):
        """Sets the gen_mode of this ShowCertificateResponse.

        证书生成方式

        :param gen_mode: The gen_mode of this ShowCertificateResponse.
        :type: str
        """
        self._gen_mode = gen_mode

    @property
    def serial_number(self):
        """Gets the serial_number of this ShowCertificateResponse.

        序列号

        :return: The serial_number of this ShowCertificateResponse.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this ShowCertificateResponse.

        序列号

        :param serial_number: The serial_number of this ShowCertificateResponse.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def create_time(self):
        """Gets the create_time of this ShowCertificateResponse.

        创建时间

        :return: The create_time of this ShowCertificateResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowCertificateResponse.

        创建时间

        :param create_time: The create_time of this ShowCertificateResponse.
        :type: str
        """
        self._create_time = create_time

    @property
    def not_before(self):
        """Gets the not_before of this ShowCertificateResponse.

        生效时间

        :return: The not_before of this ShowCertificateResponse.
        :rtype: str
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """Sets the not_before of this ShowCertificateResponse.

        生效时间

        :param not_before: The not_before of this ShowCertificateResponse.
        :type: str
        """
        self._not_before = not_before

    @property
    def not_after(self):
        """Gets the not_after of this ShowCertificateResponse.

        失效时间

        :return: The not_after of this ShowCertificateResponse.
        :rtype: str
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this ShowCertificateResponse.

        失效时间

        :param not_after: The not_after of this ShowCertificateResponse.
        :type: str
        """
        self._not_after = not_after

    @property
    def distinguished_name(self):
        """Gets the distinguished_name of this ShowCertificateResponse.


        :return: The distinguished_name of this ShowCertificateResponse.
        :rtype: DistinguishedName
        """
        return self._distinguished_name

    @distinguished_name.setter
    def distinguished_name(self, distinguished_name):
        """Sets the distinguished_name of this ShowCertificateResponse.


        :param distinguished_name: The distinguished_name of this ShowCertificateResponse.
        :type: DistinguishedName
        """
        self._distinguished_name = distinguished_name

    @property
    def issuer_id(self):
        """Gets the issuer_id of this ShowCertificateResponse.

        签发CA ID

        :return: The issuer_id of this ShowCertificateResponse.
        :rtype: str
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id):
        """Sets the issuer_id of this ShowCertificateResponse.

        签发CA ID

        :param issuer_id: The issuer_id of this ShowCertificateResponse.
        :type: str
        """
        self._issuer_id = issuer_id

    @property
    def issuer_name(self):
        """Gets the issuer_name of this ShowCertificateResponse.

        签发CA名称

        :return: The issuer_name of this ShowCertificateResponse.
        :rtype: str
        """
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, issuer_name):
        """Sets the issuer_name of this ShowCertificateResponse.

        签发CA名称

        :param issuer_name: The issuer_name of this ShowCertificateResponse.
        :type: str
        """
        self._issuer_name = issuer_name

    @property
    def key_algorithm(self):
        """Gets the key_algorithm of this ShowCertificateResponse.

        密钥算法

        :return: The key_algorithm of this ShowCertificateResponse.
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        """Sets the key_algorithm of this ShowCertificateResponse.

        密钥算法

        :param key_algorithm: The key_algorithm of this ShowCertificateResponse.
        :type: str
        """
        self._key_algorithm = key_algorithm

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this ShowCertificateResponse.

        签名算法

        :return: The signature_algorithm of this ShowCertificateResponse.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this ShowCertificateResponse.

        签名算法

        :param signature_algorithm: The signature_algorithm of this ShowCertificateResponse.
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
        if not isinstance(other, ShowCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
