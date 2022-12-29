# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertificateForm:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'cert_content': 'str',
        'private_key': 'str',
        'type': 'str',
        'instance_id': 'str',
        'trusted_root_ca': 'str'
    }

    attribute_map = {
        'name': 'name',
        'cert_content': 'cert_content',
        'private_key': 'private_key',
        'type': 'type',
        'instance_id': 'instance_id',
        'trusted_root_ca': 'trusted_root_ca'
    }

    def __init__(self, name=None, cert_content=None, private_key=None, type=None, instance_id=None, trusted_root_ca=None):
        """CertificateForm

        The model defined in huaweicloud sdk

        :param name: 证书名称
        :type name: str
        :param cert_content: 证书内容
        :type cert_content: str
        :param private_key: 证书私钥
        :type private_key: str
        :param type: 证书可见范围
        :type type: str
        :param instance_id: 所属实例ID，当type&#x3D;instance时必填
        :type instance_id: str
        :param trusted_root_ca: 信任的根证书CA
        :type trusted_root_ca: str
        """
        
        

        self._name = None
        self._cert_content = None
        self._private_key = None
        self._type = None
        self._instance_id = None
        self._trusted_root_ca = None
        self.discriminator = None

        self.name = name
        self.cert_content = cert_content
        self.private_key = private_key
        if type is not None:
            self.type = type
        if instance_id is not None:
            self.instance_id = instance_id
        if trusted_root_ca is not None:
            self.trusted_root_ca = trusted_root_ca

    @property
    def name(self):
        """Gets the name of this CertificateForm.

        证书名称

        :return: The name of this CertificateForm.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CertificateForm.

        证书名称

        :param name: The name of this CertificateForm.
        :type name: str
        """
        self._name = name

    @property
    def cert_content(self):
        """Gets the cert_content of this CertificateForm.

        证书内容

        :return: The cert_content of this CertificateForm.
        :rtype: str
        """
        return self._cert_content

    @cert_content.setter
    def cert_content(self, cert_content):
        """Sets the cert_content of this CertificateForm.

        证书内容

        :param cert_content: The cert_content of this CertificateForm.
        :type cert_content: str
        """
        self._cert_content = cert_content

    @property
    def private_key(self):
        """Gets the private_key of this CertificateForm.

        证书私钥

        :return: The private_key of this CertificateForm.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this CertificateForm.

        证书私钥

        :param private_key: The private_key of this CertificateForm.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def type(self):
        """Gets the type of this CertificateForm.

        证书可见范围

        :return: The type of this CertificateForm.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CertificateForm.

        证书可见范围

        :param type: The type of this CertificateForm.
        :type type: str
        """
        self._type = type

    @property
    def instance_id(self):
        """Gets the instance_id of this CertificateForm.

        所属实例ID，当type=instance时必填

        :return: The instance_id of this CertificateForm.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CertificateForm.

        所属实例ID，当type=instance时必填

        :param instance_id: The instance_id of this CertificateForm.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def trusted_root_ca(self):
        """Gets the trusted_root_ca of this CertificateForm.

        信任的根证书CA

        :return: The trusted_root_ca of this CertificateForm.
        :rtype: str
        """
        return self._trusted_root_ca

    @trusted_root_ca.setter
    def trusted_root_ca(self, trusted_root_ca):
        """Sets the trusted_root_ca of this CertificateForm.

        信任的根证书CA

        :param trusted_root_ca: The trusted_root_ca of this CertificateForm.
        :type trusted_root_ca: str
        """
        self._trusted_root_ca = trusted_root_ca

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
        if not isinstance(other, CertificateForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
