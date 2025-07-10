# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompilationCreateSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'git_url': 'str',
        'git_branch': 'str',
        'git_sha1': 'str',
        'compile_command': 'str',
        'compile_workspace': 'str',
        'artifact_paths': 'list[str]'
    }

    attribute_map = {
        'git_url': 'git_url',
        'git_branch': 'git_branch',
        'git_sha1': 'git_sha1',
        'compile_command': 'compile_command',
        'compile_workspace': 'compile_workspace',
        'artifact_paths': 'artifact_paths'
    }

    def __init__(self, git_url=None, git_branch=None, git_sha1=None, compile_command=None, compile_workspace=None, artifact_paths=None):
        r"""CompilationCreateSrlz

        The model defined in huaweicloud sdk

        :param git_url: 代码仓库地址
        :type git_url: str
        :param git_branch: 代码分支
        :type git_branch: str
        :param git_sha1: commit id
        :type git_sha1: str
        :param compile_command: 编译命令
        :type compile_command: str
        :param compile_workspace: 编译目录，须在挂载路径下
        :type compile_workspace: str
        :param artifact_paths: 编译产物列表，须在挂载路径下
        :type artifact_paths: list[str]
        """
        
        

        self._git_url = None
        self._git_branch = None
        self._git_sha1 = None
        self._compile_command = None
        self._compile_workspace = None
        self._artifact_paths = None
        self.discriminator = None

        self.git_url = git_url
        self.git_branch = git_branch
        self.git_sha1 = git_sha1
        self.compile_command = compile_command
        if compile_workspace is not None:
            self.compile_workspace = compile_workspace
        self.artifact_paths = artifact_paths

    @property
    def git_url(self):
        r"""Gets the git_url of this CompilationCreateSrlz.

        代码仓库地址

        :return: The git_url of this CompilationCreateSrlz.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        r"""Sets the git_url of this CompilationCreateSrlz.

        代码仓库地址

        :param git_url: The git_url of this CompilationCreateSrlz.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def git_branch(self):
        r"""Gets the git_branch of this CompilationCreateSrlz.

        代码分支

        :return: The git_branch of this CompilationCreateSrlz.
        :rtype: str
        """
        return self._git_branch

    @git_branch.setter
    def git_branch(self, git_branch):
        r"""Sets the git_branch of this CompilationCreateSrlz.

        代码分支

        :param git_branch: The git_branch of this CompilationCreateSrlz.
        :type git_branch: str
        """
        self._git_branch = git_branch

    @property
    def git_sha1(self):
        r"""Gets the git_sha1 of this CompilationCreateSrlz.

        commit id

        :return: The git_sha1 of this CompilationCreateSrlz.
        :rtype: str
        """
        return self._git_sha1

    @git_sha1.setter
    def git_sha1(self, git_sha1):
        r"""Sets the git_sha1 of this CompilationCreateSrlz.

        commit id

        :param git_sha1: The git_sha1 of this CompilationCreateSrlz.
        :type git_sha1: str
        """
        self._git_sha1 = git_sha1

    @property
    def compile_command(self):
        r"""Gets the compile_command of this CompilationCreateSrlz.

        编译命令

        :return: The compile_command of this CompilationCreateSrlz.
        :rtype: str
        """
        return self._compile_command

    @compile_command.setter
    def compile_command(self, compile_command):
        r"""Sets the compile_command of this CompilationCreateSrlz.

        编译命令

        :param compile_command: The compile_command of this CompilationCreateSrlz.
        :type compile_command: str
        """
        self._compile_command = compile_command

    @property
    def compile_workspace(self):
        r"""Gets the compile_workspace of this CompilationCreateSrlz.

        编译目录，须在挂载路径下

        :return: The compile_workspace of this CompilationCreateSrlz.
        :rtype: str
        """
        return self._compile_workspace

    @compile_workspace.setter
    def compile_workspace(self, compile_workspace):
        r"""Sets the compile_workspace of this CompilationCreateSrlz.

        编译目录，须在挂载路径下

        :param compile_workspace: The compile_workspace of this CompilationCreateSrlz.
        :type compile_workspace: str
        """
        self._compile_workspace = compile_workspace

    @property
    def artifact_paths(self):
        r"""Gets the artifact_paths of this CompilationCreateSrlz.

        编译产物列表，须在挂载路径下

        :return: The artifact_paths of this CompilationCreateSrlz.
        :rtype: list[str]
        """
        return self._artifact_paths

    @artifact_paths.setter
    def artifact_paths(self, artifact_paths):
        r"""Sets the artifact_paths of this CompilationCreateSrlz.

        编译产物列表，须在挂载路径下

        :param artifact_paths: The artifact_paths of this CompilationCreateSrlz.
        :type artifact_paths: list[str]
        """
        self._artifact_paths = artifact_paths

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
        if not isinstance(other, CompilationCreateSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
