# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLandingZoneIdentityCenterResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identity_store_id': 'str',
        'user_portal_url': 'str',
        'permission_sets': 'list[PermissionSet]',
        'groups': 'list[IdentityCenterGroup]'
    }

    attribute_map = {
        'identity_store_id': 'identity_store_id',
        'user_portal_url': 'user_portal_url',
        'permission_sets': 'permission_sets',
        'groups': 'groups'
    }

    def __init__(self, identity_store_id=None, user_portal_url=None, permission_sets=None, groups=None):
        r"""ShowLandingZoneIdentityCenterResponse

        The model defined in huaweicloud sdk

        :param identity_store_id: Identity Center目录ID。
        :type identity_store_id: str
        :param user_portal_url: Identity Center登录URL。
        :type user_portal_url: str
        :param permission_sets: Identity Center权限集。
        :type permission_sets: list[:class:`huaweicloudsdkrgc.v1.PermissionSet`]
        :param groups: Identity Center用户组。
        :type groups: list[:class:`huaweicloudsdkrgc.v1.IdentityCenterGroup`]
        """
        
        super(ShowLandingZoneIdentityCenterResponse, self).__init__()

        self._identity_store_id = None
        self._user_portal_url = None
        self._permission_sets = None
        self._groups = None
        self.discriminator = None

        if identity_store_id is not None:
            self.identity_store_id = identity_store_id
        if user_portal_url is not None:
            self.user_portal_url = user_portal_url
        if permission_sets is not None:
            self.permission_sets = permission_sets
        if groups is not None:
            self.groups = groups

    @property
    def identity_store_id(self):
        r"""Gets the identity_store_id of this ShowLandingZoneIdentityCenterResponse.

        Identity Center目录ID。

        :return: The identity_store_id of this ShowLandingZoneIdentityCenterResponse.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        r"""Sets the identity_store_id of this ShowLandingZoneIdentityCenterResponse.

        Identity Center目录ID。

        :param identity_store_id: The identity_store_id of this ShowLandingZoneIdentityCenterResponse.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def user_portal_url(self):
        r"""Gets the user_portal_url of this ShowLandingZoneIdentityCenterResponse.

        Identity Center登录URL。

        :return: The user_portal_url of this ShowLandingZoneIdentityCenterResponse.
        :rtype: str
        """
        return self._user_portal_url

    @user_portal_url.setter
    def user_portal_url(self, user_portal_url):
        r"""Sets the user_portal_url of this ShowLandingZoneIdentityCenterResponse.

        Identity Center登录URL。

        :param user_portal_url: The user_portal_url of this ShowLandingZoneIdentityCenterResponse.
        :type user_portal_url: str
        """
        self._user_portal_url = user_portal_url

    @property
    def permission_sets(self):
        r"""Gets the permission_sets of this ShowLandingZoneIdentityCenterResponse.

        Identity Center权限集。

        :return: The permission_sets of this ShowLandingZoneIdentityCenterResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.PermissionSet`]
        """
        return self._permission_sets

    @permission_sets.setter
    def permission_sets(self, permission_sets):
        r"""Sets the permission_sets of this ShowLandingZoneIdentityCenterResponse.

        Identity Center权限集。

        :param permission_sets: The permission_sets of this ShowLandingZoneIdentityCenterResponse.
        :type permission_sets: list[:class:`huaweicloudsdkrgc.v1.PermissionSet`]
        """
        self._permission_sets = permission_sets

    @property
    def groups(self):
        r"""Gets the groups of this ShowLandingZoneIdentityCenterResponse.

        Identity Center用户组。

        :return: The groups of this ShowLandingZoneIdentityCenterResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.IdentityCenterGroup`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this ShowLandingZoneIdentityCenterResponse.

        Identity Center用户组。

        :param groups: The groups of this ShowLandingZoneIdentityCenterResponse.
        :type groups: list[:class:`huaweicloudsdkrgc.v1.IdentityCenterGroup`]
        """
        self._groups = groups

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
        if not isinstance(other, ShowLandingZoneIdentityCenterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
