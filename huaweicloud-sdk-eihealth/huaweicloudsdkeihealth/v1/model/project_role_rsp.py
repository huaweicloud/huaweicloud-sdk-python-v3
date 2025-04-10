# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectRoleRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_type': 'str',
        'users': 'list[BindUserRsp]'
    }

    attribute_map = {
        'role_type': 'role_type',
        'users': 'users'
    }

    def __init__(self, role_type=None, users=None):
        r"""ProjectRoleRsp

        The model defined in huaweicloud sdk

        :param role_type: 项目角色名
        :type role_type: str
        :param users: 项目成员列表
        :type users: list[:class:`huaweicloudsdkeihealth.v1.BindUserRsp`]
        """
        
        

        self._role_type = None
        self._users = None
        self.discriminator = None

        if role_type is not None:
            self.role_type = role_type
        if users is not None:
            self.users = users

    @property
    def role_type(self):
        r"""Gets the role_type of this ProjectRoleRsp.

        项目角色名

        :return: The role_type of this ProjectRoleRsp.
        :rtype: str
        """
        return self._role_type

    @role_type.setter
    def role_type(self, role_type):
        r"""Sets the role_type of this ProjectRoleRsp.

        项目角色名

        :param role_type: The role_type of this ProjectRoleRsp.
        :type role_type: str
        """
        self._role_type = role_type

    @property
    def users(self):
        r"""Gets the users of this ProjectRoleRsp.

        项目成员列表

        :return: The users of this ProjectRoleRsp.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.BindUserRsp`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this ProjectRoleRsp.

        项目成员列表

        :param users: The users of this ProjectRoleRsp.
        :type users: list[:class:`huaweicloudsdkeihealth.v1.BindUserRsp`]
        """
        self._users = users

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
        if not isinstance(other, ProjectRoleRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
