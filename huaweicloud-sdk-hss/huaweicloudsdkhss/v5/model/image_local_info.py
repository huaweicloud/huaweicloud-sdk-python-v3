# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageLocalInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_name': 'str',
        'image_id': 'str',
        'image_digest': 'str',
        'image_version': 'str',
        'local_image_type': 'str',
        'scan_status': 'str',
        'image_size': 'int',
        'latest_update_time': 'int',
        'latest_scan_time': 'int',
        'vul_num': 'int',
        'unsafe_setting_num': 'int',
        'malicious_file_num': 'int',
        'host_num': 'int',
        'container_num': 'int',
        'component_num': 'int',
        'scan_failed_desc': 'str',
        'severity_level': 'str',
        'host_name': 'str',
        'host_id': 'str',
        'agent_id': 'str',
        'non_scan_reason': 'str'
    }

    attribute_map = {
        'image_name': 'image_name',
        'image_id': 'image_id',
        'image_digest': 'image_digest',
        'image_version': 'image_version',
        'local_image_type': 'local_image_type',
        'scan_status': 'scan_status',
        'image_size': 'image_size',
        'latest_update_time': 'latest_update_time',
        'latest_scan_time': 'latest_scan_time',
        'vul_num': 'vul_num',
        'unsafe_setting_num': 'unsafe_setting_num',
        'malicious_file_num': 'malicious_file_num',
        'host_num': 'host_num',
        'container_num': 'container_num',
        'component_num': 'component_num',
        'scan_failed_desc': 'scan_failed_desc',
        'severity_level': 'severity_level',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'agent_id': 'agent_id',
        'non_scan_reason': 'non_scan_reason'
    }

    def __init__(self, image_name=None, image_id=None, image_digest=None, image_version=None, local_image_type=None, scan_status=None, image_size=None, latest_update_time=None, latest_scan_time=None, vul_num=None, unsafe_setting_num=None, malicious_file_num=None, host_num=None, container_num=None, component_num=None, scan_failed_desc=None, severity_level=None, host_name=None, host_id=None, agent_id=None, non_scan_reason=None):
        r"""ImageLocalInfo

        The model defined in huaweicloud sdk

        :param image_name: **参数解释** 镜像名称 **取值范围** 字符长度0-256位 
        :type image_name: str
        :param image_id: **参数解释** 本地镜像的唯一标识，用于后续查询镜像详情、执行扫描等操作 **取值范围** 字符长度1-64位，支持字母、数字、短横线，符合UUID格式 
        :type image_id: str
        :param image_digest: **参数解释** 本地镜像的加密摘要（SHA-256算法），用于唯一标识镜像内容，避免篡改 **取值范围** 字符长度64-128位，以&#39;sha256:&#39;开头，后跟十六进制字符串（如sha256:ce0b5d91b072730d0bc9518f11efd07eb7fdb9f43251e11a96cab5b1918b7044） 
        :type image_digest: str
        :param image_version: **参数解释** 镜像版本 **取值范围** 字符长度0-256位 
        :type image_version: str
        :param local_image_type: **参数解释** 本地镜像的存储来源类型，标识镜像是否来自华为云SWR仓库 **取值范围** swr_image：华为云SWR仓库镜像 other_image：非SWR仓库镜像 
        :type local_image_type: str
        :param scan_status: **参数解释** 本地镜像的安全扫描状态，反映当前镜像是否完成安全检测 **取值范围** 扫描状态，包含如下：   - unscan：未扫描   - success：扫描完成   - scanning：正在扫描   - failed：扫描失败   - waiting：等待扫描 
        :type scan_status: str
        :param image_size: **参数解释** 本地镜像的实际存储大小，单位为字节（B） **取值范围** 取值0-9223372036854775807（约9EB） 
        :type image_size: int
        :param latest_update_time: **参数解释** 本地镜像版本的最后更新时间，即镜像创建或更新的时间戳 **取值范围** Unix时间戳（单位ms），取值0-9223372036854775807 
        :type latest_update_time: int
        :param latest_scan_time: **参数解释** 本地镜像最近一次完成安全扫描的时间戳，未扫描时该字段可能为0或空 **取值范围** Unix时间戳（单位ms），取值0-9223372036854775807，未扫描时为0 
        :type latest_scan_time: int
        :param vul_num: **参数解释** 本地镜像中检测到的软件漏洞总数，包含高、中、低危漏洞 **取值范围** 取值0-9223372036854775807 
        :type vul_num: int
        :param unsafe_setting_num: **参数解释** 本地镜像在安全基线扫描中未通过的检查项数量，反映镜像配置合规性 **取值范围** 取值0-9223372036854775807 
        :type unsafe_setting_num: int
        :param malicious_file_num: **参数解释** 本地镜像中检测到的恶意文件（如病毒、木马）总数 **取值范围** 取值0-9223372036854775807 
        :type malicious_file_num: int
        :param host_num: **参数解释** 当前本地镜像所关联的云服务器总数 **取值范围** 取值0-9223372036854775807 
        :type host_num: int
        :param container_num: **参数解释** 当前本地镜像所创建或关联的容器总数 **取值范围** 取值0-9223372036854775807 
        :type container_num: int
        :param component_num: **参数解释** 本地镜像中包含的软件组件（如依赖库、应用程序）总数 **取值范围** 取值0-9223372036854775807 
        :type component_num: int
        :param scan_failed_desc: **参数解释** 当scan_status为failed时，该字段说明扫描失败的具体原因，未失败时为空字符串 **取值范围** - unknown_error：未知错误 - failed_to_match_agent：对应主机未开启容器版防护或agent离线 - create_container_failed：创建容器失败      - get_container_info_failed：获取容器信息失败 - docker_offline：docker引擎不在线 - get_docker_root_failed：获取容器根文件系统失败 - image_not_exist_or_docker_api_fault：镜像不存在或docker接口错误 - huge_image：超大镜像 - docker_root_in_nfs：容器根目录位于网络挂载 - response_timed_out：响应超时 
        :type scan_failed_desc: str
        :param severity_level: **参数解释** 根据镜像的漏洞、基线违规、恶意文件情况综合评定的风险等级 **取值范围** - Security：安全 - Low：低危 - Medium：中危 - High：高危 
        :type severity_level: str
        :param host_name: **参数解释** 应用防护事件所属云服务器的名称，用于标识事件来源主机 **取值范围** 字符长度1-64位，支持中文、英文、数字、短横线、下划线，符合华为云ECS命名规范 
        :type host_name: str
        :param host_id: **参数解释**: 主机id **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及
        :type host_id: str
        :param agent_id: **参数解释** 本地镜像所在服务器上安装的HSS Agent唯一标识，用于关联Agent相关操作 **取值范围** 字符长度1-128位，支持字母、数字、短横线、下划线 
        :type agent_id: str
        :param non_scan_reason: **参数解释** 说明本地镜像无法进行安全扫描的具体原因（如镜像格式不支持、权限不足等），为空表示支持扫描 **取值范围** 字符长度0-1024位，支持中文、英文、数字、常用标点符号 
        :type non_scan_reason: str
        """
        
        

        self._image_name = None
        self._image_id = None
        self._image_digest = None
        self._image_version = None
        self._local_image_type = None
        self._scan_status = None
        self._image_size = None
        self._latest_update_time = None
        self._latest_scan_time = None
        self._vul_num = None
        self._unsafe_setting_num = None
        self._malicious_file_num = None
        self._host_num = None
        self._container_num = None
        self._component_num = None
        self._scan_failed_desc = None
        self._severity_level = None
        self._host_name = None
        self._host_id = None
        self._agent_id = None
        self._non_scan_reason = None
        self.discriminator = None

        if image_name is not None:
            self.image_name = image_name
        if image_id is not None:
            self.image_id = image_id
        if image_digest is not None:
            self.image_digest = image_digest
        if image_version is not None:
            self.image_version = image_version
        if local_image_type is not None:
            self.local_image_type = local_image_type
        if scan_status is not None:
            self.scan_status = scan_status
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
        if host_num is not None:
            self.host_num = host_num
        if container_num is not None:
            self.container_num = container_num
        if component_num is not None:
            self.component_num = component_num
        if scan_failed_desc is not None:
            self.scan_failed_desc = scan_failed_desc
        if severity_level is not None:
            self.severity_level = severity_level
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if agent_id is not None:
            self.agent_id = agent_id
        if non_scan_reason is not None:
            self.non_scan_reason = non_scan_reason

    @property
    def image_name(self):
        r"""Gets the image_name of this ImageLocalInfo.

        **参数解释** 镜像名称 **取值范围** 字符长度0-256位 

        :return: The image_name of this ImageLocalInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ImageLocalInfo.

        **参数解释** 镜像名称 **取值范围** 字符长度0-256位 

        :param image_name: The image_name of this ImageLocalInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_id(self):
        r"""Gets the image_id of this ImageLocalInfo.

        **参数解释** 本地镜像的唯一标识，用于后续查询镜像详情、执行扫描等操作 **取值范围** 字符长度1-64位，支持字母、数字、短横线，符合UUID格式 

        :return: The image_id of this ImageLocalInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ImageLocalInfo.

        **参数解释** 本地镜像的唯一标识，用于后续查询镜像详情、执行扫描等操作 **取值范围** 字符长度1-64位，支持字母、数字、短横线，符合UUID格式 

        :param image_id: The image_id of this ImageLocalInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_digest(self):
        r"""Gets the image_digest of this ImageLocalInfo.

        **参数解释** 本地镜像的加密摘要（SHA-256算法），用于唯一标识镜像内容，避免篡改 **取值范围** 字符长度64-128位，以'sha256:'开头，后跟十六进制字符串（如sha256:ce0b5d91b072730d0bc9518f11efd07eb7fdb9f43251e11a96cab5b1918b7044） 

        :return: The image_digest of this ImageLocalInfo.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        r"""Sets the image_digest of this ImageLocalInfo.

        **参数解释** 本地镜像的加密摘要（SHA-256算法），用于唯一标识镜像内容，避免篡改 **取值范围** 字符长度64-128位，以'sha256:'开头，后跟十六进制字符串（如sha256:ce0b5d91b072730d0bc9518f11efd07eb7fdb9f43251e11a96cab5b1918b7044） 

        :param image_digest: The image_digest of this ImageLocalInfo.
        :type image_digest: str
        """
        self._image_digest = image_digest

    @property
    def image_version(self):
        r"""Gets the image_version of this ImageLocalInfo.

        **参数解释** 镜像版本 **取值范围** 字符长度0-256位 

        :return: The image_version of this ImageLocalInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ImageLocalInfo.

        **参数解释** 镜像版本 **取值范围** 字符长度0-256位 

        :param image_version: The image_version of this ImageLocalInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def local_image_type(self):
        r"""Gets the local_image_type of this ImageLocalInfo.

        **参数解释** 本地镜像的存储来源类型，标识镜像是否来自华为云SWR仓库 **取值范围** swr_image：华为云SWR仓库镜像 other_image：非SWR仓库镜像 

        :return: The local_image_type of this ImageLocalInfo.
        :rtype: str
        """
        return self._local_image_type

    @local_image_type.setter
    def local_image_type(self, local_image_type):
        r"""Sets the local_image_type of this ImageLocalInfo.

        **参数解释** 本地镜像的存储来源类型，标识镜像是否来自华为云SWR仓库 **取值范围** swr_image：华为云SWR仓库镜像 other_image：非SWR仓库镜像 

        :param local_image_type: The local_image_type of this ImageLocalInfo.
        :type local_image_type: str
        """
        self._local_image_type = local_image_type

    @property
    def scan_status(self):
        r"""Gets the scan_status of this ImageLocalInfo.

        **参数解释** 本地镜像的安全扫描状态，反映当前镜像是否完成安全检测 **取值范围** 扫描状态，包含如下：   - unscan：未扫描   - success：扫描完成   - scanning：正在扫描   - failed：扫描失败   - waiting：等待扫描 

        :return: The scan_status of this ImageLocalInfo.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this ImageLocalInfo.

        **参数解释** 本地镜像的安全扫描状态，反映当前镜像是否完成安全检测 **取值范围** 扫描状态，包含如下：   - unscan：未扫描   - success：扫描完成   - scanning：正在扫描   - failed：扫描失败   - waiting：等待扫描 

        :param scan_status: The scan_status of this ImageLocalInfo.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def image_size(self):
        r"""Gets the image_size of this ImageLocalInfo.

        **参数解释** 本地镜像的实际存储大小，单位为字节（B） **取值范围** 取值0-9223372036854775807（约9EB） 

        :return: The image_size of this ImageLocalInfo.
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this ImageLocalInfo.

        **参数解释** 本地镜像的实际存储大小，单位为字节（B） **取值范围** 取值0-9223372036854775807（约9EB） 

        :param image_size: The image_size of this ImageLocalInfo.
        :type image_size: int
        """
        self._image_size = image_size

    @property
    def latest_update_time(self):
        r"""Gets the latest_update_time of this ImageLocalInfo.

        **参数解释** 本地镜像版本的最后更新时间，即镜像创建或更新的时间戳 **取值范围** Unix时间戳（单位ms），取值0-9223372036854775807 

        :return: The latest_update_time of this ImageLocalInfo.
        :rtype: int
        """
        return self._latest_update_time

    @latest_update_time.setter
    def latest_update_time(self, latest_update_time):
        r"""Sets the latest_update_time of this ImageLocalInfo.

        **参数解释** 本地镜像版本的最后更新时间，即镜像创建或更新的时间戳 **取值范围** Unix时间戳（单位ms），取值0-9223372036854775807 

        :param latest_update_time: The latest_update_time of this ImageLocalInfo.
        :type latest_update_time: int
        """
        self._latest_update_time = latest_update_time

    @property
    def latest_scan_time(self):
        r"""Gets the latest_scan_time of this ImageLocalInfo.

        **参数解释** 本地镜像最近一次完成安全扫描的时间戳，未扫描时该字段可能为0或空 **取值范围** Unix时间戳（单位ms），取值0-9223372036854775807，未扫描时为0 

        :return: The latest_scan_time of this ImageLocalInfo.
        :rtype: int
        """
        return self._latest_scan_time

    @latest_scan_time.setter
    def latest_scan_time(self, latest_scan_time):
        r"""Sets the latest_scan_time of this ImageLocalInfo.

        **参数解释** 本地镜像最近一次完成安全扫描的时间戳，未扫描时该字段可能为0或空 **取值范围** Unix时间戳（单位ms），取值0-9223372036854775807，未扫描时为0 

        :param latest_scan_time: The latest_scan_time of this ImageLocalInfo.
        :type latest_scan_time: int
        """
        self._latest_scan_time = latest_scan_time

    @property
    def vul_num(self):
        r"""Gets the vul_num of this ImageLocalInfo.

        **参数解释** 本地镜像中检测到的软件漏洞总数，包含高、中、低危漏洞 **取值范围** 取值0-9223372036854775807 

        :return: The vul_num of this ImageLocalInfo.
        :rtype: int
        """
        return self._vul_num

    @vul_num.setter
    def vul_num(self, vul_num):
        r"""Sets the vul_num of this ImageLocalInfo.

        **参数解释** 本地镜像中检测到的软件漏洞总数，包含高、中、低危漏洞 **取值范围** 取值0-9223372036854775807 

        :param vul_num: The vul_num of this ImageLocalInfo.
        :type vul_num: int
        """
        self._vul_num = vul_num

    @property
    def unsafe_setting_num(self):
        r"""Gets the unsafe_setting_num of this ImageLocalInfo.

        **参数解释** 本地镜像在安全基线扫描中未通过的检查项数量，反映镜像配置合规性 **取值范围** 取值0-9223372036854775807 

        :return: The unsafe_setting_num of this ImageLocalInfo.
        :rtype: int
        """
        return self._unsafe_setting_num

    @unsafe_setting_num.setter
    def unsafe_setting_num(self, unsafe_setting_num):
        r"""Sets the unsafe_setting_num of this ImageLocalInfo.

        **参数解释** 本地镜像在安全基线扫描中未通过的检查项数量，反映镜像配置合规性 **取值范围** 取值0-9223372036854775807 

        :param unsafe_setting_num: The unsafe_setting_num of this ImageLocalInfo.
        :type unsafe_setting_num: int
        """
        self._unsafe_setting_num = unsafe_setting_num

    @property
    def malicious_file_num(self):
        r"""Gets the malicious_file_num of this ImageLocalInfo.

        **参数解释** 本地镜像中检测到的恶意文件（如病毒、木马）总数 **取值范围** 取值0-9223372036854775807 

        :return: The malicious_file_num of this ImageLocalInfo.
        :rtype: int
        """
        return self._malicious_file_num

    @malicious_file_num.setter
    def malicious_file_num(self, malicious_file_num):
        r"""Sets the malicious_file_num of this ImageLocalInfo.

        **参数解释** 本地镜像中检测到的恶意文件（如病毒、木马）总数 **取值范围** 取值0-9223372036854775807 

        :param malicious_file_num: The malicious_file_num of this ImageLocalInfo.
        :type malicious_file_num: int
        """
        self._malicious_file_num = malicious_file_num

    @property
    def host_num(self):
        r"""Gets the host_num of this ImageLocalInfo.

        **参数解释** 当前本地镜像所关联的云服务器总数 **取值范围** 取值0-9223372036854775807 

        :return: The host_num of this ImageLocalInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this ImageLocalInfo.

        **参数解释** 当前本地镜像所关联的云服务器总数 **取值范围** 取值0-9223372036854775807 

        :param host_num: The host_num of this ImageLocalInfo.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def container_num(self):
        r"""Gets the container_num of this ImageLocalInfo.

        **参数解释** 当前本地镜像所创建或关联的容器总数 **取值范围** 取值0-9223372036854775807 

        :return: The container_num of this ImageLocalInfo.
        :rtype: int
        """
        return self._container_num

    @container_num.setter
    def container_num(self, container_num):
        r"""Sets the container_num of this ImageLocalInfo.

        **参数解释** 当前本地镜像所创建或关联的容器总数 **取值范围** 取值0-9223372036854775807 

        :param container_num: The container_num of this ImageLocalInfo.
        :type container_num: int
        """
        self._container_num = container_num

    @property
    def component_num(self):
        r"""Gets the component_num of this ImageLocalInfo.

        **参数解释** 本地镜像中包含的软件组件（如依赖库、应用程序）总数 **取值范围** 取值0-9223372036854775807 

        :return: The component_num of this ImageLocalInfo.
        :rtype: int
        """
        return self._component_num

    @component_num.setter
    def component_num(self, component_num):
        r"""Sets the component_num of this ImageLocalInfo.

        **参数解释** 本地镜像中包含的软件组件（如依赖库、应用程序）总数 **取值范围** 取值0-9223372036854775807 

        :param component_num: The component_num of this ImageLocalInfo.
        :type component_num: int
        """
        self._component_num = component_num

    @property
    def scan_failed_desc(self):
        r"""Gets the scan_failed_desc of this ImageLocalInfo.

        **参数解释** 当scan_status为failed时，该字段说明扫描失败的具体原因，未失败时为空字符串 **取值范围** - unknown_error：未知错误 - failed_to_match_agent：对应主机未开启容器版防护或agent离线 - create_container_failed：创建容器失败      - get_container_info_failed：获取容器信息失败 - docker_offline：docker引擎不在线 - get_docker_root_failed：获取容器根文件系统失败 - image_not_exist_or_docker_api_fault：镜像不存在或docker接口错误 - huge_image：超大镜像 - docker_root_in_nfs：容器根目录位于网络挂载 - response_timed_out：响应超时 

        :return: The scan_failed_desc of this ImageLocalInfo.
        :rtype: str
        """
        return self._scan_failed_desc

    @scan_failed_desc.setter
    def scan_failed_desc(self, scan_failed_desc):
        r"""Sets the scan_failed_desc of this ImageLocalInfo.

        **参数解释** 当scan_status为failed时，该字段说明扫描失败的具体原因，未失败时为空字符串 **取值范围** - unknown_error：未知错误 - failed_to_match_agent：对应主机未开启容器版防护或agent离线 - create_container_failed：创建容器失败      - get_container_info_failed：获取容器信息失败 - docker_offline：docker引擎不在线 - get_docker_root_failed：获取容器根文件系统失败 - image_not_exist_or_docker_api_fault：镜像不存在或docker接口错误 - huge_image：超大镜像 - docker_root_in_nfs：容器根目录位于网络挂载 - response_timed_out：响应超时 

        :param scan_failed_desc: The scan_failed_desc of this ImageLocalInfo.
        :type scan_failed_desc: str
        """
        self._scan_failed_desc = scan_failed_desc

    @property
    def severity_level(self):
        r"""Gets the severity_level of this ImageLocalInfo.

        **参数解释** 根据镜像的漏洞、基线违规、恶意文件情况综合评定的风险等级 **取值范围** - Security：安全 - Low：低危 - Medium：中危 - High：高危 

        :return: The severity_level of this ImageLocalInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this ImageLocalInfo.

        **参数解释** 根据镜像的漏洞、基线违规、恶意文件情况综合评定的风险等级 **取值范围** - Security：安全 - Low：低危 - Medium：中危 - High：高危 

        :param severity_level: The severity_level of this ImageLocalInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def host_name(self):
        r"""Gets the host_name of this ImageLocalInfo.

        **参数解释** 应用防护事件所属云服务器的名称，用于标识事件来源主机 **取值范围** 字符长度1-64位，支持中文、英文、数字、短横线、下划线，符合华为云ECS命名规范 

        :return: The host_name of this ImageLocalInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ImageLocalInfo.

        **参数解释** 应用防护事件所属云服务器的名称，用于标识事件来源主机 **取值范围** 字符长度1-64位，支持中文、英文、数字、短横线、下划线，符合华为云ECS命名规范 

        :param host_name: The host_name of this ImageLocalInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ImageLocalInfo.

        **参数解释**: 主机id **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及

        :return: The host_id of this ImageLocalInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ImageLocalInfo.

        **参数解释**: 主机id **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及

        :param host_id: The host_id of this ImageLocalInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def agent_id(self):
        r"""Gets the agent_id of this ImageLocalInfo.

        **参数解释** 本地镜像所在服务器上安装的HSS Agent唯一标识，用于关联Agent相关操作 **取值范围** 字符长度1-128位，支持字母、数字、短横线、下划线 

        :return: The agent_id of this ImageLocalInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ImageLocalInfo.

        **参数解释** 本地镜像所在服务器上安装的HSS Agent唯一标识，用于关联Agent相关操作 **取值范围** 字符长度1-128位，支持字母、数字、短横线、下划线 

        :param agent_id: The agent_id of this ImageLocalInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def non_scan_reason(self):
        r"""Gets the non_scan_reason of this ImageLocalInfo.

        **参数解释** 说明本地镜像无法进行安全扫描的具体原因（如镜像格式不支持、权限不足等），为空表示支持扫描 **取值范围** 字符长度0-1024位，支持中文、英文、数字、常用标点符号 

        :return: The non_scan_reason of this ImageLocalInfo.
        :rtype: str
        """
        return self._non_scan_reason

    @non_scan_reason.setter
    def non_scan_reason(self, non_scan_reason):
        r"""Sets the non_scan_reason of this ImageLocalInfo.

        **参数解释** 说明本地镜像无法进行安全扫描的具体原因（如镜像格式不支持、权限不足等），为空表示支持扫描 **取值范围** 字符长度0-1024位，支持中文、英文、数字、常用标点符号 

        :param non_scan_reason: The non_scan_reason of this ImageLocalInfo.
        :type non_scan_reason: str
        """
        self._non_scan_reason = non_scan_reason

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
        if not isinstance(other, ImageLocalInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
