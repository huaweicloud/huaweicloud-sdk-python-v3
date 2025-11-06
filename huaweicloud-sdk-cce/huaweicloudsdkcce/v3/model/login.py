# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Login:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ssh_key': 'str',
        'user_password': 'UserPassword',
        'remove_user_password': 'bool',
        'remove_ssh_key': 'bool'
    }

    attribute_map = {
        'ssh_key': 'sshKey',
        'user_password': 'userPassword',
        'remove_user_password': 'removeUserPassword',
        'remove_ssh_key': 'removeSSHKey'
    }

    def __init__(self, ssh_key=None, user_password=None, remove_user_password=None, remove_ssh_key=None):
        r"""Login

        The model defined in huaweicloud sdk

        :param ssh_key: 选择密钥对方式登录时的密钥对名称。
        :type ssh_key: str
        :param user_password: 
        :type user_password: :class:`huaweicloudsdkcce.v3.UserPassword`
        :param remove_user_password: **参数解释**： 更新节点池时，移除当前节点池密码方式登录的配置 **约束限制**： 仅更新节点池场景支持该参数，设置为true时不允许设置userPassword **取值范围**： 不涉及 **默认取值**： false
        :type remove_user_password: bool
        :param remove_ssh_key: **参数解释**： 更新节点池时，移除当前节点池密钥对方式登录的配置 **约束限制**： 仅更新节点池场景支持该参数，设置为true时不允许设置sshKey **取值范围**： 不涉及 **默认取值**： false
        :type remove_ssh_key: bool
        """
        
        

        self._ssh_key = None
        self._user_password = None
        self._remove_user_password = None
        self._remove_ssh_key = None
        self.discriminator = None

        if ssh_key is not None:
            self.ssh_key = ssh_key
        if user_password is not None:
            self.user_password = user_password
        if remove_user_password is not None:
            self.remove_user_password = remove_user_password
        if remove_ssh_key is not None:
            self.remove_ssh_key = remove_ssh_key

    @property
    def ssh_key(self):
        r"""Gets the ssh_key of this Login.

        选择密钥对方式登录时的密钥对名称。

        :return: The ssh_key of this Login.
        :rtype: str
        """
        return self._ssh_key

    @ssh_key.setter
    def ssh_key(self, ssh_key):
        r"""Sets the ssh_key of this Login.

        选择密钥对方式登录时的密钥对名称。

        :param ssh_key: The ssh_key of this Login.
        :type ssh_key: str
        """
        self._ssh_key = ssh_key

    @property
    def user_password(self):
        r"""Gets the user_password of this Login.

        :return: The user_password of this Login.
        :rtype: :class:`huaweicloudsdkcce.v3.UserPassword`
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        r"""Sets the user_password of this Login.

        :param user_password: The user_password of this Login.
        :type user_password: :class:`huaweicloudsdkcce.v3.UserPassword`
        """
        self._user_password = user_password

    @property
    def remove_user_password(self):
        r"""Gets the remove_user_password of this Login.

        **参数解释**： 更新节点池时，移除当前节点池密码方式登录的配置 **约束限制**： 仅更新节点池场景支持该参数，设置为true时不允许设置userPassword **取值范围**： 不涉及 **默认取值**： false

        :return: The remove_user_password of this Login.
        :rtype: bool
        """
        return self._remove_user_password

    @remove_user_password.setter
    def remove_user_password(self, remove_user_password):
        r"""Sets the remove_user_password of this Login.

        **参数解释**： 更新节点池时，移除当前节点池密码方式登录的配置 **约束限制**： 仅更新节点池场景支持该参数，设置为true时不允许设置userPassword **取值范围**： 不涉及 **默认取值**： false

        :param remove_user_password: The remove_user_password of this Login.
        :type remove_user_password: bool
        """
        self._remove_user_password = remove_user_password

    @property
    def remove_ssh_key(self):
        r"""Gets the remove_ssh_key of this Login.

        **参数解释**： 更新节点池时，移除当前节点池密钥对方式登录的配置 **约束限制**： 仅更新节点池场景支持该参数，设置为true时不允许设置sshKey **取值范围**： 不涉及 **默认取值**： false

        :return: The remove_ssh_key of this Login.
        :rtype: bool
        """
        return self._remove_ssh_key

    @remove_ssh_key.setter
    def remove_ssh_key(self, remove_ssh_key):
        r"""Sets the remove_ssh_key of this Login.

        **参数解释**： 更新节点池时，移除当前节点池密钥对方式登录的配置 **约束限制**： 仅更新节点池场景支持该参数，设置为true时不允许设置sshKey **取值范围**： 不涉及 **默认取值**： false

        :param remove_ssh_key: The remove_ssh_key of this Login.
        :type remove_ssh_key: bool
        """
        self._remove_ssh_key = remove_ssh_key

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Login):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
