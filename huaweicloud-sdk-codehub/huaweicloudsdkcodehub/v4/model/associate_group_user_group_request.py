# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateGroupUserGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'group_id': 'int',
        'user_group_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'group_id': 'group_id',
        'user_group_id': 'user_group_id'
    }

    def __init__(self, project_id=None, group_id=None, user_group_id=None):
        """AssociateGroupUserGroupRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param group_id: 代码组 ID
        :type group_id: int
        :param user_group_id: 成员组 ID
        :type user_group_id: str
        """
        
        

        self._project_id = None
        self._group_id = None
        self._user_group_id = None
        self.discriminator = None

        self.project_id = project_id
        self.group_id = group_id
        self.user_group_id = user_group_id

    @property
    def project_id(self):
        """Gets the project_id of this AssociateGroupUserGroupRequest.

        项目id

        :return: The project_id of this AssociateGroupUserGroupRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AssociateGroupUserGroupRequest.

        项目id

        :param project_id: The project_id of this AssociateGroupUserGroupRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def group_id(self):
        """Gets the group_id of this AssociateGroupUserGroupRequest.

        代码组 ID

        :return: The group_id of this AssociateGroupUserGroupRequest.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AssociateGroupUserGroupRequest.

        代码组 ID

        :param group_id: The group_id of this AssociateGroupUserGroupRequest.
        :type group_id: int
        """
        self._group_id = group_id

    @property
    def user_group_id(self):
        """Gets the user_group_id of this AssociateGroupUserGroupRequest.

        成员组 ID

        :return: The user_group_id of this AssociateGroupUserGroupRequest.
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """Sets the user_group_id of this AssociateGroupUserGroupRequest.

        成员组 ID

        :param user_group_id: The user_group_id of this AssociateGroupUserGroupRequest.
        :type user_group_id: str
        """
        self._user_group_id = user_group_id

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
        if not isinstance(other, AssociateGroupUserGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
