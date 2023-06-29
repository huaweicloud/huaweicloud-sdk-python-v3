# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPermissionSetsProvisionedToAccountResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission_sets': 'list[str]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'permission_sets': 'permission_sets',
        'page_info': 'page_info'
    }

    def __init__(self, permission_sets=None, page_info=None):
        """ListPermissionSetsProvisionedToAccountResponse

        The model defined in huaweicloud sdk

        :param permission_sets: 权限集列表
        :type permission_sets: list[str]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        
        super(ListPermissionSetsProvisionedToAccountResponse, self).__init__()

        self._permission_sets = None
        self._page_info = None
        self.discriminator = None

        if permission_sets is not None:
            self.permission_sets = permission_sets
        if page_info is not None:
            self.page_info = page_info

    @property
    def permission_sets(self):
        """Gets the permission_sets of this ListPermissionSetsProvisionedToAccountResponse.

        权限集列表

        :return: The permission_sets of this ListPermissionSetsProvisionedToAccountResponse.
        :rtype: list[str]
        """
        return self._permission_sets

    @permission_sets.setter
    def permission_sets(self, permission_sets):
        """Sets the permission_sets of this ListPermissionSetsProvisionedToAccountResponse.

        权限集列表

        :param permission_sets: The permission_sets of this ListPermissionSetsProvisionedToAccountResponse.
        :type permission_sets: list[str]
        """
        self._permission_sets = permission_sets

    @property
    def page_info(self):
        """Gets the page_info of this ListPermissionSetsProvisionedToAccountResponse.

        :return: The page_info of this ListPermissionSetsProvisionedToAccountResponse.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListPermissionSetsProvisionedToAccountResponse.

        :param page_info: The page_info of this ListPermissionSetsProvisionedToAccountResponse.
        :type page_info: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListPermissionSetsProvisionedToAccountResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
