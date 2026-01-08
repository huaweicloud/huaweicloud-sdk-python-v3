# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportDesktopListNewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'computer_name': 'str',
        'desktop_ip': 'str',
        'desktop_id': 'str',
        'tag': 'str',
        'language': 'str',
        'enterprise_project_id': 'str',
        'desktop_type': 'str',
        'status': 'str',
        'user_names': 'list[str]',
        'sort_field': 'str',
        'sort_type': 'str',
        'pool_id': 'str',
        'user_attached': 'bool',
        'image_id': 'str',
        'charge_mode': 'str',
        'in_maintenance_mode': 'bool',
        'subnet_id': 'str',
        'connection_status_version': 'str'
    }

    attribute_map = {
        'computer_name': 'computer_name',
        'desktop_ip': 'desktop_ip',
        'desktop_id': 'desktop_id',
        'tag': 'tag',
        'language': 'language',
        'enterprise_project_id': 'enterprise_project_id',
        'desktop_type': 'desktop_type',
        'status': 'status',
        'user_names': 'user_names',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'pool_id': 'pool_id',
        'user_attached': 'user_attached',
        'image_id': 'image_id',
        'charge_mode': 'charge_mode',
        'in_maintenance_mode': 'in_maintenance_mode',
        'subnet_id': 'subnet_id',
        'connection_status_version': 'connection_status_version'
    }

    def __init__(self, computer_name=None, desktop_ip=None, desktop_id=None, tag=None, language=None, enterprise_project_id=None, desktop_type=None, status=None, user_names=None, sort_field=None, sort_type=None, pool_id=None, user_attached=None, image_id=None, charge_mode=None, in_maintenance_mode=None, subnet_id=None, connection_status_version=None):
        r"""ExportDesktopListNewRequest

        The model defined in huaweicloud sdk

        :param computer_name: 桌面名。
        :type computer_name: str
        :param desktop_ip: 桌面IP地址。
        :type desktop_ip: str
        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param tag: 桌面的标签。标签的键和标签的值用“&#x3D;”连接。
        :type tag: str
        :param language: 语言。  - zh_CN：中文 - en_US：英文
        :type language: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param desktop_type: 桌面类型，为空时查所有桌面。 - DEDICATED：普通桌面，包括专享桌面、专属桌面等 - POOLED：池桌面，即桌面池里的桌面
        :type desktop_type: str
        :param status: 桌面状态。  - ACTIVE：运行中。 - SHUTOFF：关机。 - ERROR：异常。 - HIBERNATED：休眠。
        :type status: str
        :param user_names: 桌面所属用户，批量筛选，最多不超过100个用户。
        :type user_names: list[str]
        :param sort_field: 排序字段名称，需要结合sort_type字段一起使用。 - created 创建时间。 - computer_name 桌面名称。
        :type sort_field: str
        :param sort_type: 排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。
        :type sort_type: str
        :param pool_id: 桌面池ID,多个桌面池ID用逗号隔开。
        :type pool_id: str
        :param user_attached: 是否分配了用户。
        :type user_attached: bool
        :param image_id: 镜像ID。
        :type image_id: str
        :param charge_mode: 计费模式，0：包周期，1：按需。
        :type charge_mode: str
        :param in_maintenance_mode: 按照维护模式过滤。
        :type in_maintenance_mode: bool
        :param subnet_id: 桌面的子网ID。
        :type subnet_id: str
        :param connection_status_version: 连接状态版本，默认值为OLD。 - NEW：新版本 - OLD：老版本
        :type connection_status_version: str
        """
        
        

        self._computer_name = None
        self._desktop_ip = None
        self._desktop_id = None
        self._tag = None
        self._language = None
        self._enterprise_project_id = None
        self._desktop_type = None
        self._status = None
        self._user_names = None
        self._sort_field = None
        self._sort_type = None
        self._pool_id = None
        self._user_attached = None
        self._image_id = None
        self._charge_mode = None
        self._in_maintenance_mode = None
        self._subnet_id = None
        self._connection_status_version = None
        self.discriminator = None

        if computer_name is not None:
            self.computer_name = computer_name
        if desktop_ip is not None:
            self.desktop_ip = desktop_ip
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if tag is not None:
            self.tag = tag
        self.language = language
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if desktop_type is not None:
            self.desktop_type = desktop_type
        if status is not None:
            self.status = status
        if user_names is not None:
            self.user_names = user_names
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type
        if pool_id is not None:
            self.pool_id = pool_id
        if user_attached is not None:
            self.user_attached = user_attached
        if image_id is not None:
            self.image_id = image_id
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if in_maintenance_mode is not None:
            self.in_maintenance_mode = in_maintenance_mode
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if connection_status_version is not None:
            self.connection_status_version = connection_status_version

    @property
    def computer_name(self):
        r"""Gets the computer_name of this ExportDesktopListNewRequest.

        桌面名。

        :return: The computer_name of this ExportDesktopListNewRequest.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        r"""Sets the computer_name of this ExportDesktopListNewRequest.

        桌面名。

        :param computer_name: The computer_name of this ExportDesktopListNewRequest.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def desktop_ip(self):
        r"""Gets the desktop_ip of this ExportDesktopListNewRequest.

        桌面IP地址。

        :return: The desktop_ip of this ExportDesktopListNewRequest.
        :rtype: str
        """
        return self._desktop_ip

    @desktop_ip.setter
    def desktop_ip(self, desktop_ip):
        r"""Sets the desktop_ip of this ExportDesktopListNewRequest.

        桌面IP地址。

        :param desktop_ip: The desktop_ip of this ExportDesktopListNewRequest.
        :type desktop_ip: str
        """
        self._desktop_ip = desktop_ip

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this ExportDesktopListNewRequest.

        桌面ID。

        :return: The desktop_id of this ExportDesktopListNewRequest.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this ExportDesktopListNewRequest.

        桌面ID。

        :param desktop_id: The desktop_id of this ExportDesktopListNewRequest.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def tag(self):
        r"""Gets the tag of this ExportDesktopListNewRequest.

        桌面的标签。标签的键和标签的值用“=”连接。

        :return: The tag of this ExportDesktopListNewRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ExportDesktopListNewRequest.

        桌面的标签。标签的键和标签的值用“=”连接。

        :param tag: The tag of this ExportDesktopListNewRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def language(self):
        r"""Gets the language of this ExportDesktopListNewRequest.

        语言。  - zh_CN：中文 - en_US：英文

        :return: The language of this ExportDesktopListNewRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ExportDesktopListNewRequest.

        语言。  - zh_CN：中文 - en_US：英文

        :param language: The language of this ExportDesktopListNewRequest.
        :type language: str
        """
        self._language = language

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ExportDesktopListNewRequest.

        企业项目ID。

        :return: The enterprise_project_id of this ExportDesktopListNewRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ExportDesktopListNewRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ExportDesktopListNewRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def desktop_type(self):
        r"""Gets the desktop_type of this ExportDesktopListNewRequest.

        桌面类型，为空时查所有桌面。 - DEDICATED：普通桌面，包括专享桌面、专属桌面等 - POOLED：池桌面，即桌面池里的桌面

        :return: The desktop_type of this ExportDesktopListNewRequest.
        :rtype: str
        """
        return self._desktop_type

    @desktop_type.setter
    def desktop_type(self, desktop_type):
        r"""Sets the desktop_type of this ExportDesktopListNewRequest.

        桌面类型，为空时查所有桌面。 - DEDICATED：普通桌面，包括专享桌面、专属桌面等 - POOLED：池桌面，即桌面池里的桌面

        :param desktop_type: The desktop_type of this ExportDesktopListNewRequest.
        :type desktop_type: str
        """
        self._desktop_type = desktop_type

    @property
    def status(self):
        r"""Gets the status of this ExportDesktopListNewRequest.

        桌面状态。  - ACTIVE：运行中。 - SHUTOFF：关机。 - ERROR：异常。 - HIBERNATED：休眠。

        :return: The status of this ExportDesktopListNewRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExportDesktopListNewRequest.

        桌面状态。  - ACTIVE：运行中。 - SHUTOFF：关机。 - ERROR：异常。 - HIBERNATED：休眠。

        :param status: The status of this ExportDesktopListNewRequest.
        :type status: str
        """
        self._status = status

    @property
    def user_names(self):
        r"""Gets the user_names of this ExportDesktopListNewRequest.

        桌面所属用户，批量筛选，最多不超过100个用户。

        :return: The user_names of this ExportDesktopListNewRequest.
        :rtype: list[str]
        """
        return self._user_names

    @user_names.setter
    def user_names(self, user_names):
        r"""Sets the user_names of this ExportDesktopListNewRequest.

        桌面所属用户，批量筛选，最多不超过100个用户。

        :param user_names: The user_names of this ExportDesktopListNewRequest.
        :type user_names: list[str]
        """
        self._user_names = user_names

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ExportDesktopListNewRequest.

        排序字段名称，需要结合sort_type字段一起使用。 - created 创建时间。 - computer_name 桌面名称。

        :return: The sort_field of this ExportDesktopListNewRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ExportDesktopListNewRequest.

        排序字段名称，需要结合sort_type字段一起使用。 - created 创建时间。 - computer_name 桌面名称。

        :param sort_field: The sort_field of this ExportDesktopListNewRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        r"""Gets the sort_type of this ExportDesktopListNewRequest.

        排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。

        :return: The sort_type of this ExportDesktopListNewRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        r"""Sets the sort_type of this ExportDesktopListNewRequest.

        排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。

        :param sort_type: The sort_type of this ExportDesktopListNewRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def pool_id(self):
        r"""Gets the pool_id of this ExportDesktopListNewRequest.

        桌面池ID,多个桌面池ID用逗号隔开。

        :return: The pool_id of this ExportDesktopListNewRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this ExportDesktopListNewRequest.

        桌面池ID,多个桌面池ID用逗号隔开。

        :param pool_id: The pool_id of this ExportDesktopListNewRequest.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def user_attached(self):
        r"""Gets the user_attached of this ExportDesktopListNewRequest.

        是否分配了用户。

        :return: The user_attached of this ExportDesktopListNewRequest.
        :rtype: bool
        """
        return self._user_attached

    @user_attached.setter
    def user_attached(self, user_attached):
        r"""Sets the user_attached of this ExportDesktopListNewRequest.

        是否分配了用户。

        :param user_attached: The user_attached of this ExportDesktopListNewRequest.
        :type user_attached: bool
        """
        self._user_attached = user_attached

    @property
    def image_id(self):
        r"""Gets the image_id of this ExportDesktopListNewRequest.

        镜像ID。

        :return: The image_id of this ExportDesktopListNewRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ExportDesktopListNewRequest.

        镜像ID。

        :param image_id: The image_id of this ExportDesktopListNewRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this ExportDesktopListNewRequest.

        计费模式，0：包周期，1：按需。

        :return: The charge_mode of this ExportDesktopListNewRequest.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this ExportDesktopListNewRequest.

        计费模式，0：包周期，1：按需。

        :param charge_mode: The charge_mode of this ExportDesktopListNewRequest.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def in_maintenance_mode(self):
        r"""Gets the in_maintenance_mode of this ExportDesktopListNewRequest.

        按照维护模式过滤。

        :return: The in_maintenance_mode of this ExportDesktopListNewRequest.
        :rtype: bool
        """
        return self._in_maintenance_mode

    @in_maintenance_mode.setter
    def in_maintenance_mode(self, in_maintenance_mode):
        r"""Sets the in_maintenance_mode of this ExportDesktopListNewRequest.

        按照维护模式过滤。

        :param in_maintenance_mode: The in_maintenance_mode of this ExportDesktopListNewRequest.
        :type in_maintenance_mode: bool
        """
        self._in_maintenance_mode = in_maintenance_mode

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ExportDesktopListNewRequest.

        桌面的子网ID。

        :return: The subnet_id of this ExportDesktopListNewRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ExportDesktopListNewRequest.

        桌面的子网ID。

        :param subnet_id: The subnet_id of this ExportDesktopListNewRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def connection_status_version(self):
        r"""Gets the connection_status_version of this ExportDesktopListNewRequest.

        连接状态版本，默认值为OLD。 - NEW：新版本 - OLD：老版本

        :return: The connection_status_version of this ExportDesktopListNewRequest.
        :rtype: str
        """
        return self._connection_status_version

    @connection_status_version.setter
    def connection_status_version(self, connection_status_version):
        r"""Sets the connection_status_version of this ExportDesktopListNewRequest.

        连接状态版本，默认值为OLD。 - NEW：新版本 - OLD：老版本

        :param connection_status_version: The connection_status_version of this ExportDesktopListNewRequest.
        :type connection_status_version: str
        """
        self._connection_status_version = connection_status_version

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
        if not isinstance(other, ExportDesktopListNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
