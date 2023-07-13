# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthorizeResourceRequestBody:

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
        'project_id': 'str',
        'action': 'str',
        'privileges': 'list[Privilege]'
    }

    attribute_map = {
        'user_name': 'user_name',
        'project_id': 'projectId',
        'action': 'action',
        'privileges': 'privileges'
    }

    def __init__(self, user_name=None, project_id=None, action=None, privileges=None):
        """AuthorizeResourceRequestBody

        The model defined in huaweicloud sdk

        :param user_name: 被赋权的用户名称，该用户将有权访问指定的DLI资源权限，被收回或者更新访问权限。
        :type user_name: str
        :param project_id: 被赋权的项目ID，数据赋权给其他项目后，该项目的管理员将 有权访问指定的DLI资源权限，被收回或者更新访问权限。
        :type project_id: str
        :param action: 指定赋权或回收。值为：grant，revoke或update。  说明：当用户同时拥有grant和revoke权限的时候才有权限使用update操作。
        :type action: str
        :param privileges: 赋权信息。具体参数请参考Privilege参数。
        :type privileges: list[:class:`huaweicloudsdkdli.v1.Privilege`]
        """
        
        

        self._user_name = None
        self._project_id = None
        self._action = None
        self._privileges = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if project_id is not None:
            self.project_id = project_id
        self.action = action
        self.privileges = privileges

    @property
    def user_name(self):
        """Gets the user_name of this AuthorizeResourceRequestBody.

        被赋权的用户名称，该用户将有权访问指定的DLI资源权限，被收回或者更新访问权限。

        :return: The user_name of this AuthorizeResourceRequestBody.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AuthorizeResourceRequestBody.

        被赋权的用户名称，该用户将有权访问指定的DLI资源权限，被收回或者更新访问权限。

        :param user_name: The user_name of this AuthorizeResourceRequestBody.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def project_id(self):
        """Gets the project_id of this AuthorizeResourceRequestBody.

        被赋权的项目ID，数据赋权给其他项目后，该项目的管理员将 有权访问指定的DLI资源权限，被收回或者更新访问权限。

        :return: The project_id of this AuthorizeResourceRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AuthorizeResourceRequestBody.

        被赋权的项目ID，数据赋权给其他项目后，该项目的管理员将 有权访问指定的DLI资源权限，被收回或者更新访问权限。

        :param project_id: The project_id of this AuthorizeResourceRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def action(self):
        """Gets the action of this AuthorizeResourceRequestBody.

        指定赋权或回收。值为：grant，revoke或update。  说明：当用户同时拥有grant和revoke权限的时候才有权限使用update操作。

        :return: The action of this AuthorizeResourceRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AuthorizeResourceRequestBody.

        指定赋权或回收。值为：grant，revoke或update。  说明：当用户同时拥有grant和revoke权限的时候才有权限使用update操作。

        :param action: The action of this AuthorizeResourceRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def privileges(self):
        """Gets the privileges of this AuthorizeResourceRequestBody.

        赋权信息。具体参数请参考Privilege参数。

        :return: The privileges of this AuthorizeResourceRequestBody.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Privilege`]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this AuthorizeResourceRequestBody.

        赋权信息。具体参数请参考Privilege参数。

        :param privileges: The privileges of this AuthorizeResourceRequestBody.
        :type privileges: list[:class:`huaweicloudsdkdli.v1.Privilege`]
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
        if not isinstance(other, AuthorizeResourceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
