# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityPermissionSetMembersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'permission_set_members': 'list[PermissionSetMember]'
    }

    attribute_map = {
        'total': 'total',
        'permission_set_members': 'permission_set_members'
    }

    def __init__(self, total=None, permission_set_members=None):
        """ListSecurityPermissionSetMembersResponse

        The model defined in huaweicloud sdk

        :param total: 总条数
        :type total: int
        :param permission_set_members: 成员列表
        :type permission_set_members: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionSetMember`]
        """
        
        super(ListSecurityPermissionSetMembersResponse, self).__init__()

        self._total = None
        self._permission_set_members = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if permission_set_members is not None:
            self.permission_set_members = permission_set_members

    @property
    def total(self):
        """Gets the total of this ListSecurityPermissionSetMembersResponse.

        总条数

        :return: The total of this ListSecurityPermissionSetMembersResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListSecurityPermissionSetMembersResponse.

        总条数

        :param total: The total of this ListSecurityPermissionSetMembersResponse.
        :type total: int
        """
        self._total = total

    @property
    def permission_set_members(self):
        """Gets the permission_set_members of this ListSecurityPermissionSetMembersResponse.

        成员列表

        :return: The permission_set_members of this ListSecurityPermissionSetMembersResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionSetMember`]
        """
        return self._permission_set_members

    @permission_set_members.setter
    def permission_set_members(self, permission_set_members):
        """Sets the permission_set_members of this ListSecurityPermissionSetMembersResponse.

        成员列表

        :param permission_set_members: The permission_set_members of this ListSecurityPermissionSetMembersResponse.
        :type permission_set_members: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionSetMember`]
        """
        self._permission_set_members = permission_set_members

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
        if not isinstance(other, ListSecurityPermissionSetMembersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
