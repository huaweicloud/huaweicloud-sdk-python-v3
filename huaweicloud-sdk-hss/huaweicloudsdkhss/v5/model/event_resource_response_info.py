# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventResourceResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'region_name': 'str',
        'vpc_id': 'str',
        'cloud_id': 'str',
        'vm_name': 'str',
        'vm_uuid': 'str',
        'container_id': 'str',
        'container_status': 'str',
        'pod_uid': 'str',
        'pod_name': 'str',
        'namespace': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'image_id': 'str',
        'image_name': 'str',
        'host_attr': 'str',
        'service': 'str',
        'micro_service': 'str',
        'sys_arch': 'str',
        'os_bit': 'str',
        'os_type': 'str',
        'os_name': 'str',
        'os_version': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'region_name': 'region_name',
        'vpc_id': 'vpc_id',
        'cloud_id': 'cloud_id',
        'vm_name': 'vm_name',
        'vm_uuid': 'vm_uuid',
        'container_id': 'container_id',
        'container_status': 'container_status',
        'pod_uid': 'pod_uid',
        'pod_name': 'pod_name',
        'namespace': 'namespace',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'image_id': 'image_id',
        'image_name': 'image_name',
        'host_attr': 'host_attr',
        'service': 'service',
        'micro_service': 'micro_service',
        'sys_arch': 'sys_arch',
        'os_bit': 'os_bit',
        'os_type': 'os_type',
        'os_name': 'os_name',
        'os_version': 'os_version'
    }

    def __init__(self, domain_id=None, project_id=None, enterprise_project_id=None, region_name=None, vpc_id=None, cloud_id=None, vm_name=None, vm_uuid=None, container_id=None, container_status=None, pod_uid=None, pod_name=None, namespace=None, cluster_id=None, cluster_name=None, image_id=None, image_name=None, host_attr=None, service=None, micro_service=None, sys_arch=None, os_bit=None, os_type=None, os_name=None, os_version=None):
        r"""EventResourceResponseInfo

        The model defined in huaweicloud sdk

        :param domain_id: **参数解释**： 租户账号ID **取值范围**： 字符长度1-256位 
        :type domain_id: str
        :param project_id: **参数解释**： 项目ID **取值范围**： 字符长度1-256位 
        :type project_id: str
        :param enterprise_project_id: **参数解释**： 企业项目ID **取值范围**： 字符长度1-256位 
        :type enterprise_project_id: str
        :param region_name: **参数解释**： Region名称 **取值范围**： 字符长度1-256位 
        :type region_name: str
        :param vpc_id: **参数解释**： VPC ID **取值范围**： 字符长度1-256位 
        :type vpc_id: str
        :param cloud_id: **参数解释**： 云主机ID **取值范围**： 字符长度1-256位 
        :type cloud_id: str
        :param vm_name: **参数解释**： 虚拟机名称 **取值范围**： 字符长度1-256位 
        :type vm_name: str
        :param vm_uuid: **参数解释**： 虚拟机UUID，即主机ID **取值范围**： 字符长度1-256位 
        :type vm_uuid: str
        :param container_id: **参数解释**： 容器ID **取值范围**： 字符长度1-256位 
        :type container_id: str
        :param container_status: **参数解释**： 容器状态 **取值范围**： 字符长度1-256位 
        :type container_status: str
        :param pod_uid: **参数解释**： pod uid **取值范围**： 字符长度1-256位 
        :type pod_uid: str
        :param pod_name: **参数解释**： pod name **取值范围**： 字符长度1-256位 
        :type pod_name: str
        :param namespace: **参数解释**： namespace **取值范围**： 字符长度1-256位 
        :type namespace: str
        :param cluster_id: **参数解释**： 集群ID **取值范围**： 字符长度1-256位 
        :type cluster_id: str
        :param cluster_name: **参数解释**： 集群名称 **取值范围**： 字符长度1-256位 
        :type cluster_name: str
        :param image_id: **参数解释**： 镜像ID **取值范围**： 字符长度1-256位 
        :type image_id: str
        :param image_name: **参数解释**： 镜像名称 **取值范围**： 字符长度1-256位 
        :type image_name: str
        :param host_attr: **参数解释**： 主机属性 **取值范围**： 字符长度1-256位 
        :type host_attr: str
        :param service: **参数解释**： 业务服务 **取值范围**： 字符长度1-256位 
        :type service: str
        :param micro_service: **参数解释**： 微服务 **取值范围**： 字符长度1-256位 
        :type micro_service: str
        :param sys_arch: **参数解释**： 系统CPU架构 **取值范围**： 字符长度1-256位 
        :type sys_arch: str
        :param os_bit: **参数解释**： 操作系统位数 **取值范围**： 字符长度1-256位 
        :type os_bit: str
        :param os_type: **参数解释**： 操作系统类型 **取值范围**： 字符长度1-256位 
        :type os_type: str
        :param os_name: **参数解释**： 操作系统名称 **取值范围**： 字符长度1-256位 
        :type os_name: str
        :param os_version: **参数解释**： 操作系统版本 **取值范围**： 字符长度1-256位 
        :type os_version: str
        """
        
        

        self._domain_id = None
        self._project_id = None
        self._enterprise_project_id = None
        self._region_name = None
        self._vpc_id = None
        self._cloud_id = None
        self._vm_name = None
        self._vm_uuid = None
        self._container_id = None
        self._container_status = None
        self._pod_uid = None
        self._pod_name = None
        self._namespace = None
        self._cluster_id = None
        self._cluster_name = None
        self._image_id = None
        self._image_name = None
        self._host_attr = None
        self._service = None
        self._micro_service = None
        self._sys_arch = None
        self._os_bit = None
        self._os_type = None
        self._os_name = None
        self._os_version = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if region_name is not None:
            self.region_name = region_name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if cloud_id is not None:
            self.cloud_id = cloud_id
        if vm_name is not None:
            self.vm_name = vm_name
        if vm_uuid is not None:
            self.vm_uuid = vm_uuid
        if container_id is not None:
            self.container_id = container_id
        if container_status is not None:
            self.container_status = container_status
        if pod_uid is not None:
            self.pod_uid = pod_uid
        if pod_name is not None:
            self.pod_name = pod_name
        if namespace is not None:
            self.namespace = namespace
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if host_attr is not None:
            self.host_attr = host_attr
        if service is not None:
            self.service = service
        if micro_service is not None:
            self.micro_service = micro_service
        if sys_arch is not None:
            self.sys_arch = sys_arch
        if os_bit is not None:
            self.os_bit = os_bit
        if os_type is not None:
            self.os_type = os_type
        if os_name is not None:
            self.os_name = os_name
        if os_version is not None:
            self.os_version = os_version

    @property
    def domain_id(self):
        r"""Gets the domain_id of this EventResourceResponseInfo.

        **参数解释**： 租户账号ID **取值范围**： 字符长度1-256位 

        :return: The domain_id of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this EventResourceResponseInfo.

        **参数解释**： 租户账号ID **取值范围**： 字符长度1-256位 

        :param domain_id: The domain_id of this EventResourceResponseInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this EventResourceResponseInfo.

        **参数解释**： 项目ID **取值范围**： 字符长度1-256位 

        :return: The project_id of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this EventResourceResponseInfo.

        **参数解释**： 项目ID **取值范围**： 字符长度1-256位 

        :param project_id: The project_id of this EventResourceResponseInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this EventResourceResponseInfo.

        **参数解释**： 企业项目ID **取值范围**： 字符长度1-256位 

        :return: The enterprise_project_id of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this EventResourceResponseInfo.

        **参数解释**： 企业项目ID **取值范围**： 字符长度1-256位 

        :param enterprise_project_id: The enterprise_project_id of this EventResourceResponseInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def region_name(self):
        r"""Gets the region_name of this EventResourceResponseInfo.

        **参数解释**： Region名称 **取值范围**： 字符长度1-256位 

        :return: The region_name of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this EventResourceResponseInfo.

        **参数解释**： Region名称 **取值范围**： 字符长度1-256位 

        :param region_name: The region_name of this EventResourceResponseInfo.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this EventResourceResponseInfo.

        **参数解释**： VPC ID **取值范围**： 字符长度1-256位 

        :return: The vpc_id of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this EventResourceResponseInfo.

        **参数解释**： VPC ID **取值范围**： 字符长度1-256位 

        :param vpc_id: The vpc_id of this EventResourceResponseInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def cloud_id(self):
        r"""Gets the cloud_id of this EventResourceResponseInfo.

        **参数解释**： 云主机ID **取值范围**： 字符长度1-256位 

        :return: The cloud_id of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._cloud_id

    @cloud_id.setter
    def cloud_id(self, cloud_id):
        r"""Sets the cloud_id of this EventResourceResponseInfo.

        **参数解释**： 云主机ID **取值范围**： 字符长度1-256位 

        :param cloud_id: The cloud_id of this EventResourceResponseInfo.
        :type cloud_id: str
        """
        self._cloud_id = cloud_id

    @property
    def vm_name(self):
        r"""Gets the vm_name of this EventResourceResponseInfo.

        **参数解释**： 虚拟机名称 **取值范围**： 字符长度1-256位 

        :return: The vm_name of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._vm_name

    @vm_name.setter
    def vm_name(self, vm_name):
        r"""Sets the vm_name of this EventResourceResponseInfo.

        **参数解释**： 虚拟机名称 **取值范围**： 字符长度1-256位 

        :param vm_name: The vm_name of this EventResourceResponseInfo.
        :type vm_name: str
        """
        self._vm_name = vm_name

    @property
    def vm_uuid(self):
        r"""Gets the vm_uuid of this EventResourceResponseInfo.

        **参数解释**： 虚拟机UUID，即主机ID **取值范围**： 字符长度1-256位 

        :return: The vm_uuid of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._vm_uuid

    @vm_uuid.setter
    def vm_uuid(self, vm_uuid):
        r"""Sets the vm_uuid of this EventResourceResponseInfo.

        **参数解释**： 虚拟机UUID，即主机ID **取值范围**： 字符长度1-256位 

        :param vm_uuid: The vm_uuid of this EventResourceResponseInfo.
        :type vm_uuid: str
        """
        self._vm_uuid = vm_uuid

    @property
    def container_id(self):
        r"""Gets the container_id of this EventResourceResponseInfo.

        **参数解释**： 容器ID **取值范围**： 字符长度1-256位 

        :return: The container_id of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this EventResourceResponseInfo.

        **参数解释**： 容器ID **取值范围**： 字符长度1-256位 

        :param container_id: The container_id of this EventResourceResponseInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_status(self):
        r"""Gets the container_status of this EventResourceResponseInfo.

        **参数解释**： 容器状态 **取值范围**： 字符长度1-256位 

        :return: The container_status of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._container_status

    @container_status.setter
    def container_status(self, container_status):
        r"""Sets the container_status of this EventResourceResponseInfo.

        **参数解释**： 容器状态 **取值范围**： 字符长度1-256位 

        :param container_status: The container_status of this EventResourceResponseInfo.
        :type container_status: str
        """
        self._container_status = container_status

    @property
    def pod_uid(self):
        r"""Gets the pod_uid of this EventResourceResponseInfo.

        **参数解释**： pod uid **取值范围**： 字符长度1-256位 

        :return: The pod_uid of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._pod_uid

    @pod_uid.setter
    def pod_uid(self, pod_uid):
        r"""Sets the pod_uid of this EventResourceResponseInfo.

        **参数解释**： pod uid **取值范围**： 字符长度1-256位 

        :param pod_uid: The pod_uid of this EventResourceResponseInfo.
        :type pod_uid: str
        """
        self._pod_uid = pod_uid

    @property
    def pod_name(self):
        r"""Gets the pod_name of this EventResourceResponseInfo.

        **参数解释**： pod name **取值范围**： 字符长度1-256位 

        :return: The pod_name of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this EventResourceResponseInfo.

        **参数解释**： pod name **取值范围**： 字符长度1-256位 

        :param pod_name: The pod_name of this EventResourceResponseInfo.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def namespace(self):
        r"""Gets the namespace of this EventResourceResponseInfo.

        **参数解释**： namespace **取值范围**： 字符长度1-256位 

        :return: The namespace of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this EventResourceResponseInfo.

        **参数解释**： namespace **取值范围**： 字符长度1-256位 

        :param namespace: The namespace of this EventResourceResponseInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this EventResourceResponseInfo.

        **参数解释**： 集群ID **取值范围**： 字符长度1-256位 

        :return: The cluster_id of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this EventResourceResponseInfo.

        **参数解释**： 集群ID **取值范围**： 字符长度1-256位 

        :param cluster_id: The cluster_id of this EventResourceResponseInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this EventResourceResponseInfo.

        **参数解释**： 集群名称 **取值范围**： 字符长度1-256位 

        :return: The cluster_name of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this EventResourceResponseInfo.

        **参数解释**： 集群名称 **取值范围**： 字符长度1-256位 

        :param cluster_name: The cluster_name of this EventResourceResponseInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def image_id(self):
        r"""Gets the image_id of this EventResourceResponseInfo.

        **参数解释**： 镜像ID **取值范围**： 字符长度1-256位 

        :return: The image_id of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this EventResourceResponseInfo.

        **参数解释**： 镜像ID **取值范围**： 字符长度1-256位 

        :param image_id: The image_id of this EventResourceResponseInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this EventResourceResponseInfo.

        **参数解释**： 镜像名称 **取值范围**： 字符长度1-256位 

        :return: The image_name of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this EventResourceResponseInfo.

        **参数解释**： 镜像名称 **取值范围**： 字符长度1-256位 

        :param image_name: The image_name of this EventResourceResponseInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def host_attr(self):
        r"""Gets the host_attr of this EventResourceResponseInfo.

        **参数解释**： 主机属性 **取值范围**： 字符长度1-256位 

        :return: The host_attr of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._host_attr

    @host_attr.setter
    def host_attr(self, host_attr):
        r"""Sets the host_attr of this EventResourceResponseInfo.

        **参数解释**： 主机属性 **取值范围**： 字符长度1-256位 

        :param host_attr: The host_attr of this EventResourceResponseInfo.
        :type host_attr: str
        """
        self._host_attr = host_attr

    @property
    def service(self):
        r"""Gets the service of this EventResourceResponseInfo.

        **参数解释**： 业务服务 **取值范围**： 字符长度1-256位 

        :return: The service of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this EventResourceResponseInfo.

        **参数解释**： 业务服务 **取值范围**： 字符长度1-256位 

        :param service: The service of this EventResourceResponseInfo.
        :type service: str
        """
        self._service = service

    @property
    def micro_service(self):
        r"""Gets the micro_service of this EventResourceResponseInfo.

        **参数解释**： 微服务 **取值范围**： 字符长度1-256位 

        :return: The micro_service of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._micro_service

    @micro_service.setter
    def micro_service(self, micro_service):
        r"""Sets the micro_service of this EventResourceResponseInfo.

        **参数解释**： 微服务 **取值范围**： 字符长度1-256位 

        :param micro_service: The micro_service of this EventResourceResponseInfo.
        :type micro_service: str
        """
        self._micro_service = micro_service

    @property
    def sys_arch(self):
        r"""Gets the sys_arch of this EventResourceResponseInfo.

        **参数解释**： 系统CPU架构 **取值范围**： 字符长度1-256位 

        :return: The sys_arch of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._sys_arch

    @sys_arch.setter
    def sys_arch(self, sys_arch):
        r"""Sets the sys_arch of this EventResourceResponseInfo.

        **参数解释**： 系统CPU架构 **取值范围**： 字符长度1-256位 

        :param sys_arch: The sys_arch of this EventResourceResponseInfo.
        :type sys_arch: str
        """
        self._sys_arch = sys_arch

    @property
    def os_bit(self):
        r"""Gets the os_bit of this EventResourceResponseInfo.

        **参数解释**： 操作系统位数 **取值范围**： 字符长度1-256位 

        :return: The os_bit of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        r"""Sets the os_bit of this EventResourceResponseInfo.

        **参数解释**： 操作系统位数 **取值范围**： 字符长度1-256位 

        :param os_bit: The os_bit of this EventResourceResponseInfo.
        :type os_bit: str
        """
        self._os_bit = os_bit

    @property
    def os_type(self):
        r"""Gets the os_type of this EventResourceResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： 字符长度1-256位 

        :return: The os_type of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this EventResourceResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： 字符长度1-256位 

        :param os_type: The os_type of this EventResourceResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_name(self):
        r"""Gets the os_name of this EventResourceResponseInfo.

        **参数解释**： 操作系统名称 **取值范围**： 字符长度1-256位 

        :return: The os_name of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this EventResourceResponseInfo.

        **参数解释**： 操作系统名称 **取值范围**： 字符长度1-256位 

        :param os_name: The os_name of this EventResourceResponseInfo.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def os_version(self):
        r"""Gets the os_version of this EventResourceResponseInfo.

        **参数解释**： 操作系统版本 **取值范围**： 字符长度1-256位 

        :return: The os_version of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this EventResourceResponseInfo.

        **参数解释**： 操作系统版本 **取值范围**： 字符长度1-256位 

        :param os_version: The os_version of this EventResourceResponseInfo.
        :type os_version: str
        """
        self._os_version = os_version

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
        if not isinstance(other, EventResourceResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
