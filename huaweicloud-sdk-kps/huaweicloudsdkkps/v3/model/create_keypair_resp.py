# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateKeypairResp:

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
        'private_key': 'str',
        'fingerprint': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'public_key': 'public_key',
        'private_key': 'private_key',
        'fingerprint': 'fingerprint',
        'user_id': 'user_id'
    }

    def __init__(self, name=None, type=None, public_key=None, private_key=None, fingerprint=None, user_id=None):
        """CreateKeypairResp

        The model defined in huaweicloud sdk

        :param name: SSH密钥对的名称
        :type name: str
        :param type: SSH密钥对的类型
        :type type: str
        :param public_key: SSH密钥对对应的publicKey信息
        :type public_key: str
        :param private_key: SSH密钥对对应的privateKey信息 - 创建SSH密钥对时，响应中包括private_key的信息。 - 导入SSH密钥对时，响应中不包括private_key的信息。
        :type private_key: str
        :param fingerprint: SSH密钥对应指纹信息
        :type fingerprint: str
        :param user_id: SSH密钥对所属的用户信息
        :type user_id: str
        """
        
        

        self._name = None
        self._type = None
        self._public_key = None
        self._private_key = None
        self._fingerprint = None
        self._user_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if public_key is not None:
            self.public_key = public_key
        if private_key is not None:
            self.private_key = private_key
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if user_id is not None:
            self.user_id = user_id

    @property
    def name(self):
        """Gets the name of this CreateKeypairResp.

        SSH密钥对的名称

        :return: The name of this CreateKeypairResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateKeypairResp.

        SSH密钥对的名称

        :param name: The name of this CreateKeypairResp.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CreateKeypairResp.

        SSH密钥对的类型

        :return: The type of this CreateKeypairResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateKeypairResp.

        SSH密钥对的类型

        :param type: The type of this CreateKeypairResp.
        :type type: str
        """
        self._type = type

    @property
    def public_key(self):
        """Gets the public_key of this CreateKeypairResp.

        SSH密钥对对应的publicKey信息

        :return: The public_key of this CreateKeypairResp.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this CreateKeypairResp.

        SSH密钥对对应的publicKey信息

        :param public_key: The public_key of this CreateKeypairResp.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def private_key(self):
        """Gets the private_key of this CreateKeypairResp.

        SSH密钥对对应的privateKey信息 - 创建SSH密钥对时，响应中包括private_key的信息。 - 导入SSH密钥对时，响应中不包括private_key的信息。

        :return: The private_key of this CreateKeypairResp.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this CreateKeypairResp.

        SSH密钥对对应的privateKey信息 - 创建SSH密钥对时，响应中包括private_key的信息。 - 导入SSH密钥对时，响应中不包括private_key的信息。

        :param private_key: The private_key of this CreateKeypairResp.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def fingerprint(self):
        """Gets the fingerprint of this CreateKeypairResp.

        SSH密钥对应指纹信息

        :return: The fingerprint of this CreateKeypairResp.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this CreateKeypairResp.

        SSH密钥对应指纹信息

        :param fingerprint: The fingerprint of this CreateKeypairResp.
        :type fingerprint: str
        """
        self._fingerprint = fingerprint

    @property
    def user_id(self):
        """Gets the user_id of this CreateKeypairResp.

        SSH密钥对所属的用户信息

        :return: The user_id of this CreateKeypairResp.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CreateKeypairResp.

        SSH密钥对所属的用户信息

        :param user_id: The user_id of this CreateKeypairResp.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, CreateKeypairResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
