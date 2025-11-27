# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRepoRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'namespace': 'str',
        'repo_type': 'str',
        'git_repository_spec': 'GitRepositorySpec',
        'secret_info': 'SecretInfo'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'repo_type': 'repoType',
        'git_repository_spec': 'gitRepositorySpec',
        'secret_info': 'secretInfo'
    }

    def __init__(self, name=None, namespace=None, repo_type=None, git_repository_spec=None, secret_info=None):
        r"""UpdateRepoRequestBody

        The model defined in huaweicloud sdk

        :param name: 仓库名称
        :type name: str
        :param namespace: 所在命名空间
        :type namespace: str
        :param repo_type: 仓库类型，包括Bucket、HelmChart、GitRepository、HelmRepository，目前仅支持GitRepository
        :type repo_type: str
        :param git_repository_spec: 
        :type git_repository_spec: :class:`huaweicloudsdkucs.v1.GitRepositorySpec`
        :param secret_info: 
        :type secret_info: :class:`huaweicloudsdkucs.v1.SecretInfo`
        """
        
        

        self._name = None
        self._namespace = None
        self._repo_type = None
        self._git_repository_spec = None
        self._secret_info = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if repo_type is not None:
            self.repo_type = repo_type
        if git_repository_spec is not None:
            self.git_repository_spec = git_repository_spec
        if secret_info is not None:
            self.secret_info = secret_info

    @property
    def name(self):
        r"""Gets the name of this UpdateRepoRequestBody.

        仓库名称

        :return: The name of this UpdateRepoRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateRepoRequestBody.

        仓库名称

        :param name: The name of this UpdateRepoRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this UpdateRepoRequestBody.

        所在命名空间

        :return: The namespace of this UpdateRepoRequestBody.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this UpdateRepoRequestBody.

        所在命名空间

        :param namespace: The namespace of this UpdateRepoRequestBody.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repo_type(self):
        r"""Gets the repo_type of this UpdateRepoRequestBody.

        仓库类型，包括Bucket、HelmChart、GitRepository、HelmRepository，目前仅支持GitRepository

        :return: The repo_type of this UpdateRepoRequestBody.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        r"""Sets the repo_type of this UpdateRepoRequestBody.

        仓库类型，包括Bucket、HelmChart、GitRepository、HelmRepository，目前仅支持GitRepository

        :param repo_type: The repo_type of this UpdateRepoRequestBody.
        :type repo_type: str
        """
        self._repo_type = repo_type

    @property
    def git_repository_spec(self):
        r"""Gets the git_repository_spec of this UpdateRepoRequestBody.

        :return: The git_repository_spec of this UpdateRepoRequestBody.
        :rtype: :class:`huaweicloudsdkucs.v1.GitRepositorySpec`
        """
        return self._git_repository_spec

    @git_repository_spec.setter
    def git_repository_spec(self, git_repository_spec):
        r"""Sets the git_repository_spec of this UpdateRepoRequestBody.

        :param git_repository_spec: The git_repository_spec of this UpdateRepoRequestBody.
        :type git_repository_spec: :class:`huaweicloudsdkucs.v1.GitRepositorySpec`
        """
        self._git_repository_spec = git_repository_spec

    @property
    def secret_info(self):
        r"""Gets the secret_info of this UpdateRepoRequestBody.

        :return: The secret_info of this UpdateRepoRequestBody.
        :rtype: :class:`huaweicloudsdkucs.v1.SecretInfo`
        """
        return self._secret_info

    @secret_info.setter
    def secret_info(self, secret_info):
        r"""Sets the secret_info of this UpdateRepoRequestBody.

        :param secret_info: The secret_info of this UpdateRepoRequestBody.
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
        if not isinstance(other, UpdateRepoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
