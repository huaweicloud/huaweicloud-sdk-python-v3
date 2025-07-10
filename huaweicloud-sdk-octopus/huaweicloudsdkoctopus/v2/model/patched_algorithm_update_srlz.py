# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PatchedAlgorithmUpdateSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'id': 'int',
        'created_at': 'float',
        'updated_at': 'float',
        'compilation': 'CompilationUpdateSrlz',
        'build': 'BuildUpdateSrlz',
        'run': 'RunSrlz',
        'keys_reset': 'bool',
        'category': 'str',
        'name': 'str',
        'description': 'str',
        'git_url': 'str',
        'git_branch': 'str',
        'git_sha1': 'str',
        'mount_dir': 'str',
        'compile_command': 'str',
        'compile_workspace': 'str',
        'artifact_paths': 'list[str]',
        'run_workspace': 'str',
        'command': 'str',
        'keyword': 'str',
        'public_key': 'str',
        'cpu': 'float',
        'memory': 'int',
        'gpu': 'int',
        'image_repo_id': 'int'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'compilation': 'compilation',
        'build': 'build',
        'run': 'run',
        'keys_reset': 'keys_reset',
        'category': 'category',
        'name': 'name',
        'description': 'description',
        'git_url': 'git_url',
        'git_branch': 'git_branch',
        'git_sha1': 'git_sha1',
        'mount_dir': 'mount_dir',
        'compile_command': 'compile_command',
        'compile_workspace': 'compile_workspace',
        'artifact_paths': 'artifact_paths',
        'run_workspace': 'run_workspace',
        'command': 'command',
        'keyword': 'keyword',
        'public_key': 'public_key',
        'cpu': 'cpu',
        'memory': 'memory',
        'gpu': 'gpu',
        'image_repo_id': 'image_repo_id'
    }

    def __init__(self, url=None, id=None, created_at=None, updated_at=None, compilation=None, build=None, run=None, keys_reset=None, category=None, name=None, description=None, git_url=None, git_branch=None, git_sha1=None, mount_dir=None, compile_command=None, compile_workspace=None, artifact_paths=None, run_workspace=None, command=None, keyword=None, public_key=None, cpu=None, memory=None, gpu=None, image_repo_id=None):
        r"""PatchedAlgorithmUpdateSrlz

        The model defined in huaweicloud sdk

        :param url: 
        :type url: str
        :param id: 
        :type id: int
        :param created_at: 
        :type created_at: float
        :param updated_at: 
        :type updated_at: float
        :param compilation: 
        :type compilation: :class:`huaweicloudsdkoctopus.v2.CompilationUpdateSrlz`
        :param build: 
        :type build: :class:`huaweicloudsdkoctopus.v2.BuildUpdateSrlz`
        :param run: 
        :type run: :class:`huaweicloudsdkoctopus.v2.RunSrlz`
        :param keys_reset: 
        :type keys_reset: bool
        :param category: 算法类型，如image
        :type category: str
        :param name: 名称
        :type name: str
        :param description: 描述
        :type description: str
        :param git_url: 代码仓库地址
        :type git_url: str
        :param git_branch: 代码分支
        :type git_branch: str
        :param git_sha1: commit id
        :type git_sha1: str
        :param mount_dir: 挂载目录，需绝对路径
        :type mount_dir: str
        :param compile_command: 编译命令
        :type compile_command: str
        :param compile_workspace: 编译目录，须在挂载路径下
        :type compile_workspace: str
        :param artifact_paths: 编译产物列表，须在挂载路径下
        :type artifact_paths: list[str]
        :param run_workspace: 运行目录
        :type run_workspace: str
        :param command: 运行命令
        :type command: str
        :param keyword: 算法关键字
        :type keyword: str
        :param public_key: ssh-key公钥
        :type public_key: str
        :param cpu: cpu配额
        :type cpu: float
        :param memory: 内存配额
        :type memory: int
        :param gpu: gpu配额
        :type gpu: int
        :param image_repo_id: 镜像id
        :type image_repo_id: int
        """
        
        

        self._url = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._compilation = None
        self._build = None
        self._run = None
        self._keys_reset = None
        self._category = None
        self._name = None
        self._description = None
        self._git_url = None
        self._git_branch = None
        self._git_sha1 = None
        self._mount_dir = None
        self._compile_command = None
        self._compile_workspace = None
        self._artifact_paths = None
        self._run_workspace = None
        self._command = None
        self._keyword = None
        self._public_key = None
        self._cpu = None
        self._memory = None
        self._gpu = None
        self._image_repo_id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.compilation = compilation
        self.build = build
        if run is not None:
            self.run = run
        if keys_reset is not None:
            self.keys_reset = keys_reset
        if category is not None:
            self.category = category
        if name is not None:
            self.name = name
        self.description = description
        self.git_url = git_url
        self.git_branch = git_branch
        self.git_sha1 = git_sha1
        if mount_dir is not None:
            self.mount_dir = mount_dir
        self.compile_command = compile_command
        if compile_workspace is not None:
            self.compile_workspace = compile_workspace
        self.artifact_paths = artifact_paths
        if run_workspace is not None:
            self.run_workspace = run_workspace
        if command is not None:
            self.command = command
        if keyword is not None:
            self.keyword = keyword
        self.public_key = public_key
        self.cpu = cpu
        self.memory = memory
        self.gpu = gpu
        if image_repo_id is not None:
            self.image_repo_id = image_repo_id

    @property
    def url(self):
        r"""Gets the url of this PatchedAlgorithmUpdateSrlz.

        :return: The url of this PatchedAlgorithmUpdateSrlz.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this PatchedAlgorithmUpdateSrlz.

        :param url: The url of this PatchedAlgorithmUpdateSrlz.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this PatchedAlgorithmUpdateSrlz.

        :return: The id of this PatchedAlgorithmUpdateSrlz.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PatchedAlgorithmUpdateSrlz.

        :param id: The id of this PatchedAlgorithmUpdateSrlz.
        :type id: int
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this PatchedAlgorithmUpdateSrlz.

        :return: The created_at of this PatchedAlgorithmUpdateSrlz.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this PatchedAlgorithmUpdateSrlz.

        :param created_at: The created_at of this PatchedAlgorithmUpdateSrlz.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this PatchedAlgorithmUpdateSrlz.

        :return: The updated_at of this PatchedAlgorithmUpdateSrlz.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this PatchedAlgorithmUpdateSrlz.

        :param updated_at: The updated_at of this PatchedAlgorithmUpdateSrlz.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def compilation(self):
        r"""Gets the compilation of this PatchedAlgorithmUpdateSrlz.

        :return: The compilation of this PatchedAlgorithmUpdateSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.CompilationUpdateSrlz`
        """
        return self._compilation

    @compilation.setter
    def compilation(self, compilation):
        r"""Sets the compilation of this PatchedAlgorithmUpdateSrlz.

        :param compilation: The compilation of this PatchedAlgorithmUpdateSrlz.
        :type compilation: :class:`huaweicloudsdkoctopus.v2.CompilationUpdateSrlz`
        """
        self._compilation = compilation

    @property
    def build(self):
        r"""Gets the build of this PatchedAlgorithmUpdateSrlz.

        :return: The build of this PatchedAlgorithmUpdateSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.BuildUpdateSrlz`
        """
        return self._build

    @build.setter
    def build(self, build):
        r"""Sets the build of this PatchedAlgorithmUpdateSrlz.

        :param build: The build of this PatchedAlgorithmUpdateSrlz.
        :type build: :class:`huaweicloudsdkoctopus.v2.BuildUpdateSrlz`
        """
        self._build = build

    @property
    def run(self):
        r"""Gets the run of this PatchedAlgorithmUpdateSrlz.

        :return: The run of this PatchedAlgorithmUpdateSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.RunSrlz`
        """
        return self._run

    @run.setter
    def run(self, run):
        r"""Sets the run of this PatchedAlgorithmUpdateSrlz.

        :param run: The run of this PatchedAlgorithmUpdateSrlz.
        :type run: :class:`huaweicloudsdkoctopus.v2.RunSrlz`
        """
        self._run = run

    @property
    def keys_reset(self):
        r"""Gets the keys_reset of this PatchedAlgorithmUpdateSrlz.

        :return: The keys_reset of this PatchedAlgorithmUpdateSrlz.
        :rtype: bool
        """
        return self._keys_reset

    @keys_reset.setter
    def keys_reset(self, keys_reset):
        r"""Sets the keys_reset of this PatchedAlgorithmUpdateSrlz.

        :param keys_reset: The keys_reset of this PatchedAlgorithmUpdateSrlz.
        :type keys_reset: bool
        """
        self._keys_reset = keys_reset

    @property
    def category(self):
        r"""Gets the category of this PatchedAlgorithmUpdateSrlz.

        算法类型，如image

        :return: The category of this PatchedAlgorithmUpdateSrlz.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this PatchedAlgorithmUpdateSrlz.

        算法类型，如image

        :param category: The category of this PatchedAlgorithmUpdateSrlz.
        :type category: str
        """
        self._category = category

    @property
    def name(self):
        r"""Gets the name of this PatchedAlgorithmUpdateSrlz.

        名称

        :return: The name of this PatchedAlgorithmUpdateSrlz.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PatchedAlgorithmUpdateSrlz.

        名称

        :param name: The name of this PatchedAlgorithmUpdateSrlz.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this PatchedAlgorithmUpdateSrlz.

        描述

        :return: The description of this PatchedAlgorithmUpdateSrlz.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PatchedAlgorithmUpdateSrlz.

        描述

        :param description: The description of this PatchedAlgorithmUpdateSrlz.
        :type description: str
        """
        self._description = description

    @property
    def git_url(self):
        r"""Gets the git_url of this PatchedAlgorithmUpdateSrlz.

        代码仓库地址

        :return: The git_url of this PatchedAlgorithmUpdateSrlz.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        r"""Sets the git_url of this PatchedAlgorithmUpdateSrlz.

        代码仓库地址

        :param git_url: The git_url of this PatchedAlgorithmUpdateSrlz.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def git_branch(self):
        r"""Gets the git_branch of this PatchedAlgorithmUpdateSrlz.

        代码分支

        :return: The git_branch of this PatchedAlgorithmUpdateSrlz.
        :rtype: str
        """
        return self._git_branch

    @git_branch.setter
    def git_branch(self, git_branch):
        r"""Sets the git_branch of this PatchedAlgorithmUpdateSrlz.

        代码分支

        :param git_branch: The git_branch of this PatchedAlgorithmUpdateSrlz.
        :type git_branch: str
        """
        self._git_branch = git_branch

    @property
    def git_sha1(self):
        r"""Gets the git_sha1 of this PatchedAlgorithmUpdateSrlz.

        commit id

        :return: The git_sha1 of this PatchedAlgorithmUpdateSrlz.
        :rtype: str
        """
        return self._git_sha1

    @git_sha1.setter
    def git_sha1(self, git_sha1):
        r"""Sets the git_sha1 of this PatchedAlgorithmUpdateSrlz.

        commit id

        :param git_sha1: The git_sha1 of this PatchedAlgorithmUpdateSrlz.
        :type git_sha1: str
        """
        self._git_sha1 = git_sha1

    @property
    def mount_dir(self):
        r"""Gets the mount_dir of this PatchedAlgorithmUpdateSrlz.

        挂载目录，需绝对路径

        :return: The mount_dir of this PatchedAlgorithmUpdateSrlz.
        :rtype: str
        """
        return self._mount_dir

    @mount_dir.setter
    def mount_dir(self, mount_dir):
        r"""Sets the mount_dir of this PatchedAlgorithmUpdateSrlz.

        挂载目录，需绝对路径

        :param mount_dir: The mount_dir of this PatchedAlgorithmUpdateSrlz.
        :type mount_dir: str
        """
        self._mount_dir = mount_dir

    @property
    def compile_command(self):
        r"""Gets the compile_command of this PatchedAlgorithmUpdateSrlz.

        编译命令

        :return: The compile_command of this PatchedAlgorithmUpdateSrlz.
        :rtype: str
        """
        return self._compile_command

    @compile_command.setter
    def compile_command(self, compile_command):
        r"""Sets the compile_command of this PatchedAlgorithmUpdateSrlz.

        编译命令

        :param compile_command: The compile_command of this PatchedAlgorithmUpdateSrlz.
        :type compile_command: str
        """
        self._compile_command = compile_command

    @property
    def compile_workspace(self):
        r"""Gets the compile_workspace of this PatchedAlgorithmUpdateSrlz.

        编译目录，须在挂载路径下

        :return: The compile_workspace of this PatchedAlgorithmUpdateSrlz.
        :rtype: str
        """
        return self._compile_workspace

    @compile_workspace.setter
    def compile_workspace(self, compile_workspace):
        r"""Sets the compile_workspace of this PatchedAlgorithmUpdateSrlz.

        编译目录，须在挂载路径下

        :param compile_workspace: The compile_workspace of this PatchedAlgorithmUpdateSrlz.
        :type compile_workspace: str
        """
        self._compile_workspace = compile_workspace

    @property
    def artifact_paths(self):
        r"""Gets the artifact_paths of this PatchedAlgorithmUpdateSrlz.

        编译产物列表，须在挂载路径下

        :return: The artifact_paths of this PatchedAlgorithmUpdateSrlz.
        :rtype: list[str]
        """
        return self._artifact_paths

    @artifact_paths.setter
    def artifact_paths(self, artifact_paths):
        r"""Sets the artifact_paths of this PatchedAlgorithmUpdateSrlz.

        编译产物列表，须在挂载路径下

        :param artifact_paths: The artifact_paths of this PatchedAlgorithmUpdateSrlz.
        :type artifact_paths: list[str]
        """
        self._artifact_paths = artifact_paths

    @property
    def run_workspace(self):
        r"""Gets the run_workspace of this PatchedAlgorithmUpdateSrlz.

        运行目录

        :return: The run_workspace of this PatchedAlgorithmUpdateSrlz.
        :rtype: str
        """
        return self._run_workspace

    @run_workspace.setter
    def run_workspace(self, run_workspace):
        r"""Sets the run_workspace of this PatchedAlgorithmUpdateSrlz.

        运行目录

        :param run_workspace: The run_workspace of this PatchedAlgorithmUpdateSrlz.
        :type run_workspace: str
        """
        self._run_workspace = run_workspace

    @property
    def command(self):
        r"""Gets the command of this PatchedAlgorithmUpdateSrlz.

        运行命令

        :return: The command of this PatchedAlgorithmUpdateSrlz.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this PatchedAlgorithmUpdateSrlz.

        运行命令

        :param command: The command of this PatchedAlgorithmUpdateSrlz.
        :type command: str
        """
        self._command = command

    @property
    def keyword(self):
        r"""Gets the keyword of this PatchedAlgorithmUpdateSrlz.

        算法关键字

        :return: The keyword of this PatchedAlgorithmUpdateSrlz.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this PatchedAlgorithmUpdateSrlz.

        算法关键字

        :param keyword: The keyword of this PatchedAlgorithmUpdateSrlz.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def public_key(self):
        r"""Gets the public_key of this PatchedAlgorithmUpdateSrlz.

        ssh-key公钥

        :return: The public_key of this PatchedAlgorithmUpdateSrlz.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        r"""Sets the public_key of this PatchedAlgorithmUpdateSrlz.

        ssh-key公钥

        :param public_key: The public_key of this PatchedAlgorithmUpdateSrlz.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def cpu(self):
        r"""Gets the cpu of this PatchedAlgorithmUpdateSrlz.

        cpu配额

        :return: The cpu of this PatchedAlgorithmUpdateSrlz.
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this PatchedAlgorithmUpdateSrlz.

        cpu配额

        :param cpu: The cpu of this PatchedAlgorithmUpdateSrlz.
        :type cpu: float
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this PatchedAlgorithmUpdateSrlz.

        内存配额

        :return: The memory of this PatchedAlgorithmUpdateSrlz.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this PatchedAlgorithmUpdateSrlz.

        内存配额

        :param memory: The memory of this PatchedAlgorithmUpdateSrlz.
        :type memory: int
        """
        self._memory = memory

    @property
    def gpu(self):
        r"""Gets the gpu of this PatchedAlgorithmUpdateSrlz.

        gpu配额

        :return: The gpu of this PatchedAlgorithmUpdateSrlz.
        :rtype: int
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        r"""Sets the gpu of this PatchedAlgorithmUpdateSrlz.

        gpu配额

        :param gpu: The gpu of this PatchedAlgorithmUpdateSrlz.
        :type gpu: int
        """
        self._gpu = gpu

    @property
    def image_repo_id(self):
        r"""Gets the image_repo_id of this PatchedAlgorithmUpdateSrlz.

        镜像id

        :return: The image_repo_id of this PatchedAlgorithmUpdateSrlz.
        :rtype: int
        """
        return self._image_repo_id

    @image_repo_id.setter
    def image_repo_id(self, image_repo_id):
        r"""Sets the image_repo_id of this PatchedAlgorithmUpdateSrlz.

        镜像id

        :param image_repo_id: The image_repo_id of this PatchedAlgorithmUpdateSrlz.
        :type image_repo_id: int
        """
        self._image_repo_id = image_repo_id

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
        if not isinstance(other, PatchedAlgorithmUpdateSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
