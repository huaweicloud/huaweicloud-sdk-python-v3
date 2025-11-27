# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConfigSetResponse(SdkResponse):

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
        'namespace': 'str',
        'config_set_type': 'str',
        'repo_name': 'str',
        'bucket': 'object',
        'helm_chart': 'object',
        'git_repository': 'GitRepository',
        'helm_repository': 'object',
        'repo_status': 'str',
        'helm_release': 'object',
        'kustomization': 'Kustomization',
        'config_set_status': 'str',
        'cluster_info': 'ClusterInfo',
        'secret_info': 'SecretInfo'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'namespace': 'namespace',
        'config_set_type': 'configSetType',
        'repo_name': 'repoName',
        'bucket': 'bucket',
        'helm_chart': 'helmChart',
        'git_repository': 'gitRepository',
        'helm_repository': 'helmRepository',
        'repo_status': 'repoStatus',
        'helm_release': 'helmRelease',
        'kustomization': 'kustomization',
        'config_set_status': 'configSetStatus',
        'cluster_info': 'clusterInfo',
        'secret_info': 'secretInfo'
    }

    def __init__(self, uid=None, name=None, namespace=None, config_set_type=None, repo_name=None, bucket=None, helm_chart=None, git_repository=None, helm_repository=None, repo_status=None, helm_release=None, kustomization=None, config_set_status=None, cluster_info=None, secret_info=None):
        r"""ShowConfigSetResponse

        The model defined in huaweicloud sdk

        :param uid: 配置集合的唯一标识
        :type uid: str
        :param name: 配置集合的名称
        :type name: str
        :param namespace: 命名空间
        :type namespace: str
        :param config_set_type: 配置集合的类型
        :type config_set_type: str
        :param repo_name: 仓库名称
        :type repo_name: str
        :param bucket: bucket基本信息
        :type bucket: object
        :param helm_chart: Helm Chart源基本信息
        :type helm_chart: object
        :param git_repository: 
        :type git_repository: :class:`huaweicloudsdkucs.v1.GitRepository`
        :param helm_repository: Helm仓库的定义与状态等信息
        :type helm_repository: object
        :param repo_status: 仓库状态信息
        :type repo_status: str
        :param helm_release: Helm Chart的发布配置和状态信息
        :type helm_release: object
        :param kustomization: 
        :type kustomization: :class:`huaweicloudsdkucs.v1.Kustomization`
        :param config_set_status: 配置集合状态信息
        :type config_set_status: str
        :param cluster_info: 
        :type cluster_info: :class:`huaweicloudsdkucs.v1.ClusterInfo`
        :param secret_info: 
        :type secret_info: :class:`huaweicloudsdkucs.v1.SecretInfo`
        """
        
        super().__init__()

        self._uid = None
        self._name = None
        self._namespace = None
        self._config_set_type = None
        self._repo_name = None
        self._bucket = None
        self._helm_chart = None
        self._git_repository = None
        self._helm_repository = None
        self._repo_status = None
        self._helm_release = None
        self._kustomization = None
        self._config_set_status = None
        self._cluster_info = None
        self._secret_info = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if config_set_type is not None:
            self.config_set_type = config_set_type
        if repo_name is not None:
            self.repo_name = repo_name
        if bucket is not None:
            self.bucket = bucket
        if helm_chart is not None:
            self.helm_chart = helm_chart
        if git_repository is not None:
            self.git_repository = git_repository
        if helm_repository is not None:
            self.helm_repository = helm_repository
        if repo_status is not None:
            self.repo_status = repo_status
        if helm_release is not None:
            self.helm_release = helm_release
        if kustomization is not None:
            self.kustomization = kustomization
        if config_set_status is not None:
            self.config_set_status = config_set_status
        if cluster_info is not None:
            self.cluster_info = cluster_info
        if secret_info is not None:
            self.secret_info = secret_info

    @property
    def uid(self):
        r"""Gets the uid of this ShowConfigSetResponse.

        配置集合的唯一标识

        :return: The uid of this ShowConfigSetResponse.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this ShowConfigSetResponse.

        配置集合的唯一标识

        :param uid: The uid of this ShowConfigSetResponse.
        :type uid: str
        """
        self._uid = uid

    @property
    def name(self):
        r"""Gets the name of this ShowConfigSetResponse.

        配置集合的名称

        :return: The name of this ShowConfigSetResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowConfigSetResponse.

        配置集合的名称

        :param name: The name of this ShowConfigSetResponse.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this ShowConfigSetResponse.

        命名空间

        :return: The namespace of this ShowConfigSetResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ShowConfigSetResponse.

        命名空间

        :param namespace: The namespace of this ShowConfigSetResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def config_set_type(self):
        r"""Gets the config_set_type of this ShowConfigSetResponse.

        配置集合的类型

        :return: The config_set_type of this ShowConfigSetResponse.
        :rtype: str
        """
        return self._config_set_type

    @config_set_type.setter
    def config_set_type(self, config_set_type):
        r"""Sets the config_set_type of this ShowConfigSetResponse.

        配置集合的类型

        :param config_set_type: The config_set_type of this ShowConfigSetResponse.
        :type config_set_type: str
        """
        self._config_set_type = config_set_type

    @property
    def repo_name(self):
        r"""Gets the repo_name of this ShowConfigSetResponse.

        仓库名称

        :return: The repo_name of this ShowConfigSetResponse.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        r"""Sets the repo_name of this ShowConfigSetResponse.

        仓库名称

        :param repo_name: The repo_name of this ShowConfigSetResponse.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def bucket(self):
        r"""Gets the bucket of this ShowConfigSetResponse.

        bucket基本信息

        :return: The bucket of this ShowConfigSetResponse.
        :rtype: object
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this ShowConfigSetResponse.

        bucket基本信息

        :param bucket: The bucket of this ShowConfigSetResponse.
        :type bucket: object
        """
        self._bucket = bucket

    @property
    def helm_chart(self):
        r"""Gets the helm_chart of this ShowConfigSetResponse.

        Helm Chart源基本信息

        :return: The helm_chart of this ShowConfigSetResponse.
        :rtype: object
        """
        return self._helm_chart

    @helm_chart.setter
    def helm_chart(self, helm_chart):
        r"""Sets the helm_chart of this ShowConfigSetResponse.

        Helm Chart源基本信息

        :param helm_chart: The helm_chart of this ShowConfigSetResponse.
        :type helm_chart: object
        """
        self._helm_chart = helm_chart

    @property
    def git_repository(self):
        r"""Gets the git_repository of this ShowConfigSetResponse.

        :return: The git_repository of this ShowConfigSetResponse.
        :rtype: :class:`huaweicloudsdkucs.v1.GitRepository`
        """
        return self._git_repository

    @git_repository.setter
    def git_repository(self, git_repository):
        r"""Sets the git_repository of this ShowConfigSetResponse.

        :param git_repository: The git_repository of this ShowConfigSetResponse.
        :type git_repository: :class:`huaweicloudsdkucs.v1.GitRepository`
        """
        self._git_repository = git_repository

    @property
    def helm_repository(self):
        r"""Gets the helm_repository of this ShowConfigSetResponse.

        Helm仓库的定义与状态等信息

        :return: The helm_repository of this ShowConfigSetResponse.
        :rtype: object
        """
        return self._helm_repository

    @helm_repository.setter
    def helm_repository(self, helm_repository):
        r"""Sets the helm_repository of this ShowConfigSetResponse.

        Helm仓库的定义与状态等信息

        :param helm_repository: The helm_repository of this ShowConfigSetResponse.
        :type helm_repository: object
        """
        self._helm_repository = helm_repository

    @property
    def repo_status(self):
        r"""Gets the repo_status of this ShowConfigSetResponse.

        仓库状态信息

        :return: The repo_status of this ShowConfigSetResponse.
        :rtype: str
        """
        return self._repo_status

    @repo_status.setter
    def repo_status(self, repo_status):
        r"""Sets the repo_status of this ShowConfigSetResponse.

        仓库状态信息

        :param repo_status: The repo_status of this ShowConfigSetResponse.
        :type repo_status: str
        """
        self._repo_status = repo_status

    @property
    def helm_release(self):
        r"""Gets the helm_release of this ShowConfigSetResponse.

        Helm Chart的发布配置和状态信息

        :return: The helm_release of this ShowConfigSetResponse.
        :rtype: object
        """
        return self._helm_release

    @helm_release.setter
    def helm_release(self, helm_release):
        r"""Sets the helm_release of this ShowConfigSetResponse.

        Helm Chart的发布配置和状态信息

        :param helm_release: The helm_release of this ShowConfigSetResponse.
        :type helm_release: object
        """
        self._helm_release = helm_release

    @property
    def kustomization(self):
        r"""Gets the kustomization of this ShowConfigSetResponse.

        :return: The kustomization of this ShowConfigSetResponse.
        :rtype: :class:`huaweicloudsdkucs.v1.Kustomization`
        """
        return self._kustomization

    @kustomization.setter
    def kustomization(self, kustomization):
        r"""Sets the kustomization of this ShowConfigSetResponse.

        :param kustomization: The kustomization of this ShowConfigSetResponse.
        :type kustomization: :class:`huaweicloudsdkucs.v1.Kustomization`
        """
        self._kustomization = kustomization

    @property
    def config_set_status(self):
        r"""Gets the config_set_status of this ShowConfigSetResponse.

        配置集合状态信息

        :return: The config_set_status of this ShowConfigSetResponse.
        :rtype: str
        """
        return self._config_set_status

    @config_set_status.setter
    def config_set_status(self, config_set_status):
        r"""Sets the config_set_status of this ShowConfigSetResponse.

        配置集合状态信息

        :param config_set_status: The config_set_status of this ShowConfigSetResponse.
        :type config_set_status: str
        """
        self._config_set_status = config_set_status

    @property
    def cluster_info(self):
        r"""Gets the cluster_info of this ShowConfigSetResponse.

        :return: The cluster_info of this ShowConfigSetResponse.
        :rtype: :class:`huaweicloudsdkucs.v1.ClusterInfo`
        """
        return self._cluster_info

    @cluster_info.setter
    def cluster_info(self, cluster_info):
        r"""Sets the cluster_info of this ShowConfigSetResponse.

        :param cluster_info: The cluster_info of this ShowConfigSetResponse.
        :type cluster_info: :class:`huaweicloudsdkucs.v1.ClusterInfo`
        """
        self._cluster_info = cluster_info

    @property
    def secret_info(self):
        r"""Gets the secret_info of this ShowConfigSetResponse.

        :return: The secret_info of this ShowConfigSetResponse.
        :rtype: :class:`huaweicloudsdkucs.v1.SecretInfo`
        """
        return self._secret_info

    @secret_info.setter
    def secret_info(self, secret_info):
        r"""Sets the secret_info of this ShowConfigSetResponse.

        :param secret_info: The secret_info of this ShowConfigSetResponse.
        :type secret_info: :class:`huaweicloudsdkucs.v1.SecretInfo`
        """
        self._secret_info = secret_info

    def to_dict(self):
        import warnings
        warnings.warn("ShowConfigSetResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowConfigSetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
