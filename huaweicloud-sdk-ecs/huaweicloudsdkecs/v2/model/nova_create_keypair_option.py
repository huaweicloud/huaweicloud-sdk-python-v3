# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaCreateKeypairOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public_key': 'str',
        'type': 'str',
        'name': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'public_key': 'public_key',
        'type': 'type',
        'name': 'name',
        'user_id': 'user_id'
    }

    def __init__(self, public_key=None, type=None, name=None, user_id=None):
        """NovaCreateKeypairOption

        The model defined in huaweicloud sdk

        :param public_key: 导入的公钥信息。  建议导入的公钥长度不大于1024字节。  说明：  - 长度超过1024字节会导致云服务器注入该密钥失败。
        :type public_key: str
        :param type: 密钥类型，值为“ssh”或“x509”。  说明：  - 微版本2.2支持。
        :type type: str
        :param name: 密钥名称。  新创建的密钥名称不能和已有密钥名称相同。
        :type name: str
        :param user_id: 密钥的用户ID。  说明：  - 微版本2.10支持。
        :type user_id: str
        """
        
        

        self._public_key = None
        self._type = None
        self._name = None
        self._user_id = None
        self.discriminator = None

        if public_key is not None:
            self.public_key = public_key
        if type is not None:
            self.type = type
        self.name = name
        if user_id is not None:
            self.user_id = user_id

    @property
    def public_key(self):
        """Gets the public_key of this NovaCreateKeypairOption.

        导入的公钥信息。  建议导入的公钥长度不大于1024字节。  说明：  - 长度超过1024字节会导致云服务器注入该密钥失败。

        :return: The public_key of this NovaCreateKeypairOption.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this NovaCreateKeypairOption.

        导入的公钥信息。  建议导入的公钥长度不大于1024字节。  说明：  - 长度超过1024字节会导致云服务器注入该密钥失败。

        :param public_key: The public_key of this NovaCreateKeypairOption.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def type(self):
        """Gets the type of this NovaCreateKeypairOption.

        密钥类型，值为“ssh”或“x509”。  说明：  - 微版本2.2支持。

        :return: The type of this NovaCreateKeypairOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NovaCreateKeypairOption.

        密钥类型，值为“ssh”或“x509”。  说明：  - 微版本2.2支持。

        :param type: The type of this NovaCreateKeypairOption.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this NovaCreateKeypairOption.

        密钥名称。  新创建的密钥名称不能和已有密钥名称相同。

        :return: The name of this NovaCreateKeypairOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NovaCreateKeypairOption.

        密钥名称。  新创建的密钥名称不能和已有密钥名称相同。

        :param name: The name of this NovaCreateKeypairOption.
        :type name: str
        """
        self._name = name

    @property
    def user_id(self):
        """Gets the user_id of this NovaCreateKeypairOption.

        密钥的用户ID。  说明：  - 微版本2.10支持。

        :return: The user_id of this NovaCreateKeypairOption.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this NovaCreateKeypairOption.

        密钥的用户ID。  说明：  - 微版本2.10支持。

        :param user_id: The user_id of this NovaCreateKeypairOption.
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
        if not isinstance(other, NovaCreateKeypairOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
