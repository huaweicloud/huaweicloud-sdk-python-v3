# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_access': 'MemberAccess',
        'group_access': 'MemberAccess'
    }

    attribute_map = {
        'repository_access': 'repository_access',
        'group_access': 'group_access'
    }

    def __init__(self, repository_access=None, group_access=None):
        r"""PermissionsDto

        The model defined in huaweicloud sdk

        :param repository_access: 
        :type repository_access: :class:`huaweicloudsdkcodehub.v4.MemberAccess`
        :param group_access: 
        :type group_access: :class:`huaweicloudsdkcodehub.v4.MemberAccess`
        """
        
        

        self._repository_access = None
        self._group_access = None
        self.discriminator = None

        if repository_access is not None:
            self.repository_access = repository_access
        if group_access is not None:
            self.group_access = group_access

    @property
    def repository_access(self):
        r"""Gets the repository_access of this PermissionsDto.

        :return: The repository_access of this PermissionsDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.MemberAccess`
        """
        return self._repository_access

    @repository_access.setter
    def repository_access(self, repository_access):
        r"""Sets the repository_access of this PermissionsDto.

        :param repository_access: The repository_access of this PermissionsDto.
        :type repository_access: :class:`huaweicloudsdkcodehub.v4.MemberAccess`
        """
        self._repository_access = repository_access

    @property
    def group_access(self):
        r"""Gets the group_access of this PermissionsDto.

        :return: The group_access of this PermissionsDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.MemberAccess`
        """
        return self._group_access

    @group_access.setter
    def group_access(self, group_access):
        r"""Sets the group_access of this PermissionsDto.

        :param group_access: The group_access of this PermissionsDto.
        :type group_access: :class:`huaweicloudsdkcodehub.v4.MemberAccess`
        """
        self._group_access = group_access

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
        if not isinstance(other, PermissionsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
