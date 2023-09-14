# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateUserReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_password': 'str',
        'user_name': 'str',
        'user_desc': 'str'
    }

    attribute_map = {
        'new_password': 'new_password',
        'user_name': 'user_name',
        'user_desc': 'user_desc'
    }

    def __init__(self, new_password=None, user_name=None, user_desc=None):
        """UpdateUserReq

        The model defined in huaweicloud sdk

        :param new_password: 用户新密码。  不能与名称或倒序的名称相同。 复杂度要求： - 输入长度为8到32位的字符串。 - 必须包含如下四种字符中的三种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（&#x60;~!@#$%^&amp;*()-_&#x3D;+\\|[{}]:&#39;\&quot;,&lt;.&gt;/?）
        :type new_password: str
        :param user_name: 用户名。
        :type user_name: str
        :param user_desc: 用户描述。
        :type user_desc: str
        """
        
        

        self._new_password = None
        self._user_name = None
        self._user_desc = None
        self.discriminator = None

        if new_password is not None:
            self.new_password = new_password
        if user_name is not None:
            self.user_name = user_name
        if user_desc is not None:
            self.user_desc = user_desc

    @property
    def new_password(self):
        """Gets the new_password of this UpdateUserReq.

        用户新密码。  不能与名称或倒序的名称相同。 复杂度要求： - 输入长度为8到32位的字符串。 - 必须包含如下四种字符中的三种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（`~!@#$%^&*()-_=+\\|[{}]:'\",<.>/?）

        :return: The new_password of this UpdateUserReq.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this UpdateUserReq.

        用户新密码。  不能与名称或倒序的名称相同。 复杂度要求： - 输入长度为8到32位的字符串。 - 必须包含如下四种字符中的三种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（`~!@#$%^&*()-_=+\\|[{}]:'\",<.>/?）

        :param new_password: The new_password of this UpdateUserReq.
        :type new_password: str
        """
        self._new_password = new_password

    @property
    def user_name(self):
        """Gets the user_name of this UpdateUserReq.

        用户名。

        :return: The user_name of this UpdateUserReq.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UpdateUserReq.

        用户名。

        :param user_name: The user_name of this UpdateUserReq.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_desc(self):
        """Gets the user_desc of this UpdateUserReq.

        用户描述。

        :return: The user_desc of this UpdateUserReq.
        :rtype: str
        """
        return self._user_desc

    @user_desc.setter
    def user_desc(self, user_desc):
        """Sets the user_desc of this UpdateUserReq.

        用户描述。

        :param user_desc: The user_desc of this UpdateUserReq.
        :type user_desc: str
        """
        self._user_desc = user_desc

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
        if not isinstance(other, UpdateUserReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
