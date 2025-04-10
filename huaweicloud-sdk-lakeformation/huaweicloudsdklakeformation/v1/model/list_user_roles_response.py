# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserRolesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'roles': 'list[Role]',
        'page_info': 'PagedInfo'
    }

    attribute_map = {
        'roles': 'roles',
        'page_info': 'page_info'
    }

    def __init__(self, roles=None, page_info=None):
        r"""ListUserRolesResponse

        The model defined in huaweicloud sdk

        :param roles: 
        :type roles: list[:class:`huaweicloudsdklakeformation.v1.Role`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
        """
        
        super(ListUserRolesResponse, self).__init__()

        self._roles = None
        self._page_info = None
        self.discriminator = None

        if roles is not None:
            self.roles = roles
        if page_info is not None:
            self.page_info = page_info

    @property
    def roles(self):
        r"""Gets the roles of this ListUserRolesResponse.

        :return: The roles of this ListUserRolesResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.Role`]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        r"""Sets the roles of this ListUserRolesResponse.

        :param roles: The roles of this ListUserRolesResponse.
        :type roles: list[:class:`huaweicloudsdklakeformation.v1.Role`]
        """
        self._roles = roles

    @property
    def page_info(self):
        r"""Gets the page_info of this ListUserRolesResponse.

        :return: The page_info of this ListUserRolesResponse.
        :rtype: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListUserRolesResponse.

        :param page_info: The page_info of this ListUserRolesResponse.
        :type page_info: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
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
        if not isinstance(other, ListUserRolesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
