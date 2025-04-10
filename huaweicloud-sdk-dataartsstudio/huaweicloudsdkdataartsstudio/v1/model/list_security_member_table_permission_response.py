# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityMemberTablePermissionResponse(SdkResponse):

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
        'member_permission_list': 'list[MemberPermission]'
    }

    attribute_map = {
        'total': 'total',
        'member_permission_list': 'member_permission_list'
    }

    def __init__(self, total=None, member_permission_list=None):
        r"""ListSecurityMemberTablePermissionResponse

        The model defined in huaweicloud sdk

        :param total: 权限总数
        :type total: int
        :param member_permission_list: 成员权限列表（包含权限集的和权限审批）
        :type member_permission_list: list[:class:`huaweicloudsdkdataartsstudio.v1.MemberPermission`]
        """
        
        super(ListSecurityMemberTablePermissionResponse, self).__init__()

        self._total = None
        self._member_permission_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if member_permission_list is not None:
            self.member_permission_list = member_permission_list

    @property
    def total(self):
        r"""Gets the total of this ListSecurityMemberTablePermissionResponse.

        权限总数

        :return: The total of this ListSecurityMemberTablePermissionResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSecurityMemberTablePermissionResponse.

        权限总数

        :param total: The total of this ListSecurityMemberTablePermissionResponse.
        :type total: int
        """
        self._total = total

    @property
    def member_permission_list(self):
        r"""Gets the member_permission_list of this ListSecurityMemberTablePermissionResponse.

        成员权限列表（包含权限集的和权限审批）

        :return: The member_permission_list of this ListSecurityMemberTablePermissionResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.MemberPermission`]
        """
        return self._member_permission_list

    @member_permission_list.setter
    def member_permission_list(self, member_permission_list):
        r"""Sets the member_permission_list of this ListSecurityMemberTablePermissionResponse.

        成员权限列表（包含权限集的和权限审批）

        :param member_permission_list: The member_permission_list of this ListSecurityMemberTablePermissionResponse.
        :type member_permission_list: list[:class:`huaweicloudsdkdataartsstudio.v1.MemberPermission`]
        """
        self._member_permission_list = member_permission_list

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
        if not isinstance(other, ListSecurityMemberTablePermissionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
