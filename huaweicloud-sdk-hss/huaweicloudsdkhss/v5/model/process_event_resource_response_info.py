# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessEventResourceResponseInfo:

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
        'image_id': 'str',
        'image_name': 'str',
        'host_attr': 'str',
        'service': 'str',
        'micro_service': 'str',
        'sys_arch': 'str',
        'os_bit': 'str',
        'os_type': 'str',
        'os_name': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'public_ip': 'str',
        'host_id': 'str',
        'pod_uid': 'str',
        'pod_name': 'str',
        'namespace': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'asset_value': 'str',
        'container_status': 'str',
        'os_version': 'str',
        'agent_version': 'str'
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
        'image_id': 'image_id',
        'image_name': 'image_name',
        'host_attr': 'host_attr',
        'service': 'service',
        'micro_service': 'micro_service',
        'sys_arch': 'sys_arch',
        'os_bit': 'os_bit',
        'os_type': 'os_type',
        'os_name': 'os_name',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'public_ip': 'public_ip',
        'host_id': 'host_id',
        'pod_uid': 'pod_uid',
        'pod_name': 'pod_name',
        'namespace': 'namespace',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'asset_value': 'asset_value',
        'container_status': 'container_status',
        'os_version': 'os_version',
        'agent_version': 'agent_version'
    }

    def __init__(self, domain_id=None, project_id=None, enterprise_project_id=None, region_name=None, vpc_id=None, cloud_id=None, vm_name=None, vm_uuid=None, container_id=None, image_id=None, image_name=None, host_attr=None, service=None, micro_service=None, sys_arch=None, os_bit=None, os_type=None, os_name=None, host_name=None, host_ip=None, public_ip=None, host_id=None, pod_uid=None, pod_name=None, namespace=None, cluster_id=None, cluster_name=None, asset_value=None, container_status=None, os_version=None, agent_version=None):
        r"""ProcessEventResourceResponseInfo

        The model defined in huaweicloud sdk

        :param domain_id: **参数解释**： 租户账号ID **取值范围**： 字符长度1-64位 
        :type domain_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param region_name: Region ID
        :type region_name: str
        :param vpc_id: **参数解释**： VPC ID **取值范围**： 字符长度1-64位 
        :type vpc_id: str
        :param cloud_id: **参数解释**： 云主机ID **取值范围**： 字符长度1-64位 
        :type cloud_id: str
        :param vm_name: **参数解释**： 虚拟机名称 **取值范围**： 字符长度1-64位 
        :type vm_name: str
        :param vm_uuid: **参数解释**： 虚拟机UUID **取值范围**： 字符长度1-64位 
        :type vm_uuid: str
        :param container_id: **参数解释**: 容器ID **取值范围**: 字符长度1-128位 
        :type container_id: str
        :param image_id: **参数解释**： 镜像ID **取值范围**： 字符长度1-64位 
        :type image_id: str
        :param image_name: **参数解释**： 镜像名称，只有容器类型的告警有 **取值范围**： 字符长度1-256位 
        :type image_name: str
        :param host_attr: **参数解释**： 主机属性 **取值范围**： 字符长度1-64位 
        :type host_attr: str
        :param service: **参数解释**： 业务服务 **取值范围**： 字符长度1-64位 
        :type service: str
        :param micro_service: **参数解释**： 微服务 **取值范围**： 字符长度1-64位 
        :type micro_service: str
        :param sys_arch: **参数解释**： 系统CPU架构 **取值范围**： 字符长度1-64位 
        :type sys_arch: str
        :param os_bit: **参数解释**： 操作系统位数 **取值范围**： 字符长度1-64位 
        :type os_bit: str
        :param os_type: **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 
        :type os_type: str
        :param os_name: 操作系统名称
        :type os_name: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param host_ip: **参数解释**: 主机IP **取值范围**: 字符长度1-128位 
        :type host_ip: str
        :param public_ip: **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 
        :type public_ip: str
        :param host_id: **参数解释**： 主机ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param pod_uid: **参数解释**： pod uid **取值范围**： 字符长度1-64位 
        :type pod_uid: str
        :param pod_name: **参数解释**： pod name **取值范围**： 字符长度1-64位 
        :type pod_name: str
        :param namespace: **参数解释**： 名称空间 **取值范围**： 字符长度1-64位 
        :type namespace: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param container_status: 容器状态
        :type container_status: str
        :param os_version: 系统版本
        :type os_version: str
        :param agent_version: agent版本
        :type agent_version: str
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
        self._image_id = None
        self._image_name = None
        self._host_attr = None
        self._service = None
        self._micro_service = None
        self._sys_arch = None
        self._os_bit = None
        self._os_type = None
        self._os_name = None
        self._host_name = None
        self._host_ip = None
        self._public_ip = None
        self._host_id = None
        self._pod_uid = None
        self._pod_name = None
        self._namespace = None
        self._cluster_id = None
        self._cluster_name = None
        self._asset_value = None
        self._container_status = None
        self._os_version = None
        self._agent_version = None
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
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if host_id is not None:
            self.host_id = host_id
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
        if asset_value is not None:
            self.asset_value = asset_value
        if container_status is not None:
            self.container_status = container_status
        if os_version is not None:
            self.os_version = os_version
        if agent_version is not None:
            self.agent_version = agent_version

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ProcessEventResourceResponseInfo.

        **参数解释**： 租户账号ID **取值范围**： 字符长度1-64位 

        :return: The domain_id of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ProcessEventResourceResponseInfo.

        **参数解释**： 租户账号ID **取值范围**： 字符长度1-64位 

        :param domain_id: The domain_id of this ProcessEventResourceResponseInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ProcessEventResourceResponseInfo.

        项目ID

        :return: The project_id of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ProcessEventResourceResponseInfo.

        项目ID

        :param project_id: The project_id of this ProcessEventResourceResponseInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ProcessEventResourceResponseInfo.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ProcessEventResourceResponseInfo.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ProcessEventResourceResponseInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def region_name(self):
        r"""Gets the region_name of this ProcessEventResourceResponseInfo.

        Region ID

        :return: The region_name of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this ProcessEventResourceResponseInfo.

        Region ID

        :param region_name: The region_name of this ProcessEventResourceResponseInfo.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ProcessEventResourceResponseInfo.

        **参数解释**： VPC ID **取值范围**： 字符长度1-64位 

        :return: The vpc_id of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ProcessEventResourceResponseInfo.

        **参数解释**： VPC ID **取值范围**： 字符长度1-64位 

        :param vpc_id: The vpc_id of this ProcessEventResourceResponseInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def cloud_id(self):
        r"""Gets the cloud_id of this ProcessEventResourceResponseInfo.

        **参数解释**： 云主机ID **取值范围**： 字符长度1-64位 

        :return: The cloud_id of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._cloud_id

    @cloud_id.setter
    def cloud_id(self, cloud_id):
        r"""Sets the cloud_id of this ProcessEventResourceResponseInfo.

        **参数解释**： 云主机ID **取值范围**： 字符长度1-64位 

        :param cloud_id: The cloud_id of this ProcessEventResourceResponseInfo.
        :type cloud_id: str
        """
        self._cloud_id = cloud_id

    @property
    def vm_name(self):
        r"""Gets the vm_name of this ProcessEventResourceResponseInfo.

        **参数解释**： 虚拟机名称 **取值范围**： 字符长度1-64位 

        :return: The vm_name of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._vm_name

    @vm_name.setter
    def vm_name(self, vm_name):
        r"""Sets the vm_name of this ProcessEventResourceResponseInfo.

        **参数解释**： 虚拟机名称 **取值范围**： 字符长度1-64位 

        :param vm_name: The vm_name of this ProcessEventResourceResponseInfo.
        :type vm_name: str
        """
        self._vm_name = vm_name

    @property
    def vm_uuid(self):
        r"""Gets the vm_uuid of this ProcessEventResourceResponseInfo.

        **参数解释**： 虚拟机UUID **取值范围**： 字符长度1-64位 

        :return: The vm_uuid of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._vm_uuid

    @vm_uuid.setter
    def vm_uuid(self, vm_uuid):
        r"""Sets the vm_uuid of this ProcessEventResourceResponseInfo.

        **参数解释**： 虚拟机UUID **取值范围**： 字符长度1-64位 

        :param vm_uuid: The vm_uuid of this ProcessEventResourceResponseInfo.
        :type vm_uuid: str
        """
        self._vm_uuid = vm_uuid

    @property
    def container_id(self):
        r"""Gets the container_id of this ProcessEventResourceResponseInfo.

        **参数解释**: 容器ID **取值范围**: 字符长度1-128位 

        :return: The container_id of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ProcessEventResourceResponseInfo.

        **参数解释**: 容器ID **取值范围**: 字符长度1-128位 

        :param container_id: The container_id of this ProcessEventResourceResponseInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def image_id(self):
        r"""Gets the image_id of this ProcessEventResourceResponseInfo.

        **参数解释**： 镜像ID **取值范围**： 字符长度1-64位 

        :return: The image_id of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ProcessEventResourceResponseInfo.

        **参数解释**： 镜像ID **取值范围**： 字符长度1-64位 

        :param image_id: The image_id of this ProcessEventResourceResponseInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this ProcessEventResourceResponseInfo.

        **参数解释**： 镜像名称，只有容器类型的告警有 **取值范围**： 字符长度1-256位 

        :return: The image_name of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ProcessEventResourceResponseInfo.

        **参数解释**： 镜像名称，只有容器类型的告警有 **取值范围**： 字符长度1-256位 

        :param image_name: The image_name of this ProcessEventResourceResponseInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def host_attr(self):
        r"""Gets the host_attr of this ProcessEventResourceResponseInfo.

        **参数解释**： 主机属性 **取值范围**： 字符长度1-64位 

        :return: The host_attr of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._host_attr

    @host_attr.setter
    def host_attr(self, host_attr):
        r"""Sets the host_attr of this ProcessEventResourceResponseInfo.

        **参数解释**： 主机属性 **取值范围**： 字符长度1-64位 

        :param host_attr: The host_attr of this ProcessEventResourceResponseInfo.
        :type host_attr: str
        """
        self._host_attr = host_attr

    @property
    def service(self):
        r"""Gets the service of this ProcessEventResourceResponseInfo.

        **参数解释**： 业务服务 **取值范围**： 字符长度1-64位 

        :return: The service of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this ProcessEventResourceResponseInfo.

        **参数解释**： 业务服务 **取值范围**： 字符长度1-64位 

        :param service: The service of this ProcessEventResourceResponseInfo.
        :type service: str
        """
        self._service = service

    @property
    def micro_service(self):
        r"""Gets the micro_service of this ProcessEventResourceResponseInfo.

        **参数解释**： 微服务 **取值范围**： 字符长度1-64位 

        :return: The micro_service of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._micro_service

    @micro_service.setter
    def micro_service(self, micro_service):
        r"""Sets the micro_service of this ProcessEventResourceResponseInfo.

        **参数解释**： 微服务 **取值范围**： 字符长度1-64位 

        :param micro_service: The micro_service of this ProcessEventResourceResponseInfo.
        :type micro_service: str
        """
        self._micro_service = micro_service

    @property
    def sys_arch(self):
        r"""Gets the sys_arch of this ProcessEventResourceResponseInfo.

        **参数解释**： 系统CPU架构 **取值范围**： 字符长度1-64位 

        :return: The sys_arch of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._sys_arch

    @sys_arch.setter
    def sys_arch(self, sys_arch):
        r"""Sets the sys_arch of this ProcessEventResourceResponseInfo.

        **参数解释**： 系统CPU架构 **取值范围**： 字符长度1-64位 

        :param sys_arch: The sys_arch of this ProcessEventResourceResponseInfo.
        :type sys_arch: str
        """
        self._sys_arch = sys_arch

    @property
    def os_bit(self):
        r"""Gets the os_bit of this ProcessEventResourceResponseInfo.

        **参数解释**： 操作系统位数 **取值范围**： 字符长度1-64位 

        :return: The os_bit of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        r"""Sets the os_bit of this ProcessEventResourceResponseInfo.

        **参数解释**： 操作系统位数 **取值范围**： 字符长度1-64位 

        :param os_bit: The os_bit of this ProcessEventResourceResponseInfo.
        :type os_bit: str
        """
        self._os_bit = os_bit

    @property
    def os_type(self):
        r"""Gets the os_type of this ProcessEventResourceResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :return: The os_type of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ProcessEventResourceResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :param os_type: The os_type of this ProcessEventResourceResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_name(self):
        r"""Gets the os_name of this ProcessEventResourceResponseInfo.

        操作系统名称

        :return: The os_name of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this ProcessEventResourceResponseInfo.

        操作系统名称

        :param os_name: The os_name of this ProcessEventResourceResponseInfo.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def host_name(self):
        r"""Gets the host_name of this ProcessEventResourceResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ProcessEventResourceResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this ProcessEventResourceResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ProcessEventResourceResponseInfo.

        **参数解释**: 主机IP **取值范围**: 字符长度1-128位 

        :return: The host_ip of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ProcessEventResourceResponseInfo.

        **参数解释**: 主机IP **取值范围**: 字符长度1-128位 

        :param host_ip: The host_ip of this ProcessEventResourceResponseInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ProcessEventResourceResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :return: The public_ip of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ProcessEventResourceResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :param public_ip: The public_ip of this ProcessEventResourceResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def host_id(self):
        r"""Gets the host_id of this ProcessEventResourceResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ProcessEventResourceResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this ProcessEventResourceResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def pod_uid(self):
        r"""Gets the pod_uid of this ProcessEventResourceResponseInfo.

        **参数解释**： pod uid **取值范围**： 字符长度1-64位 

        :return: The pod_uid of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._pod_uid

    @pod_uid.setter
    def pod_uid(self, pod_uid):
        r"""Sets the pod_uid of this ProcessEventResourceResponseInfo.

        **参数解释**： pod uid **取值范围**： 字符长度1-64位 

        :param pod_uid: The pod_uid of this ProcessEventResourceResponseInfo.
        :type pod_uid: str
        """
        self._pod_uid = pod_uid

    @property
    def pod_name(self):
        r"""Gets the pod_name of this ProcessEventResourceResponseInfo.

        **参数解释**： pod name **取值范围**： 字符长度1-64位 

        :return: The pod_name of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this ProcessEventResourceResponseInfo.

        **参数解释**： pod name **取值范围**： 字符长度1-64位 

        :param pod_name: The pod_name of this ProcessEventResourceResponseInfo.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def namespace(self):
        r"""Gets the namespace of this ProcessEventResourceResponseInfo.

        **参数解释**： 名称空间 **取值范围**： 字符长度1-64位 

        :return: The namespace of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ProcessEventResourceResponseInfo.

        **参数解释**： 名称空间 **取值范围**： 字符长度1-64位 

        :param namespace: The namespace of this ProcessEventResourceResponseInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ProcessEventResourceResponseInfo.

        集群ID

        :return: The cluster_id of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ProcessEventResourceResponseInfo.

        集群ID

        :param cluster_id: The cluster_id of this ProcessEventResourceResponseInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ProcessEventResourceResponseInfo.

        集群名称

        :return: The cluster_name of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ProcessEventResourceResponseInfo.

        集群名称

        :param cluster_name: The cluster_name of this ProcessEventResourceResponseInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ProcessEventResourceResponseInfo.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ProcessEventResourceResponseInfo.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this ProcessEventResourceResponseInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def container_status(self):
        r"""Gets the container_status of this ProcessEventResourceResponseInfo.

        容器状态

        :return: The container_status of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._container_status

    @container_status.setter
    def container_status(self, container_status):
        r"""Sets the container_status of this ProcessEventResourceResponseInfo.

        容器状态

        :param container_status: The container_status of this ProcessEventResourceResponseInfo.
        :type container_status: str
        """
        self._container_status = container_status

    @property
    def os_version(self):
        r"""Gets the os_version of this ProcessEventResourceResponseInfo.

        系统版本

        :return: The os_version of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this ProcessEventResourceResponseInfo.

        系统版本

        :param os_version: The os_version of this ProcessEventResourceResponseInfo.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def agent_version(self):
        r"""Gets the agent_version of this ProcessEventResourceResponseInfo.

        agent版本

        :return: The agent_version of this ProcessEventResourceResponseInfo.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this ProcessEventResourceResponseInfo.

        agent版本

        :param agent_version: The agent_version of this ProcessEventResourceResponseInfo.
        :type agent_version: str
        """
        self._agent_version = agent_version

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
        if not isinstance(other, ProcessEventResourceResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
