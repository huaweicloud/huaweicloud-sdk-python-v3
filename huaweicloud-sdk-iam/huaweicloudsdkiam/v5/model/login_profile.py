# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoginProfile:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'password_reset_required': 'bool',
        'password_expires_at': 'datetime',
        'created_at': 'datetime'
    }

    attribute_map = {
        'user_id': 'user_id',
        'password_reset_required': 'password_reset_required',
        'password_expires_at': 'password_expires_at',
        'created_at': 'created_at'
    }

    def __init__(self, user_id=None, password_reset_required=None, password_expires_at=None, created_at=None):
        r"""LoginProfile

        The model defined in huaweicloud sdk

        :param user_id: IAM用户ID。
        :type user_id: str
        :param password_reset_required: IAM用户下次登录时是否需要修改密码。
        :type password_reset_required: bool
        :param password_expires_at: IAM用户密码过期时间。
        :type password_expires_at: datetime
        :param created_at: IAM用户登录信息创建时间。
        :type created_at: datetime
        """
        
        

        self._user_id = None
        self._password_reset_required = None
        self._password_expires_at = None
        self._created_at = None
        self.discriminator = None

        self.user_id = user_id
        self.password_reset_required = password_reset_required
        if password_expires_at is not None:
            self.password_expires_at = password_expires_at
        self.created_at = created_at

    @property
    def user_id(self):
        r"""Gets the user_id of this LoginProfile.

        IAM用户ID。

        :return: The user_id of this LoginProfile.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this LoginProfile.

        IAM用户ID。

        :param user_id: The user_id of this LoginProfile.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def password_reset_required(self):
        r"""Gets the password_reset_required of this LoginProfile.

        IAM用户下次登录时是否需要修改密码。

        :return: The password_reset_required of this LoginProfile.
        :rtype: bool
        """
        return self._password_reset_required

    @password_reset_required.setter
    def password_reset_required(self, password_reset_required):
        r"""Sets the password_reset_required of this LoginProfile.

        IAM用户下次登录时是否需要修改密码。

        :param password_reset_required: The password_reset_required of this LoginProfile.
        :type password_reset_required: bool
        """
        self._password_reset_required = password_reset_required

    @property
    def password_expires_at(self):
        r"""Gets the password_expires_at of this LoginProfile.

        IAM用户密码过期时间。

        :return: The password_expires_at of this LoginProfile.
        :rtype: datetime
        """
        return self._password_expires_at

    @password_expires_at.setter
    def password_expires_at(self, password_expires_at):
        r"""Sets the password_expires_at of this LoginProfile.

        IAM用户密码过期时间。

        :param password_expires_at: The password_expires_at of this LoginProfile.
        :type password_expires_at: datetime
        """
        self._password_expires_at = password_expires_at

    @property
    def created_at(self):
        r"""Gets the created_at of this LoginProfile.

        IAM用户登录信息创建时间。

        :return: The created_at of this LoginProfile.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this LoginProfile.

        IAM用户登录信息创建时间。

        :param created_at: The created_at of this LoginProfile.
        :type created_at: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, LoginProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
