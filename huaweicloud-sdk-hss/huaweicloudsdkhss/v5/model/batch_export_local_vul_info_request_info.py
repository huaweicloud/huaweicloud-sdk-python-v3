# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchExportLocalVulInfoRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id_list': 'list[str]',
        'operate_all': 'bool',
        'vul_type': 'str',
        'handle_status': 'str',
        'scan_status': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'image_size': 'int',
        'start_latest_update_time': 'int',
        'end_latest_update_time': 'int',
        'start_latest_scan_time': 'int',
        'end_latest_scan_time': 'int',
        'has_container': 'bool',
        'vul_id_list': 'list[str]'
    }

    attribute_map = {
        'image_id_list': 'image_id_list',
        'operate_all': 'operate_all',
        'vul_type': 'vul_type',
        'handle_status': 'handle_status',
        'scan_status': 'scan_status',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'image_size': 'image_size',
        'start_latest_update_time': 'start_latest_update_time',
        'end_latest_update_time': 'end_latest_update_time',
        'start_latest_scan_time': 'start_latest_scan_time',
        'end_latest_scan_time': 'end_latest_scan_time',
        'has_container': 'has_container',
        'vul_id_list': 'vul_id_list'
    }

    def __init__(self, image_id_list=None, operate_all=None, vul_type=None, handle_status=None, scan_status=None, image_name=None, image_version=None, image_size=None, start_latest_update_time=None, end_latest_update_time=None, start_latest_scan_time=None, end_latest_scan_time=None, has_container=None, vul_id_list=None):
        r"""BatchExportLocalVulInfoRequestInfo

        The model defined in huaweicloud sdk

        :param image_id_list: 要导出的镜像信息列表，operate_all参数为false时需要填写批量查询条件,image_id 镜像id，唯一镜像标识（注：对私有镜像和共享镜像来说是镜像列表返回的id）
        :type image_id_list: list[str]
        :param operate_all: 若为true全量查询，可筛选条件全部查询
        :type operate_all: bool
        :param vul_type: 漏洞类型，包含如下：   -linux_vul : linux漏洞   -app_vul : 应用漏洞
        :type vul_type: str
        :param handle_status: 漏洞处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理
        :type handle_status: str
        :param scan_status: **参数解释**: 扫描状态 **约束限制**: 不涉及 **取值范围**:   - unscan : 未扫描。   - success : 扫描完成。   - scanning : 扫描中。   - failed : 扫描失败。   - download_failed : 下载失败。   - image_oversized : 镜像超大。   - waiting_for_scan : 等待扫描。   - image_scan_stop : 扫描终止。 **默认取值**: 不涉及 
        :type scan_status: str
        :param image_name: 镜像名称
        :type image_name: str
        :param image_version: 镜像版本
        :type image_version: str
        :param image_size: 镜像大小
        :type image_size: int
        :param start_latest_update_time: 创建时间开始日期，时间单位 毫秒（ms）
        :type start_latest_update_time: int
        :param end_latest_update_time: 创建时间结束日期，时间单位 毫秒（ms）
        :type end_latest_update_time: int
        :param start_latest_scan_time: 最近一次扫描完成时间开始日期，时间单位 毫秒（ms）
        :type start_latest_scan_time: int
        :param end_latest_scan_time: 最近一次扫描完成时间结束日期，时间单位 毫秒（ms）
        :type end_latest_scan_time: int
        :param has_container: **参数解释**: 是否存在容器 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 
        :type has_container: bool
        :param vul_id_list: 导出镜像漏洞时的漏洞id列表
        :type vul_id_list: list[str]
        """
        
        

        self._image_id_list = None
        self._operate_all = None
        self._vul_type = None
        self._handle_status = None
        self._scan_status = None
        self._image_name = None
        self._image_version = None
        self._image_size = None
        self._start_latest_update_time = None
        self._end_latest_update_time = None
        self._start_latest_scan_time = None
        self._end_latest_scan_time = None
        self._has_container = None
        self._vul_id_list = None
        self.discriminator = None

        if image_id_list is not None:
            self.image_id_list = image_id_list
        if operate_all is not None:
            self.operate_all = operate_all
        if vul_type is not None:
            self.vul_type = vul_type
        if handle_status is not None:
            self.handle_status = handle_status
        if scan_status is not None:
            self.scan_status = scan_status
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
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
        if has_container is not None:
            self.has_container = has_container
        if vul_id_list is not None:
            self.vul_id_list = vul_id_list

    @property
    def image_id_list(self):
        r"""Gets the image_id_list of this BatchExportLocalVulInfoRequestInfo.

        要导出的镜像信息列表，operate_all参数为false时需要填写批量查询条件,image_id 镜像id，唯一镜像标识（注：对私有镜像和共享镜像来说是镜像列表返回的id）

        :return: The image_id_list of this BatchExportLocalVulInfoRequestInfo.
        :rtype: list[str]
        """
        return self._image_id_list

    @image_id_list.setter
    def image_id_list(self, image_id_list):
        r"""Sets the image_id_list of this BatchExportLocalVulInfoRequestInfo.

        要导出的镜像信息列表，operate_all参数为false时需要填写批量查询条件,image_id 镜像id，唯一镜像标识（注：对私有镜像和共享镜像来说是镜像列表返回的id）

        :param image_id_list: The image_id_list of this BatchExportLocalVulInfoRequestInfo.
        :type image_id_list: list[str]
        """
        self._image_id_list = image_id_list

    @property
    def operate_all(self):
        r"""Gets the operate_all of this BatchExportLocalVulInfoRequestInfo.

        若为true全量查询，可筛选条件全部查询

        :return: The operate_all of this BatchExportLocalVulInfoRequestInfo.
        :rtype: bool
        """
        return self._operate_all

    @operate_all.setter
    def operate_all(self, operate_all):
        r"""Sets the operate_all of this BatchExportLocalVulInfoRequestInfo.

        若为true全量查询，可筛选条件全部查询

        :param operate_all: The operate_all of this BatchExportLocalVulInfoRequestInfo.
        :type operate_all: bool
        """
        self._operate_all = operate_all

    @property
    def vul_type(self):
        r"""Gets the vul_type of this BatchExportLocalVulInfoRequestInfo.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -app_vul : 应用漏洞

        :return: The vul_type of this BatchExportLocalVulInfoRequestInfo.
        :rtype: str
        """
        return self._vul_type

    @vul_type.setter
    def vul_type(self, vul_type):
        r"""Sets the vul_type of this BatchExportLocalVulInfoRequestInfo.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -app_vul : 应用漏洞

        :param vul_type: The vul_type of this BatchExportLocalVulInfoRequestInfo.
        :type vul_type: str
        """
        self._vul_type = vul_type

    @property
    def handle_status(self):
        r"""Gets the handle_status of this BatchExportLocalVulInfoRequestInfo.

        漏洞处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :return: The handle_status of this BatchExportLocalVulInfoRequestInfo.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this BatchExportLocalVulInfoRequestInfo.

        漏洞处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :param handle_status: The handle_status of this BatchExportLocalVulInfoRequestInfo.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def scan_status(self):
        r"""Gets the scan_status of this BatchExportLocalVulInfoRequestInfo.

        **参数解释**: 扫描状态 **约束限制**: 不涉及 **取值范围**:   - unscan : 未扫描。   - success : 扫描完成。   - scanning : 扫描中。   - failed : 扫描失败。   - download_failed : 下载失败。   - image_oversized : 镜像超大。   - waiting_for_scan : 等待扫描。   - image_scan_stop : 扫描终止。 **默认取值**: 不涉及 

        :return: The scan_status of this BatchExportLocalVulInfoRequestInfo.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this BatchExportLocalVulInfoRequestInfo.

        **参数解释**: 扫描状态 **约束限制**: 不涉及 **取值范围**:   - unscan : 未扫描。   - success : 扫描完成。   - scanning : 扫描中。   - failed : 扫描失败。   - download_failed : 下载失败。   - image_oversized : 镜像超大。   - waiting_for_scan : 等待扫描。   - image_scan_stop : 扫描终止。 **默认取值**: 不涉及 

        :param scan_status: The scan_status of this BatchExportLocalVulInfoRequestInfo.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def image_name(self):
        r"""Gets the image_name of this BatchExportLocalVulInfoRequestInfo.

        镜像名称

        :return: The image_name of this BatchExportLocalVulInfoRequestInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this BatchExportLocalVulInfoRequestInfo.

        镜像名称

        :param image_name: The image_name of this BatchExportLocalVulInfoRequestInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this BatchExportLocalVulInfoRequestInfo.

        镜像版本

        :return: The image_version of this BatchExportLocalVulInfoRequestInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this BatchExportLocalVulInfoRequestInfo.

        镜像版本

        :param image_version: The image_version of this BatchExportLocalVulInfoRequestInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_size(self):
        r"""Gets the image_size of this BatchExportLocalVulInfoRequestInfo.

        镜像大小

        :return: The image_size of this BatchExportLocalVulInfoRequestInfo.
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this BatchExportLocalVulInfoRequestInfo.

        镜像大小

        :param image_size: The image_size of this BatchExportLocalVulInfoRequestInfo.
        :type image_size: int
        """
        self._image_size = image_size

    @property
    def start_latest_update_time(self):
        r"""Gets the start_latest_update_time of this BatchExportLocalVulInfoRequestInfo.

        创建时间开始日期，时间单位 毫秒（ms）

        :return: The start_latest_update_time of this BatchExportLocalVulInfoRequestInfo.
        :rtype: int
        """
        return self._start_latest_update_time

    @start_latest_update_time.setter
    def start_latest_update_time(self, start_latest_update_time):
        r"""Sets the start_latest_update_time of this BatchExportLocalVulInfoRequestInfo.

        创建时间开始日期，时间单位 毫秒（ms）

        :param start_latest_update_time: The start_latest_update_time of this BatchExportLocalVulInfoRequestInfo.
        :type start_latest_update_time: int
        """
        self._start_latest_update_time = start_latest_update_time

    @property
    def end_latest_update_time(self):
        r"""Gets the end_latest_update_time of this BatchExportLocalVulInfoRequestInfo.

        创建时间结束日期，时间单位 毫秒（ms）

        :return: The end_latest_update_time of this BatchExportLocalVulInfoRequestInfo.
        :rtype: int
        """
        return self._end_latest_update_time

    @end_latest_update_time.setter
    def end_latest_update_time(self, end_latest_update_time):
        r"""Sets the end_latest_update_time of this BatchExportLocalVulInfoRequestInfo.

        创建时间结束日期，时间单位 毫秒（ms）

        :param end_latest_update_time: The end_latest_update_time of this BatchExportLocalVulInfoRequestInfo.
        :type end_latest_update_time: int
        """
        self._end_latest_update_time = end_latest_update_time

    @property
    def start_latest_scan_time(self):
        r"""Gets the start_latest_scan_time of this BatchExportLocalVulInfoRequestInfo.

        最近一次扫描完成时间开始日期，时间单位 毫秒（ms）

        :return: The start_latest_scan_time of this BatchExportLocalVulInfoRequestInfo.
        :rtype: int
        """
        return self._start_latest_scan_time

    @start_latest_scan_time.setter
    def start_latest_scan_time(self, start_latest_scan_time):
        r"""Sets the start_latest_scan_time of this BatchExportLocalVulInfoRequestInfo.

        最近一次扫描完成时间开始日期，时间单位 毫秒（ms）

        :param start_latest_scan_time: The start_latest_scan_time of this BatchExportLocalVulInfoRequestInfo.
        :type start_latest_scan_time: int
        """
        self._start_latest_scan_time = start_latest_scan_time

    @property
    def end_latest_scan_time(self):
        r"""Gets the end_latest_scan_time of this BatchExportLocalVulInfoRequestInfo.

        最近一次扫描完成时间结束日期，时间单位 毫秒（ms）

        :return: The end_latest_scan_time of this BatchExportLocalVulInfoRequestInfo.
        :rtype: int
        """
        return self._end_latest_scan_time

    @end_latest_scan_time.setter
    def end_latest_scan_time(self, end_latest_scan_time):
        r"""Sets the end_latest_scan_time of this BatchExportLocalVulInfoRequestInfo.

        最近一次扫描完成时间结束日期，时间单位 毫秒（ms）

        :param end_latest_scan_time: The end_latest_scan_time of this BatchExportLocalVulInfoRequestInfo.
        :type end_latest_scan_time: int
        """
        self._end_latest_scan_time = end_latest_scan_time

    @property
    def has_container(self):
        r"""Gets the has_container of this BatchExportLocalVulInfoRequestInfo.

        **参数解释**: 是否存在容器 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 

        :return: The has_container of this BatchExportLocalVulInfoRequestInfo.
        :rtype: bool
        """
        return self._has_container

    @has_container.setter
    def has_container(self, has_container):
        r"""Sets the has_container of this BatchExportLocalVulInfoRequestInfo.

        **参数解释**: 是否存在容器 **约束限制**: 不涉及 **取值范围**: - true：是。 - false：否。  **默认取值**: 不涉及 

        :param has_container: The has_container of this BatchExportLocalVulInfoRequestInfo.
        :type has_container: bool
        """
        self._has_container = has_container

    @property
    def vul_id_list(self):
        r"""Gets the vul_id_list of this BatchExportLocalVulInfoRequestInfo.

        导出镜像漏洞时的漏洞id列表

        :return: The vul_id_list of this BatchExportLocalVulInfoRequestInfo.
        :rtype: list[str]
        """
        return self._vul_id_list

    @vul_id_list.setter
    def vul_id_list(self, vul_id_list):
        r"""Sets the vul_id_list of this BatchExportLocalVulInfoRequestInfo.

        导出镜像漏洞时的漏洞id列表

        :param vul_id_list: The vul_id_list of this BatchExportLocalVulInfoRequestInfo.
        :type vul_id_list: list[str]
        """
        self._vul_id_list = vul_id_list

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
        if not isinstance(other, BatchExportLocalVulInfoRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
