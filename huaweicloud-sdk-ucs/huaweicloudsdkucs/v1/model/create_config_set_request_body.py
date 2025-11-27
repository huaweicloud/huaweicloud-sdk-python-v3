# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConfigSetRequestBody:

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
        'config_set_type': 'str',
        'repo_name': 'str',
        'bucket_spec': 'object',
        'helm_chart_spec': 'object',
        'git_repository_spec': 'GitRepositorySpec',
        'helm_repository_spec': 'object',
        'kustomization_spec': 'KustomizationSpec',
        'cluster_info': 'ClusterInfo',
        'secret_info': 'SecretInfo'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'config_set_type': 'configSetType',
        'repo_name': 'repoName',
        'bucket_spec': 'bucketSpec',
        'helm_chart_spec': 'helmChartSpec',
        'git_repository_spec': 'gitRepositorySpec',
        'helm_repository_spec': 'helmRepositorySpec',
        'kustomization_spec': 'kustomizationSpec',
        'cluster_info': 'clusterInfo',
        'secret_info': 'secretInfo'
    }

    def __init__(self, name=None, namespace=None, config_set_type=None, repo_name=None, bucket_spec=None, helm_chart_spec=None, git_repository_spec=None, helm_repository_spec=None, kustomization_spec=None, cluster_info=None, secret_info=None):
        r"""CreateConfigSetRequestBody

        The model defined in huaweicloud sdk

        :param name: 配置集合的名称
        :type name: str
        :param namespace: 命名空间
        :type namespace: str
        :param config_set_type: 配置集合的类型
        :type config_set_type: str
        :param repo_name: 源代码仓库名称
        :type repo_name: str
        :param bucket_spec: 对象存储桶的基本信息
        :type bucket_spec: object
        :param helm_chart_spec: Helm Chart源基本信息
        :type helm_chart_spec: object
        :param git_repository_spec: 
        :type git_repository_spec: :class:`huaweicloudsdkucs.v1.GitRepositorySpec`
        :param helm_repository_spec: Helm仓库基本信息
        :type helm_repository_spec: object
        :param kustomization_spec: 
        :type kustomization_spec: :class:`huaweicloudsdkucs.v1.KustomizationSpec`
        :param cluster_info: 
        :type cluster_info: :class:`huaweicloudsdkucs.v1.ClusterInfo`
        :param secret_info: 
        :type secret_info: :class:`huaweicloudsdkucs.v1.SecretInfo`
        """
        
        

        self._name = None
        self._namespace = None
        self._config_set_type = None
        self._repo_name = None
        self._bucket_spec = None
        self._helm_chart_spec = None
        self._git_repository_spec = None
        self._helm_repository_spec = None
        self._kustomization_spec = None
        self._cluster_info = None
        self._secret_info = None
        self.discriminator = None

        self.name = name
        self.namespace = namespace
        if config_set_type is not None:
            self.config_set_type = config_set_type
        if repo_name is not None:
            self.repo_name = repo_name
        if bucket_spec is not None:
            self.bucket_spec = bucket_spec
        if helm_chart_spec is not None:
            self.helm_chart_spec = helm_chart_spec
        if git_repository_spec is not None:
            self.git_repository_spec = git_repository_spec
        if helm_repository_spec is not None:
            self.helm_repository_spec = helm_repository_spec
        if kustomization_spec is not None:
            self.kustomization_spec = kustomization_spec
        if cluster_info is not None:
            self.cluster_info = cluster_info
        if secret_info is not None:
            self.secret_info = secret_info

    @property
    def name(self):
        r"""Gets the name of this CreateConfigSetRequestBody.

        配置集合的名称

        :return: The name of this CreateConfigSetRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateConfigSetRequestBody.

        配置集合的名称

        :param name: The name of this CreateConfigSetRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this CreateConfigSetRequestBody.

        命名空间

        :return: The namespace of this CreateConfigSetRequestBody.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this CreateConfigSetRequestBody.

        命名空间

        :param namespace: The namespace of this CreateConfigSetRequestBody.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def config_set_type(self):
        r"""Gets the config_set_type of this CreateConfigSetRequestBody.

        配置集合的类型

        :return: The config_set_type of this CreateConfigSetRequestBody.
        :rtype: str
        """
        return self._config_set_type

    @config_set_type.setter
    def config_set_type(self, config_set_type):
        r"""Sets the config_set_type of this CreateConfigSetRequestBody.

        配置集合的类型

        :param config_set_type: The config_set_type of this CreateConfigSetRequestBody.
        :type config_set_type: str
        """
        self._config_set_type = config_set_type

    @property
    def repo_name(self):
        r"""Gets the repo_name of this CreateConfigSetRequestBody.

        源代码仓库名称

        :return: The repo_name of this CreateConfigSetRequestBody.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        r"""Sets the repo_name of this CreateConfigSetRequestBody.

        源代码仓库名称

        :param repo_name: The repo_name of this CreateConfigSetRequestBody.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def bucket_spec(self):
        r"""Gets the bucket_spec of this CreateConfigSetRequestBody.

        对象存储桶的基本信息

        :return: The bucket_spec of this CreateConfigSetRequestBody.
        :rtype: object
        """
        return self._bucket_spec

    @bucket_spec.setter
    def bucket_spec(self, bucket_spec):
        r"""Sets the bucket_spec of this CreateConfigSetRequestBody.

        对象存储桶的基本信息

        :param bucket_spec: The bucket_spec of this CreateConfigSetRequestBody.
        :type bucket_spec: object
        """
        self._bucket_spec = bucket_spec

    @property
    def helm_chart_spec(self):
        r"""Gets the helm_chart_spec of this CreateConfigSetRequestBody.

        Helm Chart源基本信息

        :return: The helm_chart_spec of this CreateConfigSetRequestBody.
        :rtype: object
        """
        return self._helm_chart_spec

    @helm_chart_spec.setter
    def helm_chart_spec(self, helm_chart_spec):
        r"""Sets the helm_chart_spec of this CreateConfigSetRequestBody.

        Helm Chart源基本信息

        :param helm_chart_spec: The helm_chart_spec of this CreateConfigSetRequestBody.
        :type helm_chart_spec: object
        """
        self._helm_chart_spec = helm_chart_spec

    @property
    def git_repository_spec(self):
        r"""Gets the git_repository_spec of this CreateConfigSetRequestBody.

        :return: The git_repository_spec of this CreateConfigSetRequestBody.
        :rtype: :class:`huaweicloudsdkucs.v1.GitRepositorySpec`
        """
        return self._git_repository_spec

    @git_repository_spec.setter
    def git_repository_spec(self, git_repository_spec):
        r"""Sets the git_repository_spec of this CreateConfigSetRequestBody.

        :param git_repository_spec: The git_repository_spec of this CreateConfigSetRequestBody.
        :type git_repository_spec: :class:`huaweicloudsdkucs.v1.GitRepositorySpec`
        """
        self._git_repository_spec = git_repository_spec

    @property
    def helm_repository_spec(self):
        r"""Gets the helm_repository_spec of this CreateConfigSetRequestBody.

        Helm仓库基本信息

        :return: The helm_repository_spec of this CreateConfigSetRequestBody.
        :rtype: object
        """
        return self._helm_repository_spec

    @helm_repository_spec.setter
    def helm_repository_spec(self, helm_repository_spec):
        r"""Sets the helm_repository_spec of this CreateConfigSetRequestBody.

        Helm仓库基本信息

        :param helm_repository_spec: The helm_repository_spec of this CreateConfigSetRequestBody.
        :type helm_repository_spec: object
        """
        self._helm_repository_spec = helm_repository_spec

    @property
    def kustomization_spec(self):
        r"""Gets the kustomization_spec of this CreateConfigSetRequestBody.

        :return: The kustomization_spec of this CreateConfigSetRequestBody.
        :rtype: :class:`huaweicloudsdkucs.v1.KustomizationSpec`
        """
        return self._kustomization_spec

    @kustomization_spec.setter
    def kustomization_spec(self, kustomization_spec):
        r"""Sets the kustomization_spec of this CreateConfigSetRequestBody.

        :param kustomization_spec: The kustomization_spec of this CreateConfigSetRequestBody.
        :type kustomization_spec: :class:`huaweicloudsdkucs.v1.KustomizationSpec`
        """
        self._kustomization_spec = kustomization_spec

    @property
    def cluster_info(self):
        r"""Gets the cluster_info of this CreateConfigSetRequestBody.

        :return: The cluster_info of this CreateConfigSetRequestBody.
        :rtype: :class:`huaweicloudsdkucs.v1.ClusterInfo`
        """
        return self._cluster_info

    @cluster_info.setter
    def cluster_info(self, cluster_info):
        r"""Sets the cluster_info of this CreateConfigSetRequestBody.

        :param cluster_info: The cluster_info of this CreateConfigSetRequestBody.
        :type cluster_info: :class:`huaweicloudsdkucs.v1.ClusterInfo`
        """
        self._cluster_info = cluster_info

    @property
    def secret_info(self):
        r"""Gets the secret_info of this CreateConfigSetRequestBody.

        :return: The secret_info of this CreateConfigSetRequestBody.
        :rtype: :class:`huaweicloudsdkucs.v1.SecretInfo`
        """
        return self._secret_info

    @secret_info.setter
    def secret_info(self, secret_info):
        r"""Sets the secret_info of this CreateConfigSetRequestBody.

        :param secret_info: The secret_info of this CreateConfigSetRequestBody.
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
        if not isinstance(other, CreateConfigSetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
