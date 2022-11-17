# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetProductAuthenticationRequestBody:

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
        'password': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'password': 'password'
    }

    def __init__(self, user_name=None, password=None):
        """ResetProductAuthenticationRequestBody

        The model defined in huaweicloud sdk

        :param user_name: 产品用户名，支持英文大小写、英文符号(-)及数字，长度限制10-50位，传参空，用户名不被重置
        :type user_name: str
        :param password: 产品密码，包含数字、英文字母大小写、特殊字符(-~!@#$%^&amp;*()-_&#x3D;+|[{}];:&lt;&gt;/?)，长度10-80位，传参空，密码不被重置。当用户名与密码都为空时，密码重置，由系统生成。
        :type password: str
        """
        
        

        self._user_name = None
        self._password = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password

    @property
    def user_name(self):
        """Gets the user_name of this ResetProductAuthenticationRequestBody.

        产品用户名，支持英文大小写、英文符号(-)及数字，长度限制10-50位，传参空，用户名不被重置

        :return: The user_name of this ResetProductAuthenticationRequestBody.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ResetProductAuthenticationRequestBody.

        产品用户名，支持英文大小写、英文符号(-)及数字，长度限制10-50位，传参空，用户名不被重置

        :param user_name: The user_name of this ResetProductAuthenticationRequestBody.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this ResetProductAuthenticationRequestBody.

        产品密码，包含数字、英文字母大小写、特殊字符(-~!@#$%^&*()-_=+|[{}];:<>/?)，长度10-80位，传参空，密码不被重置。当用户名与密码都为空时，密码重置，由系统生成。

        :return: The password of this ResetProductAuthenticationRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ResetProductAuthenticationRequestBody.

        产品密码，包含数字、英文字母大小写、特殊字符(-~!@#$%^&*()-_=+|[{}];:<>/?)，长度10-80位，传参空，密码不被重置。当用户名与密码都为空时，密码重置，由系统生成。

        :param password: The password of this ResetProductAuthenticationRequestBody.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, ResetProductAuthenticationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
