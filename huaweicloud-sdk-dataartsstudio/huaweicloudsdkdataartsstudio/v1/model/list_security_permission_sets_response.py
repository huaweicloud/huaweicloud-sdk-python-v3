# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityPermissionSetsResponse(SdkResponse):

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
        'permission_sets': 'list[PermissionSet]'
    }

    attribute_map = {
        'total': 'total',
        'permission_sets': 'permission_sets'
    }

    def __init__(self, total=None, permission_sets=None):
        r"""ListSecurityPermissionSetsResponse

        The model defined in huaweicloud sdk

        :param total: 总条数
        :type total: int
        :param permission_sets: 权限集列表
        :type permission_sets: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionSet`]
        """
        
        super(ListSecurityPermissionSetsResponse, self).__init__()

        self._total = None
        self._permission_sets = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if permission_sets is not None:
            self.permission_sets = permission_sets

    @property
    def total(self):
        r"""Gets the total of this ListSecurityPermissionSetsResponse.

        总条数

        :return: The total of this ListSecurityPermissionSetsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSecurityPermissionSetsResponse.

        总条数

        :param total: The total of this ListSecurityPermissionSetsResponse.
        :type total: int
        """
        self._total = total

    @property
    def permission_sets(self):
        r"""Gets the permission_sets of this ListSecurityPermissionSetsResponse.

        权限集列表

        :return: The permission_sets of this ListSecurityPermissionSetsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionSet`]
        """
        return self._permission_sets

    @permission_sets.setter
    def permission_sets(self, permission_sets):
        r"""Sets the permission_sets of this ListSecurityPermissionSetsResponse.

        权限集列表

        :param permission_sets: The permission_sets of this ListSecurityPermissionSetsResponse.
        :type permission_sets: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionSet`]
        """
        self._permission_sets = permission_sets

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
        if not isinstance(other, ListSecurityPermissionSetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
