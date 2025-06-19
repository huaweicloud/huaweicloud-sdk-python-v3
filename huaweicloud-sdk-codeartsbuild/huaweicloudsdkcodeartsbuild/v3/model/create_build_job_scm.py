# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBuildJobScm:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branch': 'str',
        'url': 'str',
        'repo_id': 'str',
        'web_url': 'str',
        'scm_type': 'str',
        'is_auto_build': 'bool',
        'enable_git_lfs': 'bool',
        'build_type': 'str',
        'depth': 'str',
        'end_point_id': 'str',
        'source': 'str',
        'group_name': 'str',
        'repo_name': 'str'
    }

    attribute_map = {
        'branch': 'branch',
        'url': 'url',
        'repo_id': 'repo_id',
        'web_url': 'web_url',
        'scm_type': 'scm_type',
        'is_auto_build': 'is_auto_build',
        'enable_git_lfs': 'enable_git_lfs',
        'build_type': 'build_type',
        'depth': 'depth',
        'end_point_id': 'end_point_id',
        'source': 'source',
        'group_name': 'group_name',
        'repo_name': 'repo_name'
    }

    def __init__(self, branch=None, url=None, repo_id=None, web_url=None, scm_type=None, is_auto_build=None, enable_git_lfs=None, build_type=None, depth=None, end_point_id=None, source=None, group_name=None, repo_name=None):
        r"""CreateBuildJobScm

        The model defined in huaweicloud sdk

        :param branch: 代码分支
        :type branch: str
        :param url: 代码仓地址
        :type url: str
        :param repo_id: repo的id
        :type repo_id: str
        :param web_url: 代码仓http地址
        :type web_url: str
        :param scm_type: 仓库类别，Repo、Github等
        :type scm_type: str
        :param is_auto_build: 是否自动构建
        :type is_auto_build: bool
        :param enable_git_lfs: 是否启用gitlfs
        :type enable_git_lfs: bool
        :param build_type: 构建类别
        :type build_type: str
        :param depth: 克隆深度
        :type depth: str
        :param end_point_id: endpointId
        :type end_point_id: str
        :param source: source
        :type source: str
        :param group_name: 仓库分组
        :type group_name: str
        :param repo_name: 仓库名称
        :type repo_name: str
        """
        
        

        self._branch = None
        self._url = None
        self._repo_id = None
        self._web_url = None
        self._scm_type = None
        self._is_auto_build = None
        self._enable_git_lfs = None
        self._build_type = None
        self._depth = None
        self._end_point_id = None
        self._source = None
        self._group_name = None
        self._repo_name = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        self.url = url
        if repo_id is not None:
            self.repo_id = repo_id
        if web_url is not None:
            self.web_url = web_url
        self.scm_type = scm_type
        if is_auto_build is not None:
            self.is_auto_build = is_auto_build
        if enable_git_lfs is not None:
            self.enable_git_lfs = enable_git_lfs
        if build_type is not None:
            self.build_type = build_type
        if depth is not None:
            self.depth = depth
        if end_point_id is not None:
            self.end_point_id = end_point_id
        if source is not None:
            self.source = source
        if group_name is not None:
            self.group_name = group_name
        if repo_name is not None:
            self.repo_name = repo_name

    @property
    def branch(self):
        r"""Gets the branch of this CreateBuildJobScm.

        代码分支

        :return: The branch of this CreateBuildJobScm.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this CreateBuildJobScm.

        代码分支

        :param branch: The branch of this CreateBuildJobScm.
        :type branch: str
        """
        self._branch = branch

    @property
    def url(self):
        r"""Gets the url of this CreateBuildJobScm.

        代码仓地址

        :return: The url of this CreateBuildJobScm.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CreateBuildJobScm.

        代码仓地址

        :param url: The url of this CreateBuildJobScm.
        :type url: str
        """
        self._url = url

    @property
    def repo_id(self):
        r"""Gets the repo_id of this CreateBuildJobScm.

        repo的id

        :return: The repo_id of this CreateBuildJobScm.
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        r"""Sets the repo_id of this CreateBuildJobScm.

        repo的id

        :param repo_id: The repo_id of this CreateBuildJobScm.
        :type repo_id: str
        """
        self._repo_id = repo_id

    @property
    def web_url(self):
        r"""Gets the web_url of this CreateBuildJobScm.

        代码仓http地址

        :return: The web_url of this CreateBuildJobScm.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this CreateBuildJobScm.

        代码仓http地址

        :param web_url: The web_url of this CreateBuildJobScm.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def scm_type(self):
        r"""Gets the scm_type of this CreateBuildJobScm.

        仓库类别，Repo、Github等

        :return: The scm_type of this CreateBuildJobScm.
        :rtype: str
        """
        return self._scm_type

    @scm_type.setter
    def scm_type(self, scm_type):
        r"""Sets the scm_type of this CreateBuildJobScm.

        仓库类别，Repo、Github等

        :param scm_type: The scm_type of this CreateBuildJobScm.
        :type scm_type: str
        """
        self._scm_type = scm_type

    @property
    def is_auto_build(self):
        r"""Gets the is_auto_build of this CreateBuildJobScm.

        是否自动构建

        :return: The is_auto_build of this CreateBuildJobScm.
        :rtype: bool
        """
        return self._is_auto_build

    @is_auto_build.setter
    def is_auto_build(self, is_auto_build):
        r"""Sets the is_auto_build of this CreateBuildJobScm.

        是否自动构建

        :param is_auto_build: The is_auto_build of this CreateBuildJobScm.
        :type is_auto_build: bool
        """
        self._is_auto_build = is_auto_build

    @property
    def enable_git_lfs(self):
        r"""Gets the enable_git_lfs of this CreateBuildJobScm.

        是否启用gitlfs

        :return: The enable_git_lfs of this CreateBuildJobScm.
        :rtype: bool
        """
        return self._enable_git_lfs

    @enable_git_lfs.setter
    def enable_git_lfs(self, enable_git_lfs):
        r"""Sets the enable_git_lfs of this CreateBuildJobScm.

        是否启用gitlfs

        :param enable_git_lfs: The enable_git_lfs of this CreateBuildJobScm.
        :type enable_git_lfs: bool
        """
        self._enable_git_lfs = enable_git_lfs

    @property
    def build_type(self):
        r"""Gets the build_type of this CreateBuildJobScm.

        构建类别

        :return: The build_type of this CreateBuildJobScm.
        :rtype: str
        """
        return self._build_type

    @build_type.setter
    def build_type(self, build_type):
        r"""Sets the build_type of this CreateBuildJobScm.

        构建类别

        :param build_type: The build_type of this CreateBuildJobScm.
        :type build_type: str
        """
        self._build_type = build_type

    @property
    def depth(self):
        r"""Gets the depth of this CreateBuildJobScm.

        克隆深度

        :return: The depth of this CreateBuildJobScm.
        :rtype: str
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        r"""Sets the depth of this CreateBuildJobScm.

        克隆深度

        :param depth: The depth of this CreateBuildJobScm.
        :type depth: str
        """
        self._depth = depth

    @property
    def end_point_id(self):
        r"""Gets the end_point_id of this CreateBuildJobScm.

        endpointId

        :return: The end_point_id of this CreateBuildJobScm.
        :rtype: str
        """
        return self._end_point_id

    @end_point_id.setter
    def end_point_id(self, end_point_id):
        r"""Sets the end_point_id of this CreateBuildJobScm.

        endpointId

        :param end_point_id: The end_point_id of this CreateBuildJobScm.
        :type end_point_id: str
        """
        self._end_point_id = end_point_id

    @property
    def source(self):
        r"""Gets the source of this CreateBuildJobScm.

        source

        :return: The source of this CreateBuildJobScm.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CreateBuildJobScm.

        source

        :param source: The source of this CreateBuildJobScm.
        :type source: str
        """
        self._source = source

    @property
    def group_name(self):
        r"""Gets the group_name of this CreateBuildJobScm.

        仓库分组

        :return: The group_name of this CreateBuildJobScm.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this CreateBuildJobScm.

        仓库分组

        :param group_name: The group_name of this CreateBuildJobScm.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def repo_name(self):
        r"""Gets the repo_name of this CreateBuildJobScm.

        仓库名称

        :return: The repo_name of this CreateBuildJobScm.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        r"""Sets the repo_name of this CreateBuildJobScm.

        仓库名称

        :param repo_name: The repo_name of this CreateBuildJobScm.
        :type repo_name: str
        """
        self._repo_name = repo_name

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
        if not isinstance(other, CreateBuildJobScm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
