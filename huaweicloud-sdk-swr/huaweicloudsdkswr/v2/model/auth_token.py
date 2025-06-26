# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthToken:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'enable': 'bool',
        'expire_date': 'str',
        'instance_id': 'str',
        'name': 'str',
        'token_id': 'str',
        'user_id': 'str',
        'user_profile': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'enable': 'enable',
        'expire_date': 'expire_date',
        'instance_id': 'instance_id',
        'name': 'name',
        'token_id': 'token_id',
        'user_id': 'user_id',
        'user_profile': 'user_profile'
    }

    def __init__(self, created_at=None, enable=None, expire_date=None, instance_id=None, name=None, token_id=None, user_id=None, user_profile=None):
        r"""AuthToken

        The model defined in huaweicloud sdk

        :param created_at: 创建时间
        :type created_at: str
        :param enable: 是否启用
        :type enable: bool
        :param expire_date: 过期时间
        :type expire_date: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param name: 访问凭证名称
        :type name: str
        :param token_id: 访问凭证ID
        :type token_id: str
        :param user_id: 访问凭证用户名
        :type user_id: str
        :param user_profile: 用户访问凭据信息
        :type user_profile: str
        """
        
        

        self._created_at = None
        self._enable = None
        self._expire_date = None
        self._instance_id = None
        self._name = None
        self._token_id = None
        self._user_id = None
        self._user_profile = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if enable is not None:
            self.enable = enable
        if expire_date is not None:
            self.expire_date = expire_date
        if instance_id is not None:
            self.instance_id = instance_id
        if name is not None:
            self.name = name
        if token_id is not None:
            self.token_id = token_id
        if user_id is not None:
            self.user_id = user_id
        if user_profile is not None:
            self.user_profile = user_profile

    @property
    def created_at(self):
        r"""Gets the created_at of this AuthToken.

        创建时间

        :return: The created_at of this AuthToken.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this AuthToken.

        创建时间

        :param created_at: The created_at of this AuthToken.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def enable(self):
        r"""Gets the enable of this AuthToken.

        是否启用

        :return: The enable of this AuthToken.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this AuthToken.

        是否启用

        :param enable: The enable of this AuthToken.
        :type enable: bool
        """
        self._enable = enable

    @property
    def expire_date(self):
        r"""Gets the expire_date of this AuthToken.

        过期时间

        :return: The expire_date of this AuthToken.
        :rtype: str
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        r"""Sets the expire_date of this AuthToken.

        过期时间

        :param expire_date: The expire_date of this AuthToken.
        :type expire_date: str
        """
        self._expire_date = expire_date

    @property
    def instance_id(self):
        r"""Gets the instance_id of this AuthToken.

        实例ID

        :return: The instance_id of this AuthToken.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this AuthToken.

        实例ID

        :param instance_id: The instance_id of this AuthToken.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        r"""Gets the name of this AuthToken.

        访问凭证名称

        :return: The name of this AuthToken.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AuthToken.

        访问凭证名称

        :param name: The name of this AuthToken.
        :type name: str
        """
        self._name = name

    @property
    def token_id(self):
        r"""Gets the token_id of this AuthToken.

        访问凭证ID

        :return: The token_id of this AuthToken.
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        r"""Sets the token_id of this AuthToken.

        访问凭证ID

        :param token_id: The token_id of this AuthToken.
        :type token_id: str
        """
        self._token_id = token_id

    @property
    def user_id(self):
        r"""Gets the user_id of this AuthToken.

        访问凭证用户名

        :return: The user_id of this AuthToken.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this AuthToken.

        访问凭证用户名

        :param user_id: The user_id of this AuthToken.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_profile(self):
        r"""Gets the user_profile of this AuthToken.

        用户访问凭据信息

        :return: The user_profile of this AuthToken.
        :rtype: str
        """
        return self._user_profile

    @user_profile.setter
    def user_profile(self, user_profile):
        r"""Sets the user_profile of this AuthToken.

        用户访问凭据信息

        :param user_profile: The user_profile of this AuthToken.
        :type user_profile: str
        """
        self._user_profile = user_profile

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
        if not isinstance(other, AuthToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
