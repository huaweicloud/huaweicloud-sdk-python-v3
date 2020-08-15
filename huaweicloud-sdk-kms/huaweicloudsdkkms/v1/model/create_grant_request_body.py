# coding: utf-8

import pprint
import re

import six





class CreateGrantRequestBody:


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
        'grantee_principal': 'str',
        'operations': 'list[str]',
        'name': 'str',
        'retiring_principal': 'str',
        'grantee_principal_type': 'str',
        'sequence': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'grantee_principal': 'grantee_principal',
        'operations': 'operations',
        'name': 'name',
        'retiring_principal': 'retiring_principal',
        'grantee_principal_type': 'grantee_principal_type',
        'sequence': 'sequence'
    }

    def __init__(self, key_id=None, grantee_principal=None, operations=None, name=None, retiring_principal=None, grantee_principal_type=None, sequence=None):
        """CreateGrantRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._key_id = None
        self._grantee_principal = None
        self._operations = None
        self._name = None
        self._retiring_principal = None
        self._grantee_principal_type = None
        self._sequence = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if grantee_principal is not None:
            self.grantee_principal = grantee_principal
        if operations is not None:
            self.operations = operations
        if name is not None:
            self.name = name
        if retiring_principal is not None:
            self.retiring_principal = retiring_principal
        if grantee_principal_type is not None:
            self.grantee_principal_type = grantee_principal_type
        if sequence is not None:
            self.sequence = sequence

    @property
    def key_id(self):
        """Gets the key_id of this CreateGrantRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :return: The key_id of this CreateGrantRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this CreateGrantRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :param key_id: The key_id of this CreateGrantRequestBody.
        :type: str
        """
        self._key_id = key_id

    @property
    def grantee_principal(self):
        """Gets the grantee_principal of this CreateGrantRequestBody.

        被授权用户ID，1~64字节，满足正则匹配“^[a-zA-Z0-9]{1，64}$”。 例如：0d0466b00d0466b00d0466b00d0466b0

        :return: The grantee_principal of this CreateGrantRequestBody.
        :rtype: str
        """
        return self._grantee_principal

    @grantee_principal.setter
    def grantee_principal(self, grantee_principal):
        """Sets the grantee_principal of this CreateGrantRequestBody.

        被授权用户ID，1~64字节，满足正则匹配“^[a-zA-Z0-9]{1，64}$”。 例如：0d0466b00d0466b00d0466b00d0466b0

        :param grantee_principal: The grantee_principal of this CreateGrantRequestBody.
        :type: str
        """
        self._grantee_principal = grantee_principal

    @property
    def operations(self):
        """Gets the operations of this CreateGrantRequestBody.

        授权允许的操作列表。 有效的值：“create-datakey”，“create-datakey-without-plaintext”，“encrypt-datakey”，“decrypt-datakey”，“describe-key”，“create-grant”，“retire-grant”，“encrypt-data”，“decrypt-data”。 有效值不能仅为“create-grant”。

        :return: The operations of this CreateGrantRequestBody.
        :rtype: list[str]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this CreateGrantRequestBody.

        授权允许的操作列表。 有效的值：“create-datakey”，“create-datakey-without-plaintext”，“encrypt-datakey”，“decrypt-datakey”，“describe-key”，“create-grant”，“retire-grant”，“encrypt-data”，“decrypt-data”。 有效值不能仅为“create-grant”。

        :param operations: The operations of this CreateGrantRequestBody.
        :type: list[str]
        """
        self._operations = operations

    @property
    def name(self):
        """Gets the name of this CreateGrantRequestBody.

        授权名称，取值1到255字符，满足正则匹配“^[a-zA-Z0-9:/_-]{1,255}$”。

        :return: The name of this CreateGrantRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateGrantRequestBody.

        授权名称，取值1到255字符，满足正则匹配“^[a-zA-Z0-9:/_-]{1,255}$”。

        :param name: The name of this CreateGrantRequestBody.
        :type: str
        """
        self._name = name

    @property
    def retiring_principal(self):
        """Gets the retiring_principal of this CreateGrantRequestBody.

        可退役授权的用户ID，1~64字节，满足正则匹配“^[a-zA-Z0-9]{1，64}$”。 例如：0d0466b00d0466b00d0466b00d0466b0

        :return: The retiring_principal of this CreateGrantRequestBody.
        :rtype: str
        """
        return self._retiring_principal

    @retiring_principal.setter
    def retiring_principal(self, retiring_principal):
        """Sets the retiring_principal of this CreateGrantRequestBody.

        可退役授权的用户ID，1~64字节，满足正则匹配“^[a-zA-Z0-9]{1，64}$”。 例如：0d0466b00d0466b00d0466b00d0466b0

        :param retiring_principal: The retiring_principal of this CreateGrantRequestBody.
        :type: str
        """
        self._retiring_principal = retiring_principal

    @property
    def grantee_principal_type(self):
        """Gets the grantee_principal_type of this CreateGrantRequestBody.

        授权类型。有效值：“user”，“domain”。默认值为“user”。

        :return: The grantee_principal_type of this CreateGrantRequestBody.
        :rtype: str
        """
        return self._grantee_principal_type

    @grantee_principal_type.setter
    def grantee_principal_type(self, grantee_principal_type):
        """Sets the grantee_principal_type of this CreateGrantRequestBody.

        授权类型。有效值：“user”，“domain”。默认值为“user”。

        :param grantee_principal_type: The grantee_principal_type of this CreateGrantRequestBody.
        :type: str
        """
        self._grantee_principal_type = grantee_principal_type

    @property
    def sequence(self):
        """Gets the sequence of this CreateGrantRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :return: The sequence of this CreateGrantRequestBody.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this CreateGrantRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :param sequence: The sequence of this CreateGrantRequestBody.
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
        if not isinstance(other, CreateGrantRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
