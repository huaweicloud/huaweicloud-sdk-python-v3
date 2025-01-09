# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopsDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'user_name': 'str',
        'user_names': 'list[str]',
        'sort_field': 'str',
        'sort_type': 'str',
        'computer_name': 'str',
        'desktop_ip': 'str',
        'sids': 'str',
        'offset': 'int',
        'limit': 'int',
        'desktop_id': 'list[str]',
        'desktop_type': 'str',
        'login_status': 'str',
        'tag': 'str',
        'fuzzy_query': 'bool',
        'pool_id': 'str',
        'user_attached': 'bool',
        'enterprise_project_id': 'str',
        'image_id': 'str',
        'charge_mode': 'str',
        'in_maintenance_mode': 'bool',
        'is_share_desktop': 'bool',
        'subnet_id': 'str',
        'is_support_internet': 'bool',
        'availability_zone': 'str'
    }

    attribute_map = {
        'status': 'status',
        'user_name': 'user_name',
        'user_names': 'user_names',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'computer_name': 'computer_name',
        'desktop_ip': 'desktop_ip',
        'sids': 'sids',
        'offset': 'offset',
        'limit': 'limit',
        'desktop_id': 'desktop_id',
        'desktop_type': 'desktop_type',
        'login_status': 'login_status',
        'tag': 'tag',
        'fuzzy_query': 'fuzzy_query',
        'pool_id': 'pool_id',
        'user_attached': 'user_attached',
        'enterprise_project_id': 'enterprise_project_id',
        'image_id': 'image_id',
        'charge_mode': 'charge_mode',
        'in_maintenance_mode': 'in_maintenance_mode',
        'is_share_desktop': 'is_share_desktop',
        'subnet_id': 'subnet_id',
        'is_support_internet': 'is_support_internet',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, status=None, user_name=None, user_names=None, sort_field=None, sort_type=None, computer_name=None, desktop_ip=None, sids=None, offset=None, limit=None, desktop_id=None, desktop_type=None, login_status=None, tag=None, fuzzy_query=None, pool_id=None, user_attached=None, enterprise_project_id=None, image_id=None, charge_mode=None, in_maintenance_mode=None, is_share_desktop=None, subnet_id=None, is_support_internet=None, availability_zone=None):
        """ListDesktopsDetailRequest

        The model defined in huaweicloud sdk

        :param status: 桌面状态。  - ACTIVE：运行中。 - SHUTOFF：关机。 - ERROR：异常。 - HIBERNATED：休眠。
        :type status: str
        :param user_name: 桌面所属用户，当传user_names时，本字段不生效。
        :type user_name: str
        :param user_names: 桌面所属用户，批量筛选，最多不超过100个用户。
        :type user_names: list[str]
        :param sort_field: 排序字段名称，需要结合sort_type字段一起使用。 - created 创建时间。 - computer_name 桌面名称。
        :type sort_field: str
        :param sort_type: 排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。
        :type sort_type: str
        :param computer_name: 桌面名。
        :type computer_name: str
        :param desktop_ip: 桌面IP地址。
        :type desktop_ip: str
        :param sids: 桌面的sid列表。
        :type sids: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param limit: 用于分页查询，取值范围0-500，默认值500。
        :type limit: int
        :param desktop_id: 桌面ID。
        :type desktop_id: list[str]
        :param desktop_type: 桌面类型，为空时查所有桌面。 - DEDICATED：普通桌面，包括专享桌面、专属桌面等 - POOLED：池桌面，即桌面池里的桌面
        :type desktop_type: str
        :param login_status: 桌面的登录状态。  - UNREGISTER：表示桌面未注册时的状态（桌面启动后，会自动注册）。关机后也会出现未注册的状态。 - REGISTERED：表示桌面注册以后，等待用户连接的状态。 - CONNECTED：表示用户已经成功登录，正在使用桌面。 - DISCONNECTED：表示桌面与客户端断开会话后显示的状态，可能为关闭客户端窗口，或客户端与桌面网络断开引起。
        :type login_status: str
        :param tag: 桌面的标签。样例：  - key1&#x3D;value1。 - key1&#x3D;value1，key2&#x3D;value2。
        :type tag: str
        :param fuzzy_query: 是不是模糊用户查询。
        :type fuzzy_query: bool
        :param pool_id: 桌面池ID,多个桌面池ID用逗号隔开。
        :type pool_id: str
        :param user_attached: 是否分配了用户。
        :type user_attached: bool
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param image_id: 镜像ID
        :type image_id: str
        :param charge_mode: 计费模式，0：包周期，1：按需。
        :type charge_mode: str
        :param in_maintenance_mode: 按照维护模式过滤
        :type in_maintenance_mode: bool
        :param is_share_desktop: 是否为协同桌面
        :type is_share_desktop: bool
        :param subnet_id: 桌面的子网ID。
        :type subnet_id: str
        :param is_support_internet: 是否支持上网。
        :type is_support_internet: bool
        :param availability_zone: 查询可用区
        :type availability_zone: str
        """
        
        

        self._status = None
        self._user_name = None
        self._user_names = None
        self._sort_field = None
        self._sort_type = None
        self._computer_name = None
        self._desktop_ip = None
        self._sids = None
        self._offset = None
        self._limit = None
        self._desktop_id = None
        self._desktop_type = None
        self._login_status = None
        self._tag = None
        self._fuzzy_query = None
        self._pool_id = None
        self._user_attached = None
        self._enterprise_project_id = None
        self._image_id = None
        self._charge_mode = None
        self._in_maintenance_mode = None
        self._is_share_desktop = None
        self._subnet_id = None
        self._is_support_internet = None
        self._availability_zone = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if user_name is not None:
            self.user_name = user_name
        if user_names is not None:
            self.user_names = user_names
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type
        if computer_name is not None:
            self.computer_name = computer_name
        if desktop_ip is not None:
            self.desktop_ip = desktop_ip
        if sids is not None:
            self.sids = sids
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_type is not None:
            self.desktop_type = desktop_type
        if login_status is not None:
            self.login_status = login_status
        if tag is not None:
            self.tag = tag
        if fuzzy_query is not None:
            self.fuzzy_query = fuzzy_query
        if pool_id is not None:
            self.pool_id = pool_id
        if user_attached is not None:
            self.user_attached = user_attached
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if image_id is not None:
            self.image_id = image_id
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if in_maintenance_mode is not None:
            self.in_maintenance_mode = in_maintenance_mode
        if is_share_desktop is not None:
            self.is_share_desktop = is_share_desktop
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if is_support_internet is not None:
            self.is_support_internet = is_support_internet
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def status(self):
        """Gets the status of this ListDesktopsDetailRequest.

        桌面状态。  - ACTIVE：运行中。 - SHUTOFF：关机。 - ERROR：异常。 - HIBERNATED：休眠。

        :return: The status of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListDesktopsDetailRequest.

        桌面状态。  - ACTIVE：运行中。 - SHUTOFF：关机。 - ERROR：异常。 - HIBERNATED：休眠。

        :param status: The status of this ListDesktopsDetailRequest.
        :type status: str
        """
        self._status = status

    @property
    def user_name(self):
        """Gets the user_name of this ListDesktopsDetailRequest.

        桌面所属用户，当传user_names时，本字段不生效。

        :return: The user_name of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListDesktopsDetailRequest.

        桌面所属用户，当传user_names时，本字段不生效。

        :param user_name: The user_name of this ListDesktopsDetailRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_names(self):
        """Gets the user_names of this ListDesktopsDetailRequest.

        桌面所属用户，批量筛选，最多不超过100个用户。

        :return: The user_names of this ListDesktopsDetailRequest.
        :rtype: list[str]
        """
        return self._user_names

    @user_names.setter
    def user_names(self, user_names):
        """Sets the user_names of this ListDesktopsDetailRequest.

        桌面所属用户，批量筛选，最多不超过100个用户。

        :param user_names: The user_names of this ListDesktopsDetailRequest.
        :type user_names: list[str]
        """
        self._user_names = user_names

    @property
    def sort_field(self):
        """Gets the sort_field of this ListDesktopsDetailRequest.

        排序字段名称，需要结合sort_type字段一起使用。 - created 创建时间。 - computer_name 桌面名称。

        :return: The sort_field of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this ListDesktopsDetailRequest.

        排序字段名称，需要结合sort_type字段一起使用。 - created 创建时间。 - computer_name 桌面名称。

        :param sort_field: The sort_field of this ListDesktopsDetailRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        """Gets the sort_type of this ListDesktopsDetailRequest.

        排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。

        :return: The sort_type of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        """Sets the sort_type of this ListDesktopsDetailRequest.

        排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。

        :param sort_type: The sort_type of this ListDesktopsDetailRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def computer_name(self):
        """Gets the computer_name of this ListDesktopsDetailRequest.

        桌面名。

        :return: The computer_name of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        """Sets the computer_name of this ListDesktopsDetailRequest.

        桌面名。

        :param computer_name: The computer_name of this ListDesktopsDetailRequest.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def desktop_ip(self):
        """Gets the desktop_ip of this ListDesktopsDetailRequest.

        桌面IP地址。

        :return: The desktop_ip of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._desktop_ip

    @desktop_ip.setter
    def desktop_ip(self, desktop_ip):
        """Sets the desktop_ip of this ListDesktopsDetailRequest.

        桌面IP地址。

        :param desktop_ip: The desktop_ip of this ListDesktopsDetailRequest.
        :type desktop_ip: str
        """
        self._desktop_ip = desktop_ip

    @property
    def sids(self):
        """Gets the sids of this ListDesktopsDetailRequest.

        桌面的sid列表。

        :return: The sids of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._sids

    @sids.setter
    def sids(self, sids):
        """Sets the sids of this ListDesktopsDetailRequest.

        桌面的sid列表。

        :param sids: The sids of this ListDesktopsDetailRequest.
        :type sids: str
        """
        self._sids = sids

    @property
    def offset(self):
        """Gets the offset of this ListDesktopsDetailRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListDesktopsDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDesktopsDetailRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListDesktopsDetailRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDesktopsDetailRequest.

        用于分页查询，取值范围0-500，默认值500。

        :return: The limit of this ListDesktopsDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDesktopsDetailRequest.

        用于分页查询，取值范围0-500，默认值500。

        :param limit: The limit of this ListDesktopsDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def desktop_id(self):
        """Gets the desktop_id of this ListDesktopsDetailRequest.

        桌面ID。

        :return: The desktop_id of this ListDesktopsDetailRequest.
        :rtype: list[str]
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this ListDesktopsDetailRequest.

        桌面ID。

        :param desktop_id: The desktop_id of this ListDesktopsDetailRequest.
        :type desktop_id: list[str]
        """
        self._desktop_id = desktop_id

    @property
    def desktop_type(self):
        """Gets the desktop_type of this ListDesktopsDetailRequest.

        桌面类型，为空时查所有桌面。 - DEDICATED：普通桌面，包括专享桌面、专属桌面等 - POOLED：池桌面，即桌面池里的桌面

        :return: The desktop_type of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._desktop_type

    @desktop_type.setter
    def desktop_type(self, desktop_type):
        """Sets the desktop_type of this ListDesktopsDetailRequest.

        桌面类型，为空时查所有桌面。 - DEDICATED：普通桌面，包括专享桌面、专属桌面等 - POOLED：池桌面，即桌面池里的桌面

        :param desktop_type: The desktop_type of this ListDesktopsDetailRequest.
        :type desktop_type: str
        """
        self._desktop_type = desktop_type

    @property
    def login_status(self):
        """Gets the login_status of this ListDesktopsDetailRequest.

        桌面的登录状态。  - UNREGISTER：表示桌面未注册时的状态（桌面启动后，会自动注册）。关机后也会出现未注册的状态。 - REGISTERED：表示桌面注册以后，等待用户连接的状态。 - CONNECTED：表示用户已经成功登录，正在使用桌面。 - DISCONNECTED：表示桌面与客户端断开会话后显示的状态，可能为关闭客户端窗口，或客户端与桌面网络断开引起。

        :return: The login_status of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._login_status

    @login_status.setter
    def login_status(self, login_status):
        """Sets the login_status of this ListDesktopsDetailRequest.

        桌面的登录状态。  - UNREGISTER：表示桌面未注册时的状态（桌面启动后，会自动注册）。关机后也会出现未注册的状态。 - REGISTERED：表示桌面注册以后，等待用户连接的状态。 - CONNECTED：表示用户已经成功登录，正在使用桌面。 - DISCONNECTED：表示桌面与客户端断开会话后显示的状态，可能为关闭客户端窗口，或客户端与桌面网络断开引起。

        :param login_status: The login_status of this ListDesktopsDetailRequest.
        :type login_status: str
        """
        self._login_status = login_status

    @property
    def tag(self):
        """Gets the tag of this ListDesktopsDetailRequest.

        桌面的标签。样例：  - key1=value1。 - key1=value1，key2=value2。

        :return: The tag of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListDesktopsDetailRequest.

        桌面的标签。样例：  - key1=value1。 - key1=value1，key2=value2。

        :param tag: The tag of this ListDesktopsDetailRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def fuzzy_query(self):
        """Gets the fuzzy_query of this ListDesktopsDetailRequest.

        是不是模糊用户查询。

        :return: The fuzzy_query of this ListDesktopsDetailRequest.
        :rtype: bool
        """
        return self._fuzzy_query

    @fuzzy_query.setter
    def fuzzy_query(self, fuzzy_query):
        """Sets the fuzzy_query of this ListDesktopsDetailRequest.

        是不是模糊用户查询。

        :param fuzzy_query: The fuzzy_query of this ListDesktopsDetailRequest.
        :type fuzzy_query: bool
        """
        self._fuzzy_query = fuzzy_query

    @property
    def pool_id(self):
        """Gets the pool_id of this ListDesktopsDetailRequest.

        桌面池ID,多个桌面池ID用逗号隔开。

        :return: The pool_id of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this ListDesktopsDetailRequest.

        桌面池ID,多个桌面池ID用逗号隔开。

        :param pool_id: The pool_id of this ListDesktopsDetailRequest.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def user_attached(self):
        """Gets the user_attached of this ListDesktopsDetailRequest.

        是否分配了用户。

        :return: The user_attached of this ListDesktopsDetailRequest.
        :rtype: bool
        """
        return self._user_attached

    @user_attached.setter
    def user_attached(self, user_attached):
        """Sets the user_attached of this ListDesktopsDetailRequest.

        是否分配了用户。

        :param user_attached: The user_attached of this ListDesktopsDetailRequest.
        :type user_attached: bool
        """
        self._user_attached = user_attached

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListDesktopsDetailRequest.

        企业项目ID

        :return: The enterprise_project_id of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListDesktopsDetailRequest.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ListDesktopsDetailRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def image_id(self):
        """Gets the image_id of this ListDesktopsDetailRequest.

        镜像ID

        :return: The image_id of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ListDesktopsDetailRequest.

        镜像ID

        :param image_id: The image_id of this ListDesktopsDetailRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ListDesktopsDetailRequest.

        计费模式，0：包周期，1：按需。

        :return: The charge_mode of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ListDesktopsDetailRequest.

        计费模式，0：包周期，1：按需。

        :param charge_mode: The charge_mode of this ListDesktopsDetailRequest.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def in_maintenance_mode(self):
        """Gets the in_maintenance_mode of this ListDesktopsDetailRequest.

        按照维护模式过滤

        :return: The in_maintenance_mode of this ListDesktopsDetailRequest.
        :rtype: bool
        """
        return self._in_maintenance_mode

    @in_maintenance_mode.setter
    def in_maintenance_mode(self, in_maintenance_mode):
        """Sets the in_maintenance_mode of this ListDesktopsDetailRequest.

        按照维护模式过滤

        :param in_maintenance_mode: The in_maintenance_mode of this ListDesktopsDetailRequest.
        :type in_maintenance_mode: bool
        """
        self._in_maintenance_mode = in_maintenance_mode

    @property
    def is_share_desktop(self):
        """Gets the is_share_desktop of this ListDesktopsDetailRequest.

        是否为协同桌面

        :return: The is_share_desktop of this ListDesktopsDetailRequest.
        :rtype: bool
        """
        return self._is_share_desktop

    @is_share_desktop.setter
    def is_share_desktop(self, is_share_desktop):
        """Sets the is_share_desktop of this ListDesktopsDetailRequest.

        是否为协同桌面

        :param is_share_desktop: The is_share_desktop of this ListDesktopsDetailRequest.
        :type is_share_desktop: bool
        """
        self._is_share_desktop = is_share_desktop

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ListDesktopsDetailRequest.

        桌面的子网ID。

        :return: The subnet_id of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ListDesktopsDetailRequest.

        桌面的子网ID。

        :param subnet_id: The subnet_id of this ListDesktopsDetailRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def is_support_internet(self):
        """Gets the is_support_internet of this ListDesktopsDetailRequest.

        是否支持上网。

        :return: The is_support_internet of this ListDesktopsDetailRequest.
        :rtype: bool
        """
        return self._is_support_internet

    @is_support_internet.setter
    def is_support_internet(self, is_support_internet):
        """Sets the is_support_internet of this ListDesktopsDetailRequest.

        是否支持上网。

        :param is_support_internet: The is_support_internet of this ListDesktopsDetailRequest.
        :type is_support_internet: bool
        """
        self._is_support_internet = is_support_internet

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ListDesktopsDetailRequest.

        查询可用区

        :return: The availability_zone of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ListDesktopsDetailRequest.

        查询可用区

        :param availability_zone: The availability_zone of this ListDesktopsDetailRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

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
        if not isinstance(other, ListDesktopsDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
