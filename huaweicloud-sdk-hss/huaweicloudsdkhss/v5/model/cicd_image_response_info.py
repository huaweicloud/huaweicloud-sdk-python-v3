# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CICDImageResponseInfo:

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
        'cicd_name': 'str',
        'namespace': 'str',
        'image_name': 'str',
        'image_digest': 'str',
        'image_version': 'str',
        'registry_name': 'str',
        'image_type': 'str',
        'registry_type': 'str',
        'latest_version': 'bool',
        'scan_status': 'str',
        'scan_failed_desc': 'str',
        'scan_failed_code': 'str',
        'image_size': 'int',
        'latest_update_time': 'int',
        'latest_scan_time': 'int',
        'vul_num': 'int',
        'unsafe_setting_num': 'int',
        'malicious_file_num': 'int',
        'severity_level': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'cicd_name': 'cicd_name',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_digest': 'image_digest',
        'image_version': 'image_version',
        'registry_name': 'registry_name',
        'image_type': 'image_type',
        'registry_type': 'registry_type',
        'latest_version': 'latest_version',
        'scan_status': 'scan_status',
        'scan_failed_desc': 'scan_failed_desc',
        'scan_failed_code': 'scan_failed_code',
        'image_size': 'image_size',
        'latest_update_time': 'latest_update_time',
        'latest_scan_time': 'latest_scan_time',
        'vul_num': 'vul_num',
        'unsafe_setting_num': 'unsafe_setting_num',
        'malicious_file_num': 'malicious_file_num',
        'severity_level': 'severity_level'
    }

    def __init__(self, image_id=None, cicd_name=None, namespace=None, image_name=None, image_digest=None, image_version=None, registry_name=None, image_type=None, registry_type=None, latest_version=None, scan_status=None, scan_failed_desc=None, scan_failed_code=None, image_size=None, latest_update_time=None, latest_scan_time=None, vul_num=None, unsafe_setting_num=None, malicious_file_num=None, severity_level=None):
        r"""CICDImageResponseInfo

        The model defined in huaweicloud sdk

        :param image_id: **参数解释**: cicd镜像标识 **取值范围**: 字符长度0-128位 
        :type image_id: str
        :param cicd_name: **参数解释**: cicd名称 **取值范围**: 字符长度0-128位 
        :type cicd_name: str
        :param namespace: **参数解释**: 命名空间 **取值范围**: 字符长度0-64位 
        :type namespace: str
        :param image_name: **参数解释**: 镜像名称 **取值范围**: 字符长度0-128位 
        :type image_name: str
        :param image_digest: **参数解释**: 镜像digest **取值范围**: 字符长度0-128位 
        :type image_digest: str
        :param image_version: **参数解释**: 镜像版本 **取值范围**: 字符长度0-64位 
        :type image_version: str
        :param registry_name: **参数解释**: 镜像仓库名称 **取值范围**: 字符长度1-128位 
        :type registry_name: str
        :param image_type: **参数解释**： 镜像类型 **取值范围**： - cicd ：cicd镜像。 
        :type image_type: str
        :param registry_type: **参数解释**： 镜像仓库类型 **取值范围**： - cicd ：cicd镜像。 
        :type registry_type: str
        :param latest_version: **参数解释**: 是否是最新版本 **取值范围**: - true：是。 - false：否。 
        :type latest_version: bool
        :param scan_status: **参数解释**: 扫描状态 **取值范围**: - unscan ：未扫描。 - success ：扫描完成。 - scanning ：正在扫描。 - failed ：扫描失败。 - download_failed ：下载失败。 - image_oversized ：镜像超大。 - waiting_for_scan ：等待扫描。 
        :type scan_status: str
        :param scan_failed_desc: **参数解释**: 扫描失败原因，包含如下16种。   - 未知错误   - 认证失败   - 镜像下载失败。请向技术人员寻求帮助。   - 镜像大小超限，不支持扫描。建议精简镜像。   - 获取镜像详细信息失败，镜像仓中可能已经不存在此镜像。请重新同步最新镜像。   - 镜像层数超限，不支持扫描。建议精简镜像。   - 漏洞扫描失败   - 文件扫描失败   - 软件扫描失败   - 敏感信息核查失败   - 基线检查失败   - 软件合规检查失败   - 基础镜像信息查询失败   - 响应超时   - 数据库错误   - 发送扫描请求失败 **取值范围**: 字符长度0-128位 
        :type scan_failed_desc: str
        :param scan_failed_code: **参数解释**: 扫描失败原因code，包含如下16种。   - \&quot;unknown_error\&quot;   - \&quot;authentication_failed\&quot;   - \&quot;download_failed\&quot;   - \&quot;image_over_sized\&quot;   - \&quot;get_detail_info_not_found\&quot;   - \&quot;image_layer_over_sized\&quot;   - \&quot;failed_to_scan_vulnerability\&quot;   - \&quot;failed_to_scan_file\&quot;   - \&quot;failed_to_scan_software\&quot;   - \&quot;failed_to_check_sensitive_information\&quot;   - \&quot;failed_to_check_baseline\&quot;   - \&quot;failed_to_check_software_compliance\&quot;   - \&quot;failed_to_query_basic_image_information\&quot;   - \&quot;response_timed_out\&quot;   - \&quot;database_error\&quot;   - \&quot;failed_to_send_the_scan_request\&quot; **取值范围**: 字符长度0-64位 
        :type scan_failed_code: str
        :param image_size: **参数解释**: 镜像大小 **取值范围**: 最小值0，最大值2147483547 
        :type image_size: int
        :param latest_update_time: **参数解释**: 镜像版本最后更新时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值9223372036854775807 
        :type latest_update_time: int
        :param latest_scan_time: **参数解释**: 最近扫描时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值9223372036854775807 
        :type latest_scan_time: int
        :param vul_num: **参数解释**: 漏洞个数 **取值范围**: 最小值0，最大值2147483647 
        :type vul_num: int
        :param unsafe_setting_num: **参数解释**: 基线扫描未通过数 **取值范围**: 最小值0，最大值2147483647 
        :type unsafe_setting_num: int
        :param malicious_file_num: **参数解释**: 恶意文件数 **取值范围**: 最小值0，最大值2147483647 
        :type malicious_file_num: int
        :param severity_level: **参数解释**: 镜像风险程度，在镜像扫描完成后展示 **取值范围**: - Security：安全。 - Low：低危。 - Medium：中危。 - High：高危。 
        :type severity_level: str
        """
        
        

        self._image_id = None
        self._cicd_name = None
        self._namespace = None
        self._image_name = None
        self._image_digest = None
        self._image_version = None
        self._registry_name = None
        self._image_type = None
        self._registry_type = None
        self._latest_version = None
        self._scan_status = None
        self._scan_failed_desc = None
        self._scan_failed_code = None
        self._image_size = None
        self._latest_update_time = None
        self._latest_scan_time = None
        self._vul_num = None
        self._unsafe_setting_num = None
        self._malicious_file_num = None
        self._severity_level = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if cicd_name is not None:
            self.cicd_name = cicd_name
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_digest is not None:
            self.image_digest = image_digest
        if image_version is not None:
            self.image_version = image_version
        if registry_name is not None:
            self.registry_name = registry_name
        if image_type is not None:
            self.image_type = image_type
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
        if vul_num is not None:
            self.vul_num = vul_num
        if unsafe_setting_num is not None:
            self.unsafe_setting_num = unsafe_setting_num
        if malicious_file_num is not None:
            self.malicious_file_num = malicious_file_num
        if severity_level is not None:
            self.severity_level = severity_level

    @property
    def image_id(self):
        r"""Gets the image_id of this CICDImageResponseInfo.

        **参数解释**: cicd镜像标识 **取值范围**: 字符长度0-128位 

        :return: The image_id of this CICDImageResponseInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this CICDImageResponseInfo.

        **参数解释**: cicd镜像标识 **取值范围**: 字符长度0-128位 

        :param image_id: The image_id of this CICDImageResponseInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def cicd_name(self):
        r"""Gets the cicd_name of this CICDImageResponseInfo.

        **参数解释**: cicd名称 **取值范围**: 字符长度0-128位 

        :return: The cicd_name of this CICDImageResponseInfo.
        :rtype: str
        """
        return self._cicd_name

    @cicd_name.setter
    def cicd_name(self, cicd_name):
        r"""Sets the cicd_name of this CICDImageResponseInfo.

        **参数解释**: cicd名称 **取值范围**: 字符长度0-128位 

        :param cicd_name: The cicd_name of this CICDImageResponseInfo.
        :type cicd_name: str
        """
        self._cicd_name = cicd_name

    @property
    def namespace(self):
        r"""Gets the namespace of this CICDImageResponseInfo.

        **参数解释**: 命名空间 **取值范围**: 字符长度0-64位 

        :return: The namespace of this CICDImageResponseInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this CICDImageResponseInfo.

        **参数解释**: 命名空间 **取值范围**: 字符长度0-64位 

        :param namespace: The namespace of this CICDImageResponseInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        r"""Gets the image_name of this CICDImageResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-128位 

        :return: The image_name of this CICDImageResponseInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this CICDImageResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-128位 

        :param image_name: The image_name of this CICDImageResponseInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_digest(self):
        r"""Gets the image_digest of this CICDImageResponseInfo.

        **参数解释**: 镜像digest **取值范围**: 字符长度0-128位 

        :return: The image_digest of this CICDImageResponseInfo.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        r"""Sets the image_digest of this CICDImageResponseInfo.

        **参数解释**: 镜像digest **取值范围**: 字符长度0-128位 

        :param image_digest: The image_digest of this CICDImageResponseInfo.
        :type image_digest: str
        """
        self._image_digest = image_digest

    @property
    def image_version(self):
        r"""Gets the image_version of this CICDImageResponseInfo.

        **参数解释**: 镜像版本 **取值范围**: 字符长度0-64位 

        :return: The image_version of this CICDImageResponseInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this CICDImageResponseInfo.

        **参数解释**: 镜像版本 **取值范围**: 字符长度0-64位 

        :param image_version: The image_version of this CICDImageResponseInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def registry_name(self):
        r"""Gets the registry_name of this CICDImageResponseInfo.

        **参数解释**: 镜像仓库名称 **取值范围**: 字符长度1-128位 

        :return: The registry_name of this CICDImageResponseInfo.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        r"""Sets the registry_name of this CICDImageResponseInfo.

        **参数解释**: 镜像仓库名称 **取值范围**: 字符长度1-128位 

        :param registry_name: The registry_name of this CICDImageResponseInfo.
        :type registry_name: str
        """
        self._registry_name = registry_name

    @property
    def image_type(self):
        r"""Gets the image_type of this CICDImageResponseInfo.

        **参数解释**： 镜像类型 **取值范围**： - cicd ：cicd镜像。 

        :return: The image_type of this CICDImageResponseInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this CICDImageResponseInfo.

        **参数解释**： 镜像类型 **取值范围**： - cicd ：cicd镜像。 

        :param image_type: The image_type of this CICDImageResponseInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def registry_type(self):
        r"""Gets the registry_type of this CICDImageResponseInfo.

        **参数解释**： 镜像仓库类型 **取值范围**： - cicd ：cicd镜像。 

        :return: The registry_type of this CICDImageResponseInfo.
        :rtype: str
        """
        return self._registry_type

    @registry_type.setter
    def registry_type(self, registry_type):
        r"""Sets the registry_type of this CICDImageResponseInfo.

        **参数解释**： 镜像仓库类型 **取值范围**： - cicd ：cicd镜像。 

        :param registry_type: The registry_type of this CICDImageResponseInfo.
        :type registry_type: str
        """
        self._registry_type = registry_type

    @property
    def latest_version(self):
        r"""Gets the latest_version of this CICDImageResponseInfo.

        **参数解释**: 是否是最新版本 **取值范围**: - true：是。 - false：否。 

        :return: The latest_version of this CICDImageResponseInfo.
        :rtype: bool
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this CICDImageResponseInfo.

        **参数解释**: 是否是最新版本 **取值范围**: - true：是。 - false：否。 

        :param latest_version: The latest_version of this CICDImageResponseInfo.
        :type latest_version: bool
        """
        self._latest_version = latest_version

    @property
    def scan_status(self):
        r"""Gets the scan_status of this CICDImageResponseInfo.

        **参数解释**: 扫描状态 **取值范围**: - unscan ：未扫描。 - success ：扫描完成。 - scanning ：正在扫描。 - failed ：扫描失败。 - download_failed ：下载失败。 - image_oversized ：镜像超大。 - waiting_for_scan ：等待扫描。 

        :return: The scan_status of this CICDImageResponseInfo.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this CICDImageResponseInfo.

        **参数解释**: 扫描状态 **取值范围**: - unscan ：未扫描。 - success ：扫描完成。 - scanning ：正在扫描。 - failed ：扫描失败。 - download_failed ：下载失败。 - image_oversized ：镜像超大。 - waiting_for_scan ：等待扫描。 

        :param scan_status: The scan_status of this CICDImageResponseInfo.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def scan_failed_desc(self):
        r"""Gets the scan_failed_desc of this CICDImageResponseInfo.

        **参数解释**: 扫描失败原因，包含如下16种。   - 未知错误   - 认证失败   - 镜像下载失败。请向技术人员寻求帮助。   - 镜像大小超限，不支持扫描。建议精简镜像。   - 获取镜像详细信息失败，镜像仓中可能已经不存在此镜像。请重新同步最新镜像。   - 镜像层数超限，不支持扫描。建议精简镜像。   - 漏洞扫描失败   - 文件扫描失败   - 软件扫描失败   - 敏感信息核查失败   - 基线检查失败   - 软件合规检查失败   - 基础镜像信息查询失败   - 响应超时   - 数据库错误   - 发送扫描请求失败 **取值范围**: 字符长度0-128位 

        :return: The scan_failed_desc of this CICDImageResponseInfo.
        :rtype: str
        """
        return self._scan_failed_desc

    @scan_failed_desc.setter
    def scan_failed_desc(self, scan_failed_desc):
        r"""Sets the scan_failed_desc of this CICDImageResponseInfo.

        **参数解释**: 扫描失败原因，包含如下16种。   - 未知错误   - 认证失败   - 镜像下载失败。请向技术人员寻求帮助。   - 镜像大小超限，不支持扫描。建议精简镜像。   - 获取镜像详细信息失败，镜像仓中可能已经不存在此镜像。请重新同步最新镜像。   - 镜像层数超限，不支持扫描。建议精简镜像。   - 漏洞扫描失败   - 文件扫描失败   - 软件扫描失败   - 敏感信息核查失败   - 基线检查失败   - 软件合规检查失败   - 基础镜像信息查询失败   - 响应超时   - 数据库错误   - 发送扫描请求失败 **取值范围**: 字符长度0-128位 

        :param scan_failed_desc: The scan_failed_desc of this CICDImageResponseInfo.
        :type scan_failed_desc: str
        """
        self._scan_failed_desc = scan_failed_desc

    @property
    def scan_failed_code(self):
        r"""Gets the scan_failed_code of this CICDImageResponseInfo.

        **参数解释**: 扫描失败原因code，包含如下16种。   - \"unknown_error\"   - \"authentication_failed\"   - \"download_failed\"   - \"image_over_sized\"   - \"get_detail_info_not_found\"   - \"image_layer_over_sized\"   - \"failed_to_scan_vulnerability\"   - \"failed_to_scan_file\"   - \"failed_to_scan_software\"   - \"failed_to_check_sensitive_information\"   - \"failed_to_check_baseline\"   - \"failed_to_check_software_compliance\"   - \"failed_to_query_basic_image_information\"   - \"response_timed_out\"   - \"database_error\"   - \"failed_to_send_the_scan_request\" **取值范围**: 字符长度0-64位 

        :return: The scan_failed_code of this CICDImageResponseInfo.
        :rtype: str
        """
        return self._scan_failed_code

    @scan_failed_code.setter
    def scan_failed_code(self, scan_failed_code):
        r"""Sets the scan_failed_code of this CICDImageResponseInfo.

        **参数解释**: 扫描失败原因code，包含如下16种。   - \"unknown_error\"   - \"authentication_failed\"   - \"download_failed\"   - \"image_over_sized\"   - \"get_detail_info_not_found\"   - \"image_layer_over_sized\"   - \"failed_to_scan_vulnerability\"   - \"failed_to_scan_file\"   - \"failed_to_scan_software\"   - \"failed_to_check_sensitive_information\"   - \"failed_to_check_baseline\"   - \"failed_to_check_software_compliance\"   - \"failed_to_query_basic_image_information\"   - \"response_timed_out\"   - \"database_error\"   - \"failed_to_send_the_scan_request\" **取值范围**: 字符长度0-64位 

        :param scan_failed_code: The scan_failed_code of this CICDImageResponseInfo.
        :type scan_failed_code: str
        """
        self._scan_failed_code = scan_failed_code

    @property
    def image_size(self):
        r"""Gets the image_size of this CICDImageResponseInfo.

        **参数解释**: 镜像大小 **取值范围**: 最小值0，最大值2147483547 

        :return: The image_size of this CICDImageResponseInfo.
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this CICDImageResponseInfo.

        **参数解释**: 镜像大小 **取值范围**: 最小值0，最大值2147483547 

        :param image_size: The image_size of this CICDImageResponseInfo.
        :type image_size: int
        """
        self._image_size = image_size

    @property
    def latest_update_time(self):
        r"""Gets the latest_update_time of this CICDImageResponseInfo.

        **参数解释**: 镜像版本最后更新时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The latest_update_time of this CICDImageResponseInfo.
        :rtype: int
        """
        return self._latest_update_time

    @latest_update_time.setter
    def latest_update_time(self, latest_update_time):
        r"""Sets the latest_update_time of this CICDImageResponseInfo.

        **参数解释**: 镜像版本最后更新时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值9223372036854775807 

        :param latest_update_time: The latest_update_time of this CICDImageResponseInfo.
        :type latest_update_time: int
        """
        self._latest_update_time = latest_update_time

    @property
    def latest_scan_time(self):
        r"""Gets the latest_scan_time of this CICDImageResponseInfo.

        **参数解释**: 最近扫描时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The latest_scan_time of this CICDImageResponseInfo.
        :rtype: int
        """
        return self._latest_scan_time

    @latest_scan_time.setter
    def latest_scan_time(self, latest_scan_time):
        r"""Sets the latest_scan_time of this CICDImageResponseInfo.

        **参数解释**: 最近扫描时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值9223372036854775807 

        :param latest_scan_time: The latest_scan_time of this CICDImageResponseInfo.
        :type latest_scan_time: int
        """
        self._latest_scan_time = latest_scan_time

    @property
    def vul_num(self):
        r"""Gets the vul_num of this CICDImageResponseInfo.

        **参数解释**: 漏洞个数 **取值范围**: 最小值0，最大值2147483647 

        :return: The vul_num of this CICDImageResponseInfo.
        :rtype: int
        """
        return self._vul_num

    @vul_num.setter
    def vul_num(self, vul_num):
        r"""Sets the vul_num of this CICDImageResponseInfo.

        **参数解释**: 漏洞个数 **取值范围**: 最小值0，最大值2147483647 

        :param vul_num: The vul_num of this CICDImageResponseInfo.
        :type vul_num: int
        """
        self._vul_num = vul_num

    @property
    def unsafe_setting_num(self):
        r"""Gets the unsafe_setting_num of this CICDImageResponseInfo.

        **参数解释**: 基线扫描未通过数 **取值范围**: 最小值0，最大值2147483647 

        :return: The unsafe_setting_num of this CICDImageResponseInfo.
        :rtype: int
        """
        return self._unsafe_setting_num

    @unsafe_setting_num.setter
    def unsafe_setting_num(self, unsafe_setting_num):
        r"""Sets the unsafe_setting_num of this CICDImageResponseInfo.

        **参数解释**: 基线扫描未通过数 **取值范围**: 最小值0，最大值2147483647 

        :param unsafe_setting_num: The unsafe_setting_num of this CICDImageResponseInfo.
        :type unsafe_setting_num: int
        """
        self._unsafe_setting_num = unsafe_setting_num

    @property
    def malicious_file_num(self):
        r"""Gets the malicious_file_num of this CICDImageResponseInfo.

        **参数解释**: 恶意文件数 **取值范围**: 最小值0，最大值2147483647 

        :return: The malicious_file_num of this CICDImageResponseInfo.
        :rtype: int
        """
        return self._malicious_file_num

    @malicious_file_num.setter
    def malicious_file_num(self, malicious_file_num):
        r"""Sets the malicious_file_num of this CICDImageResponseInfo.

        **参数解释**: 恶意文件数 **取值范围**: 最小值0，最大值2147483647 

        :param malicious_file_num: The malicious_file_num of this CICDImageResponseInfo.
        :type malicious_file_num: int
        """
        self._malicious_file_num = malicious_file_num

    @property
    def severity_level(self):
        r"""Gets the severity_level of this CICDImageResponseInfo.

        **参数解释**: 镜像风险程度，在镜像扫描完成后展示 **取值范围**: - Security：安全。 - Low：低危。 - Medium：中危。 - High：高危。 

        :return: The severity_level of this CICDImageResponseInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this CICDImageResponseInfo.

        **参数解释**: 镜像风险程度，在镜像扫描完成后展示 **取值范围**: - Security：安全。 - Low：低危。 - Medium：中危。 - High：高危。 

        :param severity_level: The severity_level of this CICDImageResponseInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

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
        if not isinstance(other, CICDImageResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
