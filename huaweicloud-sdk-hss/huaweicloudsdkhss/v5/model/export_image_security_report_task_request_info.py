# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportImageSecurityReportTaskRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'export_size': 'int',
        'security_report_type': 'str',
        'image_id_list': 'list[str]',
        'operate_all': 'bool',
        'image_type': 'str',
        'scan_status': 'str',
        'namespace': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'image_id': 'str',
        'latest_version': 'bool',
        'image_size': 'int',
        'start_latest_update_time': 'int',
        'end_latest_update_time': 'int',
        'start_latest_scan_time': 'int',
        'end_latest_scan_time': 'int',
        'has_malicious_file': 'bool',
        'has_vul': 'bool',
        'has_unsafe_setting': 'bool',
        'risky': 'bool',
        'severity_level': 'str',
        'instance_name': 'str',
        'cicd_name': 'str',
        'build_command_risk_level': 'str',
        'build_command_risk_name': 'str',
        'build_command_rule_id_list': 'list[str]'
    }

    attribute_map = {
        'export_size': 'export_size',
        'security_report_type': 'security_report_type',
        'image_id_list': 'image_id_list',
        'operate_all': 'operate_all',
        'image_type': 'image_type',
        'scan_status': 'scan_status',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'image_id': 'image_id',
        'latest_version': 'latest_version',
        'image_size': 'image_size',
        'start_latest_update_time': 'start_latest_update_time',
        'end_latest_update_time': 'end_latest_update_time',
        'start_latest_scan_time': 'start_latest_scan_time',
        'end_latest_scan_time': 'end_latest_scan_time',
        'has_malicious_file': 'has_malicious_file',
        'has_vul': 'has_vul',
        'has_unsafe_setting': 'has_unsafe_setting',
        'risky': 'risky',
        'severity_level': 'severity_level',
        'instance_name': 'instance_name',
        'cicd_name': 'cicd_name',
        'build_command_risk_level': 'build_command_risk_level',
        'build_command_risk_name': 'build_command_risk_name',
        'build_command_rule_id_list': 'build_command_rule_id_list'
    }

    def __init__(self, export_size=None, security_report_type=None, image_id_list=None, operate_all=None, image_type=None, scan_status=None, namespace=None, image_name=None, image_version=None, image_id=None, latest_version=None, image_size=None, start_latest_update_time=None, end_latest_update_time=None, start_latest_scan_time=None, end_latest_scan_time=None, has_malicious_file=None, has_vul=None, has_unsafe_setting=None, risky=None, severity_level=None, instance_name=None, cicd_name=None, build_command_risk_level=None, build_command_risk_name=None, build_command_rule_id_list=None):
        r"""ExportImageSecurityReportTaskRequestInfo

        The model defined in huaweicloud sdk

        :param export_size: 导出数据条数
        :type export_size: int
        :param security_report_type: **参数解释**: 安全报告类型 **约束限制**: 不涉及 **取值范围**: - malwares : 恶意文件信息 - apps : 软件信息 - files : 文件信息 - sensitive-info : 敏感信息 - non-compliant-app : 软件合规信息 - build-command-risks : 镜像构建指令风险 
        :type security_report_type: str
        :param image_id_list: 要导出的镜像id列表。operate_all参数为false时,需要填写此批量查询条件。本地/CICD镜像填写image_id，仓库镜像填写镜像列表返回的id
        :type image_id_list: list[str]
        :param operate_all: 若为true表示查询全量镜像，可传其他参数对全量镜像数据进行筛选
        :type operate_all: bool
        :param image_type: **参数解释**: 镜像类型。导出本地镜像和cicd镜像报告时，需要传参image_type。不传此参数时，默认导出其他仓库镜像数据。 **约束限制**: 不涉及 **取值范围**: - private_image : 私有镜像 - shared_image : 共享镜像 - local_image : 本地镜像 - instance_image : 企业镜像 - harbor : Harbor镜像 - jfrog : Jfrog镜像 - cicd : cicd镜像 
        :type image_type: str
        :param scan_status: 扫描状态，包含如下:   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - download_failed : 下载失败   - image_oversized : 镜像超大
        :type scan_status: str
        :param namespace: 组织名称
        :type namespace: str
        :param image_name: 镜像名称
        :type image_name: str
        :param image_version: 镜像版本
        :type image_version: str
        :param image_id: 镜像id
        :type image_id: str
        :param latest_version: 仅关注最新版本镜像
        :type latest_version: bool
        :param image_size: 镜像大小
        :type image_size: int
        :param start_latest_update_time: 创建时间开始日期，时间单位：毫秒（ms）
        :type start_latest_update_time: int
        :param end_latest_update_time: 创建时间结束日期，时间单位：毫秒（ms）
        :type end_latest_update_time: int
        :param start_latest_scan_time: 最近一次扫描完成时间开始日期，时间单位：毫秒（ms）
        :type start_latest_scan_time: int
        :param end_latest_scan_time: 最近一次扫描完成时间结束日期，时间单位：毫秒（ms）
        :type end_latest_scan_time: int
        :param has_malicious_file: 是否存在恶意文件
        :type has_malicious_file: bool
        :param has_vul: 是否存在软件漏洞
        :type has_vul: bool
        :param has_unsafe_setting: 是否存在基线检查
        :type has_unsafe_setting: bool
        :param risky: 是否有安全风险，包含如下:   - true : 有风险   - false : 无风险
        :type risky: bool
        :param severity_level: 镜像风险程度，在镜像扫描完成后展示，包含如下：   - Security：安全   - Low：低危   - Medium：中危   - High：高危
        :type severity_level: str
        :param instance_name: 企业镜像实例名称
        :type instance_name: str
        :param cicd_name: cicd名称
        :type cicd_name: str
        :param build_command_risk_level: **参数解释**: 构建指令风险程度 **约束限制**: 不涉及 **取值范围**: - critical ：严重 - high ：高危 - medium ：中危 - low ：低危  **默认取值**: 不涉及 
        :type build_command_risk_level: str
        :param build_command_risk_name: 构建指令风险名称
        :type build_command_risk_name: str
        :param build_command_rule_id_list: 要导出的构建指令风险检测规则id列表。rule_id的值可以从接口/v5/{project_id}/image/build-command-risks的返回参数获取
        :type build_command_rule_id_list: list[str]
        """
        
        

        self._export_size = None
        self._security_report_type = None
        self._image_id_list = None
        self._operate_all = None
        self._image_type = None
        self._scan_status = None
        self._namespace = None
        self._image_name = None
        self._image_version = None
        self._image_id = None
        self._latest_version = None
        self._image_size = None
        self._start_latest_update_time = None
        self._end_latest_update_time = None
        self._start_latest_scan_time = None
        self._end_latest_scan_time = None
        self._has_malicious_file = None
        self._has_vul = None
        self._has_unsafe_setting = None
        self._risky = None
        self._severity_level = None
        self._instance_name = None
        self._cicd_name = None
        self._build_command_risk_level = None
        self._build_command_risk_name = None
        self._build_command_rule_id_list = None
        self.discriminator = None

        self.export_size = export_size
        self.security_report_type = security_report_type
        if image_id_list is not None:
            self.image_id_list = image_id_list
        self.operate_all = operate_all
        if image_type is not None:
            self.image_type = image_type
        if scan_status is not None:
            self.scan_status = scan_status
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if image_id is not None:
            self.image_id = image_id
        if latest_version is not None:
            self.latest_version = latest_version
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
        if has_malicious_file is not None:
            self.has_malicious_file = has_malicious_file
        if has_vul is not None:
            self.has_vul = has_vul
        if has_unsafe_setting is not None:
            self.has_unsafe_setting = has_unsafe_setting
        if risky is not None:
            self.risky = risky
        if severity_level is not None:
            self.severity_level = severity_level
        if instance_name is not None:
            self.instance_name = instance_name
        if cicd_name is not None:
            self.cicd_name = cicd_name
        if build_command_risk_level is not None:
            self.build_command_risk_level = build_command_risk_level
        if build_command_risk_name is not None:
            self.build_command_risk_name = build_command_risk_name
        if build_command_rule_id_list is not None:
            self.build_command_rule_id_list = build_command_rule_id_list

    @property
    def export_size(self):
        r"""Gets the export_size of this ExportImageSecurityReportTaskRequestInfo.

        导出数据条数

        :return: The export_size of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: int
        """
        return self._export_size

    @export_size.setter
    def export_size(self, export_size):
        r"""Sets the export_size of this ExportImageSecurityReportTaskRequestInfo.

        导出数据条数

        :param export_size: The export_size of this ExportImageSecurityReportTaskRequestInfo.
        :type export_size: int
        """
        self._export_size = export_size

    @property
    def security_report_type(self):
        r"""Gets the security_report_type of this ExportImageSecurityReportTaskRequestInfo.

        **参数解释**: 安全报告类型 **约束限制**: 不涉及 **取值范围**: - malwares : 恶意文件信息 - apps : 软件信息 - files : 文件信息 - sensitive-info : 敏感信息 - non-compliant-app : 软件合规信息 - build-command-risks : 镜像构建指令风险 

        :return: The security_report_type of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: str
        """
        return self._security_report_type

    @security_report_type.setter
    def security_report_type(self, security_report_type):
        r"""Sets the security_report_type of this ExportImageSecurityReportTaskRequestInfo.

        **参数解释**: 安全报告类型 **约束限制**: 不涉及 **取值范围**: - malwares : 恶意文件信息 - apps : 软件信息 - files : 文件信息 - sensitive-info : 敏感信息 - non-compliant-app : 软件合规信息 - build-command-risks : 镜像构建指令风险 

        :param security_report_type: The security_report_type of this ExportImageSecurityReportTaskRequestInfo.
        :type security_report_type: str
        """
        self._security_report_type = security_report_type

    @property
    def image_id_list(self):
        r"""Gets the image_id_list of this ExportImageSecurityReportTaskRequestInfo.

        要导出的镜像id列表。operate_all参数为false时,需要填写此批量查询条件。本地/CICD镜像填写image_id，仓库镜像填写镜像列表返回的id

        :return: The image_id_list of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: list[str]
        """
        return self._image_id_list

    @image_id_list.setter
    def image_id_list(self, image_id_list):
        r"""Sets the image_id_list of this ExportImageSecurityReportTaskRequestInfo.

        要导出的镜像id列表。operate_all参数为false时,需要填写此批量查询条件。本地/CICD镜像填写image_id，仓库镜像填写镜像列表返回的id

        :param image_id_list: The image_id_list of this ExportImageSecurityReportTaskRequestInfo.
        :type image_id_list: list[str]
        """
        self._image_id_list = image_id_list

    @property
    def operate_all(self):
        r"""Gets the operate_all of this ExportImageSecurityReportTaskRequestInfo.

        若为true表示查询全量镜像，可传其他参数对全量镜像数据进行筛选

        :return: The operate_all of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: bool
        """
        return self._operate_all

    @operate_all.setter
    def operate_all(self, operate_all):
        r"""Sets the operate_all of this ExportImageSecurityReportTaskRequestInfo.

        若为true表示查询全量镜像，可传其他参数对全量镜像数据进行筛选

        :param operate_all: The operate_all of this ExportImageSecurityReportTaskRequestInfo.
        :type operate_all: bool
        """
        self._operate_all = operate_all

    @property
    def image_type(self):
        r"""Gets the image_type of this ExportImageSecurityReportTaskRequestInfo.

        **参数解释**: 镜像类型。导出本地镜像和cicd镜像报告时，需要传参image_type。不传此参数时，默认导出其他仓库镜像数据。 **约束限制**: 不涉及 **取值范围**: - private_image : 私有镜像 - shared_image : 共享镜像 - local_image : 本地镜像 - instance_image : 企业镜像 - harbor : Harbor镜像 - jfrog : Jfrog镜像 - cicd : cicd镜像 

        :return: The image_type of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ExportImageSecurityReportTaskRequestInfo.

        **参数解释**: 镜像类型。导出本地镜像和cicd镜像报告时，需要传参image_type。不传此参数时，默认导出其他仓库镜像数据。 **约束限制**: 不涉及 **取值范围**: - private_image : 私有镜像 - shared_image : 共享镜像 - local_image : 本地镜像 - instance_image : 企业镜像 - harbor : Harbor镜像 - jfrog : Jfrog镜像 - cicd : cicd镜像 

        :param image_type: The image_type of this ExportImageSecurityReportTaskRequestInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def scan_status(self):
        r"""Gets the scan_status of this ExportImageSecurityReportTaskRequestInfo.

        扫描状态，包含如下:   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - download_failed : 下载失败   - image_oversized : 镜像超大

        :return: The scan_status of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this ExportImageSecurityReportTaskRequestInfo.

        扫描状态，包含如下:   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - download_failed : 下载失败   - image_oversized : 镜像超大

        :param scan_status: The scan_status of this ExportImageSecurityReportTaskRequestInfo.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def namespace(self):
        r"""Gets the namespace of this ExportImageSecurityReportTaskRequestInfo.

        组织名称

        :return: The namespace of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ExportImageSecurityReportTaskRequestInfo.

        组织名称

        :param namespace: The namespace of this ExportImageSecurityReportTaskRequestInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        r"""Gets the image_name of this ExportImageSecurityReportTaskRequestInfo.

        镜像名称

        :return: The image_name of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ExportImageSecurityReportTaskRequestInfo.

        镜像名称

        :param image_name: The image_name of this ExportImageSecurityReportTaskRequestInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ExportImageSecurityReportTaskRequestInfo.

        镜像版本

        :return: The image_version of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ExportImageSecurityReportTaskRequestInfo.

        镜像版本

        :param image_version: The image_version of this ExportImageSecurityReportTaskRequestInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_id(self):
        r"""Gets the image_id of this ExportImageSecurityReportTaskRequestInfo.

        镜像id

        :return: The image_id of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ExportImageSecurityReportTaskRequestInfo.

        镜像id

        :param image_id: The image_id of this ExportImageSecurityReportTaskRequestInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def latest_version(self):
        r"""Gets the latest_version of this ExportImageSecurityReportTaskRequestInfo.

        仅关注最新版本镜像

        :return: The latest_version of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: bool
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this ExportImageSecurityReportTaskRequestInfo.

        仅关注最新版本镜像

        :param latest_version: The latest_version of this ExportImageSecurityReportTaskRequestInfo.
        :type latest_version: bool
        """
        self._latest_version = latest_version

    @property
    def image_size(self):
        r"""Gets the image_size of this ExportImageSecurityReportTaskRequestInfo.

        镜像大小

        :return: The image_size of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this ExportImageSecurityReportTaskRequestInfo.

        镜像大小

        :param image_size: The image_size of this ExportImageSecurityReportTaskRequestInfo.
        :type image_size: int
        """
        self._image_size = image_size

    @property
    def start_latest_update_time(self):
        r"""Gets the start_latest_update_time of this ExportImageSecurityReportTaskRequestInfo.

        创建时间开始日期，时间单位：毫秒（ms）

        :return: The start_latest_update_time of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: int
        """
        return self._start_latest_update_time

    @start_latest_update_time.setter
    def start_latest_update_time(self, start_latest_update_time):
        r"""Sets the start_latest_update_time of this ExportImageSecurityReportTaskRequestInfo.

        创建时间开始日期，时间单位：毫秒（ms）

        :param start_latest_update_time: The start_latest_update_time of this ExportImageSecurityReportTaskRequestInfo.
        :type start_latest_update_time: int
        """
        self._start_latest_update_time = start_latest_update_time

    @property
    def end_latest_update_time(self):
        r"""Gets the end_latest_update_time of this ExportImageSecurityReportTaskRequestInfo.

        创建时间结束日期，时间单位：毫秒（ms）

        :return: The end_latest_update_time of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: int
        """
        return self._end_latest_update_time

    @end_latest_update_time.setter
    def end_latest_update_time(self, end_latest_update_time):
        r"""Sets the end_latest_update_time of this ExportImageSecurityReportTaskRequestInfo.

        创建时间结束日期，时间单位：毫秒（ms）

        :param end_latest_update_time: The end_latest_update_time of this ExportImageSecurityReportTaskRequestInfo.
        :type end_latest_update_time: int
        """
        self._end_latest_update_time = end_latest_update_time

    @property
    def start_latest_scan_time(self):
        r"""Gets the start_latest_scan_time of this ExportImageSecurityReportTaskRequestInfo.

        最近一次扫描完成时间开始日期，时间单位：毫秒（ms）

        :return: The start_latest_scan_time of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: int
        """
        return self._start_latest_scan_time

    @start_latest_scan_time.setter
    def start_latest_scan_time(self, start_latest_scan_time):
        r"""Sets the start_latest_scan_time of this ExportImageSecurityReportTaskRequestInfo.

        最近一次扫描完成时间开始日期，时间单位：毫秒（ms）

        :param start_latest_scan_time: The start_latest_scan_time of this ExportImageSecurityReportTaskRequestInfo.
        :type start_latest_scan_time: int
        """
        self._start_latest_scan_time = start_latest_scan_time

    @property
    def end_latest_scan_time(self):
        r"""Gets the end_latest_scan_time of this ExportImageSecurityReportTaskRequestInfo.

        最近一次扫描完成时间结束日期，时间单位：毫秒（ms）

        :return: The end_latest_scan_time of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: int
        """
        return self._end_latest_scan_time

    @end_latest_scan_time.setter
    def end_latest_scan_time(self, end_latest_scan_time):
        r"""Sets the end_latest_scan_time of this ExportImageSecurityReportTaskRequestInfo.

        最近一次扫描完成时间结束日期，时间单位：毫秒（ms）

        :param end_latest_scan_time: The end_latest_scan_time of this ExportImageSecurityReportTaskRequestInfo.
        :type end_latest_scan_time: int
        """
        self._end_latest_scan_time = end_latest_scan_time

    @property
    def has_malicious_file(self):
        r"""Gets the has_malicious_file of this ExportImageSecurityReportTaskRequestInfo.

        是否存在恶意文件

        :return: The has_malicious_file of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: bool
        """
        return self._has_malicious_file

    @has_malicious_file.setter
    def has_malicious_file(self, has_malicious_file):
        r"""Sets the has_malicious_file of this ExportImageSecurityReportTaskRequestInfo.

        是否存在恶意文件

        :param has_malicious_file: The has_malicious_file of this ExportImageSecurityReportTaskRequestInfo.
        :type has_malicious_file: bool
        """
        self._has_malicious_file = has_malicious_file

    @property
    def has_vul(self):
        r"""Gets the has_vul of this ExportImageSecurityReportTaskRequestInfo.

        是否存在软件漏洞

        :return: The has_vul of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: bool
        """
        return self._has_vul

    @has_vul.setter
    def has_vul(self, has_vul):
        r"""Sets the has_vul of this ExportImageSecurityReportTaskRequestInfo.

        是否存在软件漏洞

        :param has_vul: The has_vul of this ExportImageSecurityReportTaskRequestInfo.
        :type has_vul: bool
        """
        self._has_vul = has_vul

    @property
    def has_unsafe_setting(self):
        r"""Gets the has_unsafe_setting of this ExportImageSecurityReportTaskRequestInfo.

        是否存在基线检查

        :return: The has_unsafe_setting of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: bool
        """
        return self._has_unsafe_setting

    @has_unsafe_setting.setter
    def has_unsafe_setting(self, has_unsafe_setting):
        r"""Sets the has_unsafe_setting of this ExportImageSecurityReportTaskRequestInfo.

        是否存在基线检查

        :param has_unsafe_setting: The has_unsafe_setting of this ExportImageSecurityReportTaskRequestInfo.
        :type has_unsafe_setting: bool
        """
        self._has_unsafe_setting = has_unsafe_setting

    @property
    def risky(self):
        r"""Gets the risky of this ExportImageSecurityReportTaskRequestInfo.

        是否有安全风险，包含如下:   - true : 有风险   - false : 无风险

        :return: The risky of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: bool
        """
        return self._risky

    @risky.setter
    def risky(self, risky):
        r"""Sets the risky of this ExportImageSecurityReportTaskRequestInfo.

        是否有安全风险，包含如下:   - true : 有风险   - false : 无风险

        :param risky: The risky of this ExportImageSecurityReportTaskRequestInfo.
        :type risky: bool
        """
        self._risky = risky

    @property
    def severity_level(self):
        r"""Gets the severity_level of this ExportImageSecurityReportTaskRequestInfo.

        镜像风险程度，在镜像扫描完成后展示，包含如下：   - Security：安全   - Low：低危   - Medium：中危   - High：高危

        :return: The severity_level of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this ExportImageSecurityReportTaskRequestInfo.

        镜像风险程度，在镜像扫描完成后展示，包含如下：   - Security：安全   - Low：低危   - Medium：中危   - High：高危

        :param severity_level: The severity_level of this ExportImageSecurityReportTaskRequestInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ExportImageSecurityReportTaskRequestInfo.

        企业镜像实例名称

        :return: The instance_name of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ExportImageSecurityReportTaskRequestInfo.

        企业镜像实例名称

        :param instance_name: The instance_name of this ExportImageSecurityReportTaskRequestInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def cicd_name(self):
        r"""Gets the cicd_name of this ExportImageSecurityReportTaskRequestInfo.

        cicd名称

        :return: The cicd_name of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: str
        """
        return self._cicd_name

    @cicd_name.setter
    def cicd_name(self, cicd_name):
        r"""Sets the cicd_name of this ExportImageSecurityReportTaskRequestInfo.

        cicd名称

        :param cicd_name: The cicd_name of this ExportImageSecurityReportTaskRequestInfo.
        :type cicd_name: str
        """
        self._cicd_name = cicd_name

    @property
    def build_command_risk_level(self):
        r"""Gets the build_command_risk_level of this ExportImageSecurityReportTaskRequestInfo.

        **参数解释**: 构建指令风险程度 **约束限制**: 不涉及 **取值范围**: - critical ：严重 - high ：高危 - medium ：中危 - low ：低危  **默认取值**: 不涉及 

        :return: The build_command_risk_level of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: str
        """
        return self._build_command_risk_level

    @build_command_risk_level.setter
    def build_command_risk_level(self, build_command_risk_level):
        r"""Sets the build_command_risk_level of this ExportImageSecurityReportTaskRequestInfo.

        **参数解释**: 构建指令风险程度 **约束限制**: 不涉及 **取值范围**: - critical ：严重 - high ：高危 - medium ：中危 - low ：低危  **默认取值**: 不涉及 

        :param build_command_risk_level: The build_command_risk_level of this ExportImageSecurityReportTaskRequestInfo.
        :type build_command_risk_level: str
        """
        self._build_command_risk_level = build_command_risk_level

    @property
    def build_command_risk_name(self):
        r"""Gets the build_command_risk_name of this ExportImageSecurityReportTaskRequestInfo.

        构建指令风险名称

        :return: The build_command_risk_name of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: str
        """
        return self._build_command_risk_name

    @build_command_risk_name.setter
    def build_command_risk_name(self, build_command_risk_name):
        r"""Sets the build_command_risk_name of this ExportImageSecurityReportTaskRequestInfo.

        构建指令风险名称

        :param build_command_risk_name: The build_command_risk_name of this ExportImageSecurityReportTaskRequestInfo.
        :type build_command_risk_name: str
        """
        self._build_command_risk_name = build_command_risk_name

    @property
    def build_command_rule_id_list(self):
        r"""Gets the build_command_rule_id_list of this ExportImageSecurityReportTaskRequestInfo.

        要导出的构建指令风险检测规则id列表。rule_id的值可以从接口/v5/{project_id}/image/build-command-risks的返回参数获取

        :return: The build_command_rule_id_list of this ExportImageSecurityReportTaskRequestInfo.
        :rtype: list[str]
        """
        return self._build_command_rule_id_list

    @build_command_rule_id_list.setter
    def build_command_rule_id_list(self, build_command_rule_id_list):
        r"""Sets the build_command_rule_id_list of this ExportImageSecurityReportTaskRequestInfo.

        要导出的构建指令风险检测规则id列表。rule_id的值可以从接口/v5/{project_id}/image/build-command-risks的返回参数获取

        :param build_command_rule_id_list: The build_command_rule_id_list of this ExportImageSecurityReportTaskRequestInfo.
        :type build_command_rule_id_list: list[str]
        """
        self._build_command_rule_id_list = build_command_rule_id_list

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
        if not isinstance(other, ExportImageSecurityReportTaskRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
