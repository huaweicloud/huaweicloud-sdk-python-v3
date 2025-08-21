# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMergeRequestCommentsByLineRequest:

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
        'merge_request_iid': 'int',
        'line': 'int',
        'with_commit_comments': 'bool',
        'path': 'str',
        'view': 'str',
        'base_sha': 'str',
        'start_sha': 'str',
        'head_sha': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'merge_request_iid': 'merge_request_iid',
        'line': 'line',
        'with_commit_comments': 'with_commit_comments',
        'path': 'path',
        'view': 'view',
        'base_sha': 'base_sha',
        'start_sha': 'start_sha',
        'head_sha': 'head_sha'
    }

    def __init__(self, repository_id=None, merge_request_iid=None, line=None, with_commit_comments=None, path=None, view=None, base_sha=None, start_sha=None, head_sha=None):
        r"""ShowMergeRequestCommentsByLineRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param merge_request_iid: **参数解释：**  合并请求 iid。
        :type merge_request_iid: int
        :param line: 
        :type line: int
        :param with_commit_comments: 
        :type with_commit_comments: bool
        :param path: **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过100000。
        :type path: str
        :param view: 
        :type view: str
        :param base_sha: 合并请求中原分支与目标分支的共同基准点
        :type base_sha: str
        :param start_sha: 合并请求中，从共同基准点开始到原分支方向的第一个提交点
        :type start_sha: str
        :param head_sha: 合并请求中原分支指向的提交点
        :type head_sha: str
        """
        
        

        self._repository_id = None
        self._merge_request_iid = None
        self._line = None
        self._with_commit_comments = None
        self._path = None
        self._view = None
        self._base_sha = None
        self._start_sha = None
        self._head_sha = None
        self.discriminator = None

        self.repository_id = repository_id
        self.merge_request_iid = merge_request_iid
        if line is not None:
            self.line = line
        if with_commit_comments is not None:
            self.with_commit_comments = with_commit_comments
        if path is not None:
            self.path = path
        if view is not None:
            self.view = view
        if base_sha is not None:
            self.base_sha = base_sha
        if start_sha is not None:
            self.start_sha = start_sha
        if head_sha is not None:
            self.head_sha = head_sha

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ShowMergeRequestCommentsByLineRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ShowMergeRequestCommentsByLineRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ShowMergeRequestCommentsByLineRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ShowMergeRequestCommentsByLineRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def merge_request_iid(self):
        r"""Gets the merge_request_iid of this ShowMergeRequestCommentsByLineRequest.

        **参数解释：**  合并请求 iid。

        :return: The merge_request_iid of this ShowMergeRequestCommentsByLineRequest.
        :rtype: int
        """
        return self._merge_request_iid

    @merge_request_iid.setter
    def merge_request_iid(self, merge_request_iid):
        r"""Sets the merge_request_iid of this ShowMergeRequestCommentsByLineRequest.

        **参数解释：**  合并请求 iid。

        :param merge_request_iid: The merge_request_iid of this ShowMergeRequestCommentsByLineRequest.
        :type merge_request_iid: int
        """
        self._merge_request_iid = merge_request_iid

    @property
    def line(self):
        r"""Gets the line of this ShowMergeRequestCommentsByLineRequest.

        :return: The line of this ShowMergeRequestCommentsByLineRequest.
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        r"""Sets the line of this ShowMergeRequestCommentsByLineRequest.

        :param line: The line of this ShowMergeRequestCommentsByLineRequest.
        :type line: int
        """
        self._line = line

    @property
    def with_commit_comments(self):
        r"""Gets the with_commit_comments of this ShowMergeRequestCommentsByLineRequest.

        :return: The with_commit_comments of this ShowMergeRequestCommentsByLineRequest.
        :rtype: bool
        """
        return self._with_commit_comments

    @with_commit_comments.setter
    def with_commit_comments(self, with_commit_comments):
        r"""Sets the with_commit_comments of this ShowMergeRequestCommentsByLineRequest.

        :param with_commit_comments: The with_commit_comments of this ShowMergeRequestCommentsByLineRequest.
        :type with_commit_comments: bool
        """
        self._with_commit_comments = with_commit_comments

    @property
    def path(self):
        r"""Gets the path of this ShowMergeRequestCommentsByLineRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过100000。

        :return: The path of this ShowMergeRequestCommentsByLineRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ShowMergeRequestCommentsByLineRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过100000。

        :param path: The path of this ShowMergeRequestCommentsByLineRequest.
        :type path: str
        """
        self._path = path

    @property
    def view(self):
        r"""Gets the view of this ShowMergeRequestCommentsByLineRequest.

        :return: The view of this ShowMergeRequestCommentsByLineRequest.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        r"""Sets the view of this ShowMergeRequestCommentsByLineRequest.

        :param view: The view of this ShowMergeRequestCommentsByLineRequest.
        :type view: str
        """
        self._view = view

    @property
    def base_sha(self):
        r"""Gets the base_sha of this ShowMergeRequestCommentsByLineRequest.

        合并请求中原分支与目标分支的共同基准点

        :return: The base_sha of this ShowMergeRequestCommentsByLineRequest.
        :rtype: str
        """
        return self._base_sha

    @base_sha.setter
    def base_sha(self, base_sha):
        r"""Sets the base_sha of this ShowMergeRequestCommentsByLineRequest.

        合并请求中原分支与目标分支的共同基准点

        :param base_sha: The base_sha of this ShowMergeRequestCommentsByLineRequest.
        :type base_sha: str
        """
        self._base_sha = base_sha

    @property
    def start_sha(self):
        r"""Gets the start_sha of this ShowMergeRequestCommentsByLineRequest.

        合并请求中，从共同基准点开始到原分支方向的第一个提交点

        :return: The start_sha of this ShowMergeRequestCommentsByLineRequest.
        :rtype: str
        """
        return self._start_sha

    @start_sha.setter
    def start_sha(self, start_sha):
        r"""Sets the start_sha of this ShowMergeRequestCommentsByLineRequest.

        合并请求中，从共同基准点开始到原分支方向的第一个提交点

        :param start_sha: The start_sha of this ShowMergeRequestCommentsByLineRequest.
        :type start_sha: str
        """
        self._start_sha = start_sha

    @property
    def head_sha(self):
        r"""Gets the head_sha of this ShowMergeRequestCommentsByLineRequest.

        合并请求中原分支指向的提交点

        :return: The head_sha of this ShowMergeRequestCommentsByLineRequest.
        :rtype: str
        """
        return self._head_sha

    @head_sha.setter
    def head_sha(self, head_sha):
        r"""Sets the head_sha of this ShowMergeRequestCommentsByLineRequest.

        合并请求中原分支指向的提交点

        :param head_sha: The head_sha of this ShowMergeRequestCommentsByLineRequest.
        :type head_sha: str
        """
        self._head_sha = head_sha

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
        if not isinstance(other, ShowMergeRequestCommentsByLineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
