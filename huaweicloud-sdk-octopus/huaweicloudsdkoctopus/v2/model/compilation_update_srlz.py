# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompilationUpdateSrlz:

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
        'artifact_paths': 'list[str]',
        'compile_image_status': 'RunImageStatusEnum',
        'public_key': 'str'
    }

    attribute_map = {
        'git_url': 'git_url',
        'git_branch': 'git_branch',
        'git_sha1': 'git_sha1',
        'compile_command': 'compile_command',
        'compile_workspace': 'compile_workspace',
        'artifact_paths': 'artifact_paths',
        'compile_image_status': 'compile_image_status',
        'public_key': 'public_key'
    }

    def __init__(self, git_url=None, git_branch=None, git_sha1=None, compile_command=None, compile_workspace=None, artifact_paths=None, compile_image_status=None, public_key=None):
        r"""CompilationUpdateSrlz

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
        :param compile_image_status: 编译镜像状态  * &#x60;0&#x60; - Success * &#x60;100&#x60; - Init * &#x60;101&#x60; - Init Failed * &#x60;200&#x60; - To Push * &#x60;201&#x60; - Uploading
        :type compile_image_status: :class:`huaweicloudsdkoctopus.v2.RunImageStatusEnum`
        :param public_key: ssh-key公钥
        :type public_key: str
        """
        
        

        self._git_url = None
        self._git_branch = None
        self._git_sha1 = None
        self._compile_command = None
        self._compile_workspace = None
        self._artifact_paths = None
        self._compile_image_status = None
        self._public_key = None
        self.discriminator = None

        self.git_url = git_url
        self.git_branch = git_branch
        self.git_sha1 = git_sha1
        self.compile_command = compile_command
        if compile_workspace is not None:
            self.compile_workspace = compile_workspace
        self.artifact_paths = artifact_paths
        self.compile_image_status = compile_image_status
        self.public_key = public_key

    @property
    def git_url(self):
        r"""Gets the git_url of this CompilationUpdateSrlz.

        代码仓库地址

        :return: The git_url of this CompilationUpdateSrlz.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        r"""Sets the git_url of this CompilationUpdateSrlz.

        代码仓库地址

        :param git_url: The git_url of this CompilationUpdateSrlz.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def git_branch(self):
        r"""Gets the git_branch of this CompilationUpdateSrlz.

        代码分支

        :return: The git_branch of this CompilationUpdateSrlz.
        :rtype: str
        """
        return self._git_branch

    @git_branch.setter
    def git_branch(self, git_branch):
        r"""Sets the git_branch of this CompilationUpdateSrlz.

        代码分支

        :param git_branch: The git_branch of this CompilationUpdateSrlz.
        :type git_branch: str
        """
        self._git_branch = git_branch

    @property
    def git_sha1(self):
        r"""Gets the git_sha1 of this CompilationUpdateSrlz.

        commit id

        :return: The git_sha1 of this CompilationUpdateSrlz.
        :rtype: str
        """
        return self._git_sha1

    @git_sha1.setter
    def git_sha1(self, git_sha1):
        r"""Sets the git_sha1 of this CompilationUpdateSrlz.

        commit id

        :param git_sha1: The git_sha1 of this CompilationUpdateSrlz.
        :type git_sha1: str
        """
        self._git_sha1 = git_sha1

    @property
    def compile_command(self):
        r"""Gets the compile_command of this CompilationUpdateSrlz.

        编译命令

        :return: The compile_command of this CompilationUpdateSrlz.
        :rtype: str
        """
        return self._compile_command

    @compile_command.setter
    def compile_command(self, compile_command):
        r"""Sets the compile_command of this CompilationUpdateSrlz.

        编译命令

        :param compile_command: The compile_command of this CompilationUpdateSrlz.
        :type compile_command: str
        """
        self._compile_command = compile_command

    @property
    def compile_workspace(self):
        r"""Gets the compile_workspace of this CompilationUpdateSrlz.

        编译目录，须在挂载路径下

        :return: The compile_workspace of this CompilationUpdateSrlz.
        :rtype: str
        """
        return self._compile_workspace

    @compile_workspace.setter
    def compile_workspace(self, compile_workspace):
        r"""Sets the compile_workspace of this CompilationUpdateSrlz.

        编译目录，须在挂载路径下

        :param compile_workspace: The compile_workspace of this CompilationUpdateSrlz.
        :type compile_workspace: str
        """
        self._compile_workspace = compile_workspace

    @property
    def artifact_paths(self):
        r"""Gets the artifact_paths of this CompilationUpdateSrlz.

        编译产物列表，须在挂载路径下

        :return: The artifact_paths of this CompilationUpdateSrlz.
        :rtype: list[str]
        """
        return self._artifact_paths

    @artifact_paths.setter
    def artifact_paths(self, artifact_paths):
        r"""Sets the artifact_paths of this CompilationUpdateSrlz.

        编译产物列表，须在挂载路径下

        :param artifact_paths: The artifact_paths of this CompilationUpdateSrlz.
        :type artifact_paths: list[str]
        """
        self._artifact_paths = artifact_paths

    @property
    def compile_image_status(self):
        r"""Gets the compile_image_status of this CompilationUpdateSrlz.

        编译镜像状态  * `0` - Success * `100` - Init * `101` - Init Failed * `200` - To Push * `201` - Uploading

        :return: The compile_image_status of this CompilationUpdateSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.RunImageStatusEnum`
        """
        return self._compile_image_status

    @compile_image_status.setter
    def compile_image_status(self, compile_image_status):
        r"""Sets the compile_image_status of this CompilationUpdateSrlz.

        编译镜像状态  * `0` - Success * `100` - Init * `101` - Init Failed * `200` - To Push * `201` - Uploading

        :param compile_image_status: The compile_image_status of this CompilationUpdateSrlz.
        :type compile_image_status: :class:`huaweicloudsdkoctopus.v2.RunImageStatusEnum`
        """
        self._compile_image_status = compile_image_status

    @property
    def public_key(self):
        r"""Gets the public_key of this CompilationUpdateSrlz.

        ssh-key公钥

        :return: The public_key of this CompilationUpdateSrlz.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        r"""Sets the public_key of this CompilationUpdateSrlz.

        ssh-key公钥

        :param public_key: The public_key of this CompilationUpdateSrlz.
        :type public_key: str
        """
        self._public_key = public_key

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
        if not isinstance(other, CompilationUpdateSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
