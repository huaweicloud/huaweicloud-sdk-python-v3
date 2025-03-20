# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class User:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'user_name': 'str',
        'is_root_user': 'bool',
        'created_at': 'datetime',
        'user_id': 'str',
        'urn': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'user_name': 'user_name',
        'is_root_user': 'is_root_user',
        'created_at': 'created_at',
        'user_id': 'user_id',
        'urn': 'urn',
        'enabled': 'enabled'
    }

    def __init__(self, description=None, user_name=None, is_root_user=None, created_at=None, user_id=None, urn=None, enabled=None):
        """User

        The model defined in huaweicloud sdk

        :param description: IAM用户描述信息，不能包含特定字符\&quot;@\&quot;、\&quot;#\&quot;、\&quot;%\&quot;、\&quot;&amp;\&quot;、\&quot;&lt;\&quot;、\&quot;&gt;\&quot;、\&quot;\\\\\&quot;、\&quot;$\&quot;、\&quot;^\&quot;和\&quot;*\&quot;的字符串。
        :type description: str
        :param user_name: IAM用户名，长度为1到64个字符，只包含字母、数字、\&quot;_\&quot;、\&quot;-\&quot;、\&quot;.\&quot;和空格的字符串，且首位不能为数字。
        :type user_name: str
        :param is_root_user: IAM用户是否为根用户。
        :type is_root_user: bool
        :param created_at: IAM用户创建时间。
        :type created_at: datetime
        :param user_id: IAM用户ID，长度为1到64个字符，只包含字母、数字和\&quot;-\&quot;的字符串。
        :type user_id: str
        :param urn: 统一资源名称。
        :type urn: str
        :param enabled: IAM用户是否启用。
        :type enabled: bool
        """
        
        

        self._description = None
        self._user_name = None
        self._is_root_user = None
        self._created_at = None
        self._user_id = None
        self._urn = None
        self._enabled = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.user_name = user_name
        self.is_root_user = is_root_user
        self.created_at = created_at
        self.user_id = user_id
        self.urn = urn
        self.enabled = enabled

    @property
    def description(self):
        """Gets the description of this User.

        IAM用户描述信息，不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\\\"、\"$\"、\"^\"和\"*\"的字符串。

        :return: The description of this User.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this User.

        IAM用户描述信息，不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\\\"、\"$\"、\"^\"和\"*\"的字符串。

        :param description: The description of this User.
        :type description: str
        """
        self._description = description

    @property
    def user_name(self):
        """Gets the user_name of this User.

        IAM用户名，长度为1到64个字符，只包含字母、数字、\"_\"、\"-\"、\".\"和空格的字符串，且首位不能为数字。

        :return: The user_name of this User.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this User.

        IAM用户名，长度为1到64个字符，只包含字母、数字、\"_\"、\"-\"、\".\"和空格的字符串，且首位不能为数字。

        :param user_name: The user_name of this User.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def is_root_user(self):
        """Gets the is_root_user of this User.

        IAM用户是否为根用户。

        :return: The is_root_user of this User.
        :rtype: bool
        """
        return self._is_root_user

    @is_root_user.setter
    def is_root_user(self, is_root_user):
        """Sets the is_root_user of this User.

        IAM用户是否为根用户。

        :param is_root_user: The is_root_user of this User.
        :type is_root_user: bool
        """
        self._is_root_user = is_root_user

    @property
    def created_at(self):
        """Gets the created_at of this User.

        IAM用户创建时间。

        :return: The created_at of this User.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this User.

        IAM用户创建时间。

        :param created_at: The created_at of this User.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def user_id(self):
        """Gets the user_id of this User.

        IAM用户ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :return: The user_id of this User.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this User.

        IAM用户ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :param user_id: The user_id of this User.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def urn(self):
        """Gets the urn of this User.

        统一资源名称。

        :return: The urn of this User.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this User.

        统一资源名称。

        :param urn: The urn of this User.
        :type urn: str
        """
        self._urn = urn

    @property
    def enabled(self):
        """Gets the enabled of this User.

        IAM用户是否启用。

        :return: The enabled of this User.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this User.

        IAM用户是否启用。

        :param enabled: The enabled of this User.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
