# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRolesForUserOnEnterpriseProjectResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'roles': 'list[RolesItem]'
    }

    attribute_map = {
        'roles': 'roles'
    }

    def __init__(self, roles=None):
        r"""ListRolesForUserOnEnterpriseProjectResponse

        The model defined in huaweicloud sdk

        :param roles: 角色列表。
        :type roles: list[:class:`huaweicloudsdkiam.v3.RolesItem`]
        """
        
        super(ListRolesForUserOnEnterpriseProjectResponse, self).__init__()

        self._roles = None
        self.discriminator = None

        if roles is not None:
            self.roles = roles

    @property
    def roles(self):
        r"""Gets the roles of this ListRolesForUserOnEnterpriseProjectResponse.

        角色列表。

        :return: The roles of this ListRolesForUserOnEnterpriseProjectResponse.
        :rtype: list[:class:`huaweicloudsdkiam.v3.RolesItem`]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        r"""Sets the roles of this ListRolesForUserOnEnterpriseProjectResponse.

        角色列表。

        :param roles: The roles of this ListRolesForUserOnEnterpriseProjectResponse.
        :type roles: list[:class:`huaweicloudsdkiam.v3.RolesItem`]
        """
        self._roles = roles

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
        if not isinstance(other, ListRolesForUserOnEnterpriseProjectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
