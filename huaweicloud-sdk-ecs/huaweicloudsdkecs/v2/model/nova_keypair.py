# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaKeypair:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fingerprint': 'str',
        'name': 'str',
        'public_key': 'str',
        'private_key': 'str',
        'user_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'fingerprint': 'fingerprint',
        'name': 'name',
        'public_key': 'public_key',
        'private_key': 'private_key',
        'user_id': 'user_id',
        'type': 'type'
    }

    def __init__(self, fingerprint=None, name=None, public_key=None, private_key=None, user_id=None, type=None):
        """NovaKeypair

        The model defined in huaweicloud sdk

        :param fingerprint: 密钥对应指纹信息。
        :type fingerprint: str
        :param name: 密钥名称。
        :type name: str
        :param public_key: 密钥对应publicKey信息。
        :type public_key: str
        :param private_key: 密钥对应privateKey信息。  - 创建SSH密钥时，响应中包括private_key的信息。 - 导入SSH密钥时，响应中不包括private_key的信息。
        :type private_key: str
        :param user_id: 密钥所属用户ID。
        :type user_id: str
        :param type: 密钥类型，默认“ssh”  微版本2.2以上支持
        :type type: str
        """
        
        

        self._fingerprint = None
        self._name = None
        self._public_key = None
        self._private_key = None
        self._user_id = None
        self._type = None
        self.discriminator = None

        self.fingerprint = fingerprint
        self.name = name
        self.public_key = public_key
        self.private_key = private_key
        self.user_id = user_id
        if type is not None:
            self.type = type

    @property
    def fingerprint(self):
        """Gets the fingerprint of this NovaKeypair.

        密钥对应指纹信息。

        :return: The fingerprint of this NovaKeypair.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this NovaKeypair.

        密钥对应指纹信息。

        :param fingerprint: The fingerprint of this NovaKeypair.
        :type fingerprint: str
        """
        self._fingerprint = fingerprint

    @property
    def name(self):
        """Gets the name of this NovaKeypair.

        密钥名称。

        :return: The name of this NovaKeypair.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NovaKeypair.

        密钥名称。

        :param name: The name of this NovaKeypair.
        :type name: str
        """
        self._name = name

    @property
    def public_key(self):
        """Gets the public_key of this NovaKeypair.

        密钥对应publicKey信息。

        :return: The public_key of this NovaKeypair.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this NovaKeypair.

        密钥对应publicKey信息。

        :param public_key: The public_key of this NovaKeypair.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def private_key(self):
        """Gets the private_key of this NovaKeypair.

        密钥对应privateKey信息。  - 创建SSH密钥时，响应中包括private_key的信息。 - 导入SSH密钥时，响应中不包括private_key的信息。

        :return: The private_key of this NovaKeypair.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this NovaKeypair.

        密钥对应privateKey信息。  - 创建SSH密钥时，响应中包括private_key的信息。 - 导入SSH密钥时，响应中不包括private_key的信息。

        :param private_key: The private_key of this NovaKeypair.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def user_id(self):
        """Gets the user_id of this NovaKeypair.

        密钥所属用户ID。

        :return: The user_id of this NovaKeypair.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this NovaKeypair.

        密钥所属用户ID。

        :param user_id: The user_id of this NovaKeypair.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def type(self):
        """Gets the type of this NovaKeypair.

        密钥类型，默认“ssh”  微版本2.2以上支持

        :return: The type of this NovaKeypair.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NovaKeypair.

        密钥类型，默认“ssh”  微版本2.2以上支持

        :param type: The type of this NovaKeypair.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, NovaKeypair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
