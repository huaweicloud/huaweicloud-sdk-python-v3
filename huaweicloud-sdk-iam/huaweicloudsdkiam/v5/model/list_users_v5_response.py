# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUsersV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'users': 'list[User]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'users': 'users',
        'page_info': 'page_info'
    }

    def __init__(self, users=None, page_info=None):
        r"""ListUsersV5Response

        The model defined in huaweicloud sdk

        :param users: IAM用户列表。
        :type users: list[:class:`huaweicloudsdkiam.v5.User`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        
        super(ListUsersV5Response, self).__init__()

        self._users = None
        self._page_info = None
        self.discriminator = None

        if users is not None:
            self.users = users
        if page_info is not None:
            self.page_info = page_info

    @property
    def users(self):
        r"""Gets the users of this ListUsersV5Response.

        IAM用户列表。

        :return: The users of this ListUsersV5Response.
        :rtype: list[:class:`huaweicloudsdkiam.v5.User`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this ListUsersV5Response.

        IAM用户列表。

        :param users: The users of this ListUsersV5Response.
        :type users: list[:class:`huaweicloudsdkiam.v5.User`]
        """
        self._users = users

    @property
    def page_info(self):
        r"""Gets the page_info of this ListUsersV5Response.

        :return: The page_info of this ListUsersV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListUsersV5Response.

        :param page_info: The page_info of this ListUsersV5Response.
        :type page_info: :class:`huaweicloudsdkiam.v5.PageInfo`
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
        if not isinstance(other, ListUsersV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
