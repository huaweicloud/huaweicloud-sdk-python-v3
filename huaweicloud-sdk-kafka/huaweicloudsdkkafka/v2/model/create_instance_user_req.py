# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceUserReq:

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
        'user_desc': 'str',
        'user_passwd': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'user_desc': 'user_desc',
        'user_passwd': 'user_passwd'
    }

    def __init__(self, user_name=None, user_desc=None, user_passwd=None):
        """CreateInstanceUserReq

        The model defined in huaweicloud sdk

        :param user_name: 用户名称。
        :type user_name: str
        :param user_desc: 用户描述。
        :type user_desc: str
        :param user_passwd: 用户密码。  密码不能和用户名相同。 复杂度要求： - 输入长度为8到32位的字符串。 - 必须包含如下四种字符中的两种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（&#x60;~!@#$%^&amp;*()-_&#x3D;+\\|[{}]:&#39;\&quot;,&lt;.&gt;/?）
        :type user_passwd: str
        """
        
        

        self._user_name = None
        self._user_desc = None
        self._user_passwd = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if user_desc is not None:
            self.user_desc = user_desc
        if user_passwd is not None:
            self.user_passwd = user_passwd

    @property
    def user_name(self):
        """Gets the user_name of this CreateInstanceUserReq.

        用户名称。

        :return: The user_name of this CreateInstanceUserReq.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CreateInstanceUserReq.

        用户名称。

        :param user_name: The user_name of this CreateInstanceUserReq.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_desc(self):
        """Gets the user_desc of this CreateInstanceUserReq.

        用户描述。

        :return: The user_desc of this CreateInstanceUserReq.
        :rtype: str
        """
        return self._user_desc

    @user_desc.setter
    def user_desc(self, user_desc):
        """Sets the user_desc of this CreateInstanceUserReq.

        用户描述。

        :param user_desc: The user_desc of this CreateInstanceUserReq.
        :type user_desc: str
        """
        self._user_desc = user_desc

    @property
    def user_passwd(self):
        """Gets the user_passwd of this CreateInstanceUserReq.

        用户密码。  密码不能和用户名相同。 复杂度要求： - 输入长度为8到32位的字符串。 - 必须包含如下四种字符中的两种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（`~!@#$%^&*()-_=+\\|[{}]:'\",<.>/?）

        :return: The user_passwd of this CreateInstanceUserReq.
        :rtype: str
        """
        return self._user_passwd

    @user_passwd.setter
    def user_passwd(self, user_passwd):
        """Sets the user_passwd of this CreateInstanceUserReq.

        用户密码。  密码不能和用户名相同。 复杂度要求： - 输入长度为8到32位的字符串。 - 必须包含如下四种字符中的两种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（`~!@#$%^&*()-_=+\\|[{}]:'\",<.>/?）

        :param user_passwd: The user_passwd of this CreateInstanceUserReq.
        :type user_passwd: str
        """
        self._user_passwd = user_passwd

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
        if not isinstance(other, CreateInstanceUserReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
