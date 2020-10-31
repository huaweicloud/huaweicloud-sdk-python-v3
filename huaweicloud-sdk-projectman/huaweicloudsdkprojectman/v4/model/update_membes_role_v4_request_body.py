# coding: utf-8

import pprint
import re

import six





class UpdateMembesRoleV4RequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'role_id': 'int',
        'user_ids': 'list[str]'
    }

    attribute_map = {
        'role_id': 'role_id',
        'user_ids': 'user_ids'
    }

    def __init__(self, role_id=None, user_ids=None):
        """UpdateMembesRoleV4RequestBody - a model defined in huaweicloud sdk"""
        
        

        self._role_id = None
        self._user_ids = None
        self.discriminator = None

        self.role_id = role_id
        self.user_ids = user_ids

    @property
    def role_id(self):
        """Gets the role_id of this UpdateMembesRoleV4RequestBody.

        成员角色 3 项目经理 4 开发人员 5 测试经理 6 测试人员 7 参与者 8 浏览者

        :return: The role_id of this UpdateMembesRoleV4RequestBody.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this UpdateMembesRoleV4RequestBody.

        成员角色 3 项目经理 4 开发人员 5 测试经理 6 测试人员 7 参与者 8 浏览者

        :param role_id: The role_id of this UpdateMembesRoleV4RequestBody.
        :type: int
        """
        self._role_id = role_id

    @property
    def user_ids(self):
        """Gets the user_ids of this UpdateMembesRoleV4RequestBody.

        用户id

        :return: The user_ids of this UpdateMembesRoleV4RequestBody.
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this UpdateMembesRoleV4RequestBody.

        用户id

        :param user_ids: The user_ids of this UpdateMembesRoleV4RequestBody.
        :type: list[str]
        """
        self._user_ids = user_ids

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateMembesRoleV4RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
