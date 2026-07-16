# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDevServerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_at': 'int',
        'update_at': 'int',
        'charging_mode': 'str',
        'cloud_server': 'CloudServer',
        'endpoints_response': 'list[Endpoints]',
        'flavor': 'str',
        'id': 'str',
        'key_pair_name': 'str',
        'name': 'str',
        'order_id': 'str',
        'status': 'str',
        'vpc_id': 'str',
        'endpoints': 'list[EndpointsRes]',
        'volumes': 'list[ServerVolume]',
        'image': 'ServerImageResponse',
        'category': 'str',
        'server_hps': 'ServerHpsInfo',
        'subnet_id': 'str'
    }

    attribute_map = {
        'create_at': 'create_at',
        'update_at': 'update_at',
        'charging_mode': 'charging_mode',
        'cloud_server': 'cloud_server',
        'endpoints_response': 'endpoints_response',
        'flavor': 'flavor',
        'id': 'id',
        'key_pair_name': 'key_pair_name',
        'name': 'name',
        'order_id': 'order_id',
        'status': 'status',
        'vpc_id': 'vpc_id',
        'endpoints': 'endpoints',
        'volumes': 'volumes',
        'image': 'image',
        'category': 'category',
        'server_hps': 'server_hps',
        'subnet_id': 'subnet_id'
    }

    def __init__(self, create_at=None, update_at=None, charging_mode=None, cloud_server=None, endpoints_response=None, flavor=None, id=None, key_pair_name=None, name=None, order_id=None, status=None, vpc_id=None, endpoints=None, volumes=None, image=None, category=None, server_hps=None, subnet_id=None):
        r"""CreateDevServerResponse

        The model defined in huaweicloud sdk

        :param create_at: **参数解释**：创建时间。 **取值范围**：不涉及。
        :type create_at: int
        :param update_at: **参数解释**：更新时间。 **取值范围**：不涉及。
        :type update_at: int
        :param charging_mode: **参数解释**：计费模式。 **取值范围**： - [COMMON：同时支持包周期和按需](tag:hws,hws_hk) - POST_PAID：按需模式 - [PRE_PAID：包周期](tag:hws,hws_hk)
        :type charging_mode: str
        :param cloud_server: 
        :type cloud_server: :class:`huaweicloudsdkmodelarts.v1.CloudServer`
        :param endpoints_response: **参数解释**：实例私有IP信息。
        :type endpoints_response: list[:class:`huaweicloudsdkmodelarts.v1.Endpoints`]
        :param flavor: **参数解释**：实例规格名称。 **取值范围**：^.{1,128}$。
        :type flavor: str
        :param id: **参数解释**：实例ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。
        :type id: str
        :param key_pair_name: **参数解释**：密钥对名称。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。
        :type key_pair_name: str
        :param name: **参数解释**：实例名称。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。
        :type name: str
        :param order_id: **参数解释**：订单ID。 **取值范围**：^[a-zA-Z0-9]{1,64}$。
        :type order_id: str
        :param status: **参数解释**：实例状态。表示实例的当前运行状态，用于监控实例的生命周期和健康状况。 **取值范围**： - CREATE_FAILED: 创建失败 - CREATING: 创建中 - DELETED: 已删除 - DELETE_FAILED: 删除失败 - DELETING: 删除中 - ERROR: 错误 - RUNNING: 运行中 - STARTING: 启动中 - START_FAILED: 启动失败 - STOPPED: 已停止 - STOPPING: 停止中 - STOP_FAILED: 停止失败 - REBOOTING: 重启中 - REBOOT_FAILED: 重启失败 - CHANGINGOS: 切换操作系统中 - CHANGINGOS_FAILED: 切换操作系统失败 - REINSTALLINGOS: 重装操作系统中 - REINSTALLINGOS_FAILED: 重装操作系统失败
        :type status: str
        :param vpc_id: **参数解释**：实例所在虚拟私有云ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。
        :type vpc_id: str
        :param endpoints: **参数解释**：服务器私有IP信息。
        :type endpoints: list[:class:`huaweicloudsdkmodelarts.v1.EndpointsRes`]
        :param volumes: **参数解释**：挂载硬盘信息。
        :type volumes: list[:class:`huaweicloudsdkmodelarts.v1.ServerVolume`]
        :param image: 
        :type image: :class:`huaweicloudsdkmodelarts.v1.ServerImageResponse`
        :param category: **参数解释**：服务器归属类型。 **取值范围**： - [HPS：超节点服务器](tag:hws,hws_hk) - [SPOD：整柜服务器](tag:hws,hws_hk) - [SERVER：单台服务器](tag:hws,hws_hk)
        :type category: str
        :param server_hps: 
        :type server_hps: :class:`huaweicloudsdkmodelarts.v1.ServerHpsInfo`
        :param subnet_id: **参数解释**：实例所在子网的ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。
        :type subnet_id: str
        """
        
        super().__init__()

        self._create_at = None
        self._update_at = None
        self._charging_mode = None
        self._cloud_server = None
        self._endpoints_response = None
        self._flavor = None
        self._id = None
        self._key_pair_name = None
        self._name = None
        self._order_id = None
        self._status = None
        self._vpc_id = None
        self._endpoints = None
        self._volumes = None
        self._image = None
        self._category = None
        self._server_hps = None
        self._subnet_id = None
        self.discriminator = None

        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if cloud_server is not None:
            self.cloud_server = cloud_server
        if endpoints_response is not None:
            self.endpoints_response = endpoints_response
        if flavor is not None:
            self.flavor = flavor
        if id is not None:
            self.id = id
        if key_pair_name is not None:
            self.key_pair_name = key_pair_name
        if name is not None:
            self.name = name
        if order_id is not None:
            self.order_id = order_id
        if status is not None:
            self.status = status
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if endpoints is not None:
            self.endpoints = endpoints
        if volumes is not None:
            self.volumes = volumes
        if image is not None:
            self.image = image
        if category is not None:
            self.category = category
        if server_hps is not None:
            self.server_hps = server_hps
        if subnet_id is not None:
            self.subnet_id = subnet_id

    @property
    def create_at(self):
        r"""Gets the create_at of this CreateDevServerResponse.

        **参数解释**：创建时间。 **取值范围**：不涉及。

        :return: The create_at of this CreateDevServerResponse.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this CreateDevServerResponse.

        **参数解释**：创建时间。 **取值范围**：不涉及。

        :param create_at: The create_at of this CreateDevServerResponse.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this CreateDevServerResponse.

        **参数解释**：更新时间。 **取值范围**：不涉及。

        :return: The update_at of this CreateDevServerResponse.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this CreateDevServerResponse.

        **参数解释**：更新时间。 **取值范围**：不涉及。

        :param update_at: The update_at of this CreateDevServerResponse.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this CreateDevServerResponse.

        **参数解释**：计费模式。 **取值范围**： - [COMMON：同时支持包周期和按需](tag:hws,hws_hk) - POST_PAID：按需模式 - [PRE_PAID：包周期](tag:hws,hws_hk)

        :return: The charging_mode of this CreateDevServerResponse.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this CreateDevServerResponse.

        **参数解释**：计费模式。 **取值范围**： - [COMMON：同时支持包周期和按需](tag:hws,hws_hk) - POST_PAID：按需模式 - [PRE_PAID：包周期](tag:hws,hws_hk)

        :param charging_mode: The charging_mode of this CreateDevServerResponse.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def cloud_server(self):
        r"""Gets the cloud_server of this CreateDevServerResponse.

        :return: The cloud_server of this CreateDevServerResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CloudServer`
        """
        return self._cloud_server

    @cloud_server.setter
    def cloud_server(self, cloud_server):
        r"""Sets the cloud_server of this CreateDevServerResponse.

        :param cloud_server: The cloud_server of this CreateDevServerResponse.
        :type cloud_server: :class:`huaweicloudsdkmodelarts.v1.CloudServer`
        """
        self._cloud_server = cloud_server

    @property
    def endpoints_response(self):
        r"""Gets the endpoints_response of this CreateDevServerResponse.

        **参数解释**：实例私有IP信息。

        :return: The endpoints_response of this CreateDevServerResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Endpoints`]
        """
        return self._endpoints_response

    @endpoints_response.setter
    def endpoints_response(self, endpoints_response):
        r"""Sets the endpoints_response of this CreateDevServerResponse.

        **参数解释**：实例私有IP信息。

        :param endpoints_response: The endpoints_response of this CreateDevServerResponse.
        :type endpoints_response: list[:class:`huaweicloudsdkmodelarts.v1.Endpoints`]
        """
        self._endpoints_response = endpoints_response

    @property
    def flavor(self):
        r"""Gets the flavor of this CreateDevServerResponse.

        **参数解释**：实例规格名称。 **取值范围**：^.{1,128}$。

        :return: The flavor of this CreateDevServerResponse.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this CreateDevServerResponse.

        **参数解释**：实例规格名称。 **取值范围**：^.{1,128}$。

        :param flavor: The flavor of this CreateDevServerResponse.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def id(self):
        r"""Gets the id of this CreateDevServerResponse.

        **参数解释**：实例ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :return: The id of this CreateDevServerResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateDevServerResponse.

        **参数解释**：实例ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :param id: The id of this CreateDevServerResponse.
        :type id: str
        """
        self._id = id

    @property
    def key_pair_name(self):
        r"""Gets the key_pair_name of this CreateDevServerResponse.

        **参数解释**：密钥对名称。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。

        :return: The key_pair_name of this CreateDevServerResponse.
        :rtype: str
        """
        return self._key_pair_name

    @key_pair_name.setter
    def key_pair_name(self, key_pair_name):
        r"""Sets the key_pair_name of this CreateDevServerResponse.

        **参数解释**：密钥对名称。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。

        :param key_pair_name: The key_pair_name of this CreateDevServerResponse.
        :type key_pair_name: str
        """
        self._key_pair_name = key_pair_name

    @property
    def name(self):
        r"""Gets the name of this CreateDevServerResponse.

        **参数解释**：实例名称。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。

        :return: The name of this CreateDevServerResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDevServerResponse.

        **参数解释**：实例名称。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。

        :param name: The name of this CreateDevServerResponse.
        :type name: str
        """
        self._name = name

    @property
    def order_id(self):
        r"""Gets the order_id of this CreateDevServerResponse.

        **参数解释**：订单ID。 **取值范围**：^[a-zA-Z0-9]{1,64}$。

        :return: The order_id of this CreateDevServerResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this CreateDevServerResponse.

        **参数解释**：订单ID。 **取值范围**：^[a-zA-Z0-9]{1,64}$。

        :param order_id: The order_id of this CreateDevServerResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def status(self):
        r"""Gets the status of this CreateDevServerResponse.

        **参数解释**：实例状态。表示实例的当前运行状态，用于监控实例的生命周期和健康状况。 **取值范围**： - CREATE_FAILED: 创建失败 - CREATING: 创建中 - DELETED: 已删除 - DELETE_FAILED: 删除失败 - DELETING: 删除中 - ERROR: 错误 - RUNNING: 运行中 - STARTING: 启动中 - START_FAILED: 启动失败 - STOPPED: 已停止 - STOPPING: 停止中 - STOP_FAILED: 停止失败 - REBOOTING: 重启中 - REBOOT_FAILED: 重启失败 - CHANGINGOS: 切换操作系统中 - CHANGINGOS_FAILED: 切换操作系统失败 - REINSTALLINGOS: 重装操作系统中 - REINSTALLINGOS_FAILED: 重装操作系统失败

        :return: The status of this CreateDevServerResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateDevServerResponse.

        **参数解释**：实例状态。表示实例的当前运行状态，用于监控实例的生命周期和健康状况。 **取值范围**： - CREATE_FAILED: 创建失败 - CREATING: 创建中 - DELETED: 已删除 - DELETE_FAILED: 删除失败 - DELETING: 删除中 - ERROR: 错误 - RUNNING: 运行中 - STARTING: 启动中 - START_FAILED: 启动失败 - STOPPED: 已停止 - STOPPING: 停止中 - STOP_FAILED: 停止失败 - REBOOTING: 重启中 - REBOOT_FAILED: 重启失败 - CHANGINGOS: 切换操作系统中 - CHANGINGOS_FAILED: 切换操作系统失败 - REINSTALLINGOS: 重装操作系统中 - REINSTALLINGOS_FAILED: 重装操作系统失败

        :param status: The status of this CreateDevServerResponse.
        :type status: str
        """
        self._status = status

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateDevServerResponse.

        **参数解释**：实例所在虚拟私有云ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :return: The vpc_id of this CreateDevServerResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateDevServerResponse.

        **参数解释**：实例所在虚拟私有云ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :param vpc_id: The vpc_id of this CreateDevServerResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def endpoints(self):
        r"""Gets the endpoints of this CreateDevServerResponse.

        **参数解释**：服务器私有IP信息。

        :return: The endpoints of this CreateDevServerResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.EndpointsRes`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this CreateDevServerResponse.

        **参数解释**：服务器私有IP信息。

        :param endpoints: The endpoints of this CreateDevServerResponse.
        :type endpoints: list[:class:`huaweicloudsdkmodelarts.v1.EndpointsRes`]
        """
        self._endpoints = endpoints

    @property
    def volumes(self):
        r"""Gets the volumes of this CreateDevServerResponse.

        **参数解释**：挂载硬盘信息。

        :return: The volumes of this CreateDevServerResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ServerVolume`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        r"""Sets the volumes of this CreateDevServerResponse.

        **参数解释**：挂载硬盘信息。

        :param volumes: The volumes of this CreateDevServerResponse.
        :type volumes: list[:class:`huaweicloudsdkmodelarts.v1.ServerVolume`]
        """
        self._volumes = volumes

    @property
    def image(self):
        r"""Gets the image of this CreateDevServerResponse.

        :return: The image of this CreateDevServerResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ServerImageResponse`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this CreateDevServerResponse.

        :param image: The image of this CreateDevServerResponse.
        :type image: :class:`huaweicloudsdkmodelarts.v1.ServerImageResponse`
        """
        self._image = image

    @property
    def category(self):
        r"""Gets the category of this CreateDevServerResponse.

        **参数解释**：服务器归属类型。 **取值范围**： - [HPS：超节点服务器](tag:hws,hws_hk) - [SPOD：整柜服务器](tag:hws,hws_hk) - [SERVER：单台服务器](tag:hws,hws_hk)

        :return: The category of this CreateDevServerResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateDevServerResponse.

        **参数解释**：服务器归属类型。 **取值范围**： - [HPS：超节点服务器](tag:hws,hws_hk) - [SPOD：整柜服务器](tag:hws,hws_hk) - [SERVER：单台服务器](tag:hws,hws_hk)

        :param category: The category of this CreateDevServerResponse.
        :type category: str
        """
        self._category = category

    @property
    def server_hps(self):
        r"""Gets the server_hps of this CreateDevServerResponse.

        :return: The server_hps of this CreateDevServerResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ServerHpsInfo`
        """
        return self._server_hps

    @server_hps.setter
    def server_hps(self, server_hps):
        r"""Sets the server_hps of this CreateDevServerResponse.

        :param server_hps: The server_hps of this CreateDevServerResponse.
        :type server_hps: :class:`huaweicloudsdkmodelarts.v1.ServerHpsInfo`
        """
        self._server_hps = server_hps

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateDevServerResponse.

        **参数解释**：实例所在子网的ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :return: The subnet_id of this CreateDevServerResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateDevServerResponse.

        **参数解释**：实例所在子网的ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :param subnet_id: The subnet_id of this CreateDevServerResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateDevServerResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateDevServerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
