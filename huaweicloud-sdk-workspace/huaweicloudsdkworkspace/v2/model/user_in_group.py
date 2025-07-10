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
        'total_desktops': 'int',
        'enterprise_project_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_name': 'user_name',
        'user_email': 'user_email',
        'user_phone': 'user_phone',
        'total_desktops': 'total_desktops',
        'enterprise_project_id': 'enterprise_project_id',
        'description': 'description'
    }

    def __init__(self, id=None, user_name=None, user_email=None, user_phone=None, total_desktops=None, enterprise_project_id=None, description=None):
        r"""UserInGroup

        The model defined in huaweicloud sdk

        :param id: 用户ID。
        :type id: str
        :param user_name: 桌面用户名。
        :type user_name: str
        :param user_email: 用户邮箱。
        :type user_email: str
        :param user_phone: 用户手机号。
        :type user_phone: str
        :param total_desktops: 用户桌面数。
        :type total_desktops: int
        :param enterprise_project_id: 企业项ID。
        :type enterprise_project_id: str
        :param description: 用户描述。
        :type description: str
        """
        
        

        self._id = None
        self._user_name = None
        self._user_email = None
        self._user_phone = None
        self._total_desktops = None
        self._enterprise_project_id = None
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
        if total_desktops is not None:
            self.total_desktops = total_desktops
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this UserInGroup.

        用户ID。

        :return: The id of this UserInGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UserInGroup.

        用户ID。

        :param id: The id of this UserInGroup.
        :type id: str
        """
        self._id = id

    @property
    def user_name(self):
        r"""Gets the user_name of this UserInGroup.

        桌面用户名。

        :return: The user_name of this UserInGroup.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this UserInGroup.

        桌面用户名。

        :param user_name: The user_name of this UserInGroup.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_email(self):
        r"""Gets the user_email of this UserInGroup.

        用户邮箱。

        :return: The user_email of this UserInGroup.
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        r"""Sets the user_email of this UserInGroup.

        用户邮箱。

        :param user_email: The user_email of this UserInGroup.
        :type user_email: str
        """
        self._user_email = user_email

    @property
    def user_phone(self):
        r"""Gets the user_phone of this UserInGroup.

        用户手机号。

        :return: The user_phone of this UserInGroup.
        :rtype: str
        """
        return self._user_phone

    @user_phone.setter
    def user_phone(self, user_phone):
        r"""Sets the user_phone of this UserInGroup.

        用户手机号。

        :param user_phone: The user_phone of this UserInGroup.
        :type user_phone: str
        """
        self._user_phone = user_phone

    @property
    def total_desktops(self):
        r"""Gets the total_desktops of this UserInGroup.

        用户桌面数。

        :return: The total_desktops of this UserInGroup.
        :rtype: int
        """
        return self._total_desktops

    @total_desktops.setter
    def total_desktops(self, total_desktops):
        r"""Sets the total_desktops of this UserInGroup.

        用户桌面数。

        :param total_desktops: The total_desktops of this UserInGroup.
        :type total_desktops: int
        """
        self._total_desktops = total_desktops

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this UserInGroup.

        企业项ID。

        :return: The enterprise_project_id of this UserInGroup.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this UserInGroup.

        企业项ID。

        :param enterprise_project_id: The enterprise_project_id of this UserInGroup.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def description(self):
        r"""Gets the description of this UserInGroup.

        用户描述。

        :return: The description of this UserInGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UserInGroup.

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
