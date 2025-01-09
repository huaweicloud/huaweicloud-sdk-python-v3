# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAssignAppAuthorizationsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_ids': 'list[str]',
        'authorization_type': 'AssignType',
        'users': 'list[AccountInfo]',
        'del_users': 'list[AccountInfo]'
    }

    attribute_map = {
        'app_ids': 'app_ids',
        'authorization_type': 'authorization_type',
        'users': 'users',
        'del_users': 'del_users'
    }

    def __init__(self, app_ids=None, authorization_type=None, users=None, del_users=None):
        """BatchAssignAppAuthorizationsReq

        The model defined in huaweicloud sdk

        :param app_ids: 批量唯一标识请求列表，一次请求数量区间 [1, 20]。
        :type app_ids: list[str]
        :param authorization_type: 
        :type authorization_type: :class:`huaweicloudsdkworkspace.v2.AssignType`
        :param users: 新增授权用户列表，一次请求数量区间 [0, 100]。
        :type users: list[:class:`huaweicloudsdkworkspace.v2.AccountInfo`]
        :param del_users: 取消授权用户列表，一次请求数量区间 [0, 100]。
        :type del_users: list[:class:`huaweicloudsdkworkspace.v2.AccountInfo`]
        """
        
        

        self._app_ids = None
        self._authorization_type = None
        self._users = None
        self._del_users = None
        self.discriminator = None

        self.app_ids = app_ids
        self.authorization_type = authorization_type
        if users is not None:
            self.users = users
        if del_users is not None:
            self.del_users = del_users

    @property
    def app_ids(self):
        """Gets the app_ids of this BatchAssignAppAuthorizationsReq.

        批量唯一标识请求列表，一次请求数量区间 [1, 20]。

        :return: The app_ids of this BatchAssignAppAuthorizationsReq.
        :rtype: list[str]
        """
        return self._app_ids

    @app_ids.setter
    def app_ids(self, app_ids):
        """Sets the app_ids of this BatchAssignAppAuthorizationsReq.

        批量唯一标识请求列表，一次请求数量区间 [1, 20]。

        :param app_ids: The app_ids of this BatchAssignAppAuthorizationsReq.
        :type app_ids: list[str]
        """
        self._app_ids = app_ids

    @property
    def authorization_type(self):
        """Gets the authorization_type of this BatchAssignAppAuthorizationsReq.

        :return: The authorization_type of this BatchAssignAppAuthorizationsReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AssignType`
        """
        return self._authorization_type

    @authorization_type.setter
    def authorization_type(self, authorization_type):
        """Sets the authorization_type of this BatchAssignAppAuthorizationsReq.

        :param authorization_type: The authorization_type of this BatchAssignAppAuthorizationsReq.
        :type authorization_type: :class:`huaweicloudsdkworkspace.v2.AssignType`
        """
        self._authorization_type = authorization_type

    @property
    def users(self):
        """Gets the users of this BatchAssignAppAuthorizationsReq.

        新增授权用户列表，一次请求数量区间 [0, 100]。

        :return: The users of this BatchAssignAppAuthorizationsReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AccountInfo`]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this BatchAssignAppAuthorizationsReq.

        新增授权用户列表，一次请求数量区间 [0, 100]。

        :param users: The users of this BatchAssignAppAuthorizationsReq.
        :type users: list[:class:`huaweicloudsdkworkspace.v2.AccountInfo`]
        """
        self._users = users

    @property
    def del_users(self):
        """Gets the del_users of this BatchAssignAppAuthorizationsReq.

        取消授权用户列表，一次请求数量区间 [0, 100]。

        :return: The del_users of this BatchAssignAppAuthorizationsReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AccountInfo`]
        """
        return self._del_users

    @del_users.setter
    def del_users(self, del_users):
        """Sets the del_users of this BatchAssignAppAuthorizationsReq.

        取消授权用户列表，一次请求数量区间 [0, 100]。

        :param del_users: The del_users of this BatchAssignAppAuthorizationsReq.
        :type del_users: list[:class:`huaweicloudsdkworkspace.v2.AccountInfo`]
        """
        self._del_users = del_users

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
        if not isinstance(other, BatchAssignAppAuthorizationsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
