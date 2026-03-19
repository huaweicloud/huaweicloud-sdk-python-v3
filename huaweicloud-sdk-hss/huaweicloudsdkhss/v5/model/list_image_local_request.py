# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageLocalRequest:

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
        'offset': 'int',
        'limit': 'int',
        'image_name': 'str',
        'image_version': 'str',
        'scan_status': 'str',
        'local_image_type': 'str',
        'image_size': 'int',
        'start_latest_update_time': 'int',
        'end_latest_update_time': 'int',
        'start_latest_scan_time': 'int',
        'end_latest_scan_time': 'int',
        'has_vul': 'bool',
        'host_name': 'str',
        'host_id': 'str',
        'host_ip': 'str',
        'container_id': 'str',
        'container_name': 'str',
        'pod_id': 'str',
        'pod_name': 'str',
        'app_name': 'str',
        'has_container': 'bool'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'scan_status': 'scan_status',
        'local_image_type': 'local_image_type',
        'image_size': 'image_size',
        'start_latest_update_time': 'start_latest_update_time',
        'end_latest_update_time': 'end_latest_update_time',
        'start_latest_scan_time': 'start_latest_scan_time',
        'end_latest_scan_time': 'end_latest_scan_time',
        'has_vul': 'has_vul',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'host_ip': 'host_ip',
        'container_id': 'container_id',
        'container_name': 'container_name',
        'pod_id': 'pod_id',
        'pod_name': 'pod_name',
        'app_name': 'app_name',
        'has_container': 'has_container'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, image_name=None, image_version=None, scan_status=None, local_image_type=None, image_size=None, start_latest_update_time=None, end_latest_update_time=None, start_latest_scan_time=None, end_latest_scan_time=None, has_vul=None, host_name=None, host_id=None, host_ip=None, container_id=None, container_name=None, pod_id=None, pod_name=None, app_name=None, has_container=None):
        r"""ListImageLocalRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param image_name: **参数解释** 本地镜像的名称，用于模糊筛选指定名称的本地镜像列表 **约束限制** 支持部分匹配（如传入&#39;web&#39;可匹配所有名称含&#39;web&#39;的镜像），区分大小写 **取值范围** 字符长度1-256位，支持字母、数字、短横线、下划线、点号，禁止含@#$%等特殊字符 **默认取值** 无 
        :type image_name: str
        :param image_version: **参数解释** 本地镜像的版本标识，用于筛选指定版本的本地镜像，需与image_name配合使用 **约束限制** 仅当指定image_name时传参有效，否则筛选条件不生效 **取值范围** 字符长度1-128位，支持字母、数字、短横线、下划线、点号、冒号 **默认取值** 无 
        :type image_version: str
        :param scan_status: **参数解释** 本地镜像的安全扫描状态，用于筛选指定扫描状态的镜像列表 **约束限制** 取值必须在指定范围内，否则返回空结果，区分大小写 **取值范围**   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - waiting_for_scan : 等待扫描 **默认取值** 无 
        :type scan_status: str
        :param local_image_type: **参数解释** 本地镜像的存储来源类型，用于筛选不同来源的本地镜像 **约束限制** 取值必须在指定范围内，否则返回空结果，区分大小写 **取值范围**  - other_image : 非SWR镜像  - swr_image : SWR镜像 **默认取值** 无 
        :type local_image_type: str
        :param image_size: **参数解释** 本地镜像的大小（单位字节），用于筛选指定大小的镜像（精确匹配） **约束限制** 仅支持精确匹配，如需范围筛选需结合业务层处理 **取值范围** 取值0-9223372036854775807（约9EB） **默认取值** 无 
        :type image_size: int
        :param start_latest_update_time: **参数解释** 本地镜像版本最后更新时间的查询起始值（Unix时间戳，单位ms），与end_latest_update_time配合筛选时间范围 **时间格式** Unix时间戳（如1697509433000表示2023-10-16 10:23:53） **约束限制** 需与end_latest_update_time同时使用，且小于end_latest_update_time，否则筛选无效 **取值范围** 取值0-9223372036854775807 **默认取值** 无 
        :type start_latest_update_time: int
        :param end_latest_update_time: **参数解释** 本地镜像版本最后更新时间的查询结束值（Unix时间戳，单位ms），与start_latest_update_time配合筛选时间范围 **时间格式** Unix时间戳（如1709973506292表示2024-03-08 15:18:26） **约束限制** 需与start_latest_update_time同时使用，且大于start_latest_update_time，否则筛选无效 **取值范围** 取值0-9223372036854775807 **默认取值** 无 
        :type end_latest_update_time: int
        :param start_latest_scan_time: **参数解释** 本地镜像最近一次扫描完成时间的查询起始值（Unix时间戳，单位ms），与end_latest_scan_time配合筛选时间范围 **时间格式** Unix时间戳（精确到毫秒） **约束限制** 仅对scan_status为success的镜像有效，需与end_latest_scan_time同时使用 **取值范围** 取值0-9223372036854775807 **默认取值** 无 
        :type start_latest_scan_time: int
        :param end_latest_scan_time: **参数解释** 本地镜像最近一次扫描完成时间的查询结束值（Unix时间戳，单位ms），与start_latest_scan_time配合筛选时间范围 **时间格式** Unix时间戳（精确到毫秒） **约束限制** 仅对scan_status为success的镜像有效，且需大于start_latest_scan_time **取值范围** 取值0-9223372036854775807 **默认取值** 无 
        :type end_latest_scan_time: int
        :param has_vul: **参数解释** 用于筛选是否存在软件漏洞的本地镜像，true表示筛选有漏洞的镜像，false表示筛选无漏洞的镜像 **约束限制** 仅对scan_status为success的镜像有效，未扫描镜像不会被筛选 **取值范围** true（存在漏洞）、false（不存在漏洞） **默认取值** 无（不筛选漏洞状态） 
        :type has_vul: bool
        :param host_name: **参数解释** 本地镜像所关联的云服务器名称，用于筛选关联指定服务器的本地镜像 **约束限制** 支持模糊匹配，区分大小写，仅对关联了服务器的镜像有效 **取值范围** 字符长度1-64位，支持中文、英文、数字、短横线、下划线，禁止含特殊字符 **默认取值** 无 
        :type host_name: str
        :param host_id: **参数解释** 本地镜像所关联的云服务器唯一标识（ECS实例ID），用于精准筛选关联指定服务器的本地镜像 **约束限制** 精确匹配，仅对关联了该服务器的镜像有效 **取值范围** 字符长度1-64位，支持字母、数字、短横线 **默认取值** 无 
        :type host_id: str
        :param host_ip: **参数解释** 本地镜像所关联服务器的公网或私网IP地址，用于筛选关联指定IP服务器的本地镜像 **约束限制** 支持IPv4格式，精确匹配，多个IP需通过业务层分批查询 **取值范围** 符合IPv4格式的字符串（如 **默认取值** 无 
        :type host_ip: str
        :param container_id: **参数解释** 本地镜像所关联的容器唯一标识（Docker容器ID），用于精准筛选关联指定容器的本地镜像 **约束限制** 精确匹配，仅对关联了容器的镜像有效 **取值范围** 字符长度1-64位，支持字母、数字、短横线、下划线 **默认取值** 无 
        :type container_id: str
        :param container_name: **参数解释** 本地镜像所关联的容器名称，用于筛选关联指定名称容器的本地镜像 **约束限制** 支持模糊匹配，区分大小写，仅对关联了容器的镜像有效 **取值范围** 字符长度1-64位，支持字母、数字、短横线、下划线、点号 **默认取值** 无 
        :type container_name: str
        :param pod_id: **参数解释** 本地镜像所关联的Kubernetes Pod唯一标识，用于精准筛选关联指定Pod的本地镜像 **约束限制** 精确匹配，仅对K8s环境中关联了Pod的镜像有效 **取值范围** 字符长度1-64位，支持字母、数字、短横线 **默认取值** 无 
        :type pod_id: str
        :param pod_name: **参数解释** 本地镜像所关联的Kubernetes Pod名称，用于筛选关联指定名称Pod的本地镜像 **约束限制** 支持模糊匹配，区分大小写，仅对K8s环境中关联了Pod的镜像有效 **取值范围** 字符长度1-63位，支持字母、数字、短横线，不能以短横线开头或结尾 **默认取值** 无 
        :type pod_name: str
        :param app_name: **参数解释** 本地镜像中部署的应用软件名称（如Nginx、MySQL），用于筛选包含指定应用的本地镜像 **约束限制** 支持模糊匹配，区分大小写，仅对已识别应用的镜像有效 **取值范围** 字符长度1-64位，支持中文、英文、数字、短横线、下划线 **默认取值** 无 
        :type app_name: str
        :param has_container: **参数解释** 用于筛选是否关联了容器的本地镜像 **取值范围**: - true：关联容器的镜像 - false：未关联容器的镜像 **默认取值** 无（不筛选容器关联状态） 
        :type has_container: bool
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._image_name = None
        self._image_version = None
        self._scan_status = None
        self._local_image_type = None
        self._image_size = None
        self._start_latest_update_time = None
        self._end_latest_update_time = None
        self._start_latest_scan_time = None
        self._end_latest_scan_time = None
        self._has_vul = None
        self._host_name = None
        self._host_id = None
        self._host_ip = None
        self._container_id = None
        self._container_name = None
        self._pod_id = None
        self._pod_name = None
        self._app_name = None
        self._has_container = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if scan_status is not None:
            self.scan_status = scan_status
        if local_image_type is not None:
            self.local_image_type = local_image_type
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
        if has_vul is not None:
            self.has_vul = has_vul
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if host_ip is not None:
            self.host_ip = host_ip
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
        if has_container is not None:
            self.has_container = has_container

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListImageLocalRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListImageLocalRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListImageLocalRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListImageLocalRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListImageLocalRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListImageLocalRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListImageLocalRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListImageLocalRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListImageLocalRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListImageLocalRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImageLocalRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListImageLocalRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def image_name(self):
        r"""Gets the image_name of this ListImageLocalRequest.

        **参数解释** 本地镜像的名称，用于模糊筛选指定名称的本地镜像列表 **约束限制** 支持部分匹配（如传入'web'可匹配所有名称含'web'的镜像），区分大小写 **取值范围** 字符长度1-256位，支持字母、数字、短横线、下划线、点号，禁止含@#$%等特殊字符 **默认取值** 无 

        :return: The image_name of this ListImageLocalRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListImageLocalRequest.

        **参数解释** 本地镜像的名称，用于模糊筛选指定名称的本地镜像列表 **约束限制** 支持部分匹配（如传入'web'可匹配所有名称含'web'的镜像），区分大小写 **取值范围** 字符长度1-256位，支持字母、数字、短横线、下划线、点号，禁止含@#$%等特殊字符 **默认取值** 无 

        :param image_name: The image_name of this ListImageLocalRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ListImageLocalRequest.

        **参数解释** 本地镜像的版本标识，用于筛选指定版本的本地镜像，需与image_name配合使用 **约束限制** 仅当指定image_name时传参有效，否则筛选条件不生效 **取值范围** 字符长度1-128位，支持字母、数字、短横线、下划线、点号、冒号 **默认取值** 无 

        :return: The image_version of this ListImageLocalRequest.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ListImageLocalRequest.

        **参数解释** 本地镜像的版本标识，用于筛选指定版本的本地镜像，需与image_name配合使用 **约束限制** 仅当指定image_name时传参有效，否则筛选条件不生效 **取值范围** 字符长度1-128位，支持字母、数字、短横线、下划线、点号、冒号 **默认取值** 无 

        :param image_version: The image_version of this ListImageLocalRequest.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def scan_status(self):
        r"""Gets the scan_status of this ListImageLocalRequest.

        **参数解释** 本地镜像的安全扫描状态，用于筛选指定扫描状态的镜像列表 **约束限制** 取值必须在指定范围内，否则返回空结果，区分大小写 **取值范围**   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - waiting_for_scan : 等待扫描 **默认取值** 无 

        :return: The scan_status of this ListImageLocalRequest.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this ListImageLocalRequest.

        **参数解释** 本地镜像的安全扫描状态，用于筛选指定扫描状态的镜像列表 **约束限制** 取值必须在指定范围内，否则返回空结果，区分大小写 **取值范围**   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - waiting_for_scan : 等待扫描 **默认取值** 无 

        :param scan_status: The scan_status of this ListImageLocalRequest.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def local_image_type(self):
        r"""Gets the local_image_type of this ListImageLocalRequest.

        **参数解释** 本地镜像的存储来源类型，用于筛选不同来源的本地镜像 **约束限制** 取值必须在指定范围内，否则返回空结果，区分大小写 **取值范围**  - other_image : 非SWR镜像  - swr_image : SWR镜像 **默认取值** 无 

        :return: The local_image_type of this ListImageLocalRequest.
        :rtype: str
        """
        return self._local_image_type

    @local_image_type.setter
    def local_image_type(self, local_image_type):
        r"""Sets the local_image_type of this ListImageLocalRequest.

        **参数解释** 本地镜像的存储来源类型，用于筛选不同来源的本地镜像 **约束限制** 取值必须在指定范围内，否则返回空结果，区分大小写 **取值范围**  - other_image : 非SWR镜像  - swr_image : SWR镜像 **默认取值** 无 

        :param local_image_type: The local_image_type of this ListImageLocalRequest.
        :type local_image_type: str
        """
        self._local_image_type = local_image_type

    @property
    def image_size(self):
        r"""Gets the image_size of this ListImageLocalRequest.

        **参数解释** 本地镜像的大小（单位字节），用于筛选指定大小的镜像（精确匹配） **约束限制** 仅支持精确匹配，如需范围筛选需结合业务层处理 **取值范围** 取值0-9223372036854775807（约9EB） **默认取值** 无 

        :return: The image_size of this ListImageLocalRequest.
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this ListImageLocalRequest.

        **参数解释** 本地镜像的大小（单位字节），用于筛选指定大小的镜像（精确匹配） **约束限制** 仅支持精确匹配，如需范围筛选需结合业务层处理 **取值范围** 取值0-9223372036854775807（约9EB） **默认取值** 无 

        :param image_size: The image_size of this ListImageLocalRequest.
        :type image_size: int
        """
        self._image_size = image_size

    @property
    def start_latest_update_time(self):
        r"""Gets the start_latest_update_time of this ListImageLocalRequest.

        **参数解释** 本地镜像版本最后更新时间的查询起始值（Unix时间戳，单位ms），与end_latest_update_time配合筛选时间范围 **时间格式** Unix时间戳（如1697509433000表示2023-10-16 10:23:53） **约束限制** 需与end_latest_update_time同时使用，且小于end_latest_update_time，否则筛选无效 **取值范围** 取值0-9223372036854775807 **默认取值** 无 

        :return: The start_latest_update_time of this ListImageLocalRequest.
        :rtype: int
        """
        return self._start_latest_update_time

    @start_latest_update_time.setter
    def start_latest_update_time(self, start_latest_update_time):
        r"""Sets the start_latest_update_time of this ListImageLocalRequest.

        **参数解释** 本地镜像版本最后更新时间的查询起始值（Unix时间戳，单位ms），与end_latest_update_time配合筛选时间范围 **时间格式** Unix时间戳（如1697509433000表示2023-10-16 10:23:53） **约束限制** 需与end_latest_update_time同时使用，且小于end_latest_update_time，否则筛选无效 **取值范围** 取值0-9223372036854775807 **默认取值** 无 

        :param start_latest_update_time: The start_latest_update_time of this ListImageLocalRequest.
        :type start_latest_update_time: int
        """
        self._start_latest_update_time = start_latest_update_time

    @property
    def end_latest_update_time(self):
        r"""Gets the end_latest_update_time of this ListImageLocalRequest.

        **参数解释** 本地镜像版本最后更新时间的查询结束值（Unix时间戳，单位ms），与start_latest_update_time配合筛选时间范围 **时间格式** Unix时间戳（如1709973506292表示2024-03-08 15:18:26） **约束限制** 需与start_latest_update_time同时使用，且大于start_latest_update_time，否则筛选无效 **取值范围** 取值0-9223372036854775807 **默认取值** 无 

        :return: The end_latest_update_time of this ListImageLocalRequest.
        :rtype: int
        """
        return self._end_latest_update_time

    @end_latest_update_time.setter
    def end_latest_update_time(self, end_latest_update_time):
        r"""Sets the end_latest_update_time of this ListImageLocalRequest.

        **参数解释** 本地镜像版本最后更新时间的查询结束值（Unix时间戳，单位ms），与start_latest_update_time配合筛选时间范围 **时间格式** Unix时间戳（如1709973506292表示2024-03-08 15:18:26） **约束限制** 需与start_latest_update_time同时使用，且大于start_latest_update_time，否则筛选无效 **取值范围** 取值0-9223372036854775807 **默认取值** 无 

        :param end_latest_update_time: The end_latest_update_time of this ListImageLocalRequest.
        :type end_latest_update_time: int
        """
        self._end_latest_update_time = end_latest_update_time

    @property
    def start_latest_scan_time(self):
        r"""Gets the start_latest_scan_time of this ListImageLocalRequest.

        **参数解释** 本地镜像最近一次扫描完成时间的查询起始值（Unix时间戳，单位ms），与end_latest_scan_time配合筛选时间范围 **时间格式** Unix时间戳（精确到毫秒） **约束限制** 仅对scan_status为success的镜像有效，需与end_latest_scan_time同时使用 **取值范围** 取值0-9223372036854775807 **默认取值** 无 

        :return: The start_latest_scan_time of this ListImageLocalRequest.
        :rtype: int
        """
        return self._start_latest_scan_time

    @start_latest_scan_time.setter
    def start_latest_scan_time(self, start_latest_scan_time):
        r"""Sets the start_latest_scan_time of this ListImageLocalRequest.

        **参数解释** 本地镜像最近一次扫描完成时间的查询起始值（Unix时间戳，单位ms），与end_latest_scan_time配合筛选时间范围 **时间格式** Unix时间戳（精确到毫秒） **约束限制** 仅对scan_status为success的镜像有效，需与end_latest_scan_time同时使用 **取值范围** 取值0-9223372036854775807 **默认取值** 无 

        :param start_latest_scan_time: The start_latest_scan_time of this ListImageLocalRequest.
        :type start_latest_scan_time: int
        """
        self._start_latest_scan_time = start_latest_scan_time

    @property
    def end_latest_scan_time(self):
        r"""Gets the end_latest_scan_time of this ListImageLocalRequest.

        **参数解释** 本地镜像最近一次扫描完成时间的查询结束值（Unix时间戳，单位ms），与start_latest_scan_time配合筛选时间范围 **时间格式** Unix时间戳（精确到毫秒） **约束限制** 仅对scan_status为success的镜像有效，且需大于start_latest_scan_time **取值范围** 取值0-9223372036854775807 **默认取值** 无 

        :return: The end_latest_scan_time of this ListImageLocalRequest.
        :rtype: int
        """
        return self._end_latest_scan_time

    @end_latest_scan_time.setter
    def end_latest_scan_time(self, end_latest_scan_time):
        r"""Sets the end_latest_scan_time of this ListImageLocalRequest.

        **参数解释** 本地镜像最近一次扫描完成时间的查询结束值（Unix时间戳，单位ms），与start_latest_scan_time配合筛选时间范围 **时间格式** Unix时间戳（精确到毫秒） **约束限制** 仅对scan_status为success的镜像有效，且需大于start_latest_scan_time **取值范围** 取值0-9223372036854775807 **默认取值** 无 

        :param end_latest_scan_time: The end_latest_scan_time of this ListImageLocalRequest.
        :type end_latest_scan_time: int
        """
        self._end_latest_scan_time = end_latest_scan_time

    @property
    def has_vul(self):
        r"""Gets the has_vul of this ListImageLocalRequest.

        **参数解释** 用于筛选是否存在软件漏洞的本地镜像，true表示筛选有漏洞的镜像，false表示筛选无漏洞的镜像 **约束限制** 仅对scan_status为success的镜像有效，未扫描镜像不会被筛选 **取值范围** true（存在漏洞）、false（不存在漏洞） **默认取值** 无（不筛选漏洞状态） 

        :return: The has_vul of this ListImageLocalRequest.
        :rtype: bool
        """
        return self._has_vul

    @has_vul.setter
    def has_vul(self, has_vul):
        r"""Sets the has_vul of this ListImageLocalRequest.

        **参数解释** 用于筛选是否存在软件漏洞的本地镜像，true表示筛选有漏洞的镜像，false表示筛选无漏洞的镜像 **约束限制** 仅对scan_status为success的镜像有效，未扫描镜像不会被筛选 **取值范围** true（存在漏洞）、false（不存在漏洞） **默认取值** 无（不筛选漏洞状态） 

        :param has_vul: The has_vul of this ListImageLocalRequest.
        :type has_vul: bool
        """
        self._has_vul = has_vul

    @property
    def host_name(self):
        r"""Gets the host_name of this ListImageLocalRequest.

        **参数解释** 本地镜像所关联的云服务器名称，用于筛选关联指定服务器的本地镜像 **约束限制** 支持模糊匹配，区分大小写，仅对关联了服务器的镜像有效 **取值范围** 字符长度1-64位，支持中文、英文、数字、短横线、下划线，禁止含特殊字符 **默认取值** 无 

        :return: The host_name of this ListImageLocalRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListImageLocalRequest.

        **参数解释** 本地镜像所关联的云服务器名称，用于筛选关联指定服务器的本地镜像 **约束限制** 支持模糊匹配，区分大小写，仅对关联了服务器的镜像有效 **取值范围** 字符长度1-64位，支持中文、英文、数字、短横线、下划线，禁止含特殊字符 **默认取值** 无 

        :param host_name: The host_name of this ListImageLocalRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListImageLocalRequest.

        **参数解释** 本地镜像所关联的云服务器唯一标识（ECS实例ID），用于精准筛选关联指定服务器的本地镜像 **约束限制** 精确匹配，仅对关联了该服务器的镜像有效 **取值范围** 字符长度1-64位，支持字母、数字、短横线 **默认取值** 无 

        :return: The host_id of this ListImageLocalRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListImageLocalRequest.

        **参数解释** 本地镜像所关联的云服务器唯一标识（ECS实例ID），用于精准筛选关联指定服务器的本地镜像 **约束限制** 精确匹配，仅对关联了该服务器的镜像有效 **取值范围** 字符长度1-64位，支持字母、数字、短横线 **默认取值** 无 

        :param host_id: The host_id of this ListImageLocalRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ListImageLocalRequest.

        **参数解释** 本地镜像所关联服务器的公网或私网IP地址，用于筛选关联指定IP服务器的本地镜像 **约束限制** 支持IPv4格式，精确匹配，多个IP需通过业务层分批查询 **取值范围** 符合IPv4格式的字符串（如 **默认取值** 无 

        :return: The host_ip of this ListImageLocalRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ListImageLocalRequest.

        **参数解释** 本地镜像所关联服务器的公网或私网IP地址，用于筛选关联指定IP服务器的本地镜像 **约束限制** 支持IPv4格式，精确匹配，多个IP需通过业务层分批查询 **取值范围** 符合IPv4格式的字符串（如 **默认取值** 无 

        :param host_ip: The host_ip of this ListImageLocalRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def container_id(self):
        r"""Gets the container_id of this ListImageLocalRequest.

        **参数解释** 本地镜像所关联的容器唯一标识（Docker容器ID），用于精准筛选关联指定容器的本地镜像 **约束限制** 精确匹配，仅对关联了容器的镜像有效 **取值范围** 字符长度1-64位，支持字母、数字、短横线、下划线 **默认取值** 无 

        :return: The container_id of this ListImageLocalRequest.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ListImageLocalRequest.

        **参数解释** 本地镜像所关联的容器唯一标识（Docker容器ID），用于精准筛选关联指定容器的本地镜像 **约束限制** 精确匹配，仅对关联了容器的镜像有效 **取值范围** 字符长度1-64位，支持字母、数字、短横线、下划线 **默认取值** 无 

        :param container_id: The container_id of this ListImageLocalRequest.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this ListImageLocalRequest.

        **参数解释** 本地镜像所关联的容器名称，用于筛选关联指定名称容器的本地镜像 **约束限制** 支持模糊匹配，区分大小写，仅对关联了容器的镜像有效 **取值范围** 字符长度1-64位，支持字母、数字、短横线、下划线、点号 **默认取值** 无 

        :return: The container_name of this ListImageLocalRequest.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ListImageLocalRequest.

        **参数解释** 本地镜像所关联的容器名称，用于筛选关联指定名称容器的本地镜像 **约束限制** 支持模糊匹配，区分大小写，仅对关联了容器的镜像有效 **取值范围** 字符长度1-64位，支持字母、数字、短横线、下划线、点号 **默认取值** 无 

        :param container_name: The container_name of this ListImageLocalRequest.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def pod_id(self):
        r"""Gets the pod_id of this ListImageLocalRequest.

        **参数解释** 本地镜像所关联的Kubernetes Pod唯一标识，用于精准筛选关联指定Pod的本地镜像 **约束限制** 精确匹配，仅对K8s环境中关联了Pod的镜像有效 **取值范围** 字符长度1-64位，支持字母、数字、短横线 **默认取值** 无 

        :return: The pod_id of this ListImageLocalRequest.
        :rtype: str
        """
        return self._pod_id

    @pod_id.setter
    def pod_id(self, pod_id):
        r"""Sets the pod_id of this ListImageLocalRequest.

        **参数解释** 本地镜像所关联的Kubernetes Pod唯一标识，用于精准筛选关联指定Pod的本地镜像 **约束限制** 精确匹配，仅对K8s环境中关联了Pod的镜像有效 **取值范围** 字符长度1-64位，支持字母、数字、短横线 **默认取值** 无 

        :param pod_id: The pod_id of this ListImageLocalRequest.
        :type pod_id: str
        """
        self._pod_id = pod_id

    @property
    def pod_name(self):
        r"""Gets the pod_name of this ListImageLocalRequest.

        **参数解释** 本地镜像所关联的Kubernetes Pod名称，用于筛选关联指定名称Pod的本地镜像 **约束限制** 支持模糊匹配，区分大小写，仅对K8s环境中关联了Pod的镜像有效 **取值范围** 字符长度1-63位，支持字母、数字、短横线，不能以短横线开头或结尾 **默认取值** 无 

        :return: The pod_name of this ListImageLocalRequest.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this ListImageLocalRequest.

        **参数解释** 本地镜像所关联的Kubernetes Pod名称，用于筛选关联指定名称Pod的本地镜像 **约束限制** 支持模糊匹配，区分大小写，仅对K8s环境中关联了Pod的镜像有效 **取值范围** 字符长度1-63位，支持字母、数字、短横线，不能以短横线开头或结尾 **默认取值** 无 

        :param pod_name: The pod_name of this ListImageLocalRequest.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def app_name(self):
        r"""Gets the app_name of this ListImageLocalRequest.

        **参数解释** 本地镜像中部署的应用软件名称（如Nginx、MySQL），用于筛选包含指定应用的本地镜像 **约束限制** 支持模糊匹配，区分大小写，仅对已识别应用的镜像有效 **取值范围** 字符长度1-64位，支持中文、英文、数字、短横线、下划线 **默认取值** 无 

        :return: The app_name of this ListImageLocalRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ListImageLocalRequest.

        **参数解释** 本地镜像中部署的应用软件名称（如Nginx、MySQL），用于筛选包含指定应用的本地镜像 **约束限制** 支持模糊匹配，区分大小写，仅对已识别应用的镜像有效 **取值范围** 字符长度1-64位，支持中文、英文、数字、短横线、下划线 **默认取值** 无 

        :param app_name: The app_name of this ListImageLocalRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def has_container(self):
        r"""Gets the has_container of this ListImageLocalRequest.

        **参数解释** 用于筛选是否关联了容器的本地镜像 **取值范围**: - true：关联容器的镜像 - false：未关联容器的镜像 **默认取值** 无（不筛选容器关联状态） 

        :return: The has_container of this ListImageLocalRequest.
        :rtype: bool
        """
        return self._has_container

    @has_container.setter
    def has_container(self, has_container):
        r"""Sets the has_container of this ListImageLocalRequest.

        **参数解释** 用于筛选是否关联了容器的本地镜像 **取值范围**: - true：关联容器的镜像 - false：未关联容器的镜像 **默认取值** 无（不筛选容器关联状态） 

        :param has_container: The has_container of this ListImageLocalRequest.
        :type has_container: bool
        """
        self._has_container = has_container

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
        if not isinstance(other, ListImageLocalRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
