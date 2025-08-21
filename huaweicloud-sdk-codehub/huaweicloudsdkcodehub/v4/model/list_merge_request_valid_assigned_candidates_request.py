# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMergeRequestValidAssignedCandidatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'target_branch': 'str',
        'merge_request_iid': 'int',
        'offset': 'int',
        'limit': 'int',
        'search': 'str',
        'search_by_name_list': 'str',
        'target_project_id': 'str',
        'view': 'str',
        'mode': 'str',
        'only_developers': 'bool'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'target_branch': 'target_branch',
        'merge_request_iid': 'merge_request_iid',
        'offset': 'offset',
        'limit': 'limit',
        'search': 'search',
        'search_by_name_list': 'search_by_name_list',
        'target_project_id': 'target_project_id',
        'view': 'view',
        'mode': 'mode',
        'only_developers': 'only_developers'
    }

    def __init__(self, repository_id=None, target_branch=None, merge_request_iid=None, offset=None, limit=None, search=None, search_by_name_list=None, target_project_id=None, view=None, mode=None, only_developers=None):
        r"""ListMergeRequestValidAssignedCandidatesRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param target_branch: **参数解释：** 目标分支。创建MR时，代码将要合入的分支。
        :type target_branch: str
        :param merge_request_iid: **参数解释：**  合并请求 iid。
        :type merge_request_iid: int
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param search: **参数解释：** 查询关键字，可模糊匹配用户名称、用户昵称、租户名称。
        :type search: str
        :param search_by_name_list: **参数解释：** Search user list by name list。
        :type search_by_name_list: str
        :param target_project_id: **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。
        :type target_project_id: str
        :param view: **参数解释：** The type of assignee, merge user or approver
        :type view: str
        :param mode: **参数解释：** The type of assignee, merge user or approver
        :type mode: str
        :param only_developers: **参数解释：** The type of memeber, developer
        :type only_developers: bool
        """
        
        

        self._repository_id = None
        self._target_branch = None
        self._merge_request_iid = None
        self._offset = None
        self._limit = None
        self._search = None
        self._search_by_name_list = None
        self._target_project_id = None
        self._view = None
        self._mode = None
        self._only_developers = None
        self.discriminator = None

        self.repository_id = repository_id
        if target_branch is not None:
            self.target_branch = target_branch
        if merge_request_iid is not None:
            self.merge_request_iid = merge_request_iid
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search is not None:
            self.search = search
        if search_by_name_list is not None:
            self.search_by_name_list = search_by_name_list
        if target_project_id is not None:
            self.target_project_id = target_project_id
        if view is not None:
            self.view = view
        if mode is not None:
            self.mode = mode
        if only_developers is not None:
            self.only_developers = only_developers

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListMergeRequestValidAssignedCandidatesRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListMergeRequestValidAssignedCandidatesRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def target_branch(self):
        r"""Gets the target_branch of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** 目标分支。创建MR时，代码将要合入的分支。

        :return: The target_branch of this ListMergeRequestValidAssignedCandidatesRequest.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** 目标分支。创建MR时，代码将要合入的分支。

        :param target_branch: The target_branch of this ListMergeRequestValidAssignedCandidatesRequest.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def merge_request_iid(self):
        r"""Gets the merge_request_iid of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：**  合并请求 iid。

        :return: The merge_request_iid of this ListMergeRequestValidAssignedCandidatesRequest.
        :rtype: int
        """
        return self._merge_request_iid

    @merge_request_iid.setter
    def merge_request_iid(self, merge_request_iid):
        r"""Sets the merge_request_iid of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：**  合并请求 iid。

        :param merge_request_iid: The merge_request_iid of this ListMergeRequestValidAssignedCandidatesRequest.
        :type merge_request_iid: int
        """
        self._merge_request_iid = merge_request_iid

    @property
    def offset(self):
        r"""Gets the offset of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListMergeRequestValidAssignedCandidatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListMergeRequestValidAssignedCandidatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListMergeRequestValidAssignedCandidatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListMergeRequestValidAssignedCandidatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search(self):
        r"""Gets the search of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** 查询关键字，可模糊匹配用户名称、用户昵称、租户名称。

        :return: The search of this ListMergeRequestValidAssignedCandidatesRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** 查询关键字，可模糊匹配用户名称、用户昵称、租户名称。

        :param search: The search of this ListMergeRequestValidAssignedCandidatesRequest.
        :type search: str
        """
        self._search = search

    @property
    def search_by_name_list(self):
        r"""Gets the search_by_name_list of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** Search user list by name list。

        :return: The search_by_name_list of this ListMergeRequestValidAssignedCandidatesRequest.
        :rtype: str
        """
        return self._search_by_name_list

    @search_by_name_list.setter
    def search_by_name_list(self, search_by_name_list):
        r"""Sets the search_by_name_list of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** Search user list by name list。

        :param search_by_name_list: The search_by_name_list of this ListMergeRequestValidAssignedCandidatesRequest.
        :type search_by_name_list: str
        """
        self._search_by_name_list = search_by_name_list

    @property
    def target_project_id(self):
        r"""Gets the target_project_id of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :return: The target_project_id of this ListMergeRequestValidAssignedCandidatesRequest.
        :rtype: str
        """
        return self._target_project_id

    @target_project_id.setter
    def target_project_id(self, target_project_id):
        r"""Sets the target_project_id of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :param target_project_id: The target_project_id of this ListMergeRequestValidAssignedCandidatesRequest.
        :type target_project_id: str
        """
        self._target_project_id = target_project_id

    @property
    def view(self):
        r"""Gets the view of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** The type of assignee, merge user or approver

        :return: The view of this ListMergeRequestValidAssignedCandidatesRequest.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        r"""Sets the view of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** The type of assignee, merge user or approver

        :param view: The view of this ListMergeRequestValidAssignedCandidatesRequest.
        :type view: str
        """
        self._view = view

    @property
    def mode(self):
        r"""Gets the mode of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** The type of assignee, merge user or approver

        :return: The mode of this ListMergeRequestValidAssignedCandidatesRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** The type of assignee, merge user or approver

        :param mode: The mode of this ListMergeRequestValidAssignedCandidatesRequest.
        :type mode: str
        """
        self._mode = mode

    @property
    def only_developers(self):
        r"""Gets the only_developers of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** The type of memeber, developer

        :return: The only_developers of this ListMergeRequestValidAssignedCandidatesRequest.
        :rtype: bool
        """
        return self._only_developers

    @only_developers.setter
    def only_developers(self, only_developers):
        r"""Sets the only_developers of this ListMergeRequestValidAssignedCandidatesRequest.

        **参数解释：** The type of memeber, developer

        :param only_developers: The only_developers of this ListMergeRequestValidAssignedCandidatesRequest.
        :type only_developers: bool
        """
        self._only_developers = only_developers

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
        if not isinstance(other, ListMergeRequestValidAssignedCandidatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
