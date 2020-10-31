# coding: utf-8

import pprint
import re

import six





class BatchAddMemberRequestV4:


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
        'user_id': 'str'
    }

    attribute_map = {
        'role_id': 'role_id',
        'user_id': 'user_id'
    }

    def __init__(self, role_id=None, user_id=None):
        """BatchAddMemberRequestV4 - a model defined in huaweicloud sdk"""
        
        

        self._role_id = None
        self._user_id = None
        self.discriminator = None

        if role_id is not None:
            self.role_id = role_id
        self.user_id = user_id

    @property
    def role_id(self):
        """Gets the role_id of this BatchAddMemberRequestV4.

        用户在项目中的角色ID 3, 4, 5, 6, 7 , 8

        :return: The role_id of this BatchAddMemberRequestV4.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this BatchAddMemberRequestV4.

        用户在项目中的角色ID 3, 4, 5, 6, 7 , 8

        :param role_id: The role_id of this BatchAddMemberRequestV4.
        :type: int
        """
        self._role_id = role_id

    @property
    def user_id(self):
        """Gets the user_id of this BatchAddMemberRequestV4.

        用户32位uuid

        :return: The user_id of this BatchAddMemberRequestV4.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BatchAddMemberRequestV4.

        用户32位uuid

        :param user_id: The user_id of this BatchAddMemberRequestV4.
        :type: str
        """
        self._user_id = user_id

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
        if not isinstance(other, BatchAddMemberRequestV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
