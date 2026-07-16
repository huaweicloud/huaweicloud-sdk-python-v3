# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInferIntranetConnectionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'applicant_user_name': 'str',
        'id': 'str',
        'message': 'str',
        'owner_domain_name': 'str',
        'scene': 'str',
        'service_id': 'str',
        'service_name': 'str',
        'status': 'str',
        'subnet_id': 'str',
        'url_list': 'list[str]',
        'custom_url_list': 'list[str]',
        'vpc_id': 'str',
        'dispatcher_group_id': 'str',
        'type': 'str',
        'maos_network_name': 'str',
        'service_type': 'str',
        'pool_id': 'str',
        'create_at': 'str',
        'update_at': 'str'
    }

    attribute_map = {
        'applicant_user_name': 'applicant_user_name',
        'id': 'id',
        'message': 'message',
        'owner_domain_name': 'owner_domain_name',
        'scene': 'scene',
        'service_id': 'service_id',
        'service_name': 'service_name',
        'status': 'status',
        'subnet_id': 'subnet_id',
        'url_list': 'url_list',
        'custom_url_list': 'custom_url_list',
        'vpc_id': 'vpc_id',
        'dispatcher_group_id': 'dispatcher_group_id',
        'type': 'type',
        'maos_network_name': 'maos_network_name',
        'service_type': 'service_type',
        'pool_id': 'pool_id',
        'create_at': 'create_at',
        'update_at': 'update_at'
    }

    def __init__(self, applicant_user_name=None, id=None, message=None, owner_domain_name=None, scene=None, service_id=None, service_name=None, status=None, subnet_id=None, url_list=None, custom_url_list=None, vpc_id=None, dispatcher_group_id=None, type=None, maos_network_name=None, service_type=None, pool_id=None, create_at=None, update_at=None):
        r"""CreateInferIntranetConnectionResponse

        The model defined in huaweicloud sdk

        :param applicant_user_name: **参数解释：** 申请方用户名。 **取值范围：** 不涉及。
        :type applicant_user_name: str
        :param id: **参数解释：** 内网接入id。 **取值范围：** 不涉及。
        :type id: str
        :param message: **参数解释：** 申请描述。 **取值范围：** 不涉及。
        :type message: str
        :param owner_domain_name: **参数解释：** 审核方domain name。  **取值范围：** 不涉及。
        :type owner_domain_name: str
        :param scene: **参数解释：** 内网访问场景。 **约束限制：** 不涉及。 **取值范围：** - POOL：用户资源池接入场景 - VPC：用户VPC接入场景 **默认取值：** 不涉及。
        :type scene: str
        :param service_id: **参数解释：** 服务ID。 **取值范围：** 不涉及。
        :type service_id: str
        :param service_name: **参数解释：** 服务名。 **取值范围：** 不涉及。
        :type service_name: str
        :param status: **参数解释：** 内网接入状态，支持列表查询。 **约束限制：** 不涉及。 **取值范围：** - APPROVING：审批中 - REJECTED：拒绝 - CONNECTING：接入中 - CONNECTED：已接入 - CANCELED：已取消 - FAILED：失败 - DELETING：删除中 **默认取值：** 不涉及。
        :type status: str
        :param subnet_id: **参数解释：** 子网ID。 **取值范围：** 不涉及。
        :type subnet_id: str
        :param url_list: **参数解释：** 访问地址列表。
        :type url_list: list[str]
        :param custom_url_list: **参数解释：** 访问地址列表。
        :type custom_url_list: list[str]
        :param vpc_id: **参数解释：** VPC ID。 **取值范围：** 不涉及。
        :type vpc_id: str
        :param dispatcher_group_id: **参数解释：** 服务绑定的dispatcher组ID。 **取值范围：** 不涉及。
        :type dispatcher_group_id: str
        :param type: **参数解释：** 接入粒度：SERVICE、GLOBAL **取值范围：** 不涉及。
        :type type: str
        :param maos_network_name: **参数解释：** 资源池网络名称。 **取值范围：** 不涉及。
        :type maos_network_name: str
        :param service_type: **参数解释：** 服务类型。 **取值范围：** 不涉及。
        :type service_type: str
        :param pool_id: **参数解释：** 资源池ID。 **取值范围：** 不涉及。
        :type pool_id: str
        :param create_at: **参数解释：** 创建时间。 **取值范围：** 不涉及。
        :type create_at: str
        :param update_at: **参数解释：** 修改时间。 **取值范围：** 不涉及。
        :type update_at: str
        """
        
        super().__init__()

        self._applicant_user_name = None
        self._id = None
        self._message = None
        self._owner_domain_name = None
        self._scene = None
        self._service_id = None
        self._service_name = None
        self._status = None
        self._subnet_id = None
        self._url_list = None
        self._custom_url_list = None
        self._vpc_id = None
        self._dispatcher_group_id = None
        self._type = None
        self._maos_network_name = None
        self._service_type = None
        self._pool_id = None
        self._create_at = None
        self._update_at = None
        self.discriminator = None

        if applicant_user_name is not None:
            self.applicant_user_name = applicant_user_name
        if id is not None:
            self.id = id
        if message is not None:
            self.message = message
        if owner_domain_name is not None:
            self.owner_domain_name = owner_domain_name
        if scene is not None:
            self.scene = scene
        if service_id is not None:
            self.service_id = service_id
        if service_name is not None:
            self.service_name = service_name
        if status is not None:
            self.status = status
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if url_list is not None:
            self.url_list = url_list
        if custom_url_list is not None:
            self.custom_url_list = custom_url_list
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if dispatcher_group_id is not None:
            self.dispatcher_group_id = dispatcher_group_id
        if type is not None:
            self.type = type
        if maos_network_name is not None:
            self.maos_network_name = maos_network_name
        if service_type is not None:
            self.service_type = service_type
        if pool_id is not None:
            self.pool_id = pool_id
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at

    @property
    def applicant_user_name(self):
        r"""Gets the applicant_user_name of this CreateInferIntranetConnectionResponse.

        **参数解释：** 申请方用户名。 **取值范围：** 不涉及。

        :return: The applicant_user_name of this CreateInferIntranetConnectionResponse.
        :rtype: str
        """
        return self._applicant_user_name

    @applicant_user_name.setter
    def applicant_user_name(self, applicant_user_name):
        r"""Sets the applicant_user_name of this CreateInferIntranetConnectionResponse.

        **参数解释：** 申请方用户名。 **取值范围：** 不涉及。

        :param applicant_user_name: The applicant_user_name of this CreateInferIntranetConnectionResponse.
        :type applicant_user_name: str
        """
        self._applicant_user_name = applicant_user_name

    @property
    def id(self):
        r"""Gets the id of this CreateInferIntranetConnectionResponse.

        **参数解释：** 内网接入id。 **取值范围：** 不涉及。

        :return: The id of this CreateInferIntranetConnectionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateInferIntranetConnectionResponse.

        **参数解释：** 内网接入id。 **取值范围：** 不涉及。

        :param id: The id of this CreateInferIntranetConnectionResponse.
        :type id: str
        """
        self._id = id

    @property
    def message(self):
        r"""Gets the message of this CreateInferIntranetConnectionResponse.

        **参数解释：** 申请描述。 **取值范围：** 不涉及。

        :return: The message of this CreateInferIntranetConnectionResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreateInferIntranetConnectionResponse.

        **参数解释：** 申请描述。 **取值范围：** 不涉及。

        :param message: The message of this CreateInferIntranetConnectionResponse.
        :type message: str
        """
        self._message = message

    @property
    def owner_domain_name(self):
        r"""Gets the owner_domain_name of this CreateInferIntranetConnectionResponse.

        **参数解释：** 审核方domain name。  **取值范围：** 不涉及。

        :return: The owner_domain_name of this CreateInferIntranetConnectionResponse.
        :rtype: str
        """
        return self._owner_domain_name

    @owner_domain_name.setter
    def owner_domain_name(self, owner_domain_name):
        r"""Sets the owner_domain_name of this CreateInferIntranetConnectionResponse.

        **参数解释：** 审核方domain name。  **取值范围：** 不涉及。

        :param owner_domain_name: The owner_domain_name of this CreateInferIntranetConnectionResponse.
        :type owner_domain_name: str
        """
        self._owner_domain_name = owner_domain_name

    @property
    def scene(self):
        r"""Gets the scene of this CreateInferIntranetConnectionResponse.

        **参数解释：** 内网访问场景。 **约束限制：** 不涉及。 **取值范围：** - POOL：用户资源池接入场景 - VPC：用户VPC接入场景 **默认取值：** 不涉及。

        :return: The scene of this CreateInferIntranetConnectionResponse.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this CreateInferIntranetConnectionResponse.

        **参数解释：** 内网访问场景。 **约束限制：** 不涉及。 **取值范围：** - POOL：用户资源池接入场景 - VPC：用户VPC接入场景 **默认取值：** 不涉及。

        :param scene: The scene of this CreateInferIntranetConnectionResponse.
        :type scene: str
        """
        self._scene = scene

    @property
    def service_id(self):
        r"""Gets the service_id of this CreateInferIntranetConnectionResponse.

        **参数解释：** 服务ID。 **取值范围：** 不涉及。

        :return: The service_id of this CreateInferIntranetConnectionResponse.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this CreateInferIntranetConnectionResponse.

        **参数解释：** 服务ID。 **取值范围：** 不涉及。

        :param service_id: The service_id of this CreateInferIntranetConnectionResponse.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def service_name(self):
        r"""Gets the service_name of this CreateInferIntranetConnectionResponse.

        **参数解释：** 服务名。 **取值范围：** 不涉及。

        :return: The service_name of this CreateInferIntranetConnectionResponse.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this CreateInferIntranetConnectionResponse.

        **参数解释：** 服务名。 **取值范围：** 不涉及。

        :param service_name: The service_name of this CreateInferIntranetConnectionResponse.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def status(self):
        r"""Gets the status of this CreateInferIntranetConnectionResponse.

        **参数解释：** 内网接入状态，支持列表查询。 **约束限制：** 不涉及。 **取值范围：** - APPROVING：审批中 - REJECTED：拒绝 - CONNECTING：接入中 - CONNECTED：已接入 - CANCELED：已取消 - FAILED：失败 - DELETING：删除中 **默认取值：** 不涉及。

        :return: The status of this CreateInferIntranetConnectionResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateInferIntranetConnectionResponse.

        **参数解释：** 内网接入状态，支持列表查询。 **约束限制：** 不涉及。 **取值范围：** - APPROVING：审批中 - REJECTED：拒绝 - CONNECTING：接入中 - CONNECTED：已接入 - CANCELED：已取消 - FAILED：失败 - DELETING：删除中 **默认取值：** 不涉及。

        :param status: The status of this CreateInferIntranetConnectionResponse.
        :type status: str
        """
        self._status = status

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateInferIntranetConnectionResponse.

        **参数解释：** 子网ID。 **取值范围：** 不涉及。

        :return: The subnet_id of this CreateInferIntranetConnectionResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateInferIntranetConnectionResponse.

        **参数解释：** 子网ID。 **取值范围：** 不涉及。

        :param subnet_id: The subnet_id of this CreateInferIntranetConnectionResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def url_list(self):
        r"""Gets the url_list of this CreateInferIntranetConnectionResponse.

        **参数解释：** 访问地址列表。

        :return: The url_list of this CreateInferIntranetConnectionResponse.
        :rtype: list[str]
        """
        return self._url_list

    @url_list.setter
    def url_list(self, url_list):
        r"""Sets the url_list of this CreateInferIntranetConnectionResponse.

        **参数解释：** 访问地址列表。

        :param url_list: The url_list of this CreateInferIntranetConnectionResponse.
        :type url_list: list[str]
        """
        self._url_list = url_list

    @property
    def custom_url_list(self):
        r"""Gets the custom_url_list of this CreateInferIntranetConnectionResponse.

        **参数解释：** 访问地址列表。

        :return: The custom_url_list of this CreateInferIntranetConnectionResponse.
        :rtype: list[str]
        """
        return self._custom_url_list

    @custom_url_list.setter
    def custom_url_list(self, custom_url_list):
        r"""Sets the custom_url_list of this CreateInferIntranetConnectionResponse.

        **参数解释：** 访问地址列表。

        :param custom_url_list: The custom_url_list of this CreateInferIntranetConnectionResponse.
        :type custom_url_list: list[str]
        """
        self._custom_url_list = custom_url_list

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateInferIntranetConnectionResponse.

        **参数解释：** VPC ID。 **取值范围：** 不涉及。

        :return: The vpc_id of this CreateInferIntranetConnectionResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateInferIntranetConnectionResponse.

        **参数解释：** VPC ID。 **取值范围：** 不涉及。

        :param vpc_id: The vpc_id of this CreateInferIntranetConnectionResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def dispatcher_group_id(self):
        r"""Gets the dispatcher_group_id of this CreateInferIntranetConnectionResponse.

        **参数解释：** 服务绑定的dispatcher组ID。 **取值范围：** 不涉及。

        :return: The dispatcher_group_id of this CreateInferIntranetConnectionResponse.
        :rtype: str
        """
        return self._dispatcher_group_id

    @dispatcher_group_id.setter
    def dispatcher_group_id(self, dispatcher_group_id):
        r"""Sets the dispatcher_group_id of this CreateInferIntranetConnectionResponse.

        **参数解释：** 服务绑定的dispatcher组ID。 **取值范围：** 不涉及。

        :param dispatcher_group_id: The dispatcher_group_id of this CreateInferIntranetConnectionResponse.
        :type dispatcher_group_id: str
        """
        self._dispatcher_group_id = dispatcher_group_id

    @property
    def type(self):
        r"""Gets the type of this CreateInferIntranetConnectionResponse.

        **参数解释：** 接入粒度：SERVICE、GLOBAL **取值范围：** 不涉及。

        :return: The type of this CreateInferIntranetConnectionResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateInferIntranetConnectionResponse.

        **参数解释：** 接入粒度：SERVICE、GLOBAL **取值范围：** 不涉及。

        :param type: The type of this CreateInferIntranetConnectionResponse.
        :type type: str
        """
        self._type = type

    @property
    def maos_network_name(self):
        r"""Gets the maos_network_name of this CreateInferIntranetConnectionResponse.

        **参数解释：** 资源池网络名称。 **取值范围：** 不涉及。

        :return: The maos_network_name of this CreateInferIntranetConnectionResponse.
        :rtype: str
        """
        return self._maos_network_name

    @maos_network_name.setter
    def maos_network_name(self, maos_network_name):
        r"""Sets the maos_network_name of this CreateInferIntranetConnectionResponse.

        **参数解释：** 资源池网络名称。 **取值范围：** 不涉及。

        :param maos_network_name: The maos_network_name of this CreateInferIntranetConnectionResponse.
        :type maos_network_name: str
        """
        self._maos_network_name = maos_network_name

    @property
    def service_type(self):
        r"""Gets the service_type of this CreateInferIntranetConnectionResponse.

        **参数解释：** 服务类型。 **取值范围：** 不涉及。

        :return: The service_type of this CreateInferIntranetConnectionResponse.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this CreateInferIntranetConnectionResponse.

        **参数解释：** 服务类型。 **取值范围：** 不涉及。

        :param service_type: The service_type of this CreateInferIntranetConnectionResponse.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def pool_id(self):
        r"""Gets the pool_id of this CreateInferIntranetConnectionResponse.

        **参数解释：** 资源池ID。 **取值范围：** 不涉及。

        :return: The pool_id of this CreateInferIntranetConnectionResponse.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this CreateInferIntranetConnectionResponse.

        **参数解释：** 资源池ID。 **取值范围：** 不涉及。

        :param pool_id: The pool_id of this CreateInferIntranetConnectionResponse.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def create_at(self):
        r"""Gets the create_at of this CreateInferIntranetConnectionResponse.

        **参数解释：** 创建时间。 **取值范围：** 不涉及。

        :return: The create_at of this CreateInferIntranetConnectionResponse.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this CreateInferIntranetConnectionResponse.

        **参数解释：** 创建时间。 **取值范围：** 不涉及。

        :param create_at: The create_at of this CreateInferIntranetConnectionResponse.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this CreateInferIntranetConnectionResponse.

        **参数解释：** 修改时间。 **取值范围：** 不涉及。

        :return: The update_at of this CreateInferIntranetConnectionResponse.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this CreateInferIntranetConnectionResponse.

        **参数解释：** 修改时间。 **取值范围：** 不涉及。

        :param update_at: The update_at of this CreateInferIntranetConnectionResponse.
        :type update_at: str
        """
        self._update_at = update_at

    def to_dict(self):
        import warnings
        warnings.warn("CreateInferIntranetConnectionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateInferIntranetConnectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
