# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserInGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'user_name': 'str',
        'user_email': 'str',
        'user_phone': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_name': 'user_name',
        'user_email': 'user_email',
        'user_phone': 'user_phone',
        'description': 'description'
    }

    def __init__(self, id=None, user_name=None, user_email=None, user_phone=None, description=None):
        """UserInGroup

        The model defined in huaweicloud sdk

        :param id: 用户ID。
        :type id: str
        :param user_name: 桌面用户名。
        :type user_name: str
        :param user_email: 用户邮箱。
        :type user_email: str
        :param user_phone: 用户手机号。
        :type user_phone: str
        :param description: 用户描述。
        :type description: str
        """
        
        

        self._id = None
        self._user_name = None
        self._user_email = None
        self._user_phone = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_name is not None:
            self.user_name = user_name
        if user_email is not None:
            self.user_email = user_email
        if user_phone is not None:
            self.user_phone = user_phone
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this UserInGroup.

        用户ID。

        :return: The id of this UserInGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserInGroup.

        用户ID。

        :param id: The id of this UserInGroup.
        :type id: str
        """
        self._id = id

    @property
    def user_name(self):
        """Gets the user_name of this UserInGroup.

        桌面用户名。

        :return: The user_name of this UserInGroup.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserInGroup.

        桌面用户名。

        :param user_name: The user_name of this UserInGroup.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_email(self):
        """Gets the user_email of this UserInGroup.

        用户邮箱。

        :return: The user_email of this UserInGroup.
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this UserInGroup.

        用户邮箱。

        :param user_email: The user_email of this UserInGroup.
        :type user_email: str
        """
        self._user_email = user_email

    @property
    def user_phone(self):
        """Gets the user_phone of this UserInGroup.

        用户手机号。

        :return: The user_phone of this UserInGroup.
        :rtype: str
        """
        return self._user_phone

    @user_phone.setter
    def user_phone(self, user_phone):
        """Sets the user_phone of this UserInGroup.

        用户手机号。

        :param user_phone: The user_phone of this UserInGroup.
        :type user_phone: str
        """
        self._user_phone = user_phone

    @property
    def description(self):
        """Gets the description of this UserInGroup.

        用户描述。

        :return: The description of this UserInGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserInGroup.

        用户描述。

        :param description: The description of this UserInGroup.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UserInGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
