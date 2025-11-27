# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uid': 'str',
        'name': 'str',
        'repo_type': 'str',
        'namespace': 'str',
        'git_repository': 'GitRepository',
        'repo_status': 'str',
        'cluster_info': 'ClusterInfo',
        'secret_info': 'SecretInfo'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'repo_type': 'repoType',
        'namespace': 'namespace',
        'git_repository': 'gitRepository',
        'repo_status': 'repoStatus',
        'cluster_info': 'clusterInfo',
        'secret_info': 'secretInfo'
    }

    def __init__(self, uid=None, name=None, repo_type=None, namespace=None, git_repository=None, repo_status=None, cluster_info=None, secret_info=None):
        r"""RepoResponse

        The model defined in huaweicloud sdk

        :param uid: 仓库的唯一标识符
        :type uid: str
        :param name: 仓库名称
        :type name: str
        :param repo_type: 仓库类型，包括Bucket、HelmChart、GitRepository、HelmRepository，目前仅支持GitRepository
        :type repo_type: str
        :param namespace: 命名空间
        :type namespace: str
        :param git_repository: 
        :type git_repository: :class:`huaweicloudsdkucs.v1.GitRepository`
        :param repo_status: 仓库状态，包括Health、Failed、Unknown、Progressing
        :type repo_status: str
        :param cluster_info: 
        :type cluster_info: :class:`huaweicloudsdkucs.v1.ClusterInfo`
        :param secret_info: 
        :type secret_info: :class:`huaweicloudsdkucs.v1.SecretInfo`
        """
        
        

        self._uid = None
        self._name = None
        self._repo_type = None
        self._namespace = None
        self._git_repository = None
        self._repo_status = None
        self._cluster_info = None
        self._secret_info = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if repo_type is not None:
            self.repo_type = repo_type
        if namespace is not None:
            self.namespace = namespace
        if git_repository is not None:
            self.git_repository = git_repository
        if repo_status is not None:
            self.repo_status = repo_status
        if cluster_info is not None:
            self.cluster_info = cluster_info
        if secret_info is not None:
            self.secret_info = secret_info

    @property
    def uid(self):
        r"""Gets the uid of this RepoResponse.

        仓库的唯一标识符

        :return: The uid of this RepoResponse.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this RepoResponse.

        仓库的唯一标识符

        :param uid: The uid of this RepoResponse.
        :type uid: str
        """
        self._uid = uid

    @property
    def name(self):
        r"""Gets the name of this RepoResponse.

        仓库名称

        :return: The name of this RepoResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RepoResponse.

        仓库名称

        :param name: The name of this RepoResponse.
        :type name: str
        """
        self._name = name

    @property
    def repo_type(self):
        r"""Gets the repo_type of this RepoResponse.

        仓库类型，包括Bucket、HelmChart、GitRepository、HelmRepository，目前仅支持GitRepository

        :return: The repo_type of this RepoResponse.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        r"""Sets the repo_type of this RepoResponse.

        仓库类型，包括Bucket、HelmChart、GitRepository、HelmRepository，目前仅支持GitRepository

        :param repo_type: The repo_type of this RepoResponse.
        :type repo_type: str
        """
        self._repo_type = repo_type

    @property
    def namespace(self):
        r"""Gets the namespace of this RepoResponse.

        命名空间

        :return: The namespace of this RepoResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this RepoResponse.

        命名空间

        :param namespace: The namespace of this RepoResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def git_repository(self):
        r"""Gets the git_repository of this RepoResponse.

        :return: The git_repository of this RepoResponse.
        :rtype: :class:`huaweicloudsdkucs.v1.GitRepository`
        """
        return self._git_repository

    @git_repository.setter
    def git_repository(self, git_repository):
        r"""Sets the git_repository of this RepoResponse.

        :param git_repository: The git_repository of this RepoResponse.
        :type git_repository: :class:`huaweicloudsdkucs.v1.GitRepository`
        """
        self._git_repository = git_repository

    @property
    def repo_status(self):
        r"""Gets the repo_status of this RepoResponse.

        仓库状态，包括Health、Failed、Unknown、Progressing

        :return: The repo_status of this RepoResponse.
        :rtype: str
        """
        return self._repo_status

    @repo_status.setter
    def repo_status(self, repo_status):
        r"""Sets the repo_status of this RepoResponse.

        仓库状态，包括Health、Failed、Unknown、Progressing

        :param repo_status: The repo_status of this RepoResponse.
        :type repo_status: str
        """
        self._repo_status = repo_status

    @property
    def cluster_info(self):
        r"""Gets the cluster_info of this RepoResponse.

        :return: The cluster_info of this RepoResponse.
        :rtype: :class:`huaweicloudsdkucs.v1.ClusterInfo`
        """
        return self._cluster_info

    @cluster_info.setter
    def cluster_info(self, cluster_info):
        r"""Sets the cluster_info of this RepoResponse.

        :param cluster_info: The cluster_info of this RepoResponse.
        :type cluster_info: :class:`huaweicloudsdkucs.v1.ClusterInfo`
        """
        self._cluster_info = cluster_info

    @property
    def secret_info(self):
        r"""Gets the secret_info of this RepoResponse.

        :return: The secret_info of this RepoResponse.
        :rtype: :class:`huaweicloudsdkucs.v1.SecretInfo`
        """
        return self._secret_info

    @secret_info.setter
    def secret_info(self, secret_info):
        r"""Sets the secret_info of this RepoResponse.

        :param secret_info: The secret_info of this RepoResponse.
        :type secret_info: :class:`huaweicloudsdkucs.v1.SecretInfo`
        """
        self._secret_info = secret_info

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RepoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
