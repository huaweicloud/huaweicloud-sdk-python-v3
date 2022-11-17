# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GrantDataPermissionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'action': 'str',
        'privileges': 'list[GrantDataPermissionRespPrivilege]'
    }

    attribute_map = {
        'user_name': 'user_name',
        'action': 'action',
        'privileges': 'privileges'
    }

    def __init__(self, user_name=None, action=None, privileges=None):
        """GrantDataPermissionReq

        The model defined in huaweicloud sdk

        :param user_name: 被赋权的用户名称，该用户将有权访问指定的数据库或数据表，被收回或者更新访问权限。
        :type user_name: str
        :param action: 指定赋权或回收。值为：grant，revoke或update。 说明： 当用户同时拥有grant和revoke权限的时候才有权限使用update操作。
        :type action: str
        :param privileges: 赋权信息。
        :type privileges: list[:class:`huaweicloudsdkdli.v1.GrantDataPermissionRespPrivilege`]
        """
        
        

        self._user_name = None
        self._action = None
        self._privileges = None
        self.discriminator = None

        self.user_name = user_name
        self.action = action
        self.privileges = privileges

    @property
    def user_name(self):
        """Gets the user_name of this GrantDataPermissionReq.

        被赋权的用户名称，该用户将有权访问指定的数据库或数据表，被收回或者更新访问权限。

        :return: The user_name of this GrantDataPermissionReq.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this GrantDataPermissionReq.

        被赋权的用户名称，该用户将有权访问指定的数据库或数据表，被收回或者更新访问权限。

        :param user_name: The user_name of this GrantDataPermissionReq.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def action(self):
        """Gets the action of this GrantDataPermissionReq.

        指定赋权或回收。值为：grant，revoke或update。 说明： 当用户同时拥有grant和revoke权限的时候才有权限使用update操作。

        :return: The action of this GrantDataPermissionReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this GrantDataPermissionReq.

        指定赋权或回收。值为：grant，revoke或update。 说明： 当用户同时拥有grant和revoke权限的时候才有权限使用update操作。

        :param action: The action of this GrantDataPermissionReq.
        :type action: str
        """
        self._action = action

    @property
    def privileges(self):
        """Gets the privileges of this GrantDataPermissionReq.

        赋权信息。

        :return: The privileges of this GrantDataPermissionReq.
        :rtype: list[:class:`huaweicloudsdkdli.v1.GrantDataPermissionRespPrivilege`]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this GrantDataPermissionReq.

        赋权信息。

        :param privileges: The privileges of this GrantDataPermissionReq.
        :type privileges: list[:class:`huaweicloudsdkdli.v1.GrantDataPermissionRespPrivilege`]
        """
        self._privileges = privileges

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
        if not isinstance(other, GrantDataPermissionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
