# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAutoInstallAppsReq:

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
        'assign_scope': 'AssignType',
        'users': 'list[AccountInfo]'
    }

    attribute_map = {
        'app_ids': 'app_ids',
        'assign_scope': 'assign_scope',
        'users': 'users'
    }

    def __init__(self, app_ids=None, assign_scope=None, users=None):
        r"""BatchAutoInstallAppsReq

        The model defined in huaweicloud sdk

        :param app_ids: 批量唯一标识请求列表，一次请求数量区间 [1, 50]。
        :type app_ids: list[str]
        :param assign_scope: 
        :type assign_scope: :class:`huaweicloudsdkworkspace.v2.AssignType`
        :param users: 用户列表，一次请求数量区间 [1, 50]。
        :type users: list[:class:`huaweicloudsdkworkspace.v2.AccountInfo`]
        """
        
        

        self._app_ids = None
        self._assign_scope = None
        self._users = None
        self.discriminator = None

        self.app_ids = app_ids
        self.assign_scope = assign_scope
        if users is not None:
            self.users = users

    @property
    def app_ids(self):
        r"""Gets the app_ids of this BatchAutoInstallAppsReq.

        批量唯一标识请求列表，一次请求数量区间 [1, 50]。

        :return: The app_ids of this BatchAutoInstallAppsReq.
        :rtype: list[str]
        """
        return self._app_ids

    @app_ids.setter
    def app_ids(self, app_ids):
        r"""Sets the app_ids of this BatchAutoInstallAppsReq.

        批量唯一标识请求列表，一次请求数量区间 [1, 50]。

        :param app_ids: The app_ids of this BatchAutoInstallAppsReq.
        :type app_ids: list[str]
        """
        self._app_ids = app_ids

    @property
    def assign_scope(self):
        r"""Gets the assign_scope of this BatchAutoInstallAppsReq.

        :return: The assign_scope of this BatchAutoInstallAppsReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AssignType`
        """
        return self._assign_scope

    @assign_scope.setter
    def assign_scope(self, assign_scope):
        r"""Sets the assign_scope of this BatchAutoInstallAppsReq.

        :param assign_scope: The assign_scope of this BatchAutoInstallAppsReq.
        :type assign_scope: :class:`huaweicloudsdkworkspace.v2.AssignType`
        """
        self._assign_scope = assign_scope

    @property
    def users(self):
        r"""Gets the users of this BatchAutoInstallAppsReq.

        用户列表，一次请求数量区间 [1, 50]。

        :return: The users of this BatchAutoInstallAppsReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AccountInfo`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this BatchAutoInstallAppsReq.

        用户列表，一次请求数量区间 [1, 50]。

        :param users: The users of this BatchAutoInstallAppsReq.
        :type users: list[:class:`huaweicloudsdkworkspace.v2.AccountInfo`]
        """
        self._users = users

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
        if not isinstance(other, BatchAutoInstallAppsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
