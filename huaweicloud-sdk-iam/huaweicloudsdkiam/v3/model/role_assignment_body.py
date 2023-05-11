# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoleAssignmentBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user': 'RoleUserAssignmentId',
        'role': 'RoleAssignmentId',
        'group': 'RoleGroupAssignmentId',
        'agency': 'RoleAgencyAssignmentId',
        'scope': 'RoleAssignmentScope',
        'is_inherited': 'bool'
    }

    attribute_map = {
        'user': 'user',
        'role': 'role',
        'group': 'group',
        'agency': 'agency',
        'scope': 'scope',
        'is_inherited': 'is_inherited'
    }

    def __init__(self, user=None, role=None, group=None, agency=None, scope=None, is_inherited=None):
        """RoleAssignmentBody

        The model defined in huaweicloud sdk

        :param user: 
        :type user: :class:`huaweicloudsdkiam.v3.RoleUserAssignmentId`
        :param role: 
        :type role: :class:`huaweicloudsdkiam.v3.RoleAssignmentId`
        :param group: 
        :type group: :class:`huaweicloudsdkiam.v3.RoleGroupAssignmentId`
        :param agency: 
        :type agency: :class:`huaweicloudsdkiam.v3.RoleAgencyAssignmentId`
        :param scope: 
        :type scope: :class:`huaweicloudsdkiam.v3.RoleAssignmentScope`
        :param is_inherited: 是否基于所有项目授权。
        :type is_inherited: bool
        """
        
        

        self._user = None
        self._role = None
        self._group = None
        self._agency = None
        self._scope = None
        self._is_inherited = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if role is not None:
            self.role = role
        if group is not None:
            self.group = group
        if agency is not None:
            self.agency = agency
        if scope is not None:
            self.scope = scope
        if is_inherited is not None:
            self.is_inherited = is_inherited

    @property
    def user(self):
        """Gets the user of this RoleAssignmentBody.

        :return: The user of this RoleAssignmentBody.
        :rtype: :class:`huaweicloudsdkiam.v3.RoleUserAssignmentId`
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this RoleAssignmentBody.

        :param user: The user of this RoleAssignmentBody.
        :type user: :class:`huaweicloudsdkiam.v3.RoleUserAssignmentId`
        """
        self._user = user

    @property
    def role(self):
        """Gets the role of this RoleAssignmentBody.

        :return: The role of this RoleAssignmentBody.
        :rtype: :class:`huaweicloudsdkiam.v3.RoleAssignmentId`
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this RoleAssignmentBody.

        :param role: The role of this RoleAssignmentBody.
        :type role: :class:`huaweicloudsdkiam.v3.RoleAssignmentId`
        """
        self._role = role

    @property
    def group(self):
        """Gets the group of this RoleAssignmentBody.

        :return: The group of this RoleAssignmentBody.
        :rtype: :class:`huaweicloudsdkiam.v3.RoleGroupAssignmentId`
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this RoleAssignmentBody.

        :param group: The group of this RoleAssignmentBody.
        :type group: :class:`huaweicloudsdkiam.v3.RoleGroupAssignmentId`
        """
        self._group = group

    @property
    def agency(self):
        """Gets the agency of this RoleAssignmentBody.

        :return: The agency of this RoleAssignmentBody.
        :rtype: :class:`huaweicloudsdkiam.v3.RoleAgencyAssignmentId`
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """Sets the agency of this RoleAssignmentBody.

        :param agency: The agency of this RoleAssignmentBody.
        :type agency: :class:`huaweicloudsdkiam.v3.RoleAgencyAssignmentId`
        """
        self._agency = agency

    @property
    def scope(self):
        """Gets the scope of this RoleAssignmentBody.

        :return: The scope of this RoleAssignmentBody.
        :rtype: :class:`huaweicloudsdkiam.v3.RoleAssignmentScope`
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this RoleAssignmentBody.

        :param scope: The scope of this RoleAssignmentBody.
        :type scope: :class:`huaweicloudsdkiam.v3.RoleAssignmentScope`
        """
        self._scope = scope

    @property
    def is_inherited(self):
        """Gets the is_inherited of this RoleAssignmentBody.

        是否基于所有项目授权。

        :return: The is_inherited of this RoleAssignmentBody.
        :rtype: bool
        """
        return self._is_inherited

    @is_inherited.setter
    def is_inherited(self, is_inherited):
        """Sets the is_inherited of this RoleAssignmentBody.

        是否基于所有项目授权。

        :param is_inherited: The is_inherited of this RoleAssignmentBody.
        :type is_inherited: bool
        """
        self._is_inherited = is_inherited

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
        if not isinstance(other, RoleAssignmentBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
