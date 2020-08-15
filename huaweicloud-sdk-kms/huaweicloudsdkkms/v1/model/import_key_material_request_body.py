# coding: utf-8

import pprint
import re

import six





class ImportKeyMaterialRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'import_token': 'str',
        'encrypted_key_material': 'str',
        'expiration_time': 'int',
        'sequence': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'import_token': 'import_token',
        'encrypted_key_material': 'encrypted_key_material',
        'expiration_time': 'expiration_time',
        'sequence': 'sequence'
    }

    def __init__(self, key_id=None, import_token=None, encrypted_key_material=None, expiration_time=None, sequence=None):
        """ImportKeyMaterialRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._key_id = None
        self._import_token = None
        self._encrypted_key_material = None
        self._expiration_time = None
        self._sequence = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if import_token is not None:
            self.import_token = import_token
        if encrypted_key_material is not None:
            self.encrypted_key_material = encrypted_key_material
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if sequence is not None:
            self.sequence = sequence

    @property
    def key_id(self):
        """Gets the key_id of this ImportKeyMaterialRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :return: The key_id of this ImportKeyMaterialRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this ImportKeyMaterialRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :param key_id: The key_id of this ImportKeyMaterialRequestBody.
        :type: str
        """
        self._key_id = key_id

    @property
    def import_token(self):
        """Gets the import_token of this ImportKeyMaterialRequestBody.

        密钥导入令牌，base64格式，满足正则匹配“^[0-9a-zA-Z+/=]{200,6144}$”。

        :return: The import_token of this ImportKeyMaterialRequestBody.
        :rtype: str
        """
        return self._import_token

    @import_token.setter
    def import_token(self, import_token):
        """Sets the import_token of this ImportKeyMaterialRequestBody.

        密钥导入令牌，base64格式，满足正则匹配“^[0-9a-zA-Z+/=]{200,6144}$”。

        :param import_token: The import_token of this ImportKeyMaterialRequestBody.
        :type: str
        """
        self._import_token = import_token

    @property
    def encrypted_key_material(self):
        """Gets the encrypted_key_material of this ImportKeyMaterialRequestBody.

        加密后的密钥材料，base64格式，满足正则匹配“^[0-9a-zA-Z+/=]{344,360}$”。

        :return: The encrypted_key_material of this ImportKeyMaterialRequestBody.
        :rtype: str
        """
        return self._encrypted_key_material

    @encrypted_key_material.setter
    def encrypted_key_material(self, encrypted_key_material):
        """Sets the encrypted_key_material of this ImportKeyMaterialRequestBody.

        加密后的密钥材料，base64格式，满足正则匹配“^[0-9a-zA-Z+/=]{344,360}$”。

        :param encrypted_key_material: The encrypted_key_material of this ImportKeyMaterialRequestBody.
        :type: str
        """
        self._encrypted_key_material = encrypted_key_material

    @property
    def expiration_time(self):
        """Gets the expiration_time of this ImportKeyMaterialRequestBody.

        密钥材料到期时间，时间戳，即从1970年1月1日至该时间的总秒数，KMS会在该时间的24小时内删除密钥材料。 例如：1550291833

        :return: The expiration_time of this ImportKeyMaterialRequestBody.
        :rtype: int
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this ImportKeyMaterialRequestBody.

        密钥材料到期时间，时间戳，即从1970年1月1日至该时间的总秒数，KMS会在该时间的24小时内删除密钥材料。 例如：1550291833

        :param expiration_time: The expiration_time of this ImportKeyMaterialRequestBody.
        :type: int
        """
        self._expiration_time = expiration_time

    @property
    def sequence(self):
        """Gets the sequence of this ImportKeyMaterialRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :return: The sequence of this ImportKeyMaterialRequestBody.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this ImportKeyMaterialRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :param sequence: The sequence of this ImportKeyMaterialRequestBody.
        :type: str
        """
        self._sequence = sequence

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImportKeyMaterialRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
