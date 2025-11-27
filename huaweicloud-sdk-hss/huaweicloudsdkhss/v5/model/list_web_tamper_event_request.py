# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWebTamperEventRequest:

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
        'type': 'str',
        'offset': 'int',
        'limit': 'int',
        'image_name': 'str',
        'image_version': 'str',
        'host_name': 'str',
        'host_id': 'str',
        'host_private_ip': 'str',
        'container_name': 'str',
        'container_id': 'str',
        'cluster_name': 'str',
        'cluster_id': 'str',
        'file_path': 'str',
        'process_path': 'str',
        'process_env': 'str',
        'web_app_name': 'str',
        'start_event_time': 'int',
        'end_event_time': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'offset': 'offset',
        'limit': 'limit',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'host_private_ip': 'host_private_ip',
        'container_name': 'container_name',
        'container_id': 'container_id',
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'file_path': 'file_path',
        'process_path': 'process_path',
        'process_env': 'process_env',
        'web_app_name': 'web_app_name',
        'start_event_time': 'start_event_time',
        'end_event_time': 'end_event_time'
    }

    def __init__(self, enterprise_project_id=None, type=None, offset=None, limit=None, image_name=None, image_version=None, host_name=None, host_id=None, host_private_ip=None, container_name=None, container_id=None, cluster_name=None, cluster_id=None, file_path=None, process_path=None, process_env=None, web_app_name=None, start_event_time=None, end_event_time=None):
        r"""ListWebTamperEventRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param type: **参数解释**: 网页防篡改类型 **约束限制**: 不涉及。 **取值范围**: - container_wtp：容器网页防篡改 **默认取值**: 不涉及 
        :type type: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param image_name: **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 
        :type image_name: str
        :param image_version: **参数解释**: 镜像版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type image_version: str
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type host_name: str
        :param host_id: **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type host_id: str
        :param host_private_ip: **参数解释**: 主机私有IP **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type host_private_ip: str
        :param container_name: **参数解释**: 容器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type container_name: str
        :param container_id: **参数解释**: 受影响容器id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type container_id: str
        :param cluster_name: **参数解释**: 所属集群名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type cluster_name: str
        :param cluster_id: **参数解释**： 集群id **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 
        :type cluster_id: str
        :param file_path: **参数解释**: 防护文件的文件路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type file_path: str
        :param process_path: **参数解释**: 进程路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type process_path: str
        :param process_env: **参数解释**: 进程环境，是指在容器内的进程或者宿主机的进程 **约束限制**: 不涉及 **取值范围**: - host：主机进程 - container：容器进程 **默认取值**: 不涉及 
        :type process_env: str
        :param web_app_name: **参数解释**: 网站应用名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type web_app_name: str
        :param start_event_time: **参数解释**: 开始时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 
        :type start_event_time: int
        :param end_event_time: **参数解释**: 开始时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 
        :type end_event_time: int
        """
        
        

        self._enterprise_project_id = None
        self._type = None
        self._offset = None
        self._limit = None
        self._image_name = None
        self._image_version = None
        self._host_name = None
        self._host_id = None
        self._host_private_ip = None
        self._container_name = None
        self._container_id = None
        self._cluster_name = None
        self._cluster_id = None
        self._file_path = None
        self._process_path = None
        self._process_env = None
        self._web_app_name = None
        self._start_event_time = None
        self._end_event_time = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.type = type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if host_private_ip is not None:
            self.host_private_ip = host_private_ip
        if container_name is not None:
            self.container_name = container_name
        if container_id is not None:
            self.container_id = container_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if file_path is not None:
            self.file_path = file_path
        if process_path is not None:
            self.process_path = process_path
        if process_env is not None:
            self.process_env = process_env
        if web_app_name is not None:
            self.web_app_name = web_app_name
        if start_event_time is not None:
            self.start_event_time = start_event_time
        if end_event_time is not None:
            self.end_event_time = end_event_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListWebTamperEventRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListWebTamperEventRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListWebTamperEventRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListWebTamperEventRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        r"""Gets the type of this ListWebTamperEventRequest.

        **参数解释**: 网页防篡改类型 **约束限制**: 不涉及。 **取值范围**: - container_wtp：容器网页防篡改 **默认取值**: 不涉及 

        :return: The type of this ListWebTamperEventRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListWebTamperEventRequest.

        **参数解释**: 网页防篡改类型 **约束限制**: 不涉及。 **取值范围**: - container_wtp：容器网页防篡改 **默认取值**: 不涉及 

        :param type: The type of this ListWebTamperEventRequest.
        :type type: str
        """
        self._type = type

    @property
    def offset(self):
        r"""Gets the offset of this ListWebTamperEventRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListWebTamperEventRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWebTamperEventRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListWebTamperEventRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListWebTamperEventRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListWebTamperEventRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWebTamperEventRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListWebTamperEventRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def image_name(self):
        r"""Gets the image_name of this ListWebTamperEventRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 

        :return: The image_name of this ListWebTamperEventRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListWebTamperEventRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 

        :param image_name: The image_name of this ListWebTamperEventRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ListWebTamperEventRequest.

        **参数解释**: 镜像版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The image_version of this ListWebTamperEventRequest.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ListWebTamperEventRequest.

        **参数解释**: 镜像版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param image_version: The image_version of this ListWebTamperEventRequest.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def host_name(self):
        r"""Gets the host_name of this ListWebTamperEventRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The host_name of this ListWebTamperEventRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListWebTamperEventRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListWebTamperEventRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListWebTamperEventRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The host_id of this ListWebTamperEventRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListWebTamperEventRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ListWebTamperEventRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_private_ip(self):
        r"""Gets the host_private_ip of this ListWebTamperEventRequest.

        **参数解释**: 主机私有IP **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The host_private_ip of this ListWebTamperEventRequest.
        :rtype: str
        """
        return self._host_private_ip

    @host_private_ip.setter
    def host_private_ip(self, host_private_ip):
        r"""Sets the host_private_ip of this ListWebTamperEventRequest.

        **参数解释**: 主机私有IP **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param host_private_ip: The host_private_ip of this ListWebTamperEventRequest.
        :type host_private_ip: str
        """
        self._host_private_ip = host_private_ip

    @property
    def container_name(self):
        r"""Gets the container_name of this ListWebTamperEventRequest.

        **参数解释**: 容器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The container_name of this ListWebTamperEventRequest.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ListWebTamperEventRequest.

        **参数解释**: 容器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param container_name: The container_name of this ListWebTamperEventRequest.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def container_id(self):
        r"""Gets the container_id of this ListWebTamperEventRequest.

        **参数解释**: 受影响容器id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The container_id of this ListWebTamperEventRequest.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ListWebTamperEventRequest.

        **参数解释**: 受影响容器id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param container_id: The container_id of this ListWebTamperEventRequest.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListWebTamperEventRequest.

        **参数解释**: 所属集群名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The cluster_name of this ListWebTamperEventRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListWebTamperEventRequest.

        **参数解释**: 所属集群名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param cluster_name: The cluster_name of this ListWebTamperEventRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListWebTamperEventRequest.

        **参数解释**： 集群id **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :return: The cluster_id of this ListWebTamperEventRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListWebTamperEventRequest.

        **参数解释**： 集群id **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :param cluster_id: The cluster_id of this ListWebTamperEventRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def file_path(self):
        r"""Gets the file_path of this ListWebTamperEventRequest.

        **参数解释**: 防护文件的文件路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The file_path of this ListWebTamperEventRequest.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ListWebTamperEventRequest.

        **参数解释**: 防护文件的文件路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param file_path: The file_path of this ListWebTamperEventRequest.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def process_path(self):
        r"""Gets the process_path of this ListWebTamperEventRequest.

        **参数解释**: 进程路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The process_path of this ListWebTamperEventRequest.
        :rtype: str
        """
        return self._process_path

    @process_path.setter
    def process_path(self, process_path):
        r"""Sets the process_path of this ListWebTamperEventRequest.

        **参数解释**: 进程路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param process_path: The process_path of this ListWebTamperEventRequest.
        :type process_path: str
        """
        self._process_path = process_path

    @property
    def process_env(self):
        r"""Gets the process_env of this ListWebTamperEventRequest.

        **参数解释**: 进程环境，是指在容器内的进程或者宿主机的进程 **约束限制**: 不涉及 **取值范围**: - host：主机进程 - container：容器进程 **默认取值**: 不涉及 

        :return: The process_env of this ListWebTamperEventRequest.
        :rtype: str
        """
        return self._process_env

    @process_env.setter
    def process_env(self, process_env):
        r"""Sets the process_env of this ListWebTamperEventRequest.

        **参数解释**: 进程环境，是指在容器内的进程或者宿主机的进程 **约束限制**: 不涉及 **取值范围**: - host：主机进程 - container：容器进程 **默认取值**: 不涉及 

        :param process_env: The process_env of this ListWebTamperEventRequest.
        :type process_env: str
        """
        self._process_env = process_env

    @property
    def web_app_name(self):
        r"""Gets the web_app_name of this ListWebTamperEventRequest.

        **参数解释**: 网站应用名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The web_app_name of this ListWebTamperEventRequest.
        :rtype: str
        """
        return self._web_app_name

    @web_app_name.setter
    def web_app_name(self, web_app_name):
        r"""Sets the web_app_name of this ListWebTamperEventRequest.

        **参数解释**: 网站应用名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param web_app_name: The web_app_name of this ListWebTamperEventRequest.
        :type web_app_name: str
        """
        self._web_app_name = web_app_name

    @property
    def start_event_time(self):
        r"""Gets the start_event_time of this ListWebTamperEventRequest.

        **参数解释**: 开始时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :return: The start_event_time of this ListWebTamperEventRequest.
        :rtype: int
        """
        return self._start_event_time

    @start_event_time.setter
    def start_event_time(self, start_event_time):
        r"""Sets the start_event_time of this ListWebTamperEventRequest.

        **参数解释**: 开始时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :param start_event_time: The start_event_time of this ListWebTamperEventRequest.
        :type start_event_time: int
        """
        self._start_event_time = start_event_time

    @property
    def end_event_time(self):
        r"""Gets the end_event_time of this ListWebTamperEventRequest.

        **参数解释**: 开始时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :return: The end_event_time of this ListWebTamperEventRequest.
        :rtype: int
        """
        return self._end_event_time

    @end_event_time.setter
    def end_event_time(self, end_event_time):
        r"""Sets the end_event_time of this ListWebTamperEventRequest.

        **参数解释**: 开始时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :param end_event_time: The end_event_time of this ListWebTamperEventRequest.
        :type end_event_time: int
        """
        self._end_event_time = end_event_time

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
        if not isinstance(other, ListWebTamperEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
