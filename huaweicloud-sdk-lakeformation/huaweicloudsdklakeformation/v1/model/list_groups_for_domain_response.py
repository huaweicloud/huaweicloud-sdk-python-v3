# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupsForDomainResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_group': 'list[UserGroup]',
        'page_info': 'PagedInfo'
    }

    attribute_map = {
        'user_group': 'user_group',
        'page_info': 'page_info'
    }

    def __init__(self, user_group=None, page_info=None):
        """ListGroupsForDomainResponse

        The model defined in huaweicloud sdk

        :param user_group: 
        :type user_group: list[:class:`huaweicloudsdklakeformation.v1.UserGroup`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
        """
        
        super(ListGroupsForDomainResponse, self).__init__()

        self._user_group = None
        self._page_info = None
        self.discriminator = None

        if user_group is not None:
            self.user_group = user_group
        if page_info is not None:
            self.page_info = page_info

    @property
    def user_group(self):
        """Gets the user_group of this ListGroupsForDomainResponse.

        :return: The user_group of this ListGroupsForDomainResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.UserGroup`]
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        """Sets the user_group of this ListGroupsForDomainResponse.

        :param user_group: The user_group of this ListGroupsForDomainResponse.
        :type user_group: list[:class:`huaweicloudsdklakeformation.v1.UserGroup`]
        """
        self._user_group = user_group

    @property
    def page_info(self):
        """Gets the page_info of this ListGroupsForDomainResponse.

        :return: The page_info of this ListGroupsForDomainResponse.
        :rtype: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListGroupsForDomainResponse.

        :param page_info: The page_info of this ListGroupsForDomainResponse.
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
        if not isinstance(other, ListGroupsForDomainResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
