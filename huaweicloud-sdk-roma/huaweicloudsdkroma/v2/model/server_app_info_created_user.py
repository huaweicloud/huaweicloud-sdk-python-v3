# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerAppInfoCreatedUser:

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
        'user_name': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'user_name': 'user_name'
    }

    def __init__(self, user_id=None, user_name=None):
        """ServerAppInfoCreatedUser

        The model defined in huaweicloud sdk

        :param user_id: 创建应用的用户ID
        :type user_id: str
        :param user_name: 创建应用的用户名称
        :type user_name: str
        """
        
        

        self._user_id = None
        self._user_name = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name

    @property
    def user_id(self):
        """Gets the user_id of this ServerAppInfoCreatedUser.

        创建应用的用户ID

        :return: The user_id of this ServerAppInfoCreatedUser.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ServerAppInfoCreatedUser.

        创建应用的用户ID

        :param user_id: The user_id of this ServerAppInfoCreatedUser.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this ServerAppInfoCreatedUser.

        创建应用的用户名称

        :return: The user_name of this ServerAppInfoCreatedUser.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ServerAppInfoCreatedUser.

        创建应用的用户名称

        :param user_name: The user_name of this ServerAppInfoCreatedUser.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, ServerAppInfoCreatedUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
