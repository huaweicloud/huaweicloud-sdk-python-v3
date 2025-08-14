# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiCloudClusterCreateRequestBody:

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
        'provider': 'str',
        'server': 'str',
        'image_repo': 'str',
        'image_repo_username': 'str',
        'image_repo_password': 'str',
        'organization': 'str',
        'image_repo_type': 'str',
        'current_expiration_date': 'int',
        'certificate_expiration_date': 'int',
        'kube_config': 'str',
        'image_arch': 'str',
        'anp_proxy': 'str',
        'hostguard_proxy': 'str',
        'container_name': 'str',
        'dns_policy': 'str',
        'dns_config': 'str'
    }

    attribute_map = {
        'name': 'name',
        'provider': 'provider',
        'server': 'server',
        'image_repo': 'image_repo',
        'image_repo_username': 'image_repo_username',
        'image_repo_password': 'image_repo_password',
        'organization': 'organization',
        'image_repo_type': 'image_repo_type',
        'current_expiration_date': 'current_expiration_date',
        'certificate_expiration_date': 'certificate_expiration_date',
        'kube_config': 'kube_config',
        'image_arch': 'image_arch',
        'anp_proxy': 'anp_proxy',
        'hostguard_proxy': 'hostguard_proxy',
        'container_name': 'container_name',
        'dns_policy': 'dns_policy',
        'dns_config': 'dns_config'
    }

    def __init__(self, name=None, provider=None, server=None, image_repo=None, image_repo_username=None, image_repo_password=None, organization=None, image_repo_type=None, current_expiration_date=None, certificate_expiration_date=None, kube_config=None, image_arch=None, anp_proxy=None, hostguard_proxy=None, container_name=None, dns_policy=None, dns_config=None):
        r"""MultiCloudClusterCreateRequestBody

        The model defined in huaweicloud sdk

        :param name: 集群名称
        :type name: str
        :param provider: **参数解释** 集群服务商 **约束限制**   - ali：阿里。   - tencent：腾讯。   - azure：微软。   - aws：亚马逊。   - self_built_hw：华为自建。   - self_built_idc：IDC自建。  **取值范围** 字符长度范围0-64 **默认取值** 不涉及 
        :type provider: str
        :param server: 集群apiserver地址
        :type server: str
        :param image_repo: 镜像仓地址
        :type image_repo: str
        :param image_repo_username: 镜像仓用户名
        :type image_repo_username: str
        :param image_repo_password: 镜像仓密码
        :type image_repo_password: str
        :param organization: 组织
        :type organization: str
        :param image_repo_type: **参数解释** 镜像仓类型 **约束限制** - harbor：Harbor镜像仓。 - quay：Quay镜像仓。 - jfrog：Jfrog镜像仓。 - other：其他镜像仓。  **取值范围** 字符长度范围0-64 **默认取值** 不涉及 
        :type image_repo_type: str
        :param current_expiration_date: 当前有效期结束时间
        :type current_expiration_date: int
        :param certificate_expiration_date: 证书有效期结束时间
        :type certificate_expiration_date: int
        :param kube_config: kubeconfig文件
        :type kube_config: str
        :param image_arch: 镜像架构类型： - x86 - arm
        :type image_arch: str
        :param anp_proxy: Anp代理地址
        :type anp_proxy: str
        :param hostguard_proxy: Hostguard代理地址
        :type hostguard_proxy: str
        :param container_name: 容器名称
        :type container_name: str
        :param dns_policy: DNS策略： - default：继承集群节点的域名解析配置 - clusterfirst：查询集群内部的CoreDNS服务 - clusterfirstwithhostnet：强制在hostNetwork网络模式下使用ClusterFirst策略 - none：忽略集群的DNS策略，使用自定义DNS配置
        :type dns_policy: str
        :param dns_config: 自定义DNS配置，一个或多个IP地址，以分号分隔
        :type dns_config: str
        """
        
        

        self._name = None
        self._provider = None
        self._server = None
        self._image_repo = None
        self._image_repo_username = None
        self._image_repo_password = None
        self._organization = None
        self._image_repo_type = None
        self._current_expiration_date = None
        self._certificate_expiration_date = None
        self._kube_config = None
        self._image_arch = None
        self._anp_proxy = None
        self._hostguard_proxy = None
        self._container_name = None
        self._dns_policy = None
        self._dns_config = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if provider is not None:
            self.provider = provider
        if server is not None:
            self.server = server
        if image_repo is not None:
            self.image_repo = image_repo
        if image_repo_username is not None:
            self.image_repo_username = image_repo_username
        if image_repo_password is not None:
            self.image_repo_password = image_repo_password
        if organization is not None:
            self.organization = organization
        if image_repo_type is not None:
            self.image_repo_type = image_repo_type
        if current_expiration_date is not None:
            self.current_expiration_date = current_expiration_date
        if certificate_expiration_date is not None:
            self.certificate_expiration_date = certificate_expiration_date
        self.kube_config = kube_config
        if image_arch is not None:
            self.image_arch = image_arch
        if anp_proxy is not None:
            self.anp_proxy = anp_proxy
        if hostguard_proxy is not None:
            self.hostguard_proxy = hostguard_proxy
        if container_name is not None:
            self.container_name = container_name
        if dns_policy is not None:
            self.dns_policy = dns_policy
        if dns_config is not None:
            self.dns_config = dns_config

    @property
    def name(self):
        r"""Gets the name of this MultiCloudClusterCreateRequestBody.

        集群名称

        :return: The name of this MultiCloudClusterCreateRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MultiCloudClusterCreateRequestBody.

        集群名称

        :param name: The name of this MultiCloudClusterCreateRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def provider(self):
        r"""Gets the provider of this MultiCloudClusterCreateRequestBody.

        **参数解释** 集群服务商 **约束限制**   - ali：阿里。   - tencent：腾讯。   - azure：微软。   - aws：亚马逊。   - self_built_hw：华为自建。   - self_built_idc：IDC自建。  **取值范围** 字符长度范围0-64 **默认取值** 不涉及 

        :return: The provider of this MultiCloudClusterCreateRequestBody.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this MultiCloudClusterCreateRequestBody.

        **参数解释** 集群服务商 **约束限制**   - ali：阿里。   - tencent：腾讯。   - azure：微软。   - aws：亚马逊。   - self_built_hw：华为自建。   - self_built_idc：IDC自建。  **取值范围** 字符长度范围0-64 **默认取值** 不涉及 

        :param provider: The provider of this MultiCloudClusterCreateRequestBody.
        :type provider: str
        """
        self._provider = provider

    @property
    def server(self):
        r"""Gets the server of this MultiCloudClusterCreateRequestBody.

        集群apiserver地址

        :return: The server of this MultiCloudClusterCreateRequestBody.
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        r"""Sets the server of this MultiCloudClusterCreateRequestBody.

        集群apiserver地址

        :param server: The server of this MultiCloudClusterCreateRequestBody.
        :type server: str
        """
        self._server = server

    @property
    def image_repo(self):
        r"""Gets the image_repo of this MultiCloudClusterCreateRequestBody.

        镜像仓地址

        :return: The image_repo of this MultiCloudClusterCreateRequestBody.
        :rtype: str
        """
        return self._image_repo

    @image_repo.setter
    def image_repo(self, image_repo):
        r"""Sets the image_repo of this MultiCloudClusterCreateRequestBody.

        镜像仓地址

        :param image_repo: The image_repo of this MultiCloudClusterCreateRequestBody.
        :type image_repo: str
        """
        self._image_repo = image_repo

    @property
    def image_repo_username(self):
        r"""Gets the image_repo_username of this MultiCloudClusterCreateRequestBody.

        镜像仓用户名

        :return: The image_repo_username of this MultiCloudClusterCreateRequestBody.
        :rtype: str
        """
        return self._image_repo_username

    @image_repo_username.setter
    def image_repo_username(self, image_repo_username):
        r"""Sets the image_repo_username of this MultiCloudClusterCreateRequestBody.

        镜像仓用户名

        :param image_repo_username: The image_repo_username of this MultiCloudClusterCreateRequestBody.
        :type image_repo_username: str
        """
        self._image_repo_username = image_repo_username

    @property
    def image_repo_password(self):
        r"""Gets the image_repo_password of this MultiCloudClusterCreateRequestBody.

        镜像仓密码

        :return: The image_repo_password of this MultiCloudClusterCreateRequestBody.
        :rtype: str
        """
        return self._image_repo_password

    @image_repo_password.setter
    def image_repo_password(self, image_repo_password):
        r"""Sets the image_repo_password of this MultiCloudClusterCreateRequestBody.

        镜像仓密码

        :param image_repo_password: The image_repo_password of this MultiCloudClusterCreateRequestBody.
        :type image_repo_password: str
        """
        self._image_repo_password = image_repo_password

    @property
    def organization(self):
        r"""Gets the organization of this MultiCloudClusterCreateRequestBody.

        组织

        :return: The organization of this MultiCloudClusterCreateRequestBody.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        r"""Sets the organization of this MultiCloudClusterCreateRequestBody.

        组织

        :param organization: The organization of this MultiCloudClusterCreateRequestBody.
        :type organization: str
        """
        self._organization = organization

    @property
    def image_repo_type(self):
        r"""Gets the image_repo_type of this MultiCloudClusterCreateRequestBody.

        **参数解释** 镜像仓类型 **约束限制** - harbor：Harbor镜像仓。 - quay：Quay镜像仓。 - jfrog：Jfrog镜像仓。 - other：其他镜像仓。  **取值范围** 字符长度范围0-64 **默认取值** 不涉及 

        :return: The image_repo_type of this MultiCloudClusterCreateRequestBody.
        :rtype: str
        """
        return self._image_repo_type

    @image_repo_type.setter
    def image_repo_type(self, image_repo_type):
        r"""Sets the image_repo_type of this MultiCloudClusterCreateRequestBody.

        **参数解释** 镜像仓类型 **约束限制** - harbor：Harbor镜像仓。 - quay：Quay镜像仓。 - jfrog：Jfrog镜像仓。 - other：其他镜像仓。  **取值范围** 字符长度范围0-64 **默认取值** 不涉及 

        :param image_repo_type: The image_repo_type of this MultiCloudClusterCreateRequestBody.
        :type image_repo_type: str
        """
        self._image_repo_type = image_repo_type

    @property
    def current_expiration_date(self):
        r"""Gets the current_expiration_date of this MultiCloudClusterCreateRequestBody.

        当前有效期结束时间

        :return: The current_expiration_date of this MultiCloudClusterCreateRequestBody.
        :rtype: int
        """
        return self._current_expiration_date

    @current_expiration_date.setter
    def current_expiration_date(self, current_expiration_date):
        r"""Sets the current_expiration_date of this MultiCloudClusterCreateRequestBody.

        当前有效期结束时间

        :param current_expiration_date: The current_expiration_date of this MultiCloudClusterCreateRequestBody.
        :type current_expiration_date: int
        """
        self._current_expiration_date = current_expiration_date

    @property
    def certificate_expiration_date(self):
        r"""Gets the certificate_expiration_date of this MultiCloudClusterCreateRequestBody.

        证书有效期结束时间

        :return: The certificate_expiration_date of this MultiCloudClusterCreateRequestBody.
        :rtype: int
        """
        return self._certificate_expiration_date

    @certificate_expiration_date.setter
    def certificate_expiration_date(self, certificate_expiration_date):
        r"""Sets the certificate_expiration_date of this MultiCloudClusterCreateRequestBody.

        证书有效期结束时间

        :param certificate_expiration_date: The certificate_expiration_date of this MultiCloudClusterCreateRequestBody.
        :type certificate_expiration_date: int
        """
        self._certificate_expiration_date = certificate_expiration_date

    @property
    def kube_config(self):
        r"""Gets the kube_config of this MultiCloudClusterCreateRequestBody.

        kubeconfig文件

        :return: The kube_config of this MultiCloudClusterCreateRequestBody.
        :rtype: str
        """
        return self._kube_config

    @kube_config.setter
    def kube_config(self, kube_config):
        r"""Sets the kube_config of this MultiCloudClusterCreateRequestBody.

        kubeconfig文件

        :param kube_config: The kube_config of this MultiCloudClusterCreateRequestBody.
        :type kube_config: str
        """
        self._kube_config = kube_config

    @property
    def image_arch(self):
        r"""Gets the image_arch of this MultiCloudClusterCreateRequestBody.

        镜像架构类型： - x86 - arm

        :return: The image_arch of this MultiCloudClusterCreateRequestBody.
        :rtype: str
        """
        return self._image_arch

    @image_arch.setter
    def image_arch(self, image_arch):
        r"""Sets the image_arch of this MultiCloudClusterCreateRequestBody.

        镜像架构类型： - x86 - arm

        :param image_arch: The image_arch of this MultiCloudClusterCreateRequestBody.
        :type image_arch: str
        """
        self._image_arch = image_arch

    @property
    def anp_proxy(self):
        r"""Gets the anp_proxy of this MultiCloudClusterCreateRequestBody.

        Anp代理地址

        :return: The anp_proxy of this MultiCloudClusterCreateRequestBody.
        :rtype: str
        """
        return self._anp_proxy

    @anp_proxy.setter
    def anp_proxy(self, anp_proxy):
        r"""Sets the anp_proxy of this MultiCloudClusterCreateRequestBody.

        Anp代理地址

        :param anp_proxy: The anp_proxy of this MultiCloudClusterCreateRequestBody.
        :type anp_proxy: str
        """
        self._anp_proxy = anp_proxy

    @property
    def hostguard_proxy(self):
        r"""Gets the hostguard_proxy of this MultiCloudClusterCreateRequestBody.

        Hostguard代理地址

        :return: The hostguard_proxy of this MultiCloudClusterCreateRequestBody.
        :rtype: str
        """
        return self._hostguard_proxy

    @hostguard_proxy.setter
    def hostguard_proxy(self, hostguard_proxy):
        r"""Sets the hostguard_proxy of this MultiCloudClusterCreateRequestBody.

        Hostguard代理地址

        :param hostguard_proxy: The hostguard_proxy of this MultiCloudClusterCreateRequestBody.
        :type hostguard_proxy: str
        """
        self._hostguard_proxy = hostguard_proxy

    @property
    def container_name(self):
        r"""Gets the container_name of this MultiCloudClusterCreateRequestBody.

        容器名称

        :return: The container_name of this MultiCloudClusterCreateRequestBody.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this MultiCloudClusterCreateRequestBody.

        容器名称

        :param container_name: The container_name of this MultiCloudClusterCreateRequestBody.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def dns_policy(self):
        r"""Gets the dns_policy of this MultiCloudClusterCreateRequestBody.

        DNS策略： - default：继承集群节点的域名解析配置 - clusterfirst：查询集群内部的CoreDNS服务 - clusterfirstwithhostnet：强制在hostNetwork网络模式下使用ClusterFirst策略 - none：忽略集群的DNS策略，使用自定义DNS配置

        :return: The dns_policy of this MultiCloudClusterCreateRequestBody.
        :rtype: str
        """
        return self._dns_policy

    @dns_policy.setter
    def dns_policy(self, dns_policy):
        r"""Sets the dns_policy of this MultiCloudClusterCreateRequestBody.

        DNS策略： - default：继承集群节点的域名解析配置 - clusterfirst：查询集群内部的CoreDNS服务 - clusterfirstwithhostnet：强制在hostNetwork网络模式下使用ClusterFirst策略 - none：忽略集群的DNS策略，使用自定义DNS配置

        :param dns_policy: The dns_policy of this MultiCloudClusterCreateRequestBody.
        :type dns_policy: str
        """
        self._dns_policy = dns_policy

    @property
    def dns_config(self):
        r"""Gets the dns_config of this MultiCloudClusterCreateRequestBody.

        自定义DNS配置，一个或多个IP地址，以分号分隔

        :return: The dns_config of this MultiCloudClusterCreateRequestBody.
        :rtype: str
        """
        return self._dns_config

    @dns_config.setter
    def dns_config(self, dns_config):
        r"""Sets the dns_config of this MultiCloudClusterCreateRequestBody.

        自定义DNS配置，一个或多个IP地址，以分号分隔

        :param dns_config: The dns_config of this MultiCloudClusterCreateRequestBody.
        :type dns_config: str
        """
        self._dns_config = dns_config

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
        if not isinstance(other, MultiCloudClusterCreateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
