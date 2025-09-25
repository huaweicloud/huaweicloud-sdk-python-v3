# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCicdImagesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'namespace': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'limit': 'int',
        'offset': 'int',
        'image_id': 'str',
        'cicd_name': 'str',
        'latest_version': 'bool',
        'image_size': 'int',
        'scan_status': 'str',
        'start_latest_update_time': 'int',
        'end_latest_update_time': 'int',
        'start_latest_scan_time': 'int',
        'end_latest_scan_time': 'int',
        'has_malicious_file': 'bool',
        'has_unsafe_setting': 'bool',
        'has_vul': 'bool',
        'severity_level': 'str',
        'risky': 'bool'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'limit': 'limit',
        'offset': 'offset',
        'image_id': 'image_id',
        'cicd_name': 'cicd_name',
        'latest_version': 'latest_version',
        'image_size': 'image_size',
        'scan_status': 'scan_status',
        'start_latest_update_time': 'start_latest_update_time',
        'end_latest_update_time': 'end_latest_update_time',
        'start_latest_scan_time': 'start_latest_scan_time',
        'end_latest_scan_time': 'end_latest_scan_time',
        'has_malicious_file': 'has_malicious_file',
        'has_unsafe_setting': 'has_unsafe_setting',
        'has_vul': 'has_vul',
        'severity_level': 'severity_level',
        'risky': 'risky'
    }

    def __init__(self, enterprise_project_id=None, namespace=None, image_name=None, image_version=None, sort_key=None, sort_dir=None, limit=None, offset=None, image_id=None, cicd_name=None, latest_version=None, image_size=None, scan_status=None, start_latest_update_time=None, end_latest_update_time=None, start_latest_scan_time=None, end_latest_scan_time=None, has_malicious_file=None, has_unsafe_setting=None, has_vul=None, severity_level=None, risky=None):
        r"""ListCicdImagesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param namespace: **参数解释**: 组织名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位。  **默认取值**: 不涉及 
        :type namespace: str
        :param image_name: **参数解释**: 镜像名称 **取值范围**: 字符长度1-128位 
        :type image_name: str
        :param image_version: **参数解释**: 镜像版本 **取值范围**: 字符长度1-64位 
        :type image_version: str
        :param sort_key: **参数解释**: 可排序字段 **约束限制**: 不涉及 **取值范围**: - latest_scan_time：最近扫描时间。  **默认取值**: 不涉及 
        :type sort_key: str
        :param sort_dir: **参数解释**: 排序的顺序 **约束限制**: 不涉及 **取值范围**:   - asc  : 正序   - desc : 倒序  **默认取值**: 正序排序 
        :type sort_dir: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param image_id: **参数解释**: cicd镜像标识 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type image_id: str
        :param cicd_name: **参数解释**: cicd名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type cicd_name: str
        :param latest_version: **参数解释**: 仅关注最新版本镜像 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 
        :type latest_version: bool
        :param image_size: **参数解释**: 镜像大小 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2147483547 **默认取值**: 不涉及 
        :type image_size: int
        :param scan_status: **参数解释** 扫描状态 **约束限制** 不涉及 **取值范围** - unscan : 未扫描。 - success : 扫描完成。 - scanning : 扫描中 - failed : 扫描失败。 - waiting_for_scan : 等待扫描。  **默认取值**: 不涉及 
        :type scan_status: str
        :param start_latest_update_time: **参数解释**: 创建时间开始日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 
        :type start_latest_update_time: int
        :param end_latest_update_time: **参数解释**: 创建时间结束日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 
        :type end_latest_update_time: int
        :param start_latest_scan_time: **参数解释**: 最近一次扫描完成时间开始日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 
        :type start_latest_scan_time: int
        :param end_latest_scan_time: **参数解释**: 最近一次扫描完成时间结束日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 
        :type end_latest_scan_time: int
        :param has_malicious_file: **参数解释**: 是否存在恶意文件 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 
        :type has_malicious_file: bool
        :param has_unsafe_setting: **参数解释**: 是否存在基线检查 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 
        :type has_unsafe_setting: bool
        :param has_vul: **参数解释**: 是否存在软件漏洞 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 
        :type has_vul: bool
        :param severity_level: **参数解释** 镜像风险程度，在镜像扫描完成后展示 **约束限制** 不涉及 **取值范围** - Security : 安全。 - Low : 低危。 - Medium : 中危 - High : 高危。  **默认取值**: 不涉及 
        :type severity_level: str
        :param risky: **参数解释**: 有安全风险 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 
        :type risky: bool
        """
        
        

        self._enterprise_project_id = None
        self._namespace = None
        self._image_name = None
        self._image_version = None
        self._sort_key = None
        self._sort_dir = None
        self._limit = None
        self._offset = None
        self._image_id = None
        self._cicd_name = None
        self._latest_version = None
        self._image_size = None
        self._scan_status = None
        self._start_latest_update_time = None
        self._end_latest_update_time = None
        self._start_latest_scan_time = None
        self._end_latest_scan_time = None
        self._has_malicious_file = None
        self._has_unsafe_setting = None
        self._has_vul = None
        self._severity_level = None
        self._risky = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if image_id is not None:
            self.image_id = image_id
        if cicd_name is not None:
            self.cicd_name = cicd_name
        if latest_version is not None:
            self.latest_version = latest_version
        if image_size is not None:
            self.image_size = image_size
        if scan_status is not None:
            self.scan_status = scan_status
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
        if has_unsafe_setting is not None:
            self.has_unsafe_setting = has_unsafe_setting
        if has_vul is not None:
            self.has_vul = has_vul
        if severity_level is not None:
            self.severity_level = severity_level
        if risky is not None:
            self.risky = risky

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListCicdImagesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListCicdImagesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListCicdImagesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListCicdImagesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def namespace(self):
        r"""Gets the namespace of this ListCicdImagesRequest.

        **参数解释**: 组织名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位。  **默认取值**: 不涉及 

        :return: The namespace of this ListCicdImagesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListCicdImagesRequest.

        **参数解释**: 组织名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位。  **默认取值**: 不涉及 

        :param namespace: The namespace of this ListCicdImagesRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        r"""Gets the image_name of this ListCicdImagesRequest.

        **参数解释**: 镜像名称 **取值范围**: 字符长度1-128位 

        :return: The image_name of this ListCicdImagesRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListCicdImagesRequest.

        **参数解释**: 镜像名称 **取值范围**: 字符长度1-128位 

        :param image_name: The image_name of this ListCicdImagesRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ListCicdImagesRequest.

        **参数解释**: 镜像版本 **取值范围**: 字符长度1-64位 

        :return: The image_version of this ListCicdImagesRequest.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ListCicdImagesRequest.

        **参数解释**: 镜像版本 **取值范围**: 字符长度1-64位 

        :param image_version: The image_version of this ListCicdImagesRequest.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListCicdImagesRequest.

        **参数解释**: 可排序字段 **约束限制**: 不涉及 **取值范围**: - latest_scan_time：最近扫描时间。  **默认取值**: 不涉及 

        :return: The sort_key of this ListCicdImagesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListCicdImagesRequest.

        **参数解释**: 可排序字段 **约束限制**: 不涉及 **取值范围**: - latest_scan_time：最近扫描时间。  **默认取值**: 不涉及 

        :param sort_key: The sort_key of this ListCicdImagesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListCicdImagesRequest.

        **参数解释**: 排序的顺序 **约束限制**: 不涉及 **取值范围**:   - asc  : 正序   - desc : 倒序  **默认取值**: 正序排序 

        :return: The sort_dir of this ListCicdImagesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListCicdImagesRequest.

        **参数解释**: 排序的顺序 **约束限制**: 不涉及 **取值范围**:   - asc  : 正序   - desc : 倒序  **默认取值**: 正序排序 

        :param sort_dir: The sort_dir of this ListCicdImagesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def limit(self):
        r"""Gets the limit of this ListCicdImagesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListCicdImagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCicdImagesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListCicdImagesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListCicdImagesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListCicdImagesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCicdImagesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListCicdImagesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def image_id(self):
        r"""Gets the image_id of this ListCicdImagesRequest.

        **参数解释**: cicd镜像标识 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The image_id of this ListCicdImagesRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListCicdImagesRequest.

        **参数解释**: cicd镜像标识 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param image_id: The image_id of this ListCicdImagesRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def cicd_name(self):
        r"""Gets the cicd_name of this ListCicdImagesRequest.

        **参数解释**: cicd名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The cicd_name of this ListCicdImagesRequest.
        :rtype: str
        """
        return self._cicd_name

    @cicd_name.setter
    def cicd_name(self, cicd_name):
        r"""Sets the cicd_name of this ListCicdImagesRequest.

        **参数解释**: cicd名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param cicd_name: The cicd_name of this ListCicdImagesRequest.
        :type cicd_name: str
        """
        self._cicd_name = cicd_name

    @property
    def latest_version(self):
        r"""Gets the latest_version of this ListCicdImagesRequest.

        **参数解释**: 仅关注最新版本镜像 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 

        :return: The latest_version of this ListCicdImagesRequest.
        :rtype: bool
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this ListCicdImagesRequest.

        **参数解释**: 仅关注最新版本镜像 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 

        :param latest_version: The latest_version of this ListCicdImagesRequest.
        :type latest_version: bool
        """
        self._latest_version = latest_version

    @property
    def image_size(self):
        r"""Gets the image_size of this ListCicdImagesRequest.

        **参数解释**: 镜像大小 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2147483547 **默认取值**: 不涉及 

        :return: The image_size of this ListCicdImagesRequest.
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this ListCicdImagesRequest.

        **参数解释**: 镜像大小 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2147483547 **默认取值**: 不涉及 

        :param image_size: The image_size of this ListCicdImagesRequest.
        :type image_size: int
        """
        self._image_size = image_size

    @property
    def scan_status(self):
        r"""Gets the scan_status of this ListCicdImagesRequest.

        **参数解释** 扫描状态 **约束限制** 不涉及 **取值范围** - unscan : 未扫描。 - success : 扫描完成。 - scanning : 扫描中 - failed : 扫描失败。 - waiting_for_scan : 等待扫描。  **默认取值**: 不涉及 

        :return: The scan_status of this ListCicdImagesRequest.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this ListCicdImagesRequest.

        **参数解释** 扫描状态 **约束限制** 不涉及 **取值范围** - unscan : 未扫描。 - success : 扫描完成。 - scanning : 扫描中 - failed : 扫描失败。 - waiting_for_scan : 等待扫描。  **默认取值**: 不涉及 

        :param scan_status: The scan_status of this ListCicdImagesRequest.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def start_latest_update_time(self):
        r"""Gets the start_latest_update_time of this ListCicdImagesRequest.

        **参数解释**: 创建时间开始日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :return: The start_latest_update_time of this ListCicdImagesRequest.
        :rtype: int
        """
        return self._start_latest_update_time

    @start_latest_update_time.setter
    def start_latest_update_time(self, start_latest_update_time):
        r"""Sets the start_latest_update_time of this ListCicdImagesRequest.

        **参数解释**: 创建时间开始日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :param start_latest_update_time: The start_latest_update_time of this ListCicdImagesRequest.
        :type start_latest_update_time: int
        """
        self._start_latest_update_time = start_latest_update_time

    @property
    def end_latest_update_time(self):
        r"""Gets the end_latest_update_time of this ListCicdImagesRequest.

        **参数解释**: 创建时间结束日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :return: The end_latest_update_time of this ListCicdImagesRequest.
        :rtype: int
        """
        return self._end_latest_update_time

    @end_latest_update_time.setter
    def end_latest_update_time(self, end_latest_update_time):
        r"""Sets the end_latest_update_time of this ListCicdImagesRequest.

        **参数解释**: 创建时间结束日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :param end_latest_update_time: The end_latest_update_time of this ListCicdImagesRequest.
        :type end_latest_update_time: int
        """
        self._end_latest_update_time = end_latest_update_time

    @property
    def start_latest_scan_time(self):
        r"""Gets the start_latest_scan_time of this ListCicdImagesRequest.

        **参数解释**: 最近一次扫描完成时间开始日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :return: The start_latest_scan_time of this ListCicdImagesRequest.
        :rtype: int
        """
        return self._start_latest_scan_time

    @start_latest_scan_time.setter
    def start_latest_scan_time(self, start_latest_scan_time):
        r"""Sets the start_latest_scan_time of this ListCicdImagesRequest.

        **参数解释**: 最近一次扫描完成时间开始日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :param start_latest_scan_time: The start_latest_scan_time of this ListCicdImagesRequest.
        :type start_latest_scan_time: int
        """
        self._start_latest_scan_time = start_latest_scan_time

    @property
    def end_latest_scan_time(self):
        r"""Gets the end_latest_scan_time of this ListCicdImagesRequest.

        **参数解释**: 最近一次扫描完成时间结束日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :return: The end_latest_scan_time of this ListCicdImagesRequest.
        :rtype: int
        """
        return self._end_latest_scan_time

    @end_latest_scan_time.setter
    def end_latest_scan_time(self, end_latest_scan_time):
        r"""Sets the end_latest_scan_time of this ListCicdImagesRequest.

        **参数解释**: 最近一次扫描完成时间结束日期，时间单位 毫秒（ms） **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :param end_latest_scan_time: The end_latest_scan_time of this ListCicdImagesRequest.
        :type end_latest_scan_time: int
        """
        self._end_latest_scan_time = end_latest_scan_time

    @property
    def has_malicious_file(self):
        r"""Gets the has_malicious_file of this ListCicdImagesRequest.

        **参数解释**: 是否存在恶意文件 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 

        :return: The has_malicious_file of this ListCicdImagesRequest.
        :rtype: bool
        """
        return self._has_malicious_file

    @has_malicious_file.setter
    def has_malicious_file(self, has_malicious_file):
        r"""Sets the has_malicious_file of this ListCicdImagesRequest.

        **参数解释**: 是否存在恶意文件 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 

        :param has_malicious_file: The has_malicious_file of this ListCicdImagesRequest.
        :type has_malicious_file: bool
        """
        self._has_malicious_file = has_malicious_file

    @property
    def has_unsafe_setting(self):
        r"""Gets the has_unsafe_setting of this ListCicdImagesRequest.

        **参数解释**: 是否存在基线检查 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 

        :return: The has_unsafe_setting of this ListCicdImagesRequest.
        :rtype: bool
        """
        return self._has_unsafe_setting

    @has_unsafe_setting.setter
    def has_unsafe_setting(self, has_unsafe_setting):
        r"""Sets the has_unsafe_setting of this ListCicdImagesRequest.

        **参数解释**: 是否存在基线检查 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 

        :param has_unsafe_setting: The has_unsafe_setting of this ListCicdImagesRequest.
        :type has_unsafe_setting: bool
        """
        self._has_unsafe_setting = has_unsafe_setting

    @property
    def has_vul(self):
        r"""Gets the has_vul of this ListCicdImagesRequest.

        **参数解释**: 是否存在软件漏洞 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 

        :return: The has_vul of this ListCicdImagesRequest.
        :rtype: bool
        """
        return self._has_vul

    @has_vul.setter
    def has_vul(self, has_vul):
        r"""Sets the has_vul of this ListCicdImagesRequest.

        **参数解释**: 是否存在软件漏洞 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 

        :param has_vul: The has_vul of this ListCicdImagesRequest.
        :type has_vul: bool
        """
        self._has_vul = has_vul

    @property
    def severity_level(self):
        r"""Gets the severity_level of this ListCicdImagesRequest.

        **参数解释** 镜像风险程度，在镜像扫描完成后展示 **约束限制** 不涉及 **取值范围** - Security : 安全。 - Low : 低危。 - Medium : 中危 - High : 高危。  **默认取值**: 不涉及 

        :return: The severity_level of this ListCicdImagesRequest.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this ListCicdImagesRequest.

        **参数解释** 镜像风险程度，在镜像扫描完成后展示 **约束限制** 不涉及 **取值范围** - Security : 安全。 - Low : 低危。 - Medium : 中危 - High : 高危。  **默认取值**: 不涉及 

        :param severity_level: The severity_level of this ListCicdImagesRequest.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def risky(self):
        r"""Gets the risky of this ListCicdImagesRequest.

        **参数解释**: 有安全风险 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 

        :return: The risky of this ListCicdImagesRequest.
        :rtype: bool
        """
        return self._risky

    @risky.setter
    def risky(self, risky):
        r"""Sets the risky of this ListCicdImagesRequest.

        **参数解释**: 有安全风险 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 

        :param risky: The risky of this ListCicdImagesRequest.
        :type risky: bool
        """
        self._risky = risky

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
        if not isinstance(other, ListCicdImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
