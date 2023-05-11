# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDeviceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permissions': 'list[str]',
        'id': 'int',
        'device_id': 'int',
        'parent_device_id': 'int',
        'parent_device_name': 'str',
        'product': 'ProductReferer',
        'device_name': 'str',
        'instance_id': 'str',
        'client_id': 'str',
        'node_id': 'str',
        'app_name': 'str',
        'status': 'int',
        'online_status': 'int',
        'description': 'str',
        'authentication': 'Authentication',
        'created_user': 'CreatedUser',
        'last_updated_user': 'LastUpdatedUser',
        'tags': 'list[str]',
        'created_datetime': 'int',
        'last_updated_datetime': 'int',
        'connect_address': 'str',
        'ssl_connect_address': 'str',
        'ipv6_connect_address': 'str',
        'ipv6_ssl_connect_address': 'str',
        'last_login_datetime': 'int',
        'node_type': 'int',
        'device_type': 'int',
        'client_ip': 'str',
        'keep_alive': 'str',
        'last_active_time': 'int',
        'version': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'permissions': 'permissions',
        'id': 'id',
        'device_id': 'device_id',
        'parent_device_id': 'parent_device_id',
        'parent_device_name': 'parent_device_name',
        'product': 'product',
        'device_name': 'device_name',
        'instance_id': 'instance_id',
        'client_id': 'client_id',
        'node_id': 'node_id',
        'app_name': 'app_name',
        'status': 'status',
        'online_status': 'online_status',
        'description': 'description',
        'authentication': 'authentication',
        'created_user': 'created_user',
        'last_updated_user': 'last_updated_user',
        'tags': 'tags',
        'created_datetime': 'created_datetime',
        'last_updated_datetime': 'last_updated_datetime',
        'connect_address': 'connect_address',
        'ssl_connect_address': 'ssl_connect_address',
        'ipv6_connect_address': 'ipv6_connect_address',
        'ipv6_ssl_connect_address': 'ipv6_ssl_connect_address',
        'last_login_datetime': 'last_login_datetime',
        'node_type': 'node_type',
        'device_type': 'device_type',
        'client_ip': 'client_ip',
        'keep_alive': 'keep_alive',
        'last_active_time': 'last_active_time',
        'version': 'version',
        'app_id': 'app_id'
    }

    def __init__(self, permissions=None, id=None, device_id=None, parent_device_id=None, parent_device_name=None, product=None, device_name=None, instance_id=None, client_id=None, node_id=None, app_name=None, status=None, online_status=None, description=None, authentication=None, created_user=None, last_updated_user=None, tags=None, created_datetime=None, last_updated_datetime=None, connect_address=None, ssl_connect_address=None, ipv6_connect_address=None, ipv6_ssl_connect_address=None, last_login_datetime=None, node_type=None, device_type=None, client_ip=None, keep_alive=None, last_active_time=None, version=None, app_id=None):
        """UpdateDeviceResponse

        The model defined in huaweicloud sdk

        :param permissions: 权限
        :type permissions: list[str]
        :param id: 设备ID
        :type id: int
        :param device_id: 设备ID（兼容20.0）
        :type device_id: int
        :param parent_device_id: 父设备ID
        :type parent_device_id: int
        :param parent_device_name: 父设备名称
        :type parent_device_name: str
        :param product: 
        :type product: :class:`huaweicloudsdkroma.v2.ProductReferer`
        :param device_name: 设备名称，支持中文、中文标点符号（）。；，：“”、？《》及英文大小写、数字及英文符号()_,#.?&#39;-@%&amp;!, 长度2-64
        :type device_name: str
        :param instance_id: 实例id
        :type instance_id: str
        :param client_id: 设备客户端ID，平台生成的设备唯一标识
        :type client_id: str
        :param node_id: 设备物理编号，通常使用MAC或者IMEI号，支持英文大小写，数字，下划线和中划线，长度2-64
        :type node_id: str
        :param app_name: 应用名称
        :type app_name: str
        :param status: 设备状态 0-启用 1-禁用
        :type status: int
        :param online_status: 是否在线 0-未连接 1-在线 2-离线
        :type online_status: int
        :param description: 备注
        :type description: str
        :param authentication: 
        :type authentication: :class:`huaweicloudsdkroma.v2.Authentication`
        :param created_user: 
        :type created_user: :class:`huaweicloudsdkroma.v2.CreatedUser`
        :param last_updated_user: 
        :type last_updated_user: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        :param tags: 标签
        :type tags: list[str]
        :param created_datetime: 创建时间，timestamp(ms)，使用UTC时区
        :type created_datetime: int
        :param last_updated_datetime: 最后修改时间，timestamp(ms)，使用UTC时区
        :type last_updated_datetime: int
        :param connect_address: 设备接入地址
        :type connect_address: str
        :param ssl_connect_address: 设备接入SSL地址
        :type ssl_connect_address: str
        :param ipv6_connect_address: 设备接入IPV6地址
        :type ipv6_connect_address: str
        :param ipv6_ssl_connect_address: 设备接入IPV6 SSL地址
        :type ipv6_ssl_connect_address: str
        :param last_login_datetime: 最后登录时间
        :type last_login_datetime: int
        :param node_type: 节点类型 0-直连 1-网关 2-子设备
        :type node_type: int
        :param device_type: 设备类型&lt;br&gt;0-普通设备（无子设备也无父设备）&lt;br&gt;1-网关设备(可挂载子设备)&lt;br&gt;2-子设备(归属于某个网关设备)
        :type device_type: int
        :param client_ip: 客户端ip
        :type client_ip: str
        :param keep_alive: 心跳时间
        :type keep_alive: str
        :param last_active_time: 最后登录时间
        :type last_active_time: int
        :param version: 设备版本
        :type version: str
        :param app_id: 应用ID
        :type app_id: str
        """
        
        super(UpdateDeviceResponse, self).__init__()

        self._permissions = None
        self._id = None
        self._device_id = None
        self._parent_device_id = None
        self._parent_device_name = None
        self._product = None
        self._device_name = None
        self._instance_id = None
        self._client_id = None
        self._node_id = None
        self._app_name = None
        self._status = None
        self._online_status = None
        self._description = None
        self._authentication = None
        self._created_user = None
        self._last_updated_user = None
        self._tags = None
        self._created_datetime = None
        self._last_updated_datetime = None
        self._connect_address = None
        self._ssl_connect_address = None
        self._ipv6_connect_address = None
        self._ipv6_ssl_connect_address = None
        self._last_login_datetime = None
        self._node_type = None
        self._device_type = None
        self._client_ip = None
        self._keep_alive = None
        self._last_active_time = None
        self._version = None
        self._app_id = None
        self.discriminator = None

        if permissions is not None:
            self.permissions = permissions
        if id is not None:
            self.id = id
        if device_id is not None:
            self.device_id = device_id
        if parent_device_id is not None:
            self.parent_device_id = parent_device_id
        if parent_device_name is not None:
            self.parent_device_name = parent_device_name
        if product is not None:
            self.product = product
        if device_name is not None:
            self.device_name = device_name
        if instance_id is not None:
            self.instance_id = instance_id
        if client_id is not None:
            self.client_id = client_id
        if node_id is not None:
            self.node_id = node_id
        if app_name is not None:
            self.app_name = app_name
        if status is not None:
            self.status = status
        if online_status is not None:
            self.online_status = online_status
        if description is not None:
            self.description = description
        if authentication is not None:
            self.authentication = authentication
        if created_user is not None:
            self.created_user = created_user
        if last_updated_user is not None:
            self.last_updated_user = last_updated_user
        if tags is not None:
            self.tags = tags
        if created_datetime is not None:
            self.created_datetime = created_datetime
        if last_updated_datetime is not None:
            self.last_updated_datetime = last_updated_datetime
        if connect_address is not None:
            self.connect_address = connect_address
        if ssl_connect_address is not None:
            self.ssl_connect_address = ssl_connect_address
        if ipv6_connect_address is not None:
            self.ipv6_connect_address = ipv6_connect_address
        if ipv6_ssl_connect_address is not None:
            self.ipv6_ssl_connect_address = ipv6_ssl_connect_address
        if last_login_datetime is not None:
            self.last_login_datetime = last_login_datetime
        if node_type is not None:
            self.node_type = node_type
        if device_type is not None:
            self.device_type = device_type
        if client_ip is not None:
            self.client_ip = client_ip
        if keep_alive is not None:
            self.keep_alive = keep_alive
        if last_active_time is not None:
            self.last_active_time = last_active_time
        if version is not None:
            self.version = version
        if app_id is not None:
            self.app_id = app_id

    @property
    def permissions(self):
        """Gets the permissions of this UpdateDeviceResponse.

        权限

        :return: The permissions of this UpdateDeviceResponse.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this UpdateDeviceResponse.

        权限

        :param permissions: The permissions of this UpdateDeviceResponse.
        :type permissions: list[str]
        """
        self._permissions = permissions

    @property
    def id(self):
        """Gets the id of this UpdateDeviceResponse.

        设备ID

        :return: The id of this UpdateDeviceResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateDeviceResponse.

        设备ID

        :param id: The id of this UpdateDeviceResponse.
        :type id: int
        """
        self._id = id

    @property
    def device_id(self):
        """Gets the device_id of this UpdateDeviceResponse.

        设备ID（兼容20.0）

        :return: The device_id of this UpdateDeviceResponse.
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this UpdateDeviceResponse.

        设备ID（兼容20.0）

        :param device_id: The device_id of this UpdateDeviceResponse.
        :type device_id: int
        """
        self._device_id = device_id

    @property
    def parent_device_id(self):
        """Gets the parent_device_id of this UpdateDeviceResponse.

        父设备ID

        :return: The parent_device_id of this UpdateDeviceResponse.
        :rtype: int
        """
        return self._parent_device_id

    @parent_device_id.setter
    def parent_device_id(self, parent_device_id):
        """Sets the parent_device_id of this UpdateDeviceResponse.

        父设备ID

        :param parent_device_id: The parent_device_id of this UpdateDeviceResponse.
        :type parent_device_id: int
        """
        self._parent_device_id = parent_device_id

    @property
    def parent_device_name(self):
        """Gets the parent_device_name of this UpdateDeviceResponse.

        父设备名称

        :return: The parent_device_name of this UpdateDeviceResponse.
        :rtype: str
        """
        return self._parent_device_name

    @parent_device_name.setter
    def parent_device_name(self, parent_device_name):
        """Sets the parent_device_name of this UpdateDeviceResponse.

        父设备名称

        :param parent_device_name: The parent_device_name of this UpdateDeviceResponse.
        :type parent_device_name: str
        """
        self._parent_device_name = parent_device_name

    @property
    def product(self):
        """Gets the product of this UpdateDeviceResponse.

        :return: The product of this UpdateDeviceResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.ProductReferer`
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this UpdateDeviceResponse.

        :param product: The product of this UpdateDeviceResponse.
        :type product: :class:`huaweicloudsdkroma.v2.ProductReferer`
        """
        self._product = product

    @property
    def device_name(self):
        """Gets the device_name of this UpdateDeviceResponse.

        设备名称，支持中文、中文标点符号（）。；，：“”、？《》及英文大小写、数字及英文符号()_,#.?'-@%&!, 长度2-64

        :return: The device_name of this UpdateDeviceResponse.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this UpdateDeviceResponse.

        设备名称，支持中文、中文标点符号（）。；，：“”、？《》及英文大小写、数字及英文符号()_,#.?'-@%&!, 长度2-64

        :param device_name: The device_name of this UpdateDeviceResponse.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def instance_id(self):
        """Gets the instance_id of this UpdateDeviceResponse.

        实例id

        :return: The instance_id of this UpdateDeviceResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UpdateDeviceResponse.

        实例id

        :param instance_id: The instance_id of this UpdateDeviceResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def client_id(self):
        """Gets the client_id of this UpdateDeviceResponse.

        设备客户端ID，平台生成的设备唯一标识

        :return: The client_id of this UpdateDeviceResponse.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this UpdateDeviceResponse.

        设备客户端ID，平台生成的设备唯一标识

        :param client_id: The client_id of this UpdateDeviceResponse.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def node_id(self):
        """Gets the node_id of this UpdateDeviceResponse.

        设备物理编号，通常使用MAC或者IMEI号，支持英文大小写，数字，下划线和中划线，长度2-64

        :return: The node_id of this UpdateDeviceResponse.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this UpdateDeviceResponse.

        设备物理编号，通常使用MAC或者IMEI号，支持英文大小写，数字，下划线和中划线，长度2-64

        :param node_id: The node_id of this UpdateDeviceResponse.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def app_name(self):
        """Gets the app_name of this UpdateDeviceResponse.

        应用名称

        :return: The app_name of this UpdateDeviceResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this UpdateDeviceResponse.

        应用名称

        :param app_name: The app_name of this UpdateDeviceResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def status(self):
        """Gets the status of this UpdateDeviceResponse.

        设备状态 0-启用 1-禁用

        :return: The status of this UpdateDeviceResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateDeviceResponse.

        设备状态 0-启用 1-禁用

        :param status: The status of this UpdateDeviceResponse.
        :type status: int
        """
        self._status = status

    @property
    def online_status(self):
        """Gets the online_status of this UpdateDeviceResponse.

        是否在线 0-未连接 1-在线 2-离线

        :return: The online_status of this UpdateDeviceResponse.
        :rtype: int
        """
        return self._online_status

    @online_status.setter
    def online_status(self, online_status):
        """Sets the online_status of this UpdateDeviceResponse.

        是否在线 0-未连接 1-在线 2-离线

        :param online_status: The online_status of this UpdateDeviceResponse.
        :type online_status: int
        """
        self._online_status = online_status

    @property
    def description(self):
        """Gets the description of this UpdateDeviceResponse.

        备注

        :return: The description of this UpdateDeviceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateDeviceResponse.

        备注

        :param description: The description of this UpdateDeviceResponse.
        :type description: str
        """
        self._description = description

    @property
    def authentication(self):
        """Gets the authentication of this UpdateDeviceResponse.

        :return: The authentication of this UpdateDeviceResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.Authentication`
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this UpdateDeviceResponse.

        :param authentication: The authentication of this UpdateDeviceResponse.
        :type authentication: :class:`huaweicloudsdkroma.v2.Authentication`
        """
        self._authentication = authentication

    @property
    def created_user(self):
        """Gets the created_user of this UpdateDeviceResponse.

        :return: The created_user of this UpdateDeviceResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.CreatedUser`
        """
        return self._created_user

    @created_user.setter
    def created_user(self, created_user):
        """Sets the created_user of this UpdateDeviceResponse.

        :param created_user: The created_user of this UpdateDeviceResponse.
        :type created_user: :class:`huaweicloudsdkroma.v2.CreatedUser`
        """
        self._created_user = created_user

    @property
    def last_updated_user(self):
        """Gets the last_updated_user of this UpdateDeviceResponse.

        :return: The last_updated_user of this UpdateDeviceResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        """
        return self._last_updated_user

    @last_updated_user.setter
    def last_updated_user(self, last_updated_user):
        """Sets the last_updated_user of this UpdateDeviceResponse.

        :param last_updated_user: The last_updated_user of this UpdateDeviceResponse.
        :type last_updated_user: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        """
        self._last_updated_user = last_updated_user

    @property
    def tags(self):
        """Gets the tags of this UpdateDeviceResponse.

        标签

        :return: The tags of this UpdateDeviceResponse.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateDeviceResponse.

        标签

        :param tags: The tags of this UpdateDeviceResponse.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def created_datetime(self):
        """Gets the created_datetime of this UpdateDeviceResponse.

        创建时间，timestamp(ms)，使用UTC时区

        :return: The created_datetime of this UpdateDeviceResponse.
        :rtype: int
        """
        return self._created_datetime

    @created_datetime.setter
    def created_datetime(self, created_datetime):
        """Sets the created_datetime of this UpdateDeviceResponse.

        创建时间，timestamp(ms)，使用UTC时区

        :param created_datetime: The created_datetime of this UpdateDeviceResponse.
        :type created_datetime: int
        """
        self._created_datetime = created_datetime

    @property
    def last_updated_datetime(self):
        """Gets the last_updated_datetime of this UpdateDeviceResponse.

        最后修改时间，timestamp(ms)，使用UTC时区

        :return: The last_updated_datetime of this UpdateDeviceResponse.
        :rtype: int
        """
        return self._last_updated_datetime

    @last_updated_datetime.setter
    def last_updated_datetime(self, last_updated_datetime):
        """Sets the last_updated_datetime of this UpdateDeviceResponse.

        最后修改时间，timestamp(ms)，使用UTC时区

        :param last_updated_datetime: The last_updated_datetime of this UpdateDeviceResponse.
        :type last_updated_datetime: int
        """
        self._last_updated_datetime = last_updated_datetime

    @property
    def connect_address(self):
        """Gets the connect_address of this UpdateDeviceResponse.

        设备接入地址

        :return: The connect_address of this UpdateDeviceResponse.
        :rtype: str
        """
        return self._connect_address

    @connect_address.setter
    def connect_address(self, connect_address):
        """Sets the connect_address of this UpdateDeviceResponse.

        设备接入地址

        :param connect_address: The connect_address of this UpdateDeviceResponse.
        :type connect_address: str
        """
        self._connect_address = connect_address

    @property
    def ssl_connect_address(self):
        """Gets the ssl_connect_address of this UpdateDeviceResponse.

        设备接入SSL地址

        :return: The ssl_connect_address of this UpdateDeviceResponse.
        :rtype: str
        """
        return self._ssl_connect_address

    @ssl_connect_address.setter
    def ssl_connect_address(self, ssl_connect_address):
        """Sets the ssl_connect_address of this UpdateDeviceResponse.

        设备接入SSL地址

        :param ssl_connect_address: The ssl_connect_address of this UpdateDeviceResponse.
        :type ssl_connect_address: str
        """
        self._ssl_connect_address = ssl_connect_address

    @property
    def ipv6_connect_address(self):
        """Gets the ipv6_connect_address of this UpdateDeviceResponse.

        设备接入IPV6地址

        :return: The ipv6_connect_address of this UpdateDeviceResponse.
        :rtype: str
        """
        return self._ipv6_connect_address

    @ipv6_connect_address.setter
    def ipv6_connect_address(self, ipv6_connect_address):
        """Sets the ipv6_connect_address of this UpdateDeviceResponse.

        设备接入IPV6地址

        :param ipv6_connect_address: The ipv6_connect_address of this UpdateDeviceResponse.
        :type ipv6_connect_address: str
        """
        self._ipv6_connect_address = ipv6_connect_address

    @property
    def ipv6_ssl_connect_address(self):
        """Gets the ipv6_ssl_connect_address of this UpdateDeviceResponse.

        设备接入IPV6 SSL地址

        :return: The ipv6_ssl_connect_address of this UpdateDeviceResponse.
        :rtype: str
        """
        return self._ipv6_ssl_connect_address

    @ipv6_ssl_connect_address.setter
    def ipv6_ssl_connect_address(self, ipv6_ssl_connect_address):
        """Sets the ipv6_ssl_connect_address of this UpdateDeviceResponse.

        设备接入IPV6 SSL地址

        :param ipv6_ssl_connect_address: The ipv6_ssl_connect_address of this UpdateDeviceResponse.
        :type ipv6_ssl_connect_address: str
        """
        self._ipv6_ssl_connect_address = ipv6_ssl_connect_address

    @property
    def last_login_datetime(self):
        """Gets the last_login_datetime of this UpdateDeviceResponse.

        最后登录时间

        :return: The last_login_datetime of this UpdateDeviceResponse.
        :rtype: int
        """
        return self._last_login_datetime

    @last_login_datetime.setter
    def last_login_datetime(self, last_login_datetime):
        """Sets the last_login_datetime of this UpdateDeviceResponse.

        最后登录时间

        :param last_login_datetime: The last_login_datetime of this UpdateDeviceResponse.
        :type last_login_datetime: int
        """
        self._last_login_datetime = last_login_datetime

    @property
    def node_type(self):
        """Gets the node_type of this UpdateDeviceResponse.

        节点类型 0-直连 1-网关 2-子设备

        :return: The node_type of this UpdateDeviceResponse.
        :rtype: int
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this UpdateDeviceResponse.

        节点类型 0-直连 1-网关 2-子设备

        :param node_type: The node_type of this UpdateDeviceResponse.
        :type node_type: int
        """
        self._node_type = node_type

    @property
    def device_type(self):
        """Gets the device_type of this UpdateDeviceResponse.

        设备类型<br>0-普通设备（无子设备也无父设备）<br>1-网关设备(可挂载子设备)<br>2-子设备(归属于某个网关设备)

        :return: The device_type of this UpdateDeviceResponse.
        :rtype: int
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this UpdateDeviceResponse.

        设备类型<br>0-普通设备（无子设备也无父设备）<br>1-网关设备(可挂载子设备)<br>2-子设备(归属于某个网关设备)

        :param device_type: The device_type of this UpdateDeviceResponse.
        :type device_type: int
        """
        self._device_type = device_type

    @property
    def client_ip(self):
        """Gets the client_ip of this UpdateDeviceResponse.

        客户端ip

        :return: The client_ip of this UpdateDeviceResponse.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this UpdateDeviceResponse.

        客户端ip

        :param client_ip: The client_ip of this UpdateDeviceResponse.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def keep_alive(self):
        """Gets the keep_alive of this UpdateDeviceResponse.

        心跳时间

        :return: The keep_alive of this UpdateDeviceResponse.
        :rtype: str
        """
        return self._keep_alive

    @keep_alive.setter
    def keep_alive(self, keep_alive):
        """Sets the keep_alive of this UpdateDeviceResponse.

        心跳时间

        :param keep_alive: The keep_alive of this UpdateDeviceResponse.
        :type keep_alive: str
        """
        self._keep_alive = keep_alive

    @property
    def last_active_time(self):
        """Gets the last_active_time of this UpdateDeviceResponse.

        最后登录时间

        :return: The last_active_time of this UpdateDeviceResponse.
        :rtype: int
        """
        return self._last_active_time

    @last_active_time.setter
    def last_active_time(self, last_active_time):
        """Sets the last_active_time of this UpdateDeviceResponse.

        最后登录时间

        :param last_active_time: The last_active_time of this UpdateDeviceResponse.
        :type last_active_time: int
        """
        self._last_active_time = last_active_time

    @property
    def version(self):
        """Gets the version of this UpdateDeviceResponse.

        设备版本

        :return: The version of this UpdateDeviceResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpdateDeviceResponse.

        设备版本

        :param version: The version of this UpdateDeviceResponse.
        :type version: str
        """
        self._version = version

    @property
    def app_id(self):
        """Gets the app_id of this UpdateDeviceResponse.

        应用ID

        :return: The app_id of this UpdateDeviceResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this UpdateDeviceResponse.

        应用ID

        :param app_id: The app_id of this UpdateDeviceResponse.
        :type app_id: str
        """
        self._app_id = app_id

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
        if not isinstance(other, UpdateDeviceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
