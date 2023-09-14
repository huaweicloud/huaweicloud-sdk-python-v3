# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportPrivateKeyKeypairBean:

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
        'user_id': 'str',
        'key_protection': 'ImportPrivateKeyProtection'
    }

    attribute_map = {
        'name': 'name',
        'user_id': 'user_id',
        'key_protection': 'key_protection'
    }

    def __init__(self, name=None, user_id=None, key_protection=None):
        """ImportPrivateKeyKeypairBean

        The model defined in huaweicloud sdk

        :param name: SSH密钥对的名称。 - 新创建的密钥对名称不能和已有密钥对的名称相同。 - SSH密钥对名称由英文字母、数字、下划线、中划线组成，长度不能超过64个字节
        :type name: str
        :param user_id: SSH密钥对所属的用户信息
        :type user_id: str
        :param key_protection: 
        :type key_protection: :class:`huaweicloudsdkkps.v3.ImportPrivateKeyProtection`
        """
        
        

        self._name = None
        self._user_id = None
        self._key_protection = None
        self.discriminator = None

        self.name = name
        if user_id is not None:
            self.user_id = user_id
        self.key_protection = key_protection

    @property
    def name(self):
        """Gets the name of this ImportPrivateKeyKeypairBean.

        SSH密钥对的名称。 - 新创建的密钥对名称不能和已有密钥对的名称相同。 - SSH密钥对名称由英文字母、数字、下划线、中划线组成，长度不能超过64个字节

        :return: The name of this ImportPrivateKeyKeypairBean.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImportPrivateKeyKeypairBean.

        SSH密钥对的名称。 - 新创建的密钥对名称不能和已有密钥对的名称相同。 - SSH密钥对名称由英文字母、数字、下划线、中划线组成，长度不能超过64个字节

        :param name: The name of this ImportPrivateKeyKeypairBean.
        :type name: str
        """
        self._name = name

    @property
    def user_id(self):
        """Gets the user_id of this ImportPrivateKeyKeypairBean.

        SSH密钥对所属的用户信息

        :return: The user_id of this ImportPrivateKeyKeypairBean.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ImportPrivateKeyKeypairBean.

        SSH密钥对所属的用户信息

        :param user_id: The user_id of this ImportPrivateKeyKeypairBean.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def key_protection(self):
        """Gets the key_protection of this ImportPrivateKeyKeypairBean.

        :return: The key_protection of this ImportPrivateKeyKeypairBean.
        :rtype: :class:`huaweicloudsdkkps.v3.ImportPrivateKeyProtection`
        """
        return self._key_protection

    @key_protection.setter
    def key_protection(self, key_protection):
        """Sets the key_protection of this ImportPrivateKeyKeypairBean.

        :param key_protection: The key_protection of this ImportPrivateKeyKeypairBean.
        :type key_protection: :class:`huaweicloudsdkkps.v3.ImportPrivateKeyProtection`
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
        if not isinstance(other, ImportPrivateKeyKeypairBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
