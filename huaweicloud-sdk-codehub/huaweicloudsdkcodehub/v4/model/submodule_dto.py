# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubmoduleDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repo_id': 'int',
        'branch': 'str',
        'path': 'str',
        'git_url': 'str',
        'submodule_branch': 'str',
        'namespace_uuid': 'str',
        'submodule_repo_id': 'int',
        'repo_name': 'str',
        'sub_commit_id': 'str',
        'deploy_key_status': 'int',
        'status': 'int'
    }

    attribute_map = {
        'repo_id': 'repo_id',
        'branch': 'branch',
        'path': 'path',
        'git_url': 'git_url',
        'submodule_branch': 'submodule_branch',
        'namespace_uuid': 'namespace_uuid',
        'submodule_repo_id': 'submodule_repo_id',
        'repo_name': 'repo_name',
        'sub_commit_id': 'sub_commitId',
        'deploy_key_status': 'deployKey_status',
        'status': 'status'
    }

    def __init__(self, repo_id=None, branch=None, path=None, git_url=None, submodule_branch=None, namespace_uuid=None, submodule_repo_id=None, repo_name=None, sub_commit_id=None, deploy_key_status=None, status=None):
        r"""SubmoduleDto

        The model defined in huaweicloud sdk

        :param repo_id: **参数解释：** 仓库ID。
        :type repo_id: int
        :param branch: **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节。
        :type branch: str
        :param path: **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节
        :type path: str
        :param git_url: **参数解释：** 子模块Git地址。
        :type git_url: str
        :param submodule_branch: **参数解释：** 子模块分支名。 **取值范围：** 最小1个字节，最大200字节。
        :type submodule_branch: str
        :param namespace_uuid: 组织名/组织名.../仓库名
        :type namespace_uuid: str
        :param submodule_repo_id: **参数解释：** 子模块仓库ID。
        :type submodule_repo_id: int
        :param repo_name: **参数解释：** 子模块仓库名称。
        :type repo_name: str
        :param sub_commit_id: **参数解释：** 子模块仓库提交。
        :type sub_commit_id: str
        :param deploy_key_status: **参数解释：** 部署秘钥同步状态。 **取值范围：** - 0，不同步。 - 1，同步。
        :type deploy_key_status: int
        :param status: **参数解释：** 子模块状态。 **取值范围：** - 0，异常。 - 1，正常。
        :type status: int
        """
        
        

        self._repo_id = None
        self._branch = None
        self._path = None
        self._git_url = None
        self._submodule_branch = None
        self._namespace_uuid = None
        self._submodule_repo_id = None
        self._repo_name = None
        self._sub_commit_id = None
        self._deploy_key_status = None
        self._status = None
        self.discriminator = None

        if repo_id is not None:
            self.repo_id = repo_id
        if branch is not None:
            self.branch = branch
        if path is not None:
            self.path = path
        if git_url is not None:
            self.git_url = git_url
        if submodule_branch is not None:
            self.submodule_branch = submodule_branch
        if namespace_uuid is not None:
            self.namespace_uuid = namespace_uuid
        if submodule_repo_id is not None:
            self.submodule_repo_id = submodule_repo_id
        if repo_name is not None:
            self.repo_name = repo_name
        if sub_commit_id is not None:
            self.sub_commit_id = sub_commit_id
        if deploy_key_status is not None:
            self.deploy_key_status = deploy_key_status
        if status is not None:
            self.status = status

    @property
    def repo_id(self):
        r"""Gets the repo_id of this SubmoduleDto.

        **参数解释：** 仓库ID。

        :return: The repo_id of this SubmoduleDto.
        :rtype: int
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        r"""Sets the repo_id of this SubmoduleDto.

        **参数解释：** 仓库ID。

        :param repo_id: The repo_id of this SubmoduleDto.
        :type repo_id: int
        """
        self._repo_id = repo_id

    @property
    def branch(self):
        r"""Gets the branch of this SubmoduleDto.

        **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节。

        :return: The branch of this SubmoduleDto.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this SubmoduleDto.

        **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节。

        :param branch: The branch of this SubmoduleDto.
        :type branch: str
        """
        self._branch = branch

    @property
    def path(self):
        r"""Gets the path of this SubmoduleDto.

        **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节

        :return: The path of this SubmoduleDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this SubmoduleDto.

        **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节

        :param path: The path of this SubmoduleDto.
        :type path: str
        """
        self._path = path

    @property
    def git_url(self):
        r"""Gets the git_url of this SubmoduleDto.

        **参数解释：** 子模块Git地址。

        :return: The git_url of this SubmoduleDto.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        r"""Sets the git_url of this SubmoduleDto.

        **参数解释：** 子模块Git地址。

        :param git_url: The git_url of this SubmoduleDto.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def submodule_branch(self):
        r"""Gets the submodule_branch of this SubmoduleDto.

        **参数解释：** 子模块分支名。 **取值范围：** 最小1个字节，最大200字节。

        :return: The submodule_branch of this SubmoduleDto.
        :rtype: str
        """
        return self._submodule_branch

    @submodule_branch.setter
    def submodule_branch(self, submodule_branch):
        r"""Sets the submodule_branch of this SubmoduleDto.

        **参数解释：** 子模块分支名。 **取值范围：** 最小1个字节，最大200字节。

        :param submodule_branch: The submodule_branch of this SubmoduleDto.
        :type submodule_branch: str
        """
        self._submodule_branch = submodule_branch

    @property
    def namespace_uuid(self):
        r"""Gets the namespace_uuid of this SubmoduleDto.

        组织名/组织名.../仓库名

        :return: The namespace_uuid of this SubmoduleDto.
        :rtype: str
        """
        return self._namespace_uuid

    @namespace_uuid.setter
    def namespace_uuid(self, namespace_uuid):
        r"""Sets the namespace_uuid of this SubmoduleDto.

        组织名/组织名.../仓库名

        :param namespace_uuid: The namespace_uuid of this SubmoduleDto.
        :type namespace_uuid: str
        """
        self._namespace_uuid = namespace_uuid

    @property
    def submodule_repo_id(self):
        r"""Gets the submodule_repo_id of this SubmoduleDto.

        **参数解释：** 子模块仓库ID。

        :return: The submodule_repo_id of this SubmoduleDto.
        :rtype: int
        """
        return self._submodule_repo_id

    @submodule_repo_id.setter
    def submodule_repo_id(self, submodule_repo_id):
        r"""Sets the submodule_repo_id of this SubmoduleDto.

        **参数解释：** 子模块仓库ID。

        :param submodule_repo_id: The submodule_repo_id of this SubmoduleDto.
        :type submodule_repo_id: int
        """
        self._submodule_repo_id = submodule_repo_id

    @property
    def repo_name(self):
        r"""Gets the repo_name of this SubmoduleDto.

        **参数解释：** 子模块仓库名称。

        :return: The repo_name of this SubmoduleDto.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        r"""Sets the repo_name of this SubmoduleDto.

        **参数解释：** 子模块仓库名称。

        :param repo_name: The repo_name of this SubmoduleDto.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def sub_commit_id(self):
        r"""Gets the sub_commit_id of this SubmoduleDto.

        **参数解释：** 子模块仓库提交。

        :return: The sub_commit_id of this SubmoduleDto.
        :rtype: str
        """
        return self._sub_commit_id

    @sub_commit_id.setter
    def sub_commit_id(self, sub_commit_id):
        r"""Sets the sub_commit_id of this SubmoduleDto.

        **参数解释：** 子模块仓库提交。

        :param sub_commit_id: The sub_commit_id of this SubmoduleDto.
        :type sub_commit_id: str
        """
        self._sub_commit_id = sub_commit_id

    @property
    def deploy_key_status(self):
        r"""Gets the deploy_key_status of this SubmoduleDto.

        **参数解释：** 部署秘钥同步状态。 **取值范围：** - 0，不同步。 - 1，同步。

        :return: The deploy_key_status of this SubmoduleDto.
        :rtype: int
        """
        return self._deploy_key_status

    @deploy_key_status.setter
    def deploy_key_status(self, deploy_key_status):
        r"""Sets the deploy_key_status of this SubmoduleDto.

        **参数解释：** 部署秘钥同步状态。 **取值范围：** - 0，不同步。 - 1，同步。

        :param deploy_key_status: The deploy_key_status of this SubmoduleDto.
        :type deploy_key_status: int
        """
        self._deploy_key_status = deploy_key_status

    @property
    def status(self):
        r"""Gets the status of this SubmoduleDto.

        **参数解释：** 子模块状态。 **取值范围：** - 0，异常。 - 1，正常。

        :return: The status of this SubmoduleDto.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SubmoduleDto.

        **参数解释：** 子模块状态。 **取值范围：** - 0，异常。 - 1，正常。

        :param status: The status of this SubmoduleDto.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, SubmoduleDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
