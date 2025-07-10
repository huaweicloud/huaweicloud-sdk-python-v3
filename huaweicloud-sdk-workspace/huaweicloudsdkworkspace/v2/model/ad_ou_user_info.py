# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdOuUserInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'expired_time': 'str',
        'has_existed': 'bool'
    }

    attribute_map = {
        'user_name': 'user_name',
        'expired_time': 'expired_time',
        'has_existed': 'has_existed'
    }

    def __init__(self, user_name=None, expired_time=None, has_existed=None):
        r"""AdOuUserInfo

        The model defined in huaweicloud sdk

        :param user_name: 名称。
        :type user_name: str
        :param expired_time: 过期时间 -1代表永不过期。
        :type expired_time: str
        :param has_existed: 是否存在于用户列表。
        :type has_existed: bool
        """
        
        

        self._user_name = None
        self._expired_time = None
        self._has_existed = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if expired_time is not None:
            self.expired_time = expired_time
        if has_existed is not None:
            self.has_existed = has_existed

    @property
    def user_name(self):
        r"""Gets the user_name of this AdOuUserInfo.

        名称。

        :return: The user_name of this AdOuUserInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this AdOuUserInfo.

        名称。

        :param user_name: The user_name of this AdOuUserInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def expired_time(self):
        r"""Gets the expired_time of this AdOuUserInfo.

        过期时间 -1代表永不过期。

        :return: The expired_time of this AdOuUserInfo.
        :rtype: str
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        r"""Sets the expired_time of this AdOuUserInfo.

        过期时间 -1代表永不过期。

        :param expired_time: The expired_time of this AdOuUserInfo.
        :type expired_time: str
        """
        self._expired_time = expired_time

    @property
    def has_existed(self):
        r"""Gets the has_existed of this AdOuUserInfo.

        是否存在于用户列表。

        :return: The has_existed of this AdOuUserInfo.
        :rtype: bool
        """
        return self._has_existed

    @has_existed.setter
    def has_existed(self, has_existed):
        r"""Sets the has_existed of this AdOuUserInfo.

        是否存在于用户列表。

        :param has_existed: The has_existed of this AdOuUserInfo.
        :type has_existed: bool
        """
        self._has_existed = has_existed

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
        if not isinstance(other, AdOuUserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
