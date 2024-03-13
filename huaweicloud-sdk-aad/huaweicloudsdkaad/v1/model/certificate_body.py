# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertificateBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'op_type': 'int',
        'cert_name': 'str',
        'cert_file': 'str',
        'cert_key_file': 'str',
        'domain_id': 'str'
    }

    attribute_map = {
        'op_type': 'op_type',
        'cert_name': 'cert_name',
        'cert_file': 'cert_file',
        'cert_key_file': 'cert_key_file',
        'domain_id': 'domain_id'
    }

    def __init__(self, op_type=None, cert_name=None, cert_file=None, cert_key_file=None, domain_id=None):
        """CertificateBody

        The model defined in huaweicloud sdk

        :param op_type: 操作类型。0 - 上传， 1 - 更换
        :type op_type: int
        :param cert_name: 证书名称
        :type cert_name: str
        :param cert_file: 证书文件。上传新证书(op_type为0)时必填，更换为已有证书(op_type为1)时置空
        :type cert_file: str
        :param cert_key_file: 私钥文件。上传新证书(op_type为0)时必填，更换为已有证书(op_type为1)时置空
        :type cert_key_file: str
        :param domain_id: 域名id
        :type domain_id: str
        """
        
        

        self._op_type = None
        self._cert_name = None
        self._cert_file = None
        self._cert_key_file = None
        self._domain_id = None
        self.discriminator = None

        self.op_type = op_type
        self.cert_name = cert_name
        if cert_file is not None:
            self.cert_file = cert_file
        if cert_key_file is not None:
            self.cert_key_file = cert_key_file
        self.domain_id = domain_id

    @property
    def op_type(self):
        """Gets the op_type of this CertificateBody.

        操作类型。0 - 上传， 1 - 更换

        :return: The op_type of this CertificateBody.
        :rtype: int
        """
        return self._op_type

    @op_type.setter
    def op_type(self, op_type):
        """Sets the op_type of this CertificateBody.

        操作类型。0 - 上传， 1 - 更换

        :param op_type: The op_type of this CertificateBody.
        :type op_type: int
        """
        self._op_type = op_type

    @property
    def cert_name(self):
        """Gets the cert_name of this CertificateBody.

        证书名称

        :return: The cert_name of this CertificateBody.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        """Sets the cert_name of this CertificateBody.

        证书名称

        :param cert_name: The cert_name of this CertificateBody.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def cert_file(self):
        """Gets the cert_file of this CertificateBody.

        证书文件。上传新证书(op_type为0)时必填，更换为已有证书(op_type为1)时置空

        :return: The cert_file of this CertificateBody.
        :rtype: str
        """
        return self._cert_file

    @cert_file.setter
    def cert_file(self, cert_file):
        """Sets the cert_file of this CertificateBody.

        证书文件。上传新证书(op_type为0)时必填，更换为已有证书(op_type为1)时置空

        :param cert_file: The cert_file of this CertificateBody.
        :type cert_file: str
        """
        self._cert_file = cert_file

    @property
    def cert_key_file(self):
        """Gets the cert_key_file of this CertificateBody.

        私钥文件。上传新证书(op_type为0)时必填，更换为已有证书(op_type为1)时置空

        :return: The cert_key_file of this CertificateBody.
        :rtype: str
        """
        return self._cert_key_file

    @cert_key_file.setter
    def cert_key_file(self, cert_key_file):
        """Sets the cert_key_file of this CertificateBody.

        私钥文件。上传新证书(op_type为0)时必填，更换为已有证书(op_type为1)时置空

        :param cert_key_file: The cert_key_file of this CertificateBody.
        :type cert_key_file: str
        """
        self._cert_key_file = cert_key_file

    @property
    def domain_id(self):
        """Gets the domain_id of this CertificateBody.

        域名id

        :return: The domain_id of this CertificateBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CertificateBody.

        域名id

        :param domain_id: The domain_id of this CertificateBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

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
        if not isinstance(other, CertificateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
