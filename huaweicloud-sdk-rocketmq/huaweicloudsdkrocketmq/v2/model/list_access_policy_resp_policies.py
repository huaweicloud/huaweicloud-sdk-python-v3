# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccessPolicyRespPolicies:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'access_key': 'str',
        'secret_key': 'str',
        'white_remote_address': 'str',
        'admin': 'bool',
        'perm': 'str'
    }

    attribute_map = {
        'access_key': 'access_key',
        'secret_key': 'secret_key',
        'white_remote_address': 'white_remote_address',
        'admin': 'admin',
        'perm': 'perm'
    }

    def __init__(self, access_key=None, secret_key=None, white_remote_address=None, admin=None, perm=None):
        """ListAccessPolicyRespPolicies

        The model defined in huaweicloud sdk

        :param access_key: 用户名。
        :type access_key: str
        :param secret_key: 秘钥。
        :type secret_key: str
        :param white_remote_address: IP白名单。
        :type white_remote_address: str
        :param admin: 是否为管理员。
        :type admin: bool
        :param perm: 权限。
        :type perm: str
        """
        
        

        self._access_key = None
        self._secret_key = None
        self._white_remote_address = None
        self._admin = None
        self._perm = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key
        if white_remote_address is not None:
            self.white_remote_address = white_remote_address
        if admin is not None:
            self.admin = admin
        if perm is not None:
            self.perm = perm

    @property
    def access_key(self):
        """Gets the access_key of this ListAccessPolicyRespPolicies.

        用户名。

        :return: The access_key of this ListAccessPolicyRespPolicies.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this ListAccessPolicyRespPolicies.

        用户名。

        :param access_key: The access_key of this ListAccessPolicyRespPolicies.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def secret_key(self):
        """Gets the secret_key of this ListAccessPolicyRespPolicies.

        秘钥。

        :return: The secret_key of this ListAccessPolicyRespPolicies.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this ListAccessPolicyRespPolicies.

        秘钥。

        :param secret_key: The secret_key of this ListAccessPolicyRespPolicies.
        :type secret_key: str
        """
        self._secret_key = secret_key

    @property
    def white_remote_address(self):
        """Gets the white_remote_address of this ListAccessPolicyRespPolicies.

        IP白名单。

        :return: The white_remote_address of this ListAccessPolicyRespPolicies.
        :rtype: str
        """
        return self._white_remote_address

    @white_remote_address.setter
    def white_remote_address(self, white_remote_address):
        """Sets the white_remote_address of this ListAccessPolicyRespPolicies.

        IP白名单。

        :param white_remote_address: The white_remote_address of this ListAccessPolicyRespPolicies.
        :type white_remote_address: str
        """
        self._white_remote_address = white_remote_address

    @property
    def admin(self):
        """Gets the admin of this ListAccessPolicyRespPolicies.

        是否为管理员。

        :return: The admin of this ListAccessPolicyRespPolicies.
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this ListAccessPolicyRespPolicies.

        是否为管理员。

        :param admin: The admin of this ListAccessPolicyRespPolicies.
        :type admin: bool
        """
        self._admin = admin

    @property
    def perm(self):
        """Gets the perm of this ListAccessPolicyRespPolicies.

        权限。

        :return: The perm of this ListAccessPolicyRespPolicies.
        :rtype: str
        """
        return self._perm

    @perm.setter
    def perm(self, perm):
        """Sets the perm of this ListAccessPolicyRespPolicies.

        权限。

        :param perm: The perm of this ListAccessPolicyRespPolicies.
        :type perm: str
        """
        self._perm = perm

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
        if not isinstance(other, ListAccessPolicyRespPolicies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
