# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateManualImageScanTaskReqInfoQueryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'local_image_type': 'str',
        'host_id': 'str',
        'host_name': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'cluster_id': 'str',
        'container_id': 'str',
        'container_name': 'str',
        'pod_id': 'str',
        'pod_name': 'str',
        'app_name': 'str',
        'has_vul': 'bool',
        'namespace': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'image_type': 'str',
        'scan_status': 'str',
        'image_size': 'int',
        'start_latest_update_time': 'int',
        'end_latest_update_time': 'int',
        'start_latest_scan_time': 'int',
        'end_latest_scan_time': 'int'
    }

    attribute_map = {
        'local_image_type': 'local_image_type',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'cluster_id': 'cluster_id',
        'container_id': 'container_id',
        'container_name': 'container_name',
        'pod_id': 'pod_id',
        'pod_name': 'pod_name',
        'app_name': 'app_name',
        'has_vul': 'has_vul',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'image_type': 'image_type',
        'scan_status': 'scan_status',
        'image_size': 'image_size',
        'start_latest_update_time': 'start_latest_update_time',
        'end_latest_update_time': 'end_latest_update_time',
        'start_latest_scan_time': 'start_latest_scan_time',
        'end_latest_scan_time': 'end_latest_scan_time'
    }

    def __init__(self, local_image_type=None, host_id=None, host_name=None, public_ip=None, private_ip=None, cluster_id=None, container_id=None, container_name=None, pod_id=None, pod_name=None, app_name=None, has_vul=None, namespace=None, image_name=None, image_version=None, image_type=None, scan_status=None, image_size=None, start_latest_update_time=None, end_latest_update_time=None, start_latest_scan_time=None, end_latest_scan_time=None):
        r"""CreateManualImageScanTaskReqInfoQueryInfo

        The model defined in huaweicloud sdk

        :param local_image_type: **参数解释**: 本地镜像类型 **约束限制**: 不涉及 **取值范围**: - swr_image：swr镜像。 - other_image：其他镜像。  **默认取值**: 不涉及 
        :type local_image_type: str
        :param host_id: **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 
        :type host_name: str
        :param public_ip: **参数解释**: 服务器公网IP **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 
        :type public_ip: str
        :param private_ip: **参数解释**: 私有IP地址 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 
        :type private_ip: str
        :param cluster_id: **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 
        :type cluster_id: str
        :param container_id: **参数解释**: 容器id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 
        :type container_id: str
        :param container_name: **参数解释**: 容器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 
        :type container_name: str
        :param pod_id: **参数解释**: pod id **约束限制**: 不涉及 **取值范围**: 字符长度0-64位。  **默认取值**: 不涉及 
        :type pod_id: str
        :param pod_name: **参数解释**: pod 名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位。  **默认取值**: 不涉及 
        :type pod_name: str
        :param app_name: **参数解释**: 软件名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位。  **默认取值**: 不涉及 
        :type app_name: str
        :param has_vul: **参数解释**: 是否存在软件漏洞 **约束限制**: 不涉及 **取值范围**: - true：存在软件漏洞。 - false：不存在软件漏洞。  **默认取值**: 不涉及 
        :type has_vul: bool
        :param namespace: **参数解释**: 组织名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位。  **默认取值**: 不涉及 
        :type namespace: str
        :param image_name: **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位。  **默认取值**: 不涉及 
        :type image_name: str
        :param image_version: **参数解释**: 镜像版本 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位。  **默认取值**: 不涉及 
        :type image_version: str
        :param image_type: **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - private_image：SWR私有镜像仓库。 - shared_image：SWR共享镜像仓库。 - instance_image：SWR企业仓库。 - harbor：harbor仓库。 - jfrog：jfrog仓库。  **默认取值**: 不涉及 
        :type image_type: str
        :param scan_status: **参数解释**: 扫描状态 **约束限制**: 不涉及 **取值范围**: - unscan：未扫描 - success：扫描完成 - scanning：扫描中 - failed：扫描失败 - download_failed：下载失败 - image_oversized：镜像超大  **默认取值**: 不涉及 
        :type scan_status: str
        :param image_size: **参数解释**: 镜像大小 **约束限制**: 不涉及 **取值范围**: 0-9223372036854775807。  **默认取值**: 不涉及 
        :type image_size: int
        :param start_latest_update_time: **参数解释**: 创建时间开始日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 0-9223372036854775807。  **默认取值**: 不涉及 
        :type start_latest_update_time: int
        :param end_latest_update_time: **参数解释**: 创建时间结束日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 0-9223372036854775807。  **默认取值**: 不涉及 
        :type end_latest_update_time: int
        :param start_latest_scan_time: **参数解释**: 最近一次扫描完成时间开始日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 0-9223372036854775807。  **默认取值**: 不涉及 
        :type start_latest_scan_time: int
        :param end_latest_scan_time: **参数解释**: 最近一次扫描完成时间结束日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 0-9223372036854775807。  **默认取值**: 不涉及 
        :type end_latest_scan_time: int
        """
        
        

        self._local_image_type = None
        self._host_id = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._cluster_id = None
        self._container_id = None
        self._container_name = None
        self._pod_id = None
        self._pod_name = None
        self._app_name = None
        self._has_vul = None
        self._namespace = None
        self._image_name = None
        self._image_version = None
        self._image_type = None
        self._scan_status = None
        self._image_size = None
        self._start_latest_update_time = None
        self._end_latest_update_time = None
        self._start_latest_scan_time = None
        self._end_latest_scan_time = None
        self.discriminator = None

        if local_image_type is not None:
            self.local_image_type = local_image_type
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name
        if pod_id is not None:
            self.pod_id = pod_id
        if pod_name is not None:
            self.pod_name = pod_name
        if app_name is not None:
            self.app_name = app_name
        if has_vul is not None:
            self.has_vul = has_vul
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if image_type is not None:
            self.image_type = image_type
        if scan_status is not None:
            self.scan_status = scan_status
        if image_size is not None:
            self.image_size = image_size
        if start_latest_update_time is not None:
            self.start_latest_update_time = start_latest_update_time
        if end_latest_update_time is not None:
            self.end_latest_update_time = end_latest_update_time
        if start_latest_scan_time is not None:
            self.start_latest_scan_time = start_latest_scan_time
        if end_latest_scan_time is not None:
            self.end_latest_scan_time = end_latest_scan_time

    @property
    def local_image_type(self):
        r"""Gets the local_image_type of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 本地镜像类型 **约束限制**: 不涉及 **取值范围**: - swr_image：swr镜像。 - other_image：其他镜像。  **默认取值**: 不涉及 

        :return: The local_image_type of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: str
        """
        return self._local_image_type

    @local_image_type.setter
    def local_image_type(self, local_image_type):
        r"""Sets the local_image_type of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 本地镜像类型 **约束限制**: 不涉及 **取值范围**: - swr_image：swr镜像。 - other_image：其他镜像。  **默认取值**: 不涉及 

        :param local_image_type: The local_image_type of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type local_image_type: str
        """
        self._local_image_type = local_image_type

    @property
    def host_id(self):
        r"""Gets the host_id of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 

        :return: The host_id of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 

        :param host_id: The host_id of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 

        :return: The host_name of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 

        :param host_name: The host_name of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 服务器公网IP **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 

        :return: The public_ip of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 服务器公网IP **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 

        :param public_ip: The public_ip of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 私有IP地址 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 

        :return: The private_ip of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 私有IP地址 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 

        :param private_ip: The private_ip of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 

        :return: The cluster_id of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 

        :param cluster_id: The cluster_id of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def container_id(self):
        r"""Gets the container_id of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 容器id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 

        :return: The container_id of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 容器id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 

        :param container_id: The container_id of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 容器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 

        :return: The container_name of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 容器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位。  **默认取值**: 不涉及 

        :param container_name: The container_name of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def pod_id(self):
        r"""Gets the pod_id of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: pod id **约束限制**: 不涉及 **取值范围**: 字符长度0-64位。  **默认取值**: 不涉及 

        :return: The pod_id of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: str
        """
        return self._pod_id

    @pod_id.setter
    def pod_id(self, pod_id):
        r"""Sets the pod_id of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: pod id **约束限制**: 不涉及 **取值范围**: 字符长度0-64位。  **默认取值**: 不涉及 

        :param pod_id: The pod_id of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type pod_id: str
        """
        self._pod_id = pod_id

    @property
    def pod_name(self):
        r"""Gets the pod_name of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: pod 名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位。  **默认取值**: 不涉及 

        :return: The pod_name of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: pod 名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位。  **默认取值**: 不涉及 

        :param pod_name: The pod_name of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def app_name(self):
        r"""Gets the app_name of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 软件名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位。  **默认取值**: 不涉及 

        :return: The app_name of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 软件名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位。  **默认取值**: 不涉及 

        :param app_name: The app_name of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def has_vul(self):
        r"""Gets the has_vul of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 是否存在软件漏洞 **约束限制**: 不涉及 **取值范围**: - true：存在软件漏洞。 - false：不存在软件漏洞。  **默认取值**: 不涉及 

        :return: The has_vul of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: bool
        """
        return self._has_vul

    @has_vul.setter
    def has_vul(self, has_vul):
        r"""Sets the has_vul of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 是否存在软件漏洞 **约束限制**: 不涉及 **取值范围**: - true：存在软件漏洞。 - false：不存在软件漏洞。  **默认取值**: 不涉及 

        :param has_vul: The has_vul of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type has_vul: bool
        """
        self._has_vul = has_vul

    @property
    def namespace(self):
        r"""Gets the namespace of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 组织名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位。  **默认取值**: 不涉及 

        :return: The namespace of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 组织名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位。  **默认取值**: 不涉及 

        :param namespace: The namespace of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        r"""Gets the image_name of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位。  **默认取值**: 不涉及 

        :return: The image_name of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位。  **默认取值**: 不涉及 

        :param image_name: The image_name of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 镜像版本 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位。  **默认取值**: 不涉及 

        :return: The image_version of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 镜像版本 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位。  **默认取值**: 不涉及 

        :param image_version: The image_version of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_type(self):
        r"""Gets the image_type of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - private_image：SWR私有镜像仓库。 - shared_image：SWR共享镜像仓库。 - instance_image：SWR企业仓库。 - harbor：harbor仓库。 - jfrog：jfrog仓库。  **默认取值**: 不涉及 

        :return: The image_type of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - private_image：SWR私有镜像仓库。 - shared_image：SWR共享镜像仓库。 - instance_image：SWR企业仓库。 - harbor：harbor仓库。 - jfrog：jfrog仓库。  **默认取值**: 不涉及 

        :param image_type: The image_type of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def scan_status(self):
        r"""Gets the scan_status of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 扫描状态 **约束限制**: 不涉及 **取值范围**: - unscan：未扫描 - success：扫描完成 - scanning：扫描中 - failed：扫描失败 - download_failed：下载失败 - image_oversized：镜像超大  **默认取值**: 不涉及 

        :return: The scan_status of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 扫描状态 **约束限制**: 不涉及 **取值范围**: - unscan：未扫描 - success：扫描完成 - scanning：扫描中 - failed：扫描失败 - download_failed：下载失败 - image_oversized：镜像超大  **默认取值**: 不涉及 

        :param scan_status: The scan_status of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def image_size(self):
        r"""Gets the image_size of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 镜像大小 **约束限制**: 不涉及 **取值范围**: 0-9223372036854775807。  **默认取值**: 不涉及 

        :return: The image_size of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 镜像大小 **约束限制**: 不涉及 **取值范围**: 0-9223372036854775807。  **默认取值**: 不涉及 

        :param image_size: The image_size of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type image_size: int
        """
        self._image_size = image_size

    @property
    def start_latest_update_time(self):
        r"""Gets the start_latest_update_time of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 创建时间开始日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 0-9223372036854775807。  **默认取值**: 不涉及 

        :return: The start_latest_update_time of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: int
        """
        return self._start_latest_update_time

    @start_latest_update_time.setter
    def start_latest_update_time(self, start_latest_update_time):
        r"""Sets the start_latest_update_time of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 创建时间开始日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 0-9223372036854775807。  **默认取值**: 不涉及 

        :param start_latest_update_time: The start_latest_update_time of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type start_latest_update_time: int
        """
        self._start_latest_update_time = start_latest_update_time

    @property
    def end_latest_update_time(self):
        r"""Gets the end_latest_update_time of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 创建时间结束日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 0-9223372036854775807。  **默认取值**: 不涉及 

        :return: The end_latest_update_time of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: int
        """
        return self._end_latest_update_time

    @end_latest_update_time.setter
    def end_latest_update_time(self, end_latest_update_time):
        r"""Sets the end_latest_update_time of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 创建时间结束日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 0-9223372036854775807。  **默认取值**: 不涉及 

        :param end_latest_update_time: The end_latest_update_time of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type end_latest_update_time: int
        """
        self._end_latest_update_time = end_latest_update_time

    @property
    def start_latest_scan_time(self):
        r"""Gets the start_latest_scan_time of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 最近一次扫描完成时间开始日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 0-9223372036854775807。  **默认取值**: 不涉及 

        :return: The start_latest_scan_time of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: int
        """
        return self._start_latest_scan_time

    @start_latest_scan_time.setter
    def start_latest_scan_time(self, start_latest_scan_time):
        r"""Sets the start_latest_scan_time of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 最近一次扫描完成时间开始日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 0-9223372036854775807。  **默认取值**: 不涉及 

        :param start_latest_scan_time: The start_latest_scan_time of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type start_latest_scan_time: int
        """
        self._start_latest_scan_time = start_latest_scan_time

    @property
    def end_latest_scan_time(self):
        r"""Gets the end_latest_scan_time of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 最近一次扫描完成时间结束日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 0-9223372036854775807。  **默认取值**: 不涉及 

        :return: The end_latest_scan_time of this CreateManualImageScanTaskReqInfoQueryInfo.
        :rtype: int
        """
        return self._end_latest_scan_time

    @end_latest_scan_time.setter
    def end_latest_scan_time(self, end_latest_scan_time):
        r"""Sets the end_latest_scan_time of this CreateManualImageScanTaskReqInfoQueryInfo.

        **参数解释**: 最近一次扫描完成时间结束日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 0-9223372036854775807。  **默认取值**: 不涉及 

        :param end_latest_scan_time: The end_latest_scan_time of this CreateManualImageScanTaskReqInfoQueryInfo.
        :type end_latest_scan_time: int
        """
        self._end_latest_scan_time = end_latest_scan_time

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
        if not isinstance(other, CreateManualImageScanTaskReqInfoQueryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
