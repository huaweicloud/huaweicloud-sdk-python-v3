# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecretRequestBody:

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
        'kms_key_id': 'str',
        'description': 'str',
        'secret_binary': 'str',
        'secret_string': 'str'
    }

    attribute_map = {
        'name': 'name',
        'kms_key_id': 'kms_key_id',
        'description': 'description',
        'secret_binary': 'secret_binary',
        'secret_string': 'secret_string'
    }

    def __init__(self, name=None, kms_key_id=None, description=None, secret_binary=None, secret_string=None):
        """CreateSecretRequestBody

        The model defined in huaweicloud sdk

        :param name: 凭据名称。  约束：取值范围为1到64个字符，满足正则匹配“^[a-zA-Z0-9._-]{1,64}$”。 
        :type name: str
        :param kms_key_id: 用于加密保护凭据值的KMS主密钥ID，如果您未指定此参数，凭据管理服务将默认使用名为csms/default的默认主密钥，用于加密您账号在本项目中创建的凭据值。如果用户账号下不存在该名称的主密钥，则凭据管理服务自动为您创建该名称的密钥。
        :type kms_key_id: str
        :param description: 凭据的描述信息。  约束：2048字节。 
        :type description: str
        :param secret_binary: 二进制类型凭据在base64编码后的明文，凭据管理服务将其加密后，存入凭据的初始版本中。  类型：base64编码的二进制数据对象。  约束：secret_binary和secret_string必须且只能设置一个，最大32K。 
        :type secret_binary: str
        :param secret_string: 文本类型凭据的明文，凭据管理服务将其加密后，存入凭据的初始版本中。  约束：secret_binary和secret_string必须且只能设置一个，最大32K。 
        :type secret_string: str
        """
        
        

        self._name = None
        self._kms_key_id = None
        self._description = None
        self._secret_binary = None
        self._secret_string = None
        self.discriminator = None

        self.name = name
        if kms_key_id is not None:
            self.kms_key_id = kms_key_id
        if description is not None:
            self.description = description
        if secret_binary is not None:
            self.secret_binary = secret_binary
        if secret_string is not None:
            self.secret_string = secret_string

    @property
    def name(self):
        """Gets the name of this CreateSecretRequestBody.

        凭据名称。  约束：取值范围为1到64个字符，满足正则匹配“^[a-zA-Z0-9._-]{1,64}$”。 

        :return: The name of this CreateSecretRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSecretRequestBody.

        凭据名称。  约束：取值范围为1到64个字符，满足正则匹配“^[a-zA-Z0-9._-]{1,64}$”。 

        :param name: The name of this CreateSecretRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def kms_key_id(self):
        """Gets the kms_key_id of this CreateSecretRequestBody.

        用于加密保护凭据值的KMS主密钥ID，如果您未指定此参数，凭据管理服务将默认使用名为csms/default的默认主密钥，用于加密您账号在本项目中创建的凭据值。如果用户账号下不存在该名称的主密钥，则凭据管理服务自动为您创建该名称的密钥。

        :return: The kms_key_id of this CreateSecretRequestBody.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """Sets the kms_key_id of this CreateSecretRequestBody.

        用于加密保护凭据值的KMS主密钥ID，如果您未指定此参数，凭据管理服务将默认使用名为csms/default的默认主密钥，用于加密您账号在本项目中创建的凭据值。如果用户账号下不存在该名称的主密钥，则凭据管理服务自动为您创建该名称的密钥。

        :param kms_key_id: The kms_key_id of this CreateSecretRequestBody.
        :type kms_key_id: str
        """
        self._kms_key_id = kms_key_id

    @property
    def description(self):
        """Gets the description of this CreateSecretRequestBody.

        凭据的描述信息。  约束：2048字节。 

        :return: The description of this CreateSecretRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSecretRequestBody.

        凭据的描述信息。  约束：2048字节。 

        :param description: The description of this CreateSecretRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def secret_binary(self):
        """Gets the secret_binary of this CreateSecretRequestBody.

        二进制类型凭据在base64编码后的明文，凭据管理服务将其加密后，存入凭据的初始版本中。  类型：base64编码的二进制数据对象。  约束：secret_binary和secret_string必须且只能设置一个，最大32K。 

        :return: The secret_binary of this CreateSecretRequestBody.
        :rtype: str
        """
        return self._secret_binary

    @secret_binary.setter
    def secret_binary(self, secret_binary):
        """Sets the secret_binary of this CreateSecretRequestBody.

        二进制类型凭据在base64编码后的明文，凭据管理服务将其加密后，存入凭据的初始版本中。  类型：base64编码的二进制数据对象。  约束：secret_binary和secret_string必须且只能设置一个，最大32K。 

        :param secret_binary: The secret_binary of this CreateSecretRequestBody.
        :type secret_binary: str
        """
        self._secret_binary = secret_binary

    @property
    def secret_string(self):
        """Gets the secret_string of this CreateSecretRequestBody.

        文本类型凭据的明文，凭据管理服务将其加密后，存入凭据的初始版本中。  约束：secret_binary和secret_string必须且只能设置一个，最大32K。 

        :return: The secret_string of this CreateSecretRequestBody.
        :rtype: str
        """
        return self._secret_string

    @secret_string.setter
    def secret_string(self, secret_string):
        """Sets the secret_string of this CreateSecretRequestBody.

        文本类型凭据的明文，凭据管理服务将其加密后，存入凭据的初始版本中。  约束：secret_binary和secret_string必须且只能设置一个，最大32K。 

        :param secret_string: The secret_string of this CreateSecretRequestBody.
        :type secret_string: str
        """
        self._secret_string = secret_string

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
        if not isinstance(other, CreateSecretRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
