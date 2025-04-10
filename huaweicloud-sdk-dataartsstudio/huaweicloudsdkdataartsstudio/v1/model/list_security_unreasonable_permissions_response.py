# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityUnreasonablePermissionsResponse(SdkResponse):

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
        'unreasonable_permissions': 'list[DiagnosePermissionDetail]'
    }

    attribute_map = {
        'total': 'total',
        'unreasonable_permissions': 'unreasonable_permissions'
    }

    def __init__(self, total=None, unreasonable_permissions=None):
        r"""ListSecurityUnreasonablePermissionsResponse

        The model defined in huaweicloud sdk

        :param total: 不合理权限配置总条数。
        :type total: int
        :param unreasonable_permissions: 不合理权限配置列表。
        :type unreasonable_permissions: list[:class:`huaweicloudsdkdataartsstudio.v1.DiagnosePermissionDetail`]
        """
        
        super(ListSecurityUnreasonablePermissionsResponse, self).__init__()

        self._total = None
        self._unreasonable_permissions = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if unreasonable_permissions is not None:
            self.unreasonable_permissions = unreasonable_permissions

    @property
    def total(self):
        r"""Gets the total of this ListSecurityUnreasonablePermissionsResponse.

        不合理权限配置总条数。

        :return: The total of this ListSecurityUnreasonablePermissionsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSecurityUnreasonablePermissionsResponse.

        不合理权限配置总条数。

        :param total: The total of this ListSecurityUnreasonablePermissionsResponse.
        :type total: int
        """
        self._total = total

    @property
    def unreasonable_permissions(self):
        r"""Gets the unreasonable_permissions of this ListSecurityUnreasonablePermissionsResponse.

        不合理权限配置列表。

        :return: The unreasonable_permissions of this ListSecurityUnreasonablePermissionsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DiagnosePermissionDetail`]
        """
        return self._unreasonable_permissions

    @unreasonable_permissions.setter
    def unreasonable_permissions(self, unreasonable_permissions):
        r"""Sets the unreasonable_permissions of this ListSecurityUnreasonablePermissionsResponse.

        不合理权限配置列表。

        :param unreasonable_permissions: The unreasonable_permissions of this ListSecurityUnreasonablePermissionsResponse.
        :type unreasonable_permissions: list[:class:`huaweicloudsdkdataartsstudio.v1.DiagnosePermissionDetail`]
        """
        self._unreasonable_permissions = unreasonable_permissions

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
        if not isinstance(other, ListSecurityUnreasonablePermissionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
