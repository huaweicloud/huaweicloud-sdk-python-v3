# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateKeyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'key_alias': 'str',
        'key_spec': 'str',
        'key_usage': 'str',
        'key_description': 'str',
        'origin': 'str',
        'enterprise_project_id': 'str',
        'sequence': 'str',
        'keystore_id': 'str'
    }

    attribute_map = {
        'key_alias': 'key_alias',
        'key_spec': 'key_spec',
        'key_usage': 'key_usage',
        'key_description': 'key_description',
        'origin': 'origin',
        'enterprise_project_id': 'enterprise_project_id',
        'sequence': 'sequence',
        'keystore_id': 'keystore_id'
    }

    def __init__(self, key_alias=None, key_spec=None, key_usage=None, key_description=None, origin=None, enterprise_project_id=None, sequence=None, keystore_id=None):
        """CreateKeyRequestBody

        The model defined in huaweicloud sdk

        :param key_alias: 非默认主密钥别名，取值范围为1到255个字符，满足正则匹配“^[a-zA-Z0-9:/_-]{1,255}$”，且不与系统服务创建的默认主密钥别名重名。
        :type key_alias: str
        :param key_spec: 密钥生成算法，默认为“AES_256”，枚举如下： - AES_256 - SM4 - RSA_2048 - RSA_3072 - RSA_4096 - EC_P256 - EC_P384 - SM2
        :type key_spec: str
        :param key_usage: 密钥用途，对称密钥默认为“ENCRYPT_DECRYPT”，非对称密钥默认为“SIGN_VERIFY”，枚举如下： - ENCRYPT_DECRYPT - SIGN_VERIFY
        :type key_usage: str
        :param key_description: 密钥描述，取值0到255字符。
        :type key_description: str
        :param origin: 密钥来源，默认为“kms”，枚举如下： - kms：表示密钥材料由kms生成。 - external：表示密钥材料由外部导入。
        :type origin: str
        :param enterprise_project_id: 企业多项目ID。 - 用户未开通企业多项目时，不需要输入该字段。 - 用户开通企业多项目时，创建资源可以输入该字段。若用户户不输入该字段，默认创建属于默认企业多项目ID（ID为“0”）的资源。 注意：若用户没有默认企业多项目ID（ID为“0”）下的创建权限，则接口报错。
        :type enterprise_project_id: str
        :param sequence: 请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff
        :type sequence: str
        :param keystore_id: 密钥库ID，默认使用KMS默认密钥库
        :type keystore_id: str
        """
        
        

        self._key_alias = None
        self._key_spec = None
        self._key_usage = None
        self._key_description = None
        self._origin = None
        self._enterprise_project_id = None
        self._sequence = None
        self._keystore_id = None
        self.discriminator = None

        if key_alias is not None:
            self.key_alias = key_alias
        if key_spec is not None:
            self.key_spec = key_spec
        if key_usage is not None:
            self.key_usage = key_usage
        if key_description is not None:
            self.key_description = key_description
        if origin is not None:
            self.origin = origin
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if sequence is not None:
            self.sequence = sequence
        if keystore_id is not None:
            self.keystore_id = keystore_id

    @property
    def key_alias(self):
        """Gets the key_alias of this CreateKeyRequestBody.

        非默认主密钥别名，取值范围为1到255个字符，满足正则匹配“^[a-zA-Z0-9:/_-]{1,255}$”，且不与系统服务创建的默认主密钥别名重名。

        :return: The key_alias of this CreateKeyRequestBody.
        :rtype: str
        """
        return self._key_alias

    @key_alias.setter
    def key_alias(self, key_alias):
        """Sets the key_alias of this CreateKeyRequestBody.

        非默认主密钥别名，取值范围为1到255个字符，满足正则匹配“^[a-zA-Z0-9:/_-]{1,255}$”，且不与系统服务创建的默认主密钥别名重名。

        :param key_alias: The key_alias of this CreateKeyRequestBody.
        :type key_alias: str
        """
        self._key_alias = key_alias

    @property
    def key_spec(self):
        """Gets the key_spec of this CreateKeyRequestBody.

        密钥生成算法，默认为“AES_256”，枚举如下： - AES_256 - SM4 - RSA_2048 - RSA_3072 - RSA_4096 - EC_P256 - EC_P384 - SM2

        :return: The key_spec of this CreateKeyRequestBody.
        :rtype: str
        """
        return self._key_spec

    @key_spec.setter
    def key_spec(self, key_spec):
        """Sets the key_spec of this CreateKeyRequestBody.

        密钥生成算法，默认为“AES_256”，枚举如下： - AES_256 - SM4 - RSA_2048 - RSA_3072 - RSA_4096 - EC_P256 - EC_P384 - SM2

        :param key_spec: The key_spec of this CreateKeyRequestBody.
        :type key_spec: str
        """
        self._key_spec = key_spec

    @property
    def key_usage(self):
        """Gets the key_usage of this CreateKeyRequestBody.

        密钥用途，对称密钥默认为“ENCRYPT_DECRYPT”，非对称密钥默认为“SIGN_VERIFY”，枚举如下： - ENCRYPT_DECRYPT - SIGN_VERIFY

        :return: The key_usage of this CreateKeyRequestBody.
        :rtype: str
        """
        return self._key_usage

    @key_usage.setter
    def key_usage(self, key_usage):
        """Sets the key_usage of this CreateKeyRequestBody.

        密钥用途，对称密钥默认为“ENCRYPT_DECRYPT”，非对称密钥默认为“SIGN_VERIFY”，枚举如下： - ENCRYPT_DECRYPT - SIGN_VERIFY

        :param key_usage: The key_usage of this CreateKeyRequestBody.
        :type key_usage: str
        """
        self._key_usage = key_usage

    @property
    def key_description(self):
        """Gets the key_description of this CreateKeyRequestBody.

        密钥描述，取值0到255字符。

        :return: The key_description of this CreateKeyRequestBody.
        :rtype: str
        """
        return self._key_description

    @key_description.setter
    def key_description(self, key_description):
        """Sets the key_description of this CreateKeyRequestBody.

        密钥描述，取值0到255字符。

        :param key_description: The key_description of this CreateKeyRequestBody.
        :type key_description: str
        """
        self._key_description = key_description

    @property
    def origin(self):
        """Gets the origin of this CreateKeyRequestBody.

        密钥来源，默认为“kms”，枚举如下： - kms：表示密钥材料由kms生成。 - external：表示密钥材料由外部导入。

        :return: The origin of this CreateKeyRequestBody.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this CreateKeyRequestBody.

        密钥来源，默认为“kms”，枚举如下： - kms：表示密钥材料由kms生成。 - external：表示密钥材料由外部导入。

        :param origin: The origin of this CreateKeyRequestBody.
        :type origin: str
        """
        self._origin = origin

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateKeyRequestBody.

        企业多项目ID。 - 用户未开通企业多项目时，不需要输入该字段。 - 用户开通企业多项目时，创建资源可以输入该字段。若用户户不输入该字段，默认创建属于默认企业多项目ID（ID为“0”）的资源。 注意：若用户没有默认企业多项目ID（ID为“0”）下的创建权限，则接口报错。

        :return: The enterprise_project_id of this CreateKeyRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateKeyRequestBody.

        企业多项目ID。 - 用户未开通企业多项目时，不需要输入该字段。 - 用户开通企业多项目时，创建资源可以输入该字段。若用户户不输入该字段，默认创建属于默认企业多项目ID（ID为“0”）的资源。 注意：若用户没有默认企业多项目ID（ID为“0”）下的创建权限，则接口报错。

        :param enterprise_project_id: The enterprise_project_id of this CreateKeyRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def sequence(self):
        """Gets the sequence of this CreateKeyRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :return: The sequence of this CreateKeyRequestBody.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this CreateKeyRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :param sequence: The sequence of this CreateKeyRequestBody.
        :type sequence: str
        """
        self._sequence = sequence

    @property
    def keystore_id(self):
        """Gets the keystore_id of this CreateKeyRequestBody.

        密钥库ID，默认使用KMS默认密钥库

        :return: The keystore_id of this CreateKeyRequestBody.
        :rtype: str
        """
        return self._keystore_id

    @keystore_id.setter
    def keystore_id(self, keystore_id):
        """Sets the keystore_id of this CreateKeyRequestBody.

        密钥库ID，默认使用KMS默认密钥库

        :param keystore_id: The keystore_id of this CreateKeyRequestBody.
        :type keystore_id: str
        """
        self._keystore_id = keystore_id

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
        if not isinstance(other, CreateKeyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
