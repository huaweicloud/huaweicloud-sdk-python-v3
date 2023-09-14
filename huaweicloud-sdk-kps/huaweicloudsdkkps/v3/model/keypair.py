# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Keypair:

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
        'scope': 'str',
        'public_key': 'str',
        'fingerprint': 'str',
        'is_key_protection': 'bool',
        'frozen_state': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'scope': 'scope',
        'public_key': 'public_key',
        'fingerprint': 'fingerprint',
        'is_key_protection': 'is_key_protection',
        'frozen_state': 'frozen_state'
    }

    def __init__(self, name=None, type=None, scope=None, public_key=None, fingerprint=None, is_key_protection=None, frozen_state=None):
        """Keypair

        The model defined in huaweicloud sdk

        :param name: SSH密钥对的名称
        :type name: str
        :param type: SSH密钥对的类型，值为“ssh”或“x509”
        :type type: str
        :param scope: 租户级或者用户级。domain或user。
        :type scope: str
        :param public_key: SSH密钥对对应的publicKey信息
        :type public_key: str
        :param fingerprint: SSH密钥对应指纹信息
        :type fingerprint: str
        :param is_key_protection: 是否托管密钥
        :type is_key_protection: bool
        :param frozen_state: 冻结状态 - 0：正常状态 - 1：普通冻结 - 2：公安冻结 - 3：普通冻结及公安冻结 - 4：违规冻结 - 5：普通冻结及违规冻结 - 6：公安冻结及违规冻结 - 7：普通冻结、公安冻结及违规冻结 - 8：未实名认证冻结 - 9：普通冻结及未实名认证冻结 - 10：公安冻结及未实名认证冻结
        :type frozen_state: str
        """
        
        

        self._name = None
        self._type = None
        self._scope = None
        self._public_key = None
        self._fingerprint = None
        self._is_key_protection = None
        self._frozen_state = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if scope is not None:
            self.scope = scope
        if public_key is not None:
            self.public_key = public_key
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if is_key_protection is not None:
            self.is_key_protection = is_key_protection
        if frozen_state is not None:
            self.frozen_state = frozen_state

    @property
    def name(self):
        """Gets the name of this Keypair.

        SSH密钥对的名称

        :return: The name of this Keypair.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Keypair.

        SSH密钥对的名称

        :param name: The name of this Keypair.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this Keypair.

        SSH密钥对的类型，值为“ssh”或“x509”

        :return: The type of this Keypair.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Keypair.

        SSH密钥对的类型，值为“ssh”或“x509”

        :param type: The type of this Keypair.
        :type type: str
        """
        self._type = type

    @property
    def scope(self):
        """Gets the scope of this Keypair.

        租户级或者用户级。domain或user。

        :return: The scope of this Keypair.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Keypair.

        租户级或者用户级。domain或user。

        :param scope: The scope of this Keypair.
        :type scope: str
        """
        self._scope = scope

    @property
    def public_key(self):
        """Gets the public_key of this Keypair.

        SSH密钥对对应的publicKey信息

        :return: The public_key of this Keypair.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this Keypair.

        SSH密钥对对应的publicKey信息

        :param public_key: The public_key of this Keypair.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def fingerprint(self):
        """Gets the fingerprint of this Keypair.

        SSH密钥对应指纹信息

        :return: The fingerprint of this Keypair.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this Keypair.

        SSH密钥对应指纹信息

        :param fingerprint: The fingerprint of this Keypair.
        :type fingerprint: str
        """
        self._fingerprint = fingerprint

    @property
    def is_key_protection(self):
        """Gets the is_key_protection of this Keypair.

        是否托管密钥

        :return: The is_key_protection of this Keypair.
        :rtype: bool
        """
        return self._is_key_protection

    @is_key_protection.setter
    def is_key_protection(self, is_key_protection):
        """Sets the is_key_protection of this Keypair.

        是否托管密钥

        :param is_key_protection: The is_key_protection of this Keypair.
        :type is_key_protection: bool
        """
        self._is_key_protection = is_key_protection

    @property
    def frozen_state(self):
        """Gets the frozen_state of this Keypair.

        冻结状态 - 0：正常状态 - 1：普通冻结 - 2：公安冻结 - 3：普通冻结及公安冻结 - 4：违规冻结 - 5：普通冻结及违规冻结 - 6：公安冻结及违规冻结 - 7：普通冻结、公安冻结及违规冻结 - 8：未实名认证冻结 - 9：普通冻结及未实名认证冻结 - 10：公安冻结及未实名认证冻结

        :return: The frozen_state of this Keypair.
        :rtype: str
        """
        return self._frozen_state

    @frozen_state.setter
    def frozen_state(self, frozen_state):
        """Sets the frozen_state of this Keypair.

        冻结状态 - 0：正常状态 - 1：普通冻结 - 2：公安冻结 - 3：普通冻结及公安冻结 - 4：违规冻结 - 5：普通冻结及违规冻结 - 6：公安冻结及违规冻结 - 7：普通冻结、公安冻结及违规冻结 - 8：未实名认证冻结 - 9：普通冻结及未实名认证冻结 - 10：公安冻结及未实名认证冻结

        :param frozen_state: The frozen_state of this Keypair.
        :type frozen_state: str
        """
        self._frozen_state = frozen_state

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
        if not isinstance(other, Keypair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
