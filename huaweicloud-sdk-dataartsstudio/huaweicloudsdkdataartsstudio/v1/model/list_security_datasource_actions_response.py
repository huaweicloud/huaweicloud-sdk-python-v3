# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityDatasourceActionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission_actions': 'list[PermissionActions]'
    }

    attribute_map = {
        'permission_actions': 'permission_actions'
    }

    def __init__(self, permission_actions=None):
        """ListSecurityDatasourceActionsResponse

        The model defined in huaweicloud sdk

        :param permission_actions: 权限操作列表
        :type permission_actions: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionActions`]
        """
        
        super(ListSecurityDatasourceActionsResponse, self).__init__()

        self._permission_actions = None
        self.discriminator = None

        if permission_actions is not None:
            self.permission_actions = permission_actions

    @property
    def permission_actions(self):
        """Gets the permission_actions of this ListSecurityDatasourceActionsResponse.

        权限操作列表

        :return: The permission_actions of this ListSecurityDatasourceActionsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionActions`]
        """
        return self._permission_actions

    @permission_actions.setter
    def permission_actions(self, permission_actions):
        """Sets the permission_actions of this ListSecurityDatasourceActionsResponse.

        权限操作列表

        :param permission_actions: The permission_actions of this ListSecurityDatasourceActionsResponse.
        :type permission_actions: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionActions`]
        """
        self._permission_actions = permission_actions

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
        if not isinstance(other, ListSecurityDatasourceActionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
