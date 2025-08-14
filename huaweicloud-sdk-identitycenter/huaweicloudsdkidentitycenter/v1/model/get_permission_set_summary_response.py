# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetPermissionSetSummaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission_sets': 'int',
        'permission_sets_quota': 'int',
        'permission_policy_count_quota': 'int',
        'permission_policy_quota': 'int'
    }

    attribute_map = {
        'permission_sets': 'permission_sets',
        'permission_sets_quota': 'permission_sets_quota',
        'permission_policy_count_quota': 'permission_policy_count_quota',
        'permission_policy_quota': 'permission_policy_quota'
    }

    def __init__(self, permission_sets=None, permission_sets_quota=None, permission_policy_count_quota=None, permission_policy_quota=None):
        r"""GetPermissionSetSummaryResponse

        The model defined in huaweicloud sdk

        :param permission_sets: 已创建的权限集数量
        :type permission_sets: int
        :param permission_sets_quota: 权限集配额
        :type permission_sets_quota: int
        :param permission_policy_count_quota: 允许权限集可绑定的策略配额
        :type permission_policy_count_quota: int
        :param permission_policy_quota: 允许权限集可绑定的身份策略配额
        :type permission_policy_quota: int
        """
        
        super(GetPermissionSetSummaryResponse, self).__init__()

        self._permission_sets = None
        self._permission_sets_quota = None
        self._permission_policy_count_quota = None
        self._permission_policy_quota = None
        self.discriminator = None

        if permission_sets is not None:
            self.permission_sets = permission_sets
        if permission_sets_quota is not None:
            self.permission_sets_quota = permission_sets_quota
        if permission_policy_count_quota is not None:
            self.permission_policy_count_quota = permission_policy_count_quota
        if permission_policy_quota is not None:
            self.permission_policy_quota = permission_policy_quota

    @property
    def permission_sets(self):
        r"""Gets the permission_sets of this GetPermissionSetSummaryResponse.

        已创建的权限集数量

        :return: The permission_sets of this GetPermissionSetSummaryResponse.
        :rtype: int
        """
        return self._permission_sets

    @permission_sets.setter
    def permission_sets(self, permission_sets):
        r"""Sets the permission_sets of this GetPermissionSetSummaryResponse.

        已创建的权限集数量

        :param permission_sets: The permission_sets of this GetPermissionSetSummaryResponse.
        :type permission_sets: int
        """
        self._permission_sets = permission_sets

    @property
    def permission_sets_quota(self):
        r"""Gets the permission_sets_quota of this GetPermissionSetSummaryResponse.

        权限集配额

        :return: The permission_sets_quota of this GetPermissionSetSummaryResponse.
        :rtype: int
        """
        return self._permission_sets_quota

    @permission_sets_quota.setter
    def permission_sets_quota(self, permission_sets_quota):
        r"""Sets the permission_sets_quota of this GetPermissionSetSummaryResponse.

        权限集配额

        :param permission_sets_quota: The permission_sets_quota of this GetPermissionSetSummaryResponse.
        :type permission_sets_quota: int
        """
        self._permission_sets_quota = permission_sets_quota

    @property
    def permission_policy_count_quota(self):
        r"""Gets the permission_policy_count_quota of this GetPermissionSetSummaryResponse.

        允许权限集可绑定的策略配额

        :return: The permission_policy_count_quota of this GetPermissionSetSummaryResponse.
        :rtype: int
        """
        return self._permission_policy_count_quota

    @permission_policy_count_quota.setter
    def permission_policy_count_quota(self, permission_policy_count_quota):
        r"""Sets the permission_policy_count_quota of this GetPermissionSetSummaryResponse.

        允许权限集可绑定的策略配额

        :param permission_policy_count_quota: The permission_policy_count_quota of this GetPermissionSetSummaryResponse.
        :type permission_policy_count_quota: int
        """
        self._permission_policy_count_quota = permission_policy_count_quota

    @property
    def permission_policy_quota(self):
        r"""Gets the permission_policy_quota of this GetPermissionSetSummaryResponse.

        允许权限集可绑定的身份策略配额

        :return: The permission_policy_quota of this GetPermissionSetSummaryResponse.
        :rtype: int
        """
        return self._permission_policy_quota

    @permission_policy_quota.setter
    def permission_policy_quota(self, permission_policy_quota):
        r"""Sets the permission_policy_quota of this GetPermissionSetSummaryResponse.

        允许权限集可绑定的身份策略配额

        :param permission_policy_quota: The permission_policy_quota of this GetPermissionSetSummaryResponse.
        :type permission_policy_quota: int
        """
        self._permission_policy_quota = permission_policy_quota

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
        if not isinstance(other, GetPermissionSetSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
