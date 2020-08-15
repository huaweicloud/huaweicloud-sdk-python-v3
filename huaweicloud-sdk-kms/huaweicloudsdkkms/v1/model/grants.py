# coding: utf-8

import pprint
import re

import six





class Grants:


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
        'grant_id': 'str',
        'grantee_principal': 'str',
        'grantee_principal_type': 'str',
        'operations': 'list[str]',
        'issuing_principal': 'str',
        'creation_date': 'str',
        'name': 'str',
        'retiring_principal': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'grant_id': 'grant_id',
        'grantee_principal': 'grantee_principal',
        'grantee_principal_type': 'grantee_principal_type',
        'operations': 'operations',
        'issuing_principal': 'issuing_principal',
        'creation_date': 'creation_date',
        'name': 'name',
        'retiring_principal': 'retiring_principal'
    }

    def __init__(self, key_id=None, grant_id=None, grantee_principal=None, grantee_principal_type=None, operations=None, issuing_principal=None, creation_date=None, name=None, retiring_principal=None):
        """Grants - a model defined in huaweicloud sdk"""
        
        

        self._key_id = None
        self._grant_id = None
        self._grantee_principal = None
        self._grantee_principal_type = None
        self._operations = None
        self._issuing_principal = None
        self._creation_date = None
        self._name = None
        self._retiring_principal = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if grant_id is not None:
            self.grant_id = grant_id
        if grantee_principal is not None:
            self.grantee_principal = grantee_principal
        if grantee_principal_type is not None:
            self.grantee_principal_type = grantee_principal_type
        if operations is not None:
            self.operations = operations
        if issuing_principal is not None:
            self.issuing_principal = issuing_principal
        if creation_date is not None:
            self.creation_date = creation_date
        if name is not None:
            self.name = name
        if retiring_principal is not None:
            self.retiring_principal = retiring_principal

    @property
    def key_id(self):
        """Gets the key_id of this Grants.

        密钥ID。

        :return: The key_id of this Grants.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this Grants.

        密钥ID。

        :param key_id: The key_id of this Grants.
        :type: str
        """
        self._key_id = key_id

    @property
    def grant_id(self):
        """Gets the grant_id of this Grants.

        授权ID，64字节。

        :return: The grant_id of this Grants.
        :rtype: str
        """
        return self._grant_id

    @grant_id.setter
    def grant_id(self, grant_id):
        """Sets the grant_id of this Grants.

        授权ID，64字节。

        :param grant_id: The grant_id of this Grants.
        :type: str
        """
        self._grant_id = grant_id

    @property
    def grantee_principal(self):
        """Gets the grantee_principal of this Grants.

        被授权用户ID，1~64字节，满足正则匹配“^[a-zA-Z0-9]{1，64}$”。 例如：0d0466b00d0466b00d0466b00d0466b0

        :return: The grantee_principal of this Grants.
        :rtype: str
        """
        return self._grantee_principal

    @grantee_principal.setter
    def grantee_principal(self, grantee_principal):
        """Sets the grantee_principal of this Grants.

        被授权用户ID，1~64字节，满足正则匹配“^[a-zA-Z0-9]{1，64}$”。 例如：0d0466b00d0466b00d0466b00d0466b0

        :param grantee_principal: The grantee_principal of this Grants.
        :type: str
        """
        self._grantee_principal = grantee_principal

    @property
    def grantee_principal_type(self):
        """Gets the grantee_principal_type of this Grants.

        授权类型。 有效值：“user”，“domain”。

        :return: The grantee_principal_type of this Grants.
        :rtype: str
        """
        return self._grantee_principal_type

    @grantee_principal_type.setter
    def grantee_principal_type(self, grantee_principal_type):
        """Sets the grantee_principal_type of this Grants.

        授权类型。 有效值：“user”，“domain”。

        :param grantee_principal_type: The grantee_principal_type of this Grants.
        :type: str
        """
        self._grantee_principal_type = grantee_principal_type

    @property
    def operations(self):
        """Gets the operations of this Grants.

        授权允许的操作列表。 有效的值：“create-datakey”，“create-datakey-without-plaintext”，“encrypt-datakey”，“decrypt-datakey”，“describe-key”，“create-grant”，“retire-grant”，“encrypt-data”，“decrypt-data”。 有效值不能仅为“create-grant”。

        :return: The operations of this Grants.
        :rtype: list[str]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this Grants.

        授权允许的操作列表。 有效的值：“create-datakey”，“create-datakey-without-plaintext”，“encrypt-datakey”，“decrypt-datakey”，“describe-key”，“create-grant”，“retire-grant”，“encrypt-data”，“decrypt-data”。 有效值不能仅为“create-grant”。

        :param operations: The operations of this Grants.
        :type: list[str]
        """
        self._operations = operations

    @property
    def issuing_principal(self):
        """Gets the issuing_principal of this Grants.

        创建授权用户ID，1~64字节，满足正则匹配“^[a-zA-Z0-9]{1，64}$”。 例如：0d0466b00d0466b00d0466b00d0466b0

        :return: The issuing_principal of this Grants.
        :rtype: str
        """
        return self._issuing_principal

    @issuing_principal.setter
    def issuing_principal(self, issuing_principal):
        """Sets the issuing_principal of this Grants.

        创建授权用户ID，1~64字节，满足正则匹配“^[a-zA-Z0-9]{1，64}$”。 例如：0d0466b00d0466b00d0466b00d0466b0

        :param issuing_principal: The issuing_principal of this Grants.
        :type: str
        """
        self._issuing_principal = issuing_principal

    @property
    def creation_date(self):
        """Gets the creation_date of this Grants.

        创建时间，时间戳，即从1970年1月1日至该时间的总秒数。 例如：1497341531000

        :return: The creation_date of this Grants.
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Grants.

        创建时间，时间戳，即从1970年1月1日至该时间的总秒数。 例如：1497341531000

        :param creation_date: The creation_date of this Grants.
        :type: str
        """
        self._creation_date = creation_date

    @property
    def name(self):
        """Gets the name of this Grants.

        授权名字，取值1到255字符，满足正则匹配“^[a-zA-Z0-9:/_-]{1,255}$”。

        :return: The name of this Grants.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Grants.

        授权名字，取值1到255字符，满足正则匹配“^[a-zA-Z0-9:/_-]{1,255}$”。

        :param name: The name of this Grants.
        :type: str
        """
        self._name = name

    @property
    def retiring_principal(self):
        """Gets the retiring_principal of this Grants.

        可退役授权的用户ID，1~64字节，满足正则匹配“^[a-zA-Z0-9]{1，64}$”。 例如：0d0466b00d0466b00d0466b00d0466b0

        :return: The retiring_principal of this Grants.
        :rtype: str
        """
        return self._retiring_principal

    @retiring_principal.setter
    def retiring_principal(self, retiring_principal):
        """Sets the retiring_principal of this Grants.

        可退役授权的用户ID，1~64字节，满足正则匹配“^[a-zA-Z0-9]{1，64}$”。 例如：0d0466b00d0466b00d0466b00d0466b0

        :param retiring_principal: The retiring_principal of this Grants.
        :type: str
        """
        self._retiring_principal = retiring_principal

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
        if not isinstance(other, Grants):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
