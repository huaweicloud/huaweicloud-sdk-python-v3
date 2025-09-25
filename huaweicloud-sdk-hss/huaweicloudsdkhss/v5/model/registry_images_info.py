# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegistryImagesInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'namespace': 'str',
        'image_name': 'str',
        'image_id': 'str',
        'image_digest': 'str',
        'image_version': 'str',
        'image_type': 'str',
        'registry_id': 'str',
        'registry_name': 'str',
        'registry_type': 'str',
        'latest_version': 'bool',
        'scan_status': 'str',
        'scan_failed_desc': 'str',
        'scan_failed_code': 'str',
        'image_size': 'int',
        'latest_update_time': 'int',
        'latest_scan_time': 'int',
        'latest_sync_time': 'int',
        'vul_num': 'int',
        'unsafe_setting_num': 'int',
        'malicious_file_num': 'int',
        'domain_name': 'str',
        'shared_status': 'str',
        'scannable': 'bool',
        'is_multiple_arch': 'bool',
        'instance_name': 'str',
        'instance_id': 'str',
        'instance_url': 'str',
        'severity_level': 'str',
        'association_images': 'list[AssociateImagesInfo]'
    }

    attribute_map = {
        'id': 'id',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_id': 'image_id',
        'image_digest': 'image_digest',
        'image_version': 'image_version',
        'image_type': 'image_type',
        'registry_id': 'registry_id',
        'registry_name': 'registry_name',
        'registry_type': 'registry_type',
        'latest_version': 'latest_version',
        'scan_status': 'scan_status',
        'scan_failed_desc': 'scan_failed_desc',
        'scan_failed_code': 'scan_failed_code',
        'image_size': 'image_size',
        'latest_update_time': 'latest_update_time',
        'latest_scan_time': 'latest_scan_time',
        'latest_sync_time': 'latest_sync_time',
        'vul_num': 'vul_num',
        'unsafe_setting_num': 'unsafe_setting_num',
        'malicious_file_num': 'malicious_file_num',
        'domain_name': 'domain_name',
        'shared_status': 'shared_status',
        'scannable': 'scannable',
        'is_multiple_arch': 'is_multiple_arch',
        'instance_name': 'instance_name',
        'instance_id': 'instance_id',
        'instance_url': 'instance_url',
        'severity_level': 'severity_level',
        'association_images': 'association_images'
    }

    def __init__(self, id=None, namespace=None, image_name=None, image_id=None, image_digest=None, image_version=None, image_type=None, registry_id=None, registry_name=None, registry_type=None, latest_version=None, scan_status=None, scan_failed_desc=None, scan_failed_code=None, image_size=None, latest_update_time=None, latest_scan_time=None, latest_sync_time=None, vul_num=None, unsafe_setting_num=None, malicious_file_num=None, domain_name=None, shared_status=None, scannable=None, is_multiple_arch=None, instance_name=None, instance_id=None, instance_url=None, severity_level=None, association_images=None):
        r"""RegistryImagesInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**: id **取值范围**: 最小值0，最大值9223372036854775807 
        :type id: int
        :param namespace: **参数解释**: 组织名称 **取值范围**: 字符长度0-64位 
        :type namespace: str
        :param image_name: **参数解释**: 镜像名称 **取值范围**: 字符长度0-128位 
        :type image_name: str
        :param image_id: **参数解释**: 镜像id **取值范围**: 字符长度0-64位 
        :type image_id: str
        :param image_digest: **参数解释**: 镜像digest **取值范围**: 字符长度0-128位 
        :type image_digest: str
        :param image_version: **参数解释**: 镜像版本 **取值范围**: 字符长度0-64位 
        :type image_version: str
        :param image_type: **参数解释**: 镜像类型 **取值范围**: - private_image：SWR私有镜像。 - shared_image：SWR共享镜像。 - instance_image：SWR企业版镜像。 - harbor：Harbor仓库镜像。 - jfrog：Jfrog镜像。 
        :type image_type: str
        :param registry_id: **参数解释**: 镜像仓id **取值范围**: 字符长度1-64位 
        :type registry_id: str
        :param registry_name: **参数解释**: 镜像仓库名称 **取值范围**: 字符长度1-128位 
        :type registry_name: str
        :param registry_type: **参数解释**： 镜像仓库类型 **取值范围**： - SwrPrivate：swr私有。 - SwrShared：swr共享。 - SwrEnterprise：swr企业。 - Harbor：harbor仓库。 - Jfrog：jfrog仓库。 - Other：其他仓库。 
        :type registry_type: str
        :param latest_version: 是否是最新版本
        :type latest_version: bool
        :param scan_status: **参数解释**： 扫描状态 **取值范围**： - unscan：未扫描。 - success：扫描完成。 - scanning：正在扫描。 - failed：扫描失败。 - download_failed：下载失败。 - image_oversized：镜像超大。 - waiting_for_scan：等待扫描。 
        :type scan_status: str
        :param scan_failed_desc: **参数解释**： 扫描失败原因描述 **取值范围**： 扫描失败原因code和描述对应关系如下 - unknown_error：未知错误。 - authentication_failed：认证失败。 - download_failed：镜像下载失败。请向技术人员寻求帮助。 - image_over_sized：镜像大小超限，不支持扫描。建议精简镜像。 - get_detail_info_not_found：获取镜像详细信息失败，镜像仓中可能已经不存在此镜像。请重新同步最新镜像。 - image_layer_over_sized：镜像层数超限，不支持扫描。建议精简镜像。 - schema_v1_not_support：Schema V1镜像不支持扫描。建议升级到V2版本。 - access_swr_failed：访问SWR服务出错。请向技术人员寻求帮助。 - swr_authentication_error：缺少SWR授权。请参考镜像授权指导设置权限。 - failed_to_scan_vulnerability：漏洞扫描失败。 - failed_to_scan_file：文件扫描失败。 - failed_to_scan_software：软件扫描失败。 - failed_to_check_sensitive_information：敏感信息核查失败。 - failed_to_check_baseline：基线检查失败。 - failed_to_check_software_compliance：软件合规检查失败。 - failed_to_query_basic_image_information：基础镜像信息查询失败。 - failed_to_check_build_cmd：镜像构建指令扫描失败。 - response_timed_out：响应超时。 - database_error：数据库错误。 - failed_to_send_the_scan_request：发送扫描请求失败。 
        :type scan_failed_desc: str
        :param scan_failed_code: **参数解释**： 扫描失败原因code **取值范围**： 扫描失败原因code和描述对应关系如下 - unknown_error：未知错误。 - authentication_failed：认证失败。 - download_failed：镜像下载失败。请向技术人员寻求帮助。 - image_over_sized：镜像大小超限，不支持扫描。建议精简镜像。 - get_detail_info_not_found：获取镜像详细信息失败，镜像仓中可能已经不存在此镜像。请重新同步最新镜像。 - image_layer_over_sized：镜像层数超限，不支持扫描。建议精简镜像。 - schema_v1_not_support：Schema V1镜像不支持扫描。建议升级到V2版本。 - access_swr_failed：访问SWR服务出错。请向技术人员寻求帮助。 - swr_authentication_error：缺少SWR授权。请参考镜像授权指导设置权限。 - failed_to_scan_vulnerability：漏洞扫描失败。 - failed_to_scan_file：文件扫描失败。 - failed_to_scan_software：软件扫描失败。 - failed_to_check_sensitive_information：敏感信息核查失败。 - failed_to_check_baseline：基线检查失败。 - failed_to_check_software_compliance：软件合规检查失败。 - failed_to_query_basic_image_information：基础镜像信息查询失败。 - failed_to_check_build_cmd：镜像构建指令扫描失败。 - response_timed_out：响应超时。 - database_error：数据库错误。 - failed_to_send_the_scan_request：发送扫描请求失败。 
        :type scan_failed_code: str
        :param image_size: **参数解释**: 镜像大小 **取值范围**: 取值0-2147483547 
        :type image_size: int
        :param latest_update_time: **参数解释**: 镜像版本最后更新时间，时间单位 毫秒（ms） **取值范围**: 取值0-9223372036854775807 
        :type latest_update_time: int
        :param latest_scan_time: **参数解释**: 最近扫描时间，时间单位 毫秒（ms） **取值范围**: 取值0-9223372036854775807 
        :type latest_scan_time: int
        :param latest_sync_time: **参数解释**: 最近同步时间，时间单位 毫秒（ms） **取值范围**: 取值0-9223372036854775807 
        :type latest_sync_time: int
        :param vul_num: **参数解释**: 漏洞个数 **取值范围**: 取值0-2147483647 
        :type vul_num: int
        :param unsafe_setting_num: **参数解释**: 基线扫描未通过数 **取值范围**: 取值0-2147483647 
        :type unsafe_setting_num: int
        :param malicious_file_num: **参数解释**: 恶意文件数 **取值范围**: 取值0-2147483647 
        :type malicious_file_num: int
        :param domain_name: **参数解释**: 拥有者（共享镜像参数） **取值范围**: 字符长度0-128 
        :type domain_name: str
        :param shared_status: **参数解释**： 共享镜像状态 **取值范围**： - expired：已过期。 - effective：有效。 
        :type shared_status: str
        :param scannable: 是否可扫描
        :type scannable: bool
        :param is_multiple_arch: 是否是多架构镜像
        :type is_multiple_arch: bool
        :param instance_name: **参数解释**: 企业版镜像实例名称 **取值范围**: 字符长度0-128 
        :type instance_name: str
        :param instance_id: **参数解释**: 企业版镜像实例ID **取值范围**: 字符长度0-64 
        :type instance_id: str
        :param instance_url: **参数解释**: 企业版镜像实例URL **取值范围**: 字符长度0-256 
        :type instance_url: str
        :param severity_level: **参数解释**: 镜像风险程度，在镜像扫描完成后展示 **取值范围**: - Security：安全。 - Low：低危。 - Medium：中危。 - High：高危。 
        :type severity_level: str
        :param association_images: 多架构关联镜像信息
        :type association_images: list[:class:`huaweicloudsdkhss.v5.AssociateImagesInfo`]
        """
        
        

        self._id = None
        self._namespace = None
        self._image_name = None
        self._image_id = None
        self._image_digest = None
        self._image_version = None
        self._image_type = None
        self._registry_id = None
        self._registry_name = None
        self._registry_type = None
        self._latest_version = None
        self._scan_status = None
        self._scan_failed_desc = None
        self._scan_failed_code = None
        self._image_size = None
        self._latest_update_time = None
        self._latest_scan_time = None
        self._latest_sync_time = None
        self._vul_num = None
        self._unsafe_setting_num = None
        self._malicious_file_num = None
        self._domain_name = None
        self._shared_status = None
        self._scannable = None
        self._is_multiple_arch = None
        self._instance_name = None
        self._instance_id = None
        self._instance_url = None
        self._severity_level = None
        self._association_images = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_id is not None:
            self.image_id = image_id
        if image_digest is not None:
            self.image_digest = image_digest
        if image_version is not None:
            self.image_version = image_version
        if image_type is not None:
            self.image_type = image_type
        if registry_id is not None:
            self.registry_id = registry_id
        if registry_name is not None:
            self.registry_name = registry_name
        if registry_type is not None:
            self.registry_type = registry_type
        if latest_version is not None:
            self.latest_version = latest_version
        if scan_status is not None:
            self.scan_status = scan_status
        if scan_failed_desc is not None:
            self.scan_failed_desc = scan_failed_desc
        if scan_failed_code is not None:
            self.scan_failed_code = scan_failed_code
        if image_size is not None:
            self.image_size = image_size
        if latest_update_time is not None:
            self.latest_update_time = latest_update_time
        if latest_scan_time is not None:
            self.latest_scan_time = latest_scan_time
        if latest_sync_time is not None:
            self.latest_sync_time = latest_sync_time
        if vul_num is not None:
            self.vul_num = vul_num
        if unsafe_setting_num is not None:
            self.unsafe_setting_num = unsafe_setting_num
        if malicious_file_num is not None:
            self.malicious_file_num = malicious_file_num
        if domain_name is not None:
            self.domain_name = domain_name
        if shared_status is not None:
            self.shared_status = shared_status
        if scannable is not None:
            self.scannable = scannable
        if is_multiple_arch is not None:
            self.is_multiple_arch = is_multiple_arch
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_url is not None:
            self.instance_url = instance_url
        if severity_level is not None:
            self.severity_level = severity_level
        if association_images is not None:
            self.association_images = association_images

    @property
    def id(self):
        r"""Gets the id of this RegistryImagesInfo.

        **参数解释**: id **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The id of this RegistryImagesInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RegistryImagesInfo.

        **参数解释**: id **取值范围**: 最小值0，最大值9223372036854775807 

        :param id: The id of this RegistryImagesInfo.
        :type id: int
        """
        self._id = id

    @property
    def namespace(self):
        r"""Gets the namespace of this RegistryImagesInfo.

        **参数解释**: 组织名称 **取值范围**: 字符长度0-64位 

        :return: The namespace of this RegistryImagesInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this RegistryImagesInfo.

        **参数解释**: 组织名称 **取值范围**: 字符长度0-64位 

        :param namespace: The namespace of this RegistryImagesInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        r"""Gets the image_name of this RegistryImagesInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-128位 

        :return: The image_name of this RegistryImagesInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this RegistryImagesInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-128位 

        :param image_name: The image_name of this RegistryImagesInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_id(self):
        r"""Gets the image_id of this RegistryImagesInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-64位 

        :return: The image_id of this RegistryImagesInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this RegistryImagesInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-64位 

        :param image_id: The image_id of this RegistryImagesInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_digest(self):
        r"""Gets the image_digest of this RegistryImagesInfo.

        **参数解释**: 镜像digest **取值范围**: 字符长度0-128位 

        :return: The image_digest of this RegistryImagesInfo.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        r"""Sets the image_digest of this RegistryImagesInfo.

        **参数解释**: 镜像digest **取值范围**: 字符长度0-128位 

        :param image_digest: The image_digest of this RegistryImagesInfo.
        :type image_digest: str
        """
        self._image_digest = image_digest

    @property
    def image_version(self):
        r"""Gets the image_version of this RegistryImagesInfo.

        **参数解释**: 镜像版本 **取值范围**: 字符长度0-64位 

        :return: The image_version of this RegistryImagesInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this RegistryImagesInfo.

        **参数解释**: 镜像版本 **取值范围**: 字符长度0-64位 

        :param image_version: The image_version of this RegistryImagesInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_type(self):
        r"""Gets the image_type of this RegistryImagesInfo.

        **参数解释**: 镜像类型 **取值范围**: - private_image：SWR私有镜像。 - shared_image：SWR共享镜像。 - instance_image：SWR企业版镜像。 - harbor：Harbor仓库镜像。 - jfrog：Jfrog镜像。 

        :return: The image_type of this RegistryImagesInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this RegistryImagesInfo.

        **参数解释**: 镜像类型 **取值范围**: - private_image：SWR私有镜像。 - shared_image：SWR共享镜像。 - instance_image：SWR企业版镜像。 - harbor：Harbor仓库镜像。 - jfrog：Jfrog镜像。 

        :param image_type: The image_type of this RegistryImagesInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def registry_id(self):
        r"""Gets the registry_id of this RegistryImagesInfo.

        **参数解释**: 镜像仓id **取值范围**: 字符长度1-64位 

        :return: The registry_id of this RegistryImagesInfo.
        :rtype: str
        """
        return self._registry_id

    @registry_id.setter
    def registry_id(self, registry_id):
        r"""Sets the registry_id of this RegistryImagesInfo.

        **参数解释**: 镜像仓id **取值范围**: 字符长度1-64位 

        :param registry_id: The registry_id of this RegistryImagesInfo.
        :type registry_id: str
        """
        self._registry_id = registry_id

    @property
    def registry_name(self):
        r"""Gets the registry_name of this RegistryImagesInfo.

        **参数解释**: 镜像仓库名称 **取值范围**: 字符长度1-128位 

        :return: The registry_name of this RegistryImagesInfo.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        r"""Sets the registry_name of this RegistryImagesInfo.

        **参数解释**: 镜像仓库名称 **取值范围**: 字符长度1-128位 

        :param registry_name: The registry_name of this RegistryImagesInfo.
        :type registry_name: str
        """
        self._registry_name = registry_name

    @property
    def registry_type(self):
        r"""Gets the registry_type of this RegistryImagesInfo.

        **参数解释**： 镜像仓库类型 **取值范围**： - SwrPrivate：swr私有。 - SwrShared：swr共享。 - SwrEnterprise：swr企业。 - Harbor：harbor仓库。 - Jfrog：jfrog仓库。 - Other：其他仓库。 

        :return: The registry_type of this RegistryImagesInfo.
        :rtype: str
        """
        return self._registry_type

    @registry_type.setter
    def registry_type(self, registry_type):
        r"""Sets the registry_type of this RegistryImagesInfo.

        **参数解释**： 镜像仓库类型 **取值范围**： - SwrPrivate：swr私有。 - SwrShared：swr共享。 - SwrEnterprise：swr企业。 - Harbor：harbor仓库。 - Jfrog：jfrog仓库。 - Other：其他仓库。 

        :param registry_type: The registry_type of this RegistryImagesInfo.
        :type registry_type: str
        """
        self._registry_type = registry_type

    @property
    def latest_version(self):
        r"""Gets the latest_version of this RegistryImagesInfo.

        是否是最新版本

        :return: The latest_version of this RegistryImagesInfo.
        :rtype: bool
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this RegistryImagesInfo.

        是否是最新版本

        :param latest_version: The latest_version of this RegistryImagesInfo.
        :type latest_version: bool
        """
        self._latest_version = latest_version

    @property
    def scan_status(self):
        r"""Gets the scan_status of this RegistryImagesInfo.

        **参数解释**： 扫描状态 **取值范围**： - unscan：未扫描。 - success：扫描完成。 - scanning：正在扫描。 - failed：扫描失败。 - download_failed：下载失败。 - image_oversized：镜像超大。 - waiting_for_scan：等待扫描。 

        :return: The scan_status of this RegistryImagesInfo.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this RegistryImagesInfo.

        **参数解释**： 扫描状态 **取值范围**： - unscan：未扫描。 - success：扫描完成。 - scanning：正在扫描。 - failed：扫描失败。 - download_failed：下载失败。 - image_oversized：镜像超大。 - waiting_for_scan：等待扫描。 

        :param scan_status: The scan_status of this RegistryImagesInfo.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def scan_failed_desc(self):
        r"""Gets the scan_failed_desc of this RegistryImagesInfo.

        **参数解释**： 扫描失败原因描述 **取值范围**： 扫描失败原因code和描述对应关系如下 - unknown_error：未知错误。 - authentication_failed：认证失败。 - download_failed：镜像下载失败。请向技术人员寻求帮助。 - image_over_sized：镜像大小超限，不支持扫描。建议精简镜像。 - get_detail_info_not_found：获取镜像详细信息失败，镜像仓中可能已经不存在此镜像。请重新同步最新镜像。 - image_layer_over_sized：镜像层数超限，不支持扫描。建议精简镜像。 - schema_v1_not_support：Schema V1镜像不支持扫描。建议升级到V2版本。 - access_swr_failed：访问SWR服务出错。请向技术人员寻求帮助。 - swr_authentication_error：缺少SWR授权。请参考镜像授权指导设置权限。 - failed_to_scan_vulnerability：漏洞扫描失败。 - failed_to_scan_file：文件扫描失败。 - failed_to_scan_software：软件扫描失败。 - failed_to_check_sensitive_information：敏感信息核查失败。 - failed_to_check_baseline：基线检查失败。 - failed_to_check_software_compliance：软件合规检查失败。 - failed_to_query_basic_image_information：基础镜像信息查询失败。 - failed_to_check_build_cmd：镜像构建指令扫描失败。 - response_timed_out：响应超时。 - database_error：数据库错误。 - failed_to_send_the_scan_request：发送扫描请求失败。 

        :return: The scan_failed_desc of this RegistryImagesInfo.
        :rtype: str
        """
        return self._scan_failed_desc

    @scan_failed_desc.setter
    def scan_failed_desc(self, scan_failed_desc):
        r"""Sets the scan_failed_desc of this RegistryImagesInfo.

        **参数解释**： 扫描失败原因描述 **取值范围**： 扫描失败原因code和描述对应关系如下 - unknown_error：未知错误。 - authentication_failed：认证失败。 - download_failed：镜像下载失败。请向技术人员寻求帮助。 - image_over_sized：镜像大小超限，不支持扫描。建议精简镜像。 - get_detail_info_not_found：获取镜像详细信息失败，镜像仓中可能已经不存在此镜像。请重新同步最新镜像。 - image_layer_over_sized：镜像层数超限，不支持扫描。建议精简镜像。 - schema_v1_not_support：Schema V1镜像不支持扫描。建议升级到V2版本。 - access_swr_failed：访问SWR服务出错。请向技术人员寻求帮助。 - swr_authentication_error：缺少SWR授权。请参考镜像授权指导设置权限。 - failed_to_scan_vulnerability：漏洞扫描失败。 - failed_to_scan_file：文件扫描失败。 - failed_to_scan_software：软件扫描失败。 - failed_to_check_sensitive_information：敏感信息核查失败。 - failed_to_check_baseline：基线检查失败。 - failed_to_check_software_compliance：软件合规检查失败。 - failed_to_query_basic_image_information：基础镜像信息查询失败。 - failed_to_check_build_cmd：镜像构建指令扫描失败。 - response_timed_out：响应超时。 - database_error：数据库错误。 - failed_to_send_the_scan_request：发送扫描请求失败。 

        :param scan_failed_desc: The scan_failed_desc of this RegistryImagesInfo.
        :type scan_failed_desc: str
        """
        self._scan_failed_desc = scan_failed_desc

    @property
    def scan_failed_code(self):
        r"""Gets the scan_failed_code of this RegistryImagesInfo.

        **参数解释**： 扫描失败原因code **取值范围**： 扫描失败原因code和描述对应关系如下 - unknown_error：未知错误。 - authentication_failed：认证失败。 - download_failed：镜像下载失败。请向技术人员寻求帮助。 - image_over_sized：镜像大小超限，不支持扫描。建议精简镜像。 - get_detail_info_not_found：获取镜像详细信息失败，镜像仓中可能已经不存在此镜像。请重新同步最新镜像。 - image_layer_over_sized：镜像层数超限，不支持扫描。建议精简镜像。 - schema_v1_not_support：Schema V1镜像不支持扫描。建议升级到V2版本。 - access_swr_failed：访问SWR服务出错。请向技术人员寻求帮助。 - swr_authentication_error：缺少SWR授权。请参考镜像授权指导设置权限。 - failed_to_scan_vulnerability：漏洞扫描失败。 - failed_to_scan_file：文件扫描失败。 - failed_to_scan_software：软件扫描失败。 - failed_to_check_sensitive_information：敏感信息核查失败。 - failed_to_check_baseline：基线检查失败。 - failed_to_check_software_compliance：软件合规检查失败。 - failed_to_query_basic_image_information：基础镜像信息查询失败。 - failed_to_check_build_cmd：镜像构建指令扫描失败。 - response_timed_out：响应超时。 - database_error：数据库错误。 - failed_to_send_the_scan_request：发送扫描请求失败。 

        :return: The scan_failed_code of this RegistryImagesInfo.
        :rtype: str
        """
        return self._scan_failed_code

    @scan_failed_code.setter
    def scan_failed_code(self, scan_failed_code):
        r"""Sets the scan_failed_code of this RegistryImagesInfo.

        **参数解释**： 扫描失败原因code **取值范围**： 扫描失败原因code和描述对应关系如下 - unknown_error：未知错误。 - authentication_failed：认证失败。 - download_failed：镜像下载失败。请向技术人员寻求帮助。 - image_over_sized：镜像大小超限，不支持扫描。建议精简镜像。 - get_detail_info_not_found：获取镜像详细信息失败，镜像仓中可能已经不存在此镜像。请重新同步最新镜像。 - image_layer_over_sized：镜像层数超限，不支持扫描。建议精简镜像。 - schema_v1_not_support：Schema V1镜像不支持扫描。建议升级到V2版本。 - access_swr_failed：访问SWR服务出错。请向技术人员寻求帮助。 - swr_authentication_error：缺少SWR授权。请参考镜像授权指导设置权限。 - failed_to_scan_vulnerability：漏洞扫描失败。 - failed_to_scan_file：文件扫描失败。 - failed_to_scan_software：软件扫描失败。 - failed_to_check_sensitive_information：敏感信息核查失败。 - failed_to_check_baseline：基线检查失败。 - failed_to_check_software_compliance：软件合规检查失败。 - failed_to_query_basic_image_information：基础镜像信息查询失败。 - failed_to_check_build_cmd：镜像构建指令扫描失败。 - response_timed_out：响应超时。 - database_error：数据库错误。 - failed_to_send_the_scan_request：发送扫描请求失败。 

        :param scan_failed_code: The scan_failed_code of this RegistryImagesInfo.
        :type scan_failed_code: str
        """
        self._scan_failed_code = scan_failed_code

    @property
    def image_size(self):
        r"""Gets the image_size of this RegistryImagesInfo.

        **参数解释**: 镜像大小 **取值范围**: 取值0-2147483547 

        :return: The image_size of this RegistryImagesInfo.
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this RegistryImagesInfo.

        **参数解释**: 镜像大小 **取值范围**: 取值0-2147483547 

        :param image_size: The image_size of this RegistryImagesInfo.
        :type image_size: int
        """
        self._image_size = image_size

    @property
    def latest_update_time(self):
        r"""Gets the latest_update_time of this RegistryImagesInfo.

        **参数解释**: 镜像版本最后更新时间，时间单位 毫秒（ms） **取值范围**: 取值0-9223372036854775807 

        :return: The latest_update_time of this RegistryImagesInfo.
        :rtype: int
        """
        return self._latest_update_time

    @latest_update_time.setter
    def latest_update_time(self, latest_update_time):
        r"""Sets the latest_update_time of this RegistryImagesInfo.

        **参数解释**: 镜像版本最后更新时间，时间单位 毫秒（ms） **取值范围**: 取值0-9223372036854775807 

        :param latest_update_time: The latest_update_time of this RegistryImagesInfo.
        :type latest_update_time: int
        """
        self._latest_update_time = latest_update_time

    @property
    def latest_scan_time(self):
        r"""Gets the latest_scan_time of this RegistryImagesInfo.

        **参数解释**: 最近扫描时间，时间单位 毫秒（ms） **取值范围**: 取值0-9223372036854775807 

        :return: The latest_scan_time of this RegistryImagesInfo.
        :rtype: int
        """
        return self._latest_scan_time

    @latest_scan_time.setter
    def latest_scan_time(self, latest_scan_time):
        r"""Sets the latest_scan_time of this RegistryImagesInfo.

        **参数解释**: 最近扫描时间，时间单位 毫秒（ms） **取值范围**: 取值0-9223372036854775807 

        :param latest_scan_time: The latest_scan_time of this RegistryImagesInfo.
        :type latest_scan_time: int
        """
        self._latest_scan_time = latest_scan_time

    @property
    def latest_sync_time(self):
        r"""Gets the latest_sync_time of this RegistryImagesInfo.

        **参数解释**: 最近同步时间，时间单位 毫秒（ms） **取值范围**: 取值0-9223372036854775807 

        :return: The latest_sync_time of this RegistryImagesInfo.
        :rtype: int
        """
        return self._latest_sync_time

    @latest_sync_time.setter
    def latest_sync_time(self, latest_sync_time):
        r"""Sets the latest_sync_time of this RegistryImagesInfo.

        **参数解释**: 最近同步时间，时间单位 毫秒（ms） **取值范围**: 取值0-9223372036854775807 

        :param latest_sync_time: The latest_sync_time of this RegistryImagesInfo.
        :type latest_sync_time: int
        """
        self._latest_sync_time = latest_sync_time

    @property
    def vul_num(self):
        r"""Gets the vul_num of this RegistryImagesInfo.

        **参数解释**: 漏洞个数 **取值范围**: 取值0-2147483647 

        :return: The vul_num of this RegistryImagesInfo.
        :rtype: int
        """
        return self._vul_num

    @vul_num.setter
    def vul_num(self, vul_num):
        r"""Sets the vul_num of this RegistryImagesInfo.

        **参数解释**: 漏洞个数 **取值范围**: 取值0-2147483647 

        :param vul_num: The vul_num of this RegistryImagesInfo.
        :type vul_num: int
        """
        self._vul_num = vul_num

    @property
    def unsafe_setting_num(self):
        r"""Gets the unsafe_setting_num of this RegistryImagesInfo.

        **参数解释**: 基线扫描未通过数 **取值范围**: 取值0-2147483647 

        :return: The unsafe_setting_num of this RegistryImagesInfo.
        :rtype: int
        """
        return self._unsafe_setting_num

    @unsafe_setting_num.setter
    def unsafe_setting_num(self, unsafe_setting_num):
        r"""Sets the unsafe_setting_num of this RegistryImagesInfo.

        **参数解释**: 基线扫描未通过数 **取值范围**: 取值0-2147483647 

        :param unsafe_setting_num: The unsafe_setting_num of this RegistryImagesInfo.
        :type unsafe_setting_num: int
        """
        self._unsafe_setting_num = unsafe_setting_num

    @property
    def malicious_file_num(self):
        r"""Gets the malicious_file_num of this RegistryImagesInfo.

        **参数解释**: 恶意文件数 **取值范围**: 取值0-2147483647 

        :return: The malicious_file_num of this RegistryImagesInfo.
        :rtype: int
        """
        return self._malicious_file_num

    @malicious_file_num.setter
    def malicious_file_num(self, malicious_file_num):
        r"""Sets the malicious_file_num of this RegistryImagesInfo.

        **参数解释**: 恶意文件数 **取值范围**: 取值0-2147483647 

        :param malicious_file_num: The malicious_file_num of this RegistryImagesInfo.
        :type malicious_file_num: int
        """
        self._malicious_file_num = malicious_file_num

    @property
    def domain_name(self):
        r"""Gets the domain_name of this RegistryImagesInfo.

        **参数解释**: 拥有者（共享镜像参数） **取值范围**: 字符长度0-128 

        :return: The domain_name of this RegistryImagesInfo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this RegistryImagesInfo.

        **参数解释**: 拥有者（共享镜像参数） **取值范围**: 字符长度0-128 

        :param domain_name: The domain_name of this RegistryImagesInfo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def shared_status(self):
        r"""Gets the shared_status of this RegistryImagesInfo.

        **参数解释**： 共享镜像状态 **取值范围**： - expired：已过期。 - effective：有效。 

        :return: The shared_status of this RegistryImagesInfo.
        :rtype: str
        """
        return self._shared_status

    @shared_status.setter
    def shared_status(self, shared_status):
        r"""Sets the shared_status of this RegistryImagesInfo.

        **参数解释**： 共享镜像状态 **取值范围**： - expired：已过期。 - effective：有效。 

        :param shared_status: The shared_status of this RegistryImagesInfo.
        :type shared_status: str
        """
        self._shared_status = shared_status

    @property
    def scannable(self):
        r"""Gets the scannable of this RegistryImagesInfo.

        是否可扫描

        :return: The scannable of this RegistryImagesInfo.
        :rtype: bool
        """
        return self._scannable

    @scannable.setter
    def scannable(self, scannable):
        r"""Sets the scannable of this RegistryImagesInfo.

        是否可扫描

        :param scannable: The scannable of this RegistryImagesInfo.
        :type scannable: bool
        """
        self._scannable = scannable

    @property
    def is_multiple_arch(self):
        r"""Gets the is_multiple_arch of this RegistryImagesInfo.

        是否是多架构镜像

        :return: The is_multiple_arch of this RegistryImagesInfo.
        :rtype: bool
        """
        return self._is_multiple_arch

    @is_multiple_arch.setter
    def is_multiple_arch(self, is_multiple_arch):
        r"""Sets the is_multiple_arch of this RegistryImagesInfo.

        是否是多架构镜像

        :param is_multiple_arch: The is_multiple_arch of this RegistryImagesInfo.
        :type is_multiple_arch: bool
        """
        self._is_multiple_arch = is_multiple_arch

    @property
    def instance_name(self):
        r"""Gets the instance_name of this RegistryImagesInfo.

        **参数解释**: 企业版镜像实例名称 **取值范围**: 字符长度0-128 

        :return: The instance_name of this RegistryImagesInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this RegistryImagesInfo.

        **参数解释**: 企业版镜像实例名称 **取值范围**: 字符长度0-128 

        :param instance_name: The instance_name of this RegistryImagesInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this RegistryImagesInfo.

        **参数解释**: 企业版镜像实例ID **取值范围**: 字符长度0-64 

        :return: The instance_id of this RegistryImagesInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this RegistryImagesInfo.

        **参数解释**: 企业版镜像实例ID **取值范围**: 字符长度0-64 

        :param instance_id: The instance_id of this RegistryImagesInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_url(self):
        r"""Gets the instance_url of this RegistryImagesInfo.

        **参数解释**: 企业版镜像实例URL **取值范围**: 字符长度0-256 

        :return: The instance_url of this RegistryImagesInfo.
        :rtype: str
        """
        return self._instance_url

    @instance_url.setter
    def instance_url(self, instance_url):
        r"""Sets the instance_url of this RegistryImagesInfo.

        **参数解释**: 企业版镜像实例URL **取值范围**: 字符长度0-256 

        :param instance_url: The instance_url of this RegistryImagesInfo.
        :type instance_url: str
        """
        self._instance_url = instance_url

    @property
    def severity_level(self):
        r"""Gets the severity_level of this RegistryImagesInfo.

        **参数解释**: 镜像风险程度，在镜像扫描完成后展示 **取值范围**: - Security：安全。 - Low：低危。 - Medium：中危。 - High：高危。 

        :return: The severity_level of this RegistryImagesInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this RegistryImagesInfo.

        **参数解释**: 镜像风险程度，在镜像扫描完成后展示 **取值范围**: - Security：安全。 - Low：低危。 - Medium：中危。 - High：高危。 

        :param severity_level: The severity_level of this RegistryImagesInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def association_images(self):
        r"""Gets the association_images of this RegistryImagesInfo.

        多架构关联镜像信息

        :return: The association_images of this RegistryImagesInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AssociateImagesInfo`]
        """
        return self._association_images

    @association_images.setter
    def association_images(self, association_images):
        r"""Sets the association_images of this RegistryImagesInfo.

        多架构关联镜像信息

        :param association_images: The association_images of this RegistryImagesInfo.
        :type association_images: list[:class:`huaweicloudsdkhss.v5.AssociateImagesInfo`]
        """
        self._association_images = association_images

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
        if not isinstance(other, RegistryImagesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
