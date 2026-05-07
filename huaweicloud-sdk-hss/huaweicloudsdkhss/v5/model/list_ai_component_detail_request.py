# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiComponentDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'category': 'str',
        'catalogue': 'str',
        'server_name': 'str',
        'server_ip': 'str',
        'ai_application': 'str',
        'host_id': 'str',
        'ai_tool': 'str',
        'type': 'str',
        'version': 'str',
        'installation_path': 'str',
        'first_scan_time': 'int',
        'latest_scan_time': 'int',
        'container_name': 'str',
        'container_id': 'str',
        'image_name': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'category': 'category',
        'catalogue': 'catalogue',
        'server_name': 'server_name',
        'server_ip': 'server_ip',
        'ai_application': 'ai_application',
        'host_id': 'host_id',
        'ai_tool': 'ai_tool',
        'type': 'type',
        'version': 'version',
        'installation_path': 'installation_path',
        'first_scan_time': 'first_scan_time',
        'latest_scan_time': 'latest_scan_time',
        'container_name': 'container_name',
        'container_id': 'container_id',
        'image_name': 'image_name'
    }

    def __init__(self, limit=None, offset=None, category=None, catalogue=None, server_name=None, server_ip=None, ai_application=None, host_id=None, ai_tool=None, type=None, version=None, installation_path=None, first_scan_time=None, latest_scan_time=None, container_name=None, container_id=None, image_name=None):
        r"""ListAiComponentDetailRequest

        The model defined in huaweicloud sdk

        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param category: **参数解释**: 资产类别 **约束限制**: 不涉及 **取值范围**: - host：主机资产 - container：容器资产  **默认取值**: host 
        :type category: str
        :param catalogue: **参数解释**: AI组件类别 **约束限制**: 不涉及 **取值范围**: - app：应用 - tool：工具  **默认取值**: 不涉及
        :type catalogue: str
        :param server_name: **参数解释**: category&#x3D;&#x3D;host时 表示服务器名称 category&#x3D;&#x3D;container时 表示节点名称 category&#x3D;&#x3D;serverless时 表示实例名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type server_name: str
        :param server_ip: **参数解释**: category&#x3D;&#x3D;host时 表示服务器IP地址 category&#x3D;&#x3D;container时 表示节点IP地址 category&#x3D;&#x3D;serverless时 表示实例IP地址 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type server_ip: str
        :param ai_application: **参数解释**: AI应用名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type ai_application: str
        :param host_id: **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type host_id: str
        :param ai_tool: **参数解释**: AI工具名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type ai_tool: str
        :param type: **参数解释**: AI应用类型 **约束限制**: 不涉及 **取值范围**: 字符长度0-64位 **默认取值**: 不涉及 
        :type type: str
        :param version: **参数解释**: AI版本 **约束限制**: 不涉及 **取值范围**: 字符长度0-32位 **默认取值**: 不涉及 
        :type version: str
        :param installation_path: **参数解释**: 安装路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及 
        :type installation_path: str
        :param first_scan_time: **参数解释**: 首次扫描时间，时间单位毫秒（ms） **约束限制**: 不涉及 **取值范围**: 取值0-9223372036854775807 **默认取值**: 不涉及 
        :type first_scan_time: int
        :param latest_scan_time: **参数解释**: 最近扫描时间，时间单位毫秒（ms） **约束限制**: 不涉及 **取值范围**: 取值0-9223372036854775807 **默认取值**: 不涉及 
        :type latest_scan_time: int
        :param container_name: **参数解释**: 容器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type container_name: str
        :param container_id: **参数解释**: 容器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type container_id: str
        :param image_name: **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type image_name: str
        """
        
        

        self._limit = None
        self._offset = None
        self._category = None
        self._catalogue = None
        self._server_name = None
        self._server_ip = None
        self._ai_application = None
        self._host_id = None
        self._ai_tool = None
        self._type = None
        self._version = None
        self._installation_path = None
        self._first_scan_time = None
        self._latest_scan_time = None
        self._container_name = None
        self._container_id = None
        self._image_name = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.category = category
        self.catalogue = catalogue
        if server_name is not None:
            self.server_name = server_name
        if server_ip is not None:
            self.server_ip = server_ip
        if ai_application is not None:
            self.ai_application = ai_application
        if host_id is not None:
            self.host_id = host_id
        if ai_tool is not None:
            self.ai_tool = ai_tool
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if installation_path is not None:
            self.installation_path = installation_path
        if first_scan_time is not None:
            self.first_scan_time = first_scan_time
        if latest_scan_time is not None:
            self.latest_scan_time = latest_scan_time
        if container_name is not None:
            self.container_name = container_name
        if container_id is not None:
            self.container_id = container_id
        if image_name is not None:
            self.image_name = image_name

    @property
    def limit(self):
        r"""Gets the limit of this ListAiComponentDetailRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListAiComponentDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAiComponentDetailRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListAiComponentDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAiComponentDetailRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListAiComponentDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAiComponentDetailRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListAiComponentDetailRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def category(self):
        r"""Gets the category of this ListAiComponentDetailRequest.

        **参数解释**: 资产类别 **约束限制**: 不涉及 **取值范围**: - host：主机资产 - container：容器资产  **默认取值**: host 

        :return: The category of this ListAiComponentDetailRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListAiComponentDetailRequest.

        **参数解释**: 资产类别 **约束限制**: 不涉及 **取值范围**: - host：主机资产 - container：容器资产  **默认取值**: host 

        :param category: The category of this ListAiComponentDetailRequest.
        :type category: str
        """
        self._category = category

    @property
    def catalogue(self):
        r"""Gets the catalogue of this ListAiComponentDetailRequest.

        **参数解释**: AI组件类别 **约束限制**: 不涉及 **取值范围**: - app：应用 - tool：工具  **默认取值**: 不涉及

        :return: The catalogue of this ListAiComponentDetailRequest.
        :rtype: str
        """
        return self._catalogue

    @catalogue.setter
    def catalogue(self, catalogue):
        r"""Sets the catalogue of this ListAiComponentDetailRequest.

        **参数解释**: AI组件类别 **约束限制**: 不涉及 **取值范围**: - app：应用 - tool：工具  **默认取值**: 不涉及

        :param catalogue: The catalogue of this ListAiComponentDetailRequest.
        :type catalogue: str
        """
        self._catalogue = catalogue

    @property
    def server_name(self):
        r"""Gets the server_name of this ListAiComponentDetailRequest.

        **参数解释**: category==host时 表示服务器名称 category==container时 表示节点名称 category==serverless时 表示实例名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The server_name of this ListAiComponentDetailRequest.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        r"""Sets the server_name of this ListAiComponentDetailRequest.

        **参数解释**: category==host时 表示服务器名称 category==container时 表示节点名称 category==serverless时 表示实例名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param server_name: The server_name of this ListAiComponentDetailRequest.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def server_ip(self):
        r"""Gets the server_ip of this ListAiComponentDetailRequest.

        **参数解释**: category==host时 表示服务器IP地址 category==container时 表示节点IP地址 category==serverless时 表示实例IP地址 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The server_ip of this ListAiComponentDetailRequest.
        :rtype: str
        """
        return self._server_ip

    @server_ip.setter
    def server_ip(self, server_ip):
        r"""Sets the server_ip of this ListAiComponentDetailRequest.

        **参数解释**: category==host时 表示服务器IP地址 category==container时 表示节点IP地址 category==serverless时 表示实例IP地址 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param server_ip: The server_ip of this ListAiComponentDetailRequest.
        :type server_ip: str
        """
        self._server_ip = server_ip

    @property
    def ai_application(self):
        r"""Gets the ai_application of this ListAiComponentDetailRequest.

        **参数解释**: AI应用名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The ai_application of this ListAiComponentDetailRequest.
        :rtype: str
        """
        return self._ai_application

    @ai_application.setter
    def ai_application(self, ai_application):
        r"""Sets the ai_application of this ListAiComponentDetailRequest.

        **参数解释**: AI应用名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param ai_application: The ai_application of this ListAiComponentDetailRequest.
        :type ai_application: str
        """
        self._ai_application = ai_application

    @property
    def host_id(self):
        r"""Gets the host_id of this ListAiComponentDetailRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The host_id of this ListAiComponentDetailRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListAiComponentDetailRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ListAiComponentDetailRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def ai_tool(self):
        r"""Gets the ai_tool of this ListAiComponentDetailRequest.

        **参数解释**: AI工具名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The ai_tool of this ListAiComponentDetailRequest.
        :rtype: str
        """
        return self._ai_tool

    @ai_tool.setter
    def ai_tool(self, ai_tool):
        r"""Sets the ai_tool of this ListAiComponentDetailRequest.

        **参数解释**: AI工具名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param ai_tool: The ai_tool of this ListAiComponentDetailRequest.
        :type ai_tool: str
        """
        self._ai_tool = ai_tool

    @property
    def type(self):
        r"""Gets the type of this ListAiComponentDetailRequest.

        **参数解释**: AI应用类型 **约束限制**: 不涉及 **取值范围**: 字符长度0-64位 **默认取值**: 不涉及 

        :return: The type of this ListAiComponentDetailRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListAiComponentDetailRequest.

        **参数解释**: AI应用类型 **约束限制**: 不涉及 **取值范围**: 字符长度0-64位 **默认取值**: 不涉及 

        :param type: The type of this ListAiComponentDetailRequest.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this ListAiComponentDetailRequest.

        **参数解释**: AI版本 **约束限制**: 不涉及 **取值范围**: 字符长度0-32位 **默认取值**: 不涉及 

        :return: The version of this ListAiComponentDetailRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListAiComponentDetailRequest.

        **参数解释**: AI版本 **约束限制**: 不涉及 **取值范围**: 字符长度0-32位 **默认取值**: 不涉及 

        :param version: The version of this ListAiComponentDetailRequest.
        :type version: str
        """
        self._version = version

    @property
    def installation_path(self):
        r"""Gets the installation_path of this ListAiComponentDetailRequest.

        **参数解释**: 安装路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及 

        :return: The installation_path of this ListAiComponentDetailRequest.
        :rtype: str
        """
        return self._installation_path

    @installation_path.setter
    def installation_path(self, installation_path):
        r"""Sets the installation_path of this ListAiComponentDetailRequest.

        **参数解释**: 安装路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及 

        :param installation_path: The installation_path of this ListAiComponentDetailRequest.
        :type installation_path: str
        """
        self._installation_path = installation_path

    @property
    def first_scan_time(self):
        r"""Gets the first_scan_time of this ListAiComponentDetailRequest.

        **参数解释**: 首次扫描时间，时间单位毫秒（ms） **约束限制**: 不涉及 **取值范围**: 取值0-9223372036854775807 **默认取值**: 不涉及 

        :return: The first_scan_time of this ListAiComponentDetailRequest.
        :rtype: int
        """
        return self._first_scan_time

    @first_scan_time.setter
    def first_scan_time(self, first_scan_time):
        r"""Sets the first_scan_time of this ListAiComponentDetailRequest.

        **参数解释**: 首次扫描时间，时间单位毫秒（ms） **约束限制**: 不涉及 **取值范围**: 取值0-9223372036854775807 **默认取值**: 不涉及 

        :param first_scan_time: The first_scan_time of this ListAiComponentDetailRequest.
        :type first_scan_time: int
        """
        self._first_scan_time = first_scan_time

    @property
    def latest_scan_time(self):
        r"""Gets the latest_scan_time of this ListAiComponentDetailRequest.

        **参数解释**: 最近扫描时间，时间单位毫秒（ms） **约束限制**: 不涉及 **取值范围**: 取值0-9223372036854775807 **默认取值**: 不涉及 

        :return: The latest_scan_time of this ListAiComponentDetailRequest.
        :rtype: int
        """
        return self._latest_scan_time

    @latest_scan_time.setter
    def latest_scan_time(self, latest_scan_time):
        r"""Sets the latest_scan_time of this ListAiComponentDetailRequest.

        **参数解释**: 最近扫描时间，时间单位毫秒（ms） **约束限制**: 不涉及 **取值范围**: 取值0-9223372036854775807 **默认取值**: 不涉及 

        :param latest_scan_time: The latest_scan_time of this ListAiComponentDetailRequest.
        :type latest_scan_time: int
        """
        self._latest_scan_time = latest_scan_time

    @property
    def container_name(self):
        r"""Gets the container_name of this ListAiComponentDetailRequest.

        **参数解释**: 容器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The container_name of this ListAiComponentDetailRequest.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ListAiComponentDetailRequest.

        **参数解释**: 容器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param container_name: The container_name of this ListAiComponentDetailRequest.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def container_id(self):
        r"""Gets the container_id of this ListAiComponentDetailRequest.

        **参数解释**: 容器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The container_id of this ListAiComponentDetailRequest.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ListAiComponentDetailRequest.

        **参数解释**: 容器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param container_id: The container_id of this ListAiComponentDetailRequest.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def image_name(self):
        r"""Gets the image_name of this ListAiComponentDetailRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The image_name of this ListAiComponentDetailRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListAiComponentDetailRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param image_name: The image_name of this ListAiComponentDetailRequest.
        :type image_name: str
        """
        self._image_name = image_name

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
        if not isinstance(other, ListAiComponentDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
