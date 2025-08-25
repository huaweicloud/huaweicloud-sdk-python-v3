# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectProtectedBranchesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'search': 'str',
        'user_actions': 'bool',
        'view': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'offset': 'offset',
        'limit': 'limit',
        'search': 'search',
        'user_actions': 'user_actions',
        'view': 'view'
    }

    def __init__(self, project_id=None, offset=None, limit=None, search=None, user_actions=None, view=None):
        r"""ListProjectProtectedBranchesRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。
        :type project_id: str
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param search: **参数解释：** 保护分支名称。 **取值范围：** 字符串长度不少于1，不超过2000。
        :type search: str
        :param user_actions: **参数解释：** 是否使用actions权限点的返回内容。 **取值范围：** 字符串长度不少于1，不超过2000。
        :type user_actions: bool
        :param view: **参数解释：** 参数值只有simple ，意为使用简单模式，只返回名称。 **取值范围：** 字符串长度不少于1，不超过2000。
        :type view: str
        """
        
        

        self._project_id = None
        self._offset = None
        self._limit = None
        self._search = None
        self._user_actions = None
        self._view = None
        self.discriminator = None

        self.project_id = project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search is not None:
            self.search = search
        if user_actions is not None:
            self.user_actions = user_actions
        if view is not None:
            self.view = view

    @property
    def project_id(self):
        r"""Gets the project_id of this ListProjectProtectedBranchesRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :return: The project_id of this ListProjectProtectedBranchesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListProjectProtectedBranchesRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :param project_id: The project_id of this ListProjectProtectedBranchesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListProjectProtectedBranchesRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListProjectProtectedBranchesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListProjectProtectedBranchesRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListProjectProtectedBranchesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListProjectProtectedBranchesRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListProjectProtectedBranchesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListProjectProtectedBranchesRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListProjectProtectedBranchesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search(self):
        r"""Gets the search of this ListProjectProtectedBranchesRequest.

        **参数解释：** 保护分支名称。 **取值范围：** 字符串长度不少于1，不超过2000。

        :return: The search of this ListProjectProtectedBranchesRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListProjectProtectedBranchesRequest.

        **参数解释：** 保护分支名称。 **取值范围：** 字符串长度不少于1，不超过2000。

        :param search: The search of this ListProjectProtectedBranchesRequest.
        :type search: str
        """
        self._search = search

    @property
    def user_actions(self):
        r"""Gets the user_actions of this ListProjectProtectedBranchesRequest.

        **参数解释：** 是否使用actions权限点的返回内容。 **取值范围：** 字符串长度不少于1，不超过2000。

        :return: The user_actions of this ListProjectProtectedBranchesRequest.
        :rtype: bool
        """
        return self._user_actions

    @user_actions.setter
    def user_actions(self, user_actions):
        r"""Sets the user_actions of this ListProjectProtectedBranchesRequest.

        **参数解释：** 是否使用actions权限点的返回内容。 **取值范围：** 字符串长度不少于1，不超过2000。

        :param user_actions: The user_actions of this ListProjectProtectedBranchesRequest.
        :type user_actions: bool
        """
        self._user_actions = user_actions

    @property
    def view(self):
        r"""Gets the view of this ListProjectProtectedBranchesRequest.

        **参数解释：** 参数值只有simple ，意为使用简单模式，只返回名称。 **取值范围：** 字符串长度不少于1，不超过2000。

        :return: The view of this ListProjectProtectedBranchesRequest.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        r"""Sets the view of this ListProjectProtectedBranchesRequest.

        **参数解释：** 参数值只有simple ，意为使用简单模式，只返回名称。 **取值范围：** 字符串长度不少于1，不超过2000。

        :param view: The view of this ListProjectProtectedBranchesRequest.
        :type view: str
        """
        self._view = view

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
        if not isinstance(other, ListProjectProtectedBranchesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
