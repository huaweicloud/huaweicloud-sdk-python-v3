# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'cert_id': 'str',
        'common_name': 'str',
        'type': 'str',
        'status': 'str',
        'key_algorithm': 'str',
        'signature_algorithm': 'str',
        'apply': 'str',
        'not_before': 'str',
        'not_after': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'cert_id': 'cert_id',
        'common_name': 'common_name',
        'type': 'type',
        'status': 'status',
        'key_algorithm': 'key_algorithm',
        'signature_algorithm': 'signature_algorithm',
        'apply': 'apply',
        'not_before': 'not_before',
        'not_after': 'not_after'
    }

    def __init__(self, tenant_id=None, cert_id=None, common_name=None, type=None, status=None, key_algorithm=None, signature_algorithm=None, apply=None, not_before=None, not_after=None):
        r"""CertItem

        The model defined in huaweicloud sdk

        :param tenant_id: 租户id。
        :type tenant_id: str
        :param cert_id: 证书id。
        :type cert_id: str
        :param common_name: 证书名。
        :type common_name: str
        :param type: 证书类型ROOT, SUBORDINATE。
        :type type: str
        :param status: 证书状态 DISABLE,ENABLE,EXPIRED,DELETE。
        :type status: str
        :param key_algorithm: 密钥生成算法 RSA-2048,RSA-3072。
        :type key_algorithm: str
        :param signature_algorithm: 签名哈希算法。
        :type signature_algorithm: str
        :param apply: 应用场景。
        :type apply: str
        :param not_before: 生效时间。
        :type not_before: str
        :param not_after: 过期时间。
        :type not_after: str
        """
        
        

        self._tenant_id = None
        self._cert_id = None
        self._common_name = None
        self._type = None
        self._status = None
        self._key_algorithm = None
        self._signature_algorithm = None
        self._apply = None
        self._not_before = None
        self._not_after = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if cert_id is not None:
            self.cert_id = cert_id
        if common_name is not None:
            self.common_name = common_name
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if key_algorithm is not None:
            self.key_algorithm = key_algorithm
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if apply is not None:
            self.apply = apply
        if not_before is not None:
            self.not_before = not_before
        if not_after is not None:
            self.not_after = not_after

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this CertItem.

        租户id。

        :return: The tenant_id of this CertItem.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this CertItem.

        租户id。

        :param tenant_id: The tenant_id of this CertItem.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def cert_id(self):
        r"""Gets the cert_id of this CertItem.

        证书id。

        :return: The cert_id of this CertItem.
        :rtype: str
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        r"""Sets the cert_id of this CertItem.

        证书id。

        :param cert_id: The cert_id of this CertItem.
        :type cert_id: str
        """
        self._cert_id = cert_id

    @property
    def common_name(self):
        r"""Gets the common_name of this CertItem.

        证书名。

        :return: The common_name of this CertItem.
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        r"""Sets the common_name of this CertItem.

        证书名。

        :param common_name: The common_name of this CertItem.
        :type common_name: str
        """
        self._common_name = common_name

    @property
    def type(self):
        r"""Gets the type of this CertItem.

        证书类型ROOT, SUBORDINATE。

        :return: The type of this CertItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CertItem.

        证书类型ROOT, SUBORDINATE。

        :param type: The type of this CertItem.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this CertItem.

        证书状态 DISABLE,ENABLE,EXPIRED,DELETE。

        :return: The status of this CertItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CertItem.

        证书状态 DISABLE,ENABLE,EXPIRED,DELETE。

        :param status: The status of this CertItem.
        :type status: str
        """
        self._status = status

    @property
    def key_algorithm(self):
        r"""Gets the key_algorithm of this CertItem.

        密钥生成算法 RSA-2048,RSA-3072。

        :return: The key_algorithm of this CertItem.
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        r"""Sets the key_algorithm of this CertItem.

        密钥生成算法 RSA-2048,RSA-3072。

        :param key_algorithm: The key_algorithm of this CertItem.
        :type key_algorithm: str
        """
        self._key_algorithm = key_algorithm

    @property
    def signature_algorithm(self):
        r"""Gets the signature_algorithm of this CertItem.

        签名哈希算法。

        :return: The signature_algorithm of this CertItem.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        r"""Sets the signature_algorithm of this CertItem.

        签名哈希算法。

        :param signature_algorithm: The signature_algorithm of this CertItem.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def apply(self):
        r"""Gets the apply of this CertItem.

        应用场景。

        :return: The apply of this CertItem.
        :rtype: str
        """
        return self._apply

    @apply.setter
    def apply(self, apply):
        r"""Sets the apply of this CertItem.

        应用场景。

        :param apply: The apply of this CertItem.
        :type apply: str
        """
        self._apply = apply

    @property
    def not_before(self):
        r"""Gets the not_before of this CertItem.

        生效时间。

        :return: The not_before of this CertItem.
        :rtype: str
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        r"""Sets the not_before of this CertItem.

        生效时间。

        :param not_before: The not_before of this CertItem.
        :type not_before: str
        """
        self._not_before = not_before

    @property
    def not_after(self):
        r"""Gets the not_after of this CertItem.

        过期时间。

        :return: The not_after of this CertItem.
        :rtype: str
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        r"""Sets the not_after of this CertItem.

        过期时间。

        :param not_after: The not_after of this CertItem.
        :type not_after: str
        """
        self._not_after = not_after

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CertItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
