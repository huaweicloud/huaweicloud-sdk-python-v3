# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulAffectImagesResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'image_name': 'str',
        'vul_id': 'str',
        'repair_necessity': 'str',
        'container_num': 'int',
        'image_digest': 'str',
        'image_version': 'str',
        'agent_id': 'str',
        'status': 'str',
        'first_scan_time': 'str',
        'latest_scan_time': 'str',
        'image_type': 'str',
        'image_size': 'str',
        'organization': 'str',
        'registry_type': 'str',
        'registry_name': 'str',
        'is_multi_arch': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'image_name': 'image_name',
        'vul_id': 'vul_id',
        'repair_necessity': 'repair_necessity',
        'container_num': 'container_num',
        'image_digest': 'image_digest',
        'image_version': 'image_version',
        'agent_id': 'agent_id',
        'status': 'status',
        'first_scan_time': 'first_scan_time',
        'latest_scan_time': 'latest_scan_time',
        'image_type': 'image_type',
        'image_size': 'image_size',
        'organization': 'organization',
        'registry_type': 'registry_type',
        'registry_name': 'registry_name',
        'is_multi_arch': 'is_multi_arch',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name'
    }

    def __init__(self, image_id=None, image_name=None, vul_id=None, repair_necessity=None, container_num=None, image_digest=None, image_version=None, agent_id=None, status=None, first_scan_time=None, latest_scan_time=None, image_type=None, image_size=None, organization=None, registry_type=None, registry_name=None, is_multi_arch=None, cluster_id=None, cluster_name=None):
        r"""VulAffectImagesResponseInfo

        The model defined in huaweicloud sdk

        :param image_id: **参数解释**: 镜像id **取值范围**: 字符长度0-256位 
        :type image_id: str
        :param image_name: **参数解释**: 镜像名称 **取值范围**: 字符长度0-512位 
        :type image_name: str
        :param vul_id: **参数解释**: 漏洞id **取值范围**: 字符长度0-256位 
        :type vul_id: str
        :param repair_necessity: **参数解释**: 危险程度 **取值范围**: - Low：低危 - Medium：中危 - High：高危 - Critical：严重 
        :type repair_necessity: str
        :param container_num: **参数解释**: 关联容器数 **取值范围**: 取值0-2147483547 
        :type container_num: int
        :param image_digest: **参数解释**: 镜像标识 **取值范围**: 字符长度0-256位 
        :type image_digest: str
        :param image_version: **参数解释**: 镜像版本 **取值范围**: 字符长度0-64位 
        :type image_version: str
        :param agent_id: **参数解释**: Agent ID **取值范围**: 字符长度0-128位 
        :type agent_id: str
        :param status: **参数解释**: 漏洞当前状态 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 
        :type status: str
        :param first_scan_time: **参数解释**: 首次扫描时间（时间戳，单位为毫秒） **取值范围**: 字符长度0-32位 
        :type first_scan_time: str
        :param latest_scan_time: **参数解释**: 最近扫描时间（时间戳，单位为毫秒） **取值范围**: 字符长度0-32位 
        :type latest_scan_time: str
        :param image_type: **参数解释**: 镜像类型 **取值范围**: - local_image：本地镜像 - registry：仓库镜像 - cicd：CI/CD镜像 
        :type image_type: str
        :param image_size: **参数解释**: 镜像大小 **取值范围**: 字符长度0-128位 
        :type image_size: str
        :param organization: **参数解释**: 所属组织 **取值范围**: 字符长度0-256位 
        :type organization: str
        :param registry_type: **参数解释**: 镜像仓类型 **取值范围**: - Harbor：harbor - Jfrog：jfrog - SwrPrivate：swr私有 - SwrShared：swr共享 - SwrEnterprise：swr企业 - Other：其他仓库 
        :type registry_type: str
        :param registry_name: **参数解释**: 仓库名称 **取值范围**: 字符长度0-256位 
        :type registry_name: str
        :param is_multi_arch: **参数解释**: 是否为多架构 **取值范围**: - true：是多架构 - false：不是多架构 
        :type is_multi_arch: str
        :param cluster_id: **参数解释**: 集群ID **取值范围**: 字符长度0-128位 
        :type cluster_id: str
        :param cluster_name: **参数解释**: 集群名称 **取值范围**: 字符长度0-256位 
        :type cluster_name: str
        """
        
        

        self._image_id = None
        self._image_name = None
        self._vul_id = None
        self._repair_necessity = None
        self._container_num = None
        self._image_digest = None
        self._image_version = None
        self._agent_id = None
        self._status = None
        self._first_scan_time = None
        self._latest_scan_time = None
        self._image_type = None
        self._image_size = None
        self._organization = None
        self._registry_type = None
        self._registry_name = None
        self._is_multi_arch = None
        self._cluster_id = None
        self._cluster_name = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if vul_id is not None:
            self.vul_id = vul_id
        if repair_necessity is not None:
            self.repair_necessity = repair_necessity
        if container_num is not None:
            self.container_num = container_num
        if image_digest is not None:
            self.image_digest = image_digest
        if image_version is not None:
            self.image_version = image_version
        if agent_id is not None:
            self.agent_id = agent_id
        if status is not None:
            self.status = status
        if first_scan_time is not None:
            self.first_scan_time = first_scan_time
        if latest_scan_time is not None:
            self.latest_scan_time = latest_scan_time
        if image_type is not None:
            self.image_type = image_type
        if image_size is not None:
            self.image_size = image_size
        if organization is not None:
            self.organization = organization
        if registry_type is not None:
            self.registry_type = registry_type
        if registry_name is not None:
            self.registry_name = registry_name
        if is_multi_arch is not None:
            self.is_multi_arch = is_multi_arch
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name

    @property
    def image_id(self):
        r"""Gets the image_id of this VulAffectImagesResponseInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-256位 

        :return: The image_id of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this VulAffectImagesResponseInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-256位 

        :param image_id: The image_id of this VulAffectImagesResponseInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this VulAffectImagesResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-512位 

        :return: The image_name of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this VulAffectImagesResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-512位 

        :param image_name: The image_name of this VulAffectImagesResponseInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def vul_id(self):
        r"""Gets the vul_id of this VulAffectImagesResponseInfo.

        **参数解释**: 漏洞id **取值范围**: 字符长度0-256位 

        :return: The vul_id of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this VulAffectImagesResponseInfo.

        **参数解释**: 漏洞id **取值范围**: 字符长度0-256位 

        :param vul_id: The vul_id of this VulAffectImagesResponseInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def repair_necessity(self):
        r"""Gets the repair_necessity of this VulAffectImagesResponseInfo.

        **参数解释**: 危险程度 **取值范围**: - Low：低危 - Medium：中危 - High：高危 - Critical：严重 

        :return: The repair_necessity of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._repair_necessity

    @repair_necessity.setter
    def repair_necessity(self, repair_necessity):
        r"""Sets the repair_necessity of this VulAffectImagesResponseInfo.

        **参数解释**: 危险程度 **取值范围**: - Low：低危 - Medium：中危 - High：高危 - Critical：严重 

        :param repair_necessity: The repair_necessity of this VulAffectImagesResponseInfo.
        :type repair_necessity: str
        """
        self._repair_necessity = repair_necessity

    @property
    def container_num(self):
        r"""Gets the container_num of this VulAffectImagesResponseInfo.

        **参数解释**: 关联容器数 **取值范围**: 取值0-2147483547 

        :return: The container_num of this VulAffectImagesResponseInfo.
        :rtype: int
        """
        return self._container_num

    @container_num.setter
    def container_num(self, container_num):
        r"""Sets the container_num of this VulAffectImagesResponseInfo.

        **参数解释**: 关联容器数 **取值范围**: 取值0-2147483547 

        :param container_num: The container_num of this VulAffectImagesResponseInfo.
        :type container_num: int
        """
        self._container_num = container_num

    @property
    def image_digest(self):
        r"""Gets the image_digest of this VulAffectImagesResponseInfo.

        **参数解释**: 镜像标识 **取值范围**: 字符长度0-256位 

        :return: The image_digest of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        r"""Sets the image_digest of this VulAffectImagesResponseInfo.

        **参数解释**: 镜像标识 **取值范围**: 字符长度0-256位 

        :param image_digest: The image_digest of this VulAffectImagesResponseInfo.
        :type image_digest: str
        """
        self._image_digest = image_digest

    @property
    def image_version(self):
        r"""Gets the image_version of this VulAffectImagesResponseInfo.

        **参数解释**: 镜像版本 **取值范围**: 字符长度0-64位 

        :return: The image_version of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this VulAffectImagesResponseInfo.

        **参数解释**: 镜像版本 **取值范围**: 字符长度0-64位 

        :param image_version: The image_version of this VulAffectImagesResponseInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def agent_id(self):
        r"""Gets the agent_id of this VulAffectImagesResponseInfo.

        **参数解释**: Agent ID **取值范围**: 字符长度0-128位 

        :return: The agent_id of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this VulAffectImagesResponseInfo.

        **参数解释**: Agent ID **取值范围**: 字符长度0-128位 

        :param agent_id: The agent_id of this VulAffectImagesResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def status(self):
        r"""Gets the status of this VulAffectImagesResponseInfo.

        **参数解释**: 漏洞当前状态 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 

        :return: The status of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VulAffectImagesResponseInfo.

        **参数解释**: 漏洞当前状态 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 

        :param status: The status of this VulAffectImagesResponseInfo.
        :type status: str
        """
        self._status = status

    @property
    def first_scan_time(self):
        r"""Gets the first_scan_time of this VulAffectImagesResponseInfo.

        **参数解释**: 首次扫描时间（时间戳，单位为毫秒） **取值范围**: 字符长度0-32位 

        :return: The first_scan_time of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._first_scan_time

    @first_scan_time.setter
    def first_scan_time(self, first_scan_time):
        r"""Sets the first_scan_time of this VulAffectImagesResponseInfo.

        **参数解释**: 首次扫描时间（时间戳，单位为毫秒） **取值范围**: 字符长度0-32位 

        :param first_scan_time: The first_scan_time of this VulAffectImagesResponseInfo.
        :type first_scan_time: str
        """
        self._first_scan_time = first_scan_time

    @property
    def latest_scan_time(self):
        r"""Gets the latest_scan_time of this VulAffectImagesResponseInfo.

        **参数解释**: 最近扫描时间（时间戳，单位为毫秒） **取值范围**: 字符长度0-32位 

        :return: The latest_scan_time of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._latest_scan_time

    @latest_scan_time.setter
    def latest_scan_time(self, latest_scan_time):
        r"""Sets the latest_scan_time of this VulAffectImagesResponseInfo.

        **参数解释**: 最近扫描时间（时间戳，单位为毫秒） **取值范围**: 字符长度0-32位 

        :param latest_scan_time: The latest_scan_time of this VulAffectImagesResponseInfo.
        :type latest_scan_time: str
        """
        self._latest_scan_time = latest_scan_time

    @property
    def image_type(self):
        r"""Gets the image_type of this VulAffectImagesResponseInfo.

        **参数解释**: 镜像类型 **取值范围**: - local_image：本地镜像 - registry：仓库镜像 - cicd：CI/CD镜像 

        :return: The image_type of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this VulAffectImagesResponseInfo.

        **参数解释**: 镜像类型 **取值范围**: - local_image：本地镜像 - registry：仓库镜像 - cicd：CI/CD镜像 

        :param image_type: The image_type of this VulAffectImagesResponseInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def image_size(self):
        r"""Gets the image_size of this VulAffectImagesResponseInfo.

        **参数解释**: 镜像大小 **取值范围**: 字符长度0-128位 

        :return: The image_size of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this VulAffectImagesResponseInfo.

        **参数解释**: 镜像大小 **取值范围**: 字符长度0-128位 

        :param image_size: The image_size of this VulAffectImagesResponseInfo.
        :type image_size: str
        """
        self._image_size = image_size

    @property
    def organization(self):
        r"""Gets the organization of this VulAffectImagesResponseInfo.

        **参数解释**: 所属组织 **取值范围**: 字符长度0-256位 

        :return: The organization of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        r"""Sets the organization of this VulAffectImagesResponseInfo.

        **参数解释**: 所属组织 **取值范围**: 字符长度0-256位 

        :param organization: The organization of this VulAffectImagesResponseInfo.
        :type organization: str
        """
        self._organization = organization

    @property
    def registry_type(self):
        r"""Gets the registry_type of this VulAffectImagesResponseInfo.

        **参数解释**: 镜像仓类型 **取值范围**: - Harbor：harbor - Jfrog：jfrog - SwrPrivate：swr私有 - SwrShared：swr共享 - SwrEnterprise：swr企业 - Other：其他仓库 

        :return: The registry_type of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._registry_type

    @registry_type.setter
    def registry_type(self, registry_type):
        r"""Sets the registry_type of this VulAffectImagesResponseInfo.

        **参数解释**: 镜像仓类型 **取值范围**: - Harbor：harbor - Jfrog：jfrog - SwrPrivate：swr私有 - SwrShared：swr共享 - SwrEnterprise：swr企业 - Other：其他仓库 

        :param registry_type: The registry_type of this VulAffectImagesResponseInfo.
        :type registry_type: str
        """
        self._registry_type = registry_type

    @property
    def registry_name(self):
        r"""Gets the registry_name of this VulAffectImagesResponseInfo.

        **参数解释**: 仓库名称 **取值范围**: 字符长度0-256位 

        :return: The registry_name of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        r"""Sets the registry_name of this VulAffectImagesResponseInfo.

        **参数解释**: 仓库名称 **取值范围**: 字符长度0-256位 

        :param registry_name: The registry_name of this VulAffectImagesResponseInfo.
        :type registry_name: str
        """
        self._registry_name = registry_name

    @property
    def is_multi_arch(self):
        r"""Gets the is_multi_arch of this VulAffectImagesResponseInfo.

        **参数解释**: 是否为多架构 **取值范围**: - true：是多架构 - false：不是多架构 

        :return: The is_multi_arch of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._is_multi_arch

    @is_multi_arch.setter
    def is_multi_arch(self, is_multi_arch):
        r"""Sets the is_multi_arch of this VulAffectImagesResponseInfo.

        **参数解释**: 是否为多架构 **取值范围**: - true：是多架构 - false：不是多架构 

        :param is_multi_arch: The is_multi_arch of this VulAffectImagesResponseInfo.
        :type is_multi_arch: str
        """
        self._is_multi_arch = is_multi_arch

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this VulAffectImagesResponseInfo.

        **参数解释**: 集群ID **取值范围**: 字符长度0-128位 

        :return: The cluster_id of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this VulAffectImagesResponseInfo.

        **参数解释**: 集群ID **取值范围**: 字符长度0-128位 

        :param cluster_id: The cluster_id of this VulAffectImagesResponseInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this VulAffectImagesResponseInfo.

        **参数解释**: 集群名称 **取值范围**: 字符长度0-256位 

        :return: The cluster_name of this VulAffectImagesResponseInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this VulAffectImagesResponseInfo.

        **参数解释**: 集群名称 **取值范围**: 字符长度0-256位 

        :param cluster_name: The cluster_name of this VulAffectImagesResponseInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

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
        if not isinstance(other, VulAffectImagesResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
