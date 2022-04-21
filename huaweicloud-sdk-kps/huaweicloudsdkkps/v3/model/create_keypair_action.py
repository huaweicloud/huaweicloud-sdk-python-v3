# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateKeypairAction:

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
        'type': 'str',
        'public_key': 'str',
        'scope': 'str',
        'user_id': 'str',
        'key_protection': 'KeyProtection'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'public_key': 'public_key',
        'scope': 'scope',
        'user_id': 'user_id',
        'key_protection': 'key_protection'
    }

    def __init__(self, name=None, type=None, public_key=None, scope=None, user_id=None, key_protection=None):
        """CreateKeypairAction

        The model defined in huaweicloud sdk

        :param name: SSH密钥对的名称。 - 新创建的密钥对名称不能和已有密钥对的名称相同。 - SSH密钥对名称由英文字母、数字、下划线、中划线组成，长度不能超过64个字节
        :type name: str
        :param type: SSH密钥对的类型
        :type type: str
        :param public_key: 导入公钥的字符串信息。
        :type public_key: str
        :param scope: 租户级或者用户级
        :type scope: str
        :param user_id: SSH密钥对所属的用户信息
        :type user_id: str
        :param key_protection: 
        :type key_protection: :class:`huaweicloudsdkkps.v3.KeyProtection`
        """
        
        

        self._name = None
        self._type = None
        self._public_key = None
        self._scope = None
        self._user_id = None
        self._key_protection = None
        self.discriminator = None

        self.name = name
        if type is not None:
            self.type = type
        if public_key is not None:
            self.public_key = public_key
        if scope is not None:
            self.scope = scope
        if user_id is not None:
            self.user_id = user_id
        if key_protection is not None:
            self.key_protection = key_protection

    @property
    def name(self):
        """Gets the name of this CreateKeypairAction.

        SSH密钥对的名称。 - 新创建的密钥对名称不能和已有密钥对的名称相同。 - SSH密钥对名称由英文字母、数字、下划线、中划线组成，长度不能超过64个字节

        :return: The name of this CreateKeypairAction.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateKeypairAction.

        SSH密钥对的名称。 - 新创建的密钥对名称不能和已有密钥对的名称相同。 - SSH密钥对名称由英文字母、数字、下划线、中划线组成，长度不能超过64个字节

        :param name: The name of this CreateKeypairAction.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CreateKeypairAction.

        SSH密钥对的类型

        :return: The type of this CreateKeypairAction.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateKeypairAction.

        SSH密钥对的类型

        :param type: The type of this CreateKeypairAction.
        :type type: str
        """
        self._type = type

    @property
    def public_key(self):
        """Gets the public_key of this CreateKeypairAction.

        导入公钥的字符串信息。

        :return: The public_key of this CreateKeypairAction.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this CreateKeypairAction.

        导入公钥的字符串信息。

        :param public_key: The public_key of this CreateKeypairAction.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def scope(self):
        """Gets the scope of this CreateKeypairAction.

        租户级或者用户级

        :return: The scope of this CreateKeypairAction.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this CreateKeypairAction.

        租户级或者用户级

        :param scope: The scope of this CreateKeypairAction.
        :type scope: str
        """
        self._scope = scope

    @property
    def user_id(self):
        """Gets the user_id of this CreateKeypairAction.

        SSH密钥对所属的用户信息

        :return: The user_id of this CreateKeypairAction.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CreateKeypairAction.

        SSH密钥对所属的用户信息

        :param user_id: The user_id of this CreateKeypairAction.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def key_protection(self):
        """Gets the key_protection of this CreateKeypairAction.


        :return: The key_protection of this CreateKeypairAction.
        :rtype: :class:`huaweicloudsdkkps.v3.KeyProtection`
        """
        return self._key_protection

    @key_protection.setter
    def key_protection(self, key_protection):
        """Sets the key_protection of this CreateKeypairAction.


        :param key_protection: The key_protection of this CreateKeypairAction.
        :type key_protection: :class:`huaweicloudsdkkps.v3.KeyProtection`
        """
        self._key_protection = key_protection

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
        if not isinstance(other, CreateKeypairAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
