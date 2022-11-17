# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserAuth:

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
        'user_name': 'str',
        'auth': 'int'
    }

    attribute_map = {
        'user_id': 'user_id',
        'user_name': 'user_name',
        'auth': 'auth'
    }

    def __init__(self, user_id=None, user_name=None, auth=None):
        """UserAuth

        The model defined in huaweicloud sdk

        :param user_id: 用户id，需要从IAM服务获取
        :type user_id: str
        :param user_name: 用户名，需要从IAM服务获取
        :type user_name: str
        :param auth: 用户权限，7表示管理权限，3表示编辑权限，1表示读取权限
        :type auth: int
        """
        
        

        self._user_id = None
        self._user_name = None
        self._auth = None
        self.discriminator = None

        self.user_id = user_id
        self.user_name = user_name
        self.auth = auth

    @property
    def user_id(self):
        """Gets the user_id of this UserAuth.

        用户id，需要从IAM服务获取

        :return: The user_id of this UserAuth.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserAuth.

        用户id，需要从IAM服务获取

        :param user_id: The user_id of this UserAuth.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this UserAuth.

        用户名，需要从IAM服务获取

        :return: The user_name of this UserAuth.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserAuth.

        用户名，需要从IAM服务获取

        :param user_name: The user_name of this UserAuth.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def auth(self):
        """Gets the auth of this UserAuth.

        用户权限，7表示管理权限，3表示编辑权限，1表示读取权限

        :return: The auth of this UserAuth.
        :rtype: int
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this UserAuth.

        用户权限，7表示管理权限，3表示编辑权限，1表示读取权限

        :param auth: The auth of this UserAuth.
        :type auth: int
        """
        self._auth = auth

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
        if not isinstance(other, UserAuth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
