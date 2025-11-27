# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OnPremisesVersionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kubernetes_version': 'str',
        'release_version': 'str',
        'ucsctl_download_url': 'str',
        'arch': 'str',
        'obs_endpoint': 'str',
        'package_path': 'str',
        'images_package_path': 'str',
        'target_version': 'str'
    }

    attribute_map = {
        'kubernetes_version': 'kubernetesVersion',
        'release_version': 'releaseVersion',
        'ucsctl_download_url': 'ucsctlDownloadURL',
        'arch': 'arch',
        'obs_endpoint': 'obsEndpoint',
        'package_path': 'packagePath',
        'images_package_path': 'imagesPackagePath',
        'target_version': 'targetVersion'
    }

    def __init__(self, kubernetes_version=None, release_version=None, ucsctl_download_url=None, arch=None, obs_endpoint=None, package_path=None, images_package_path=None, target_version=None):
        r"""OnPremisesVersionInfo

        The model defined in huaweicloud sdk

        :param kubernetes_version: Kubernetes集群版本
        :type kubernetes_version: str
        :param release_version: 发布版本
        :type release_version: str
        :param ucsctl_download_url: ucs-ctl工具下载链接
        :type ucsctl_download_url: str
        :param arch: 兼容CPU架构
        :type arch: str
        :param obs_endpoint: 对象存储服务访问端点
        :type obs_endpoint: str
        :param package_path: 软件包存储路径
        :type package_path: str
        :param images_package_path: 镜像包存储路径
        :type images_package_path: str
        :param target_version: 目标版本
        :type target_version: str
        """
        
        

        self._kubernetes_version = None
        self._release_version = None
        self._ucsctl_download_url = None
        self._arch = None
        self._obs_endpoint = None
        self._package_path = None
        self._images_package_path = None
        self._target_version = None
        self.discriminator = None

        if kubernetes_version is not None:
            self.kubernetes_version = kubernetes_version
        if release_version is not None:
            self.release_version = release_version
        if ucsctl_download_url is not None:
            self.ucsctl_download_url = ucsctl_download_url
        if arch is not None:
            self.arch = arch
        if obs_endpoint is not None:
            self.obs_endpoint = obs_endpoint
        if package_path is not None:
            self.package_path = package_path
        if images_package_path is not None:
            self.images_package_path = images_package_path
        if target_version is not None:
            self.target_version = target_version

    @property
    def kubernetes_version(self):
        r"""Gets the kubernetes_version of this OnPremisesVersionInfo.

        Kubernetes集群版本

        :return: The kubernetes_version of this OnPremisesVersionInfo.
        :rtype: str
        """
        return self._kubernetes_version

    @kubernetes_version.setter
    def kubernetes_version(self, kubernetes_version):
        r"""Sets the kubernetes_version of this OnPremisesVersionInfo.

        Kubernetes集群版本

        :param kubernetes_version: The kubernetes_version of this OnPremisesVersionInfo.
        :type kubernetes_version: str
        """
        self._kubernetes_version = kubernetes_version

    @property
    def release_version(self):
        r"""Gets the release_version of this OnPremisesVersionInfo.

        发布版本

        :return: The release_version of this OnPremisesVersionInfo.
        :rtype: str
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        r"""Sets the release_version of this OnPremisesVersionInfo.

        发布版本

        :param release_version: The release_version of this OnPremisesVersionInfo.
        :type release_version: str
        """
        self._release_version = release_version

    @property
    def ucsctl_download_url(self):
        r"""Gets the ucsctl_download_url of this OnPremisesVersionInfo.

        ucs-ctl工具下载链接

        :return: The ucsctl_download_url of this OnPremisesVersionInfo.
        :rtype: str
        """
        return self._ucsctl_download_url

    @ucsctl_download_url.setter
    def ucsctl_download_url(self, ucsctl_download_url):
        r"""Sets the ucsctl_download_url of this OnPremisesVersionInfo.

        ucs-ctl工具下载链接

        :param ucsctl_download_url: The ucsctl_download_url of this OnPremisesVersionInfo.
        :type ucsctl_download_url: str
        """
        self._ucsctl_download_url = ucsctl_download_url

    @property
    def arch(self):
        r"""Gets the arch of this OnPremisesVersionInfo.

        兼容CPU架构

        :return: The arch of this OnPremisesVersionInfo.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this OnPremisesVersionInfo.

        兼容CPU架构

        :param arch: The arch of this OnPremisesVersionInfo.
        :type arch: str
        """
        self._arch = arch

    @property
    def obs_endpoint(self):
        r"""Gets the obs_endpoint of this OnPremisesVersionInfo.

        对象存储服务访问端点

        :return: The obs_endpoint of this OnPremisesVersionInfo.
        :rtype: str
        """
        return self._obs_endpoint

    @obs_endpoint.setter
    def obs_endpoint(self, obs_endpoint):
        r"""Sets the obs_endpoint of this OnPremisesVersionInfo.

        对象存储服务访问端点

        :param obs_endpoint: The obs_endpoint of this OnPremisesVersionInfo.
        :type obs_endpoint: str
        """
        self._obs_endpoint = obs_endpoint

    @property
    def package_path(self):
        r"""Gets the package_path of this OnPremisesVersionInfo.

        软件包存储路径

        :return: The package_path of this OnPremisesVersionInfo.
        :rtype: str
        """
        return self._package_path

    @package_path.setter
    def package_path(self, package_path):
        r"""Sets the package_path of this OnPremisesVersionInfo.

        软件包存储路径

        :param package_path: The package_path of this OnPremisesVersionInfo.
        :type package_path: str
        """
        self._package_path = package_path

    @property
    def images_package_path(self):
        r"""Gets the images_package_path of this OnPremisesVersionInfo.

        镜像包存储路径

        :return: The images_package_path of this OnPremisesVersionInfo.
        :rtype: str
        """
        return self._images_package_path

    @images_package_path.setter
    def images_package_path(self, images_package_path):
        r"""Sets the images_package_path of this OnPremisesVersionInfo.

        镜像包存储路径

        :param images_package_path: The images_package_path of this OnPremisesVersionInfo.
        :type images_package_path: str
        """
        self._images_package_path = images_package_path

    @property
    def target_version(self):
        r"""Gets the target_version of this OnPremisesVersionInfo.

        目标版本

        :return: The target_version of this OnPremisesVersionInfo.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this OnPremisesVersionInfo.

        目标版本

        :param target_version: The target_version of this OnPremisesVersionInfo.
        :type target_version: str
        """
        self._target_version = target_version

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
        if not isinstance(other, OnPremisesVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
